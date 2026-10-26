# -*- coding: utf-8 -*-
"""News: Tennessee Board of Regents selects LioraAI (announcement page, NewsArticle schema)."""
import datetime
from core import *
from data_tbr import TBR, TBR_COLLEGES, NEWS_PATH, NEWS_DATE, NATIONWIDE_STATES

TITLE = "Tennessee Board of Regents Selects LioraAI for 11 Community Colleges"
DESC = "The Tennessee Board of Regents has selected LioraAI, EnlitEDU’s AI transcript evaluation software, for 11 community colleges across the College System of Tennessee."

def news_faqs():
    names = ", ".join(n.replace(" Community College", "") for n, _, _, _ in TBR_COLLEGES[:-1]) + " and " + TBR_COLLEGES[-1][0].replace(" Community College", "")
    return [
        ("Which Tennessee colleges use LioraAI?", "The Tennessee Board of Regents has selected LioraAI for 11 community colleges across the College System of Tennessee: %s. Roane State and Nashville State are already live." % names),
        ("What is the Tennessee Board of Regents?", "The Tennessee Board of Regents (TBR) governs the College System of Tennessee, the state’s public community colleges and colleges of applied technology. The system includes 13 community colleges."),
        ("What does LioraAI do for TBR colleges?", "LioraAI evaluates incoming transcripts against each college’s own catalog, articulation agreements and state rules, drafts a credit decision with the evidence, and lets staff and faculty approve it before credit posts to the student information system."),
        ("Does each college keep its own transfer rules?", "Yes. Each college keeps its own equivalencies, reviewers and approvals, while shared Tennessee transfer rules can be applied the same way at every campus."),
        ("Does EnlitEDU work with colleges outside Tennessee?", "Yes. Beyond Tennessee, EnlitEDU works with HBCUs, universities, technical and community colleges in %s, and serves institutions nationwide." % NATIONWIDE_STATES),
    ]

def build_tbr_news():
    path = NEWS_PATH; set_depth(path); url = BASE + "/" + path
    d = datetime.date.fromisoformat(NEWS_DATE); date_h = d.strftime("%B %d, %Y").replace(" 0", " ")
    hero = ('<section class="page-hero on-dark"><div class="container"><div class="article">%s%s<h1 style="font-size:clamp(32px,4vw,50px)">%s</h1>'
            '<p class="sub">The College System of Tennessee brings LioraAI, EnlitEDU’s AI transcript evaluation software, to 11 community colleges from Memphis to Blountville.</p>'
            '<div class="meta-row"><span><i class="fa-solid fa-calendar-days"></i> %s</span><span><i class="fa-solid fa-newspaper"></i> Announcement</span><span><i class="fa-solid fa-location-dot"></i> Tennessee</span></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("News", None)]), eyebrow("News · Tennessee Board of Regents"), e(TITLE), date_h))
    cards = "".join('<li class="tbr-li"><img src="%s" alt="%s" loading="lazy"><span><b>%s</b><small><i class="fa-solid fa-location-dot"></i> %s, Tennessee</small></span><a href="%s" target="_blank" rel="noopener" aria-label="%s website">Website <i class="fa-solid fa-arrow-up-right-from-square"></i></a></li>'
                    % (u("assets/img/enlitedu/" + lg), e(n), e(n), e(c), w, e(n)) for n, c, lg, w in TBR_COLLEGES)
    body_html = (
        '<div class="article-body">'
        '<p class="lead-lg"><strong>%s</strong> EnlitEDU today announced that the <a href="%s" target="_blank" rel="noopener">Tennessee Board of Regents</a> (TBR), which governs the College System of Tennessee, has selected LioraAI for 11 of the system’s community colleges.</p>'
        '<p>LioraAI is EnlitEDU’s AI transcript evaluation software. It reads incoming transcripts, applies each college’s own catalog, articulation agreements and state transfer rules, and gives staff a documented recommendation to approve, so students get a credit answer in minutes instead of waiting weeks.</p>'
        '<h2>Which colleges are included?</h2><ul class="tbr-list">%s</ul>'
        '<h2>What is the Tennessee Board of Regents?</h2>'
        '<p>The Tennessee Board of Regents governs the College System of Tennessee, the state’s public community colleges and colleges of applied technology. The system includes 13 community colleges serving students across the state, from Memphis in the west to the Tri-Cities in the east.</p>'
        '<h2>What LioraAI brings to the system</h2><ul>'
        '<li><strong>One engine, each college’s rules.</strong> Every college keeps its own equivalencies, reviewers and approvals, while shared Tennessee transfer rules apply the same way at every campus.</li>'
        '<li><strong>Consistent answers for students.</strong> A course from a partner college is evaluated the same way wherever a student applies within the system.</li>'
        '<li><strong>People stay in charge.</strong> LioraAI drafts each decision with the evidence; staff and faculty approve every one.</li>'
        '<li><strong>Credit posted to the SIS.</strong> Approved credit writes back to the student information system without manual re-keying.</li></ul>'
        '<h2>Already proven in Tennessee</h2>'
        '<p>Two TBR colleges are already live. <a href="%s">Roane State Community College</a> cut transcript evaluation from about three weeks to two days and went live on Ellucian Banner in 18 days. '
        '<a href="%s">Nashville State Community College</a> cut per-transcript evaluation time from about 15 minutes to 2 minutes after going live across the institution in July 2026.</p>'
        '<h2>About EnlitEDU</h2>'
        '<p>EnlitEDU builds LioraAI, AI transcript evaluation software for colleges and universities across the United States, including LioraAI Transfer Credit Intelligence and LioraAI Freshman Intelligence. '
        'Beyond Tennessee, EnlitEDU works with HBCUs, universities, technical and community colleges in %s. The company is headquartered in Cumming, Georgia.</p>'
        '<p><strong>Media contact:</strong> <a href="mailto:info@enlitedu.com">info@enlitedu.com</a></p>'
        '<div class="callout" style="display:flex;gap:18px;align-items:center;flex-wrap:wrap"><div style="flex:1;min-width:220px"><strong>Running a multi-campus system?</strong> See how LioraAI applies shared rules while each campus keeps its own decisions.</div>'
        '<a class="btn-x btn-navy btn-sm" href="%s">LioraAI for state systems <i class="fa-solid fa-arrow-right"></i></a></div>'
        '<h2>Frequently asked questions</h2><div class="faq-wrap">%s</div></div>'
        % ("Tennessee, %s." % date_h, TBR["url"], cards, u("case-studies/roane-state-community-college.html"), u("case-studies/nashville-state-community-college.html"),
           NATIONWIDE_STATES, u("who-we-serve/state-systems.html"),
           "".join('<div class="faq-item%s"><button class="faq-q" type="button" aria-expanded="%s">%s<span class="pm"><i class="fa-solid fa-plus"></i></span></button><div class="faq-a"><div><p>%s</p></div></div></div>'
                   % (" open" if i == 0 else "", "true" if i == 0 else "false", e(q), e(a)) for i, (q, a) in enumerate(news_faqs()))))
    logo_band = ('<div class="article" style="margin-top:-60px;position:relative;z-index:2"><div class="tbr-banner"><img src="%s" alt="Tennessee Board of Regents, the College System of Tennessee" width="394" height="60"><span><b>11</b> community colleges across the College System of Tennessee</span></div></div>'
                 % u("assets/img/enlitedu/" + TBR["logo"]))
    page_body = (hero + logo_band + '<section class="sec" style="padding-top:36px"><div class="container"><div class="article">%s</div></div></section>' % body_html
                 + cta_band(h2="Bring LioraAI to <span class=\"grad\">your</span> campus.", p="See how one engine with your own rules turns weeks of transcript evaluation into same-week credit decisions."))
    college_nodes = [{"@type": "CollegeOrUniversity", "name": n, "url": w, "address": {"@type": "PostalAddress", "addressLocality": c, "addressRegion": "TN", "addressCountry": "US"}}
                     for n, c, lg, w in TBR_COLLEGES]
    schema = [breadcrumb([("Home", "index.html"), ("News", path)]),
              {"@type": "NewsArticle", "@id": url + "#article", "headline": TITLE, "description": DESC, "url": url, "mainEntityOfPage": url,
               "datePublished": NEWS_DATE, "dateModified": NEWS_DATE, "inLanguage": "en-US",
               "author": {"@id": BASE + "/#organization"}, "publisher": {"@id": BASE + "/#organization"},
               "image": [BASE + "/assets/img/enlitedu/og-lioraai.jpg", BASE + "/assets/img/enlitedu/" + TBR["logo"]],
               "about": [{"@type": "EducationalOrganization", "name": TBR["name"], "alternateName": TBR["system"], "url": TBR["url"], "sameAs": [TBR["url"]]},
                         {"@id": BASE + "/#lioraai"}],
               "mentions": college_nodes,
               "keywords": "Tennessee Board of Regents, College System of Tennessee, TBR community colleges, transcript evaluation software, transfer credit evaluation, LioraAI"},
              {"@type": "ItemList", "@id": url + "#colleges", "name": "TBR community colleges using LioraAI", "numberOfItems": len(TBR_COLLEGES),
               "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": w} for i, (n, c, lg, w) in enumerate(TBR_COLLEGES)]},
              faq_schema(news_faqs(), path)]
    page(path, "TBR Selects LioraAI for 11 Tennessee Community Colleges", DESC, page_body, schema=schema, active="resources", og_type="article")
