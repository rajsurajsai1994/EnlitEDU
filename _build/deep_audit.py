# -*- coding: utf-8 -*-
"""Deepest pre-launch pass: tag uniqueness and consistency, canonical/OG agreement, NAP consistency,
redirect chains/loops, dates, image weights, leftover dev references.  python _build/deep_audit.py"""
import os, re, json, glob, html, datetime, collections, sys

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, "_build")
BASE = "https://www.enlitedu.com"
TODAY = datetime.date.today()
pages = sorted(f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("assets", "_build", "google")))
P = collections.defaultdict(list)
one = lambda t, rx: re.findall(rx, t, re.S)

for f in pages:
    t = open(f, encoding="utf-8").read(); head = t.split("</head>")[0]
    url = BASE + "/" + ("" if f == "index.html" else f)
    noidx = "noindex" in re.search(r'<meta name="robots" content="([^"]*)"', head).group(1)
    # exactly one of each head tag
    for name, rx in [("title", r"<title>"), ("canonical", r'rel="canonical"'), ("description", r'name="description"'), ("robots", r'name="robots"'),
                     ("viewport", r'name="viewport"'), ("charset", r"<meta charset"), ("og:title", r'property="og:title"'), ("og:url", r'property="og:url"'),
                     ("og:image", r'property="og:image"'), ("twitter:card", r'name="twitter:card"'), ("h1", r"<h1[\s>]")]:
        n = len(re.findall(rx, head if name != "h1" else t))
        if n != 1: P[f].append("%s x%d" % (name, n))
    can = re.search(r'rel="canonical" href="([^"]+)"', head).group(1)
    if can != url: P[f].append("canonical %s != %s" % (can, url))
    if not can.startswith("https://www."): P[f].append("canonical not https://www")
    ogu = re.search(r'property="og:url" content="([^"]+)"', head).group(1)
    if ogu != can: P[f].append("og:url != canonical")
    ti = html.unescape(re.search(r"<title>(.*?)</title>", head).group(1)); ogt = html.unescape(re.search(r'property="og:title" content="([^"]*)"', head).group(1))
    if ti != ogt: P[f].append("og:title != title")
    d1 = html.unescape(re.search(r'name="description" content="([^"]*)"', head).group(1)); d2 = html.unescape(re.search(r'property="og:description" content="([^"]*)"', head).group(1))
    if d1 != d2: P[f].append("og:description != description")
    if not re.search(r'property="og:image" content="https://', head): P[f].append("og:image not absolute https")
    if '<html lang="en' not in t: P[f].append("lang")
    # leftovers from development
    for bad in ("localhost", "127.0.0.1", "file://", "vercel.app", "Lorem", "data-test", "console.log("):
        if bad in t and not (bad == "vercel.app" and f == "x"): P[f].append("leftover '%s'" % bad)
    # JSON-LD: one script, parseable, single FAQPage, dates sane, no duplicate @id
    blocks = one(t, r'<script type="application/ld\+json">(.*?)</script>')
    if len(blocks) != 1: P[f].append("JSON-LD blocks %d" % len(blocks))
    for b in blocks:
        g = json.loads(b)["@graph"]
        types = [n.get("@type") if isinstance(n.get("@type"), str) else n.get("@type")[0] for n in g]
        if types.count("FAQPage") > 1: P[f].append("multiple FAQPage")
        ids = [n["@id"] for n in g if "@id" in n]
        if len(ids) != len(set(ids)): P[f].append("duplicate @id in graph")
        for d in re.findall(r'"(?:datePublished|dateModified|uploadDate|datePosted)":"([0-9-]{10})', b):
            if datetime.date.fromisoformat(d) > TODAY: P[f].append("future date " + d)
        if not noidx and "BreadcrumbList" not in types and f != "index.html": P[f].append("no breadcrumb schema")
    # visible breadcrumb exists where schema breadcrumb exists (except home)
    if f != "index.html" and 'class="crumbs' not in t and 'aria-label="Breadcrumb"' not in t and not noidx: P[f].append("no visible breadcrumb")

# NAP (name, address, email) consistency
nap = collections.Counter()
for f in pages:
    t = open(f, encoding="utf-8").read()
    for m in re.findall(r"3840 Windermere Pkwy[^<\"]{0,60}", t): nap[re.sub(r"\s+", " ", html.unescape(m)).strip()[:45]] += 1
    for m in set(re.findall(r"[\w.+-]+@enlitedu\.com", t)): nap["email:" + m] += 1
print("NAP variants seen:", dict(nap))

# redirect chains / loops / targets
import deploy
exact = dict(deploy.EXACT)
for s, dst in exact.items():
    if dst in exact: P["redirects"].append("chain %s -> %s -> %s" % (s, dst, exact[dst]))
    if s == dst: P["redirects"].append("loop " + s)
    if not os.path.exists((dst.split("#")[0].lstrip("/") or "index.html")): P["redirects"].append("missing target " + dst)
sm = re.findall(r"<loc>([^<]+)</loc>", open("sitemap.xml", encoding="utf-8").read())
for u in sm:
    path = "/" + u[len(BASE) + 1:]
    if path in exact: P["sitemap.xml"].append("lists a redirected URL " + path)
    if not u.startswith(BASE + "/"): P["sitemap.xml"].append("bad host " + u)
v = json.load(open("vercel.json"))
print("vercel.json: %d redirects, %d header rules; robots.txt %d lines; sitemap %d URLs" % (len(v["redirects"]), len(v["headers"]), len(open("robots.txt").read().splitlines()), len(sm)))

# images: local file weights
big = [(os.path.getsize(p) // 1024, p.replace(os.sep, "/")) for p in glob.glob("assets/img/**/*.*", recursive=True) if os.path.getsize(p) > 400 * 1024]
used = set()
for f in pages: used |= set(re.findall(r'(assets/img/[^"?\s,)]+)', open(f, encoding="utf-8").read()))
big_used = [(k, p) for k, p in big if p in used]
print("Local images over 400KB that pages use: %s" % (big_used or "none"))

print("\nDEEP FINDINGS:", "none" if not P else "")
for k, vv in sorted(P.items()): print(" ", k, "->", sorted(set(vv))[:6])
