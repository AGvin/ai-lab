# Documentation Requirements

## Scenario Fit

- Present this scenario for a school, district, college, university, research/teaching institution, or comparable education organization selecting AI for teaching, learning, research support, student services, and institutional operations.
- Keep the scenario organization-scale. A single learner belongs in personal routes; one teacher/researcher belongs in the relevant professional scenario; broad regulatory or high-security architecture belongs in `regulated-organization/` or `high-security-environment/` when those constraints dominate.
- The defining constraints are **learner age, educational purpose, academic integrity, student-record privacy, institutional identity/admin controls, accessibility/equity, curriculum and assessment design, teacher/faculty oversight, research integrity, and high-impact student decisions**.
- Distinguish K-12, higher education, adult/professional education, and research environments. Their age, consent, privacy, assessment, and governance boundaries can differ materially.
- Do not turn this page into pedagogy policy or legal advice. It owns the AI model/workspace route and acceptance controls for educational use.

## Educational Purpose Before Model Choice

- Define the intended role before choosing a model or product:
  - student tutor/practice partner;
  - writing/coding/math/language assistance;
  - teacher/faculty lesson and material preparation;
  - formative feedback;
  - assessment creation;
  - grading/rubric support;
  - research/discovery/synthesis;
  - accessibility/accommodation support;
  - advising/student services;
  - administrative knowledge/workflow assistance;
  - institutional data analysis;
  - software/research engineering;
  - creative/media production.
- Do not use one campus-wide `AI assistant` configuration as proof that all educational use cases have the same risk or acceptance threshold.
- Preserve the learning objective: a model that completes the work too well can be pedagogically unsuitable when the objective is for the learner to practice the underlying skill.
- Evaluate whether AI should explain, scaffold, critique, provide hints, generate examples, or produce a final answer for each instructional context.

## Managed Education Workspace as the Default Shared Route

- Prefer an institution-managed education/enterprise AI workspace when broad student/faculty/staff access is intended and hosted processing is permitted.
- Current ChatGPT Edu provides institution-managed workspaces with SSO, SCIM, group/role controls, GPT management, advanced tools, and enterprise privacy controls; treat exact models, limits, apps, exports, residency, and admin behavior as mutable.
- Current Google Workspace for Education provides Gemini access under education-domain administration with education-license-dependent features and enterprise-grade data protections; Google states that school-account Gemini chats/uploads are not reviewed by humans or used to improve generative models under the applicable education protections.
- Treat these products as examples of current managed routes, not permanent recommendations.
- Compare the exact institution plan/account configuration, not a personal consumer account with the same brand name.

## Personal vs Institution-Managed Accounts

- Keep student/faculty personal AI accounts distinct from institution-managed accounts.
- Institutional data, student records, research data, course materials, confidential feedback, or internal documents should use the approved managed account/configuration when policy requires institutional control.
- Current managed ChatGPT account behavior gives administrators control over managed-account data according to organization settings and agreements; personal accounts remain separately governed.
- Do not assume that switching between personal and institutional accounts transfers governance, retention, permissions, or data ownership automatically.
- Provide clear user guidance so staff and students understand which account to use for which data classes.

## Learner Age and Access

- Treat age as a first-class model/product-access constraint.
- Verify provider minimum-age rules, education-account eligibility, parental/guardian or school authorization requirements, jurisdictional child-privacy rules, and institution policy before enabling direct learner use.
- Current education AI products can expose age-dependent features; exact feature restrictions and account eligibility are mutable and must be checked at deployment time.
- Do not infer that an institutional license makes every AI capability appropriate for every age group.
- Use age-appropriate interaction design, safety controls, curriculum framing, and human supervision for minors.
- Preserve teacher/guardian/institution escalation paths for harmful, unsafe, or developmentally inappropriate interactions.

## Student Records and Privacy

- Classify student information before model use: identity/contact, enrollment, grades, assessment submissions, attendance, accommodations/disability, behavior/discipline, advising, financial aid, health/counseling, demographic data, research participation, and other education records.
- Apply the institution's current jurisdiction-specific privacy rules and contractual obligations rather than a generic global privacy assumption.
- In the United States, FERPA-related use of online services can require institution control over education-record PII and restrictions on disclosure/reuse; U.S. Department of Education guidance explicitly recommends checking institution approval before classroom use of services that collect student-record PII.
- Do not upload broad student datasets when de-identified, aggregated, pseudonymized, or minimal fields satisfy the objective.
- Treat generated embeddings, classifications, summaries, risk labels, and feedback tied to identifiable students as potentially sensitive student data.
- Keep secrets, authentication material, payment details, and unrelated personal data out of model context.

## Data Processing Boundary

- Map the complete path for prompts, files, LMS/SIS data, connected apps, search, retrieval indexes, model inference, logs, exports, feedback, and agent tools.
- Verify provider training/data-use defaults, retention, admin access, export, connected-app permissions, regional/residency options, subprocessors, and optional features for the exact education plan.
- Current ChatGPT Edu/business-data controls include no-training-by-default and configurable retention/residency/admin controls for eligible configurations; exact eligibility varies.
- Current Google Workspace for Education Gemini protections apply to school-account use under the applicable Workspace license; feature/data handling varies by license and age.
- Do not assume a web-search, plugin/app, external API, model router, or browser extension inherits the core education workspace's privacy boundary.

## Institution Identity and Administration

- Prefer institution-managed SSO/domain identity, lifecycle provisioning/deprovisioning, role/group access, and centralized policy.
- Separate student, faculty, researcher, teaching assistant, staff, administrator, contractor, guest, and service/workload identities where permissions differ.
- Current ChatGPT Edu supports enterprise identity/admin capabilities such as SSO/SCIM/group permissions; current managed education suites similarly provide domain administration.
- Test offboarding, role changes, course completion, graduation, guest/affiliate access, and temporary accounts.
- Do not make course or institutional data accessible solely because an AI workspace member can discover a connector.

## Course and Classroom Data Boundary

- Treat each course/class/cohort as a meaningful permission/context boundary when course materials or student work are connected.
- Preserve LMS/course permissions for assignments, feedback, grades, discussions, recordings, and roster data.
- Do not expose one student's work, feedback, accommodations, or grades to another student through retrieval or shared assistant memory.
- Separate instructor-only materials such as answer keys, grading rubrics, exam banks, moderation notes, and future assessments from student-accessible sources.
- Test direct and indirect attempts to retrieve restricted course material.

## Academic Integrity Policy

- Define institution/course-specific allowed and prohibited AI assistance instead of relying on the model to infer academic-integrity rules.
- Separate uses such as brainstorming, tutoring, translation, citation discovery, code explanation, editing, full drafting, answer generation, and assessment completion.
- Require instructors to communicate allowed AI use for each assessment where policy expects it.
- Do not treat AI use itself as misconduct without the applicable course/institution policy and evidence.
- Preserve an appeal/review path for academic-integrity decisions.

## AI Detection Is Not Proof

- Do not use an AI-text/code detector as the sole basis for accusing a student of misconduct.
- Treat detector outputs as uncertain signals requiring appropriate evidence and human process.
- Prefer assessment design, process evidence, version history, oral explanation, source verification, and student/instructor review over opaque authorship probabilities.
- Evaluate detector error across languages, writing ability, disability/accommodation, and non-native speakers if such tools are used at all.
- Do not present a numerical detector score as a factual authorship determination.

## Assessment Design

- Decide whether the assessment measures unaided recall/skill, AI-assisted professional practice, critical evaluation of AI, process, collaboration, or another objective.
- If AI is prohibited, design the assessment environment and instructions accordingly rather than relying only on post-hoc detection.
- If AI is allowed, define what must remain student-authored and what evidence of process/citations/tool use is required.
- Use oral defense, iterative drafts, version history, in-class components, personalized data/tasks, or reflective explanation where they support the learning objective.
- Do not let broad AI capability invalidate an assessment silently; redesign when the model can trivially complete the intended skill test.

## Grading and Feedback

- Use AI for rubric drafting, formative feedback, comment suggestions, clustering common errors, or first-pass review only under a defined faculty policy and validation process.
- Keep final grades and consequential academic judgments human/institution controlled unless a deterministic approved scoring process is already authoritative.
- Preserve the official rubric, answer key, learning outcomes, and accommodation rules outside model memory.
- Validate AI-generated feedback against representative student work before scaling.
- Do not allow a model to penalize writing style, dialect, disability-related expression, or cultural variation that is outside the rubric.
- Require instructor review for ambiguous, high-stakes, or appeal-prone grading.

## Tutoring and Learning Assistance

- Evaluate tutoring on whether it improves learning rather than whether it produces correct final answers quickly.
- Test hinting/scaffolding behavior, misconception detection, Socratic questioning where appropriate, explanation quality, source correctness, level adaptation, and refusal to bypass course policy.
- Configure the tutor to ask what the learner has tried and to support the learning objective when direct answer delivery would undermine practice.
- Do not let an AI tutor become the only support path for struggling students.
- Provide human instructor/tutor escalation for persistent misunderstanding, welfare concerns, or accommodations.

## Factual and Source Grounding

- Require current authoritative sources for policies, course rules, schedules, academic requirements, campus services, research procedures, and other institutional facts.
- Do not let model memory answer current registrar, admissions, financial-aid, policy, safety, or program-requirement questions when authoritative systems exist.
- Preserve source links/IDs and effective dates for material institutional guidance.
- Route live transactional facts such as enrollment, balance, grades, holds, and registration through deterministic SIS/ERP APIs rather than document RAG when possible.

## Accessibility and Accommodations

- Evaluate AI as a support tool for captioning, transcription, summarization, reading-level adaptation, language support, alternative explanations, drafting assistance, or accessible content generation where permitted.
- Keep formal accommodation decisions and disability documentation with qualified institutional processes.
- Do not infer disability or accommodation need from student behavior or model analysis.
- Validate generated captions, alt text, translations, equations, diagrams, and accessible documents against applicable accessibility requirements.
- Provide non-AI alternatives when AI tooling creates an accessibility or technology barrier.

## Equity and Digital Access

- Evaluate differences in device access, bandwidth, language, disability access, subscription availability, model limits, and AI literacy across students.
- Do not design required coursework around a premium personal AI subscription unless the institution provides equivalent access or an alternative.
- Test the chosen route on institution-standard student devices and networks.
- Account for usage quotas/rate limits during peak assignment/exam periods.
- Preserve alternatives for students who cannot or should not use a specific AI feature.

## Multilingual Education

- Evaluate each target language on curriculum terminology, instruction quality, translation fidelity, names/numbers, citations, and assessment policy.
- Do not infer equal pedagogical quality across all supported interface languages from provider language-count claims.
- Use qualified/native review for high-stakes translated course/policy/assessment content.
- Preserve approved glossaries and source materials for recurring multilingual teaching.

## Teacher and Faculty Workflows

- Use AI for lesson/lecture planning, examples, quizzes, rubric drafts, slide/text drafting, feedback preparation, coding/data demonstrations, literature discovery, and administrative summaries when source and policy boundaries permit.
- Require faculty review for factual accuracy, curriculum alignment, level, copyright/license, accessibility, and assessment integrity.
- Do not publish model-generated course facts, readings, citations, or answer keys without verification.
- Preserve approved course materials in institutional systems rather than personal chat history.

## Research and Scholarship

- Treat AI-assisted research under normal research-integrity, citation, authorship, data-governance, IRB/ethics, sponsor, publication, and disciplinary standards.
- Route detailed research evidence methodology to `professionals/researcher/` or `teams/research-and-insights-team/` while applying institution research policy here.
- Do not fabricate citations, datasets, experimental results, quotations, participant information, or source provenance.
- Distinguish AI assistance from authorship/accountability according to publisher/funder/institution rules.
- Protect unpublished research, participant data, intellectual property, export-controlled material, and sponsor-confidential data under the appropriate route.

## Research Computing and Coding

- Route coding/model-development work to software-engineering scenarios and fixed hardware to the hardware-selection journey.
- Keep research environments, repositories, data platforms, HPC/GPU resources, and reproducibility artifacts authoritative.
- Do not let a coding agent modify shared research datasets or analysis pipelines without version control and project verification.
- Preserve exact software/model/data versions for reproducible research where material.

## Admissions, Advising, and Student Services

- Use AI for general information retrieval, FAQ, appointment preparation, document summarization, and staff drafting under current authoritative policy/data.
- Treat admissions, financial aid, disciplinary, disability accommodation, academic standing, progression, and other decisions materially affecting students as higher-risk.
- Do not let generative model output become the sole basis for eligibility, admission, aid, discipline, grading, or progression decisions when institution policy/law requires deterministic criteria or human review.
- Preserve decision rules, evidence, human ownership, and appeal/reconsideration paths.
- Avoid generating unsupported promises about acceptance, scholarship, credits, graduation, or immigration/status matters.

## Student Wellbeing and Sensitive Topics

- Do not position a general education assistant as a substitute for qualified counseling, healthcare, safeguarding, crisis, legal, or disability services.
- Define escalation and campus/local support paths for safety/wellbeing disclosures according to institution policy.
- Minimize sensitive counseling/health data exposure to general-purpose models.
- Do not infer mental-health diagnoses or disciplinary risk from ordinary student interactions.

## Connected Apps and Institutional Knowledge

- Use connected LMS, Drive/SharePoint, email, calendars, knowledge bases, libraries, or repositories only with institution approval and permission preservation.
- Current managed ChatGPT app controls support admin configuration, user authorization, permission preservation, and stronger action consent; treat exact apps/actions as mutable.
- Separate retrieval/read access from write actions such as sending messages, editing files, creating calendar items, or changing records.
- Treat course documents, email, web pages, and connected content as untrusted prompt-injection inputs when tools/actions are available.

## Student/Faculty Custom Assistants

- Allow institution/course custom assistants/GPTs/Gems/agents only under a governance model that defines owner, audience, source data, instructions, tools, retention, update responsibility, and retirement.
- Do not allow an instructor-built assistant to expose restricted answer keys, student records, or unpublished research through broad sharing.
- Review shared assistants after course rollover or staff departure.
- Distinguish pedagogical configuration from authoritative institutional policy.

## Agentic Actions

- Treat agents that modify SIS/LMS records, send student communications, schedule appointments, change course materials, create grades/comments, submit forms, approve requests, or operate research infrastructure as side-effecting systems.
- Start with read/search/draft/proposal workflows.
- Apply least privilege, explicit destination, student/course identity, deterministic validation, approval gates, idempotency, logs, and rollback/reconciliation for writes.
- Do not grant a teaching assistant or student-facing agent administrative system scopes beyond the educational task.
- Require stronger approval for grades, enrollment, financial aid, discipline, accommodations, access rights, external communications, or research/system changes.

## Prompt Injection and Student-Provided Content

- Treat student submissions, discussion posts, uploaded documents, code, websites, emails, and external sources as potentially adversarial instructions when an agent can access tools or privileged context.
- Student-provided text must not reveal answer keys, grades, other students' data, instructor notes, system prompts, or administrative secrets.
- Keep authoritative instructions/tool policy outside retrieved student content.
- Include prompt-injection cases in evaluation for LMS/retrieval/grading/agent workflows.

## Copyright, Course Materials, and Generated Media

- Verify rights/licenses for readings, textbooks, publisher content, lecture recordings, images, music, student work, research materials, and datasets before upload or reuse.
- Technical upload access does not prove permission to use content for AI processing or redistribution.
- Review generated course media/text for factual accuracy, attribution, licensing, accessibility, and inappropriate resemblance/reproduction where relevant.
- Preserve original sources and approved final materials.

## Institutional AI Literacy

- Provide students and staff practical guidance on model limitations, hallucinations, source verification, privacy, prompt injection, academic-integrity rules, copyright, and when human expertise is required.
- Teach learners to inspect sources and reasoning evidence rather than equating fluent output with truth.
- Distinguish current product behavior from enduring AI concepts because models/features change rapidly.
- Include role-specific training for faculty, administrators, researchers, and students rather than one generic tutorial.

## Evaluation Suite

- Build a versioned institution evaluation set covering representative educational roles and risk levels:
  - student tutoring;
  - course factual question;
  - writing/coding assistance;
  - assessment-policy boundary;
  - instructor content generation;
  - grading/feedback suggestion;
  - accessibility/language task;
  - research/citation task;
  - student-services question;
  - restricted student-data case;
  - prompt-injected student document;
  - side-effecting action requiring approval where used.
- Score factual/source correctness, pedagogy/learning fit, privacy/permission leakage, academic-integrity adherence, harmful bias, accessibility, escalation, teacher correction time, latency, and cost.
- Evaluate separately for age groups, courses/disciplines, languages, and user roles where performance can differ.
- Re-run after model, provider, workspace controls, course policy, connector, retrieval source, or agent-action changes.

## Human Oversight and Appeals

- Define who owns material AI-assisted educational decisions: instructor, department, registrar/admissions/aid office, research PI, student-services professional, or another accountable role.
- Preserve meaningful human review for grades, misconduct, admissions, aid, accommodations, progression, discipline, safeguarding, and other high-impact decisions.
- Provide a process for students to challenge an AI-influenced decision or incorrect record where institution policy/law requires it.
- Do not use `human in the loop` as nominal approval if the reviewer lacks the evidence/time/authority to detect errors.

## Monitoring and Change Management

- Monitor usage, incidents, data leakage, prompt injection, unsupported content, grade/feedback corrections, accessibility problems, policy violations, quotas, cost, and provider/model changes as relevant.
- Maintain approved-provider/model/feature lists and re-evaluate after major model/workspace/control changes.
- Pilot new high-impact uses with bounded courses/groups before institution-wide rollout.
- Keep rollback/disable paths for models, apps, custom assistants, and agents.
- Do not auto-enable new provider features for all users without checking age/data/pedagogy/action implications.

## Cost per Accepted Educational Outcome

- Compare **total cost per accepted educational outcome**: licenses/API/credits, support/admin, identity/integration, faculty training, curriculum/assessment redesign, accessibility work, review/correction, privacy/security governance, research compute, and student-equity impact.
- A managed institution workspace can be economically stronger than reimbursing personal subscriptions when identity/admin/privacy/support matter.
- A cheaper model can be more expensive if faculty/student correction burden or pedagogical failure is high.
- Do not measure success only by messages generated or time saved; include learning quality, accepted work, staff burden, access/equity, and error consequences.

## Local and Private Routes

- Use local/private inference when student/research data boundaries, offline teaching/research, sovereignty, or institution infrastructure justify it and exact model/runtime/hardware passes evaluation.
- Keep institutional identity, course/data permissions, assessment policy, and authoritative systems unchanged as governance owners.
- Local inference does not remove child/privacy, academic-integrity, accessibility, prompt-injection, model-license, security, or evaluation requirements.
- Route shared model gateway/runtime operations to `internal-ai-platform/`; route disconnected/air-gapped environments to `high-security-environment/`.

## Escalation Triggers

- Move to this scenario when AI use spans institution-managed students/faculty/staff, courses, student records, academic policy, or educational operations.
- Move to `regulated-organization/` when formal sector/privacy/audit obligations become the dominant cross-institution architecture concern.
- Move to `high-security-environment/` when disconnected/sovereign research or sensitive networks dominate.
- Move to `internal-ai-platform/` when centralized model gateway/runtime/portfolio engineering becomes the primary problem.
- Keep research, software engineering, data analysis, knowledge retrieval, and media-specific acceptance in their scenario owners while applying the education governance layer.
- Do not recommend a route when it cannot satisfy both the learning/operational objective and the required student-data/age/integrity controls.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local school/lab/research inference target materially constrains model selection.
- Use `../../../hardware/sub/computers/`, `../../../hardware/sub/servers/`, `../../../hardware/sub/single-board/`, or `../../../hardware/sub/embedded/` according to the actual institution-owned target.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link student privacy/regulatory governance to `catalog/models/selection/user-scenarios/organizations/regulated-organization` where it becomes organization-wide compliance architecture.
- Link central model platform operations to `catalog/models/selection/user-scenarios/organizations/internal-ai-platform`.
- Link disconnected research/teaching environments to `catalog/models/selection/user-scenarios/organizations/high-security-environment`.
- Link research, software development, data analysis, knowledge, and creative workflows to their canonical scenario/decision owners rather than duplicating them here.
- Link named education AI services/models to canonical catalog owners only when materialized/current.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party ChatGPT Edu/managed-account/enterprise-privacy/admin-control documentation, current Google Workspace for Education Gemini data-protection/age-feature documentation, current U.S. Department of Education Student Privacy Policy Office guidance for education-record privacy and approved online educational services, and UNESCO guidance for human-centred, age-appropriate, privacy-conscious generative AI in education and research.
- Current evidence establishes institution-managed AI workspaces with centralized identity/admin/privacy controls and education-specific account/age behavior, while education privacy guidance emphasizes institution control over student-record data and UNESCO guidance emphasizes privacy, age appropriateness, ethical validation, pedagogy, and human agency.
- Education products/models/features, age eligibility, quotas, connected apps/actions, data handling, retention/residency, regulations, academic-integrity policies, and institutional rules are mutable; recheck them before rendering current guidance.
- The institution's learning objectives, current policies/law, student-data governance, qualified faculty/staff review, and measured educational outcomes remain the acceptance authority.

## Validation

- K-12, higher education, adult/professional education, and research contexts are not collapsed into one age/privacy/assessment model.
- Institution-managed accounts are distinguished from personal consumer AI accounts.
- Learner age, student-record privacy, course permissions, academic integrity, accessibility, and equity are first-class model-route constraints.
- AI detection is not treated as proof of academic misconduct.
- Assessment design and tutoring preserve the intended learning objective instead of optimizing only answer completion.
- Grades, admissions, aid, discipline, accommodations, progression, and other high-impact student decisions retain meaningful human/institutional authority.
- Student submissions and connected course content cannot expand agent authority or leak restricted material.
- Research and institutional facts preserve source/provenance/currentness rather than model memory.
- Local/private operation does not remove educational privacy/integrity/accessibility requirements.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
