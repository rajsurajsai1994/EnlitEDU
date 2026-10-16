# -*- coding: utf-8 -*-
"""Verify where each target keyword actually appears on the built site.  python _build/keyword_map.py"""
import os, re, glob, html, json

os.chdir(os.path.join(os.path.dirname(__file__), ".."))

# keyword, cluster, intent, demand signal (from Google + Bing + DuckDuckGo autocomplete, Oct 2026), target page, regex
K = [
 # --- core software (B2B)
 ("transcript evaluation software", "Core software", "Buyer (B2B)", "Medium", "index.html", r"transcript evaluation software"),
 ("transfer credit evaluation software", "Core software", "Buyer (B2B)", "Low–Medium", "articulate.html", r"transfer credit evaluation software"),
 ("credit evaluation software", "Core software", "Buyer (mixed with finance)", "Low", "georgia.html", r"credit evaluation software"),
 ("AI transcript evaluation", "Core software", "Buyer (B2B)", "Low, rising", "blog/how-to-choose-transcript-evaluation-software.html", r"ai transcript evaluation|ai-assisted transcript"),
 ("transcript review software", "Core software", "Buyer (B2B)", "Low", "blog/how-to-choose-transcript-evaluation-software.html", r"transcript review software"),
 ("college credit evaluation", "Core software", "Mixed", "Low–Medium", "articulate.html", r"credit evaluation"),
 # --- local
 ("transcript evaluation software Georgia", "Georgia / Atlanta", "Buyer (local)", "Very low (long-tail)", "georgia.html", r"transcript (and|&|and credit) ?(credit )?evaluation software (for|built in).{0,30}georgia|georgia.{0,40}transcript evaluation software"),
 ("credit evaluation software Georgia", "Georgia / Atlanta", "Buyer (local)", "Very low (long-tail)", "georgia.html", r"credit evaluation software for georgia|credit evaluation software built in metro atlanta"),
 ("transcript evaluation Atlanta", "Georgia / Atlanta", "Mixed (local)", "Low", "georgia/atlanta-transcript-evaluation.html", r"transcript evaluation (software )?in atlanta|transcript evaluation for atlanta|atlanta transcript evaluation"),
 ("transcript evaluation software Atlanta GA", "Georgia / Atlanta", "Buyer (local)", "Very low (long-tail)", "georgia/atlanta-transcript-evaluation.html", r"transcript evaluation software in atlanta"),
 ("Atlanta edtech company", "Georgia / Atlanta", "Discovery", "Low", "georgia/atlanta-transcript-evaluation.html", r"atlanta-area edtech company"),
 ("freshman transcript evaluation Atlanta", "Georgia / Atlanta", "Buyer (local)", "Very low (long-tail)", "georgia/freshman-transcript-evaluation.html", r"freshman transcript evaluation (in|for) atlanta"),
 ("freshman transcript evaluation Georgia", "Georgia / Atlanta", "Buyer (local)", "Very low (long-tail)", "georgia/freshman-transcript-evaluation.html", r"freshman transcript evaluation.{0,40}georgia"),
 ("transfer credit evaluation Georgia", "Georgia / Atlanta", "Buyer (local)", "Low", "georgia/transfer-credit-evaluation.html", r"transfer credit evaluation (software )?(for|in) georgia|georgia transfer credit evaluation"),
 ("military transcript evaluation Georgia", "Georgia / Atlanta", "Buyer (local)", "Very low (long-tail)", "georgia/military-transcript-evaluation.html", r"military (& jst )?transcript evaluation (in|for) georgia|military transcript evaluation for georgia"),
 ("transcript evaluation near me", "Near me", "Mostly individuals", "High (individual intent)", "transcript-evaluation-near-me.html", r"transcript evaluation near me"),
 ("credential evaluation near me", "Near me", "Individuals", "Medium (individual intent)", "transcript-evaluation-near-me.html", r"credential evaluation near me"),
 ("foreign transcript evaluation near me", "Near me", "Individuals", "Medium (individual intent)", "transcript-evaluation-near-me.html", r"foreign transcript evaluation near me"),
 # --- Georgia system topics
 ("TCSG to USG transfer", "Georgia topics (AEO)", "Practitioner / student", "Low–Medium (GA)", "georgia/transfer-credit-evaluation.html", r"tcsg to usg|tcsg–usg|tcsg-usg"),
 ("Core IMPACTS transfer", "Georgia topics (AEO)", "Practitioner / student", "Medium (GA)", "blog/tcsg-to-usg-transfer-core-impacts-guide.html", r"core impacts"),
 ("HOPE GPA vs admissions GPA", "Georgia topics (AEO)", "Practitioner / parent", "Medium (GA, student-heavy)", "blog/hope-gpa-vs-admissions-gpa-georgia.html", r"hope gpa"),
 ("Georgia Dual Enrollment credit", "Georgia topics (AEO)", "Practitioner / parent", "Low–Medium (GA)", "georgia/freshman-transcript-evaluation.html", r"georgia dual enrollment"),
 # --- modules (national)
 ("military transcript evaluation", "Modules", "Buyer / practitioner", "Low–Medium", "veterans.html", r"military transcript evaluation"),
 ("JST transcript evaluation", "Modules", "Practitioner", "Low", "veterans.html", r"joint services transcript|\bjst\b"),
 ("ACE military credit", "Modules", "Practitioner", "Low", "veterans.html", r"ace (credit )?recommendation"),
 ("credit for prior learning software", "Modules", "Buyer", "Low", "pla.html", r"credit for prior learning"),
 ("high school transcript evaluation", "Modules", "Mixed", "Low–Medium", "assess.html", r"high school transcript"),
 ("GPA standardization", "Modules", "Practitioner", "Low", "assess.html", r"gpa standardization|standardize[sd]? (every )?gpa"),
 ("NCAA progress toward degree", "Modules", "Practitioner", "Medium", "athletics.html", r"progress-toward-degree|progress toward degree"),
 ("will my credits transfer", "Modules", "Students (pre-applicants)", "Medium", "degree-pathway.html", r"will my credits transfer"),
 ("reverse transfer", "Modules", "Practitioner", "Low", "mobility.html", r"reverse transfer"),
 # --- question keywords
 ("what is transcript evaluation", "Questions (AEO)", "Informational", "Medium", "transcript-evaluation-near-me.html", r"what is transcript evaluation"),
 ("how long does transcript evaluation take", "Questions (AEO)", "Informational", "Medium", "transcript-evaluation-near-me.html", r"how long does (a )?transcript evaluation take|how long does (a )?military transcript evaluation take"),
 ("transcript evaluation cost", "Questions (AEO)", "Informational", "Medium", "transcript-evaluation-near-me.html", r"how much does (a )?transcript evaluation|transcript evaluation software cost"),
 ("how do I know if my credits will transfer", "Questions (AEO)", "Students", "Medium", "georgia/transfer-credit-evaluation.html", r"how do i know if my credits will transfer"),
 ("do TCSG credits transfer to USG", "Questions (AEO)", "Students / practitioners", "Low (GA)", "georgia/transfer-credit-evaluation.html", r"do tcsg credits transfer"),
 ("what is USG Core IMPACTS", "Questions (AEO)", "Informational (GA)", "Low–Medium (GA)", "georgia/transfer-credit-evaluation.html", r"what is usg core impacts|what is core impacts"),
 ("is the HOPE GPA the same as admissions GPA", "Questions (AEO)", "Informational (GA)", "Low–Medium (GA)", "georgia/freshman-transcript-evaluation.html", r"is the hope gpa the same"),
]

def strip(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).replace(" ,", ",").lower()

pages = {}
for f in glob.glob("**/*.html", recursive=True):
    f = f.replace(os.sep, "/")
    if f.startswith(("assets", "_build")): continue
    t = open(f, encoding="utf-8").read()
    if 'content="noindex' in t: continue
    main = re.search(r'<main id="main">(.*)</main>', t, re.S).group(1)
    pages[f] = dict(title=strip(re.search(r"<title>(.*?)</title>", t).group(1)),
                    desc=strip(re.search(r'<meta name="description" content="([^"]*)"', t).group(1)),
                    h1=strip(" ".join(re.findall(r"<h1[^>]*>(.*?)</h1>", main, re.S))),
                    hx=strip(" ".join(re.findall(r"<h[23][^>]*>(.*?)</h[23]>", main, re.S))),
                    faq=strip(" ".join(re.findall(r'class="faq-q"[^>]*>(.*?)<span', main, re.S)) + " " + " ".join(re.findall(r'<p class="q">(.*?)</p>', main, re.S))),
                    body=strip(re.sub(r"<(script|style)[^>]*>.*?</\1>", "", main, flags=re.S)))

out = []
for kw, cluster, intent, demand, target, rx in K:
    r = re.compile(rx, re.I)
    tp = pages.get(target, {})
    where = [k for k in ("title", "desc", "h1", "hx", "faq") if tp and r.search(tp[k])]
    also = sorted([p for p, d in pages.items() if p != target and r.search(d["body"])])
    out.append(dict(kw=kw, cluster=cluster, intent=intent, demand=demand, target=target, on_target=bool(tp and r.search(tp["body"])),
                    where=where, also=also, also_n=len(also)))
json.dump(out, open("_build/keyword_map.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for o in out:
    print("%-45s %-48s target:%s  in:%s  +%d pages" % (o["kw"], o["target"], "YES" if o["on_target"] else "NO ", ",".join(o["where"]) or "-", o["also_n"]))
