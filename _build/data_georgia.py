# -*- coding: utf-8 -*-
"""Phase 1 local SEO / GEO / AEO content: Georgia and metro Atlanta."""

COUNTIES = ["Fulton", "DeKalb", "Gwinnett", "Cobb", "Forsyth", "Cherokee", "Clayton", "Henry", "Hall"]
GA_CITIES = ["Atlanta", "Savannah", "Augusta", "Columbus", "Macon", "Athens", "Valdosta", "Albany", "Rome", "Dalton"]

# Shared "local trust" facts
LOCAL = dict(
    hq="Cumming, Georgia (Forsyth County, north metro Atlanta)",
    street="3840 Windermere Pkwy, Suite 403", city="Cumming", region="GA", zip="30041",
    maps="https://www.google.com/maps/search/?api=1&query=3840+Windermere+Pkwy+Suite+403+Cumming+GA+30041",
)

from data_regional import GA_PAGES, NEAR_ME_PATCH  # national-first rewrite (Oct 2026)

NEAR_ME = dict(
 path="transcript-evaluation-near-me.html",
 title="Transcript Evaluation Near Me: Atlanta Guide | EnlitEDU",
 desc="Searching “transcript evaluation near me” in Atlanta? See which service you need: software for colleges (LioraAI) or a credential evaluation for your own transcript.",
 h1="Transcript Evaluation Near Me: <span class=\"accent\">Which One Do You Need?</span>",
 sub="“Transcript evaluation” means two different things. Colleges evaluate thousands of transcripts to award credit. Individuals get one transcript evaluated, usually a foreign degree. Here’s how to find the right help in Atlanta and across Georgia.",
 answer=("Where can I get a transcript evaluation near me in Atlanta?",
         "If you are a college or university, EnlitEDU in north metro Atlanta provides LioraAI transcript evaluation software and in-person demos. If you are a student who needs your own foreign transcript or degree evaluated, use a credential evaluation service accepted by your college, usually a NACES member; most work online, so location rarely matters."),
 faqs=[
  ("What is transcript evaluation?", "Transcript evaluation is reviewing a student’s academic record to decide what it means at another institution: which courses transfer, how grades convert and how much credit applies. Colleges do it for admission and transfer; credential evaluators do it for foreign transcripts."),
  ("How long does transcript evaluation take?", "At colleges, manual transfer evaluations often take three to eight weeks. With LioraAI, a transcript is evaluated in under a minute and staff typically approve decisions in days. Credential evaluation services for foreign transcripts set their own processing times."),
  ("How much does a transcript evaluation cost?", "For individuals, credential evaluation services charge per report and publish their own fees. For colleges, LioraAI is priced by institution size, volume and modules."),
  ("Who can evaluate my foreign transcript?", "Ask your college which evaluators it accepts. Most require a member of the National Association of Credential Evaluation Services (NACES). Many services work entirely online."),
  ("Does EnlitEDU evaluate individual transcripts?", "No. EnlitEDU provides LioraAI software to colleges and universities, which use it to evaluate their applicants’ and students’ transcripts."),
 ],
)

NEAR_ME.update(NEAR_ME_PATCH)

GA_GLOSSARY = [
 ("Core IMPACTS (Georgia)", "The University System of Georgia’s general education curriculum: 42 credit hours across seven areas. Credit completed in an area at one USG institution counts in the same area at another, even when courses are not identical.", ["transfer-credit-evaluation", "tcsg-usg-transfer-agreement-georgia"]),
 ("TCSG–USG transfer agreement (Georgia)", "An agreement between the Technical College System of Georgia and the University System of Georgia that maps listed TCSG general education courses to direct USG equivalents or Core IMPACTS areas.", ["core-impacts-georgia", "articulation-agreement"]),
 ("HOPE GPA (Georgia)", "The GPA the Georgia Student Finance Commission calculates from core high school courses to determine HOPE and Zell Miller Scholarship eligibility. It uses its own weighting rules and can differ from an institution’s admissions GPA.", ["gpa-standardization", "georgia-dual-enrollment"]),
 ("Georgia Dual Enrollment", "Georgia’s program, formerly Move On When Ready, that lets high school students take college courses for credit, with tuition paid by the Georgia Student Finance Commission. The college credit must be evaluated when the student enrolls elsewhere.", ["transfer-credit-evaluation", "first-year-freshman-applicant"]),
]

GA_FAQ_GROUP = ("Where we work", [
 ("Where does EnlitEDU work?", "With colleges and universities across the United States. Demos, implementation and training run online for institutions in any state, and the team is headquartered in Cumming, Georgia, in north metro Atlanta."),
 ("Does LioraAI support state-specific transfer rules?", "Yes. State transfer agreements, common course numbering, guaranteed pathways and general education frameworks, such as Georgia’s USG Core IMPACTS and the TCSG–USG agreement, can be configured as rules and applied to every transcript."),
 ("Can we meet the EnlitEDU team in person?", "Demos and workshops run online for institutions anywhere in the U.S. In-person visits are available on request and are easiest for institutions in Georgia, where the team is based."),
 ("Where is EnlitEDU headquartered?", "At 3840 Windermere Pkwy, Suite 403, Cumming, Georgia 30041, in Forsyth County, north metro Atlanta."),
 ("Can individuals use EnlitEDU to evaluate their own transcripts?", "No. EnlitEDU provides software to institutions. Individuals who need a foreign transcript evaluated should use a credential evaluation service accepted by their college."),
])

# --------------------------------------------------------------- native Georgia blog posts
GA_POSTS = [
dict(
 slug="tcsg-to-usg-transfer-core-impacts-guide",
 title="TCSG to USG Transfer Under Core IMPACTS: A Plain-English Guide for Georgia Registrars",
 desc="How general education credit moves from Georgia’s technical colleges to USG under Core IMPACTS, where it slows down, and how to keep it consistent.",
 sub="Core IMPACTS made general education transfer in Georgia simpler on paper. Here is what actually changed for the people evaluating TCSG transcripts, and what still takes time.",
 date="2026-10-07", tag="Transfer Credit", mins=7, img="students-group", region="Georgia",
 keywords="TCSG to USG transfer, Core IMPACTS transfer, TCSG USG articulation agreement, Georgia transfer credit evaluation, USG general education transfer",
 body="""
<div class="takeaways"><h2>Key takeaways</h2><ul>
<li>USG Core IMPACTS is 42 hours of general education across seven domains, and that credit transfers domain to domain between USG institutions.</li>
<li>The TCSG–USG agreement maps listed technical college courses to a USG course or a Core IMPACTS domain.</li>
<li>The slow cases are everything outside the agreement: technical courses, older coursework, private and out-of-state transcripts, and military credit.</li>
<li>Writing the agreement down as rules, once, is what makes evaluation consistent across evaluators and terms.</li>
</ul></div>
<p>If you work in a Georgia registrar’s office, you’ve probably had some version of this conversation: a student finishes general education at a technical college, transfers to a university in the system, and wants to know why one of their courses landed as an elective instead of where they expected. Core IMPACTS was supposed to make that conversation rarer. It mostly has. But not entirely, and the gaps are worth understanding.</p>
<h2>What is Core IMPACTS, in one paragraph?</h2>
<p>Core IMPACTS is the University System of Georgia’s general education curriculum. Since 2024 it has been 42 credit hours arranged in seven areas, which spell the name: Institutional Priority; Mathematics and Quantitative Skills; Political Science and U.S. History; Arts, Humanities and Ethics; Communicating in Writing; Technology, Mathematics and Sciences; and Social Sciences. The important part for transfer is the rule that sits on top of it: a course completed in a Core IMPACTS area at one USG institution receives full credit in the same area at another, as long as that area carries the same number of hours at both schools, even if the receiving school doesn’t teach an identical course.</p>
<h2>How do technical college courses fit in?</h2>
<p>USG and the Technical College System of Georgia maintain a general education transfer agreement. TCSG courses on the list map either to a direct USG course or to a Core IMPACTS domain. So a student who completes listed general education courses at one of the 22 TCSG colleges carries that credit into the right domain at a USG institution.</p>
<p>That is the part that works well. The friction is everywhere else.</p>
<h2>Where does TCSG to USG evaluation still slow down?</h2>
<ul>
<li><strong>Courses that aren’t on the list.</strong> Technical and occupational courses usually fall outside the general education agreement, so someone has to decide whether they count as electives, toward a major, or not at all.</li>
<li><strong>Older coursework.</strong> Students returning after several years bring courses completed under the previous core curriculum, which have to be placed under today’s rules.</li>
<li><strong>Mixed transcripts.</strong> A typical transfer student might bring TCSG courses, a semester from a private college, a course from another state and military training. Each source follows different rules.</li>
<li><strong>Field-of-study prerequisites.</strong> Beyond the 42 core hours, majors require their own prerequisites, and those still need course-level decisions.</li>
<li><strong>Re-keying.</strong> Even a perfect decision has to be entered into Banner or another SIS by hand in many offices.</li>
</ul>
<blockquote>The agreement tells you where general education credit goes. It doesn’t tell you what to do with the other half of the transcript.</blockquote>
<h2>How do you keep evaluations consistent?</h2>
<p>The offices that handle this well do one thing in common: they write their decisions down as rules instead of keeping them in an evaluator’s head. In practice that means three layers:</p>
<ol>
<li><strong>System rules.</strong> Core IMPACTS domain placement and the TCSG–USG agreement, loaded once and applied automatically.</li>
<li><strong>Institutional rules.</strong> Your own equivalencies, grade minimums, residency and course-age limits.</li>
<li><strong>Precedent.</strong> When an evaluator decides how an unlisted course transfers, that decision becomes the default the next time the same course appears.</li>
</ol>
<p>With those three layers in place, the second student from the same technical college with the same course gets the same answer as the first, in minutes.</p>
<h2>Where software fits</h2>
<p>This is the work <a href="../transfer-credit-intelligence.html">LioraAI Transfer Credit Intelligence</a> does. It reads the transcript, applies Core IMPACTS placement and the TCSG–USG agreement as rules, suggests matches for everything else with the evidence attached, and lets your evaluators approve, edit or flag each course. Approved credit posts to your SIS. EnlitEDU is based in north metro Atlanta, so Georgia institutions can work through their rule set with us in person.</p>
""",
 faqs=[
  ("Do TCSG general education courses transfer to USG?", "Courses listed in the TCSG–USG general education agreement transfer as a direct USG equivalent or into a Core IMPACTS domain. Other courses are evaluated by the receiving institution."),
  ("How many hours is USG Core IMPACTS?", "Core IMPACTS is 42 credit hours of general education arranged across seven domains."),
  ("What happens if a receiving USG institution doesn’t have the same course?", "Core IMPACTS credit transfers domain to domain, so the credit counts in the same domain even if the courses are not identical."),
  ("Why do some technical college courses transfer as electives?", "Technical and occupational courses usually fall outside the general education agreement, so the receiving institution decides under its own policy whether they count toward a major, as electives or not at all."),
 ],
),
dict(
 slug="hope-gpa-vs-admissions-gpa-georgia",
 title="HOPE GPA vs. Admissions GPA: What Georgia Admissions Offices Should Know",
 desc="Georgia freshman applicants carry two GPAs: the HOPE GPA calculated by GSFC and your admissions GPA. Why they differ and why it matters.",
 sub="Every Georgia high school senior has more than one GPA. For admissions offices, keeping the HOPE GPA and your own admissions GPA separate is the first step to evaluating freshman transcripts fairly.",
 date="2026-10-07", tag="Admissions", mins=6, img="student-table", region="Georgia",
 keywords="HOPE GPA vs admissions GPA, HOPE GPA Georgia, freshman transcript evaluation Georgia, Georgia dual enrollment transcript, weighted GPA Georgia",
 body="""
<div class="takeaways"><h2>Key takeaways</h2><ul>
<li>The HOPE GPA is calculated by the Georgia Student Finance Commission for scholarship eligibility, not for admission.</li>
<li>It uses core courses only, removes high school weighting, then adds half a point to B, C, D and F grades in AP, IB and Dual Enrollment core courses.</li>
<li>Your admissions GPA follows your institution’s policy and can be higher or lower than the HOPE GPA.</li>
<li>Dual Enrollment credit appears on a college transcript too, and needs a transfer evaluation.</li>
</ul></div>
<p>Ask a Georgia high school senior for their GPA and you might get three different numbers: the weighted GPA on their transcript, the unweighted one, and their HOPE GPA from GAfutures. Ask an admissions office which one it uses and the honest answer should be “none of those, exactly: we calculate our own.” Here’s why that distinction matters.</p>
<h2>What is the HOPE GPA?</h2>
<p>The HOPE GPA is calculated by the Georgia Student Finance Commission (GSFC) to decide eligibility for the HOPE and Zell Miller Scholarships. It uses core curriculum courses: English, math, science, social science and foreign language. Any weighting the high school added is removed, and then half a point is added back to grades of B, C, D and F in AP, IB and degree-level Dual Enrollment core courses. An A stays at 4.0. Students need at least a 3.0 HOPE GPA, along with rigor course requirements. GSFC publishes the current rules, and they are worth checking each year.</p>
<h2>Why isn’t the HOPE GPA your admissions GPA?</h2>
<p>Because it answers a different question. HOPE asks “is this student eligible for state scholarship funds?” Your admissions policy asks “how well prepared is this student for our programs?” Your institution may include different courses, weight rigor differently, or recalculate from scratch for every applicant regardless of state. Out-of-state and international applicants don’t have a HOPE GPA at all, so relying on it would treat Georgia applicants differently from everyone else.</p>
<blockquote>Use the HOPE GPA for what it’s for. Evaluate the transcript under your own policy.</blockquote>
<h2>Where Dual Enrollment complicates things</h2>
<p>Georgia Dual Enrollment, formerly Move On When Ready, lets high school students take college courses with tuition paid by GSFC. Many first-year applicants now arrive with a semester or more of college credit. That coursework does two jobs: it appears on the high school transcript, and it appears on a college transcript that has to be evaluated like any other transfer credit. Offices that only look at the high school side miss telling the student what will count toward their degree.</p>
<h2>How to keep freshman evaluation consistent</h2>
<ol>
<li><strong>Document your admissions GPA formula</strong>, including which courses count and how AP, IB, Honors and Dual Enrollment are weighted.</li>
<li><strong>Apply it to every applicant</strong>, Georgia and out-of-state, with the same conversion for 4.0, 5.0 and 100-point scales.</li>
<li><strong>Evaluate Dual Enrollment college credit</strong> through your transfer process so the student knows what applies before orientation.</li>
<li><strong>Keep the HOPE GPA in its lane</strong> as a financial aid data point.</li>
</ol>
<p><a href="../freshman-intelligence.html">LioraAI Freshman Intelligence</a> automates steps one and two for admissions teams, and <a href="../transfer-credit-intelligence.html">LioraAI Transfer Credit Intelligence</a> handles the Dual Enrollment transfer evaluation. See how it works for <a href="../georgia/freshman-transcript-evaluation.html">freshman transcript evaluation in Atlanta and across Georgia</a>.</p>
""",
 faqs=[
  ("Who calculates the HOPE GPA?", "The Georgia Student Finance Commission calculates the HOPE GPA from a student’s core high school courses to determine HOPE and Zell Miller Scholarship eligibility."),
  ("Is the HOPE GPA weighted?", "High school weighting is removed, then half a point is added to grades of B, C, D and F in AP, IB and degree-level Dual Enrollment core courses. An A remains 4.0."),
  ("Should colleges use the HOPE GPA for admission?", "Most institutions calculate their own admissions GPA under their own policy so that Georgia, out-of-state and international applicants are evaluated consistently."),
  ("Do Georgia Dual Enrollment credits count as transfer credit?", "Dual Enrollment coursework appears on a college transcript and is evaluated under the receiving institution’s transfer policy."),
 ],
),
]

GA_POSTS.append(dict(
 slug="how-to-choose-transcript-evaluation-software",
 title="How to Choose Transcript Evaluation Software: A Buyer’s Checklist for Colleges",
 desc="What to look for in transcript evaluation software: formats, rules, human review, explainability, SIS write-back, FERPA, security and vendor questions.",
 sub="Transcript evaluation software ranges from equivalency databases to AI that drafts the whole evaluation. Here is a practical checklist for registrars, admissions leaders and IT teams comparing options.",
 date="2026-10-07", tag="Technical Insights", mins=8, img="team-collab",
 keywords="transcript evaluation software, transfer credit evaluation software, AI transcript evaluation, credit evaluation software, how to choose transcript evaluation software",
 body="""
<div class="takeaways"><h2>Key takeaways</h2><ul>
<li>Decide first what you need automated: data entry, equivalency lookup, or the evaluation itself.</li>
<li>Insist on human approval, visible evidence for every suggestion, and an audit trail.</li>
<li>SIS write-back and security documentation (FERPA, DPA, SOC 2, HECVAT) separate pilots from production tools.</li>
<li>Test with your own transcripts, including the messy ones.</li>
</ul></div>
<p>Most registrar’s offices start looking for transcript evaluation software after a peak season that went badly: a backlog, a few students who enrolled elsewhere while they waited, and evaluators doing the same research they did last term. The market can look crowded, because “transcript evaluation software” covers several different kinds of tools. Sorting them out first saves a lot of demo time.</p>
<h2>What kinds of transcript evaluation software are there?</h2>
<ul>
<li><strong>Equivalency databases and workflow tools</strong> (sometimes called transcript review software). Systems such as CollegeSource’s Transfer Evaluation System (TES) help staff research course descriptions, track evaluations and manage equivalency tables.</li>
<li><strong>Document capture.</strong> Intelligent capture products extract data from transcript documents so staff don’t key it by hand.</li>
<li><strong>CRM add-ons.</strong> Admissions CRMs increasingly include transcript extraction or evaluation agents inside the admissions workflow.</li>
<li><strong>AI evaluation platforms.</strong> Tools such as DegreeSight and EnlitEDU’s LioraAI read the transcript, recommend equivalencies, and leave approval to staff.</li>
</ul>
<p>None of these is wrong. They automate different parts of the job, so the right choice depends on where your time actually goes.</p>
<h2>What should a transcript evaluation tool do?</h2>
<ol>
<li><strong>Read every format you receive</strong>: PDF, scanned paper, EDI/SPEEDE and PESC XML, high school and college, domestic and international, plus the JST and CCAF transcript if you serve military students.</li>
<li><strong>Apply your rules, not a generic table.</strong> Grade minimums, residency, credit caps, course age, articulation agreements and state transfer frameworks, such as common course numbering, guaranteed pathways or Georgia’s USG Core IMPACTS.</li>
<li><strong>Show its work.</strong> Every suggestion should come with the evidence: matched course descriptions, the rule applied, your prior decisions.</li>
<li><strong>Keep people in charge.</strong> Staff and faculty approve, edit or override every decision.</li>
<li><strong>Write back to your SIS.</strong> If approved credit still has to be re-keyed into Banner, Colleague, Workday Student or PeopleSoft, a large part of the time savings disappears.</li>
<li><strong>Keep an audit trail</strong> of evidence, rule version, recommendation and approver for appeals and accreditation.</li>
</ol>
<h2>What security and privacy questions should you ask?</h2>
<ul>
<li>Will you sign a Data Processing Agreement, and act as a FERPA school official under our direct control?</li>
<li>Can you share a SOC 2 report or bridge letter and a completed HECVAT?</li>
<li>Is student data ever used to train general-purpose or commercial AI models?</li>
<li>Where is data hosted, and how is it encrypted in transit and at rest?</li>
</ul>
<blockquote>The best test is your own transcripts. Ask every vendor to run twenty of your recent ones, including the messy scans.</blockquote>
<h2>Questions to ask in every demo</h2>
<ul>
<li>How long did your last three implementations take, on which SIS?</li>
<li>What happens when the tool isn’t confident about a course?</li>
<li>Can we talk to a customer at an institution like ours?</li>
<li>How is pricing structured: per transcript, per student or by institution size?</li>
</ul>
<h2>Where LioraAI fits</h2>
<p>LioraAI is EnlitEDU’s AI evaluation platform. It covers transfer credit, first-year transcripts, military records, and credit for prior learning in one engine, applies your rules, and posts approved credit to your SIS. Roane State Community College went live on Banner in 18 days. EnlitEDU works with colleges and universities across the U.S. <a href="../request-demo.html">Request a demo</a> with your own transcripts.</p>
""",
 faqs=[
  ("What is transcript evaluation software?", "Software that helps colleges evaluate incoming transcripts: extracting courses and grades, matching them to the institution’s catalog and rules, and recording transfer or admission decisions. Some tools only extract data or manage equivalency tables; AI evaluation platforms draft the evaluation for staff to approve."),
  ("What is the difference between TES and AI transcript evaluation?", "TES from CollegeSource is a research and workflow system for managing course equivalencies. AI evaluation platforms such as LioraAI read the transcript and draft equivalency recommendations with evidence for staff approval. Many institutions use an equivalency database and an evaluation tool together."),
  ("Is AI transcript evaluation accurate?", "Accuracy depends on transcript quality and how well your rules are documented. Look for tools that show confidence levels, route uncertain courses to people and let you test on your own transcripts."),
  ("How long does it take to implement transcript evaluation software?", "Standard SIS integrations typically take two to four weeks; complex setups longer. Ask vendors for recent implementation timelines on your SIS."),
 ],
))
