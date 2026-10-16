# -*- coding: utf-8 -*-
"""Shared layout, helpers and components for the EnlitEDU static site."""
import json, html, os, re

BASE = "https://www.enlitedu.com"
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
import hashlib
ASSET_VER = hashlib.md5(b"".join(open(os.path.join(OUT, "assets", p), "rb").read() for p in ("css/enlitedu.css", "js/enlitedu.js"))).hexdigest()[:8]  # cache-bust on change
TODAY = "2026-10-16"

SITE = {
    "name": "EnlitEDU",
    "product": "LioraAI",
    "email": "info@enlitedu.com",
    "street": "3840 Windermere Pkwy, Suite 403",
    "city": "Cumming", "region": "GA", "zip": "30041",
    "linkedin": "https://www.linkedin.com/company/enlitedu/",
    "youtube": "https://www.youtube.com/@LioraAIOfficial",
    "instagram": "https://www.instagram.com/enlitedu.ai",
    "facebook": "https://www.facebook.com/share/18WnT89D1S/",
    "gtm": "",  # put the real GTM-XXXXXXX here to enable analytics on every page
}

# ---------------------------------------------------------------- paths
_prefix = [""]
def set_depth(path):
    d = path.count("/")
    _prefix[0] = "../" * d
def u(p):
    """Relative URL from the page currently being rendered."""
    if p.startswith(("http", "mailto:", "tel:", "#")):
        return p
    return _prefix[0] + p
def e(s):
    return html.escape(s, quote=True)

# ---------------------------------------------------------------- images
U = {
    "students-laptop": ("1758270705518-b61b40527e76", "Students collaborating around a laptop in a lecture hall"),
    "students-group": ("1758270705317-3ef6142d306f", "Diverse group of college students working together"),
    "lecture-talk": ("1758270705482-cee87ea98738", "Students talking in a lecture hall"),
    "lecture-laugh": ("1758270704763-22072a90d3b6", "Students laughing together in a lecture hall"),
    "campus-steps": ("1553893304-448dd3e66fd1", "Students sitting outside a campus building"),
    "study-table": ("1522202176988-66273c2fd55f", "Three students studying and laughing at a table"),
    "student-backpack": ("1759852692971-a2abc6799cbd", "Smiling student with a backpack and books walking on campus"),
    "campus-columns": ("1763890498955-13f109b2fbd7", "Campus building with columns on a green lawn"),
    "veteran-smile": ("1771343917024-0b5397850ccd", "Smiling service member in uniform"),
    "veteran-notes": ("1560812349-4cb4cc930866", "Service member in uniform writing on a notepad"),
    "veteran-boots": ("1423492759094-e98da7756991", "Military boots and backpack beside a person standing"),
    "veteran-family": ("1674049406385-08fb37eeebd4", "Service member in uniform hugging her daughter"),
    "athlete-basketball": ("1712619223227-24da1f112150", "College basketball player on an arena court"),
    "athlete-runner": ("1535571638417-bc38e1002ccc", "Student-athlete running on a field"),
    "athlete-track": ("1552209841-d2dc5fd68a30", "Runners racing on a track"),
    "athlete-football": ("1485313260896-6e6edf486858", "Football player holding a ball"),
    "adult-learner": ("1604933762021-54a5858c9832", "Adult learner working on a laptop at a desk"),
    "adult-man": ("1571826867433-29518cc0b091", "Adult learner smiling while using a laptop"),
    "student-table": ("1719245309441-c577e0d1959d", "Student working at a table with a laptop"),
    "grad-woman": ("1591655694472-cc751117d95f", "Smiling graduate in cap and gown"),
    "grad-young": ("1784569338239-6c43301e4303", "Young graduate wearing a cap and gown"),
    "grad-smile": ("1618355776464-8666794d2520", "Graduate smiling outdoors in a black gown"),
    "caps-toss": ("1541339907198-e08756dedf3f", "Graduates throwing their caps in the air"),
    "registrar-docs": ("1758876201660-103984519266", "Registrar staff member reviewing documents at an office desk"),
    "registrar-desk": ("1781268034959-8706486c22a4", "Staff member focused on a computer and records at an office desk"),
    "registrar-folder": ("1762341113148-41a938d2e957", "Staff member working at a desk with a laptop and folder"),
    "leaders-talk": ("1758518727600-2c5f48419eac", "Two higher education leaders in conversation"),
    "team-collab": ("1758518731706-be5d5230e5a5", "Diverse team collaborating in a modern office"),
    "four-meeting": ("1758518729685-f88df7890776", "Four professionals in a planning meeting"),
    "cabinet": ("1573167507387-6b4b98cb7c13", "Leadership team listening to a presenter at a conference table"),
    "presenter": ("1542744173-8e7e53415bb0", "Presenter walking a team through a plan"),
    "team-hands": ("1521737604893-d14cc237f11d", "Team putting their hands together"),
    "library-people": ("1683319598210-d70486f2f996", "Students studying in a university library"),
    "library-red": ("1564981797816-1043664bf78d", "University library with tall windows and study tables"),
    "campus-aerial": ("1638636214032-581196ffd400", "Aerial view of a university campus"),
    "university-building": ("1565963479542-3cf82a9ee7e9", "Historic university building"),
    "meeting-standing": ("1530099486328-e021101a494a", "Team meeting in an office"),
    "atlanta-skyline": ("1762738174408-8f0166ecccf5", "Downtown skyline with tall buildings"),
}
LOCAL = {
    "grads-jump": ("assets/img/enlitedu/hero-students.jpg", "Graduates jumping and celebrating on campus", 1200, 800),
    "grads-selfie": ("assets/img/enlitedu/celebrating-university-graduates.jpg", "Graduates celebrating together", 900, 621),
    "jamie": ("assets/img/enlitedu/jamie-stringer.jpg", "Jamie Stringer, Roane State Community College", 400, 400),
    "alexis": ("assets/img/enlitedu/alexis-pope.jpg", "Alexis Pope, Nashville State Community College", 400, 400),
    "jessica": ("assets/img/enlitedu/jessica-hunsaker.jpg", "Jessica Hunsaker, Roane State Community College", 400, 400),
    "paul": ("assets/img/enlitedu/paul-charpie.jpg", "Paul Charpie, Roane State Community College", 400, 400),
    "chaitanya": ("assets/img/enlitedu/chaitanya-saripalli.jpg", "Chaitanya Saripalli, Founder and CEO of EnlitEDU", 400, 500),
    "sajan": ("assets/img/enlitedu/sajan-patel.jpg", "Sajan Patel, Business Development at EnlitEDU", 400, 500),
}

def src_url(key, w=1200):
    if key in LOCAL:
        return u(LOCAL[key][0])
    return "https://images.unsplash.com/photo-%s?auto=format&fit=crop&w=%d&q=72" % (U[key][0], w)

def img(key, w=1200, alt=None, cls="", sizes="(max-width: 991px) 100vw, 50vw", eager=False, ratio=(3, 2)):
    """Responsive <img>. Unsplash images get a width-based srcset; local files are used as-is."""
    lazy = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = (' class="%s"' % cls) if cls else ""
    if key in LOCAL:
        p, a, W, H = LOCAL[key]
        return '<img src="%s" alt="%s" width="%d" height="%d" %s decoding="async"%s>' % (u(p), e(alt if alt is not None else a), W, H, lazy, c)
    pid, a = U[key]
    widths = [w2 for w2 in (480, 800, 1200, 1600) if w2 <= max(w, 480) * 1.4] or [w]
    srcset = ", ".join("https://images.unsplash.com/photo-%s?auto=format&fit=crop&w=%d&q=72 %dw" % (pid, x, x) for x in widths)
    h = int(w * ratio[1] / ratio[0])
    return ('<img src="%s" srcset="%s" sizes="%s" alt="%s" width="%d" height="%d" %s decoding="async"%s>'
            % (src_url(key, w), srcset, sizes, e(alt if alt is not None else a), w, h, lazy, c))

# ---------------------------------------------------------------- navigation data
MODULES_NAV = [
    # (group, url, category, name, desc, icon)
    ("Credit Evaluation", "transfer-credit-intelligence.html", "Transfer Credit Evaluation", "LioraAI Transfer Credit Intelligence", "Map any transcript to your catalog", "fa-right-left"),
    ("Credit Evaluation", "freshman-intelligence.html", "High School Transcripts", "LioraAI Freshman Intelligence", "GPA standardization for admissions", "fa-graduation-cap"),
    ("Credit Evaluation", "pla.html", "Credit for Prior Learning", "Prior Learning Assessment", "Work, certifications & portfolios", "fa-briefcase"),
    ("Credit Evaluation", "veterans.html", "Military & JST Credit", "LioraAI for Veterans & JST", "JST, CCAF & DD-214 evaluation", "fa-medal"),
    ("Compliance & Certification", "athletics.html", "NCAA Eligibility Support", "LioraAI Athlete Transcripts", "Progress-toward-degree, documented", "fa-trophy"),
    ("Student Pathways", "degree-pathway.html", "Student Self-Service", "Student Degree Pathway", "Every student's path to a degree", "fa-route"),
    ("Student Pathways", "mobility.html", "Transfer Analytics", "Student Mobility Intelligence", "Pathways, credit loss & retention", "fa-chart-line"),
]
from data_modules import HIDDEN as HIDDEN_MODULES  # to launch a hidden module, remove it from HIDDEN in data_modules.py
MODULES_NAV = [n for n in MODULES_NAV if n[1][:-5] not in HIDDEN_MODULES]
PLATFORM_NAV = [
    ("platform.html", "Platform overview", "One engine, six modules", "fa-layer-group"),
    ("how-it-works.html", "How LioraAI works", "AI that shows its work", "fa-microchip"),
    ("integrations.html", "Integrations", "Banner, Workday, Colleague & more", "fa-plug"),
    ("security.html", "Security & Trust", "FERPA, SOC 2 program, DPA", "fa-shield-halved"),
]
SOLUTIONS_NAV = [
    ("solutions/speed-up-credit-evaluation.html", "Speed Up Credit Evaluation", "Clear the backlog without adding staff", "fa-bolt"),
    ("solutions/grow-transfer-enrollment.html", "Grow Transfer Enrollment", "Answer “will my credits transfer?” first", "fa-chart-line"),
    ("solutions/serve-military-and-adult-learners.html", "Serve Military & Adult Learners", "Credit for service and experience", "fa-flag-usa"),
    ("solutions/stay-audit-ready.html", "Stay Consistent & Audit-Ready", "Every decision documented", "fa-clipboard-check"),
    ("solutions/improve-completion-and-retention.html", "Improve Completion & Retention", "A path every student can see", "fa-user-graduate"),
]
AUDIENCE_NAV = [
    ("who-we-serve/community-colleges.html", "Community Colleges", "Transfer-in, transfer-out, CPL", "fa-school"),
    ("who-we-serve/four-year-universities.html", "Four-Year Universities", "First-year & transfer admits", "fa-building-columns"),
    ("who-we-serve/hbcus-and-msis.html", "HBCUs & MSIs", "Fair, consistent evaluation", "fa-users"),
    ("who-we-serve/state-systems.html", "State Systems & Consortia", "One set of rules across campuses", "fa-sitemap"),
]
REGION_NAV = ("georgia.html", "Georgia (headquarters state)", "On-campus visits and Georgia transfer rules", "fa-location-dot")
RESOURCES_NAV = [
    ("blog.html", "Blog", "Practical guides for registrars", "fa-newspaper"),
    ("case-studies.html", "Customer Stories", "Results from real campuses", "fa-star"),
    ("glossary.html", "Glossary", "Credit evaluation terms, defined", "fa-book-open"),
    ("faq.html", "FAQ", "Straight answers before you buy", "fa-circle-question"),
    ("events.html", "Events & Webinars", "Meet the team", "fa-calendar-days"),
]
ABOUT_NAV = [
    ("about.html", "About EnlitEDU", "Our story and mission", "fa-circle-info"),
    ("about.html#leadership", "Leadership", "The people behind LioraAI", "fa-user-tie"),
    ("careers.html", "Careers", "Work with us", "fa-briefcase"),
    ("contact.html", "Contact", "Questions, partnerships, press", "fa-envelope"),
]

def _mlink(url, name, desc, icon, cat=None):
    c = '<span class="cat">%s</span>' % e(cat) if cat else ""
    return ('<a class="mega-link" href="%s"><span class="ico"><i class="fa-solid %s" aria-hidden="true"></i></span>'
            '<span><span class="t">%s%s</span><span class="d">%s</span></span></a>' % (u(url), icon, c, e(name), e(desc)))

def _feature(img_key, kicker, title, link, label):
    return ('<a class="mega-feature" href="%s">%s<span class="c"><span class="k">%s</span><h4>%s</h4><span class="link">%s →</span></span></a>'
            % (u(link), img(img_key, 600, alt="", sizes="300px"), e(kicker), e(title), e(label)))

def header_html(active=""):
    groups = {}
    for g, url, cat, name, desc, ic in MODULES_NAV:
        groups.setdefault(g, []).append(_mlink(url, name, desc, ic, cat))
    # Put Compliance + Pathways in one column to leave room for Platform
    prod = ('<div class="inner"><div><p class="mega-title">Credit Evaluation</p>%s</div>'
            '<div>%s<p class="mega-title">Student Pathways</p>%s</div>'
            '<div><p class="mega-title">Platform</p>%s</div>%s</div>'
            % ("".join(groups["Credit Evaluation"]), ('<p class="mega-title">Compliance &amp; Certification</p>%s<div style="height:18px"></div>' % "".join(groups["Compliance & Certification"])) if groups.get("Compliance & Certification") else "", "".join(groups["Student Pathways"]),
               "".join(_mlink(*p) for p in PLATFORM_NAV),
               _feature("registrar-docs", "See it live", "Watch LioraAI evaluate a transcript in two minutes", "how-it-works.html", "How it works")))
    sol = ('<div class="inner cols-2"><div><p class="mega-title">By outcome</p>%s</div><div><p class="mega-title">&nbsp;</p>%s</div>%s</div>'
           % ("".join(_mlink(*s) for s in SOLUTIONS_NAV[:3]), "".join(_mlink(*s) for s in SOLUTIONS_NAV[3:]),
              _feature("grads-selfie", "Customer story", "Nashville State: 15 minutes to 2 per transcript", "case-studies/nashville-state-community-college.html", "Read the story")))
    aud = ('<div class="inner cols-2"><div><p class="mega-title">By institution, nationwide</p>%s</div><div><p class="mega-title">&nbsp;</p>%s<p class="mega-title" style="margin-top:18px">By region</p>%s</div>%s</div>'
           % ("".join(_mlink(*a) for a in AUDIENCE_NAV[:2]), "".join(_mlink(*a) for a in AUDIENCE_NAV[2:]), _mlink(*REGION_NAV),
              _feature("campus-columns", "Customer story", "Roane State cut transcript evaluation from three weeks to two days", "case-studies/roane-state-community-college.html", "Read the story")))
    res = ('<div class="inner cols-2"><div><p class="mega-title">Learn</p>%s</div><div><p class="mega-title">&nbsp;</p>%s</div>%s</div>'
           % ("".join(_mlink(*r) for r in RESOURCES_NAV[:3]), "".join(_mlink(*r) for r in RESOURCES_NAV[3:]),
              _feature("veteran-notes", "New guide", "How to read a Joint Services Transcript without losing an afternoon", "blog/how-to-evaluate-joint-services-transcript-jst.html", "Read the guide")))
    abt = ('<div class="inner cols-2"><div><p class="mega-title">Company</p>%s</div><div><p class="mega-title">&nbsp;</p>%s</div>%s</div>'
           % ("".join(_mlink(*a) for a in ABOUT_NAV[:2]), "".join(_mlink(*a) for a in ABOUT_NAV[2:]),
              _feature("team-collab", "Our mission", "Every student deserves a fast, fair answer about their credit", "about.html", "About us")))

    def li(label, key, panel):
        cls = "has-mega" + (" active" if active == key else "")
        return ('<li class="%s"><button type="button" aria-expanded="false" aria-haspopup="true">%s <i class="fa-solid fa-chevron-down" aria-hidden="true"></i></button>'
                '<div class="mega"><div class="container">%s</div></div></li>' % (cls, label, panel))
    cust = '<li><a href="%s"%s>Customers</a></li>' % (u("case-studies.html"), ' aria-current="page"' if active == "customers" else "")

    # mobile drawer
    def dsub(title, links):
        return ('<details><summary>%s <i class="fa-solid fa-chevron-down" aria-hidden="true"></i></summary><div class="sub">%s</div></details>'
                % (title, "".join(links)))
    dprod = ['<div class="grp">%s</div>' % e(g) if i == 0 or MODULES_NAV[i - 1][0] != g else "" for i, (g, *_r) in enumerate(MODULES_NAV)]
    dprod_links = []
    for i, (g, url, cat, name, desc, ic) in enumerate(MODULES_NAV):
        dprod_links.append(dprod[i] + '<a href="%s">%s</a>' % (u(url), e(name)))
    dprod_links.append('<div class="grp">Platform</div>' + "".join('<a href="%s">%s</a>' % (u(p[0]), e(p[1])) for p in PLATFORM_NAV))
    drawer = ('<div class="drawer" aria-hidden="true"><div class="scrim"></div><nav class="panel" aria-label="Mobile">'
              '<div class="top"><a class="brand" href="%s"><img src="%s" alt="EnlitEDU" width="160" height="40"></a>'
              '<button class="close" type="button" aria-label="Close menu"><i class="fa-solid fa-xmark"></i></button></div>%s%s%s'
              '<a class="plain" href="%s">Customers</a>%s%s<a class="btn-x btn-gold" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a></nav></div>'
              % (u("index.html"), u("assets/img/enlitedu/logo.svg"),
                 dsub("Products", dprod_links),
                 dsub("Solutions", ['<a href="%s">%s</a>' % (u(s[0]), e(s[1])) for s in SOLUTIONS_NAV]),
                 dsub("Who We Serve", ['<a href="%s">%s</a>' % (u(s[0]), e(s[1])) for s in AUDIENCE_NAV] + ['<div class="grp">By region</div><a href="%s">%s</a>' % (u(REGION_NAV[0]), e(REGION_NAV[1]))]),
                 u("case-studies.html"),
                 dsub("Resources", ['<a href="%s">%s</a>' % (u(s[0]), e(s[1])) for s in RESOURCES_NAV]),
                 dsub("About", ['<a href="%s">%s</a>' % (u(s[0]), e(s[1])) for s in ABOUT_NAV]),
                 u("request-demo.html")))

    topbar = ('<div class="topbar"><div class="container"><div class="inner"><p class="announce" style="margin:0"><span class="badge-new">NEW</span>'
              '<span>New names, same engine: LioraAI Transfer Credit Intelligence and LioraAI Freshman Intelligence, for colleges across the U.S. <a href="%s">See all modules →</a></span></p>'
              '<div class="meta"><a href="mailto:%s"><i class="fa-solid fa-envelope"></i>%s</a><a href="%s" target="_blank" rel="noopener" aria-label="EnlitEDU on LinkedIn"><i class="fa-brands fa-linkedin"></i>LinkedIn</a>'
              '<a href="%s" target="_blank" rel="noopener" aria-label="LioraAI on YouTube"><i class="fa-brands fa-youtube"></i>YouTube</a></div></div></div></div>'
              % (u("platform.html"), SITE["email"], SITE["email"], SITE["linkedin"], SITE["youtube"]))

    return (topbar +
            '<header class="site-header"><div class="container"><div class="bar">'
            '<a class="brand" href="%s" aria-label="EnlitEDU home"><img src="%s" alt="EnlitEDU" width="170" height="42"></a>'
            '<nav aria-label="Main"><ul class="nav-main">%s%s%s%s%s%s</ul></nav>'
            '<div class="header-cta"><a class="btn-x btn-ghost btn-sm" href="%s">Contact</a><a class="btn-x btn-gold btn-sm" href="%s"><span><span class="hide-sm">Request a </span>Demo</span> <i class="fa-solid fa-arrow-right"></i></a>'
            '<button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><i class="fa-solid fa-bars"></i></button></div>'
            '</div></div></header>' % (u("index.html"), u("assets/img/enlitedu/logo.svg"),
                                        li("Products", "products", prod), li("Solutions", "solutions", sol),
                                        li("Who We Serve", "audience", aud), cust, li("Resources", "resources", res),
                                        li("About", "about", abt), u("contact.html"), u("request-demo.html"))
            + drawer)

def footer_html(show_cta=True):
    cta = ""
    if show_cta:
        cta = ('<div class="footer-cta"><div class="container"><div class="row align-items-center g-4"><div class="col-lg-8">'
               '<h2>See what LioraAI does with <span class="grad">your</span> last 100 transcripts.</h2></div>'
               '<div class="col-lg-4 text-lg-end"><div class="btn-row justify-content-lg-end"><a class="btn-x btn-gold" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a></div></div>'
               '</div></div></div>' % u("request-demo.html"))
    col = lambda title, links: ('<div class="col-6 col-md-3 col-lg-2"><h3>%s</h3><ul>%s</ul></div>' %
                                (title, "".join('<li><a href="%s">%s</a></li>' % (u(a), e(b)) for a, b in links)))
    return ('<footer class="site-footer"><div class="sig-bar"></div>%s<div class="footer-main"><div class="container"><div class="row g-4">'
            '<div class="col-lg-4 footer-brand"><img src="%s" alt="EnlitEDU" width="170" height="42" loading="lazy">'
            '<p>EnlitEDU builds LioraAI, the academic record intelligence platform that helps colleges and universities across the U.S. evaluate transfer, first-year, military and prior-learning credit fast, fairly and with every decision documented.</p>'
            '<address>%s<br>%s, %s %s<br><a href="mailto:%s">%s</a></address>'
            '<div class="socials"><a href="%s" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>'
            '<a href="%s" target="_blank" rel="noopener" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>'
            '<a href="%s" target="_blank" rel="noopener" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>'
            '<a href="%s" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a></div>'
            '<div class="footer-badges"><span><i class="fa-solid fa-shield-halved"></i>FERPA-aligned</span><span><i class="fa-solid fa-lock"></i>SOC 2 program</span><span><i class="fa-solid fa-user-check"></i>Human-approved decisions</span></div></div>'
            '%s%s%s%s</div></div></div>'
            '<div class="container"><div class="footer-bottom"><span>© <span data-year>2026</span> EnlitEDU Inc. All rights reserved.</span>'
            '<nav aria-label="Legal"><a href="%s">Privacy</a><a href="%s">Terms</a><a href="%s">Security</a><a href="%s">Accessibility</a><a href="%s">Sitemap</a></nav></div></div></footer>'
            '<button class="to-top" type="button" aria-label="Back to top"><i class="fa-solid fa-arrow-up"></i></button>'
            '<div class="vmodal" role="dialog" aria-modal="true" aria-label="Video player"><div class="box"><button class="x" type="button" aria-label="Close video"><i class="fa-solid fa-xmark"></i></button></div></div>'
            % (cta, u("assets/img/enlitedu/logo-white.svg"), SITE["street"], SITE["city"], SITE["region"], SITE["zip"], SITE["email"], SITE["email"],
               SITE["linkedin"], SITE["youtube"], SITE["instagram"], SITE["facebook"],
               col("Products", [(m[1], m[3].replace("LioraAI for ", "").replace("LioraAI ", "")) for m in MODULES_NAV] + [("integrations.html", "Integrations")]),
               col("Solutions", [(s[0], s[1]) for s in SOLUTIONS_NAV]),
               col("Who We Serve", [(s[0], s[1]) for s in AUDIENCE_NAV] + [("case-studies.html", "Customer Stories"), ("georgia.html", "Georgia (HQ state)")]),
               col("Company", [("about.html", "About"), ("blog.html", "Blog"), ("glossary.html", "Glossary"), ("faq.html", "FAQ"), ("transcript-evaluation-near-me.html", "Transcript Evaluation Guide"), ("careers.html", "Careers"), ("contact.html", "Contact"), ("request-demo.html", "Request a Demo")]),
               u("privacy.html"), u("terms.html"), u("security.html"), u("accessibility.html"), u("sitemap.xml")))

# ---------------------------------------------------------------- schema
ORG = {
    "@type": ["Organization", "LocalBusiness"], "@id": BASE + "/#organization", "name": "EnlitEDU", "legalName": "EnlitEDU Inc.",
    "url": BASE + "/", "logo": {"@type": "ImageObject", "url": BASE + "/assets/img/enlitedu/logo.png"}, "image": BASE + "/assets/img/enlitedu/og-lioraai.jpg",
    "description": "EnlitEDU builds LioraAI, AI transcript evaluation software for colleges and universities across the United States. LioraAI evaluates transfer, first-year, military (JST) and prior-learning credit, and gives students a self-service path to a degree. EnlitEDU is headquartered in Cumming, Georgia, in north metro Atlanta.",
    "email": SITE["email"],
    "address": {"@type": "PostalAddress", "streetAddress": SITE["street"], "addressLocality": SITE["city"], "addressRegion": SITE["region"], "postalCode": SITE["zip"], "addressCountry": "US"},
    "areaServed": [{"@type": "Country", "name": "United States"}, {"@type": "State", "name": "Georgia"}, {"@type": "City", "name": "Atlanta", "containedInPlace": {"@type": "State", "name": "Georgia"}}],
    "location": {"@type": "Place", "name": "EnlitEDU headquarters, Cumming, Georgia (north metro Atlanta)", "address": {"@type": "PostalAddress", "streetAddress": "3840 Windermere Pkwy, Suite 403", "addressLocality": "Cumming", "addressRegion": "GA", "postalCode": "30041", "addressCountry": "US"}},
    "slogan": "Recognize Every Credit. Advance Every Learner.",
    "brand": {"@type": "Brand", "name": "LioraAI"},
    "sameAs": [SITE["linkedin"], SITE["youtube"], SITE["instagram"], SITE["facebook"]],
    "founder": {"@id": BASE + "/#chaitanya-saripalli"},
    "knowsAbout": ["Transcript evaluation software", "Transfer credit evaluation", "USG Core IMPACTS", "TCSG to USG transfer", "HOPE GPA", "Georgia Dual Enrollment", "Course articulation", "GPA standardization", "Credit for prior learning", "Joint Services Transcript", "ACE credit recommendations", "Degree audit", "FERPA", "Student information systems"],
    "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": SITE["email"], "areaServed": "US", "availableLanguage": "English"},
}

def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + "/" + (p if p != "index.html" else "")} for i, (n, p) in enumerate(items)]}

def faq_schema(faqs, url):
    return {"@type": "FAQPage", "@id": BASE + "/" + url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(_strip(a))}} for q, a in faqs]}

def _strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)

# ---------------------------------------------------------------- page shell
CS_LINKEDIN = "https://www.linkedin.com/in/chaitanyasaripalli/"
PERSON_CS = {"@type": "Person", "@id": BASE + "/#chaitanya-saripalli", "name": "Chaitanya Saripalli", "jobTitle": "Founder & CEO",
             "worksFor": {"@id": BASE + "/#organization"}, "url": BASE + "/about.html#leadership", "image": BASE + "/assets/img/enlitedu/chaitanya-saripalli.jpg",
             "sameAs": [CS_LINKEDIN], "knowsAbout": ["Transcript evaluation", "Transfer credit evaluation", "Student information systems", "Higher education technology"]}

# Entities defined on other pages: build.py registers them so cross-page @id references carry a type and name.
REG = {PERSON_CS["@id"]: {k: v for k, v in PERSON_CS.items() if k != "@id"}}
WEBSITE = {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": "EnlitEDU", "alternateName": "LioraAI by EnlitEDU",
           "publisher": {"@id": BASE + "/#organization"}, "inLanguage": "en-US"}
LIORAAI = {"@type": "SoftwareApplication", "@id": BASE + "/#lioraai", "name": "LioraAI", "applicationCategory": "BusinessApplication",
           "operatingSystem": "Web", "url": BASE + "/platform.html", "publisher": {"@id": BASE + "/#organization"},
           "description": "Academic record intelligence for colleges and universities across the U.S.: transfer, first-year, military and prior-learning credit evaluation, degree pathways and transfer analytics.",
           "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "USD"}, "description": "Priced by institution size, volume and modules."}}

def _normalize(graph, canon, desc):
    """Dedupe nodes, fill recommended properties, and resolve cross-page @id references."""
    out, seen = [], set()
    for n in graph:
        if n.get("@id") and n["@id"] in seen: continue
        if n.get("@id"): seen.add(n["@id"])
        out.append(n)
    def walk(x, refs):
        if isinstance(x, dict):
            if list(x.keys()) == ["@id"]: refs.append(x)
            for v in x.values(): walk(v, refs)
        elif isinstance(x, list):
            for v in x: walk(v, refs)
    refs = []; walk(out, refs)
    if any(r["@id"] == LIORAAI["@id"] for r in refs) and LIORAAI["@id"] not in seen:
        out.append(LIORAAI); seen.add(LIORAAI["@id"])
    for r in refs:
        if r["@id"] not in seen and r["@id"] in REG:
            r.update(REG[r["@id"]])
    for n in out:
        ty = n.get("@type"); tys = set(ty if isinstance(ty, list) else [ty])
        if tys & {"WebPage", "CollectionPage", "AboutPage", "ContactPage", "Service", "HowTo", "Article"} and not n.get("description"):
            n["description"] = desc
        if tys & {"WebPage", "CollectionPage", "AboutPage", "ContactPage", "FAQPage"} and not n.get("isPartOf"):
            n["isPartOf"] = {"@id": WEBSITE["@id"]}
        if tys & {"Article", "BlogPosting"} and not n.get("dateModified") and n.get("datePublished"):
            n["dateModified"] = n["datePublished"]
    return out

def page(path, title, desc, body, schema=None, active="", noindex=False, show_cta=False, og_type="website", image=None):
    """Write a complete HTML document to OUT/path."""
    set_depth(path)
    canon = BASE + "/" + (path if path != "index.html" else "")
    graph = _normalize([ORG, WEBSITE] + (schema or []), canon, desc)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    ogimg = image or (BASE + "/assets/img/enlitedu/og-lioraai.jpg")
    if "images.unsplash.com" in ogimg:  # social cards: exact 1200x630 crop
        ogimg = re.sub(r"&w=\d+", "&w=1200&h=630", ogimg)
    gtm_head = gtm_body = ""
    if SITE["gtm"]:
        gtm_head = ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
                    "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
                    "})(window,document,'script','dataLayer','%s');</script>" % SITE["gtm"])
        gtm_body = '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%s" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>' % SITE["gtm"]
    doc = """<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
%(gtm_head)s<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="%(robots)s">
<link rel="canonical" href="%(canon)s">
<meta property="og:type" content="%(og_type)s"><meta property="og:site_name" content="EnlitEDU"><meta property="og:locale" content="en_US">
<meta property="og:title" content="%(title)s"><meta property="og:description" content="%(desc)s"><meta property="og:url" content="%(canon)s">
<meta property="og:image" content="%(ogimg)s"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%(title)s"><meta name="twitter:description" content="%(desc)s"><meta name="twitter:image" content="%(ogimg)s">
<meta name="theme-color" content="#0a1d3a">
<link rel="icon" type="image/png" sizes="32x32" href="%(p)sassets/img/enlitedu/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="%(p)sassets/img/enlitedu/favicon-192.png">
<link rel="apple-touch-icon" href="%(p)sassets/img/enlitedu/apple-touch-icon.png">
<link rel="manifest" href="%(p)smanifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap">
<link rel="stylesheet" href="%(p)sassets/css/bootstrap.min.css">
<link rel="stylesheet" href="%(p)sassets/css/all.min.css">
<link rel="stylesheet" href="%(p)sassets/css/swiper-bundle.min.css">
<link rel="stylesheet" href="%(p)sassets/css/aos.css">
<link rel="stylesheet" href="%(p)sassets/css/enlitedu.css?v=%(ver)s">
<script type="application/ld+json">%(ld)s</script>
</head>
<body>
%(gtm_body)s<a class="skip-link" href="#main">Skip to main content</a>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
<script src="%(p)sassets/js/swiper-bundle.min.js" defer></script>
<script src="%(p)sassets/js/aos.js" defer></script>
<script src="%(p)sassets/js/enlitedu.js?v=%(ver)s" defer></script>
</body>
</html>
""" % dict(ver=ASSET_VER, title=e(title), desc=e(desc), robots="noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1",
           canon=canon, og_type=og_type, ogimg=ogimg, p=_prefix[0], ld=ld.replace("</", "<\\/"), header=header_html(active),
           body=body, footer=footer_html(show_cta), gtm_head=gtm_head, gtm_body=gtm_body)
    doc = tidy_dashes(_size_images(doc, path))
    full = os.path.join(OUT, path.replace("/", os.sep))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    PAGES.append((path, noindex))
    return full

PAGES = []

# ---------------------------------------------------------------- image dimensions (prevents layout shift)
_DIMS = {}
def _dims(fp):
    if fp in _DIMS: return _DIMS[fp]
    import struct
    w = h = None
    try:
        data = open(fp, "rb").read(256 * 1024)
        if data[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", data[16:24])
        elif data[:2] == b"\xff\xd8":
            i = 2
            while i < len(data) - 9:
                if data[i] != 0xFF: i += 1; continue
                mk = data[i + 1]
                if mk in (0xC0, 0xC1, 0xC2):
                    h, w = struct.unpack(">HH", data[i + 5:i + 9]); break
                i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
        elif fp.endswith(".svg"):
            txt = data.decode("utf-8", "ignore")
            m = re.search(r'viewBox="[\d.\-]+[\s,]+[\d.\-]+[\s,]+([\d.]+)[\s,]+([\d.]+)"', txt)
            if m: w, h = int(float(m.group(1))), int(float(m.group(2)))
    except OSError:
        pass
    _DIMS[fp] = (w, h)
    return w, h

EM, EN = "\u2014", "\u2013"
_DASH_COMMA = r"(?:and|but|or|not|so|yet|which|who|while|because|before|after|based|especially|including|just|then|than|it|it's|that|this|those|these|with|without|whether|instead|even|usually|often)\b"
def tidy_dashes(s):
    """House style (Oct 2026): no long dashes. En dash -> hyphen; em dash -> comma where it joins a clause, otherwise a spaced hyphen."""
    s = s.replace(EN, "-")
    s = re.sub(r" %s ([^%s<>\n]{1,80}?) %s " % (EM, EM, EM), r", \1, ", s)
    s = re.sub(r" %s (?=%s)" % (EM, _DASH_COMMA), ", ", s)
    s = s.replace(" %s " % EM, " - ").replace(EM, "-")
    return s.replace(", ,", ",")

def _size_images(doc, path):
    base = os.path.dirname(os.path.join(OUT, path.replace("/", os.sep)))
    def fix(m):
        tag = m.group(0)
        if "width=" in tag: return tag
        src = re.search(r'src="([^"]+)"', tag)
        if not src or src.group(1).startswith(("http", "data:")): return tag
        w, h = _dims(os.path.normpath(os.path.join(base, src.group(1))))
        if not w or not h: return tag
        tag = re.sub(r'\sheight="\d+"', "", tag)
        return tag.replace("<img ", '<img width="%d" height="%d" ' % (w, h), 1)
    return re.sub(r"<img\b[^>]*>", fix, doc)

# ---------------------------------------------------------------- components
def eyebrow(t):
    return '<span class="eyebrow"><span class="dot"></span>%s</span>' % t

def sec_head(eb, h2, lede="", center=False, aos=True):
    a = ' data-aos="fade-up"' if aos else ""
    return ('<div class="sec-head%s"%s>%s<h2>%s</h2>%s</div>'
            % (" center" if center else "", a, eyebrow(eb) if eb else "", h2, '<p class="lede">%s</p>' % lede if lede else ""))

def crumbs(items):
    lis = []
    for i, (n, p) in enumerate(items):
        if p and i < len(items) - 1:
            lis.append('<li><a href="%s">%s</a></li>' % (u(p), e(n)))
        else:
            lis.append('<li aria-current="page">%s</li>' % e(n))
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">%s</ol></nav>' % "".join(lis)

def faq_block(faqs, title="Frequently asked questions", lede="", side_img=None, eb="FAQ"):
    items = "".join(
        '<div class="faq-item%s"><button class="faq-q" type="button" aria-expanded="%s">%s<span class="pm"><i class="fa-solid fa-plus"></i></span></button>'
        '<div class="faq-a"><div><p>%s</p></div></div></div>' % (" open" if i == 0 else "", "true" if i == 0 else "false", e(q), a)
        for i, (q, a) in enumerate(faqs))
    side = ""
    if side_img:
        side = '<div class="ph">%s</div>' % img(side_img, 800, sizes="(max-width: 991px) 100vw, 33vw")
    return ('<section class="sec tint" aria-labelledby="faq-h"><div class="container"><div class="row g-5">'
            '<div class="col-lg-4"><div class="faq-side" data-aos="fade-up">%s<h2 id="faq-h">%s</h2><p class="muted">%s</p>'
            '<a class="link-arrow" href="%s">See all FAQs <i class="fa-solid fa-arrow-right"></i></a>%s</div></div>'
            '<div class="col-lg-8"><div class="faq-wrap" data-aos="fade-up" data-aos-delay="100">%s</div></div></div></div></section>'
            % (eyebrow(eb), title, lede or "Straight answers to what registrars, enrollment leaders and IT teams ask us most.", u("faq.html"), side, items))

def cta_band(h2="See what LioraAI does with <span class=\"grad\">your</span> transcripts.", p="Bring a few real transcripts to a 30-minute demo. We’ll run them live against your catalog and rules, and show you the review screen and the SIS write-back.", img_key="caps-toss", secondary=("Watch the 2-minute overview", "Ti6YBv2R_Gc")):
    sec = ""
    if secondary:
        sec = '<a class="btn-x btn-ghost-light" href="https://www.youtube.com/watch?v=%s" data-video="%s"><i class="fa-solid fa-play"></i> %s</a>' % (secondary[1], secondary[1], e(secondary[0]))
    return ('<section class="sec-sm"><div class="container"><div class="cta-band on-dark" data-aos="zoom-in-up">%s<div class="row align-items-center g-4">'
            '<div class="col-lg-8"><h2>%s</h2><p>%s</p></div><div class="col-lg-4"><div class="btn-row justify-content-lg-end">'
            '<a class="btn-x btn-gold" href="%s">Request a Demo <i class="fa-solid fa-arrow-right"></i></a>%s</div></div></div></div></div></section>'
            % (img(img_key, 1600, alt="", sizes="100vw"), h2, p, u("request-demo.html"), sec))

def float_card(icon, tone, title, sub, cls=""):
    return ('<div class="float-card %s"><span class="ic %s"><i class="fa-solid %s" aria-hidden="true"></i></span><span><b>%s</b><span>%s</span></span></div>'
            % (cls, tone, icon, title, sub))

TESTIMONIALS = [
    # key, youtube id, start, name, role, institution, upload, duration, desc
    ("jamie", "UUpuMEJX3Tk", 6, "Jamie Stringer", "Vice President of Student Services & Innovation", "Roane State Community College", "2026-03-12", "PT3M51S",
     "Jamie Stringer, Vice President of Student Services & Innovation at Roane State Community College, on how LioraAI changed their transfer credit evaluation."),
    ("alexis", "_lUO-AJF2Cs", 0, "Alexis Pope", "Vice President, Student Affairs & Enrollment Management", "Nashville State Community College", "2026-05-29", "PT3M34S",
     "Alexis Pope, Vice President of Student Affairs & Enrollment Management at Nashville State Community College, on working with EnlitEDU and LioraAI."),
    ("jessica", "5Kqhrc2fyO8", 16, "Jessica Hunsaker", "Registrar, Director of Admissions, Records & Graduation", "Roane State Community College", "2026-05-20", "PT4M38S",
     "Jessica Hunsaker, Registrar at Roane State Community College, on how LioraAI changed the registrar's evaluation workflow."),
    ("paul", "8sF5xILZTmU", 6, "Paul Charpie", "Computer Programmer Analyst", "Roane State Community College", "2026-03-14", "PT3M08S",
     "Paul Charpie, Computer Programmer Analyst at Roane State Community College, on integrating LioraAI with Ellucian Banner."),
]
OVERVIEW_VIDEO = ("Ti6YBv2R_Gc", "LioraAI Product Overview", "A 2-minute overview of LioraAI: transcript evaluation, transfer credit articulation, GPA standardization and prior learning assessment for higher education.", "2024-01-01", "PT2M")

def video_schema(t):
    key, vid, start, name, role, inst, up, dur, desc = t
    return {"@type": "VideoObject", "@id": "https://www.youtube.com/watch?v=" + vid, "name": "LioraAI review: %s, %s" % (name, inst),
            "description": desc, "thumbnailUrl": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % vid, "uploadDate": up, "duration": dur,
            "contentUrl": "https://www.youtube.com/watch?v=" + vid, "embedUrl": "https://www.youtube-nocookie.com/embed/" + vid,
            "publisher": {"@id": BASE + "/#organization"}}

def vt_card(t):
    key, vid, start, name, role, inst, *_ = t
    return ('<button class="vt-card" type="button" data-video="%s" data-start="%d" aria-label="Play video: %s, %s">%s'
            '<span class="play"><i class="fa-solid fa-play"></i></span><span class="meta"><b>%s</b><span>%s<br>%s</span><em>Watch the interview</em></span></button>'
            % (vid, start, e(name), e(inst), img(key, 400, alt="", sizes="300px"), e(name), e(role), e(inst)))

def testimonials_section(ids=None, eb="In their own words", h2="Hear it from the people who <span class=\"grad\">run</span> the office", lede="Registrars, VPs and IT leads at Tennessee community colleges talk about what changed after LioraAI went live.", dark=True):
    ts = [t for t in TESTIMONIALS if not ids or t[0] in ids]
    slides = "".join('<div class="swiper-slide">%s</div>' % vt_card(t) for t in ts)
    return ('<section class="sec%s" id="voices"><div class="container"><div class="d-flex flex-wrap justify-content-between align-items-end gap-3 mb-5">'
            '<div class="sec-head mb-0" data-aos="fade-up">%s<h2>%s</h2><p class="lede">%s</p></div>'
            '<div class="swiper-ctrl"><button type="button" data-prev="vt" aria-label="Previous"><i class="fa-solid fa-arrow-left"></i></button><button type="button" data-next="vt" aria-label="Next"><i class="fa-solid fa-arrow-right"></i></button></div></div>'
            '<div class="swiper" data-swiper="vt" data-xl="4"><div class="swiper-wrapper">%s</div></div></div></section>'
            % (" dark" if dark else "", eyebrow(eb), h2, lede, slides))

LOGOS = [
    ("alabama-a-m-university.png", "Alabama A&M University"),
    ("bronx-community-college.png", "Bronx Community College"),
    ("roane-state-community-college.png", "Roane State Community College"),
    ("emory-university.png", "Emory University"),
    ("johnson-c-smith-university.png", "Johnson C. Smith University"),
    ("miles-college.png", "Miles College"),
]
def logo_marquee(label="Trusted by enrollment teams across the U.S."):
    imgs = "".join('<img src="%s" alt="%s" height="46" loading="lazy">' % (u("assets/img/enlitedu/" + f), e(n)) for f, n in LOGOS)
    dup = "".join('<img src="%s" alt="" aria-hidden="true" height="46" loading="lazy">' % u("assets/img/enlitedu/" + f) for f, n in LOGOS)
    return ('<section class="trust" aria-label="Institutions"><div class="container"><p class="lbl">%s</p>'
            '<div class="marquee"><div class="marquee-track">%s%s%s%s</div></div></div></section>' % (e(label), imgs, dup, dup, dup))

INTEGRATIONS = [
    ("logo-ellucian.svg", "Ellucian Banner & Colleague"), ("logo-workday.svg", "Workday Student"), ("logo-peoplesoft.png", "PeopleSoft Campus Solutions"),
    ("logo-jenzabar.png", "Jenzabar"), ("logo-slate.png", "Slate by Technolutions"), ("logo-salesforce.png", "Salesforce"),
]
def integrations_strip(extra=True):
    items = "".join('<div class="int-item" title="%s"><img src="%s" alt="%s" loading="lazy"></div>' % (e(n), u("assets/img/enlitedu/" + f), e(n)) for f, n in INTEGRATIONS)
    if extra:
        items += "".join('<div class="int-item"><span>%s</span></div>' % e(t) for t in ("Common App", "DegreeWorks", "uAchieve", "PESC XML & EDI", "SFTP", "ACE / JST"))
    return '<div class="int-grid" data-aos="fade-up">%s</div>' % items

def mod_card(url, cat, name, desc, icon, img_key):
    return ('<a class="mod-card" href="%s"><div class="thumb">%s<span class="ico"><i class="fa-solid %s"></i></span></div>'
            '<div class="body"><span class="cat">%s</span><h3>%s</h3><p>%s</p><span class="link-arrow">Learn more <i class="fa-solid fa-arrow-right"></i></span></div></a>'
            % (u(url), img(img_key, 800, alt="", sizes="(max-width: 767px) 100vw, 33vw"), icon, e(cat), e(name), desc))
