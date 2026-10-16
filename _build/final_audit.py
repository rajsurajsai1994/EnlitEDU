# -*- coding: utf-8 -*-
"""Extra pre-launch checks: content leaks, sitemap/llms consistency, accessibility basics, page weight.  python _build/final_audit.py"""
import os, re, glob, html, collections

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
BASE = "https://www.enlitedu.com"
pages = sorted(f.replace(os.sep, "/") for f in glob.glob("**/*.html", recursive=True) if not f.startswith(("assets", "_build", "google")))
src = {f: open(f, encoding="utf-8").read() for f in pages}
noidx = {f for f, t in src.items() if "noindex" in re.search(r'<meta name="robots" content="([^"]*)"', t).group(1)}
idx = [f for f in pages if f not in noidx]
P = collections.defaultdict(list)
def visible(t):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))

# 1. content that must not appear on live pages
LEAKS = [(r"\bNCAA\b", "NCAA (hidden product)"), (r"Athlete Transcripts", "Athlete Transcripts (hidden)"), (r"Degree Pathway", "Degree Pathway (hidden)"),
         (r"\b(seven|six) modules\b|\b[67] modules\b", "old module count"), (r"24% (increase in )?transfer yield|transfer yield 24%", "unsupported Nashville 24% claim"),
         (r"LioraAI (Articulate|Assess)\b(?!.{0,3}\))", "old module name"), (r"—|–", "long dash"), (r"lorem|ipsum|TODO|TBD|Edupls|placeholder", "template leftovers"),
         (r"\boffshore\b|\bonshore\b", "offshore/onshore")]
for f in idx:
    v = visible(src[f])
    for rx, label in LEAKS:
        if f == "blog/transfer-portal-athlete-eligibility-certification.html" and label.startswith("NCAA"):
            continue  # general article about NCAA certification, not a product claim
        m = re.search(rx, v, re.I if "lorem" in rx else 0)
        if m and not ("formerly" in v[max(0, m.start() - 40):m.end() + 40] and label == "old module name"):
            P[f].append("%s: ...%s..." % (label, v[max(0, m.start() - 40):m.end() + 30].strip()))

# 2. links from indexable pages to hidden pages
hidden_targets = {f for f in noidx if f not in ("404.html",)}
for f in idx:
    for a in re.findall(r'href="([^"#?]+)', src[f]):
        if a.startswith(("http", "mailto", "tel")): continue
        tgt = os.path.normpath(os.path.join(os.path.dirname(f), a)).replace(os.sep, "/")
        if tgt in hidden_targets: P[f].append("links to hidden page " + tgt)

# 3. sitemap / llms.txt consistency
sm = set(u[len(BASE) + 1:] or "index.html" for u in re.findall(r"<loc>([^<]+)</loc>", open("sitemap.xml", encoding="utf-8").read()))
if sm != set(idx): P["sitemap.xml"].append("mismatch: missing %s, extra %s" % (sorted(set(idx) - sm), sorted(sm - set(idx))))
llms = open("llms.txt", encoding="utf-8").read()
for u in re.findall(r"\]\((https://www\.enlitedu\.com/[^)]+)\)", llms):
    p = u[len(BASE) + 1:] or "index.html"
    if p in noidx: P["llms.txt"].append("lists hidden page " + p)
missing_llms = [f for f in idx if f.startswith(("blog/", "careers/", "case-studies/")) or f.count("/") == 0][:0]

# 4. accessibility basics
for f in pages:
    t = src[f]
    if t.count("<main") != 1: P[f].append("main landmark count %d" % t.count("<main"))
    if 'class="skip' not in t and "skip-link" not in t and 'href="#main"' not in t: P[f].append("no skip link")
    ids = set(re.findall(r'<label[^>]*for="([^"]+)"', t))
    for m in re.finditer(r'<(input|select|textarea)\b([^>]*)>', t):
        attrs = m.group(2)
        if re.search(r'type="(hidden|submit|checkbox)"', attrs) and 'name="botcheck"' in attrs or 'type="hidden"' in attrs: continue
        if 'type="checkbox"' in attrs: continue
        i = re.search(r'id="([^"]+)"', attrs)
        if not (i and i.group(1) in ids) and "aria-label" not in attrs: P[f].append("form field without label: " + attrs[:60])
    for m in re.finditer(r"<a\b([^>]*)>(.*?)</a>", t, re.S):
        if not re.sub(r"<[^>]+>|\s", "", m.group(2)) and "aria-label" not in m.group(1) and "<img" not in m.group(2):
            P[f].append("empty link text: " + m.group(1)[:60]); break
    for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", t, re.S):
        if not re.sub(r"<[^>]+>|\s", "", m.group(2)) and "aria-label" not in m.group(1):
            P[f].append("button without text/label"); break

# 5. weight
sizes = sorted(((os.path.getsize(f) // 1024, f) for f in pages), reverse=True)
css = sum(os.path.getsize(f) for f in glob.glob("assets/css/*.css")) // 1024
js = sum(os.path.getsize(f) for f in glob.glob("assets/js/*.js")) // 1024
used_css = set(re.findall(r'href="[./]*(assets/css/[^"?]+)', src["index.html"])); used_js = set(re.findall(r'src="[./]*(assets/js/[^"?]+)', src["index.html"]))
used_kb = (sum(os.path.getsize(p) for p in used_css), sum(os.path.getsize(p) for p in used_js))
eager = len(re.findall(r'<img[^>]*loading="eager"', src["index.html"])); lazy = len(re.findall(r'<img[^>]*loading="lazy"', src["index.html"]))
unsplash = len(set(re.findall(r"images\.unsplash\.com/photo-[^?\"]+", " ".join(src.values()))))

print("Pages: %d (%d indexable, %d hidden: %s)" % (len(pages), len(idx), len(noidx), ", ".join(sorted(noidx))))
print("Sitemap URLs: %d | llms.txt links: %d" % (len(sm), len(re.findall(r"\]\(https://www\.enlitedu\.com/", llms))))
print("Largest HTML: %s" % ", ".join("%s %dKB" % (f, k) for k, f in sizes[:3]))
print("Homepage loads CSS %dKB + JS %dKB (all assets: css %dKB, js %dKB); images: %d eager, %d lazy; %d unique Unsplash photos hotlinked"
      % (used_kb[0] // 1024, used_kb[1] // 1024, css, js, eager, lazy, unsplash))
print("\nFINDINGS:", "none" if not P else "")
for k, v in sorted(P.items()): print(" ", k, "->", sorted(set(v))[:5])
