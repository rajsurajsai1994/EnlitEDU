# -*- coding: utf-8 -*-
"""Georgia / Atlanta local pages, the 'near me' guide, and Georgia blocks reused on other pages."""
import re
from core import *
from pages import (BLOG, story_card, posts_row, arrow, MOD_IMG)
from data_modules import BY_SLUG, CARD, HIDDEN
from data_georgia import GA_PAGES, NEAR_ME, LOCAL, COUNTIES, GA_CITIES

GA_BY_PATH = {p["path"]: p for p in GA_PAGES}
GA_NAV_LABEL = {"georgia/freshman-transcript-evaluation.html": "Freshman transcript evaluation", "georgia/transfer-credit-evaluation.html": "Transfer credit & state rules",
                "georgia/military-transcript-evaluation.html": "Military & JST evaluation", "transcript-evaluation-near-me.html": "Transcript evaluation guide",
                "georgia/atlanta-transcript-evaluation.html": "Our Atlanta team", "georgia.html": "Georgia (headquarters state)"}

def answer_box(q, a):
    """Short, quotable answer near the top of the page (AEO / AI overviews)."""
    return ('<section class="sec-sm" style="padding-bottom:0"><div class="container"><div class="answer-box" data-aos="fade-up">'
            '<p class="q">%s</p><p class="a">%s</p></div></div></section>' % (e(q), e(a)))

def local_card():
    return ('<div class="local-card"><h3>Work with us from any state</h3>'
            '<p class="small">Demos, implementation and training run online for colleges and universities across the U.S. On-campus visits are available on request.</p>'
            '<address><b>EnlitEDU headquarters</b><br>%s<br>%s, %s %s</address>'
            '<div class="btn-row"><a class="btn-x btn-gold btn-sm" href="%s">Request a demo</a><a class="btn-x btn-ghost btn-sm" href="%s" target="_blank" rel="noopener">Open in Maps</a></div></div>'
            % (LOCAL["street"], LOCAL["city"], LOCAL["region"], LOCAL["zip"], u("request-demo.html"), LOCAL["maps"]))

def ga_links(current=None, title="Related guides"):
    items = "".join('<a class="ga-link" href="%s"><i class="fa-solid fa-arrow-right"></i>%s</a>' % (u(p), e(l)) for p, l in GA_NAV_LABEL.items() if p != current)
    return '<div class="ga-links"><p class="small fw-bold mb-2">%s</p>%s</div>' % (e(title), items)

def service_schema(p, url):
    areas = [{"@type": "Country", "name": "United States"}, {"@type": "State", "name": "Georgia", "containedInPlace": {"@type": "Country", "name": "United States"}}]
    if p.get("city"):
        areas.append({"@type": "City", "name": "Atlanta", "containedInPlace": {"@type": "State", "name": "Georgia"}})
    return {"@type": "Service", "@id": url + "#service", "name": p["service"], "serviceType": "Transcript and credit evaluation software",
            "provider": {"@id": BASE + "/#organization"}, "areaServed": areas, "url": url,
            "audience": {"@type": "Audience", "audienceType": "Colleges, universities and technical colleges"},
            "isRelatedTo": {"@id": BASE + "/#lioraai"}}

def build_ga_page(p):
    path = p["path"]; set_depth(path)
    url = BASE + "/" + path
    st = "".join('<div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in p["stats"])
    crumb = [("Home", "index.html"), (p["nav"], None)]
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-6">%s<h1>%s</h1><p class="sub">%s</p>'
            '<div class="btn-row mt-4"><a class="btn-x btn-gold" href="%s">Request a demo <i class="fa-solid fa-arrow-right"></i></a><a class="btn-x btn-ghost-light" href="#ga-content">How it works</a></div>'
            '<div class="hero-stats">%s</div></div><div class="col-lg-6"><div class="visual"><div class="ph">%s</div>%s</div></div></div></div></section>'
            % (crumbs(crumb), eyebrow(e(p["eyebrow"])), p["h1"], p["sub"], u("request-demo.html"), st,
               img(p["img"], 900, eager=True, ratio=(4, 3.3)), float_card("fa-flag-usa", "gold", "Colleges across the U.S.", "Online demos in every state", "fc-a")))
    secs = ""
    for i, (h2, html_) in enumerate(p["sections"]):
        html_ = re.sub(r'href="\.\./([^"]+)"', lambda m: 'href="%s"' % u(m.group(1)), html_)
        if path == "georgia.html":
            html_ = html_.replace('href="../', 'href="')
        secs += '<div class="ga-sec" data-aos="fade-up"><h2>%s</h2>%s</div>' % (e(h2), html_)
    side = ('<aside class="ga-side"><div class="split-img mb-4">%s</div>%s%s</aside>' % (img(p["img2"], 700, ratio=(4, 3.4)), local_card(), ga_links(path)))
    content = ('<section class="sec anchor" id="ga-content"><div class="container"><div class="row g-5"><div class="col-lg-8"><div class="ga-body">%s</div></div><div class="col-lg-4">%s</div></div></div></section>' % (secs, side))
    mods = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d">%s</div>' % ((i % 3) * 80, mod_card(BY_SLUG[k]["slug"] + ".html", BY_SLUG[k]["cat"], BY_SLUG[k]["name"], CARD[k], BY_SLUG[k]["icon"], MOD_IMG[k])) for i, k in enumerate([k for k in p["modules"] if k not in HIDDEN]))
    mod_sec = '<section class="sec tint"><div class="container">%s<div class="row g-4">%s</div></div></section>' % (sec_head("LioraAI modules", "Modules Teams Usually <span class=\"grad\">Start With</span>", "", center=True), mods)
    proof = ('<section class="sec"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-5" data-aos="fade-up">%s<h2>Proven at <span class="grad">Community Colleges</span></h2>'
             '<p class="lead-lg">Our first customers are Tennessee community colleges. Roane State cut transcript evaluation from about three weeks to two days, and Nashville State cut per-transcript time from 15 minutes to 2.</p>%s</div>'
             '<div class="col-lg-7"><div class="row g-4"><div class="col-md-6">%s</div><div class="col-md-6">%s</div></div></div></div></div></section>'
             % (eyebrow("Customer proof"), arrow("All customer stories", "case-studies.html"), story_card("roane"), story_card("nashville")))
    body = (hero + answer_box(*p["answer"]) + content + mod_sec + proof + testimonials_section(dark=True)
            + faq_block(p["faqs"], title="Frequently Asked Questions", side_img=p["img2"]) + posts_row([b for b in p["blog"] if b in BLOG], tint=True)
            + cta_band(h2="See LioraAI on <span class=\"grad\">your</span> transcripts.", p="Bring a few anonymized transcripts and we’ll run them live against your catalog, online from anywhere in the U.S. or on your campus."))
    bc = [("Home", "index.html"), (p["nav"], path)]
    schema = [breadcrumb(bc), service_schema(p, url),
              {"@type": "WebPage", "@id": url, "url": url, "name": p["title"], "about": {"@id": url + "#service"},
               "spatialCoverage": {"@type": "Country", "name": "United States"},
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".answer-box"]}},
              faq_schema([(p["answer"][0], p["answer"][1])] + p["faqs"], path)]
    page(path, p["title"], p["desc"], body, schema=schema, active="audience")

def build_near_me():
    p = NEAR_ME; path = p["path"]; set_depth(path); url = BASE + "/" + path
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row g-5"><div class="col-lg-8">%s<h1>%s</h1><p class="sub">%s</p></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Transcript evaluation near me", None)]), eyebrow("Guide · Colleges and individuals"), p["h1"], p["sub"]))
    paths = ('<section class="sec"><div class="container"><div class="row g-4">'
             '<div class="col-lg-6" data-aos="fade-up"><div class="card-x d-flex flex-column"><div class="ico"><i class="fa-solid fa-building-columns"></i></div><span class="cat-lbl">For colleges &amp; universities</span>'
             '<h2 style="font-size:28px">You evaluate transcripts for admission or transfer</h2><p>Registrar’s offices, admissions teams, School Certifying Officials and athletics compliance staff evaluate thousands of transcripts a year. '
             'That is what <strong>LioraAI</strong> is for: it reads each transcript, applies your rules, and gives staff a documented recommendation to approve. EnlitEDU works with colleges across the U.S., online or on campus.</p>'
             '<ul class="check-list"><li>Transfer credit, freshman, military and prior-learning transcripts</li><li>Any state’s transfer rules, configured for you</li><li>Online demos in every state; on-campus on request</li></ul>'
             '<div class="btn-row mt-auto"><a class="btn-x btn-gold" href="%s">Book a demo <i class="fa-solid fa-arrow-right"></i></a><a class="link-arrow" href="%s">See all modules <i class="fa-solid fa-arrow-right"></i></a></div></div></div>'
             '<div class="col-lg-6" data-aos="fade-up" data-aos-delay="100"><div class="card-x d-flex flex-column"><div class="ico gold"><i class="fa-solid fa-user"></i></div><span class="cat-lbl">For individuals</span>'
             '<h2 style="font-size:28px">You need your own transcript or degree evaluated</h2><p>If you studied outside the U.S. and a college, employer or licensing board asked for an evaluation, you need a <strong>credential evaluation service</strong>, not software. '
             'Most colleges require a member of the National Association of Credential Evaluation Services (NACES). Searches like “credential evaluation near me” or “foreign transcript evaluation near me” usually mean this kind of service.</p>'
             '<ul class="check-list"><li>Ask your college or board which evaluators it accepts</li><li>Choose document-by-document or course-by-course, as required</li><li>Most services work online, so location rarely matters</li></ul>'
             '<p class="small muted mt-auto mb-0">EnlitEDU does not evaluate individual transcripts.</p></div></div></div></div></section>'
             % (u("request-demo.html"), u("platform.html")))
    explain = ('<section class="sec tint"><div class="container"><div class="row g-5"><div class="col-lg-7" data-aos="fade-up"><div class="ga-body">'
               '<div class="ga-sec"><h2>What is transcript evaluation?</h2><p>Transcript evaluation means reviewing an academic record to decide what it is worth somewhere else: which courses transfer, how grades convert, and how much credit applies to a degree. Colleges do it for every transfer, first-year, military and returning student. Credential evaluators do it for individuals with foreign records.</p></div>'
               '<div class="ga-sec"><h2>How long does transcript evaluation take?</h2><p>In many registrar’s offices a manual transfer evaluation takes three to eight weeks. With LioraAI, a transcript is evaluated in under a minute and staff typically approve decisions within days. Roane State Community College went from about three weeks to two days.</p></div>'
               '<div class="ga-sec"><h2>Does “near me” matter for colleges?</h2><p>Less than fit. What matters is a vendor that knows your state’s transfer rules, works with your SIS and can meet in person when you need it. EnlitEDU works with colleges across the U.S. online, and its team is headquartered in Cumming, Georgia, in north metro Atlanta, for institutions that want to meet face to face.</p></div>'
               '</div></div><div class="col-lg-5">%s%s</div></div></div></section>' % (local_card(), ga_links(path, "Related guides")))
    body = (hero + answer_box(*p["answer"]) + paths + explain
            + faq_block(p["faqs"], title="Transcript Evaluation Questions", side_img="registrar-folder") + cta_band(secondary=None))
    schema = [breadcrumb([("Home", "index.html"), ("Transcript evaluation near me", path)]),
              {"@type": "WebPage", "@id": url, "url": url, "name": p["title"], "about": {"@id": BASE + "/#lioraai"},
               "spatialCoverage": {"@type": "Country", "name": "United States"}, "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".answer-box"]}},
              faq_schema([(p["answer"][0], p["answer"][1])] + p["faqs"], path)]
    page(path, p["title"], p["desc"], body, schema=schema, active="audience")

def home_nationwide_section():
    cards = [("fa-scale-balanced", "Every state’s transfer rules", "State agreements, common course numbering, guaranteed pathways and general education frameworks, configured as rules for your institution.", "solutions/stay-audit-ready.html", "Consistent decisions"),
             ("fa-laptop", "Implemented remotely, anywhere", "Demos, configuration and training run online for institutions in every state. Standard SIS integrations take two to four weeks.", "integrations.html", "Integrations"),
             ("fa-star", "Proven at community colleges", "Roane State and Nashville State in Tennessee report much faster evaluations and approvals.", "case-studies.html", "Customer stories"),
             ("fa-building", "Headquartered in metro Atlanta", "Our team is based in Cumming, Georgia. Georgia institutions can also meet us on campus.", "georgia.html", "Georgia")]
    cs = "".join('<div class="col-sm-6 col-xl-3" data-aos="fade-up" data-aos-delay="%d"><a class="ga-card" href="%s"><i class="fa-solid %s"></i><b>%s</b><span>%s</span><span class="link-arrow mt-auto pt-2">%s <i class="fa-solid fa-arrow-right"></i></span></a></div>' % (i * 70, u(h), ic, e(t), e(dsc), e(lbl)) for i, (ic, t, dsc, h, lbl) in enumerate(cards))
    return ('<section class="sec"><div class="container">%s<div class="row g-3">%s</div></div></section>'
            % (sec_head("Wherever your campus is", "Built for Colleges <span class=\"grad\">Across the U.S.</span>", "LioraAI works with any state’s rules and any major student information system, so the same evaluation engine serves a community college in one state and a university system in another.", center=True), cs))

GA_CALLOUT = {
    "transfer-credit-intelligence": ("georgia/transfer-credit-evaluation.html", "Evaluating TCSG or USG transcripts in Georgia?", "See how LioraAI applies Core IMPACTS domains and the TCSG–USG agreement."),
    "freshman-intelligence": ("georgia/freshman-transcript-evaluation.html", "Reviewing Georgia freshman transcripts?", "Weighted GPAs, Dual Enrollment credit and the HOPE GPA, handled consistently."),
    "veterans": ("georgia/military-transcript-evaluation.html", "Serving students from Georgia’s military bases?", "JST and CCAF evaluation for Fort Benning, Fort Gordon, Fort Stewart, Robins and Moody."),
    "prior-learning-assessment": ("georgia.html", "A Georgia institution?", "Meet our team in metro Atlanta for an on-campus demo."),
    "athletics": ("georgia.html", "A Georgia institution?", "Meet our team in metro Atlanta for an on-campus demo."),
    "degree-pathway": ("georgia/transfer-credit-evaluation.html", "Georgia transfer students asking “will my credits transfer?”", "See how pathways work with USG and TCSG rules."),
    "mobility": ("georgia/transfer-credit-evaluation.html", "Mapping TCSG-to-USG transfer pathways?", "Mobility Intelligence for Georgia partnerships."),
}
def ga_callout(slug):
    href, t, d = GA_CALLOUT[slug]
    return ('<section class="sec-sm" style="padding:0 0 40px"><div class="container"><a class="ga-callout" href="%s"><i class="fa-solid fa-location-dot"></i><span><b>%s</b>%s</span><span class="link-arrow">Georgia &amp; Atlanta <i class="fa-solid fa-arrow-right"></i></span></a></div></section>'
            % (u(href), e(t), e(d)))
