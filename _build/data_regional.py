# -*- coding: utf-8 -*-
"""Regional landing pages, written national-first (Oct 2026 rewrite).
EnlitEDU serves colleges across the U.S.; each page keeps ONE clearly labelled Georgia section
so the Phase 1 local keywords (Atlanta / Georgia) still have a home, without the page reading Georgia-only."""

GA_PAGES = [
# ------------------------------------------------------------------ HUB (georgia.html)
dict(
 path="georgia.html", nav="Georgia", icon="fa-location-dot", img="campus-columns", img2="registrar-desk",
 title="Transcript & Credit Evaluation Software | Georgia & U.S.",
 desc="LioraAI is transcript and credit evaluation software for colleges across the U.S., from a team headquartered in Cumming, Georgia. Georgia rules included.",
 eyebrow="Headquartered in Georgia · Serving the U.S.",
 h1="Transcript and Credit Evaluation Software, <span class=\"accent\">Headquartered in Georgia</span>",
 sub="EnlitEDU builds LioraAI for colleges and universities across the United States. Our team is based in Cumming, Georgia, so this page also covers what is specific to Georgia institutions, from USG Core IMPACTS to the TCSG–USG transfer agreement.",
 answer=("Is EnlitEDU only for Georgia colleges?",
         "No. LioraAI is transcript and credit evaluation software for colleges and universities across the U.S., and its first customers are Tennessee community colleges. EnlitEDU is headquartered in Cumming, Georgia, so Georgia institutions can also meet the team in person, and Georgia’s transfer rules are already configured."),
 stats=[("U.S.-wide", "colleges and universities in any state"), ("Any SIS", "Banner, Colleague, Workday Student, PeopleSoft, Jenzabar"), ("2-4 weeks", "typical go-live for standard SIS integrations")],
 sections=[
  ("Who uses LioraAI?",
   "<p>Any institution that admits students evaluates transcripts. LioraAI is used by:</p><ul>"
   "<li><strong><a href=\"../who-we-serve/community-colleges.html\">Community and technical colleges</a></strong> evaluating transfer-in credit, prior learning and military training.</li>"
   "<li><strong><a href=\"../who-we-serve/four-year-universities.html\">Four-year universities</a></strong> reviewing first-year applicants and transfer admits.</li>"
   "<li><strong><a href=\"../who-we-serve/state-systems.html\">State systems and consortia</a></strong> applying shared transfer rules across campuses.</li>"
   "<li><strong><a href=\"../who-we-serve/hbcus-and-msis.html\">HBCUs and MSIs</a></strong> serving transfer and returning students with lean teams.</li></ul>"),
  ("How does LioraAI handle each state’s transfer rules?",
   "<p>Every state moves credit differently: common course numbering in Texas and Florida, transfer degrees in California, guaranteed pathways in Tennessee, a shared general education core in Georgia. LioraAI loads your state’s framework and your own equivalencies as rules, applies them to every transcript, and routes everything else to an evaluator with the evidence attached. Our <a href=\"../blog/state-transfer-policies-us-guide.html\">guide to state transfer policies</a> compares five states.</p>"),
  ("What is configured for Georgia institutions?",
   "<p>LioraAI is transcript and credit evaluation software built in metro Atlanta, with Georgia’s own rules ready to use:</p><ul>"
   "<li><strong>USG Core IMPACTS</strong>, the 42-hour general education core whose credit transfers area to area between USG institutions.</li>"
   "<li><strong>The TCSG–USG general education agreement</strong> for students moving from the 22 TCSG colleges.</li>"
   "<li><strong>Georgia Dual Enrollment</strong> college credit on first-year applications, and the separate <strong>HOPE GPA</strong>.</li>"
   "<li><strong>JST and CCAF transcripts</strong> from Georgia’s military installations.</li></ul>"),
  ("How does implementation work?",
   "<p>Demos, configuration workshops and training run online for institutions in any state, and standard SIS integrations typically go live in two to four weeks. Roane State Community College in Tennessee went live on Banner in 18 days. Institutions that prefer to meet in person can request an on-campus visit; it is easiest for campuses in Georgia, near our team.</p>"),
 ],
 modules=["transfer-credit-intelligence", "freshman-intelligence", "veterans", "prior-learning-assessment", "degree-pathway", "mobility"],
 faqs=[
  ("Does EnlitEDU only work with Georgia colleges?", "No. EnlitEDU serves colleges and universities across the United States, and its first customers are Tennessee community colleges. Georgia institutions can also meet the team in person."),
  ("Where is EnlitEDU based?", "EnlitEDU is headquartered at 3840 Windermere Pkwy, Suite 403, Cumming, Georgia 30041, in north metro Atlanta, and works with institutions nationwide."),
  ("Does LioraAI support state-specific transfer rules?", "Yes. Common course numbering, transferable general education blocks, guaranteed pathways and statewide articulation agreements can be configured as rules and applied to every transcript."),
  ("Does LioraAI support USG Core IMPACTS?", "Yes. For Georgia institutions, Core IMPACTS areas and the TCSG–USG agreement are configured as transfer rules, so general education credit is placed area to area as USG policy requires."),
  ("Which student information systems does LioraAI work with?", "Ellucian Banner and Colleague, Workday Student, PeopleSoft Campus Solutions and Jenzabar, plus Slate and Common App on the admissions side."),
  ("Can the EnlitEDU team visit our campus?", "Demos and workshops run online for institutions anywhere in the U.S. In-person visits are available on request and are easiest for campuses in Georgia."),
  ("Does LioraAI make the final credit decision?", "No. LioraAI drafts recommendations with evidence. Your registrar, evaluators and faculty approve every decision, and each one is recorded in an audit trail."),
 ],
 related=[],
 blog=["state-transfer-policies-us-guide", "us-community-college-transfer-statistics", "tcsg-to-usg-transfer-core-impacts-guide"],
 service="Transcript and credit evaluation software for U.S. colleges and universities",
),
# ------------------------------------------------------------------ ATLANTA
dict(
 path="georgia/atlanta-transcript-evaluation.html", nav="Atlanta team", icon="fa-city", img="atlanta-skyline", img2="team-collab",
 title="Transcript Evaluation Software | Atlanta HQ, Serving the U.S.",
 desc="EnlitEDU builds LioraAI transcript and credit evaluation software in metro Atlanta for colleges across the U.S. Online demos anywhere, on-campus visits on request.",
 eyebrow="Atlanta headquarters · Serving the U.S.",
 h1="Transcript Evaluation Software <span class=\"accent\">From a Team in Metro Atlanta</span>",
 sub="LioraAI serves colleges and universities nationwide, turning weeks of manual transcript and transfer credit evaluation into days. Our team works from Cumming, in north metro Atlanta, and meets institutions online anywhere in the U.S. or in person on request.",
 answer=("Who makes transcript evaluation software in Atlanta?",
         "EnlitEDU, an Atlanta-area edtech company headquartered in Cumming, Georgia, makes LioraAI: AI-assisted transcript and credit evaluation software used by colleges and universities across the U.S. It evaluates transfer, first-year, military and prior-learning credit with each institution’s own rules."),
 stats=[("Any state", "colleges and universities nationwide"), ("Online + on site", "demos anywhere; visits on request"), ("Days", "not weeks: evaluation turnaround once live")],
 sections=[
  ("What does LioraAI do for a registrar’s office?",
   "<p>One engine and one set of your rules for every kind of transcript: transfer credit with <a href=\"../transfer-credit-intelligence.html\">LioraAI Transfer Credit Intelligence</a>, first-year applicants with <a href=\"../freshman-intelligence.html\">LioraAI Freshman Intelligence</a>, military records with <a href=\"../veterans.html\">Veterans &amp; JST</a> and work experience with <a href=\"../prior-learning-assessment.html\">Prior Learning Assessment</a>. Evaluators approve every decision, and approved credit posts to your SIS.</p>"),
  ("How do we work with institutions outside Atlanta?",
   "<p>The same way we work with everyone: discovery, configuration workshops and training run online, in your time zone, and standard SIS integrations go live in two to four weeks. Our first customers are community colleges in Tennessee. Roane State went live on Banner in 18 days, and Nashville State cut per-transcript time from 15 minutes to 2.</p>"),
  ("Transcript evaluation in Atlanta: meeting in person",
   "<p>Looking for transcript evaluation software in Atlanta? Because our team is based in Cumming, Atlanta-area institutions can also meet us in person for discovery, workshops and training, and we already know Georgia’s USG Core IMPACTS, the TCSG–USG agreement and Georgia Dual Enrollment.</p>"),
  ("Looking for a transcript evaluation for yourself?",
   "<p>LioraAI is software for colleges and universities. If you are a student who needs a <strong>foreign transcript or degree evaluated</strong> for admission, licensing or immigration, you need a credential evaluation service, usually a member of NACES. Check which evaluators your college accepts first. Our <a href=\"../transcript-evaluation-near-me.html\">transcript evaluation guide</a> explains the difference.</p>"),
 ],
 modules=["transfer-credit-intelligence", "freshman-intelligence", "veterans", "prior-learning-assessment"],
 faqs=[
  ("Is EnlitEDU only for colleges in Atlanta?", "No. EnlitEDU works with colleges and universities across the U.S. The team is headquartered in north metro Atlanta, so Atlanta-area institutions can also meet in person."),
  ("Is there a transcript evaluation software company in Atlanta?", "Yes. EnlitEDU, the maker of LioraAI, is based in Cumming, Georgia, in north metro Atlanta, and builds transcript and credit evaluation software for colleges nationwide."),
  ("Can we get an in-person demo?", "Demos run online for institutions anywhere in the U.S. In-person demos are available on request and are easiest across metro Atlanta and Georgia."),
  ("How long does transcript evaluation take with LioraAI?", "LioraAI evaluates a full transcript in under a minute. Institutions typically move from multi-week manual turnaround to decisions in days once evaluators review recommendations instead of researching every course."),
  ("I’m a student. Can EnlitEDU evaluate my transcript?", "No. EnlitEDU provides software to institutions. Students who need a foreign transcript evaluated should use a credential evaluation service accepted by their college, usually a NACES member."),
  ("How much does transcript evaluation software cost?", "LioraAI is priced by institution size, transcript volume and modules. We provide a written quote after a demo, and qualified institutions can run a proof-of-concept on their own transcripts."),
 ],
 related=[],
 blog=["how-to-speed-up-transfer-credit-evaluation", "us-community-college-transfer-statistics", "registrar-office-efficiency-technology"],
 service="Transcript evaluation software for colleges across the U.S., from metro Atlanta",
 city=True,
),
# ------------------------------------------------------------------ FRESHMAN
dict(
 path="georgia/freshman-transcript-evaluation.html", nav="Freshman transcripts", icon="fa-graduation-cap", img="student-table", img2="grad-young",
 title="Freshman Transcript Evaluation Guide for Colleges | LioraAI",
 desc="How colleges evaluate freshman transcripts: GPA standardization, AP/IB/Honors weighting, dual enrollment credit and state scholarship GPAs such as Georgia’s HOPE.",
 eyebrow="First-year admissions · Nationwide",
 h1="Freshman Transcript Evaluation <span class=\"accent\">for Colleges Across the U.S.</span>",
 sub="High school transcripts arrive on different GPA scales, with AP, IB and dual enrollment credit, and sometimes a separate state scholarship GPA. LioraAI Freshman Intelligence reads them all and applies your admissions policy the same way to every first-year (freshman) applicant, from any state.",
 answer=("How do colleges evaluate freshman transcripts?",
         "Admissions offices extract courses and grades from each high school transcript, recalculate a GPA under their own admissions policy, recognize AP, IB, Honors and dual enrollment rigor, and evaluate any dual enrollment college credit for transfer. LioraAI Freshman Intelligence automates the extraction and applies your documented rules consistently."),
 stats=[("Any scale", "4.0, weighted 5.0 and 100-point, converted with one rule"), ("AP · IB · DE", "rigor recognized by your policy"), ("1 rule", "applied the same way to every applicant")],
 sections=[
  ("Why are freshman transcripts hard to evaluate consistently?",
   "<ul><li><strong>Different scales.</strong> High schools report on 4.0, weighted 5.0 and 100-point scales, and international schools use their own.</li>"
   "<li><strong>More than one GPA.</strong> Some states calculate a separate GPA for state scholarships. Your admissions GPA follows your own policy, and mixing them up causes inconsistent decisions.</li>"
   "<li><strong>Dual enrollment credit.</strong> Dual enrollment students made up 22% of U.S. community college enrollment in 2023–24, so many applicants arrive with a college transcript that also needs a transfer evaluation (see our <a href=\"../blog/dual-enrollment-credit-evaluation-us-colleges.html\">dual enrollment guide</a>).</li>"
   "<li><strong>Rigor.</strong> AP, IB, Honors and dual enrollment courses need to be recognized the same way for every applicant.</li></ul>"),
  ("What does LioraAI Freshman Intelligence do for admissions teams?",
   "<p>LioraAI Freshman Intelligence extracts courses, grades and rigor indicators from PDF, scanned and electronic high school transcripts, converts every scale with your documented formula, applies your weighting policy and sends clean records to Slate, Banner or your SIS. Dual enrollment college coursework is routed to <a href=\"../transfer-credit-intelligence.html\">LioraAI Transfer Credit Intelligence</a> for a transfer evaluation, so applicants know what will count before they enroll.</p>"),
  ("Is “freshman” the right word?",
   "<p>Many community and technical colleges say <em>first-year</em> or <em>first-time student</em> rather than freshman. LioraAI follows your terminology. In short: students coming from high school, homeschool or a GED are first-year applicants; anyone bringing credit from another college, at any level, is a transfer student.</p>"),
  ("Freshman transcript evaluation in Georgia",
   "<p>Two state specifics matter for freshman transcript evaluation in Atlanta and across Georgia: the <strong>HOPE GPA</strong>, calculated by the Georgia Student Finance Commission for scholarship eligibility and distinct from an admissions GPA, and <strong>Georgia Dual Enrollment</strong> college credit. LioraAI handles both; our <a href=\"../blog/hope-gpa-vs-admissions-gpa-georgia.html\">HOPE GPA guide</a> explains the difference.</p>"),
 ],
 modules=["freshman-intelligence", "transfer-credit-intelligence", "degree-pathway"],
 faqs=[
  ("What is freshman transcript evaluation?", "It is the review of a first-year applicant’s high school transcript: extracting courses and grades, calculating a GPA under the institution’s admissions policy, recognizing course rigor such as AP, IB, Honors and dual enrollment, and checking requirements."),
  ("How should dual enrollment credit be evaluated?", "Dual enrollment coursework appears on a college transcript and should be evaluated like transfer credit under your institution’s policy, in addition to its role on the high school transcript."),
  ("Is the HOPE GPA the same as an admissions GPA?", "No. In Georgia, the HOPE GPA is calculated by the Georgia Student Finance Commission from core courses for HOPE and Zell Miller eligibility. An institution’s admissions GPA follows its own policy and can differ."),
  ("Can LioraAI handle out-of-state and international freshman transcripts?", "Yes. LioraAI converts out-of-state and international grading scales with your documented rules and flags records that need a credential evaluation service."),
  ("Does LioraAI work with Slate?", "Yes. Evaluated first-year data can be delivered to Slate reader views and to your SIS without re-keying."),
 ],
 related=[],
 blog=["dual-enrollment-credit-evaluation-us-colleges", "gpa-standardization-problem", "hope-gpa-vs-admissions-gpa-georgia"],
 service="Freshman (first-year) transcript evaluation software for U.S. colleges",
),
# ------------------------------------------------------------------ TRANSFER
dict(
 path="georgia/transfer-credit-evaluation.html", nav="Transfer credit", icon="fa-right-left", img="students-group", img2="lecture-talk",
 title="Transfer Credit Evaluation by State Rules: U.S. & Georgia",
 desc="Transfer credit evaluation that applies state rules, from common course numbering to Georgia’s Core IMPACTS and TCSG–USG agreement, then posts credit to your SIS.",
 eyebrow="Transfer credit · Any state’s rules",
 h1="Transfer Credit Evaluation <span class=\"accent\">Built Around Your State’s Rules</span>",
 sub="Students move between community colleges, universities, private colleges and out-of-state schools every term. LioraAI Transfer Credit Intelligence applies your state’s transfer framework and your own equivalencies to every transcript, so the same course always gets the same answer.",
 answer=("How do state transfer rules affect credit evaluation?",
         "Most states use common course numbering, a transferable general education block, guaranteed pathways or statewide articulation agreements. These settle many in-state, public-to-public decisions in advance, while out-of-state, private, older and military coursework is still evaluated under each institution’s policy. LioraAI loads the state framework and your rules, and routes exceptions to evaluators with evidence."),
 stats=[("31.6%", "of community college starters transfer to a four-year school within six years"), ("~43%", "of credits lost on average by transfer students (GAO)"), ("Any state", "framework configured as rules")],
 sections=[
  ("Where does transfer evaluation slow down?",
   "<ul><li>Courses outside your state’s agreements, such as technical and occupational courses</li><li>Coursework completed under an older general education model or catalog</li><li>Private, out-of-state and international transcripts</li><li>Military and prior-learning credit arriving alongside college transcripts</li><li>Re-keying approved credit into Banner or another SIS</li></ul>"
   "<p>These are exactly the cases LioraAI is built for: suggestions with evidence, one review queue and write-back to your SIS. See <a href=\"../blog/us-community-college-transfer-statistics.html\">what national transfer data shows</a>.</p>"),
  ("How does LioraAI apply state transfer rules?",
   "<p>Common course numbering crosswalks, transferable general education blocks, guaranteed pathways and statewide articulation agreements are loaded once as rules and applied automatically. Your institutional rules sit on top: grade minimums, residency, course age and credit caps. Rules are versioned, so students with older catalog rights keep them. Our <a href=\"../blog/state-transfer-policies-us-guide.html\">state transfer policy guide</a> compares Florida, Texas, California, Tennessee and Georgia.</p>"),
  ("Transfer credit evaluation in Georgia: TCSG, USG and Core IMPACTS",
   "<p>For transfer credit evaluation in Georgia, two frameworks do most of the work. USG’s Core IMPACTS general education curriculum, in place since 2024, is 42 credit hours across seven areas; a course completed in an area at one USG institution receives full credit in the same area at another, provided the area carries the same hours at both. The TCSG–USG general education agreement maps listed courses from the 22 TCSG colleges to a direct USG course or a Core IMPACTS area. LioraAI applies both as rules and routes everything else to an evaluator.</p>"),
  ("Can students see if their credits will transfer before they apply?",
   "<p>Sooner than before. Because <a href=\"../transfer-credit-intelligence.html\">LioraAI Transfer Credit Intelligence</a> drafts each evaluation in minutes against your real rules, institutions can give prospective transfer students a documented credit answer early, with staff approving every decision. That answer often decides where a transfer student enrolls.</p>"),
 ],
 modules=["transfer-credit-intelligence", "degree-pathway", "mobility"],
 faqs=[
  ("How do I know if my credits will transfer?", "Check the receiving institution’s transfer equivalency information and any state agreement that applies. Institutions using LioraAI can return a documented evaluation quickly, often before the student commits."),
  ("Can LioraAI apply my state’s transfer rules?", "Yes. Common course numbering, general education blocks, guaranteed pathways and articulation agreements from any state can be configured as rules, alongside your own equivalencies."),
  ("What is USG Core IMPACTS?", "Core IMPACTS is the University System of Georgia’s general education curriculum: 42 credit hours across seven areas. General education credit transfers area to area between USG institutions."),
  ("Do TCSG credits transfer to USG universities?", "In Georgia, general education courses listed in the TCSG–USG transfer agreement do, either as a direct course equivalent or into a Core IMPACTS area. Other courses are evaluated by the receiving institution."),
  ("Does LioraAI support reverse transfer?", "Yes. Student Mobility Intelligence identifies students who have met a partner college’s associate degree requirements so consent and conferral can begin."),
 ],
 related=[],
 blog=["state-transfer-policies-us-guide", "us-community-college-transfer-statistics", "tcsg-to-usg-transfer-core-impacts-guide"],
 service="Transfer credit evaluation software that applies each state’s transfer rules",
),
# ------------------------------------------------------------------ MILITARY
dict(
 path="georgia/military-transcript-evaluation.html", nav="Military & JST", icon="fa-medal", img="veteran-smile", img2="veteran-notes",
 title="Military Transcript Evaluation Guide: JST & CCAF | LioraAI",
 desc="How colleges evaluate JST, CCAF and DD-214 records with ACE recommendations and state military-credit rules, with School Certifying Official review.",
 eyebrow="Military-connected students · Nationwide",
 h1="Military Transcript Evaluation <span class=\"accent\">for Military-Connected Students</span>",
 sub="Service members, veterans and military spouses enroll at colleges in every state. LioraAI for Veterans & JST turns Joint Services Transcripts and CCAF transcripts into ACE-cited credit recommendations your School Certifying Officials can approve the same day.",
 answer=("How do colleges evaluate military transcripts?",
         "Colleges review the Joint Services Transcript (Army, Navy, Marine Corps, Coast Guard) or the Community College of the Air Force transcript (Air Force, Space Force), use American Council on Education credit recommendations as a baseline, and decide which courses or electives to award under their own policy and any state rules. LioraAI drafts that evaluation with ACE citations for staff to approve."),
 stats=[("<1 minute", "to produce a full JST evaluation"), ("JST · CCAF", "Army, Navy, Marines, Coast Guard, Air Force, Space Force"), ("ACE-cited", "every recommendation shows its source")],
 sections=[
  ("Which records do military-connected students bring?",
   "<p>Army, Navy, Marine Corps and Coast Guard training appears on the Joint Services Transcript (JST). Air Force and Space Force training appears on the Community College of the Air Force (CCAF) transcript. Veterans may also bring a DD-214. Each needs to be matched to ACE recommendations and then to your catalog. Our guide to <a href=\"../blog/how-to-evaluate-joint-services-transcript-jst.html\">reading a JST</a> walks through it.</p>"),
  ("How LioraAI helps School Certifying Officials",
   "<ul><li>Reads the JST, CCAF transcript or DD-214 in under a minute</li><li>Aligns every course and occupation to ACE recommendations, with citations</li><li>Maps recommendations to your catalog with your rules</li><li>One SCO review queue with an audit trail for VA and State Approving Agency reviews</li><li>A self-service view so prospective students see likely credit before enrolling</li></ul>"),
  ("Military transcript evaluation in Georgia",
   "<p>Georgia law directs the USG Board of Regents and the TCSG State Board to award credit for relevant military training. Georgia’s installations, including Fort Benning, Fort Gordon, Fort Stewart, Robins Air Force Base and Moody Air Force Base, produce a steady flow of JST and CCAF transcripts. LioraAI applies those rules alongside each institution’s own policy.</p>"),
 ],
 modules=["veterans", "prior-learning-assessment", "transfer-credit-intelligence"],
 faqs=[
  ("Do colleges have to give credit for military training?", "Many states direct public colleges to award credit for relevant military training; Georgia, for example, directs USG and TCSG to do so. Each institution decides how that credit applies to its programs under its own policy."),
  ("What is the difference between a JST and a CCAF transcript?", "The Joint Services Transcript covers the Army, Navy, Marine Corps and Coast Guard. Air Force and Space Force training appears on the Community College of the Air Force transcript. LioraAI evaluates both."),
  ("How long does a military transcript evaluation take with LioraAI?", "LioraAI produces a full JST evaluation in under a minute. School Certifying Officials then review and approve the recommendations, typically the same or next day."),
  ("Does LioraAI decide how much military credit a student receives?", "No. LioraAI drafts recommendations with ACE citations. Your certifying officials, registrar and faculty approve every award."),
 ],
 related=[],
 blog=["how-to-evaluate-joint-services-transcript-jst", "prior-learning-assessment-guide", "state-transfer-policies-us-guide"],
 service="Military (JST and CCAF) transcript evaluation software for U.S. colleges",
),
]

NEAR_ME_PATCH = dict(
 title="Transcript Evaluation Near Me: Which Service Do You Need?",
 desc="Searching “transcript evaluation near me”? See which you need: LioraAI software for colleges across the U.S., or a credential evaluation for your own transcript.",
 sub="“Transcript evaluation” means two different things. Colleges evaluate thousands of transcripts to award credit. Individuals get one transcript evaluated, usually a foreign degree. Here’s how to find the right help, wherever you are.",
 answer=("Where can I get a transcript evaluation near me?",
         "If you are a college or university anywhere in the U.S., EnlitEDU provides LioraAI transcript evaluation software, with online demos in every state and in-person visits on request from its metro Atlanta team. If you are a student who needs your own foreign transcript or degree evaluated, use a credential evaluation service accepted by your college, usually a NACES member; most work online, so location rarely matters."),
)
