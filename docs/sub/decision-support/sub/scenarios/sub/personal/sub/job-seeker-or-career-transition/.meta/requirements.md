# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual actively seeking a job, changing career direction, returning to work, or repositioning existing experience for a new role/industry.
- Keep the decision centered on the **end-to-end personal job-search context**: vacancy discovery, company/role research, CV/resume tailoring, portfolio/application material, interview practice, application tracking, privacy, budget, and truthfulness all affect the useful model route.
- Distinguish this scenario from `everyday-home-user/`: occasional help rewriting a CV is ordinary personal use; this scenario applies when job search or career transition is a sustained workflow whose research, document, interview, and tracking requirements materially shape model choice.
- Distinguish it from professional work scenarios: the user is acting as an applicant/career changer, not processing employer/client confidential data as part of their current job.
- Distinguish it from `personal-data-analysis/`: application-pipeline metrics can be one subtask, but that scenario becomes the owner only when structured-data analysis itself dominates the decision.
- Do not turn this page into employment/legal advice, recruiter tooling, or an ATS-optimization manual. It owns model-route selection for the individual applicant.

## Separate the Job-Search Workloads

- Classify the recurring work before selecting one assistant/model:
  - vacancy discovery and requirement extraction;
  - company, team, product, and industry research;
  - fit/gap analysis against the user's real experience;
  - CV/resume restructuring and role-specific tailoring;
  - cover letters, application questions, outreach, and follow-up drafts;
  - portfolio/case-study/project description refinement;
  - interview-question generation and mock interviews;
  - technical/behavioral interview preparation;
  - salary/market research where reliable current sources exist;
  - application tracking and next-action planning;
  - career-transition skill-gap planning and learning-roadmap support.
- Do not force every workload into one model. Web research, document editing, voice interview simulation, spreadsheet/application tracking, deterministic reminders, and local/private drafting can use different components.
- Keep the authoritative copies of the CV, portfolio, job description, submitted application, interview schedule, and application status outside conversational memory.

## Default Managed Route

- Use one current managed assistant with strong document handling and current web/search capability as the default starting route when hosted processing fits the user's data boundary.
- Current canonical examples include ChatGPT and Gemini; Claude can remain a credible document/drafting alternative when its current product capabilities fit the user's workflow. Do not rank them globally from benchmark reputation.
- Evaluate candidates on the user's actual job-search tasks: parse one real vacancy, compare it against the source CV, produce a truthful targeted revision, research the employer from primary/current sources, generate interview questions, and explain every material change.
- Prefer one primary assistant so the user maintains a consistent workflow and source set. Add a second service only when it repeatedly produces a distinct accepted-result advantage such as stronger research, document editing, voice interaction, or ecosystem fit.
- Treat exact model names, quotas, paid-plan features, web/deep-research limits, file limits, voice features, and regional availability as mutable service facts.

## Vacancy and Employer Research

- Treat vacancy/company research as a **current-information workflow**, not a model-memory task.
- Prefer the employer's current careers page, official job posting, product/company site, regulatory filing, official engineering/blog material, or other primary source for material claims about the role or company.
- Use reputable secondary sources for context only when needed and distinguish them from employer-owned claims.
- Current ChatGPT Deep Research can search the public web or selected sites, use uploaded files/connected read sources, and return a report with citations/source links. Current Gemini Deep Research can combine Google Search with uploaded files and selected connected sources. Treat availability/limits as mutable.
- For a specific vacancy, preserve the original job description and date captured. Roles can be edited, closed, reposted, or copied incorrectly by aggregators.
- Verify location, remote/hybrid expectations, employment type, seniority, required language, compensation where published, application deadline, work authorization, and other material constraints against a current source before investing in tailoring.
- Do not infer hidden hiring criteria, company culture, team quality, or interview process as fact from generic model knowledge.

## CV and Resume Tailoring

- Use the user's **source-of-truth CV/profile** as the factual boundary. Every generated bullet, skill, role, date, metric, certification, project, technology, responsibility, and achievement must be traceable to information the user actually supplied or explicitly confirmed.
- Never fabricate experience to satisfy a vacancy. If a requirement is missing, present it as a gap, adjacent transferable skill, learning target, or interview question rather than inventing evidence.
- Tailor emphasis and terminology only when truthful. Matching terminology from the job description can improve clarity, but do not keyword-stuff or claim that a particular wording will reliably “beat the ATS.”
- Ask the model to show material edits and the evidence each edit came from when correctness matters. The user should be able to distinguish factual transformation from newly proposed wording.
- Preserve measurable claims exactly unless the user verifies a revised value. Do not turn vague responsibilities into invented percentages, revenue, latency, user counts, team sizes, or other metrics.
- Keep a canonical master CV plus role-specific derived versions so an accepted edit for one vacancy does not silently rewrite the factual source used for later applications.

## Application Questions and Written Materials

- Use the assistant to draft from verified user facts, the exact vacancy, and the target organization's current context.
- Avoid generic praise and unsupported claims such as “I have always admired your company” unless they are genuinely true and relevant.
- For motivation/behavioral questions, preserve the user's own reasoning and examples. The model should structure and clarify the answer rather than manufacture a personal story.
- For STAR-style or similar examples, label missing Situation/Task/Action/Result evidence instead of filling gaps with plausible fiction.
- Review tone, language, spelling, named company/role, dates, links, and requested word/character limits before submission.
- Keep final submitted text in the application tracker or document store so later interview preparation can use the exact claims that were actually sent.

## Interview Preparation

- Use conversational or voice-capable assistants for mock interviews when the product supports the user's required language/modality and the user finds real-time practice valuable.
- Build interview simulations from the exact vacancy, company research, source CV, portfolio, and verified application claims rather than generic question lists alone.
- Ask the model to challenge vague answers, request evidence, identify contradictions, and separate content quality from speaking style.
- For technical interviews, require executable/verifiable reasoning where possible: run code, check complexity, test examples, or compare against authoritative documentation instead of accepting fluent explanations.
- Do not use covert AI assistance in a live interview, assessment, take-home task, or examination when the employer's rules prohibit it or when doing so would misrepresent the applicant's independent ability.
- Treat interview feedback from the model as practice guidance, not as evidence of how a specific interviewer will score the answer.

## Career-Transition Route

- When the target role differs materially from the user's prior work, use the model to build an evidence-based gap map: existing transferable experience, missing required capabilities, optional/nice-to-have skills, portfolio proof needed, and realistic learning priorities.
- Separate `must learn before applying` from `can learn on the job` and `not actually required`; ground that distinction in multiple current vacancies and primary role information rather than one posting.
- Prefer small demonstrable portfolio artifacts and verifiable skills over generating large amounts of superficial application text.
- Do not ask the model to certify employability, seniority, salary level, or readiness from self-description alone. Validate against current market evidence, interviews, assessments, and actual outcomes.

## Application Tracking and Deterministic State

- Keep application status in a deterministic system such as a spreadsheet, database, task manager, or purpose-built tracker rather than relying on assistant memory.
- Record at minimum the employer, role, source URL, date captured/applied, submitted CV/application version, current status, next action, deadlines, and important contacts when the user needs systematic tracking.
- The assistant may summarize or analyze the tracker, but the structured store remains authoritative.
- Do not allow an agent to mass-submit applications, withdraw applications, message recruiters, schedule interviews, or modify records with high impact without clear scope, identity, and confirmation controls.
- Optimize for application quality and learning from outcomes rather than maximum submission count.

## Personal Data and Privacy

- A job-search corpus commonly contains direct identifiers and sensitive personal/professional history: name, phone, email, address/location, employment dates, education, references, salary expectations, visa/work-authorization information, and portfolio/contact details.
- Minimize uploaded data when the model does not need it. Redact home address, personal phone/email, reference contact details, identity-document numbers, signatures, or unrelated personal information from test/evaluation copies.
- Never provide job-board, email, password-manager, identity-provider, banking, government-portal, or one-time authentication credentials to a general assistant.
- Treat references and other people's contact information as third-party personal data; do not upload it merely because it appears in the user's application materials.
- Before connecting mail, drive, calendar, or other accounts, inspect the scopes/data boundary and connect only what the job-search workflow actually needs.

## Fraud, Impersonation, and Suspicious Opportunities

- Treat job offers, recruiter messages, payment requests, identity-document requests, links, and onboarding instructions as untrusted until verified through authoritative company channels.
- Do not let model confidence substitute for verification of a recruiter/company identity.
- Flag requests for passwords, authentication codes, unusual payments, cryptocurrency transfers, purchase of equipment through an unknown party, or unnecessary identity/financial information for independent verification.
- Use the assistant to organize red flags and verification steps, but verify the employer/recruiter through current official contact information rather than relying on generated conclusions.

## Local and Hybrid Route

- Present local inference as an optional privacy/control route for CVs, personal notes, interview journals, and other sensitive drafting when the user accepts local setup and the exact device passes fit tests.
- `Phi-4 Mini Instruct` is a current compact local text candidate for memory/compute-constrained drafting and analysis; `Qwen3 8B` is a broader local text/reasoning candidate where measured memory and latency permit it. Test the exact language, CV style, reasoning, and instruction-following workload rather than assuming model-card capability equals accepted application quality.
- A useful hybrid can keep the private master CV and personal notes local while using a hosted/search-capable assistant for public company/vacancy research, passing only the minimum facts needed for each step.
- Do not use a local model's stale training memory for current vacancy/company facts merely to avoid a hosted search. Retrieve current public evidence separately.
- Do not infer practical local fit from parameter count, quantized file size, or load success. Use the sibling hardware route for exact resource/runtime evaluation.

## High-Stakes and Truthfulness Boundary

- The user owns every claim submitted to an employer. Require final human review before sending a CV, application answer, portfolio statement, recruiter message, salary response, or other consequential representation.
- Preserve uncertainty when dates, titles, responsibilities, metrics, certifications, education, or legal/work-authorization details are unclear. Ask the user to confirm instead of choosing a plausible value.
- Do not provide legal conclusions about visas, discrimination, contracts, background checks, benefits, taxes, or employment rights from model memory. Use current authoritative/legal sources and qualified advice when consequences are material.
- Do not encourage impersonation, forged references, fake credentials, fabricated work samples, or undisclosed completion of assessments in place of the applicant.

## Cost and Accepted Job-Search Outcome

- Compare routes by **cost per accepted job-search outcome**, not token price or number of generated documents.
- Include subscription/API spend, research limits, document/voice tool access, correction/review time, duplicated provider subscriptions, local setup cost, and the cost of inaccurate or inconsistent applications.
- A free managed assistant can be sufficient for low-volume drafting/research when limits and quality are adequate.
- A temporary paid month can be rational during an intensive search if deeper research, higher limits, better file/voice workflows, or correction-time savings materially improve the user's process; do not assume a permanent subscription is required.
- A second provider is justified only by a measured recurring advantage, not because more models automatically improve applications.
- Track outcomes such as applications that accurately fit the user's evidence, interview invitations, recurring failure points, correction burden, and time per accepted application. Do not optimize blindly for submission volume.

## Escalation Triggers

- Move from ordinary personal-assistant use to this scenario when job search/career transition becomes sustained and multi-step.
- Add deep/current research when employer/role understanding is a recurring bottleneck rather than relying on model memory.
- Add a second provider only when one workflow repeatedly fails acceptance criteria on the primary assistant.
- Move to local/hybrid processing when personal-data sensitivity materially outweighs hosted convenience and the exact device has verified fit.
- Move toward `personal-data-analysis/` when application-pipeline analysis, structured tracking, or outcome metrics become the dominant task.
- Move toward professional/legal/human expert review when immigration, contract, discrimination, compensation, background-check, or other high-consequence employment issues require authoritative interpretation.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when the user selects a local/private model route and exact owned hardware determines feasibility.
- Use `../../../hardware/sub/computers/` for ordinary laptop/desktop local inference and the applicable accelerator specialization when known.
- Hardware purchasing remains outside this scenario; do not recommend buying a GPU merely to avoid a short-lived job-search subscription without an independent workload justification.

## Canonical Links

- Link managed assistant examples to `catalog/services/assistant-workspaces/chatgpt`, `catalog/services/assistant-workspaces/gemini`, and `catalog/services/assistant-workspaces/claude` when named.
- Link local candidates to `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct` and `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link sibling hardware and scenario owners rather than duplicating their runtime/device-fit or structured-data guidance.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party ChatGPT and Gemini deep-research/file capability documentation plus canonical AI Lab assistant/model owners.
- Current ChatGPT evidence establishes web/source-controlled deep research, uploaded-file use, cited reports, and document/spreadsheet file handling; current Gemini evidence establishes Deep Research with Google Search plus supported uploaded/connected sources. These are capability/product facts, not proof that one service produces better job-search outcomes.
- Vacancy content, company information, compensation, hiring process, job availability, plan limits, model aliases, research/file/voice features, pricing, and provider data terms are mutable and must be rechecked when material.
- Provider claims and model outputs do not establish whether an employer will select the applicant. Real application/interview outcomes and factual review remain the acceptance evidence.

## Validation

- The scenario remains an applicant/career-transition route and does not become employer/recruiter automation guidance.
- Current vacancy/company facts come from current sources rather than training memory.
- Every submitted professional claim remains traceable to user-provided or explicitly confirmed evidence.
- ATS language is treated as truthful clarity/terminology matching, not a promise to game an opaque ranking system.
- Master CV, submitted variants, vacancy source, and application state remain explicit artifacts outside conversational memory.
- Interview simulation supports practice without encouraging prohibited covert assistance or misrepresentation.
- Local/private and hosted/current-research routes can be combined without leaking the full private corpus unnecessarily.
- Credentials, third-party reference data, and unnecessary identifiers stay outside general assistant prompts.
- Final consequential application material requires human review.
- Mutable current claims carry the 2026-08-24 evidence boundary.
