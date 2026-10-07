# -*- coding: utf-8 -*-
"""Build the EnlitEDU website (Edupls-based variation).  Run:  python _build/build.py"""
import os, re, json, glob, html as _html, datetime, sys
sys.path.insert(0, os.path.dirname(__file__))
from core import *
import pages as P
import pages2 as P2
import pages3 as P3
from data_georgia import GA_PAGES, GA_POSTS, NEAR_ME
from data_modules import MODULES, BY_SLUG
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
POST_MODULE = {"how-to-evaluate-joint-services-transcript-jst": "veterans", "transfer-portal-athlete-eligibility-certification": "athletics",
               "will-my-credits-transfer-self-service-answer": "degree-pathway", "international-transcript-evaluation-first-year-admissions": "assess",
               "reverse-transfer-associate-degree-explained": "mobility", "gpa-standardization-problem": "assess", "prior-learning-assessment-guide": "pla",
               "community-college-transfer-student-success": "articulate", "transfer-student-retention-strategies": "degree-pathway", "hbcu-enrollment-transfer-credit-challenges": "articulate",
               "tcsg-to-usg-transfer-core-impacts-guide": "articulate", "hope-gpa-vs-admissions-gpa-georgia": "assess", "how-to-choose-transcript-evaluation-software": "articulate"}

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
    for g in GA_POSTS:  # native posts written for the Georgia / AEO phase
        d = datetime.date.fromisoformat(g["date"])
        posts[g["slug"]] = dict(g, date_h=d.strftime("%B %-d, %Y") if os.name != "nt" else d.strftime("%B %#d, %Y"),
                                filter=FILTER.get(g["tag"], "transfer"), modified=g["date"])
    return posts

def build_post(p, posts):
    path = "blog/%s.html" % p["slug"]; set_depth(path)
    body = p["body"]
    body = re.sub(r'href="\.\./([a-z\-]+\.html)"', lambda m: 'href="%s"' % u(m.group(1)), body)
    m = BY_SLUG.get(POST_MODULE.get(p["slug"], ""))
    hero = ('<section class="page-hero on-dark"><div class="container"><div class="article">%s<span class="eyebrow">%s</span><h1 style="font-size:clamp(32px,4vw,50px)">%s</h1><p class="sub">%s</p>'
            '<div class="meta-row"><span><i class="fa-solid fa-calendar-days"></i> %s</span><span><i class="fa-solid fa-clock"></i> %d min read</span><span><i class="fa-solid fa-user"></i> EnlitEDU Team</span></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Blog", "blog.html"), (p["tag"], None)]), e(p["tag"]), e(p["title"]), e(p["sub"] or p["desc"]), p["date_h"], p["mins"]))
    cover = '<div class="article" style="margin-top:-70px;position:relative;z-index:2"><div class="split-img" style="aspect-ratio:16/8.5">%s</div></div>' % img(p["img"], 1200, eager=True, sizes="(max-width: 800px) 100vw, 760px", ratio=(16, 8.5))
    author = ('<div class="author-box"><span class="av"><img src="%s" alt="" width="52" height="52"></span><div><b>EnlitEDU Team</b><span>Written with registrars, evaluators and enrollment leaders. Updated %s.</span></div></div>'
              % (u("assets/img/enlitedu/favicon-192.png"), p["modified"]))
    faq_html = ""
    if p["faqs"]:
        items = "".join('<div class="faq-item%s"><button class="faq-q" type="button" aria-expanded="%s">%s<span class="pm"><i class="fa-solid fa-plus"></i></span></button><div class="faq-a"><div><p>%s</p></div></div></div>'
                        % (" open" if i == 0 else "", "true" if i == 0 else "false", e(q), a) for i, (q, a) in enumerate(p["faqs"]))
        faq_html = '<h2>Frequently asked questions</h2><div class="faq-wrap">%s</div>' % items
    inline_cta = ""
    if m:
        inline_cta = ('<div class="callout" style="display:flex;gap:18px;align-items:center;flex-wrap:wrap"><div style="flex:1;min-width:220px"><strong>See it in practice: %s</strong>%s</div><a class="btn-x btn-navy btn-sm" href="%s">Explore %s <i class="fa-solid fa-arrow-right"></i></a></div>'
                      % (e(m["name"]), e(__import__("data_modules").CARD[m["slug"]]), u(m["slug"] + ".html"), e(m["short"])))
    article = ('<section class="sec" style="padding-top:0"><div class="container"><div class="article">%s<div class="article-body">%s%s%s</div></div></div></section>' % (author, body, inline_cta, faq_html))
    rel = [s for s in posts if s != p["slug"] and posts[s]["filter"] == p["filter"]][:3]
    rel += [s for s in sorted(posts, key=lambda s: posts[s]["date"], reverse=True) if s != p["slug"] and s not in rel][:3 - len(rel)]
    page_body = hero + cover + article + P.posts_row(rel, eb="Keep reading", h2="Related <span class=\"grad\">Articles</span>", tint=True) + cta_band()
    url = BASE + "/" + path
    schema = [breadcrumb([("Home", "index.html"), ("Blog", "blog.html"), (p["title"], path)]),
              {"@type": "BlogPosting", "@id": url + "#article", "headline": p["title"], "description": p["desc"], "url": url, "mainEntityOfPage": url,
               "datePublished": p["date"], "dateModified": p["modified"], "author": {"@id": BASE + "/#organization"}, "publisher": {"@id": BASE + "/#organization"},
               "image": src_url(p["img"], 1200), "articleSection": p["tag"], "keywords": p["keywords"], "inLanguage": "en-US", "timeRequired": "PT%dM" % p["mins"],
               "isPartOf": {"@type": "Blog", "@id": BASE + "/blog.html#blog", "name": "EnlitEDU Blog"},
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".page-hero .sub"]}}]
    if p["faqs"]:
        schema.append(faq_schema(p["faqs"], path))
    page(path, "%s | EnlitEDU" % p["title"] if len(p["title"]) < 52 else p["title"], p["desc"], page_body, schema=schema, active="resources", og_type="article", image=src_url(p["img"], 1200))

def build_blog_index(posts):
    path = "blog.html"; set_depth(path)
    order = sorted(posts, key=lambda s: posts[s]["date"], reverse=True)
    feat = posts[order[0]]
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-6">%s<h1>Guides From the <span class="accent">Registrar’s Desk</span></h1>'
            '<p class="sub">Practical, plain-English articles on transfer credit, military and prior-learning credit, GPA standardization, FERPA and student success.</p></div>'
            '<div class="col-lg-6"><a class="post-card" href="%s" style="box-shadow:var(--sh-3)"><div class="thumb">%s<span class="tag">Latest · %s</span></div><div class="body"><span class="meta">%s · %d min read</span><h3>%s</h3><p>%s</p></div></a></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Blog", None)]), eyebrow("The EnlitEDU blog"), u("blog/%s.html" % feat["slug"]), img(feat["img"], 900, alt="", eager=True), e(feat["tag"]), feat["date_h"], feat["mins"], e(feat["title"]), e(feat["desc"])))
    filters = [("all", "All"), ("transfer", "Transfer & credit"), ("admissions", "Admissions"), ("student-success", "Student success"), ("enrollment", "Enrollment"), ("compliance", "Compliance"), ("technical", "Technical")]
    bar = '<div class="filter-bar" data-filter-group="#post-grid" role="group" aria-label="Filter articles">%s</div>' % "".join(
        '<button type="button" data-filter="%s" aria-pressed="%s">%s</button>' % (k, "true" if k == "all" else "false", v) for k, v in filters)
    cards = "".join('<div class="col-md-6 col-lg-4" data-tags="%s" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (posts[s]["filter"], (i % 3) * 80, P.post_card(s, h=2)) for i, s in enumerate(order))
    body = hero + '<section class="sec"><div class="container">%s<div class="row g-4" id="post-grid">%s</div></div></section>' % (bar, cards) + cta_band()
    schema = [breadcrumb([("Home", "index.html"), ("Blog", path)]),
              {"@type": "Blog", "@id": BASE + "/blog.html#blog", "name": "EnlitEDU Blog", "url": BASE + "/blog.html", "publisher": {"@id": BASE + "/#organization"},
               "blogPost": [{"@id": BASE + "/blog/%s.html#article" % s} for s in order]}]
    page(path, "Higher Ed Transfer Credit & Enrollment Blog | EnlitEDU",
         "Practical guides for registrars and enrollment leaders: transfer credit, JST and CPL/PLA, GPA standardization, FERPA, reverse transfer and student success.", body, schema=schema, active="resources")

def write(path, text):
    with open(os.path.join(OUT, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

def main():
    posts = load_posts()
    for s, p in posts.items():
        P.BLOG[s] = p
    P.build_home()
    for m in MODULES: P.build_module(m)
    for s in SOLUTIONS: P.build_solution(s)
    for a in AUDIENCES: P.build_audience(a)
    P2.build_platform(); P2.build_how(); P2.build_integrations(); P2.build_stories(); P2.build_about()
    P2.build_demo(); P2.build_contact(); P2.build_thanks(); P2.build_legal(); P2.build_accessibility()
    P2.build_glossary(); P2.build_faq(); P2.build_small()
    for g in GA_PAGES: P3.build_ga_page(g)
    P3.build_near_me()
    build_blog_index(posts)
    for p in posts.values(): build_post(p, posts)

    # 404 must work at any depth -> root-absolute URLs
    f404 = os.path.join(OUT, "404.html")
    t = open(f404, encoding="utf-8").read()
    t = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|data:)', r'\1="/', t)
    open(f404, "w", encoding="utf-8", newline="\n").write(t)

    # sitemap / robots / llms
    urls = "".join("<url><loc>%s/%s</loc><lastmod>%s</lastmod></url>" % (BASE, "" if p == "index.html" else p, TODAY) for p, nx in PAGES if not nx and p != "404.html")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
    bots = ["Googlebot", "Bingbot", "DuckDuckBot", "Applebot", "Applebot-Extended", "Google-Extended", "GPTBot", "OAI-SearchBot", "ChatGPT-User",
            "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "CCBot"]
    robots = ("# EnlitEDU / LioraAI: search engines and AI answer engines are welcome.\n# Machine-readable summary: %s/llms.txt\n\n"
              "User-agent: *\nAllow: /\nDisallow: /_build/\nDisallow: /thank-you.html\n\n" % BASE)
    robots += "".join("User-agent: %s\nAllow: /\nDisallow: /_build/\n\n" % b for b in bots)
    write("robots.txt", robots + "Sitemap: %s/sitemap.xml\n" % BASE)
    llm = ["# EnlitEDU — LioraAI", "",
           "> EnlitEDU builds LioraAI, an academic record intelligence platform for U.S. colleges and universities. LioraAI evaluates transfer, first-year (freshman), military (JST/CCAF) and prior-learning (CPL/PLA) credit against each institution's own rules, supports NCAA progress-toward-degree documentation, gives students a self-service path to a degree, and provides transfer analytics. Staff and faculty approve every decision; approved credit is written back to the SIS (Banner, Colleague, Workday Student, PeopleSoft, Jenzabar).", "",
           "Key facts: Roane State Community College cut transcript evaluation from about three weeks to two days (reported 90% faster) and went live on Ellucian Banner in 18 days. Nashville State Community College reported a 24% increase in transfer yield in one cycle with Student Mobility Intelligence. Student records are never used to train general-purpose AI models. EnlitEDU acts as a FERPA school official under the institution's control. Headquarters: Cumming, Georgia. Contact: info@enlitedu.com.", "",
           "## Modules"] + ["- [%s](%s/%s.html): %s" % (m["name"], BASE, m["slug"], m["desc"]) for m in MODULES] + [
           "", "## Solutions"] + ["- [%s](%s/solutions/%s.html): %s" % (s["nav"], BASE, s["slug"], s["desc"]) for s in SOLUTIONS] + [
           "", "## Who we serve"] + ["- [%s](%s/who-we-serve/%s.html): %s" % (a["nav"], BASE, a["slug"], a["desc"]) for a in AUDIENCES] + [
           "", "## Georgia & Atlanta (EnlitEDU is headquartered in Cumming, Georgia, north metro Atlanta)"] + [
           "- [%s](%s/%s): %s" % (g["title"].split(" | ")[0], BASE, g["path"], g["desc"]) for g in GA_PAGES] + [
           "- [Transcript evaluation near me](%s/%s): %s" % (BASE, NEAR_ME["path"], NEAR_ME["desc"]),
           "- Georgia rules LioraAI supports: USG Core IMPACTS (42-hour general education core in seven areas; credit transfers area to area between USG institutions), the TCSG–USG general education transfer agreement, Georgia Dual Enrollment college credit, the HOPE GPA calculated by the Georgia Student Finance Commission (distinct from an admissions GPA), and JST/CCAF transcripts from Georgia military installations.",
           "- EnlitEDU provides software to institutions; it does not evaluate individual students' transcripts.",
           "", "## Proof", "- [Roane State Community College](%s/case-studies/roane-state-community-college.html)" % BASE, "- [Nashville State Community College](%s/case-studies/nashville-state-community-college.html)" % BASE,
           "", "## Reference", "- [How LioraAI works](%s/how-it-works.html)" % BASE, "- [Integrations](%s/integrations.html)" % BASE, "- [Security & Trust](%s/security.html)" % BASE,
           "- [Glossary](%s/glossary.html)" % BASE, "- [FAQ](%s/faq.html)" % BASE, "", "## Blog"] + [
           "- [%s](%s/blog/%s.html)" % (posts[s]["title"], BASE, s) for s in sorted(posts, key=lambda s: posts[s]["date"], reverse=True)]
    write("llms.txt", "\n".join(llm) + "\n")
    print("Built %d pages (%d indexable) + sitemap, robots.txt, llms.txt" % (len(PAGES), sum(1 for p, n in PAGES if not n)))

if __name__ == "__main__":
    main()
