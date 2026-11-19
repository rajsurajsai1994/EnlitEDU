# -*- coding: utf-8 -*-
"""Articles written by EnlitEDU's founder, adapted from her own LinkedIn posts.
Regulatory facts were checked against the final rule text (FR Doc. 2026-22174, public-inspection PDF) on 2026-11-20:
34 CFR 602.24(e)(1)-(5), 34 CFR 668.43(a)(11) and (c)(3)-(5), Section IV (implementation dates) and the RIA transfer data (Table 3.1)."""

LI_ARTICLE = "https://www.linkedin.com/pulse/new-federal-transfer-rule-changes-question-colleges-have-saripalli-ztkre"
LI_CAROUSEL = "https://www.linkedin.com/posts/chaitanyasaripalli_the-new-federal-transfer-rule-what-colleges-activity-7529256800534052864-8Oy6"
FR_URL = "https://www.federalregister.gov/d/2026-22174"
FR_PDF = "https://www.govinfo.gov/content/pkg/FR-2026-10-30/pdf/2026-22174.pdf"
FR_PI = "https://public-inspection.federalregister.gov/2026-22174.pdf"
IMG = "../assets/img/enlitedu/blog/"

SLIDES = [
    "Slide 1 of 8: The new transfer rule changes the question colleges have to answer. What the Department of Education’s AIM rule requires, and where to start. By Chaitanya (Tanya) Saripalli, CEO, EnlitEDU.",
    "Slide 2 of 8: Transfer students have asked “Will my credits count?” and too often heard “We’ll let you know.” On October 30, 2026, the Department published the AIM final rule. It takes effect July 1, 2027.",
    "Slide 3 of 8: Credit decisions need a reason. Award comparable credit or explain why not, don’t deny credit because of where it came from, and give students 15 calendar days to appeal.",
    "Slide 4 of 8: Students must know before they commit. Tell students up front which credits transfer, before they sign, register or pay, and publish the rules, including the transcript deadline.",
    "Slide 5 of 8: Why it matters. 1.8 million students receiving federal aid switched schools in a single year, according to the Department’s own data.",
    "Slide 6 of 8: The hard part isn’t the policy, it’s the workflow: a course-by-course decision, a written reason for every denial and an estimate of how long it will take to finish.",
    "Slide 7 of 8: Five places to start: map your workflow, audit your denial reasons, set your transcript deadline, test degree applicability and plan for appeals.",
    "Slide 8 of 8: A personal note. At EnlitEDU we built LioraAI to give students instant, clear answers about their credits, with staff approving every decision. Source: 91 FR 68626, 34 CFR 602.24(e) and 668.43.",
]

def _fig(n, caption):
    return ('<figure class="slide-fig"><img src="%sfederal-transfer-rule-slide-%d.png" alt="%s" width="1023" height="1280" loading="lazy" decoding="async">'
            '<figcaption>%s</figcaption></figure>' % (IMG, n, SLIDES[n - 1].replace('"', "&quot;"), caption))

_gallery = "".join('<a class="slide-thumb" href="%sfederal-transfer-rule-slide-%d.png" target="_blank" rel="noopener"><img src="%sfederal-transfer-rule-slide-%d.png" alt="%s" width="1023" height="1280" loading="lazy" decoding="async"></a>'
                   % (IMG, i, IMG, i, SLIDES[i - 1].replace('"', "&quot;")) for i in range(1, 9))

FOUNDER_POSTS = [
dict(
 slug="new-federal-transfer-credit-rule-aim-2027",
 author="cs",
 title="The New Federal Transfer Credit Rule: What Colleges Must Do by July 1, 2027",
 seo_title="New Federal Transfer Credit Rule: What Colleges Must Do",
 desc="The Education Department’s AIM rule takes effect July 1, 2027: course-by-course transfer credit decisions, written denial reasons and a 15-day appeal window.",
 sub="On October 30, 2026, the U.S. Department of Education published its Accreditation, Innovation, and Modernization (AIM) final rule. Most headlines are about accreditation. Inside it is one of the most significant transfer credit reforms in decades.",
 date="2026-11-20", original_date="2026-11-19", tag="Compliance", mins=9, img="aim-cover", cover_ratio=(16, 9),
 og_image="/assets/img/enlitedu/blog/federal-transfer-rule-aim-cover.png",
 images=["/assets/img/enlitedu/blog/federal-transfer-rule-aim-cover.png"] + ["/assets/img/enlitedu/blog/federal-transfer-rule-slide-%d.png" % i for i in range(1, 9)],
 based_on=[LI_ARTICLE, LI_CAROUSEL],
 about_rule={"@type": "Legislation", "name": "Accreditation, Innovation, and Modernization (AIM) final rule", "alternateName": "AIM rule",
             "legislationIdentifier": "91 FR 68626; FR Doc. 2026-22174; RIN 1840-AD82; Docket ED-2026-OPE-1042",
             "legislationDate": "2026-10-30", "legislationType": "Final rule", "url": FR_URL,
             "legislationResponsible": {"@type": "GovernmentOrganization", "name": "U.S. Department of Education", "url": "https://www.ed.gov/"},
             "legislationJurisdiction": {"@type": "Country", "name": "United States"},
             "temporalCoverage": "2027-07-01/.."},
 keywords="federal transfer credit rule, AIM final rule, Accreditation Innovation and Modernization rule, 34 CFR 602.24(e), 34 CFR 668.43, transfer credit written denial reason, transfer credit appeal 15 days, July 1 2027 transfer rule, Department of Education transfer credit regulation, transfer credit compliance",
 body="""
<div class="takeaways"><h2>Key takeaways</h2><ul>
<li>The U.S. Department of Education published the Accreditation, Innovation, and Modernization (AIM) final rule on October 30, 2026 (91 FR 68626). It takes effect <strong>July 1, 2027</strong>.</li>
<li>For undergraduate programs, colleges must award transfer credit for comparable coursework from an institution accredited by a recognized agency, or give the student a <strong>written reason specific to each course</strong>.</li>
<li>Credit can’t be denied because of the institution where the coursework was completed or the agency that accredits it, as long as that agency is recognized by the Secretary.</li>
<li>Students get <strong>15 calendar days</strong> to appeal a denial after receiving the college’s written notice.</li>
<li>When a transcript arrives on time, the college must tell the student in writing which credits it will and won’t award, and the estimated time and courses needed to replace the rest, <strong>before the student signs an enrollment agreement, registers or makes a nonrefundable payment</strong>.</li>
<li>Accreditors confirm that institutions’ transfer policies meet these requirements during accreditation reviews.</li>
</ul></div>

<p>For years, transfer students have asked colleges one simple question: “Will my credits count?” Too often, the honest answer has been “We’ll let you know,” sometimes weeks later, often after the student has already registered or paid.</p>
<p>That’s about to change. Most of the headlines about the AIM rule are about accreditation. But tucked inside is one of the most significant transfer credit reforms in decades, and it takes effect July 1, 2027.</p>
<div class="callout"><strong>From our founder</strong>This article is adapted from Chaitanya Saripalli’s <a href="%(li_a)s" target="_blank" rel="noopener">LinkedIn article</a> and <a href="%(li_c)s" target="_blank" rel="noopener">8-slide carousel</a>, both published November 19, 2026. Every regulatory detail below was checked against the final rule text in the <a href="%(fr)s" target="_blank" rel="noopener">Federal Register</a>.</div>

<h2>What is the AIM rule?</h2>
<p>The Accreditation, Innovation, and Modernization (AIM) rule is a U.S. Department of Education final rule (Docket ED-2026-OPE-1042, RIN 1840-AD82) that revises 34 CFR Parts 600, 602 and 668. It was published in the Federal Register on October 30, 2026 as document 2026-22174. Most of the rule changes how the Secretary recognizes accrediting agencies, implementing Executive Order 14279, <em>Reforming Accreditation to Strengthen Higher Education</em>. It also rewrites the transfer of credit requirements in <strong>34 CFR 602.24(e)</strong> and the transfer disclosures colleges must make under <strong>34 CFR 668.43</strong>.</p>
<p>The Department proposed the rule earlier in 2026 (91 FR 53940) and received 7,051 public comments before publishing the final version.</p>

<h2>What does the new federal transfer credit rule require?</h2>
<p>In plain terms, here is what colleges will need to do, and where each requirement sits in the regulations.</p>
<table>
<thead><tr><th>Requirement</th><th>What it means for your office</th><th>Regulation</th></tr></thead>
<tbody>
<tr><td><strong>Award comparable credit, or explain why not</strong></td><td>For undergraduate programs, award credit for coursework successfully completed at an institution accredited by a recognized agency when it is comparable in content and learning outcomes to your own courses, unless you give a written basis for denial grounded in your academic standards or curricular requirements.</td><td>34 CFR 602.24(e)(4)</td></tr>
<tr><td><strong>A written reason for every denied course</strong></td><td>If you decline to award credit, the student receives a written rationale specific to each course that does not transfer.</td><td>34 CFR 668.43(c)(4)</td></tr>
<tr><td><strong>Don’t deny credit because of where it came from</strong></td><td>A course can’t be rejected because of the institution where it was completed or the agency that accredits that institution, as long as the agency is recognized by the Secretary.</td><td>34 CFR 602.24(e)(3)</td></tr>
<tr><td><strong>A right to appeal</strong></td><td>Students can appeal a denial within 15 calendar days of receiving your written notification.</td><td>34 CFR 602.24(e)(5)</td></tr>
<tr><td><strong>Tell students before they commit</strong></td><td>When a student provides a transcript on time, tell them the credit you will award, the credit you decline to award, and the estimated time and, when applicable, courses needed to replace what didn’t transfer. This goes to the student in writing (email counts) by the earlier of signing an enrollment agreement, completing registration or making a nonrefundable financial commitment.</td><td>34 CFR 668.43(c)(3) and (c)(5)</td></tr>
<tr><td><strong>Publish the rules</strong></td><td>Your public transfer of credit policy must include the timeline for submitting a transcript for timely review, your transfer criteria, any types of institutions or sources you won’t accept credit from, your articulation agreements, written criteria for credit for prior learning (including military service), and whether you consider non-degree or non-credit work.</td><td>34 CFR 668.43(a)(11)</td></tr>
<tr><td><strong>Weigh comparability and applicability</strong></td><td>Your transfer criteria must consider both the comparability and the applicability of coursework completed elsewhere.</td><td>34 CFR 602.24(e)(2)</td></tr>
</tbody></table>
<p>Accreditors will check. Under 602.24(e), an accrediting agency must confirm, as part of its review for initial accreditation, preaccreditation or renewal, that the institution’s transfer of credit policies include these provisions.</p>
<div class="slide-pair">%(fig3)s%(fig4)s</div>

<h2>When does the new transfer credit rule take effect?</h2>
<p>The rule is effective <strong>July 1, 2027</strong>. The Department designated all sections for early implementation beginning January 1, 2027, but accrediting agencies that adopt provisions early may not impose new requirements on institutions that take effect before July 1, 2027.</p>
<p>July 2027 is closer than it looks, especially with budgets and implementations planned a year ahead.</p>

<h2>Does the rule mean colleges must accept every transfer credit?</h2>
<p>No. The award requirement covers coursework that is comparable in content and learning outcomes to the institution’s own courses, and a college can still decline credit with a written, course-specific basis tied to its academic standards or curricular requirements. In its response to comments, the Department said institutions “must retain academic discretion to evaluate comparability and applicability of coursework.” What changes is that every denial now needs a documented reason, a notice to the student and an appeal path.</p>

<h2>Why it matters: 1.8 million transfer students a year</h2>
<p>According to the Department’s regulatory impact analysis, 1.8 million title IV students transferred institutions between the 2023–24 and 2024–25 award years. About 60%% of them received federal student aid in the year they transferred, a total of $8.8 billion at their new institutions, or roughly $8,300 per transfer student.</p>
<p>Every one of them deserves to know what their past work is worth before they invest in what comes next.</p>

<h2>The hard part isn’t the policy. It’s the workflow.</h2>
<p>Most colleges already have a transfer policy. Far fewer have a process that can deliver all of this for every prospective student, before they register:</p>
<ul>
<li>a course-by-course decision</li>
<li>a written reason for every denial</li>
<li>an estimate of how long it will take to finish</li>
</ul>
<p>That last requirement is the one to underline. It’s not enough to say a course transfers. Colleges now have to show how credit applies: what’s left, and how long it will take. During the comment period, several commenters urged the Department to distinguish <strong>transferability</strong> (whether a course can be accepted for credit) from <strong>applicability</strong> (whether accepted credit applies to specific degree requirements). The final rule effectively asks colleges to answer both.</p>
<p>For registrars and transfer offices already stretched thin, doing this manually at scale will be very hard.</p>
%(fig6)s

<h2>What colleges can do now: five places to start</h2>
<ol>
<li><strong>Map your current workflow.</strong> How long does a transfer evaluation take today, from transcript to decision?</li>
<li><strong>Audit your denial reasons.</strong> Could you give every student a specific written reason today?</li>
<li><strong>Set your transcript deadline.</strong> Decide what “timely” means for your institution, and publish it. Your public policy has to state this timeline under 668.43(a)(11)(i); the Department chose not to set a single federal deadline.</li>
<li><strong>Test your degree applicability.</strong> Can you tell a prospective student how many terms they have left before they enroll?</li>
<li><strong>Plan for appeals.</strong> Who reviews them, and how will you meet the 15-day window?</li>
</ol>
<p>Related reading: <a href="how-to-speed-up-transfer-credit-evaluation.html">why transfer credit takes weeks, and how to fix it</a>, <a href="state-transfer-policies-us-guide.html">state transfer policies across the U.S.</a> and <a href="will-my-credits-transfer-self-service-answer.html">giving students the “will my credits transfer?” answer early</a>.</p>

<h2>A personal note from Chaitanya Saripalli</h2>
<blockquote>As someone who built my own path through education, often far from home, I know what it means to have your past effort recognized, or not. This rule puts students’ time and money at the center of the transfer conversation, where it belongs.</blockquote>
<p>Chaitanya, Founder &amp; CEO of EnlitEDU, shared this analysis on LinkedIn. <a href="%(li_a)s" target="_blank" rel="noopener">Read the original article</a>, see <a href="%(li_c)s" target="_blank" rel="noopener">the carousel</a>, or <a href="https://www.linkedin.com/in/chaitanyasaripalli/" target="_blank" rel="noopener">follow her on LinkedIn</a> and compare notes. Her question for registrars: what part of compliance worries you most?</p>

<h2>How LioraAI helps colleges get ready</h2>
<p>At EnlitEDU, we built LioraAI to give students instant, clear answers about their credits, with staff approving every decision. <a href="../transfer-credit-intelligence.html">LioraAI Transfer Credit Intelligence</a> reads each incoming transcript, matches courses to your catalog using your own transfer rules and past decisions, and gives evaluators a recommendation to approve, edit or flag. Every decision carries its evidence and approver, which is the raw material for course-by-course notices and written denial reasons. Approved credit posts to your SIS without re-keying.</p>
<p>It is already in use: <a href="../case-studies/roane-state-community-college.html">Roane State Community College</a> cut transcript evaluation from 72 hours to less than 5 minutes, <a href="../case-studies/nashville-state-community-college.html">Nashville State Community College</a> brought transcript evaluation to less than 10 minutes, and the <a href="../news/tennessee-board-of-regents-selects-lioraai.html">Tennessee Board of Regents has selected LioraAI</a> for 11 community colleges that are preparing for what’s ahead.</p>
<p>Software doesn’t make an institution compliant on its own. Your transfer policy, transcript deadline and appeal process are still yours to set. LioraAI makes it practical to apply them to every transcript, on time.</p>

<h2>The AIM transfer rule in 8 slides</h2>
<p>Chaitanya’s <a href="%(li_c)s" target="_blank" rel="noopener">LinkedIn carousel</a> summarizes the rule. Select a slide to open it full size.</p>
<div class="slide-gallery">%(gallery)s</div>

<h3>Sources</h3>
<ul class="sources">
<li>U.S. Department of Education, <a href="%(fr)s" target="_blank" rel="noopener">Accreditation, Innovation, and Modernization: The Secretary’s Recognition of Accrediting Agencies; Institutional Eligibility Under the Higher Education Act of 1965, as Amended; Student Assistance General Provisions</a>, final rule, 91 FR 68626, October 30, 2026 (FR Doc. 2026-22174). <a href="%(fr_pdf)s" target="_blank" rel="noopener">Official PDF (govinfo)</a>.</li>
<li>Amended regulations: 34 CFR 602.24(e) (transfer of credit policies) and 34 CFR 668.43(a)(11) and (c) (institutional disclosures), as set out in the final rule.</li>
<li>Implementation dates: Section IV, “Implementation Date of These Regulations,” and transfer data from the regulatory impact analysis (Table 3.1), final rule <a href="%(fr_pi)s" target="_blank" rel="noopener">public-inspection copy</a>.</li>
<li>Chaitanya Saripalli, <a href="%(li_a)s" target="_blank" rel="noopener">The New Federal Transfer Rule Changes the Question Colleges Have to Answer</a>, LinkedIn, November 19, 2026.</li>
<li>Chaitanya Saripalli, <a href="%(li_c)s" target="_blank" rel="noopener">The New Federal Transfer Rule: What Colleges Need to Know</a> (8-slide carousel), LinkedIn, November 19, 2026.</li>
</ul>
<p class="note">This article explains a federal regulation for general information. It is not legal advice; confirm your obligations with your compliance office or counsel.</p>
""" % dict(li_a=LI_ARTICLE, li_c=LI_CAROUSEL, fr=FR_URL, fr_pdf=FR_PDF, fr_pi=FR_PI,
           fig3=_fig(3, "Slide 3: credit decisions need a reason."), fig4=_fig(4, "Slide 4: students must know before they commit."),
           fig6=_fig(6, "Slide 6: the hard part is the workflow."), gallery=_gallery),
 faqs=[
  ("What is the AIM rule?", "The Accreditation, Innovation, and Modernization (AIM) rule is a U.S. Department of Education final rule published October 30, 2026 (91 FR 68626, FR Doc. 2026-22174). It revises accreditation regulations and rewrites the transfer of credit requirements in 34 CFR 602.24(e) and 668.43."),
  ("When does the new federal transfer credit rule take effect?", "July 1, 2027. Accrediting agencies may implement provisions early from January 1, 2027, but they cannot impose new requirements on institutions that take effect before July 1, 2027."),
  ("Do colleges have to accept all transfer credits under the AIM rule?", "No. For undergraduate programs, colleges must award credit for coursework that is comparable in content and learning outcomes to their own courses, unless they give a written, course-specific basis for denial grounded in their academic standards or curricular requirements."),
  ("How long do students have to appeal a transfer credit denial?", "Students must have the opportunity to appeal within 15 calendar days of receiving the institution’s written notification that it declined to award transfer credit, under 34 CFR 602.24(e)(5)."),
  ("What must colleges tell transfer students before they enroll?", "If a student provides a transcript on time, the college must tell the student in writing which credits it will award, which it declines to award, and the estimated time and courses needed to replace them, by the earlier of signing an enrollment agreement, completing registration or making a nonrefundable financial commitment."),
  ("Can a college deny transfer credit because of where it was earned?", "No. Under 34 CFR 602.24(e)(3), transfer credit cannot be denied based on the institution where the coursework was completed or the agency that accredits it, as long as that agency is recognized by the Secretary."),
  ("Does the AIM rule set a transcript submission deadline?", "No single federal deadline. Each institution must publish the timeline by which a transcript must be submitted for timely review, so a prospective student can decide before enrolling, registering or paying."),
  ("Who enforces the new transfer credit requirements?", "Accrediting agencies. As part of initial accreditation, preaccreditation or renewal reviews, an agency must confirm that the institution’s transfer of credit policies meet 34 CFR 602.24(e)."),
  ("What is the difference between transferability and applicability?", "Transferability is whether a course can be accepted for credit. Applicability is whether accepted credit counts toward specific degree requirements. The AIM rule requires transfer criteria to consider both."),
 ],
),
]
