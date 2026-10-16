# -*- coding: utf-8 -*-
import re
from core import *
from data_modules import MODULES, BY_SLUG, FOOTNOTE, CARD, HIDDEN
from data_more import SOLUTIONS, AUDIENCES, GLOSSARY, FAQ_HUB, NSC, GAO, WEEKS

MOD_IMG = {"transfer-credit-intelligence": "registrar-docs", "freshman-intelligence": "student-table", "pla": "adult-learner", "veterans": "veteran-smile",
           "athletics": "athlete-runner", "degree-pathway": "student-backpack", "mobility": "cabinet"}
BLOG = {}  # filled by build.py: slug -> dict(title, desc, date, tag, img)

def slugify(s):
    s = s.lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def arrow(label, href):
    return '<a class="link-arrow" href="%s">%s <i class="fa-solid fa-arrow-right"></i></a>' % (u(href), label)

def stat_cards(stats, cols="col-md-4"):
    out = ""
    for i, (n, t, src) in enumerate(stats):
        out += ('<div class="%s" data-aos="fade-up" data-aos-delay="%d"><div class="stat-card"><div class="n%s">%s</div><p>%s</p><cite>Source: %s</cite></div></div>'
                % (cols, i * 100, " gold" if i == 1 else "", n, t, src))
    return out

def post_card(slug, h=3):
    p = BLOG[slug]
    return ('<a class="post-card" href="%s" data-tags="%s"><div class="thumb">%s<span class="tag">%s</span></div><div class="body">'
            '<span class="meta">%s · %s min read</span><h%d>%s</h%d><p>%s</p><span class="link-arrow mt-auto">Read the article <i class="fa-solid fa-arrow-right"></i></span></div></a>'
            % (u("blog/%s.html" % slug), p["filter"], img(p["img"], 800, alt="", sizes="(max-width: 767px) 100vw, 33vw"), e(p["tag"]), p["date_h"], p["mins"], h, e(p["title"]), h, e(p["desc"])))

def posts_row(slugs, eb="Further reading", h2="Guides from the <span class=\"grad\">registrar’s</span> desk", tint=False):
    cards = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (i * 100, post_card(s)) for i, s in enumerate(slugs) if s in BLOG)
    return ('<section class="sec%s"><div class="container"><div class="d-flex flex-wrap justify-content-between align-items-end gap-3 mb-5">'
            '<div class="sec-head mb-0" data-aos="fade-up">%s<h2>%s</h2></div>%s</div><div class="row g-4">%s</div></div></section>'
            % (" tint" if tint else "", eyebrow(eb), h2, arrow("All articles", "blog.html"), cards))

STORIES = {
 "roane": dict(url="case-studies/roane-state-community-college.html", name="Roane State Community College", logo="roane-state-community-college.png",
               title="Roane State Community College cuts transcript evaluation from three weeks to two days",
               kpis=[("90%", "faster evaluations"), ("18 days", "to go live on Banner")], img="campus-columns", tags="transfer-credit-intelligence community-college"),
 "nashville": dict(url="case-studies/nashville-state-community-college.html", name="Nashville State Community College", logo=None,
                   title="Nashville State cuts transfer evaluation from 15 minutes to 2 per transcript",
                   kpis=[("-87%", "per-transcript time"), ("-56%", "approval turnaround")], img="lecture-laugh", tags="transfer-credit-intelligence community-college"),
}
def story_card(k):
    s = STORIES[k]
    logo = ('<span class="logo"><img src="%s" alt="%s"></span>' % (u("assets/img/enlitedu/" + s["logo"]), e(s["name"]))) if s["logo"] else \
           '<span class="logo" style="font-weight:800;color:var(--navy);font-size:14px">%s</span>' % e(s["name"])
    kp = "".join('<div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in s["kpis"])
    return ('<a class="story-card" href="%s" data-tags="%s"><div class="thumb">%s%s</div><div class="body"><span class="small muted">%s · Community college</span>'
            '<h3>%s</h3><div class="kpis">%s</div><span class="link-arrow">Read the story <i class="fa-solid fa-arrow-right"></i></span></div></a>'
            % (u(s["url"]), s["tags"], img(s["img"], 800, alt="", sizes="(max-width: 767px) 100vw, 50vw"), logo, e(s["name"]), e(s["title"]), kp))

AUD_CARD = {
    "community-colleges": "Transfer-in, transfer-out, CPL and military credit, with one set of your rules.",
    "four-year-universities": "First-year GPA standardization and transfer admit evaluation in one engine.",
    "hbcus-and-msis": "Fair, consistent evaluation for transfer, first-generation and adult learners.",
    "state-systems": "One set of transfer rules and one mobility view across every campus.",
}

def families_html():
    def card(m, cls, d):
        return '<div class="%s" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (cls, d, mod_card(m["slug"] + ".html", m["cat"], m["name"], CARD[m["slug"]], m["icon"], MOD_IMG[m["slug"]]))
    ce = [m for m in MODULES if m["family"] == "Credit Evaluation"]
    cc = [m for m in MODULES if m["family"] == "Compliance & Certification"]
    sp = [m for m in MODULES if m["family"] == "Student Pathways"]
    head = lambda f, s: '<div class="family-head"><h3>%s</h3><span>%s</span></div>' % (e(f), e(s))
    row1 = '<div class="family">%s<div class="row g-4">%s</div></div>' % (head("Credit Evaluation", "Every way a student brings credit to your door"), "".join(card(m, "col-md-6 col-lg-3", i * 80) for i, m in enumerate(ce)))
    if cc:
        row2 = ('<div class="row g-4 fam-row"><div class="col-lg-4"><div class="family">%s<div class="row g-4">%s</div></div></div>'
                '<div class="col-lg-8"><div class="family">%s<div class="row g-4">%s</div></div></div></div>'
                % (head("Compliance & Certification", "Documentation that stands up to review"), "".join(card(m, "col-12", 0) for m in cc),
                   head("Student Pathways", "Visibility for students, advisors and leaders"), "".join(card(m, "col-md-6", i * 80) for i, m in enumerate(sp))))
    else:
        row2 = ('<div class="family fam-row">%s<div class="row g-4">%s</div></div>'
                % (head("Student Pathways", "Visibility for students, advisors and leaders"), "".join(card(m, "col-md-6", i * 80) for i, m in enumerate(sp))))
    return row1 + row2

def which_module():
    rows = [("Students coming to college for the first time from high school, homeschool or a GED (first-year / freshman)", "freshman-intelligence.html", "LioraAI Freshman Intelligence"),
            ("Anyone bringing credit from another college or university, whatever their class standing", "transfer-credit-intelligence.html", "LioraAI Transfer Credit Intelligence"),
            ("Service members and veterans with a JST, CCAF transcript or DD-214", "veterans.html", "Veterans & JST"),
            ("Adult learners with certifications, work experience, exams or a portfolio", "pla.html", "Prior Learning Assessment")]
    r = "".join('<div class="row-q"><span>%s</span><a href="%s">%s →</a></div>' % (a, u(h), e(n)) for a, h, n in rows)
    return ('<div class="which" data-aos="fade-up"><h3>Which module do I need?</h3><p style="color:#c9d3e6">Plain definitions, because community colleges and universities don’t always use the same words.</p>%s</div>' % r)

# ===================================================================== HOME
FLAGSHIP = ("transfer-credit-intelligence", "freshman-intelligence")
FLAG = {
    "transfer-credit-intelligence": ("Automated transfer credit evaluation", "Evaluate every transfer transcript against your catalog, articulation agreements and state rules, then post approved credit to your SIS.",
                                     ["Maps any college transcript to your courses, with the evidence shown", "Applies state frameworks and your own equivalencies", "Writes approved credit to Banner, Colleague, Workday Student or PeopleSoft"],
                                     ("15 min → 2 min", "per transcript at Nashville State")),
    "freshman-intelligence": ("High school transcript automation", "Standardize every freshman applicant’s high school transcript with your documented GPA and rigor rules, the same way every time.",
                              ["Converts 4.0, 5.0, 6.0 and 100-point scales with one rule", "Recognizes AP, IB, Honors and dual enrollment rigor", "Sends clean records to Slate and your SIS"],
                              ("1 rule", "applied the same way to every applicant")),
}

def flagship_html():
    cards = ""
    for i, k in enumerate(FLAGSHIP):
        m = BY_SLUG[k]; cat, desc, bullets, (pn, pl) = FLAG[k]
        cards += ('<div class="col-lg-6" data-aos="fade-up" data-aos-delay="%d"><a class="flag-card" href="%s"><div class="ph">%s</div><div class="c">'
                  '<span class="cat-lbl">%s</span><h3>%s</h3><p>%s</p><ul class="flag-list">%s</ul>'
                  '<div class="flag-proof"><b>%s</b><span>%s</span></div><span class="link-arrow">Explore %s <i class="fa-solid fa-arrow-right"></i></span></div></a></div>'
                  % (i * 100, u(k + ".html"), img(MOD_IMG[k], 800, alt="", sizes="(max-width: 991px) 100vw, 50vw", ratio=(16, 9)),
                     e(cat), e(m["name"]), e(desc), "".join("<li>%s</li>" % e(b) for b in bullets), pn, e(pl), e(m["short"])))
    return ('<section class="sec"><div class="container">%s<div class="row g-4">%s</div></div></section>'
            % (sec_head("Start with what’s proven", "Two Products That Move Credit <span class=\"grad\">Faster</span>",
                        "Most institutions start with transfer and high school transcripts, where the backlog is biggest. Both run on one engine with your rules and your approval.", center=True), cards))

def state_story_html(variant="home"):
    pts = [("fa-sitemap", "Shared rules, local decisions", "System-wide transfer policy, common course numbering and pathways apply everywhere, while each campus keeps its own equivalencies and approvals."),
           ("fa-equals", "The same course, the same answer", "One rules engine means a course from a partner college is evaluated the same way at every campus in the system."),
           ("fa-users-cog", "Each campus runs its own team", "Institutions manage their own roles and reviewers. Nashville State administrators create their own LioraAI roles with no EnlitEDU configuration step."),
           ("fa-chart-bar", "One system-wide view", "Decisions, turnaround and credit applied roll up across campuses for the system office.")]
    cards = "".join('<div class="col-sm-6" data-aos="fade-up" data-aos-delay="%d"><div class="card-x"><div class="ico"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div></div>' % (i * 70, ic, t, dsc) for i, (ic, t, dsc) in enumerate(pts))
    head = ("For state systems and multi-campus institutions", "Proven at Tennessee Community Colleges. <span class=\"grad\">Built for Systems.</span>") if variant == "home" else \
           ("Proof from Tennessee", "Proven on Two Campuses. <span class=\"grad\">Ready for Yours.</span>")
    link = arrow("LioraAI for state systems", "who-we-serve/state-systems.html") if variant == "home" else arrow("Read both customer stories", "case-studies.html")
    return ('<section class="sec tint-2"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-5" data-aos="fade-up">%s<h2>%s</h2>'
            '<p class="lede">Roane State Community College and Nashville State Community College, two Tennessee community colleges, run LioraAI on their own catalogs and rules. '
            'The same engine scales across every campus in a system: shared transfer policy where you want consistency, campus decisions where you need them.</p>'
            '<ul class="check-list"><li><span><b>Roane State:</b> live on Ellucian Banner in 18 days; evaluation from three weeks to two days</span></li>'
            '<li><span><b>Nashville State:</b> full institutional go-live in July 2026; 2,158+ transcripts processed by September</span></li></ul>%s</div>'
            '<div class="col-lg-7"><div class="row g-3">%s</div></div></div></div></section>' % (eyebrow(head[0]), head[1], link, cards))

def build_home():
    path = "index.html"; set_depth(path)
    av = "".join(img(k, 92, alt="", sizes="46px") for k in ("jamie", "alexis", "jessica", "paul"))
    orbit = ('<div class="orbit" aria-hidden="true"><svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="96" fill="none" stroke="rgba(255,255,255,.22)" stroke-width=".6" stroke-dasharray="1 3"/>'
             '<circle cx="100" cy="4" r="2.6" fill="#ffd43e"/><circle cx="196" cy="100" r="2" fill="#6b85f8"/><circle cx="32" cy="168" r="2.2" fill="#ffd43e"/><circle cx="18" cy="52" r="1.6" fill="#fff"/><circle cx="170" cy="170" r="1.6" fill="#fff"/></svg></div>')
    hero = ('<section class="hero on-dark"><div class="container"><div class="row align-items-center g-5"><div class="col-lg-6">'
            '%s<h1>From Transcripts to Credit Decisions. <span class="accent">In Minutes, Not Days.</span></h1>'
            '<p class="sub">LioraAI helps admissions and registrar teams evaluate transfer and high school transcripts, apply your institution’s rules and speed up enrollment decisions, with AI doing the work and your staff approving every decision.</p>'
            '<div class="sig-bar"></div><div class="btn-row"><a class="btn-x btn-gold" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a>'
            '<a class="btn-x btn-ghost-light" href="%s">Watch Customer Stories <i class="fa-solid fa-play"></i></a></div>'
            '<div class="proof-line"><div class="avatars">%s</div><span class="proof-pts"><span><b>Nashville State:</b> 15 min → 2 min per transcript</span><span><b>Roane State:</b> 3 weeks → 2 days to evaluate</span></span></div></div>'
            '<div class="col-lg-6"><div class="hero-visual">%s<div class="hero-photo">%s</div>%s%s%s</div></div></div></div></section>'
            % (eyebrow("LioraAI · AI transcript evaluation software for higher education"), u("request-demo.html"), u("case-studies.html") + "#voices", av, orbit,
               img("students-laptop", 900, eager=True, sizes="(max-width: 991px) 100vw, 560px", ratio=(5, 5.6)),
               float_card("fa-circle-check", "ok", "Transcript evaluated", "15 credits ready to post to Banner", "fc-1"),
               float_card("fa-graduation-cap", "gold", "High school GPA standardized", "100-point scale → 3.70 on your rules", "fc-2"),
               float_card("fa-user-check", "blue", "Faculty review", "1 course flagged for a decision", "fc-3")))

    problem = ('<section class="sec"><div class="container"><div class="row align-items-center g-5"><div class="col-lg-5" data-aos="fade-right">'
               '<div class="img-stack"><div class="a">%s</div><div class="b">%s</div><div class="tag"><b>3 wks → 2 days</b><span>Evaluation turnaround at Roane State</span></div></div></div>'
               '<div class="col-lg-7"><div class="sec-head mb-4" data-aos="fade-up">%s<h2>Students Move. Their Credit Should <span class="grad">Too.</span></h2>'
               '<p class="lede">More than a third of students transfer. Veterans bring years of training. Adult learners bring certifications and work experience. Every one of them asks the same question: what counts? The institution that answers first, and fairly, earns the enrollment.</p></div>'
               '<div class="row g-3">%s</div></div></div></div></section>'
               % (img("grads-jump", 800, sizes="(max-width: 991px) 100vw, 40vw", ratio=(4, 4.6)), img("registrar-desk", 480, alt="", sizes="200px", ratio=(1, 1)),
                  eyebrow("Why it matters"), stat_cards([NSC, GAO, WEEKS])))

    tab_btns = tab_panels = ""
    tab_data = [
        ("speed-up-credit-evaluation", "registrar-folder", ("fa-circle-check", "ok", "Queue cleared", "212 evaluations this week"), ["transfer-credit-intelligence", "freshman-intelligence", "veterans"]),
        ("grow-transfer-enrollment", "students-group", ("fa-bolt", "ok", "15 min → 2 min", "Per transcript at Nashville State"), ["degree-pathway", "transfer-credit-intelligence", "mobility"]),
        ("serve-military-and-adult-learners", "veteran-family", ("fa-medal", "gold", "12 credits awarded", "JST evaluated with ACE citations"), ["veterans", "pla"]),
        ("stay-audit-ready", "four-meeting", ("fa-fingerprint", "blue", "Decision recorded", "Evidence, rule and approver logged"), ["transfer-credit-intelligence", "freshman-intelligence", "veterans"]),
        ("improve-completion-and-retention", "grad-woman", ("fa-route", "blue", "4 terms to graduation", "Plan shared with advisor"), ["degree-pathway", "mobility"]),
    ]
    for i, (slug, ik, fc, mods) in enumerate(tab_data):
        s = next(x for x in SOLUTIONS if x["slug"] == slug)
        short = {"speed-up-credit-evaluation": "Speed Up Evaluation", "grow-transfer-enrollment": "Grow Transfer Enrollment", "serve-military-and-adult-learners": "Serve Military & Adult Learners", "stay-audit-ready": "Stay Audit-Ready", "improve-completion-and-retention": "Improve Completion"}[slug]
        tab_btns += '<button class="tab-btn" role="tab" id="tab-%d" aria-controls="tp-%d" aria-selected="%s" tabindex="%d"><i class="fa-solid %s"></i>%s</button>' % (i, i, "true" if i == 0 else "false", 0 if i == 0 else -1, s["icon"], e(short))
        chips = "".join('<a class="chip" href="%s">%s</a>' % (u(BY_SLUG[m]["slug"] + ".html"), e(BY_SLUG[m]["short"])) for m in mods)
        lis = "".join("<li>%s</li>" % b for b in s["bullets"][:3])
        tab_panels += ('<div class="tab-panel%s" role="tabpanel" id="tp-%d" aria-labelledby="tab-%d"%s><div class="row align-items-center g-5"><div class="col-lg-6"><div class="media">%s%s</div></div>'
                       '<div class="col-lg-6"><h3>%s</h3><p class="lead-lg">%s</p><ul class="check-list">%s</ul><p class="small muted mb-2">Modules that do the work</p><div class="chips mb-4">%s</div>%s</div></div></div>'
                       % (" active" if i == 0 else "", i, i, "" if i == 0 else " hidden", img(ik, 900, sizes="(max-width: 991px) 100vw, 50vw", ratio=(16, 12)),
                          float_card(*fc), re.sub(r'<span class="accent">(.*?)</span>', r"\1", s["h1"]), s["sub"], lis, chips, arrow("See how", "solutions/%s.html" % slug)))
    tabs = ('<section class="sec tint"><div class="container">%s<div data-tabs><div class="tabs-nav" role="tablist" aria-label="Outcomes">%s</div>%s</div></div></section>'
            % (sec_head("Solutions by outcome", "One Platform for Every <span class=\"grad\">Credit</span> Decision", "Start with the result you’re accountable for. LioraAI’s modules share one engine, one set of your rules and one audit trail.", center=True), tab_btns, tab_panels))

    expand = [m for m in MODULES if m["slug"] not in FLAGSHIP]
    exp_cards = "".join('<div class="col-md-6 col-lg-3" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (i * 80, mod_card(m["slug"] + ".html", m["cat"], m["name"], CARD[m["slug"]], m["icon"], MOD_IMG[m["slug"]])) for i, m in enumerate(expand))
    modules = ('<section class="sec"><div class="container">%s<div class="row g-4">%s</div><div class="mt-5">%s</div></div></section>'
               % (sec_head("The LioraAI platform", "Expand Across the <span class=\"grad\">Student Journey</span>", "Once transfer and high school transcripts run on LioraAI, the same engine, rules and audit trail extend to military credit, prior learning, degree pathways and transfer analytics.", center=True), exp_cards, which_module()))

    steps = "".join('<div class="step" data-aos="fade-up" data-aos-delay="%d"><div class="num"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div>' % (i * 90, ic, t, d)
                    for i, (ic, t, d) in enumerate(BY_SLUG["transfer-credit-intelligence"]["steps"]))
    how = ('<section class="sec tint-2"><div class="container">%s<div class="steps mb-5">%s</div>'
           '<div class="row align-items-center g-5 mt-4"><div class="col-lg-6" data-aos="fade-right"><div class="sec-head mb-3">%s<h2>A Live Workflow, <span class="grad">Not</span> a Black Box</h2>'
           '<p class="lede">Every suggestion shows its evidence: the matched course descriptions, the rule that applied and your past decisions on the same course. Anything uncertain goes to a person.</p></div>'
           '<ul class="check-list"><li>Your evaluators approve, edit or override every recommendation</li><li>Confidence levels send edge cases to the right reviewer</li><li>Student records never train general-purpose AI models</li></ul>%s</div>'
           '<div class="col-lg-6" data-aos="fade-left">%s</div></div></div></section>'
           % (sec_head("How LioraAI works", "From Transcript to Decision, <span class=\"grad\">Without the Manual Work</span>", "The same flow for transfer and high school transcripts: LioraAI reads the record, applies your rules and hands your team a documented recommendation to approve, then posts the credit to your SIS.", center=True), steps,
              eyebrow("Explainable by design"), arrow("How LioraAI works", "how-it-works.html"), BY_SLUG["transfer-credit-intelligence"]["mock"]()))

    proof_cells = [("1", "M+", "course descriptions in LioraAI’s mapping corpus", "EnlitEDU", ""), ("60", "s", "or less to evaluate a full transcript", "EnlitEDU product measurement", "<"),
                   ("90", "%", "faster transcript evaluation at Roane State Community College", "Reported by Roane State", ""), ("18", " days", "from kickoff to live on Ellucian Banner", "Roane State implementation", ""),
                   ("87", "%", "less time per transcript at Nashville State (15 min to 2 min)", "LioraAI platform data, Sept 2026", ""), ("130", "+", "countries’ transcripts supported, with grading normalized", "EnlitEDU", "")]
    cells = "".join('<div class="cell" data-aos="fade-up" data-aos-delay="%d"><b>%s<span data-count="%s">%s</span><span class="u">%s</span></b><span>%s</span><small>%s</small></div>'
                    % (i * 70, e(pre), n, n, suf, t, src) for i, (n, suf, t, src, pre) in enumerate(proof_cells))
    proof = ('<section class="sec dark"><div class="container">%s<div class="proof">%s</div><p class="note mt-3">%s</p></div></section>'
             % (sec_head("Proof, not promises", "Built Only for Higher Ed <span class=\"grad\">Credit</span>", "LioraAI does one thing: turn academic records into fast, fair, documented credit decisions.", center=True, aos=True), cells, FOOTNOTE))
    voices = testimonials_section(dark=False)

    tiles_data = [
        ("fa-star", "Customer Stories", "campus-columns", "Results from real campuses", "Roane State cut evaluation turnaround from three weeks to two days. Nashville State cut per-transcript time from 15 minutes to 2.", "Read customer stories", "case-studies.html"),
        ("fa-rocket", "Live in Weeks", "team-collab", "Live in two to four weeks", "Standard Banner, Colleague, Workday and PeopleSoft integrations take two to four weeks. Roane State went live on Banner in 18 days.", "See integrations", "integrations.html"),
        ("fa-shield-halved", "Security & FERPA", "registrar-desk", "Built for institutions that answer to FERPA", "EnlitEDU acts as a school official under your control. Encryption, a DPA with every contract, a SOC 2 program and no training on student records.", "Security & Trust", "security.html"),
        ("fa-lightbulb", "Research & Insights", "library-red", "Practical guides for registrars", "Plain-English guides on JST evaluation, reverse transfer, GPA standardization, FERPA and the transfer portal, written for the people who do the work.", "Read the blog", "blog.html"),
    ]
    tl = ""
    for i, (ic, lbl, ik, h3, p, cta, href) in enumerate(tiles_data):
        tl += ('<div class="tile%s" role="button" tabindex="0" aria-expanded="%s">%s<span class="lbl"><i class="fa-solid %s"></i>%s</span>'
               '<div class="content"><h3>%s</h3><p>%s</p><a class="btn-x btn-gold btn-sm" href="%s">%s <i class="fa-solid fa-arrow-right"></i></a></div></div>'
               % (" active" if i == 0 else "", "true" if i == 0 else "false", img(ik, 1000, alt="", sizes="(max-width: 991px) 100vw, 60vw"), ic, lbl, h3, p, u(href), cta))
    tiles = ('<section class="sec"><div class="container">%s<div class="tiles" data-aos="fade-up">%s</div></div></section>'
             % (sec_head("Why institutions choose EnlitEDU", "Built 100% for the <span class=\"grad\">Registrar’s</span> Office", "", center=True), tl))

    aud = "".join('<div class="col-sm-6 col-xl-3" data-aos="fade-up" data-aos-delay="%d"><a class="aud-card" href="%s">%s<span class="c"><h3>%s</h3><p>%s</p><span class="link-arrow">See how <i class="fa-solid fa-arrow-right"></i></span></span></a></div>'
                  % (i * 90, u("who-we-serve/%s.html" % a["slug"]), img(a["img"], 700, alt="", sizes="(max-width: 575px) 100vw, 25vw", ratio=(3, 3.7)), e(a["nav"]), e(AUD_CARD[a["slug"]]))
                  for i, a in enumerate(AUDIENCES))
    audiences = ('<section class="sec tint"><div class="container">%s<div class="row g-4">%s</div></div></section>'
                 % (sec_head("Who we serve", "The Same Engine, <span class=\"grad\">Your</span> Vocabulary", "Community colleges and universities don’t use the same words for the same students. LioraAI follows yours.", center=True), aud))

    ints = ('<section class="sec-sm"><div class="container"><div class="row align-items-center g-4"><div class="col-lg-4" data-aos="fade-up">%s<h2 style="font-size:clamp(28px,3vw,38px)">Works With the Systems You Already Run</h2>'
            '<p class="muted">Approved decisions post to your SIS through API or secure SFTP. No re-keying, no new system of record.</p>%s</div><div class="col-lg-8">%s</div></div></div></section>'
            % (eyebrow("Integrations"), arrow("All integrations", "integrations.html"), integrations_strip()))

    home_faqs = FAQ_HUB[0][1][:3] + [FAQ_HUB[5][1][0], FAQ_HUB[1][1][0], FAQ_HUB[2][1][0], FAQ_HUB[3][1][0]]
    faq = faq_block(home_faqs[1:], title="Questions We Hear Every Week", side_img="leaders-talk")
    latest = posts_row(["us-community-college-transfer-statistics", "state-transfer-policies-us-guide", "dual-enrollment-credit-evaluation-us-colleges"],
                       eb="Insights", h2="Fresh From the <span class=\"grad\">Blog</span>")
    from pages3 import home_nationwide_section, answer_box
    body = (hero + answer_box(*home_faqs[0]) + logo_marquee() + flagship_html() + how + proof + voices + state_story_html()
            + problem + tabs + modules + audiences + home_nationwide_section() + ints + faq + latest + cta_band())

    schema = [{"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "EnlitEDU", "publisher": {"@id": BASE + "/#organization"}, "inLanguage": "en-US"},
              {"@type": "SoftwareApplication", "@id": BASE + "/#lioraai", "name": "LioraAI", "applicationCategory": "BusinessApplication", "applicationSubCategory": "Higher education transcript evaluation",
               "operatingSystem": "Web", "url": BASE + "/platform.html", "publisher": {"@id": BASE + "/#organization"},
               "description": "AI transcript evaluation software for higher education. LioraAI Transfer Credit Intelligence automates transfer credit evaluation and LioraAI Freshman Intelligence automates high school transcript review, with staff approving every decision. Additional modules cover military credit, prior learning, degree pathways and transfer analytics.",
               "featureList": [m["name"] for m in MODULES], "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "USD"}, "description": "Priced by institution size, volume and modules."}},
              {"@type": "WebPage", "@id": BASE + "/#webpage", "url": BASE + "/", "name": "AI Transcript Evaluation Software for Colleges | LioraAI", "isPartOf": {"@id": BASE + "/#website"}, "about": {"@id": BASE + "/#lioraai"},
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".hero .sub", ".answer-box"]}},
              faq_schema(home_faqs, "index.html")] + [video_schema(t) for t in TESTIMONIALS]
    page(path, "AI Transcript Evaluation Software for Colleges | LioraAI",
         "LioraAI is AI transcript evaluation software for U.S. colleges: automated transfer credit evaluation and high school transcript review, approved by your staff.",
         body, schema=schema)

# ===================================================================== MODULE
def build_module(m):
    path = m["slug"] + ".html"; set_depth(path)
    st = "".join('<div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in m["stats"])
    fc = "".join(float_card(*f, cls=c) for f, c in zip(m["floats"], ("fc-a", "fc-b")))
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-6">'
            '<span class="lockup"><span class="mk"><i class="fa-solid %s"></i></span><span><small>%s</small>%s</span></span>'
            '<h1>%s</h1><p class="sub">%s</p><div class="btn-row mt-4"><a class="btn-x btn-gold" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a>'
            '<a class="btn-x btn-ghost-light" href="#how">See how it works</a></div><div class="hero-stats">%s</div></div>'
            '<div class="col-lg-6"><div class="visual"><div class="ph">%s</div>%s</div></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Products", "platform.html"), (m["name"], None)]), m["icon"], e(m["cat"]), e(m["name"]),
               m["h1"], m["sub"], u("request-demo.html"), st, img(m["hero_img"], 900, eager=True, sizes="(max-width: 991px) 100vw, 50vw", ratio=(4, 3.3)), fc))

    who = ('<section class="sec"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-6" data-aos="fade-right">%s<h2>%s</h2><p class="lead-lg">%s</p><p class="small muted">%s</p></div>'
           '<div class="col-lg-6" data-aos="fade-left">%s</div></div></div></section>'
           % (eyebrow(m["eyebrow"]), m["who_title"], m["who"], FOOTNOTE if m["slug"] in ("transfer-credit-intelligence", "veterans", "mobility") else "",
              which_module() if m.get("clarifier") else '<div class="split-img">%s%s</div>' % (img(MOD_IMG[m["slug"]] if MOD_IMG[m["slug"]] != m["hero_img"] else "team-collab", 900, ratio=(4, 3.4)), float_card(*m["floats"][1]))))

    pains = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d"><div class="pain"><i class="fa-solid fa-xmark"></i><p>%s</p></div></div>' % ((i % 3) * 80, p) for i, p in enumerate(m["pains"]))
    from pages3 import answer_box
    pain_sec = ('<section class="sec tint"><div class="container">%s<div class="row g-3">%s</div></div></section>'
                % (sec_head("The challenge", "The Problems You Know <span class=\"grad\">Too Well</span>", "", center=True), pains))

    diffs = "".join('<div class="col-md-6" data-aos="fade-up" data-aos-delay="%d"><div class="card-x diff"><div class="ico%s"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div></div>'
                    % ((i % 2) * 100, " gold" if i % 2 else "", ("fa-scale-balanced", "fa-user-check", "fa-fingerprint", "fa-database")[i], t, d) for i, (t, d) in enumerate(m["diffs"]))
    diff_sec = ('<section class="sec"><div class="container"><div class="row g-5"><div class="col-lg-4" data-aos="fade-up">%s<h2>Why Teams Choose <span class="grad">LioraAI</span></h2>'
                '<p class="lede muted">Built with the people who do the work, around one idea: your rules, applied every time, with a person approving every decision.</p><div class="split-img mt-4">%s</div></div>'
                '<div class="col-lg-8"><div class="row g-4">%s</div></div></div></div></section>'
                % (eyebrow("The difference"), img(m["hero_img"] if m["slug"] != "athletics" else "athlete-track", 700, ratio=(4, 3.4)), diffs))

    steps = "".join('<div class="step" data-aos="fade-up" data-aos-delay="%d"><div class="num"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div>' % (i * 90, ic, t, d) for i, (ic, t, d) in enumerate(m["steps"]))
    style = ' steps-%d' % len(m["steps"]) if len(m["steps"]) != 5 else ""  # class, so the mobile breakpoints still apply
    how = ('<section class="sec dark anchor" id="how"><div class="container">%s<div class="steps%s">%s</div>'
           '<div class="row justify-content-center mt-6"><div class="col-lg-9" data-aos="zoom-in-up">%s</div></div></div></section>'
           % (sec_head("How it works", "Simple for Staff. <span class=\"grad\">Documented</span> for Everyone.", "", center=True), style, steps, m["mock"]()))

    feats = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d"><div class="feature"><span class="ico"><i class="fa-solid %s"></i></span><div><h3>%s</h3><p>%s</p></div></div></div>' % ((i % 3) * 80, ic, t, d) for i, (ic, t, d) in enumerate(m["features"]))
    feat_sec = ('<section class="sec"><div class="container">%s<div class="row g-5">%s</div></div></section>'
                % (sec_head("Key capabilities", "Built for the Way <span class=\"grad\">Your</span> Office Works", "", center=True), feats))

    pr = m["proof"]
    vts = [t for t in TESTIMONIALS if t[0] in pr["testimonials"]]
    if pr["story"]:
        k = "roane" if "roane" in pr["story"] else "nashville"
        vids = "".join('<div class="col-sm-6" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (i * 90, vt_card(t)) for i, t in enumerate(vts[:2]))
        proof_sec = ('<section class="sec tint"><div class="container">%s<div class="row g-4 align-items-stretch"><div class="col-lg-5" data-aos="fade-up">%s</div><div class="col-lg-7"><div class="row g-4">%s</div></div></div></div></section>'
                     % (sec_head("Customer proof", pr["title"], "Real people, real offices, on video."), story_card(k), vids))
    else:
        vids = "".join('<div class="col-sm-6" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (i * 90, vt_card(t)) for i, t in enumerate(vts[:2]))
        proof_sec = ('<section class="sec tint"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-5" data-aos="fade-up">%s<h2>%s</h2><p class="lead-lg">Registrars, VPs and IT leads at Tennessee community colleges explain what changed after LioraAI went live.</p>%s</div>'
                     '<div class="col-lg-7"><div class="row g-4">%s</div></div></div></div></section>'
                     % (eyebrow("Customer proof"), pr["title"], arrow("Read customer stories", "case-studies.html"), vids))
    ints = ('<section class="sec-sm"><div class="container">%s%s</div></section>'
            % (sec_head("Integrations", "Works With Your <span class=\"grad\">Existing</span> Systems", "", center=True), integrations_strip()))
    related = "".join('<div class="col-md-4" data-aos="fade-up" data-aos-delay="%d">%s</div>' % (i * 90, mod_card(BY_SLUG[r]["slug"] + ".html", BY_SLUG[r]["cat"], BY_SLUG[r]["name"], CARD[r], BY_SLUG[r]["icon"], MOD_IMG[r])) for i, r in enumerate(m["related"]))
    rel_sec = ('<section class="sec"><div class="container">%s<div class="row g-4">%s</div></div></section>'
               % (sec_head("Works even better with", "Related <span class=\"grad\">Modules</span>", "", center=True), related))
    body = (hero + answer_box(*m["faqs"][0]) + who + pain_sec + diff_sec + how + feat_sec + proof_sec + ints + faq_block(m["faqs"][1:], side_img=m["hero_img"]) + rel_sec
            + posts_row(m["blog"], tint=True) + cta_band(h2="See %s on <span class=\"grad\">your</span> transcripts." % e(m["name"])))
    schema = [breadcrumb([("Home", "index.html"), ("Products", "platform.html"), (m["name"], path)]),
              {"@type": "SoftwareApplication", "@id": BASE + "/" + path + "#software", "name": m["name"], "alternateName": m["cat"],
               "applicationCategory": "BusinessApplication", "operatingSystem": "Web", "url": BASE + "/" + path, "isPartOf": {"@id": BASE + "/#lioraai"},
               "description": m["desc"], "featureList": m["features_schema"], "publisher": {"@id": BASE + "/#organization"},
               "audience": {"@type": "Audience", "audienceType": m["audience"]},
               "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "description": "Priced by institution size and volume. Contact EnlitEDU for a quote."}},
              {"@type": "WebPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": m["title"], "about": {"@id": BASE + "/" + path + "#software"},
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", ".answer-box", ".page-hero .sub"]}},
              faq_schema(m["faqs"], path)]
    page(path, m["title"], m["desc"], body, schema=schema, active="products", noindex=m["slug"] in HIDDEN)

# ===================================================================== SOLUTION
def proof_block(k):
    if k == "roane":
        return ('<div class="row g-4 align-items-stretch"><div class="col-lg-5" data-aos="fade-up">%s</div><div class="col-lg-7"><div class="row g-4">%s%s</div></div></div>'
                % (story_card("roane"), '<div class="col-sm-6" data-aos="fade-up">%s</div>' % vt_card(TESTIMONIALS[0]), '<div class="col-sm-6" data-aos="fade-up" data-aos-delay="100">%s</div>' % vt_card(TESTIMONIALS[2])))
    return ('<div class="row g-4 align-items-stretch"><div class="col-lg-5" data-aos="fade-up">%s</div><div class="col-lg-7"><div class="row g-4">%s%s</div></div></div>'
            % (story_card("nashville"), '<div class="col-sm-6" data-aos="fade-up">%s</div>' % vt_card(TESTIMONIALS[1]), '<div class="col-sm-6" data-aos="fade-up" data-aos-delay="100">%s</div>' % vt_card(TESTIMONIALS[0])))

def build_solution(s):
    path = "solutions/%s.html" % s["slug"]; set_depth(path)
    n, t, src = s["stat"]
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-6">%s<h1>%s</h1><p class="sub">%s</p>'
            '<div class="btn-row mt-4"><a class="btn-x btn-gold" href="%s">Request a Consultation <i class="fa-solid fa-arrow-right"></i></a><a class="btn-x btn-ghost-light" href="#help">How we help</a></div>'
            '<div class="hero-stats" style="grid-template-columns:1fr"><div><b>%s</b><span>%s · <em>%s</em></span></div></div></div>'
            '<div class="col-lg-6"><div class="visual"><div class="ph">%s</div></div></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Solutions", None), (s["nav"], None)]), eyebrow("Solution · " + e(s["nav"])), s["h1"], s["sub"], u("request-demo.html"),
               n, t, re.sub(r"<[^>]+>", "", src), img(s["img"], 900, eager=True, ratio=(4, 3.3))))
    ch = "".join('<div class="col-md-4" data-aos="fade-up" data-aos-delay="%d"><div class="card-x"><div class="ico red"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div></div>' % (i * 100, ic, a, b) for i, (ic, a, b) in enumerate(s["challenges"]))
    ch_sec = '<section class="sec tint"><div class="container">%s<div class="row g-4">%s</div></div></section>' % (sec_head("The challenge", "What’s Getting in <span class=\"grad\">the Way</span>", "", center=True), ch)
    helps = "".join('<div class="col-md-6" data-aos="fade-up" data-aos-delay="%d"><a class="card-x d-flex flex-column" href="%s" style="color:inherit"><div class="ico"><i class="fa-solid %s"></i></div><span class="cat-lbl">%s</span><h3 class="mt-1">%s</h3><p>%s</p><span class="link-arrow">Explore %s <i class="fa-solid fa-arrow-right"></i></span></a></div>'
                    % ((i % 2) * 100, u(BY_SLUG[k]["slug"] + ".html"), BY_SLUG[k]["icon"], e(BY_SLUG[k]["cat"]), e(BY_SLUG[k]["name"]), d, e(BY_SLUG[k]["short"])) for i, (k, d) in enumerate(s["helps"]))
    lis = "".join("<li>%s</li>" % b for b in s["bullets"])
    help_sec = ('<section class="sec anchor" id="help"><div class="container"><div class="row g-5"><div class="col-lg-4" data-aos="fade-up">%s<h2>How LioraAI <span class="grad">Helps</span></h2><ul class="check-list">%s</ul></div>'
                '<div class="col-lg-8"><div class="row g-4">%s</div></div></div></div></section>' % (eyebrow("How we help"), lis, helps))
    proof = '<section class="sec dark"><div class="container">%s%s</div></section>' % (sec_head("Proof", "Results at <span class=\"grad\">Real</span> Institutions", "", center=False), proof_block(s["proof"]))
    body = hero + ch_sec + help_sec + proof + faq_block(s["faqs"], side_img=s["img"]) + posts_row(s["blog"]) + cta_band()
    schema = [breadcrumb([("Home", "index.html"), ("Solutions", "platform.html"), (s["nav"], path)]),
              {"@type": "WebPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": s["title"], "about": {"@id": BASE + "/#lioraai"},
               "mentions": [{"@id": BASE + "/" + BY_SLUG[k]["slug"] + ".html#software"} for k, _ in s["helps"]]},
              faq_schema(s["faqs"], path)]
    page(path, s["title"], s["desc"], body, schema=schema, active="solutions")

# ===================================================================== AUDIENCE
def build_audience(a):
    path = "who-we-serve/%s.html" % a["slug"]; set_depth(path)
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row align-items-center g-5"><div class="col-lg-6">%s<h1>%s</h1><p class="sub">%s</p>'
            '<div class="btn-row mt-4"><a class="btn-x btn-gold" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a><a class="btn-x btn-ghost-light" href="#modules">Modules for you</a></div></div>'
            '<div class="col-lg-6"><div class="visual"><div class="ph">%s</div>%s</div></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Who We Serve", None), (a["nav"], None)]), eyebrow("Who we serve · " + e(a["nav"])), a["h1"], a["sub"], u("request-demo.html"),
               img(a["img"], 900, eager=True, ratio=(4, 3.3)), float_card("fa-language", "blue", "Your vocabulary", e(a["words"][0]) + " · " + e(a["words"][1]), "fc-a")))
    words = "".join('<span class="chip gold">%s</span>' % e(w) for w in a["words"])
    pains = "".join('<div class="col-md-6" data-aos="fade-up" data-aos-delay="%d"><div class="pain"><i class="fa-solid fa-xmark"></i><p>%s</p></div></div>' % ((i % 2) * 80, p) for i, p in enumerate(a["pains"]))
    talk = ('<section class="sec"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-6" data-aos="fade-right"><div class="split-img">%s</div></div>'
            '<div class="col-lg-6" data-aos="fade-left">%s<h2>What We Hear From <span class="grad">%s</span></h2><div class="row g-3 mb-4">%s</div><p class="small muted mb-2">We speak your language</p><div class="chips">%s</div></div></div></div></section>'
            % (img(a["img2"], 900, ratio=(4, 3.4)), eyebrow("Sound familiar?"), e(a["nav"]), pains, words))
    ranked = "".join('<div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="%d">%s</div>'
                     % ((i % 3) * 80, mod_card(BY_SLUG[k]["slug"] + ".html", ("Start here · " if i == 0 else "") + BY_SLUG[k]["cat"], BY_SLUG[k]["name"], CARD[k], BY_SLUG[k]["icon"], MOD_IMG[k])) for i, k in enumerate(a["ranked"]))
    mods = ('<section class="sec tint anchor" id="modules"><div class="container">%s<div class="row g-4">%s</div><div class="mt-5">%s</div></div></section>'
            % (sec_head("Modules, in the order most %s start" % e(a["nav"].lower()), "Where to <span class=\"grad\">Start</span>", "", center=True), ranked, which_module()))
    proofs = "".join('<div class="col-md-6" data-aos="fade-up">%s</div>' % story_card(k) for k in a["proofs"])
    proof = ('<section class="sec"><div class="container"><div class="row g-5 align-items-center"><div class="col-lg-5" data-aos="fade-up">%s<h2>Proof From Institutions <span class="grad">Like Yours</span></h2><p class="lead-lg">%s</p>%s</div>'
             '<div class="col-lg-7"><div class="row g-4">%s</div></div></div></div></section>' % (eyebrow("Customer proof"), a["why"], arrow("All customer stories", "case-studies.html"), proofs))
    story = state_story_html("system") if a["slug"] == "state-systems" else ""
    body = hero + story + talk + mods + proof + testimonials_section() + faq_block(a["faqs"], side_img=a["img2"]) + posts_row(a["blog"], tint=True) + cta_band()
    schema = [breadcrumb([("Home", "index.html"), ("Who We Serve", "platform.html"), (a["nav"], path)]),
              {"@type": "WebPage", "@id": BASE + "/" + path, "url": BASE + "/" + path, "name": a["title"], "about": {"@id": BASE + "/#lioraai"},
               "audience": {"@type": "EducationalAudience", "educationalRole": a["nav"]}},
              faq_schema(a["faqs"], path)]
    page(path, a["title"], a["desc"], body, schema=schema, active="audience")
