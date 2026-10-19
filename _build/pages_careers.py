# -*- coding: utf-8 -*-
"""Careers: careers.html (open roles), careers/<slug>.html (role + application form + JobPosting schema), application-received.html."""
from core import *
from pages2 import simple_hero
from data_careers import JOBS, ABOUT_ENLITEDU

OPEN = [j for j in JOBS if j.get("open")]

def careers_faqs():
    roles = ", ".join(j["title"] for j in OPEN) or "no open roles at the moment"
    return [
        ("Is EnlitEDU hiring?", "Yes. Current openings: %s. Each role has its own page with the full description and an online application." % roles),
        ("Are EnlitEDU jobs remote?", "Many are. Each posting lists its location; the %s role is remote. EnlitEDU is headquartered in Cumming, Georgia." % (OPEN[0]["title"] if OPEN else "first")),
        ("How do I apply for a job at EnlitEDU?", "Open the role, fill in the application form with a link to your résumé, and submit. You can also email your résumé to hr@enlitedu.com with the role in the subject line."),
        ("What happens after I apply?", "We read every application. If your experience is a fit, we email you to set up an introductory call with the team."),
        ("Can I apply if there is no open role that fits?", "Yes. Send your résumé and a short note about the work you’d like to do to hr@enlitedu.com, and we will keep it on file for future openings."),
    ]

def _meta_chips(j):
    return "".join('<span class="job-chip"><i class="fa-solid %s"></i>%s</span>' % (ic, e(t)) for ic, t in
                   (("fa-location-dot", j["location"]), ("fa-briefcase", j["employment"]), ("fa-chart-line", j["experience"] + " experience")))

def job_card(j):
    return ('<a class="job-card" href="%s"><div><h3>%s</h3><p>%s</p><div class="job-chips">%s</div></div>'
            '<span class="btn-x btn-navy btn-sm">View role &amp; apply <i class="fa-solid fa-arrow-right"></i></span></a>'
            % (u("careers/%s.html" % j["slug"]), e(j["title"]), e(j["summary"]), _meta_chips(j)))

def build_careers():
    path = "careers.html"; set_depth(path)
    hero = simple_hero([("Home", "index.html"), ("Careers", None)], "Careers at EnlitEDU", "Build the Future of <span class=\"accent\">Credit Mobility</span>",
                       "Join a small, fast-moving team building LioraAI, the platform that helps colleges across the U.S. give students a fast, fair answer about their credit.",
                       "team-collab", float_card("fa-briefcase", "gold", "%d open role%s" % (len(OPEN), "" if len(OPEN) == 1 else "s"), "Remote-friendly", "fc-a"))
    why = [("fa-graduation-cap", "Work that reaches students", "Every implementation shortens how long students wait for a credit decision."),
           ("fa-laptop-house", "Remote-friendly", "Our team works across locations, with headquarters in Cumming, Georgia."),
           ("fa-hand-holding-heart", "Ownership from day one", "Small team, real responsibility and direct access to leadership."),
           ("fa-rocket", "A growing product", "Live at community colleges, with new modules and institutions every term.")]
    whyh = "".join('<div class="col-sm-6 col-lg-3" data-aos="fade-up" data-aos-delay="%d"><div class="card-x"><div class="ico"><i class="fa-solid %s"></i></div><h3>%s</h3><p>%s</p></div></div>' % (i * 70, ic, t, d) for i, (ic, t, d) in enumerate(why))
    roles = "".join('<div class="col-12" data-aos="fade-up">%s</div>' % job_card(j) for j in OPEN) or '<div class="col-12"><p class="lead-lg">No open roles right now.</p></div>'
    body = (hero
            + '<section class="sec anchor" id="open-roles"><div class="container">%s<div class="row g-3">%s</div>'
              '<p class="muted mt-4 mb-0">Don’t see your role? Send your résumé and a note about what you’d like to work on to <a href="mailto:hr@enlitedu.com?subject=Careers%%20at%%20EnlitEDU">hr@enlitedu.com</a>.</p></div></section>'
              % (sec_head("Open positions", "Current <span class=\"grad\">Openings</span>", "", center=False), roles)
            + '<section class="sec tint"><div class="container">%s<div class="row g-4">%s</div></div></section>' % (sec_head("Why EnlitEDU", "Why People <span class=\"grad\">Join Us</span>", "", center=True), whyh)
            + faq_block(careers_faqs(), title="Working at EnlitEDU", side_img="team-hands")
            + cta_band(h2="Questions about <span class=\"grad\">a role</span>?", p="Email hr@enlitedu.com and we’ll get back to you.", secondary=None))
    url = BASE + "/" + path
    schema = [breadcrumb([("Home", "index.html"), ("Careers", path)]), faq_schema(careers_faqs(), path),
              {"@type": "CollectionPage", "@id": url, "url": url, "name": "Careers at EnlitEDU",
               "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": BASE + "/careers/%s.html" % j["slug"], "name": j["title"]} for i, j in enumerate(OPEN)]}}]
    page(path, "Careers at EnlitEDU | Open Roles",
         "Join EnlitEDU, the team behind LioraAI transcript evaluation software. See open roles, including remote positions, and apply online.", body, schema=schema, active="about")

def _apply_form(j):
    yrs = "".join("<option>%s</option>" % o for o in ("Less than 5 years", "5-8 years", "8+ years"))
    return ('<form class="form-card" data-web3 data-key="771756d7-6fd4-4664-a3c6-2b07a0650a71" data-email="hr@enlitedu.com" data-subject="Job application: %s" data-redirect="%s" novalidate>'
            '<h2>Apply for this role</h2><p class="muted small">Fields marked <span style="color:#c0392b">*</span> are required. We review every application and reply to shortlisted candidates.</p>'
            '<input type="hidden" name="position" value="%s">'
            '<div class="fgrid"><div class="field"><label for="a-first">First name <span class="req">*</span></label><input id="a-first" name="first_name" autocomplete="given-name" required></div>'
            '<div class="field"><label for="a-last">Last name <span class="req">*</span></label><input id="a-last" name="last_name" autocomplete="family-name" required></div>'
            '<div class="field"><label for="a-email">Email <span class="req">*</span></label><input id="a-email" name="email" type="email" autocomplete="email" required></div>'
            '<div class="field"><label for="a-phone">Phone <span class="req">*</span></label><input id="a-phone" name="phone" type="tel" autocomplete="tel" required></div>'
            '<div class="field"><label for="a-loc">Current location (city, state/country) <span class="req">*</span></label><input id="a-loc" name="location" autocomplete="address-level2" required></div>'
            '<div class="field"><label for="a-yrs">Relevant experience <span class="req">*</span></label><select id="a-yrs" name="experience" required><option value="">Select…</option>%s</select></div>'
            '<div class="field"><label for="a-li">LinkedIn profile URL</label><input id="a-li" name="linkedin" type="url" placeholder="https://www.linkedin.com/in/…"></div>'
            '<div class="field"><label for="a-cv">Résumé link (Google Drive, Dropbox, OneDrive) <span class="req">*</span></label><input id="a-cv" name="resume_link" type="url" placeholder="https://…" required></div>'
            '<div class="field"><label for="a-start">Earliest start date / notice period</label><input id="a-start" name="availability"></div>'
            '<div class="field"><label for="a-auth">Authorized to work in the U.S.? <span class="req">*</span></label><select id="a-auth" name="work_authorization" required><option value="">Select…</option><option>Yes</option><option>Yes, with sponsorship</option><option>No</option></select></div>'
            '<div class="field full"><label for="a-msg">Tell us about an implementation you led, and why this role <span class="req">*</span></label><textarea id="a-msg" name="message" required></textarea></div></div>'
            '<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
            '<button class="btn-x btn-gold w-100 mt-4" type="submit">Submit application <i class="fa-solid fa-arrow-right"></i></button><div class="form-msg" role="alert"></div>'
            '<p class="note mt-3 mb-0">Make sure your résumé link is viewable by anyone with the link. Prefer email? Send your résumé to <a href="mailto:hr@enlitedu.com?subject=%s">hr@enlitedu.com</a> with the role in the subject. '
            'By applying, you agree to our <a href="%s">Privacy Policy</a>.</p></form>'
            % (e(j["title"]), u("application-received.html"), e(j["title"]), yrs, ("Application%3A%20" + j["title"].replace(" ", "%20")), u("privacy.html")))

def build_job(j):
    path = "careers/%s.html" % j["slug"]; set_depth(path); url = BASE + "/" + path
    hero = ('<section class="page-hero on-dark"><div class="container">%s<div class="row g-5 align-items-end"><div class="col-lg-8">%s<h1>%s</h1><p class="sub">%s</p>'
            '<div class="job-chips light mt-3">%s</div><div class="btn-row mt-4"><a class="btn-x btn-gold" href="#apply">Apply now <i class="fa-solid fa-arrow-right"></i></a>'
            '<a class="btn-x btn-ghost-light" href="%s">All open roles</a></div></div></div></div></section>'
            % (crumbs([("Home", "index.html"), ("Careers", "careers.html"), (j["title"], None)]), eyebrow("Careers · %s · %s" % (j["location"], j["employment"])),
               e(j["title"]), e(j["summary"]), _meta_chips(j), u("careers.html")))
    ul = lambda items: "<ul>%s</ul>" % "".join("<li>%s</li>" % e(x) for x in items)
    resp = "".join("<h3>%d. %s</h3>%s" % (i + 1, e(h), ul(items)) for i, (h, items) in enumerate(j["responsibilities"]))
    succ = "".join('<div class="col-md-6 col-xl-4"><div class="stat-card"><div class="n" style="font-size:24px">%s</div>%s</div></div>' % (e(h), ul(items)) for h, items in j["success"])
    desc_html = ('<h2>About EnlitEDU</h2><p>%s</p><p>%s</p><h2>Key responsibilities</h2>%s<h2>Required qualifications</h2>%s<h2>Preferred qualifications</h2>%s'
                 % (e(ABOUT_ENLITEDU), e(j["intro"]), resp, ul(j["required"]), ul(j["preferred"])))
    content = ('<div class="prose job-body">%s<h2>What success looks like</h2><div class="row g-3 mt-1">%s</div><h2>Ideal candidate</h2><p>%s</p></div>' % (desc_html, succ, e(j["ideal"])))
    side = ('<aside class="glance"><h3>Role summary</h3><dl><dt>Company</dt><dd>EnlitEDU Inc.</dd><dt>Location</dt><dd>%s</dd><dt>Employment type</dt><dd>%s</dd>'
            '<dt>Experience</dt><dd>%s</dd><dt>Reports to</dt><dd>%s</dd><dt>Posted</dt><dd>%s</dd></dl>'
            '<a class="btn-x btn-gold w-100 mt-4" href="#apply">Apply now <i class="fa-solid fa-arrow-right"></i></a></aside>'
            % (e(j["location"]), e(j["employment"]), e(j["experience"]), e(j["reports_to"]), __import__("datetime").date.fromisoformat(j["posted"]).strftime("%B %d, %Y").replace(" 0", " ")))
    body = (hero + '<section class="sec"><div class="container"><div class="row g-5"><div class="col-lg-8">%s</div><div class="col-lg-4"><div class="ga-side">%s</div></div></div></div></section>' % (content, side)
            + '<section class="sec tint anchor" id="apply"><div class="container"><div class="row justify-content-center"><div class="col-lg-9">%s</div></div></div></section>' % _apply_form(j))
    posting = {"@type": "JobPosting", "@id": url + "#job", "title": j["title"], "url": url,
               "description": "<p>%s</p><p>%s</p>" % (e(ABOUT_ENLITEDU), e(j["intro"])) + desc_html.split("<h2>Key responsibilities</h2>", 1)[1] + "<h2>Ideal candidate</h2><p>%s</p>" % e(j["ideal"]),
               "identifier": {"@type": "PropertyValue", "name": "EnlitEDU", "value": j["slug"]},
               "datePosted": j["posted"], "validThrough": j["valid_through"] + "T23:59:59-05:00", "employmentType": j["employment_schema"],
               "hiringOrganization": {"@type": "Organization", "@id": BASE + "/#organization", "name": "EnlitEDU Inc.", "sameAs": BASE + "/", "logo": BASE + "/assets/img/enlitedu/logo.png"},
               "experienceRequirements": {"@type": "OccupationalExperienceRequirements", "monthsOfExperience": j["experience_months"]},
               "skills": ", ".join(j["skills"]), "industry": "Higher education software", "directApply": True}
    if j.get("remote"):
        posting["jobLocationType"] = "TELECOMMUTE"
        posting["applicantLocationRequirements"] = {"@type": "Country", "name": j.get("applicant_country", "US")}
    schema = [breadcrumb([("Home", "index.html"), ("Careers", "careers.html"), (j["title"], path)]), posting]
    title = "%s (Remote) | EnlitEDU Careers" % j["title"] if j.get("remote") else "%s | EnlitEDU Careers" % j["title"]
    page(path, title, ("%s at EnlitEDU: %s %s. Apply online." % (j["title"], j["employment"].lower(), "remote role" if j.get("remote") else "role") + " " + j["summary"])[:160].rsplit(" ", 1)[0].rstrip(",.") + ".",
         body, schema=schema, active="about")

def build_application_received():
    path = "application-received.html"; set_depth(path)
    body = ('<section class="page-hero on-dark"><div class="container"><div class="row justify-content-center text-center"><div class="col-lg-8">'
            '<div style="width:84px;height:84px;border-radius:50%%;background:var(--gold);color:var(--navy);display:grid;place-items:center;font-size:34px;margin:0 auto 24px"><i class="fa-solid fa-check"></i></div>'
            '<h1>Application Received</h1><p class="sub mx-auto">Thank you for applying to EnlitEDU. We review every application, and shortlisted candidates will hear from us by email.</p>'
            '<div class="btn-row justify-content-center mt-4"><a class="btn-x btn-gold" href="%s">See open roles</a><a class="btn-x btn-ghost-light" href="%s">About EnlitEDU</a></div></div></div></div></section>'
            % (u("careers.html"), u("about.html")))
    page(path, "Application Received | EnlitEDU", "Thanks for applying to EnlitEDU.", body, noindex=True,
         schema=[breadcrumb([("Home", "index.html"), ("Careers", "careers.html"), ("Application received", path)])])

def build_all():
    build_careers()
    for j in OPEN:
        build_job(j)
    build_application_received()
