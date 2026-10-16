# -*- coding: utf-8 -*-
"""Open roles. Add a dict to JOBS to publish a new role: build.py creates careers/<slug>.html with an application form
and Google for Jobs (JobPosting) structured data, and lists it on careers.html. Remove it (or set open=False) to close it."""

ABOUT_ENLITEDU = ("EnlitEDU is a growing AI-powered higher education technology company transforming how colleges and universities process "
                  "academic transcripts, evaluate transfer credits and streamline student enrollment workflows. Our LioraAI platform helps "
                  "institutions automate manual processes, improve operational efficiency and accelerate student enrollment decisions.")

JOBS = [
dict(
 slug="technical-implementation-manager", open=True,
 title="Technical Implementation Manager",
 location="Remote", remote=True, applicant_country="US",
 employment="Full-time", employment_schema="FULL_TIME",
 experience="5-8+ years", experience_months=60, reports_to="CEO / CTO",
 posted="2026-10-16", valid_through="2027-01-14",
 summary="Lead client implementations of LioraAI at colleges and universities, coordinate our developers and QA, and make sure every go-live lands on time.",
 intro="We are looking for a highly accountable, hands-on Technical Implementation Manager to lead client implementations, coordinate internal technical teams and ensure successful delivery of our solutions.",
 responsibilities=[
  ("Client implementation and delivery", [
   "Own end-to-end implementation of EnlitEDU solutions across multiple colleges and universities.",
   "Lead client onboarding, requirements gathering, project planning, configuration, testing and go-live activities.",
   "Develop and maintain implementation timelines, milestones, deliverables and resource plans.",
   "Serve as the primary point of contact for clients throughout implementation.",
   "Proactively identify risks, resolve blockers and manage client expectations.",
   "Ensure timely and successful implementations with minimal executive intervention."]),
  ("Technical team coordination", [
   "Coordinate day-to-day activities across developers, QA, product and technical resources.",
   "Lead daily scrum meetings, sprint planning and implementation status reviews.",
   "Assign and track deliverables, ensuring clear ownership and accountability.",
   "Identify technical dependencies, bottlenecks and resource constraints.",
   "Work closely with the CTO to resolve technical challenges and prioritize delivery.",
   "Ensure development commitments are completed on schedule."]),
  ("Technical and product understanding", [
   "Develop a strong understanding of EnlitEDU’s AI-powered transcript processing and transfer credit evaluation platform.",
   "Understand client requirements and translate them into actionable technical tasks.",
   "Coordinate integrations with higher education systems such as Ellucian Banner, Colleague, PeopleSoft, Workday and Slate.",
   "Work with APIs, SFTP, data mapping and system integration workflows.",
   "Participate in technical troubleshooting and solution discussions.",
   "Be comfortable reviewing technical approaches and working hands-on when needed."]),
  ("Resource and delivery management", [
   "Manage multiple concurrent client implementations and internal priorities.",
   "Assess team capacity and identify additional technical resource needs.",
   "Recommend staffing requirements, including senior developers, QA engineers or integration specialists.",
   "Monitor project progress, resource utilization and delivery performance.",
   "Establish clear processes for task management, escalation and accountability."]),
  ("Quality assurance and go-live readiness", [
   "Coordinate functional testing, integration testing and user acceptance testing (UAT).",
   "Ensure client requirements are validated before production deployment.",
   "Manage go-live checklists, production readiness and post-launch stabilization.",
   "Coordinate resolution of implementation-related defects.",
   "Ensure proper technical documentation and handoff to support teams."]),
  ("Client communication and stakeholder management", [
   "Conduct weekly client implementation meetings and provide clear progress updates.",
   "Communicate timelines, risks, dependencies and decisions professionally.",
   "Build strong relationships with institutional IT, admissions, registrar and enrollment teams.",
   "Escalate critical issues with proposed solutions rather than simply reporting problems."]),
 ],
 required=[
  "5-8+ years of experience in technical project management, SaaS implementations or software delivery.",
  "Experience managing software development teams and multiple client implementations.",
  "Strong understanding of Agile/Scrum methodologies.",
  "Technical familiarity with APIs, databases, data integrations and cloud-based SaaS platforms.",
  "Experience translating business requirements into technical deliverables.",
  "Excellent communication, organizational and problem-solving skills.",
  "Ability to independently manage priorities and drive projects to completion.",
  "Strong sense of ownership, urgency and accountability."],
 preferred=[
  "Experience in higher education technology or EdTech SaaS.",
  "Familiarity with student information systems (Banner, Colleague, PeopleSoft, Workday) and Slate CRM.",
  "Background in software development, systems integration or solution architecture.",
  "Experience coordinating distributed or offshore engineering teams.",
  "Understanding of AI/ML-based products and document processing workflows.",
  "Familiarity with Jira, Azure DevOps or similar project management tools."],
 success=[
  ("First 30 days", ["Understand EnlitEDU products, client implementations and development workflows.",
                     "Take ownership of daily scrum and project tracking.",
                     "Establish visibility into all active implementations, blockers and milestones."]),
  ("First 60 days", ["Independently manage client implementation meetings and delivery schedules.",
                     "Establish consistent accountability across development teams.",
                     "Improve sprint predictability and implementation reporting."]),
  ("First 90 days", ["Own all active client implementations from kickoff through go-live.",
                     "Proactively manage resources, risks and client expectations.",
                     "Reduce the CEO’s involvement in routine delivery coordination.",
                     "Establish a repeatable, scalable implementation process."]),
 ],
 ideal=("We are looking for someone who is more than a project coordinator. The ideal candidate is a proactive, technically capable "
        "delivery leader who takes ownership, anticipates problems, drives teams toward results and ensures commitments are met. "
        "This person should be comfortable in a fast-growing startup where priorities evolve, initiative is valued and successful execution matters."),
 skills=["Technical project management", "SaaS implementation", "Agile/Scrum", "APIs", "SFTP", "Data mapping", "System integration",
         "Ellucian Banner", "Ellucian Colleague", "PeopleSoft", "Workday", "Slate", "UAT", "Jira", "Azure DevOps"],
),
]
