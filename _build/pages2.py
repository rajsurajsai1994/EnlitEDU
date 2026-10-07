# -*- coding: utf-8 -*-
import re, os, json, html as _html
from core import *
from pages import (BLOG, STORIES, story_card, post_card, posts_row, which_module, arrow, slugify, MOD_IMG, proof_block, families_html)
from data_modules import MODULES, BY_SLUG, FOOTNOTE
from data_more import SOLUTIONS, AUDIENCES, GLOSSARY, FAQ_HUB

SRC = r"C:\Users\SurajPaluri\Downloads\Enlitedu_Website\src"

def simple_hero(crumb, eb, h1, sub, img_key=None, extra=""):
    vis = ""
    col = "col-lg-8"
    if img_key:
        col = "col-lg-6"
        vis = '<div class="col-lg-6"><div class="visual"><div class="ph">%s</div>%s</div></div>' % (img(img_key, 900, eager=True, ratio=(4, 3.3)), extra)
    return ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="%s">%s<h1>%s</h1><p class="sub">%s</p></div>%s</div></div></section>'
            % (crumbs(crumb), col, eyebrow(eb), h1, sub, vis))

# ===================================================================== PLATFORM
def build_platform():
    path = "platform.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Platform", None)], "The LioraAI platform", "One Evaluation Engine. <span class=\"accent\">Seven Modules.</span>",
                       "Every way a student brings credit to your institution, evaluated with one set of your rules, approved by your people and written back to your SIS.", "team-collab",
                       float_card("fa-layer-group", "blue", "7 modules, 1 engine", "Shared rules, queue and audit trail", "fc-a"))
    fams = families_html()
    shared = [("fa-scale-balanced", "Rules engine", "Transfer policy, articulation agreements, GPA conversion and CPL frameworks, configured once and versioned."),
              ("fa-list-check", "One review queue", "Every credit type in one place, routed by confidence, role and department."),
              ("fa-fingerprint", "Audit trail", "Evidence, rule version, recommendation and approver recorded for every decision."),
              ("fa-database", "SIS write-back", "Approved decisions post to Banner, Colleague, Workday Student, PeopleSoft or Jenzabar."),
              ("fa-chart-line", "Analytics", "Turnaround, volume, exceptions, credit loss and pathways by term."),
              ("fa-shield-halved", "Security", "FERPA-aligned processing, encryption, SSO and role-based access.")]
    sh = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d"><div class="feature"><span class="ico"><i class="fa-solid %s"></i></span><div><h4>%s</h4><p>%s</p></div></div></div>' % ((i % 3) * 80, a, b, c) for i, (a, b, c) in enumerate(shared))
    body = (hero + '<section class="sec"><div class="container">%s%s<div class="mt-5">%s</div></div></section>' % (sec_head("Modules", "Pick What You Need, <span class=\"grad\">Add the Rest</span> Later", "", center=True), fams, which_module())
            + '<section class="sec dark"><div class="container">%s<div class="row g-5">%s</div></div></section>' % (sec_head("Shared foundation", "What Every Module <span class=\"grad\">Shares</span>", "", center=True), sh)
            + '<section class="sec-sm"><div class="container">%s%s</div></section>' % (sec_head("Integrations", "Works With the Systems <span class=\"grad\">You Run</span>", "", center=True), integrations_strip())
            + testimonials_section(dark=False) + cta_band())
    schema = [breadcrumb([("Home", "index.html"), ("Platform", path)]),
              {"@type": "CollectionPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": "LioraAI platform", "about": {"@id": BASE + "/#lioraai"},
               "hasPart": [{"@id": BASE + "/%s.html#software" % m["slug"]} for m in MODULES]}]
    page(path, "LioraAI Platform | 7 Modules for Credit Evaluation | EnlitEDU",
         "One evaluation engine, seven modules: transfer credit, first-year GPA, CPL/PLA, JST/military, NCAA progress-toward-degree, degree pathways and transfer analytics.", body, schema=schema, active="products")

# ===================================================================== HOW IT WORKS
def build_how():
    path = "how-it-works.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Platform", "platform.html"), ("How LioraAI works", None)], "How LioraAI works",
                       "AI That Shows Its Work, <span class=\"accent\">and Waits for Your Approval</span>",
                       "LioraAI drafts every credit decision with the evidence behind it. Your evaluators and faculty make the call. Here is exactly what happens to a transcript.", "registrar-docs",
                       float_card("fa-user-check", "ok", "Human-approved", "Every decision reviewed by your staff", "fc-a"))
    steps = BY_SLUG["articulate"]["steps"]
    detail = [
        "Transcripts arrive by upload, email inbox, SFTP or electronic exchange (EDI/SPEEDE, PESC XML). Scanned and photographed documents are read with document AI tuned for academic records.",
        "LioraAI identifies the institution, terms, courses, grades, credit units and repeats, then normalizes grading scales and credit systems, including quarter hours and international formats.",
        "Each course is compared with your catalog using course descriptions from a corpus of more than a million, your articulation agreements and your evaluators’ past decisions. Your transfer policy is applied: grade minimums, residency, caps and course age.",
        "Recommendations above your confidence threshold go to a reviewer for one-click approval. Anything uncertain is flagged with the reason and routed to the right evaluator or faculty member.",
        "Approved decisions post to your SIS through API or SFTP, and the full record (evidence, rule version, recommendation, approver) is stored in the audit trail.",
    ]
    rows = "".join('<div class="row g-4 align-items-center mb-5" data-aos="fade-up"><div class="col-md-2"><div class="step" style="padding:0"><div class="num" style="margin:0"><i class="fa-solid %s"></i></div></div></div>'
                   '<div class="col-md-10"><h3>%d. %s</h3><p class="mb-0">%s</p></div></div>' % (ic, i + 1, t, detail[i]) for i, (ic, t, d) in enumerate(steps))
    ai_vs = ('<div class="row g-4"><div class="col-md-6" data-aos="fade-up"><div class="card-x"><div class="ico"><i class="fa-solid fa-microchip"></i></div><h3>What LioraAI does</h3><ul class="check-list">'
             '<li>Reads and normalizes transcripts in any format</li><li>Researches course descriptions and ACE recommendations</li><li>Applies your documented rules consistently</li><li>Drafts recommendations with evidence and confidence</li><li>Records everything in the audit trail</li></ul></div></div>'
             '<div class="col-md-6" data-aos="fade-up" data-aos-delay="100"><div class="card-x"><div class="ico gold"><i class="fa-solid fa-user-tie"></i></div><h3>What your people do</h3><ul class="check-list">'
             '<li>Set and own the rules and agreements</li><li>Approve, edit or decline every recommendation</li><li>Make judgment calls on unusual coursework</li><li>Handle appeals with the full record in hand</li><li>Decide whether LioraAI learns from their decisions</li></ul></div></div></div>')
    faqs = FAQ_HUB[1][1] + [FAQ_HUB[3][1][2]]
    body = (hero + '<section class="sec"><div class="container">%s%s</div></section>' % (sec_head("Step by step", "From Upload to Posted Credit", "", center=True), rows)
            + '<section class="sec tint"><div class="container">%s%s</div></section>' % (sec_head("Human in the loop", "Clear Lines Between the AI <span class=\"grad\">and Your Team</span>", "", center=True), ai_vs)
            + '<section class="sec dark"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-5" data-aos="fade-up">%s<h2>See a Real <span class="grad">Evaluation</span></h2><p>This is what an evaluator sees: each incoming course, the suggested equivalent, and a clear status. Click any row in the product to see the evidence behind it.</p>%s</div><div class="col-lg-7" data-aos="fade-left">%s</div></div></div></section>'
              % (eyebrow("The review screen"), '<a class="btn-x btn-gold mt-3" href="https://www.youtube.com/watch?v=Ti6YBv2R_Gc" data-video="Ti6YBv2R_Gc"><i class="fa-solid fa-play"></i> Watch the 2-minute overview</a>', BY_SLUG["articulate"]["mock"]())
            + faq_block(faqs, title="Questions About the AI", side_img="presenter") + cta_band())
    schema = [breadcrumb([("Home", "index.html"), ("Platform", "platform.html"), ("How LioraAI works", path)]),
              {"@type": "HowTo", "name": "How LioraAI evaluates a transcript", "step": [{"@type": "HowToStep", "position": i + 1, "name": t, "text": detail[i]} for i, (_, t, _d) in enumerate(steps)]},
              faq_schema(faqs, path)]
    page(path, "How LioraAI Works | Explainable, Human-Approved Credit Evaluation",
         "See how LioraAI turns any transcript into posted credit: ingest, extract, match to your catalog with your rules, human review, and SIS write-back with a full audit trail.", body, schema=schema, active="products")

# ===================================================================== INTEGRATIONS
def build_integrations():
    path = "integrations.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Platform", "platform.html"), ("Integrations", None)], "Integrations",
                       "Works With the Systems <span class=\"accent\">You Already Run</span>",
                       "LioraAI reads from and writes to your student information system, CRM and degree audit, so evaluated credit lands where your team already works.", "team-collab",
                       float_card("fa-plug", "ok", "Live on Banner", "Roane State · 18 days from kickoff", "fc-a"))
    rows = [("Ellucian Banner", "Student information system", "Banner 9 through the Ethos API (two-way); Banner 8 through scheduled SFTP. Approved transfer credit posts to the transfer articulation tables."),
            ("Ellucian Colleague", "Student information system", "API or SFTP exchange for transcripts, equivalencies and posted credit."),
            ("Workday Student", "Student information system", "Web services integration for external coursework and transfer credit."),
            ("PeopleSoft Campus Solutions", "Student information system", "Integration Broker or file-based exchange for transfer credit rules and results."),
            ("Jenzabar", "Student information system", "API or SFTP exchange for evaluated credit."),
            ("Slate by Technolutions", "Admissions CRM", "Evaluated first-year and transfer data delivered to reader views."),
            ("Common App", "Applications", "Transcript and school report documents ingested for evaluation."),
            ("Salesforce", "CRM", "Evaluation status and estimates available to recruitment and advising."),
            ("DegreeWorks & uAchieve", "Degree audit", "Applicable credit flows into audit; Degree Pathway can sit alongside."),
            ("Compliance Assistant & Teamworks ARMS", "Athletics compliance", "Progress-toward-degree evidence available to compliance workflows."),
            ("Joint Services Transcript (ACE)", "Military records", "JST, CCAF and DD-214 documents with ACE credit recommendation lookup."),
            ("EDI (SPEEDE) & PESC XML", "Electronic transcripts", "Standard electronic transcripts processed without data entry."),
            ("SSO (SAML 2.0)", "Identity", "Single sign-on with your identity provider and role-based access.")]
    tr = "".join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (e(a), e(b), e(c)) for a, b, c in rows)
    table = ('<div class="mock" data-aos="fade-up"><div class="mbar"><i class="d"></i><i class="d"></i><i class="d"></i><span class="fn">supported integrations</span></div>'
             '<div class="mbody mock-wrap"><table style="min-width:680px"><thead><tr><th>System</th><th>Type</th><th>How it connects</th></tr></thead><tbody>%s</tbody></table></div></div>') % tr.replace("<td>", '<td style="white-space:normal;font-family:var(--f-sans);font-size:14.5px">')
    timeline = [("Week 1", "Kickoff", "Integration plan, SSO, data access and rule documentation."), ("Weeks 1–2", "Configure", "Your catalog, transfer policy and agreements loaded and tested."),
                ("Weeks 2–3", "Validate", "Evaluators review LioraAI results on your own recent transcripts."), ("Weeks 3–4", "Go live", "Write-back switched on; training and support handover.")]
    tl = "".join('<div class="ev" data-aos="fade-up"><span class="yr">%s</span><h4>%s</h4><p>%s</p></div>' % (a, b, c) for a, b, c in timeline)
    faqs = FAQ_HUB[2][1]
    body = (hero + '<section class="sec"><div class="container">%s%s</div></section>' % (sec_head("Connected systems", "Systems We <span class=\"grad\">Integrate</span> With", "", center=True), integrations_strip())
            + '<section class="sec tint"><div class="container">%s%s</div></section>' % (sec_head("Details", "How Each <span class=\"grad\">Connection</span> Works", "", center=True), table)
            + '<section class="sec"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-6" data-aos="fade-right">%s<h2>Live in Two to Four <span class="grad">Weeks</span></h2><p class="lead-lg">Standard integrations take two to four weeks; more complex API setups take four to six. Roane State Community College went live on Ellucian Banner in 18 days.</p><div class="timeline mt-4">%s</div></div><div class="col-lg-6">%s</div></div></div></section>'
              % (eyebrow("Implementation"), tl, '<div class="row g-4">%s</div>' % "".join('<div class="col-sm-6">%s</div>' % vt_card(t) for t in TESTIMONIALS if t[0] in ("paul", "jamie")))
            + faq_block(faqs, title="Implementation Questions", side_img="meeting-standing") + cta_band())
    schema = [breadcrumb([("Home", "index.html"), ("Platform", "platform.html"), ("Integrations", path)]), faq_schema(faqs, path)]
    page(path, "LioraAI Integrations | Banner, Colleague, Workday, PeopleSoft, Slate",
         "LioraAI integrates with Ellucian Banner and Colleague, Workday Student, PeopleSoft, Jenzabar, Slate, Common App and degree audit. Live in two to four weeks.", body, schema=schema, active="products")

# ===================================================================== STORIES
def build_stories():
    path = "case-studies.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Customer Stories", None)], "Customer stories", "Results From <span class=\"accent\">Real Campuses</span>",
                       "Community college leaders explain, on video and in numbers, what changed after LioraAI went live.", "campus-columns",
                       float_card("fa-star", "gold", "3 weeks → 2 days", "Roane State evaluation turnaround", "fc-a"))
    bar = ('<div class="filter-bar" data-filter-group="#story-grid" role="group" aria-label="Filter stories">'
           '<button type="button" data-filter="all" aria-pressed="true">All</button><button type="button" data-filter="community-college" aria-pressed="false">Community colleges</button>'
           '<button type="button" data-filter="articulate" aria-pressed="false">Articulate</button><button type="button" data-filter="mobility" aria-pressed="false">Mobility Intelligence</button></div>')
    next_card = ('<div class="story-card" data-tags="all community-college articulate mobility" style="background:var(--navy);color:#c9d3e6;justify-content:center;padding:34px">'
                 '<span class="eyebrow">Your institution next</span><h3 style="color:#fff;font-family:var(--f-serif);font-size:30px">Want to be our next story?</h3>'
                 '<p>Run LioraAI on your own transcripts in a proof-of-concept and see the turnaround for yourself.</p><a class="btn-x btn-gold mt-2" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a></div>') % u("request-demo.html")
    grid = ('<div class="row g-4" id="story-grid"><div class="col-md-6 col-lg-4" data-tags="community-college articulate" data-aos="fade-up">%s</div><div class="col-md-6 col-lg-4" data-tags="community-college mobility" data-aos="fade-up" data-aos-delay="100">%s</div>'
            '<div class="col-md-6 col-lg-4" data-tags="community-college articulate mobility" data-aos="fade-up" data-aos-delay="200">%s</div></div>') % (story_card("roane"), story_card("nashville"), next_card)
    body = (hero + '<section class="sec"><div class="container">%s%s%s</div></section>' % (sec_head("Featured", "Stories by Module and <span class=\"grad\">Institution</span>", "", center=False), bar, grid)
            + testimonials_section(dark=True) + cta_band())
    schema = [breadcrumb([("Home", "index.html"), ("Customer Stories", path)]),
              {"@type": "CollectionPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": "LioraAI customer stories",
               "hasPart": [{"@id": BASE + "/" + STORIES[k]["url"]} for k in STORIES]}] + [video_schema(t) for t in TESTIMONIALS]
    page(path, "LioraAI Customer Stories | Roane State & Nashville State Results",
         "How Roane State cut transcript evaluation from three weeks to two days, and how Nashville State lifted transfer yield 24% with LioraAI. With video interviews.", body, schema=schema, active="customers")

    # ---- Roane State
    p2 = "case-studies/roane-state-community-college.html"; set_depth(p2)
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-7">%s<h1>Roane State Community College Cuts Transcript Evaluation From <span class="accent">Three Weeks to Two Days</span></h1>'
            '<p class="sub">How a Tennessee community college moved its evaluators from research to review with LioraAI Articulate, and went live on Ellucian Banner in 18 days.</p></div>'
            '<div class="col-lg-5"><div class="visual"><div class="ph">%s</div>%s</div></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Customer Stories", "case-studies.html"), ("Roane State", None)]), eyebrow("Customer story · Community college"),
               img("campus-columns", 900, eager=True, alt="Community college campus building", ratio=(4, 3.3)), float_card("fa-bolt", "ok", "90% faster", "Transcript evaluation", "fc-a")))
    glance = ('<aside class="glance"><h3>At a glance</h3><img src="%s" alt="Roane State Community College" style="height:52px;width:auto;margin-bottom:12px">'
              '<div class="big"><div><b>90%%</b><span>faster evaluations</span></div><div><b>2 days</b><span>turnaround, from ~3 weeks</span></div></div>'
              '<dl><dt>Institution</dt><dd>Roane State Community College, Tennessee</dd><dt>Type</dt><dd>Public community college</dd><dt>SIS</dt><dd>Ellucian Banner</dd>'
              '<dt>Modules</dt><dd><a href="%s">LioraAI Articulate</a></dd><dt>Time to go live</dt><dd>18 days, kickoff to production</dd></dl>'
              '<a class="btn-x btn-gold w-100 mt-4" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a></aside>') % (u("assets/img/enlitedu/roane-state-community-college.png"), u("articulate.html"), u("request-demo.html"))
    story = ('<div class="story-body"><h2>The challenge</h2><p class="lead-lg">Like most community colleges, Roane State evaluates a steady flow of transcripts from students bringing credit from other institutions, with peaks before every term.</p>'
             '<p>Each transfer evaluation was researched and keyed by hand. A typical turnaround was about three weeks, which is a long time for a student deciding where to enroll, and it left the records team little room during peak periods. Approved credit then had to be entered into Banner manually.</p>'
             '<h2>The solution</h2><p>Roane State implemented <a href="%s">LioraAI Articulate</a> with a direct Ellucian Banner integration. LioraAI reads each incoming transcript, matches courses to Roane State’s catalog using the college’s own transfer rules and past decisions, and gives evaluators a recommendation to approve, edit or flag.</p>'
             '<p>The integration was completed in 18 days from kickoff to production, with the college’s IT team. Approved decisions now post to Banner without re-keying.</p>'
             '<h2>The results</h2><h3>Evaluation turnaround: about three weeks to two days</h3><p>Evaluators review recommendations instead of researching every course, which the college reports as a 90%% reduction in evaluation time.</p>'
             '<h3>No more double entry</h3><p>Approved transfer credit flows straight into Banner, removing a manual step and a source of errors.</p>'
             '<h3>Consistent, documented decisions</h3><p>Every decision carries its evidence and approver, so the same course is treated the same way every term.</p>'
             '<h2>In their own words</h2><p>Three members of the Roane State team talk about the change: the VP of Student Services &amp; Innovation, the Registrar, and the IT lead who ran the Banner integration.</p>'
             '<div class="row g-4 mt-2">%s</div><p class="note mt-4">%s</p></div>') % (u("articulate.html"), "".join('<div class="col-sm-6 col-lg-4">%s</div>' % vt_card(t) for t in TESTIMONIALS if t[0] in ("jamie", "jessica", "paul")), FOOTNOTE)
    body = (hero + '<section class="sec"><div class="container"><div class="row g-5"><div class="col-lg-8">%s</div><div class="col-lg-4">%s</div></div></div></section>' % (story, glance)
            + posts_row(["how-to-speed-up-transfer-credit-evaluation", "ellucian-banner-integration-transcript-evaluation", "community-college-transfer-student-success"], tint=True) + cta_band())
    schema = [breadcrumb([("Home", "index.html"), ("Customer Stories", "case-studies.html"), ("Roane State Community College", p2)]),
              {"@type": "Article", "@id": BASE + "/" + p2, "headline": "Roane State Community College cuts transcript evaluation from three weeks to two days", "author": {"@id": BASE + "/#organization"},
               "publisher": {"@id": BASE + "/#organization"}, "datePublished": "2026-10-03", "image": BASE + "/assets/img/enlitedu/og-lioraai.jpg",
               "about": [{"@type": "CollegeOrUniversity", "name": "Roane State Community College"}, {"@id": BASE + "/articulate.html#software"}]}] + [video_schema(t) for t in TESTIMONIALS if t[0] in ("jamie", "jessica", "paul")]
    page(p2, "Roane State Community College Case Study | 3 Weeks to 2 Days | LioraAI",
         "Roane State Community College cut transcript evaluation from about three weeks to two days with LioraAI Articulate and went live on Ellucian Banner in 18 days.", body, schema=schema, active="customers", og_type="article")

    # ---- Nashville State
    p3 = "case-studies/nashville-state-community-college.html"; set_depth(p3)
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-7">%s<h1>Nashville State Lifts Transfer Yield <span class="accent">24%% in One Cycle</span></h1>'
            '<p class="sub">How Nashville State Community College used Student Mobility Intelligence to see its transfer pathways clearly and act on them.</p></div>'
            '<div class="col-lg-5"><div class="visual"><div class="ph">%s</div>%s</div></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Customer Stories", "case-studies.html"), ("Nashville State", None)]), eyebrow("Customer story · Community college"),
               img("lecture-laugh", 900, eager=True, alt="Community college students in a lecture hall", ratio=(4, 3.3)), float_card("fa-chart-line", "ok", "+24% transfer yield", "One enrollment cycle", "fc-a")))
    glance = ('<aside class="glance"><h3>At a glance</h3><p style="font-weight:800;color:var(--navy);font-size:18px;margin-bottom:6px">Nashville State Community College</p>'
              '<div class="big"><div><b>+24%%</b><span>transfer yield in one cycle</span></div><div><b>3</b><span>partner pathways mapped</span></div></div>'
              '<dl><dt>Institution</dt><dd>Nashville State Community College, Tennessee</dd><dt>Type</dt><dd>Public community college</dd>'
              '<dt>Modules</dt><dd><a href="%s">Student Mobility Intelligence</a></dd><dt>Focus</dt><dd>Transfer enrollment planning</dd></dl>'
              '<a class="btn-x btn-gold w-100 mt-4" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a></aside>') % (u("mobility.html"), u("request-demo.html"))
    story = ('<div class="story-body"><h2>The challenge</h2><p class="lead-lg">Transfer enrollment depends on knowing where students come from, which pathways work and where credit is being lost. That information was spread across systems and hard to act on.</p>'
             '<p>Enrollment leaders needed a clear, current view of transfer pathways with partner institutions to plan outreach and partnership conversations.</p>'
             '<h2>The solution</h2><p>Nashville State adopted <a href="%s">Student Mobility Intelligence</a>, which combines LioraAI evaluation detail with enrollment data to map transfer pathways, measure credit applied and lost, and highlight where to focus.</p>'
             '<p>Three partner school pathways were mapped in the first cycle, giving the enrollment team shared evidence for planning.</p>'
             '<h2>The results</h2><h3>Transfer yield up 24%% in one cycle</h3><p>With clearer pathway data and faster answers for students, the college reports a 24%% increase in transfer yield in a single enrollment cycle.</p>'
             '<h3>Partnerships grounded in data</h3><p>Mapped pathways give Nashville State and its partners a common picture of how students move and where credit applies.</p>'
             '<h2>In their own words</h2><p>Alexis Pope, Vice President of Student Affairs &amp; Enrollment Management, explains what changed.</p>'
             '<div class="row g-4 mt-2"><div class="col-sm-6 col-lg-5">%s</div></div><p class="note mt-4">%s</p></div>') % (u("mobility.html"), vt_card(TESTIMONIALS[1]), FOOTNOTE)
    body = (hero + '<section class="sec"><div class="container"><div class="row g-5"><div class="col-lg-8">%s</div><div class="col-lg-4">%s</div></div></div></section>' % (story, glance)
            + posts_row(["community-college-transfer-student-success", "will-my-credits-transfer-self-service-answer", "reverse-transfer-associate-degree-explained"], tint=True) + cta_band())
    schema = [breadcrumb([("Home", "index.html"), ("Customer Stories", "case-studies.html"), ("Nashville State Community College", p3)]),
              {"@type": "Article", "@id": BASE + "/" + p3, "headline": "Nashville State lifts transfer yield 24% in one cycle", "author": {"@id": BASE + "/#organization"},
               "publisher": {"@id": BASE + "/#organization"}, "datePublished": "2026-10-03", "image": BASE + "/assets/img/enlitedu/og-lioraai.jpg",
               "about": [{"@type": "CollegeOrUniversity", "name": "Nashville State Community College"}, {"@id": BASE + "/mobility.html#software"}]}, video_schema(TESTIMONIALS[1])]
    page(p3, "Nashville State Case Study: +24% Transfer Yield | LioraAI",
         "Nashville State Community College lifted transfer yield 24% in one cycle with LioraAI Student Mobility Intelligence and mapped three partner transfer pathways.", body, schema=schema, active="customers", og_type="article")

# ===================================================================== ABOUT
def build_about():
    path = "about.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("About", None)], "About EnlitEDU", "Every Student Deserves a Fast, Fair Answer <span class=\"accent\">About Their Credit</span>",
                       "EnlitEDU builds LioraAI so that every registrar’s office can give that answer, consistently and on the record, without adding staff.", "team-hands",
                       float_card("fa-location-dot", "blue", "Cumming, Georgia", "Serving U.S. colleges and universities", "fc-a"))
    mission = ('<section class="sec"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-6" data-aos="fade-right"><div class="img-stack"><div class="a">%s</div><div class="b">%s</div></div></div>'
               '<div class="col-lg-6" data-aos="fade-left">%s<h2>Why We <span class="grad">Exist</span></h2><p class="lead-lg">Transcript evaluation decides whether a student’s past work counts. It is high-stakes, detailed work, and in most offices it is still done by hand.</p>'
               '<p>We started EnlitEDU after years of supporting colleges through student information system projects. We kept seeing the same thing: talented records teams buried in research, students waiting weeks, and the same course evaluated differently depending on who picked up the file.</p>'
               '<p>LioraAI is our answer: software that does the research, applies each institution’s own rules, and leaves every decision with the people accountable for it.</p></div></div></div></section>'
               % (img("grads-selfie", 800, ratio=(4, 4.6)), img("registrar-folder", 480, alt="", ratio=(1, 1)), eyebrow("Our mission")))
    nums = [("1", "M+", "course descriptions in our mapping corpus"), ("60", "s", "or less to evaluate a full transcript"), ("7", "", "LioraAI modules, one engine"), ("18", " days", "fastest go-live on Banner")]
    cells = "".join('<div class="cell"><b>%s<span data-count="%s">%s</span><span class="u">%s</span></b><span>%s</span></div>' % ("<" if n == "60" else "", n, n, s, t) for n, s, t in nums)
    proof = '<section class="sec dark"><div class="container">%s<div class="proof" style="grid-template-columns:repeat(4,minmax(0,1fr))">%s</div></div></section>' % (sec_head("By the numbers", "Built Only for Higher Ed <span class=\"grad\">Credit</span>", "", center=True), cells)
    proof = proof.replace('style="grid-template-columns:repeat(4,minmax(0,1fr))"', 'style="--c:4"')
    values = [("fa-bullseye", "Precision", "We hold our work to the standard of an official academic record."), ("fa-scale-balanced", "Fairness", "One documented rule for every student, so the result never depends on who evaluated it."),
              ("fa-user-check", "People decide", "Software drafts; accountable people approve. Always."), ("fa-lock", "Privacy first", "Student records are never used to train general-purpose AI."),
              ("fa-handshake", "Partnership", "Every feature is shaped with registrars, SCOs and enrollment leaders."), ("fa-seedling", "Access", "Small colleges deserve the same tools as the largest universities.")]
    vals = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d"><div class="card-x"><div class="ico%s"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div></div>' % ((i % 3) * 80, " gold" if i % 2 else "", a, b, c) for i, (a, b, c) in enumerate(values))
    tl = [("2021", "Founded as Anatta IT Solutions", "Enterprise IT consulting and student information system support for colleges."),
          ("2023", "Supporting ERP migrations", "Helping institutions modernize student systems and data across several states."),
          ("2025", "LioraAI beta", "Beta with partner institutions, validating AI-assisted evaluation in live production."),
          ("2025", "LioraAI launches", "First customers go live, including Tennessee community colleges."),
          ("2026", "Seven modules", "Veterans & JST, Athlete Transcripts and Student Degree Pathway join the platform.")]
    tls = "".join('<div class="ev" data-aos="fade-up"><span class="yr">%s</span><h4>%s</h4><p>%s</p></div>' % x for x in tl)
    team = [("chaitanya", "Chaitanya Saripalli", "Founder & CEO", "Founder of Anatta IT Solutions and EnlitEDU. Chaitanya spent years inside the operational realities of enrollment and records teams and built LioraAI to solve them directly."),
            ("sajan", "Sajan Patel", "Business Development", "Sajan works with registrars, VPs and enrollment directors across the U.S. to connect LioraAI’s capabilities to the practical needs of their offices.")]
    tm = "".join('<div class="col-sm-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d"><div class="team-card"><div class="ph">%s</div><div class="c"><h3>%s</h3><p class="role">%s</p><p>%s</p></div></div></div>' % (i * 100, img(k, 400), n, r, b) for i, (k, n, r, b) in enumerate(team))
    tm += '<div class="col-sm-6 col-lg-4" data-aos="fade-up" data-aos-delay="200"><div class="team-card promo" style="background:var(--navy);color:#c9d3e6"><h3 style="color:#fff;font-family:var(--f-serif);font-size:28px">Join us</h3><p>We’re a small team building tools that change how quickly students get credit for their work.</p><a class="link-arrow" href="%s">See careers <i class="fa-solid fa-arrow-right"></i></a></div></div>' % u("careers.html")
    partner = ('<div class="d-flex flex-wrap align-items-center gap-4"><img src="%s" alt="Slate partner badge" style="height:90px;width:auto" loading="lazy"><img src="%s" alt="AICPA SOC" style="height:90px;width:auto;border-radius:12px" loading="lazy"></div>'
               % (u("assets/img/enlitedu/slate-partner-badge.png"), u("assets/img/enlitedu/soc2-aicpa.jpg")))
    body = (hero + mission + proof
            + '<section class="sec"><div class="container">%s<div class="row g-4">%s</div></div></section>' % (sec_head("Our values", "What We <span class=\"grad\">Stand For</span>", "", center=True), vals)
            + '<section class="sec tint"><div class="container"><div class="row g-5"><div class="col-lg-5" data-aos="fade-up">%s<h2>Our <span class="grad">Journey</span></h2><p class="lead-lg">From IT services for colleges to a dedicated platform for academic records.</p>%s</div><div class="col-lg-7"><div class="timeline">%s</div></div></div></div></section>' % (eyebrow("Timeline"), partner, tls)
            + '<section class="sec anchor" id="leadership"><div class="container">%s<div class="row g-4 justify-content-center">%s</div></div></section>' % (sec_head("Leadership", "The People Behind <span class=\"grad\">LioraAI</span>", "", center=True), tm)
            + cta_band(h2="Let’s talk about <span class=\"grad\">your</span> office.", p="Tell us how transcripts move through your institution today. We’ll show you what changes with LioraAI."))
    body = body.replace('style="--c:4"', 'style="grid-template-columns:repeat(4,minmax(0,1fr))"')
    schema = [breadcrumb([("Home", "index.html"), ("About", path)]),
              {"@type": "AboutPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": "About EnlitEDU", "mainEntity": {"@id": BASE + "/#organization"}},
              {"@type": "Person", "name": "Chaitanya Saripalli", "jobTitle": "Founder & CEO", "worksFor": {"@id": BASE + "/#organization"}, "image": BASE + "/assets/img/enlitedu/chaitanya-saripalli.jpg"},
              {"@type": "Person", "name": "Sajan Patel", "jobTitle": "Business Development", "worksFor": {"@id": BASE + "/#organization"}, "image": BASE + "/assets/img/enlitedu/sajan-patel.jpg"}]
    page(path, "About EnlitEDU | The Team Behind LioraAI",
         "EnlitEDU builds LioraAI so every student gets a fast, fair answer about their credit. Our story, values, timeline and leadership.", body, schema=schema, active="about")

# ===================================================================== FORMS
ROLES = ["Registrar / Records", "Transfer credit evaluator", "VP of Enrollment / Student Affairs", "Director of Admissions", "Veteran Services / SCO", "Athletic compliance",
         "CPL / PLA coordinator", "CIO / IT", "Provost / President", "Other"]
def form_html(kind="demo"):
    opts = "".join('<option>%s</option>' % e(r) for r in ROLES)
    mods = "".join('<label><input type="checkbox" name="modules" value="%s"> %s</label>' % (e(m["name"]), e(m["short"])) for m in MODULES)
    demo_extra = ""
    if kind == "demo":
        demo_extra = ('<div class="field"><label for="f-type">Institution type <span class="req">*</span></label><select id="f-type" name="institution_type" required><option value="">Select…</option>'
                      '<option>Community college</option><option>Four-year public university</option><option>Four-year private college or university</option><option>HBCU / MSI</option><option>State system or consortium</option><option>Other</option></select></div>'
                      '<div class="field"><label for="f-sis">Student information system</label><select id="f-sis" name="sis"><option value="">Select…</option><option>Ellucian Banner</option><option>Ellucian Colleague</option><option>Workday Student</option><option>PeopleSoft Campus Solutions</option><option>Jenzabar</option><option>Other / not sure</option></select></div>'
                      '<div class="field full"><label>Modules you’re interested in</label><div class="checks">%s</div></div>') % mods
    title = "Book your 30-minute demo" if kind == "demo" else "Send us a message"
    btn = "Request my demo" if kind == "demo" else "Send message"
    return ('<form class="form-card" data-web3 data-subject="%s" data-redirect="%s" novalidate><h2>%s</h2><p class="muted small">We reply within one business day. Fields marked <span style="color:#c0392b">*</span> are required.</p>'
            '<div class="fgrid"><div class="field"><label for="f-first">First name <span class="req">*</span></label><input id="f-first" name="first_name" autocomplete="given-name" required></div>'
            '<div class="field"><label for="f-last">Last name <span class="req">*</span></label><input id="f-last" name="last_name" autocomplete="family-name" required></div>'
            '<div class="field"><label for="f-email">Work email <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>'
            '<div class="field"><label for="f-inst">Institution <span class="req">*</span></label><input id="f-inst" name="institution" autocomplete="organization" required></div>'
            '<div class="field"><label for="f-role">Your role <span class="req">*</span></label><select id="f-role" name="role" required><option value="">Select…</option>%s</select></div>'
            '<div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>%s'
            '<div class="field full"><label for="f-msg">%s</label><textarea id="f-msg" name="message"></textarea></div></div>'
            '<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
            '<button class="btn-x btn-gold w-100 mt-4" type="submit">%s <i class="fa-solid fa-arrow-right"></i></button><div class="form-msg" role="alert"></div>'
            '<p class="note mt-3 mb-0">By submitting, you agree to our <a href="%s">Privacy Policy</a>. We never sell your information.</p></form>'
            % ("Demo request · enlitedu.com" if kind == "demo" else "Contact · enlitedu.com", u("thank-you.html"), title, opts, demo_extra,
               "Anything we should know? (current process, volume, timeline)" if kind == "demo" else "How can we help?", btn, u("privacy.html")))

def build_demo():
    path = "request-demo.html"; set_depth(path)
    expect = [("fa-file-lines", "Your transcripts, live", "Send a few anonymized transcripts and we’ll run them against your catalog during the call."),
              ("fa-list-check", "The review screen", "See exactly what your evaluators would approve, edit or flag, with the evidence."),
              ("fa-database", "Your SIS write-back", "How approved credit reaches Banner, Colleague, Workday, PeopleSoft or Jenzabar."),
              ("fa-calculator", "Your numbers", "A realistic turnaround and capacity projection for your volume.")]
    ex = "".join('<li><i class="fa-solid %s"></i><span><b>%s</b>%s</span></li>' % x for x in expect)
    left = ('%s<h1 style="font-size:clamp(34px,4vw,52px)">See LioraAI on <span class="accent" style="color:var(--gold)">Your</span> Transcripts</h1>'
            '<p class="sub">A 30-minute demo tailored to your SIS and workflow. No generic slideshow.</p><ul class="expect">%s</ul>'
            '<p style="color:#fff;font-weight:700;margin-bottom:6px">Who should join</p><p>Your registrar or records lead, a transfer evaluator, and someone from IT if you want to talk integration.</p>'
            '<div class="quote-card mt-4">%s<div><b>Hear from Roane State</b><span>Jamie Stringer, VP of Student Services &amp; Innovation</span><br><a href="https://www.youtube.com/watch?v=UUpuMEJX3Tk" data-video="UUpuMEJX3Tk" data-start="6" style="color:var(--gold);font-weight:700;font-size:14px">Watch the interview →</a></div></div>'
            '<div class="footer-badges mt-4"><span><i class="fa-solid fa-shield-halved"></i>FERPA-aligned</span><span><i class="fa-solid fa-lock"></i>SOC 2 program</span><span><i class="fa-solid fa-clock"></i>Reply in 1 business day</span></div>'
            % (eyebrow("Request a demo"), ex, img("jamie", 124, alt="", sizes="62px")))
    body = ('<section class="page-hero on-dark" style="padding-bottom:110px"><div class="container">%s<div class="row g-5 align-items-start"><div class="col-lg-6">%s</div><div class="col-lg-6">%s</div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Request a Demo", None)]), left, form_html("demo")))
    body += logo_marquee()
    schema = [breadcrumb([("Home", "index.html"), ("Request a Demo", path)]), {"@type": "ContactPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": "Request a LioraAI demo"}]
    page(path, "Request a LioraAI Demo | See It on Your Own Transcripts | EnlitEDU",
         "Book a 30-minute LioraAI demo tailored to your SIS. Send a few anonymized transcripts and see them evaluated live, with the review screen and SIS write-back.", body, schema=schema)

def build_contact():
    path = "contact.html"; set_depth(path)
    info = ('%s<h1 style="font-size:clamp(34px,4vw,52px)">Talk to <span style="color:var(--gold)">EnlitEDU</span></h1><p class="sub">Questions about LioraAI, partnerships, press or support. A person reads every message.</p>'
            '<ul class="expect"><li><i class="fa-solid fa-envelope"></i><span><b>Email</b><a href="mailto:%s" style="color:#fff">%s</a></span></li>'
            '<li><i class="fa-solid fa-location-dot"></i><span><b>Office</b>%s<br>%s, %s %s<br><a href="https://www.google.com/maps/search/?api=1&query=3840+Windermere+Pkwy+Suite+403+Cumming+GA+30041" target="_blank" rel="noopener" style="color:var(--gold)">Open in Maps →</a></span></li>'
            '<li><i class="fa-solid fa-clock"></i><span><b>Hours</b>9 AM – 6 PM Eastern, Monday to Friday</span></li>'
            '<li><i class="fa-solid fa-calendar-check"></i><span><b>Want a demo?</b><a href="%s" style="color:var(--gold)">Request a demo instead →</a></span></li></ul>'
            % (eyebrow("Contact"), SITE["email"], SITE["email"], SITE["street"], SITE["city"], SITE["region"], SITE["zip"], u("request-demo.html")))
    body = ('<section class="page-hero on-dark" style="padding-bottom:110px"><div class="container">%s<div class="row g-5 align-items-start"><div class="col-lg-5">%s</div><div class="col-lg-7">%s</div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Contact", None)]), info, form_html("contact")))
    body += faq_block(FAQ_HUB[4][1], title="Before You Reach Out", side_img="leaders-talk")
    schema = [breadcrumb([("Home", "index.html"), ("Contact", path)]), {"@type": "ContactPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": "Contact EnlitEDU"}, faq_schema(FAQ_HUB[4][1], path)]
    page(path, "Contact EnlitEDU | LioraAI Questions, Partnerships & Support",
         "Contact EnlitEDU about LioraAI: email info@enlitedu.com or send a message. Office in Cumming, Georgia; we reply within one business day.", body, schema=schema, active="about")

def build_thanks():
    path = "thank-you.html"; set_depth(path)
    body = ('<section class="page-hero on-dark"><div class="container"><div class="row justify-content-center text-center"><div class="col-lg-8">'
            '<div style="width:84px;height:84px;border-radius:50%%;background:var(--gold);color:var(--navy);display:grid;place-items:center;font-size:34px;margin:0 auto 24px"><i class="fa-solid fa-check"></i></div>'
            '<h1>Thank You. We’ve Got It.</h1><p class="sub mx-auto">A member of the EnlitEDU team will reply within one business day. While you wait, hear from the people already using LioraAI.</p>'
            '<div class="btn-row justify-content-center mt-4"><a class="btn-x btn-gold" href="%s">Back to home</a><a class="btn-x btn-ghost-light" href="%s">Read customer stories</a></div></div></div></div></section>'
            % (u("index.html"), u("case-studies.html"))) + testimonials_section(dark=False)
    page(path, "Thank You | EnlitEDU", "Thanks for contacting EnlitEDU. We reply within one business day.", body, noindex=True)

# ===================================================================== LEGAL (ported)
def _port_main(name):
    s = open(os.path.join(SRC, name + ".njk"), encoding="utf-8").read()
    b = re.search(r"{% block main %}{% raw %}(.*?){% endraw %}", s, re.S).group(1)
    b = re.sub(r"</?main[^>]*>", "", b)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", b, re.S).group(1)
    upd = re.search(r'<p class="updated">(.*?)</p>', b, re.S)
    b = re.sub(r'<div class="eyebrow">.*?</div>', "", b, count=1, flags=re.S)
    b = re.sub(r"<h1[^>]*>.*?</h1>", "", b, count=1, flags=re.S)
    b = re.sub(r'<p class="updated">.*?</p>', "", b, count=1, flags=re.S)
    b = b.replace('src="images/', 'src="assets/img/enlitedu/').replace('class="intro"', 'class="lead-lg"')
    b = b.replace('class="badges"', 'class="d-flex gap-3 flex-wrap my-4"').replace('<div class="note">', '<div class="callout" style="background:var(--blue-50);border-radius:16px;padding:18px 22px;margin:20px 0">')
    b = re.sub(r'href="([a-z\-]+)\.html"', lambda m: 'href="%s"' % u(m.group(1) + ".html"), b)
    b = re.sub(r'<img ', '<img style="height:90px;width:auto;border-radius:10px" ', b)
    return h1, (upd.group(1) if upd else ""), b

def build_legal():
    for name, title, desc, ttl in [("privacy", "Privacy Policy", "How EnlitEDU collects, uses and protects information, including student education records processed for institutions under FERPA.", "Privacy Policy | EnlitEDU"),
                                   ("terms", "Terms of Service", "Terms governing use of the EnlitEDU website and, where no signed agreement applies, the LioraAI platform.", "Terms of Service | EnlitEDU"),
                                   ("security", "Security & Trust", "How LioraAI protects student records: FERPA school-official role, SOC 2 program, DPA, encryption, US hosting and no AI training on student data.", "Security & Trust | FERPA, SOC 2 Program, DPA | EnlitEDU")]:
        path = name + ".html"; set_depth(path)
        h1, upd, b = _port_main(name)
        hero = simple_hero([("Home", "index.html"), (title, None)], "Legal" if name != "security" else "Security & Trust", h1, upd or "", "registrar-desk" if name == "security" else None,
                           float_card("fa-shield-halved", "ok", "FERPA-aligned", "School official under your control", "fc-a") if name == "security" else "")
        body = hero + '<section class="sec"><div class="container"><div class="prose">%s</div></div></section>' % b
        if name == "security":
            body += cta_band(h2="Need our security <span class=\"grad\">package</span>?", p="We provide the SOC 2 report or bridge letter, DPA template, sub-processor list and a completed HECVAT under NDA.", secondary=None)
        page(path, ttl, desc, body, schema=[breadcrumb([("Home", "index.html"), (title, path)])], active="products" if name == "security" else "")

def build_accessibility():
    path = "accessibility.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Accessibility", None)], "Accessibility", "Accessibility Statement", "Last updated: 3 October 2026")
    b = ('<p class="lead-lg">EnlitEDU wants everyone, including students, staff and visitors with disabilities, to be able to use our website and the LioraAI platform.</p>'
         '<h2>Our goal</h2><p>We design and test this website and the LioraAI student-facing views toward the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA. Public institutions in the U.S. have upcoming obligations under the ADA Title II rule, and we build with those requirements in mind.</p>'
         '<h2>What we do</h2><ul><li>Semantic HTML with a logical heading order on every page</li><li>Keyboard access to menus, tabs, accordions and forms, with visible focus</li><li>Text alternatives for meaningful images</li><li>Color contrast that meets AA for body text</li><li>Respect for reduced-motion preferences</li><li>Captions available on our YouTube videos</li></ul>'
         '<h2>Known limitations</h2><p>Some third-party content, such as embedded videos, is controlled by its provider. If anything on this site is hard to use, please tell us and we will provide the information another way.</p>'
         '<h2>Contact us</h2><p>Email <a href="mailto:info@enlitedu.com">info@enlitedu.com</a> with the page and the problem. We aim to respond within two business days. Institutions can request a VPAT for LioraAI.</p>')
    page(path, "Accessibility Statement | EnlitEDU", "EnlitEDU’s accessibility commitment: WCAG 2.1 AA target for this website and LioraAI student views, and how to report a barrier.",
         hero + '<section class="sec"><div class="container"><div class="prose">%s</div></div></section>' % b, schema=[breadcrumb([("Home", "index.html"), ("Accessibility", path)])])

# ===================================================================== GLOSSARY / FAQ
def build_glossary():
    path = "glossary.html"; set_depth(path)
    terms = sorted(GLOSSARY, key=lambda t: t[0].lower())
    names = {slugify(t[0]): t[0] for t in terms}
    letters = sorted(set(t[0][0].upper() for t in terms))
    az = '<nav class="az" aria-label="Jump to letter">%s</nav>' % "".join('<a href="#letter-%s">%s</a>' % (l, l) for l in letters)
    out, cur = "", ""
    for t, d, see in terms:
        L = t[0].upper()
        if L != cur:
            out += '<p class="anchor" id="letter-%s" style="font-family:var(--f-serif);font-size:44px;color:var(--blue);margin:34px 0 0;line-height:1">%s</p>' % (L, L); cur = L
        links = ", ".join('<a href="#%s">%s</a>' % (s, e(names[s])) for s in see if s in names)
        out += '<div class="term" id="%s"><h2>%s</h2><p>%s</p>%s</div>' % (slugify(t), e(t), e(d), '<p class="see muted">See also: %s</p>' % links if links else "")
    hero = simple_hero([("Home", "index.html"), ("Resources", "blog.html"), ("Glossary", None)], "Glossary", "Credit Evaluation Terms, <span class=\"accent\">Defined Plainly</span>",
                       "From ACE recommendations to reverse transfer: short, accurate definitions of the terms registrars, admissions teams and veteran services offices use every day.", "library-red")
    body = hero + '<section class="sec"><div class="container"><div class="row g-5"><div class="col-lg-3"><div style="position:sticky;top:110px">%s<p class="small muted">%d terms</p></div></div><div class="col-lg-9">%s</div></div></div></section>' % (az, len(terms), out) + cta_band()
    schema = [breadcrumb([("Home", "index.html"), ("Glossary", path)]),
              {"@type": "DefinedTermSet", "@id": BASE + "/" + path, "name": "Higher education credit evaluation glossary", "url": BASE + "/" + path,
               "hasDefinedTerm": [{"@type": "DefinedTerm", "@id": BASE + "/" + path + "#" + slugify(t), "name": t, "description": d, "inDefinedTermSet": BASE + "/" + path} for t, d, _ in terms]}]
    page(path, "Credit Evaluation Glossary: Transfer, JST, CPL | EnlitEDU",
         "Plain definitions of transfer credit, articulation, JST, ACE recommendations, CPL/PLA, reverse transfer, progress-toward-degree, FERPA and more.", body, schema=schema, active="resources")

def build_faq():
    path = "faq.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Resources", "blog.html"), ("FAQ", None)], "FAQ", "Straight Answers <span class=\"accent\">Before You Buy</span>",
                       "What registrars, enrollment leaders, IT teams and procurement ask us most about LioraAI.", "leaders-talk")
    allq, groups = [], ""
    for gi, (g, qs) in enumerate(FAQ_HUB):
        allq += qs
        items = "".join('<div class="faq-item%s"><button class="faq-q" type="button" aria-expanded="%s">%s<span class="pm"><i class="fa-solid fa-plus"></i></span></button><div class="faq-a"><div><p>%s</p></div></div></div>'
                        % (" open" if i == 0 else "", "true" if i == 0 else "false", e(q), a) for i, (q, a) in enumerate(qs))
        groups += '<div class="mb-5 anchor" id="%s" data-aos="fade-up"><h2 style="font-size:30px">%s</h2><div class="faq-wrap">%s</div></div>' % (slugify(g), e(g), items)
    toc = "".join('<a class="chip mb-2" href="#%s">%s</a> ' % (slugify(g), e(g)) for g, _ in FAQ_HUB)
    body = hero + '<section class="sec tint"><div class="container"><div class="row g-5"><div class="col-lg-3"><div style="position:sticky;top:110px"><p class="small muted fw-bold">Jump to</p><div class="chips">%s</div></div></div><div class="col-lg-9">%s</div></div></div></section>' % (toc, groups) + cta_band()
    page(path, "LioraAI FAQ | Implementation, AI, FERPA, Pricing | EnlitEDU",
         "Answers about LioraAI: which module you need, how the AI works, implementation time, integrations, FERPA and SOC 2, data use, pricing and demos.",
         body, schema=[breadcrumb([("Home", "index.html"), ("FAQ", path)]), faq_schema(allq, path)], active="resources")

# ===================================================================== SMALL PAGES
def build_small():
    for path, title, eb, h1, sub, ttl, desc, imgk, noidx, extra in [
        ("careers.html", "Careers", "Careers", "Build the Future of <span class=\"accent\">Credit Mobility</span>",
         "EnlitEDU is a small, fast-moving team building tools that change how quickly students get credit for their work. Roles are opening soon.",
         "Careers at EnlitEDU", "Join EnlitEDU, the team behind LioraAI. Based in Cumming, GA, with remote-friendly roles.", "team-collab", False,
         '<p class="lead-lg">We don’t have open postings right now, but we always want to hear from people who care about students and good software.</p><p>Send your résumé and a note about what you’d like to work on to <a href="mailto:info@enlitedu.com?subject=Careers%20at%20EnlitEDU">info@enlitedu.com</a>. The team is based in Cumming, Georgia, and remote-friendly roles are available.</p>'),
        ("events.html", "Events & Webinars", "Events", "Events & <span class=\"accent\">Webinars</span>",
         "We’re building a calendar of webinars and conference sessions for registrars, enrollment leaders and veteran services offices.",
         "Events & Webinars | EnlitEDU", "Upcoming LioraAI webinars and conference appearances for registrars and enrollment leaders.", "presenter", True,
         '<p class="lead-lg">Our first webinars are being scheduled now.</p><p>Meeting at a conference? Email <a href="mailto:info@enlitedu.com">info@enlitedu.com</a> to set a time with the team. In the meantime, <a href="blog.html">read the blog</a> or <a href="case-studies.html">watch customer interviews</a>.</p>'),
    ]:
        set_depth(path)
        hero = simple_hero([("Home", "index.html"), (title, None)], eb, h1, sub, imgk)
        page(path, ttl, desc, hero + '<section class="sec"><div class="container"><div class="prose">%s</div></div></section>' % re.sub(r'href="([a-z\-]+\.html)"', lambda m: 'href="%s"' % u(m.group(1)), extra) + cta_band(),
             schema=[breadcrumb([("Home", "index.html"), (title, path)])], noindex=noidx, active="about")
    # 404
    path = "404.html"; set_depth(path)
    body = ('<section class="page-hero on-dark"><div class="container"><div class="row justify-content-center text-center"><div class="col-lg-8">'
            '<p style="font-family:var(--f-serif);font-size:120px;line-height:1;color:var(--gold);margin:0">404</p><h1>This Page Didn’t Transfer</h1>'
            '<p class="sub mx-auto">The page you’re looking for has moved or no longer exists. These will get you back on track.</p>'
            '<div class="btn-row justify-content-center mt-4"><a class="btn-x btn-gold" href="%s">Home</a><a class="btn-x btn-ghost-light" href="%s">Products</a><a class="btn-x btn-ghost-light" href="%s">Blog</a><a class="btn-x btn-ghost-light" href="%s">Contact</a></div></div></div></div></section>'
            % (u("index.html"), u("platform.html"), u("blog.html"), u("contact.html")))
    page(path, "Page Not Found | EnlitEDU", "The page you were looking for could not be found.", body, noindex=True)
