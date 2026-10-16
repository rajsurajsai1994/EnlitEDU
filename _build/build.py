# -*- coding: utf-8 -*-
"""Build the EnlitEDU website (Edupls-based variation).  Run:  python _build/build.py"""
import os, re, json, glob, html as _html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from core import *
import pages as P
import pages2 as P2
import pages3 as P3
from data_georgia import GA_PAGES, GA_POSTS, NEAR_ME
from data_us_posts import US_POSTS
from data_modules import MODULES, MODULES_ALL, BY_SLUG
from data_more import SOLUTIONS, AUDIENCES

SRC = P2.SRC
POST_IMG = {
    "ai-in-higher-education-admissions-2025": "presenter", "best-sis-integrations-higher-education-2025": "team-collab",
    "community-college-transfer-student-success": "students-group", "ellucian-banner-integration-transcript-evaluation": "registrar-desk",
    "enrollment-management-strategies-2025": "cabinet", "ferpa-compliance-ai-admissions": "registrar-folder",
    "gpa-standardization-problem": "student-table", "hbcu-enrollment-transfer-credit-challenges": "campus-steps",
    "how-to-evaluate-joint-services-transcript-jst": "veteran-notes", "how-to-speed-up-transfer-credit-evaluation": "registrar-docs",
    "international-transcript-evaluation-first-year-admissions": "library-people", "prior-learning-assessment-guide": "adult-man",
    "registrar-office-efficiency-technology": "meeting-standing", "reverse-transfer-associate-degree-explained": "grad-smile",
    "transfer-portal-athlete-eligibility-certification": "athlete-track", "transfer-student-retention-strategies": "study-table",
    "will-my-credits-transfer-self-service-answer": "student-backpack",
}
FILTER = {"Transfer Credit": "transfer", "Veterans & JST": "transfer", "Best Practices": "transfer", "Admissions": "admissions", "AI & Innovation": "admissions",
          "Student Success": "student-success", "Athletics": "student-success", "Enrollment": "enrollment", "Enrollment Management": "enrollment",
          "Compliance": "compliance", "Technical Insights": "technical"}
POST_MODULE = {"how-to-evaluate-joint-services-transcript-jst": "veterans", "transfer-portal-athlete-eligibility-certification": "transfer-credit-intelligence",
               "will-my-credits-transfer-self-service-answer": "transfer-credit-intelligence", "international-transcript-evaluation-first-year-admissions": "freshman-intelligence",
               "reverse-transfer-associate-degree-explained": "mobility", "gpa-standardization-problem": "freshman-intelligence", "prior-learning-assessment-guide": "pla",
               "community-college-transfer-student-success": "transfer-credit-intelligence", "transfer-student-retention-strategies": "transfer-credit-intelligence", "hbcu-enrollment-transfer-credit-challenges": "transfer-credit-intelligence",
               "tcsg-to-usg-transfer-core-impacts-guide": "transfer-credit-intelligence", "hope-gpa-vs-admissions-gpa-georgia": "freshman-intelligence", "how-to-choose-transcript-evaluation-software": "transfer-credit-intelligence",
               "us-community-college-transfer-statistics": "mobility", "state-transfer-policies-us-guide": "transfer-credit-intelligence", "dual-enrollment-credit-evaluation-us-colleges": "freshman-intelligence"}

ATHLETE_P = ('<p><a href="../athletics.html">LioraAI Athlete Transcripts</a> is built for that spot in the process. It evaluates the incoming transcript against your degree requirements and hands your certification officer a draft — eligibility status, degree progress, and the specific gaps — while the portal window is still open instead of after it\'s closed.</p>')
ATHLETE_NEW = ('<p><a href="../transfer-credit-intelligence.html">LioraAI Transfer Credit Intelligence</a> fits that spot in the process. It evaluates the incoming transcript against your catalog and rules, the same way for athletes and non-athletes, and hands your staff a documented draft while the portal window is still open instead of after it\'s closed.</p>')

PATHWAY_P = ('<p>That\'s what <a href="../degree-pathway.html">Student Degree Pathway</a> is for \u2014 putting an indicative evaluation and a clear path to the degree in the prospective student\'s hands early, running on the same articulation rules your official process uses so the two don\'t contradict each other.</p>')
PATHWAY_NEW = ('<p>That\'s what <a href="../transfer-credit-intelligence.html">LioraAI Transfer Credit Intelligence</a> helps with: a fast, documented evaluation that runs on the same articulation rules as your official process, so the early answer and the official one don\'t contradict each other.</p>')

def _rename(s):
    """Module names changed in Oct 2026; the ported posts still use the old ones."""
    s = s.replace(ATHLETE_P, ATHLETE_NEW).replace(PATHWAY_P, PATHWAY_NEW)
    s = s.replace("LioraAI Articulate", "LioraAI Transfer Credit Intelligence").replace("LioraAI Assess", "LioraAI Freshman Intelligence")
    s = re.sub(r"\barticulate\.html", "transfer-credit-intelligence.html", s)
    s = re.sub(r"\bassess\.html", "freshman-intelligence.html", s)
    s = re.sub(r"(\d)\s?wks\b", r"\1 weeks", s)   # house style: no shorthand units
    s = re.sub(r"(\d)\s?hrs\b", r"\1 hours", s)
    return re.sub(r'<a href="[^"]*(?:athletics|degree-pathway)\.html"[^>]*>(.*?)</a>', r"\1", s)

def load_posts():
    posts = {}
    for f in sorted(glob.glob(os.path.join(SRC, "blog", "*.njk"))):
        slug = os.path.basename(f)[:-4]
        t = open(f, encoding="utf-8").read()
        lds = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)]
        bp = next((x for x in lds if x.get("@type") == "BlogPosting"), {})
        tag = re.search(r'class="post-tag"[^>]*>([^<]+)<', t).group(1).strip()
        sub = re.search(r'class="post-subtitle">(.*?)</p>', t, re.S)
        desc = re.search(r'<meta name="description" content="([^"]*)"', t).group(1)
        main = re.search(r'{% block main %}{% raw %}(.*?){% endraw %}', t, re.S).group(1)
        body = re.search(r'<(?:article|div) class="post-body">(.*?)<div class="post-faq', main, re.S).group(1)
        faqs = []
        for m in re.finditer(r'faq-q-text">(.*?)</span>.*?faq-answer-inner">(.*?)</div>', main, re.S):
            faqs.append((_html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()), re.sub(r"\s+", " ", m.group(2)).strip()))
        date = bp.get("datePublished", "2025-01-01")[:10]
        d = datetime.date.fromisoformat(date)
        mins = int(re.sub(r"\D", "", bp.get("timeRequired", "PT7M")) or 7)
        posts[slug] = dict(slug=slug, title=_html.unescape(bp.get("headline", slug)), desc=_html.unescape(desc), date=date,
                           date_h=d.strftime("%B %-d, %Y") if os.name != "nt" else d.strftime("%B %#d, %Y"),
                           mins=mins, tag=_html.unescape(tag), filter=FILTER.get(_html.unescape(tag), "transfer"), img=POST_IMG.get(slug, "library-people"),
                           sub=_html.unescape(re.sub(r"<[^>]+>", "", sub.group(1)).strip()) if sub else "", body=body, faqs=faqs,
                           keywords=bp.get("keywords", ""), modified=bp.get("dateModified", date)[:10])
    for p in posts.values():
        for k in ("body", "title", "desc", "sub"):
            p[k] = _rename(p[k])
        p["faqs"] = [(_rename(q), _rename(a)) for q, a in p["faqs"]]
    DESC_FIX = {"international-transcript-evaluation-first-year-admissions": "Different grading scales, diploma structures and definitions of secondary school: how to handle international transcripts without outsourcing every file.",
                "reverse-transfer-associate-degree-explained": "A student transfers in with 50 credits and earns 20 more, leaving an unclaimed associate degree behind. Reverse transfer fixes that, if the plumbing works."}
    for k, v in DESC_FIX.items():
        if k in posts: posts[k]["desc"] = v
    for g in GA_POSTS + US_POSTS:  # native posts (Georgia guides + national articles)
        d = datetime.date.fromisoformat(g["date"])
        posts[g["slug"]] = dict(g, region=g.get("region"), date_h=d.strftime("%B %-d, %Y") if os.name != "nt" else d.strftime("%B %#d, %Y"),
                                filter=FILTER.get(g["tag"], "transfer"), modified=g["date"])
    return posts

SEO_TITLE = {
    "ai-in-higher-education-admissions-2025": "AI in Higher Education Admissions: 2025 Guide | EnlitEDU",
    "how-to-speed-up-transfer-credit-evaluation": "How to Speed Up Transfer Credit Evaluation | EnlitEDU",
    "best-sis-integrations-higher-education-2025": "Best SIS Integrations for Higher Education | EnlitEDU",
    "community-college-transfer-student-success": "Community College Transfer Students: Why They’re Underserved",
    "hbcu-enrollment-transfer-credit-challenges": "HBCU Transfer Credit & Enrollment Challenges | EnlitEDU",
    "hope-gpa-vs-admissions-gpa-georgia": "HOPE GPA vs. Admissions GPA in Georgia | EnlitEDU",
    "how-to-choose-transcript-evaluation-software": "How to Choose Transcript Evaluation Software (Checklist)",
    "how-to-evaluate-joint-services-transcript-jst": "How to Read a Joint Services Transcript (JST) | EnlitEDU",
    "international-transcript-evaluation-first-year-admissions": "International Transcript Evaluation for First-Year Admissions",
    "registrar-office-efficiency-technology": "Registrar Office Technology That Reduces Workload",
    "reverse-transfer-associate-degree-explained": "Reverse Transfer Explained: Awarding Associate Degrees",
    "tcsg-to-usg-transfer-core-impacts-guide": "TCSG to USG Transfer Under Core IMPACTS: Georgia Guide",
    "transfer-portal-athlete-eligibility-certification": "Transfer Portal Athlete Eligibility Certification | EnlitEDU",
    "will-my-credits-transfer-self-service-answer": "Will My Credits Transfer? Give Students the Answer Early",
}

def build_post(p, posts):
    path = "blog/%s.html" % p["slug"]; set_depth(path)
    body = p["body"]
    body = re.sub(r'href="\.\./([a-z\-]+\.html)"', lambda m: 'href="%s"' % u(m.group(1)), body)
    m = BY_SLUG.get(POST_MODULE.get(p["slug"], ""))
    hero = ('<section class="page-hero on-dark"><div class="container"><div class="article">%s<span class="eyebrow">%s</span><h1 style="font-size:clamp(32px,4vw,50px)">%s</h1><p class="sub">%s</p>'
            '<div class="meta-row"><span><i class="fa-solid fa-calendar-days"></i> %s</span><span><i class="fa-solid fa-clock"></i> %d min read</span><span><i class="fa-solid fa-user"></i> EnlitEDU Team · Reviewed by Chaitanya Saripalli</span></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Blog", "blog.html"), (p["tag"], None)]), e(p["tag"]), e(p["title"]), e(p["sub"] or p["desc"]), p["date_h"], p["mins"]))
    cover = '<div class="article" style="margin-top:-70px;position:relative;z-index:2"><div class="split-img" style="aspect-ratio:16/8.5">%s</div></div>' % img(p["img"], 1200, eager=True, sizes="(max-width: 800px) 100vw, 760px", ratio=(16, 8.5))
    author = ('<div class="author-box"><span class="av"><img src="%s" alt="" width="52" height="52"></span><div><b>EnlitEDU Team</b><span>Written with registrars, evaluators and enrollment leaders. Updated %s.</span></div></div>'
              % (u("assets/img/enlitedu/favicon-192.png"), p["modified"]))
    author += ('<div class="author-box reviewer"><span class="av"><img src="%s" alt="Chaitanya Saripalli" width="52" height="52" style="object-fit:cover"></span><div>'
               '<b>Reviewed by <a href="%s">Chaitanya Saripalli</a></b><span>Founder &amp; CEO of EnlitEDU and founder of Anatta IT Solutions, which supports colleges’ student information systems. '
               '<a href="%s" target="_blank" rel="noopener">LinkedIn</a></span></div></div>' % (u("assets/img/enlitedu/chaitanya-saripalli.jpg"), u("about.html#leadership"), CS_LINKEDIN))
    faq_html = ""
    if p["faqs"]:
        items = "".join('<div class="faq-item%s"><button class="faq-q" type="button" aria-expanded="%s">%s<span class="pm"><i class="fa-solid fa-plus"></i></span></button><div class="faq-a"><div><p>%s</p></div></div></div>'
                        % (" open" if i == 0 else "", "true" if i == 0 else "false", e(q), a) for i, (q, a) in enumerate(p["faqs"]))
        faq_html = '<h2>Frequently asked questions</h2><div class="faq-wrap">%s</div>' % items
    inline_cta = ""
    if m:
        inline_cta = ('<div class="callout" style="display:flex;gap:18px;align-items:center;flex-wrap:wrap"><div style="flex:1;min-width:220px"><strong>See it in practice: %s</strong>%s</div><a class="btn-x btn-navy btn-sm" href="%s">Explore %s <i class="fa-solid fa-arrow-right"></i></a></div>'
                      % (e(m["name"]), e(__import__("data_modules").CARD[m["slug"]]), u(m["slug"] + ".html"), e(m["short"])))
    article = ('<section class="sec" style="padding-top:0"><div class="container"><div class="article">%s<div class="article-body">%s%s%s</div></div></div></section>' % ('<div class="authors">%s</div>' % author, body, inline_cta, faq_html))
    regional = lambda s: posts[s].get("region") == "Georgia"
    pool = [s for s in posts if s != p["slug"] and (regional(s) == regional(p["slug"]) or not regional(s))]
    rel = [s for s in pool if posts[s]["filter"] == p["filter"]][:3]
    rel += [s for s in sorted(pool, key=lambda s: posts[s]["date"], reverse=True) if s not in rel][:3 - len(rel)]
    page_body = hero + cover + article + P.posts_row(rel, eb="Keep reading", h2="Related <span class=\"grad\">Articles</span>", tint=True) + cta_band()
    url = BASE + "/" + path
    schema = [breadcrumb([("Home", "index.html"), ("Blog", "blog.html"), (p["title"], path)]),
              {"@type": "BlogPosting", "@id": url + "#article", "headline": p["title"], "description": p["desc"], "url": url, "mainEntityOfPage": url,
               "datePublished": p["date"], "dateModified": p["modified"], "author": {"@id": BASE + "/#organization"}, "editor": {"@id": PERSON_CS["@id"]}, "publisher": {"@id": BASE + "/#organization"},
               "image": src_url(p["img"], 1200), "articleSection": p["tag"], "keywords": p["keywords"], "inLanguage": "en-US", "timeRequired": "PT%dM" % p["mins"],
               "isPartOf": {"@type": "Blog", "@id": BASE + "/blog.html#blog", "name": "EnlitEDU Blog"},
               "audience": {"@type": "Audience", "audienceType": "College registrars, admissions and enrollment leaders"},
               "spatialCoverage": {"@type": "State", "name": "Georgia"} if p.get("region") == "Georgia" else {"@type": "Country", "name": "United States"},
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".page-hero .sub"]}}]
    cites = re.findall(r'<ul class="sources">(.*?)</ul>', body, re.S)
    if cites:
        schema[1]["citation"] = sorted(set(re.findall(r'href="(https?://[^"]+)"', cites[0])))
    if p["faqs"]:
        schema.append(faq_schema(p["faqs"], path))
    page(path, SEO_TITLE.get(p["slug"]) or ("%s | EnlitEDU" % p["title"] if len(p["title"]) < 52 else p["title"]), p["desc"], page_body, schema=schema, active="resources", og_type="article", image=src_url(p["img"], 1200))

def build_blog_index(posts):
    path = "blog.html"; set_depth(path)
    order = sorted(posts, key=lambda s: posts[s]["date"], reverse=True)
    national = [s for s in order if posts[s].get("region") != "Georgia"]
    regional_posts = [s for s in order if posts[s].get("region") == "Georgia"]
    feat = posts[national[0]]
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-6">%s<h1>Guides From the <span class="accent">Registrar’s Desk</span></h1>'
            '<p class="sub">Practical, plain-English articles on transfer credit, military and prior-learning credit, GPA standardization, FERPA and student success.</p></div>'
            '<div class="col-lg-6"><a class="post-card" href="%s" style="box-shadow:var(--sh-3)"><div class="thumb">%s<span class="tag">Latest · %s</span></div><div class="body"><span class="meta">%s · %d min read</span><h2>%s</h2><p>%s</p></div></a></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Blog", None)]), eyebrow("The EnlitEDU blog"), u("blog/%s.html" % feat["slug"]), img(feat["img"], 900, alt="", eager=True), e(feat["tag"]), feat["date_h"], feat["mins"], e(feat["title"]), e(feat["desc"])))
    filters = [("all", "All"), ("transfer", "Transfer & credit"), ("admissions", "Admissions"), ("student-success", "Student success"), ("enrollment", "Enrollment"), ("compliance", "Compliance"), ("technical", "Technical")]
    bar = '<div class="filter-bar" data-filter-group="#post-grid" role="group" aria-label="Filter articles">%s</div>' % "".join(
        '<button type="button" data-filter="%s" aria-pressed="%s">%s</button>' % (k, "true" if k == "all" else "false", v) for k, v in filters)
    cards = "".join('<div class="col-md-6 col-lg-4" data-tags="%s" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (posts[s]["filter"], (i % 3) * 80, P.post_card(s, h=2)) for i, s in enumerate(national))
    reg = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up">%s</div>' % P.post_card(s, h=3) for s in regional_posts)
    reg_sec = ('<section class="sec tint"><div class="container"><div class="sec-head" data-aos="fade-up">%s<h2>State Guides: <span class="grad">Georgia</span></h2><p class="lede">Rules that only apply in one state. We work with institutions nationwide; these guides cover Georgia’s transfer and admissions specifics.</p></div><div class="row g-4">%s</div></div></section>'
               % (eyebrow("Regional"), reg)) if regional_posts else ""
    body = hero + '<section class="sec"><div class="container">%s<div class="row g-4" id="post-grid">%s</div></div></section>' % (bar, cards) + reg_sec + cta_band()
    schema = [breadcrumb([("Home", "index.html"), ("Blog", path)]),
              {"@type": "Blog", "@id": BASE + "/blog.html#blog", "name": "EnlitEDU Blog", "url": BASE + "/blog.html", "publisher": {"@id": BASE + "/#organization"},
               "blogPost": [{"@id": BASE + "/blog/%s.html#article" % s} for s in order]}]
    page(path, "Higher Ed Transfer Credit & Enrollment Blog | EnlitEDU",
         "Practical guides for registrars and enrollment leaders: transfer credit, JST and CPL/PLA, GPA standardization, FERPA, reverse transfer and student success.", body, schema=schema, active="resources")

def write(path, text):
    with open(os.path.join(OUT, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(tidy_dashes(text))

def main():
    posts = load_posts()
    for s, p in posts.items():
        P.BLOG[s] = p
        REG[BASE + "/blog/%s.html#article" % s] = {"@type": "BlogPosting", "headline": p["title"], "url": BASE + "/blog/%s.html" % s, "datePublished": p["date"]}
    for m in MODULES_ALL:
        REG[BASE + "/%s.html#software" % m["slug"]] = {"@type": "SoftwareApplication", "name": m["name"], "url": BASE + "/%s.html" % m["slug"]}
    for slug, name in (("roane-state-community-college", "Roane State Community College customer story"), ("nashville-state-community-college", "Nashville State Community College customer story")):
        REG[BASE + "/case-studies/%s.html" % slug] = {"@type": "Article", "headline": name, "url": BASE + "/case-studies/%s.html" % slug}
    P.build_home()
    for m in MODULES_ALL: P.build_module(m)
    # old module URLs (renamed Oct 2026) -> noindex stubs that forward to the new pages
    for old, new, oldname in (("articulate.html", "transfer-credit-intelligence.html", "LioraAI Articulate"), ("assess.html", "freshman-intelligence.html", "LioraAI Assess")):
        set_depth(old); nm = BY_SLUG[new[:-5]]["name"]
        body = ('<section class="page-hero on-dark"><div class="container"><div class="row"><div class="col-lg-8"><h1>This Page Has Moved</h1>'
                '<p class="sub">%s is now <a style="color:#fff;text-decoration:underline" href="%s">%s</a>.</p></div></div></div></section>'
                '<script>location.replace("%s")</script>' % (oldname, u(new), nm, u(new)))
        page(old, "%s is now %s" % (oldname, nm), "%s has been renamed %s. This page forwards to the new address." % (oldname, nm), body,
             schema=[breadcrumb([("Home", "index.html"), ("%s is now %s" % (oldname, nm), old)])], noindex=True)
    for s in SOLUTIONS: P.build_solution(s)
    for a in AUDIENCES: P.build_audience(a)
    P2.build_platform(); P2.build_how(); P2.build_integrations(); P2.build_stories(); P2.build_about()
    P2.build_demo(); P2.build_contact(); P2.build_thanks(); P2.build_legal(); P2.build_accessibility()
    P2.build_glossary(); P2.build_faq(); P2.build_small()
    for g in GA_PAGES: P3.build_ga_page(g)
    P3.build_near_me()
    import pages_careers; pages_careers.build_all()
    build_blog_index(posts)
    for p in posts.values(): build_post(p, posts)

    # 404 must work at any depth -> root-absolute URLs
    f404 = os.path.join(OUT, "404.html")
    t = open(f404, encoding="utf-8").read()
    t = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|data:)', r'\1="/', t)
    open(f404, "w", encoding="utf-8", newline="\n").write(t)

    # sitemap / robots / llms
    lm = {"blog/%s.html" % s: posts[s]["modified"] for s in posts}
    urls = "".join("<url><loc>%s/%s</loc><lastmod>%s</lastmod></url>" % (BASE, "" if p == "index.html" else p, lm.get(p, TODAY)) for p, nx in PAGES if not nx and p != "404.html")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
    bots = ["Googlebot", "Bingbot", "DuckDuckBot", "Applebot", "Applebot-Extended", "Google-Extended", "GPTBot", "OAI-SearchBot", "ChatGPT-User",
            "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "CCBot"]
    robots = ("# EnlitEDU / LioraAI: search engines and AI answer engines are welcome.\n# Machine-readable summary: %s/llms.txt\n\n"
              "User-agent: *\nAllow: /\nDisallow: /_build/\nDisallow: /thank-you.html\nDisallow: /application-received.html\n\n" % BASE)
    robots += "".join("User-agent: %s\nAllow: /\nDisallow: /_build/\n\n" % b for b in bots)
    write("robots.txt", robots + "Sitemap: %s/sitemap.xml\n" % BASE)
    llm = ["# EnlitEDU — LioraAI", "",
           "> EnlitEDU builds LioraAI, AI transcript evaluation software for U.S. colleges and universities. Lead products: LioraAI Transfer Credit Intelligence (automated transfer credit evaluation) and LioraAI Freshman Intelligence (high school transcript automation). LioraAI evaluates transfer, first-year (freshman), military (JST/CCAF) and prior-learning (CPL/PLA) credit against each institution's own rules and provides transfer analytics. Staff and faculty approve every decision; approved credit is written back to the SIS (Banner, Colleague, Workday Student, PeopleSoft, Jenzabar).", "",
           "Key facts: Roane State Community College cut transcript evaluation from about three weeks to two days (reported 90% faster) and went live on Ellucian Banner in 18 days. Nashville State Community College cut per-transcript evaluation time from about 15 minutes to 2 minutes (87%) and approval turnaround from 18 to 8 hours (56%) after going live in July 2026. Student records are never used to train general-purpose AI models. EnlitEDU acts as a FERPA school official under the institution's control. Headquarters: Cumming, Georgia. Contact: info@enlitedu.com.", "",
           "Leadership: Chaitanya Saripalli, Founder & CEO of EnlitEDU (https://www.linkedin.com/in/chaitanyasaripalli/). Module names: LioraAI Transfer Credit Intelligence (formerly Articulate) for transfer credit evaluation; LioraAI Freshman Intelligence (formerly Assess) for freshman / first-year transcript evaluation.", "",
           "Where we work: colleges, universities, technical colleges and state systems across the United States. Demos, implementation and training run online in every state. Georgia/Atlanta pages below are regional guides, not a service limit.", "",
           "## Modules"] + ["- [%s](%s/%s.html): %s" % (m["name"], BASE, m["slug"], m["desc"]) for m in MODULES] + [
           "", "## Solutions"] + ["- [%s](%s/solutions/%s.html): %s" % (s["nav"], BASE, s["slug"], s["desc"]) for s in SOLUTIONS] + [
           "", "## Who we serve"] + ["- [%s](%s/who-we-serve/%s.html): %s" % (a["nav"], BASE, a["slug"], a["desc"]) for a in AUDIENCES] + [
           "", "## Guides (national, each with a short Georgia section; Georgia is the headquarters state, not a service limit)"] + [
           "- [%s](%s/%s): %s" % (g["title"].split(" | ")[0], BASE, g["path"], g["desc"]) for g in GA_PAGES] + [
           "- [Transcript evaluation near me](%s/%s): %s" % (BASE, NEAR_ME["path"], NEAR_ME["desc"]),
           "- Georgia rules LioraAI supports: USG Core IMPACTS (42-hour general education core in seven areas; credit transfers area to area between USG institutions), the TCSG–USG general education transfer agreement, Georgia Dual Enrollment college credit, the HOPE GPA calculated by the Georgia Student Finance Commission (distinct from an admissions GPA), and JST/CCAF transcripts from Georgia military installations.",
           "- EnlitEDU provides software to institutions; it does not evaluate individual students' transcripts.",
           "", "## Careers", "- [Careers at EnlitEDU](%s/careers.html)" % BASE] + [
           "- [%s](%s/careers/%s.html): %s, %s. %s" % (j["title"], BASE, j["slug"], j["location"], j["employment"].lower(), j["summary"]) for j in __import__("data_careers").JOBS if j.get("open")] + [
           "", "## Proof", "- [Roane State Community College](%s/case-studies/roane-state-community-college.html)" % BASE, "- [Nashville State Community College](%s/case-studies/nashville-state-community-college.html)" % BASE,
           "", "## Reference", "- [How LioraAI works](%s/how-it-works.html)" % BASE, "- [Integrations](%s/integrations.html)" % BASE, "- [Security & Trust](%s/security.html)" % BASE,
           "- [Glossary](%s/glossary.html)" % BASE, "- [FAQ](%s/faq.html)" % BASE, "", "## Blog"] + [
           "- [%s](%s/blog/%s.html)" % (posts[s]["title"], BASE, s) for s in sorted(posts, key=lambda s: posts[s]["date"], reverse=True)]
    write("llms.txt", "\n".join(llm) + "\n")
    import deploy  # redirects, headers, error pages and manifest for Vercel, CloudFront, Netlify and Apache
    n = deploy.write_all(OUT, old_site_dir=r"C:\Users\SurajPaluri\Downloads\Enlitedu_Website\_site")
    print("Deploy files: vercel.json, cloudfront-function-redirects.js, _redirects, _headers, .htaccess, manifest.json (%d redirects)" % len(n))
    print("Built %d pages (%d indexable) + sitemap, robots.txt, llms.txt" % (len(PAGES), sum(1 for p, n in PAGES if not n)))

if __name__ == "__main__":
    main()
