# -*- coding: utf-8 -*-
"""Where does Georgia/Atlanta appear on pages that are NOT Georgia pages?  python _build/geo_scan.py"""
import os, re, glob, html
os.chdir(os.path.join(os.path.dirname(__file__), ".."))
RX = re.compile(r"georgia|atlanta|cumming|\bGA\b|tcsg|\busg\b|hope gpa|core impacts", re.I)
def vis(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))
rows = []
for f in sorted(glob.glob("**/*.html", recursive=True)):
    f = f.replace(os.sep, "/")
    if f.startswith(("assets", "_build", "google")): continue
    t = open(f, encoding="utf-8").read()
    head_title = re.search(r"<title>(.*?)</title>", t).group(1)
    topbar = vis(re.search(r'<div class="topbar">(.*?)</header>', t, re.S).group(1))
    main = vis(re.search(r'<main id="main">(.*)</main>', t, re.S).group(1))
    foot = vis(re.search(r'<footer class="site-footer">(.*?)</footer>', t, re.S).group(1))
    n_main = len(RX.findall(main))
    rows.append((f, n_main, len(RX.findall(topbar)), len(RX.findall(foot)), bool(RX.search(head_title))))
local = ("georgia", "transcript-evaluation-near-me", "tcsg-to-usg", "hope-gpa")
print("%-62s main  nav/top  footer  title" % "page")
for f, m, n, ft, ti in rows:
    if any(k in f for k in local): continue
    if m or ti:
        print("%-62s %4d %7d %7d  %s" % (f, m, n, ft, "TITLE" if ti else ""))
print("\nnav/top-bar mentions on every page:", rows[0][2], "| footer mentions on every page:", rows[0][3])
for f in ("index.html", "transfer-credit-intelligence.html", "faq.html", "about.html", "request-demo.html", "case-studies.html", "blog/how-to-choose-transcript-evaluation-software.html"):
    t = vis(re.search(r'<main id="main">(.*)</main>', open(f, encoding="utf-8").read(), re.S).group(1))
    print("\n==", f)
    for m in RX.finditer(t):
        print("   ...", t[max(0, m.start() - 70): m.end() + 60].strip())
