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

GA_PAGES = [
# ------------------------------------------------------------------ GEORGIA HUB
dict(
 path="georgia.html", nav="Georgia Colleges", icon="fa-location-dot", img="campus-columns", img2="registrar-desk",
 title="Transcript & Credit Evaluation Software for Georgia | LioraAI",
 desc="Transcript and credit evaluation software built in metro Atlanta for Georgia colleges: USG Core IMPACTS, TCSG transfer, freshman review and JST.",
 eyebrow="Georgia · Built in metro Atlanta",
 h1="Transcript and Credit Evaluation Software <span class=\"accent\">for Georgia Colleges</span>",
 sub="EnlitEDU serves colleges and universities across the U.S. from its headquarters in Cumming, Georgia. This page covers what’s specific to Georgia institutions: USG Core IMPACTS domains, the TCSG–USG transfer agreement, Georgia Dual Enrollment credit, HOPE-era freshman transcripts and military records from Georgia’s bases.",
 answer=("What is the best transcript evaluation software for Georgia colleges?",
         "LioraAI by EnlitEDU is transcript and credit evaluation software built in metro Atlanta for Georgia colleges. It reads any transcript, applies your institution’s rules, including USG Core IMPACTS domains and the TCSG–USG general education agreement, and sends staff a documented recommendation to approve. Approved credit posts to Banner, Colleague, Workday Student or PeopleSoft."),
 stats=[("Local", "headquarters in Cumming, north metro Atlanta"), ("On site", "demos and workshops anywhere in Georgia"), ("2–4 wks", "typical go-live for standard SIS integrations")],
 sections=[
  ("Who in Georgia uses transcript evaluation software?",
   "<p>Every Georgia institution that admits students evaluates transcripts, but the work looks different by sector:</p><ul>"
   "<li><strong>University System of Georgia (USG) universities and state colleges</strong> evaluate transfer coursework against Core IMPACTS domains and their own major requirements.</li>"
   "<li><strong>The 22 colleges of the Technical College System of Georgia (TCSG)</strong> evaluate incoming credit, credit for prior learning and military training, and prepare students to transfer to USG.</li>"
   "<li><strong>Private and independent colleges</strong> apply their own transfer policy to students arriving from USG, TCSG and out-of-state schools.</li>"
   "<li><strong>Admissions offices</strong> across all three review first-year (freshman) transcripts from Georgia high schools, many of which now include Georgia Dual Enrollment college credit.</li></ul>"),
  ("What makes credit evaluation in Georgia different?",
   "<p>Georgia has rules a generic tool doesn’t know about. LioraAI is configured for them:</p><ul>"
   "<li><strong>USG Core IMPACTS.</strong> The 42-hour general education curriculum is organized into seven domains, and general education credit transfers domain to domain between USG institutions, even when the courses aren’t identical.</li>"
   "<li><strong>The TCSG–USG general education agreement.</strong> Listed TCSG courses map to a direct USG equivalent or to a Core IMPACTS domain, so technical college transfers keep their general education credit.</li>"
   "<li><strong>Georgia Dual Enrollment.</strong> Many first-year applicants arrive with college credit earned in high school, which has to be evaluated as transfer credit.</li>"
   "<li><strong>Two GPAs for freshmen.</strong> The HOPE GPA calculated by the Georgia Student Finance Commission is not the same as your admissions GPA.</li>"
   "<li><strong>Military records.</strong> Georgia law directs USG and TCSG to award credit for relevant military training, and Georgia’s Army, Air Force and Navy installations produce a steady flow of JST and CCAF transcripts.</li></ul>"),
  ("How does LioraAI work for a Georgia registrar’s office?",
   "<p>Transcripts arrive by upload, SFTP or electronic exchange. LioraAI extracts every course, matches it to your catalog and the agreements you’ve configured, and gives evaluators a recommendation with the evidence behind it. Staff approve, edit or flag each course, and approved credit posts to your SIS. Nothing is decided without a person.</p>"
   "<p>Because EnlitEDU is based in north metro Atlanta, Georgia institutions can meet the team in person for discovery, configuration workshops and training, not only on video calls.</p>"),
 ],
 modules=["articulate", "assess", "veterans", "pla", "degree-pathway", "mobility"],
 faqs=[
  ("Does EnlitEDU only work with Georgia colleges?", "No. EnlitEDU serves colleges and universities across the United States, and its first customers are Tennessee community colleges. Being headquartered in metro Atlanta means Georgia institutions can also meet the team in person."),
  ("Is there transcript evaluation software built in Georgia?", "Yes. EnlitEDU, the company behind LioraAI, is headquartered in Cumming, Georgia, in north metro Atlanta. LioraAI evaluates transfer, first-year, military and prior-learning credit for colleges and universities."),
  ("Does LioraAI support USG Core IMPACTS?", "Yes. Core IMPACTS domains can be configured as transfer rules, so general education credit is placed domain to domain as USG policy requires, while major-specific courses are matched course to course."),
  ("Can LioraAI apply the TCSG–USG transfer agreement?", "Yes. The courses listed in the TCSG–USG general education agreement can be loaded as articulation rules, so every TCSG transcript is evaluated against the agreement the same way, by every evaluator."),
  ("Which Georgia student information systems does LioraAI work with?", "Ellucian Banner and Colleague, Workday Student, PeopleSoft Campus Solutions and Jenzabar, plus Slate and Common App on the admissions side."),
  ("Can the EnlitEDU team visit our campus?", "Yes. The team is based in Cumming, Georgia, and can meet in person anywhere in metro Atlanta and across the state for demos, workshops and training."),
  ("Does LioraAI make the final credit decision?", "No. LioraAI drafts recommendations with evidence. Your registrar, evaluators and faculty approve every decision, and each one is recorded in an audit trail."),
 ],
 related=["georgia/atlanta-transcript-evaluation.html", "georgia/transfer-credit-evaluation.html", "georgia/freshman-transcript-evaluation.html", "georgia/military-transcript-evaluation.html"],
 blog=["tcsg-to-usg-transfer-core-impacts-guide", "hope-gpa-vs-admissions-gpa-georgia", "how-to-speed-up-transfer-credit-evaluation"],
 service="Transcript and credit evaluation software for Georgia colleges and universities",
),
# ------------------------------------------------------------------ ATLANTA
dict(
 path="georgia/atlanta-transcript-evaluation.html", nav="Atlanta", icon="fa-city", img="atlanta-skyline", img2="team-collab",
 title="Transcript Evaluation Software in Atlanta, GA | EnlitEDU",
 desc="Transcript evaluation in Atlanta: EnlitEDU builds LioraAI in metro Atlanta, AI transcript and credit evaluation software for colleges, with on-campus demos.",
 eyebrow="Atlanta, Georgia · Local team",
 h1="Transcript Evaluation Software, <span class=\"accent\">Built in Metro Atlanta</span>",
 sub="LioraAI serves colleges and universities nationwide. For Atlanta-area institutions, it turns weeks of manual transcript and transfer credit evaluation into days, and because the EnlitEDU team is based in Cumming, we can sit down with your registrar’s office in person.",
 answer=("Who offers transcript evaluation software in Atlanta?",
         "EnlitEDU, headquartered in Cumming in north metro Atlanta, makes LioraAI: AI-assisted transcript and credit evaluation software for colleges and universities. It evaluates transfer, first-year, military and prior-learning credit with your rules, and the team offers in-person demos and training across the Atlanta area."),
 stats=[("Local", "EnlitEDU headquarters in Cumming, north metro Atlanta"), ("On site", "demos across Fulton, DeKalb, Gwinnett, Cobb and more"), ("Days", "not weeks: evaluation turnaround once live")],
 sections=[
  ("Transcript evaluation for Atlanta institutions",
   "<p>Metro Atlanta has one of the densest concentrations of higher education in the Southeast: research universities, state colleges, technical colleges, HBCUs and private colleges, all exchanging students. That makes transfer credit evaluation a daily job for registrar’s offices from downtown to Gwinnett and Kennesaw. EnlitEDU is an Atlanta-area edtech company that builds software for exactly that job.</p>"
   "<p>LioraAI handles that volume with one set of your rules: transfer credit with <a href=\"../articulate.html\">LioraAI Articulate</a>, first-year applicants with <a href=\"../assess.html\">LioraAI Assess</a>, military records with <a href=\"../veterans.html\">Veterans &amp; JST</a> and work experience with <a href=\"../pla.html\">Prior Learning Assessment</a>.</p>"),
  ("Why work with a local Atlanta team?",
   "<ul><li><strong>In-person discovery.</strong> We map your current evaluation workflow at your desk, not from a slide.</li>"
   "<li><strong>On-site configuration workshops</strong> with your registrar, transfer evaluators and IT.</li>"
   "<li><strong>Training where your staff work</strong>, plus remote support afterwards.</li>"
   "<li><strong>Same time zone, same state rules.</strong> We know USG Core IMPACTS, the TCSG–USG agreement and Georgia Dual Enrollment.</li></ul>"),
  ("Areas we serve in metro Atlanta",
   "<p>We meet institutions across Fulton, DeKalb, Gwinnett, Cobb, Forsyth, Cherokee, Clayton, Henry and Hall counties, and travel statewide to Savannah, Augusta, Columbus, Macon, Athens and beyond. Prefer a call? Every demo is also available online.</p>"),
  ("Looking for a transcript evaluation for yourself?",
   "<p>LioraAI is software for colleges and universities. If you are a student who needs a <strong>foreign transcript or degree evaluated</strong> for admission, licensing or immigration, you need a credential evaluation service, usually a member of NACES. Check which evaluators your college accepts first. Our <a href=\"../transcript-evaluation-near-me.html\">transcript evaluation near me guide</a> explains the difference.</p>"),
 ],
 modules=["articulate", "assess", "veterans", "pla"],
 faqs=[
  ("Is there a transcript evaluation software company in Atlanta?", "Yes. EnlitEDU, the maker of LioraAI, is based in Cumming, Georgia, in north metro Atlanta, and builds transcript and credit evaluation software for colleges and universities."),
  ("Does EnlitEDU serve colleges outside Atlanta and Georgia?", "Yes. LioraAI is used by institutions outside Georgia, and demos are available online anywhere in the U.S. The Atlanta team adds in-person visits for Georgia institutions."),
  ("Can we get an in-person LioraAI demo in Atlanta?", "Yes. The team offers in-person demos and workshops across metro Atlanta, including Fulton, DeKalb, Gwinnett, Cobb, Forsyth, Cherokee, Clayton and Henry counties."),
  ("How long does transcript evaluation take with LioraAI?", "LioraAI evaluates a full transcript in under a minute. Institutions typically move from multi-week manual turnaround to decisions in days once evaluators review recommendations instead of researching every course."),
  ("I’m a student in Atlanta. Can EnlitEDU evaluate my transcript?", "No. EnlitEDU provides software to institutions. Students who need a foreign transcript evaluated should use a credential evaluation service accepted by their college, usually a NACES member."),
  ("How much does transcript evaluation software cost?", "LioraAI is priced by institution size, transcript volume and modules. We provide a written quote after a demo, and qualified institutions can run a proof-of-concept on their own transcripts."),
 ],
 related=["georgia.html", "georgia/freshman-transcript-evaluation.html", "georgia/transfer-credit-evaluation.html", "transcript-evaluation-near-me.html"],
 blog=["how-to-speed-up-transfer-credit-evaluation", "tcsg-to-usg-transfer-core-impacts-guide", "registrar-office-efficiency-technology"],
 service="Transcript evaluation software for colleges in metro Atlanta",
 city=True,
),
# ------------------------------------------------------------------ FRESHMAN
dict(
 path="georgia/freshman-transcript-evaluation.html", nav="Freshman transcripts", icon="fa-graduation-cap", img="student-table", img2="grad-young",
 title="Freshman Transcript Evaluation in Atlanta & Georgia | LioraAI",
 desc="Freshman transcript evaluation for Atlanta and Georgia colleges: GPA standardization, AP/IB/Honors weighting, Georgia Dual Enrollment credit and HOPE-aware review.",
 eyebrow="Georgia admissions · First-year applicants",
 h1="Freshman Transcript Evaluation <span class=\"accent\">for Atlanta and Georgia Colleges</span>",
 sub="Georgia high school transcripts carry weighted GPAs, AP and IB courses, Georgia Dual Enrollment college credit and a separate HOPE GPA. LioraAI Assess reads them all and applies your admissions policy the same way to every first-year (freshman) applicant.",
 answer=("How do Georgia colleges evaluate freshman transcripts?",
         "Georgia admissions offices extract courses and grades from each high school transcript, recalculate a GPA under their own admissions policy, recognize AP, IB, Honors and Dual Enrollment rigor, and evaluate any Dual Enrollment college credit for transfer. LioraAI Assess automates the extraction and applies your documented rules consistently."),
 stats=[("Any scale", "4.0, weighted 5.0 and 100-point, converted with one rule"), ("AP · IB · DE", "rigor recognized by your policy"), ("1 rule", "applied the same way to every applicant")],
 sections=[
  ("Why are Georgia freshman transcripts hard to evaluate consistently?",
   "<ul><li><strong>Different scales.</strong> Georgia and out-of-state high schools report on 4.0, weighted 5.0 and 100-point scales.</li>"
   "<li><strong>Two GPAs.</strong> The HOPE GPA is calculated by the Georgia Student Finance Commission from core courses with its own weighting rules. Your admissions GPA follows your institution’s policy. Mixing them up causes inconsistent decisions.</li>"
   "<li><strong>Dual Enrollment credit.</strong> Georgia Dual Enrollment lets high school students earn college credit, so a first-year applicant may arrive with a college transcript that also needs a transfer evaluation.</li>"
   "<li><strong>Rigor.</strong> AP, IB, Honors and Dual Enrollment courses need to be recognized the same way for every applicant.</li></ul>"),
  ("What does LioraAI Assess do for Atlanta admissions teams?",
   "<p>LioraAI Assess extracts courses, grades and rigor indicators from PDF, scanned and electronic high school transcripts, converts every scale with your documented formula, applies your weighting policy and sends clean records to Slate, Banner or your SIS. Dual Enrollment college coursework is routed to <a href=\"../articulate.html\">LioraAI Articulate</a> for a transfer evaluation, so applicants know what will count before they enroll.</p>"),
  ("Is “freshman” the right word?",
   "<p>Many community and technical colleges say <em>first-year</em> or <em>first-time student</em> rather than freshman. LioraAI follows your terminology. In short: students coming from high school, homeschool or a GED are first-year applicants; anyone bringing credit from another college, at any level, is a transfer student.</p>"),
 ],
 modules=["assess", "articulate", "degree-pathway"],
 faqs=[
  ("What is freshman transcript evaluation?", "It is the review of a first-year applicant’s high school transcript: extracting courses and grades, calculating a GPA under the institution’s admissions policy, recognizing course rigor such as AP, IB, Honors and Dual Enrollment, and checking requirements."),
  ("Is the HOPE GPA the same as an admissions GPA?", "No. The HOPE GPA is calculated by the Georgia Student Finance Commission from core courses for HOPE and Zell Miller eligibility. An institution’s admissions GPA follows its own policy and can differ."),
  ("How should Georgia Dual Enrollment credit be evaluated?", "Dual Enrollment coursework appears on a college transcript and should be evaluated like transfer credit under your institution’s policy, in addition to its role on the high school transcript."),
  ("Can LioraAI handle out-of-state and international freshman transcripts?", "Yes. LioraAI converts out-of-state and international grading scales with your documented rules and flags records that need a credential evaluation service."),
  ("Does LioraAI work with Slate?", "Yes. Evaluated first-year data can be delivered to Slate reader views and to your SIS without re-keying."),
 ],
 related=["georgia.html", "georgia/atlanta-transcript-evaluation.html", "georgia/transfer-credit-evaluation.html", "assess.html"],
 blog=["hope-gpa-vs-admissions-gpa-georgia", "gpa-standardization-problem", "international-transcript-evaluation-first-year-admissions"],
 service="Freshman (first-year) transcript evaluation software for Georgia admissions offices",
),
# ------------------------------------------------------------------ TRANSFER
dict(
 path="georgia/transfer-credit-evaluation.html", nav="Transfer credit", icon="fa-right-left", img="students-group", img2="lecture-talk",
 title="Georgia Transfer Credit Evaluation: TCSG, USG & Core IMPACTS",
 desc="Transfer credit evaluation software for Georgia: apply USG Core IMPACTS and the TCSG–USG agreement consistently, then post credit to your SIS.",
 eyebrow="Georgia transfer · TCSG · USG · Core IMPACTS",
 h1="Transfer Credit Evaluation <span class=\"accent\">Built Around Georgia’s Rules</span>",
 sub="Students move between TCSG technical colleges, USG institutions, private colleges and out-of-state schools every term. For transfer credit evaluation in Georgia, LioraAI Articulate applies Core IMPACTS domains, the TCSG–USG agreement and your own equivalencies to every transcript, so the same course always gets the same answer.",
 answer=("How does transfer credit work between TCSG and USG?",
         "General education courses listed in the TCSG–USG agreement transfer to USG institutions as a direct equivalent or into a Core IMPACTS domain. Within USG, Core IMPACTS credit transfers domain to domain. Courses outside the agreement, such as technical or major courses, are evaluated by the receiving institution under its own policy."),
 stats=[("42 hrs", "USG Core IMPACTS general education"), ("7 areas", "Core IMPACTS credit transfers area to area within USG"), ("22", "colleges in the Technical College System of Georgia")],
 sections=[
  ("How does Core IMPACTS change transfer evaluation?",
   "<p>USG’s Core IMPACTS general education curriculum, in place since 2024, is 42 credit hours across seven areas: Institutional Priority; Mathematics and Quantitative Skills; Political Science and U.S. History; Arts, Humanities and Ethics; Communicating in Writing; Technology, Mathematics and Sciences; and Social Sciences. A course completed in a Core IMPACTS area at one USG institution receives full credit in the same area at another, provided the area carries the same number of credit hours at both.</p>"
   "<p>That simplifies general education, but evaluators still have to place each course in the right domain, handle field-of-study prerequisites, and evaluate everything that falls outside the core.</p>"),
  ("What about TCSG to USG transfer?",
   "<p>USG and TCSG maintain a general education transfer agreement. Listed TCSG courses map either to a direct USG course or to a Core IMPACTS domain. LioraAI loads the agreement as rules, so every TCSG transcript is evaluated against it automatically, and anything not covered is routed to an evaluator with suggestions.</p>"),
  ("Where does Georgia transfer evaluation still slow down?",
   "<ul><li>Technical and occupational courses outside the general education agreement</li><li>Coursework completed before Core IMPACTS took effect</li><li>Private, out-of-state and international transcripts</li><li>Military and prior-learning credit arriving alongside college transcripts</li><li>Re-keying approved credit into Banner or another SIS</li></ul>"
   "<p>These are exactly the cases LioraAI is built for: suggestions with evidence, one review queue and write-back to your SIS.</p>"),
  ("Can students see if their credits will transfer before they apply?",
   "<p>Yes. With <a href=\"../degree-pathway.html\">Student Degree Pathway</a>, prospective transfer students see an indicative estimate based on your real rules, clearly labeled as subject to official review. It answers the question that decides where many Georgia transfer students enroll.</p>"),
 ],
 modules=["articulate", "degree-pathway", "mobility"],
 faqs=[
  ("What is USG Core IMPACTS?", "Core IMPACTS is the University System of Georgia’s general education curriculum: 42 credit hours across seven domains. General education credit transfers domain to domain between USG institutions."),
  ("Do TCSG credits transfer to USG universities?", "General education courses listed in the TCSG–USG transfer agreement do, either as a direct course equivalent or into a Core IMPACTS domain. Other courses are evaluated by the receiving institution."),
  ("How do I know if my credits will transfer in Georgia?", "Check the receiving institution’s transfer equivalency information and the TCSG–USG agreement. Institutions using LioraAI Student Degree Pathway can also give prospective students an indicative estimate before they apply."),
  ("Can LioraAI evaluate transfer credit for Georgia private colleges?", "Yes. Private and independent colleges configure their own transfer policy and equivalencies, and LioraAI applies them to transcripts from USG, TCSG and out-of-state institutions."),
  ("Does LioraAI support reverse transfer in Georgia?", "Yes. Student Mobility Intelligence identifies students who have met a partner college’s associate degree requirements so consent and conferral can begin."),
 ],
 related=["georgia.html", "georgia/atlanta-transcript-evaluation.html", "georgia/military-transcript-evaluation.html", "articulate.html"],
 blog=["tcsg-to-usg-transfer-core-impacts-guide", "will-my-credits-transfer-self-service-answer", "reverse-transfer-associate-degree-explained"],
 service="Transfer credit evaluation software for Georgia (USG and TCSG) institutions",
),
# ------------------------------------------------------------------ MILITARY
dict(
 path="georgia/military-transcript-evaluation.html", nav="Military & JST", icon="fa-medal", img="veteran-smile", img2="veteran-notes",
 title="Military & JST Transcript Evaluation in Georgia | LioraAI",
 desc="JST, CCAF and DD-214 transcript evaluation for Georgia colleges serving students from Fort Benning, Fort Gordon, Fort Stewart, Robins and Moody, with ACE citations.",
 eyebrow="Georgia · Military-connected students",
 h1="Military Transcript Evaluation <span class=\"accent\">for Georgia’s Military-Connected Students</span>",
 sub="Georgia is home to major Army, Air Force, Navy and Marine Corps installations. LioraAI for Veterans & JST turns Joint Services Transcripts and CCAF transcripts into ACE-cited credit recommendations your School Certifying Officials can approve the same day.",
 answer=("How do Georgia colleges evaluate military transcripts?",
         "Georgia colleges review the Joint Services Transcript (Army, Navy, Marine Corps, Coast Guard) or the Community College of the Air Force transcript (Air Force, Space Force), use American Council on Education credit recommendations as a baseline, and decide which courses or electives to award under their own policy. LioraAI drafts that evaluation with ACE citations for staff to approve."),
 stats=[("<60s", "to produce a full JST evaluation"), ("JST · CCAF", "Army, Navy, Marines, Coast Guard, Air Force, Space Force"), ("ACE-cited", "every recommendation shows its source")],
 sections=[
  ("Which Georgia students bring military transcripts?",
   "<p>Service members, veterans and spouses from installations across the state, including Fort Benning near Columbus, Fort Gordon near Augusta, Fort Stewart and Hunter Army Airfield near Savannah, Robins Air Force Base near Warner Robins, Moody Air Force Base near Valdosta, Naval Submarine Base Kings Bay, and Dobbins Air Reserve Base in Marietta. Army and Navy records arrive on the JST; Air Force records arrive on the CCAF transcript.</p>"),
  ("What does Georgia require for military credit?",
   "<p>Georgia law directs the USG Board of Regents and the TCSG State Board to award academic credit for relevant military training and experience, using the Joint Services Transcript and recognized credit recommendations. Each institution still decides how that credit applies to its programs, which is where consistent, documented evaluation matters.</p>"),
  ("How LioraAI helps School Certifying Officials",
   "<ul><li>Reads the JST, CCAF transcript or DD-214 in under a minute</li><li>Aligns every course and occupation to ACE recommendations, with citations</li><li>Maps recommendations to your catalog with your rules</li><li>One SCO review queue with an audit trail for VA and State Approving Agency reviews</li><li>A self-service view so prospective students see likely credit before enrolling</li></ul>"),
 ],
 modules=["veterans", "pla", "articulate"],
 faqs=[
  ("Do Georgia colleges give credit for military training?", "Yes. Georgia law directs USG and TCSG to award academic credit for relevant military training and experience, using the Joint Services Transcript and recognized credit recommendations. Each institution applies it under its own policy."),
  ("What is the difference between a JST and a CCAF transcript?", "The Joint Services Transcript covers the Army, Navy, Marine Corps and Coast Guard. Air Force and Space Force training appears on the Community College of the Air Force transcript. LioraAI evaluates both."),
  ("How long does a military transcript evaluation take with LioraAI?", "LioraAI produces a full JST evaluation in under a minute. School Certifying Officials then review and approve the recommendations, typically the same or next day."),
  ("Does LioraAI decide how much military credit a student receives?", "No. LioraAI drafts recommendations with ACE citations. Your certifying officials, registrar and faculty approve every award."),
 ],
 related=["georgia.html", "georgia/transfer-credit-evaluation.html", "veterans.html", "pla.html"],
 blog=["how-to-evaluate-joint-services-transcript-jst", "prior-learning-assessment-guide", "hbcu-enrollment-transfer-credit-challenges"],
 service="Military (JST and CCAF) transcript evaluation software for Georgia colleges",
),
]

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
  ("Who can evaluate my foreign transcript in Georgia?", "Ask your college which evaluators it accepts. Most require a member of the National Association of Credential Evaluation Services (NACES). Many services work entirely online."),
  ("Does EnlitEDU evaluate individual transcripts?", "No. EnlitEDU provides LioraAI software to colleges and universities, which use it to evaluate their applicants’ and students’ transcripts."),
 ],
)

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
<p>This is the work <a href="../articulate.html">LioraAI Articulate</a> does. It reads the transcript, applies Core IMPACTS placement and the TCSG–USG agreement as rules, suggests matches for everything else with the evidence attached, and lets your evaluators approve, edit or flag each course. Approved credit posts to your SIS. EnlitEDU is based in north metro Atlanta, so Georgia institutions can work through their rule set with us in person.</p>
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
<p><a href="../assess.html">LioraAI Assess</a> automates steps one and two for admissions teams, and <a href="../articulate.html">LioraAI Articulate</a> handles the Dual Enrollment transfer evaluation. See how it works for <a href="../georgia/freshman-transcript-evaluation.html">freshman transcript evaluation in Atlanta and across Georgia</a>.</p>
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
<p>LioraAI is EnlitEDU’s AI evaluation platform. It covers transfer credit, first-year transcripts, military records, credit for prior learning and athlete transcripts in one engine, applies your rules, and posts approved credit to your SIS. Roane State Community College went live on Banner in 18 days. EnlitEDU works with colleges and universities across the U.S. <a href="../request-demo.html">Request a demo</a> with your own transcripts.</p>
""",
 faqs=[
  ("What is transcript evaluation software?", "Software that helps colleges evaluate incoming transcripts: extracting courses and grades, matching them to the institution’s catalog and rules, and recording transfer or admission decisions. Some tools only extract data or manage equivalency tables; AI evaluation platforms draft the evaluation for staff to approve."),
  ("What is the difference between TES and AI transcript evaluation?", "TES from CollegeSource is a research and workflow system for managing course equivalencies. AI evaluation platforms such as LioraAI read the transcript and draft equivalency recommendations with evidence for staff approval. Many institutions use an equivalency database and an evaluation tool together."),
  ("Is AI transcript evaluation accurate?", "Accuracy depends on transcript quality and how well your rules are documented. Look for tools that show confidence levels, route uncertain courses to people and let you test on your own transcripts."),
  ("How long does it take to implement transcript evaluation software?", "Standard SIS integrations typically take two to four weeks; complex setups longer. Ask vendors for recent implementation timelines on your SIS."),
 ],
))
