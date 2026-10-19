# -*- coding: utf-8 -*-
"""Audit the LIVE site against the local build.  python _build/live_audit.py
Checks hosts/HTTPS, every sitemap URL (status, no redirect, identical to the local file), robots/sitemap/llms/manifest/
verification file, redirects, real 404s, hidden pages, private files not served, security and cache headers."""
import os, re, sys, glob, hashlib, urllib.request, urllib.error, ssl, concurrent.futures, collections, json

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, "_build")
BASE = "https://www.enlitedu.com"
ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (EnlitEDU launch audit)"}
P = collections.defaultdict(list)

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
opener = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=ctx))

def get(url, follow=False):
    req = urllib.request.Request(url, headers=UA)
    try:
        r = (urllib.request.urlopen(req, timeout=30, context=ctx) if follow else opener.open(req, timeout=30))
        return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()
    except Exception as e:
        return type(e).__name__, {}, b""

local = lambda p: open(p, "rb").read()
norm = lambda b: re.sub(rb"\r\n", b"\n", b).strip()

# 1. hosts and HTTPS
for u in ("http://enlitedu.com/", "https://enlitedu.com/", "http://www.enlitedu.com/"):
    s, h, _ = get(u)
    loc = h.get("Location") or h.get("location") or ""
    ok = s in (301, 302, 307, 308) and loc.rstrip("/").startswith("https://www.enlitedu.com")
    print("%-28s %s -> %s %s" % (u, s, loc, "OK" if ok else "CHECK"))
    if not ok: P["hosts"].append("%s gave %s %s" % (u, s, loc))

# 2. home + headers
s, h, body = get(BASE + "/")
hl = {k.lower(): v for k, v in h.items()}
print("\nHome: %s | server: %s | %d bytes" % (s, hl.get("server", "?"), len(body)))
for k in ("strict-transport-security", "x-content-type-options", "x-frame-options", "referrer-policy", "permissions-policy"):
    if k not in hl: P["headers"].append("missing " + k)
if "x-robots-tag" in hl: P["headers"].append("x-robots-tag on production: " + hl["x-robots-tag"])

# 3. root files identical to local build
for f in ("robots.txt", "sitemap.xml", "llms.txt", "manifest.json", "google6a18e45d8fd24580.html"):
    s, h, b = get(BASE + "/" + f)
    same = s == 200 and norm(b) == norm(local(f))
    print("%-34s %s %s" % (f, s, "identical to build" if same else "DIFFERENT/MISSING"))
    if not same: P["root files"].append("%s status %s" % (f, s))

# 4. every page in the sitemap: 200, no redirect, same bytes as local, canonical = itself, indexable
locs = re.findall(r"<loc>([^<]+)</loc>", local("sitemap.xml").decode())
def check(u):
    s, h, b = get(u)
    f = u[len(BASE) + 1:] or "index.html"
    issues = []
    if s != 200: issues.append("status %s %s" % (s, (h.get("Location") or h.get("location") or "")))
    else:
        if norm(b) != norm(local(f)): issues.append("differs from local build")
        t = b.decode("utf-8", "ignore")
        m = re.search(r'rel="canonical" href="([^"]+)"', t)
        if not m or m.group(1) != u: issues.append("canonical " + (m.group(1) if m else "missing"))
        if 'content="noindex' in t: issues.append("noindex on a sitemap page")
        xr = {k.lower(): v for k, v in h.items()}.get("x-robots-tag", "")
        if "noindex" in xr: issues.append("x-robots-tag noindex")
    return u, issues
with concurrent.futures.ThreadPoolExecutor(10) as ex:
    res = list(ex.map(check, locs))
bad = [(u, i) for u, i in res if i]
print("\nSitemap pages: %d checked, %d with issues" % (len(locs), len(bad)))
for u, i in bad: P["pages"].append("%s: %s" % (u, i))

# 5. hidden pages are reachable but noindex
for f in ("thank-you.html", "application-received.html", "athletics.html", "degree-pathway.html", "events.html"):
    s, h, b = get(BASE + "/" + f)
    if s != 200 or b'content="noindex' not in b: P["hidden pages"].append("%s status %s noindex=%s" % (f, s, b'content="noindex' in b))

# 6. redirects (sample of every kind)
import deploy
tests = {"/articulate.html": "/transfer-credit-intelligence.html", "/assess.html": "/freshman-intelligence.html", "/pla.html": "/prior-learning-assessment.html",
         "/pla": "/prior-learning-assessment.html", "/demo": "/request-demo.html", "/blog/": "/blog.html", "/careers/": "/careers.html",
         "/2024/05/old-post/": "/blog.html", "/images/og-lioraai.jpg": "/assets/img/enlitedu/og-lioraai.jpg", "/favicon.ico": "/assets/img/enlitedu/favicon-32.png",
         "/who-we-serve": "/who-we-serve/community-colleges.html", "/transfer-credit": "/transfer-credit-intelligence.html"}
print()
for src, dst in tests.items():
    s, h, _ = get(BASE + src)
    loc = (h.get("Location") or h.get("location") or "").replace(BASE, "")
    ok = s in (301, 308) and loc == dst
    print("redirect %-26s %s -> %-40s %s" % (src, s, loc, "OK" if ok else "CHECK"))
    if not ok: P["redirects"].append("%s gave %s %s (expected %s)" % (src, s, loc, dst))

# 7. real 404 + private files not served
s, h, b = get(BASE + "/this-page-does-not-exist-12345")
print("\nMissing page -> %s, branded 404 page: %s" % (s, b"This Page Didn" in b))
if s != 404 or b"This Page Didn" not in b: P["404"].append("status %s branded=%s" % (s, b"This Page Didn" in b))
for f in ("/_build/build.py", "/README.md", "/.git/config", "/.vercelignore"):
    s, h, b = get(BASE + f)
    if s == 200: P["private files"].append(f + " is publicly served")

# 8. assets + caching
t = local("index.html").decode()
for a in sorted(set(re.findall(r'(?:href|src)="(assets/(?:css|js)/[^"]+)"', t))):
    s, h, b = get(BASE + "/" + a)
    cc = {k.lower(): v for k, v in h.items()}.get("cache-control", "")
    if s != 200: P["assets"].append("%s status %s" % (a, s))
    print("asset %-45s %s  cache: %s" % (a, s, cc))

print("\nLIVE FINDINGS:", "none" if not P else "")
for k, v in P.items():
    print(" ", k)
    for x in v[:12]: print("     -", x)
