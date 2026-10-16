# -*- coding: utf-8 -*-
"""Broken-link check for the built site.  python _build/link_check.py [--external]
Internal: every href / src / srcset / poster / CSS url() / #anchor on every page.  --external: live HTTP check of every outside URL."""
import os, re, sys, glob, html, collections, concurrent.futures, urllib.request, urllib.error, ssl

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
pages = sorted(f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("assets", "_build", "google")))
ids = {}
for f in pages:
    ids[f] = set(re.findall(r'\sid="([^"]+)"', open(f, encoding="utf-8").read()))

broken = collections.defaultdict(set); external = collections.defaultdict(set); checked = 0
def resolve(base, ref):
    if ref.startswith("/"): return ref.lstrip("/") or "index.html"
    p = os.path.normpath(os.path.join(os.path.dirname(base), ref)).replace(os.sep, "/")
    return p if p != "." else "index.html"

def check(base, ref, kind):
    global checked
    ref = html.unescape(ref.strip())
    if not ref or ref.startswith(("mailto:", "tel:", "data:", "javascript:", "#!")): return
    if ref.startswith(("http://", "https://", "//")):
        external[ref.split("#")[0]].add(base); return
    checked += 1
    path, _, frag = ref.partition("#")
    path = path.split("?")[0]
    target = resolve(base, path) if path else base
    if os.path.isdir(target): target = target.rstrip("/") + "/index.html"
    if not os.path.exists(target):
        broken[base].add("%s %s" % (kind, ref)); return
    if frag and target.endswith(".html") and frag not in ids.get(target, set()) and kind == "href":
        broken[base].add("missing #%s in %s" % (frag, target))

for f in pages:
    t = open(f, encoding="utf-8").read()
    t_nojs = re.sub(r"<script[^>]*>.*?</script>", "", t, flags=re.S)
    for a, v in re.findall(r'\s(href|src|poster|action)="([^"]*)"', t_nojs): check(f, v, a)
    for v in re.findall(r'\ssrcset="([^"]*)"', t_nojs):
        for part in v.split(","):
            if part.strip(): check(f, part.strip().split()[0], "srcset")
    for v in re.findall(r"url\(['\"]?([^)'\"]+)", t_nojs): check(f, v, "css-url")
for css in glob.glob("assets/css/*.css"):
    for v in re.findall(r"url\(['\"]?([^)'\"]+)", open(css, encoding="utf-8", errors="ignore").read()):
        if not v.startswith(("data:", "http", "#")):
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(css), v.split("?")[0].split("#")[0]))):
                broken[css.replace(os.sep, "/")].add("css url " + v)

print("INTERNAL: %d references checked on %d pages; broken: %d" % (checked, len(pages), sum(len(v) for v in broken.values())))
for f, v in sorted(broken.items()): print("  ", f, "->", sorted(v)[:8])

if "--external" in sys.argv:
    ctx = ssl.create_default_context()
    def probe(u):
        url = "https:" + u if u.startswith("//") else u
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(url, method=method, headers={"User-Agent": "Mozilla/5.0 (EnlitEDU link check)"})
                with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                    return u, r.status
            except urllib.error.HTTPError as e:
                if method == "GET" or e.code not in (403, 405, 400, 429): return u, e.code
            except Exception as e:
                if method == "GET": return u, type(e).__name__
        return u, "?"
    skip = ("fonts.googleapis.com", "fonts.gstatic.com", "googletagmanager.com", "api.web3forms.com", "schema.org", "openapi.vercel.sh")
    urls = sorted(u for u in external if not any(s in u for s in skip))
    with concurrent.futures.ThreadPoolExecutor(12) as ex:
        res = list(ex.map(probe, urls))
    bad = [(u, s) for u, s in res if s != 200]
    print("\nEXTERNAL: %d unique URLs checked; not 200: %d" % (len(urls), len(bad)))
    for u, s in bad: print("   %s  %s  (on %s)" % (s, u, sorted(external[u])[0]))
