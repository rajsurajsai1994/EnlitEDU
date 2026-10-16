# -*- coding: utf-8 -*-
"""Pre-launch technical checks not covered by audit.py / schema_audit.py.  python _build/prelaunch_check.py"""
import os, re, glob, html, collections
import xml.etree.ElementTree as ET

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
BASE = "https://www.enlitedu.com"
files = sorted(f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("assets", "_build")))
P = collections.defaultdict(list)

# sitemap
tree = ET.parse("sitemap.xml"); ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
locs = [u.find("s:loc", ns).text for u in tree.getroot()]
lastmods = [u.find("s:lastmod", ns).text for u in tree.getroot()]
print("sitemap.xml: valid XML, %d URLs, lastmod range %s..%s" % (len(locs), min(lastmods), max(lastmods)))
if len(set(locs)) != len(locs): P["sitemap.xml"].append("duplicate URLs")
for u in locs:
    f = u[len(BASE) + 1:] or "index.html"
    t = open(f, encoding="utf-8").read()
    if "noindex" in re.search(r'<meta name="robots" content="([^"]*)"', t).group(1): P["sitemap.xml"].append("noindex page listed: " + f)

# robots
rb = open("robots.txt", encoding="utf-8").read()
print("robots.txt: Sitemap line %s; /_build/ disallowed %s; %d user-agent groups" % ("Sitemap: %s/sitemap.xml" % BASE in rb, "Disallow: /_build/" in rb, rb.count("User-agent:")))

h1s = collections.defaultdict(list)
for f in files:
    t = open(f, encoding="utf-8").read(); head = t.split("</head>")[0]
    noidx = "noindex" in re.search(r'<meta name="robots" content="([^"]*)"', head).group(1)
    for need in ('<meta charset="utf-8">', 'name="viewport"', 'rel="icon"', 'rel="apple-touch-icon"', 'property="og:description"', 'name="twitter:image"', 'property="og:url"'):
        if need.lower() not in head.lower(): P[f].append("head missing " + need)
    ti = html.unescape(re.search(r"<title>(.*?)</title>", t).group(1))
    if not noidx and not 25 <= len(ti) <= 65: P[f].append("title length %d: %s" % (len(ti), ti))
    m = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)
    if m and not noidx: h1s[re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip()].append(f)
    if re.search(r'(src|href)="http://', t): P[f].append("insecure http:// URL")
    for a in re.finditer(r"<a\b[^>]*>", t):
        tag = a.group(0)
        if 'target="_blank"' in tag and "noopener" not in tag: P[f].append("target=_blank without noopener"); break
    for im in re.finditer(r"<img\b[^>]*>", t):
        src = re.search(r'src="([^"]+)"', im.group(0)).group(1)
        if not src.startswith(("http", "data:")):
            p = os.path.normpath(os.path.join(os.path.dirname(f), src.lstrip("/") if src.startswith("/") else src))
            if src.startswith("/"): p = src.lstrip("/")
            if not os.path.exists(p.split("?")[0]): P[f].append("missing image " + src)
    if "—" in t or "–" in t: P[f].append("long dash present")
    vis = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S))
    for bad in ("lorem ipsum", "TODO", "Edupls", "placeholder text"):
        if bad.lower() in vis.lower(): P[f].append("leftover text: " + bad)
    og = re.search(r'property="og:image" content="([^"]+)"', head).group(1)
    if og.startswith(BASE) and not os.path.exists(og[len(BASE) + 1:]): P[f].append("og:image file missing " + og)

for h, fs in h1s.items():
    if len(fs) > 1: P["(duplicate H1)"].append("%s -> %s" % (h, fs))
print("\nPRE-LAUNCH ISSUES:", "none" if not P else "")
for k, v in P.items(): print(" ", k, "->", sorted(set(v))[:6])
