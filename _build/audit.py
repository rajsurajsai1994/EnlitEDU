# -*- coding: utf-8 -*-
"""SEO / AEO audit of the built site. Run from the project root:  python _build/audit.py"""
import os, re, json, glob, html, collections

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
files = [f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("assets", "_build", "google"))]
sitemap = open("sitemap.xml", encoding="utf-8").read()
titles, descs = collections.defaultdict(list), collections.defaultdict(list)
inbound = collections.Counter()
issues = collections.defaultdict(list)
nofaq, types_by, words = [], collections.defaultdict(set), {}

for f in files:
    t = open(f, encoding="utf-8").read()
    ti = html.unescape(re.search(r"<title>(.*?)</title>", t).group(1)); titles[ti].append(f)
    d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', t).group(1)); descs[d].append(f)
    noidx = "noindex" in re.search(r'<meta name="robots" content="([^"]*)"', t).group(1)
    if len(ti) > 65 and not f.startswith("blog/"): issues[f].append("title %d chars" % len(ti))
    if not 110 <= len(d) <= 165 and not noidx: issues[f].append("description %d chars" % len(d))
    can = re.search(r'<link rel="canonical" href="([^"]+)"', t).group(1)
    exp = "https://www.enlitedu.com/" + ("" if f == "index.html" else f)
    if can != exp: issues[f].append("canonical " + can)
    in_sm = ("<loc>" + exp + "</loc>") in sitemap
    if not noidx and f != "404.html" and not in_sm: issues[f].append("missing from sitemap")
    if noidx and in_sm: issues[f].append("noindex but in sitemap")
    for k in ('property="og:title"', 'property="og:image"', 'name="twitter:card"'):
        if k not in t: issues[f].append("missing " + k)
    body = re.search(r'<main id="main">(.*)</main>', t, re.S).group(1)
    hs = [int(x) for x in re.findall(r"<h([1-6])[\s>]", body)]
    if hs.count(1) != 1: issues[f].append("h1 count %d" % hs.count(1))
    prev = 1
    for h in hs[1:]:
        if h > prev + 1:
            issues[f].append("heading skip h%d->h%d" % (prev, h)); break
        prev = h
    for m in re.finditer(r"<img\b[^>]*>", t):
        tag = m.group(0)
        if "alt=" not in tag: issues[f].append("img without alt")
        if "width=" not in tag: issues[f].append("img without width"); break
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try:
            g = json.loads(b.replace("<\\/", "</"))
        except Exception:
            issues[f].append("invalid JSON-LD"); continue
        for n in g.get("@graph", []):
            ty = n.get("@type"); ty = ty if isinstance(ty, list) else [ty]
            types_by[f].update(ty)
            if "FAQPage" in ty:
                vis = t.count('class="faq-item') + (1 if 'class="answer-box"' in t else 0)
                if vis != len(n["mainEntity"]): issues[f].append("FAQ schema %d vs visible %d" % (len(n["mainEntity"]), vis))
    if "faq-item" not in t and not noidx: nofaq.append(f)
    if "BreadcrumbList" not in types_by[f] and f not in ("index.html", "404.html", "thank-you.html"): issues[f].append("no BreadcrumbList")
    for a in re.findall(r'href="([^"#?]+)', t):
        if a.startswith(("http", "mailto:", "tel:", "//")): continue
        p = os.path.normpath(os.path.join(os.path.dirname(f), a.lstrip("/") if a.startswith("/") else a)).replace(os.sep, "/")
        if a.startswith("/"): p = a.lstrip("/") or "index.html"
        inbound[p] += 1
        if not os.path.exists(p): issues[f].append("broken link " + a)
    txt = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", "", body, flags=re.S))
    words[f] = len(txt.split())
    if words[f] < 350 and not noidx: issues[f].append("thin: %d words" % words[f])

print("PAGES:", len(files), "| indexable:", sitemap.count("<loc>"))
print("\nISSUES")
for f, v in sorted(issues.items()): print(" ", f, "->", sorted(set(v)))
print("\nDUPLICATE TITLES:", {k: v for k, v in titles.items() if len(v) > 1})
print("DUPLICATE DESCRIPTIONS:", {k: v for k, v in descs.items() if len(v) > 1})
NOIDX = {f for f in files if "noindex" in open(f, encoding="utf-8").read()[:6000]}
print("ORPHANS:", [f for f in files if inbound[f] == 0 and f not in ("index.html", "404.html", "thank-you.html") and f not in NOIDX])
print("HIDDEN / NOINDEX PAGES:", sorted(NOIDX))
print("NO VISIBLE FAQ (indexable):", nofaq)
print("SCHEMA TYPES ON GEORGIA PAGES:", {f: sorted(types_by[f]) for f in files if "georgia" in f or "near-me" in f})
