# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale legal/contract operations covering legal research, contract review/drafting/comparison, due diligence, discovery/document review, clause/obligation extraction, legal knowledge, matter support, and governed legal workflows.
- Keep the scenario organization-scale. One lawyer/consultant handling sensitive material belongs in `professionals/sensitive-data-professional/`; generic high-volume extraction belongs in `high-volume-document-processing/` when legal interpretation is not the governing constraint.
- The defining constraints are **authoritative legal sources, jurisdiction/effective date, privilege/confidentiality, matter/client separation, contract version/provenance, citation verification, qualified legal judgment, document scale, and controlled downstream actions**.
- Do not turn this page into legal-service procurement or legal advice. It owns the AI route and acceptance/control boundary.

## Qualified Legal Judgment Remains Authoritative

- Use AI to retrieve, organize, extract, compare, summarize, draft, and identify issues; keep qualified legal professionals and governing legal/business approval processes authoritative for legal conclusions and consequential decisions.
- Do not let model fluency or provider branding substitute for lawyer review where legal judgment, professional responsibility, privilege, filing, negotiation, or client advice is required.
- Preserve uncertainty, assumptions, jurisdiction, effective date, factual dependencies, and unresolved questions in material legal outputs.
- Define which outputs are research/draft/work product versus approved legal advice or executed contractual state.

## Authoritative Legal Research Route

- Prefer legal-research assistants integrated with authoritative current legal databases when case law, statutes, regulations, secondary authority, citators, jurisdiction, and source lineage materially affect the task.
- Current Thomson Reuters CoCounsel/Westlaw and Lexis+ AI/Protégé are examples of legal-native generative research routes with source-linked legal content and drafting/review workflows. Treat exact models/features/jurisdiction/content access and pricing as mutable.
- Require citations to actual retrievable authorities and verify that each authority supports the proposition stated.
- Check jurisdiction, court/authority level, precedential status, publication status, treatment/history, amendments, effective dates, and later developments where material.
- Do not accept a plausible case/statute/citation from model memory without source verification.

## Citation Verification

- Verify citation identity: case/statute/regulation/source name, court/body, date, reporter/identifier, section, jurisdiction, and source URL/database record where applicable.
- Verify the proposition against the cited passage, not only the title/headnote/generated summary.
- Use citator/treatment/currentness tooling when the legal task requires it.
- Distinguish primary authority, secondary authority, commentary, client/matter documents, and model interpretation.
- Do not generate quotations unless the exact text can be verified in the source.
- Preserve source/research date so future readers know the currentness boundary.

## Legal Research Coverage

- Define research scope before using AI: jurisdiction, issue, dates, authority types, databases, known terms, and exclusions.
- Use specialist databases/official sources rather than open-web search alone for legal research where coverage/currentness matter.
- Treat absence of found authority as an uncertain search result unless the research method supports a stronger conclusion.
- Preserve potentially adverse/contrary authority instead of summarizing toward the desired position.
- Require stronger manual research for novel/high-stakes/poorly indexed issues or where the AI cannot access relevant sources.

## Matter and Client Boundary

- Treat each legal matter/client/transaction/investigation as a separate confidentiality/authorization boundary where applicable.
- Separate documents, chat histories, embeddings/indexes, connected sources, workspaces, API projects, exports, and generated deliverables enough to prevent cross-matter leakage.
- Do not use confidential information from one client/matter to answer another.
- Verify the active matter/workspace/source before uploading documents or running broad retrieval.
- Preserve ethical-screen/information-barrier requirements through deterministic permissions rather than prompt instructions alone.

## Privilege and Confidentiality

- Determine whether material is privileged, work product, confidential, personal, regulated, litigation-sensitive, trade secret, or subject to protective order before model use.
- Use only organization-approved services/accounts/configurations whose contractual/data-processing boundary fits the material.
- Review provider retention, training/data-use defaults, subprocessors, access, residency, connectors, logs, and support paths rather than relying on a generic `enterprise` label.
- Minimize disclosure and avoid sending entire matter repositories when a scoped subset satisfies the task.
- Preserve privilege/confidentiality markings and do not expose protected content in broad shared workspaces or external research prompts.

## Contract Source of Truth

- Keep executed agreements, approved templates/playbooks, clause libraries, amendments, exhibits/schedules, order forms, negotiation redlines, and contract-management systems authoritative.
- Preserve exact document/version/date/party/matter identifiers for AI review.
- Do not let a model summarize an outdated draft as the signed agreement.
- Apply amendment/precedence/order-of-documents rules explicitly rather than assuming the newest file name controls.
- Keep generated contract summaries as derived artifacts linked to the governing source.

## Contract Review and Extraction

- Use AI to extract clauses, obligations, dates, parties, governing law, renewals, termination, liability, indemnity, security/privacy, payment, SLA, data-processing, change-of-control, and other defined fields only through an explicit schema/playbook.
- Preserve source page/section/clause text or location for material extracted items.
- Distinguish absent clause, ambiguous clause, conflicting clause, not applicable, inferred concept, and extraction failure.
- Do not let the model invent missing obligations or normalize unusual terms into standard language silently.
- Validate exact dates, amounts, percentages, defined terms, party names, notice addresses, and cross-references independently where consequence is material.

## Contract Comparison and Playbooks

- Compare proposed clauses against approved legal playbooks/templates and identify deviation, not merely semantic similarity.
- Keep the playbook/risk position/version/owner authoritative.
- Use AI to explain deviations and draft alternatives while preserving who can approve each exception.
- Do not allow a model to approve a non-standard clause or risk position solely because it labels the deviation `low risk`.
- Preserve negotiation history and approved exception rationale where the organization requires it.

## Drafting and Redlining

- Use AI to draft clauses, revise language, explain edits, create issue lists, or propose redlines from verified instructions/playbooks.
- Keep defined terms, internal cross-references, hierarchy, exhibits, numbering, governing law, and document consistency explicit.
- Verify that a generated edit does not accidentally broaden/narrow obligations elsewhere in the agreement.
- Require human legal review before external negotiation or execution.
- Preserve the actual redline/diff rather than relying on prose summary of changes.

## Due Diligence and Large Document Sets

- Decompose diligence into ingestion/identity/classification/extraction/issue spotting/validation/review/reporting rather than one prompt over a mixed corpus.
- Preserve document provenance and matter/entity grouping.
- Define review questions/playbook and materiality thresholds before batch processing.
- Sample high-confidence results and route ambiguous/high-risk findings to legal reviewers.
- Keep missing/unreadable/duplicate/superseded documents visible.
- Route generic OCR/extraction-scale concerns to `high-volume-document-processing/` when applicable.

## Litigation, Discovery, and Investigations

- Preserve chain of custody, collection/source identity, date/time, custodian, access, document version, and legal hold/retention requirements where applicable.
- Use AI for summarization, issue tagging, chronology, search/query assistance, and evidence organization only under the governing discovery/investigation process.
- Do not alter original evidence or let generated summaries replace it.
- Treat privilege review, responsiveness/relevance, production/redaction, and legal strategy as separate review/control stages.
- Escalate forensic/evidentiary decisions to qualified owners.

## Legal Knowledge and Internal Precedent

- Use permission-aware retrieval for internal memos, templates, prior advice, playbooks, contracts, and matter knowledge.
- Preserve matter/client permissions and ethical screens.
- Do not treat prior advice as current law or universally applicable precedent without checking facts/jurisdiction/currentness.
- Keep source author/date/matter/context available.
- Route broad enterprise retrieval architecture to `business-knowledge-assistant/` while preserving legal-specific permission/currentness rules here.

## Current Law and Regulatory Change

- Treat legal/regulatory status as time-sensitive retrieval, not model-memory knowledge.
- Use current official/legal database sources and record effective dates, proposed/final status, jurisdiction, transition periods, and superseded rules.
- Distinguish enacted/adopted/effective/proposed/guidance/enforcement posture.
- Define monitoring/recheck workflow for obligations that change frequently.
- Do not auto-update legal advice, templates, or contracts merely from an AI-detected regulatory change without legal review.

## Structured and Quantitative Legal Work

- Use deterministic calculations for damages, interest, deadlines, notice periods, thresholds, pricing, caps, allocations, or other exact values.
- Preserve source inputs/rules and timezone/business-day/calendar assumptions.
- Use AI to explain/generate formulas but verify the calculation independently.
- Do not allow model-generated arithmetic to control filings, payments, deadlines, or contractual notices without deterministic validation.

## Filing, Signing, and External Actions

- Separate research/drafting from actions such as filing, submitting, sending legal notices, signing, accepting terms, changing matter status, publishing legal content, or communicating binding positions.
- Define identity/authority, approval, required attachments, recipient/court/body, deadlines, version, signature authority, and confirmation for every consequential action.
- Do not let a model infer that document access grants signature/filing authority.
- Verify final filed/sent/executed state in the authoritative system.

## Legal Agents and Tool Use

- Treat legal agents with DMS, email, research database, CLM, e-signature, billing, filing, matter-management, or workflow tools as side-effecting systems.
- Use least privilege, scoped matter access, explicit tools, approval gates, bounded retries, idempotency, audit, and rollback/reconciliation.
- Prevent retrieved documents/emails/web content from expanding agent authority through prompt injection.
- Do not expose privileged material to external tools not approved for the matter.
- Require higher controls for autonomous negotiation, external communication, filing, signature, or contract changes.

## Prompt Injection and Adversarial Documents

- Treat contracts, opposing-party documents, emails, web pages, discovery materials, attachments, and linked content as untrusted instructions.
- Document text must not override system policy, request secrets, change tools, suppress contrary authority, or initiate external actions.
- Test hidden/visible prompt injection and malicious links/files for agentic legal workflows.
- Keep legal playbooks/policies/tool permissions outside document-controlled context.

## Human Review and Professional Responsibility

- Define qualified reviewer requirements by task/failure severity.
- Use AI review acceleration without lowering the professional standard for material advice, filing, privilege, negotiation, or contractual risk.
- Preserve who reviewed/approved material outputs.
- Do not use AI-generated confidence as a substitute for legal reviewer competence.
- Escalate ambiguous authority/facts, conflicts, novel issues, and high-impact risk explicitly.

## Evaluation Suite

- Build a versioned legal evaluation set covering research/citation, contrary authority, contract extraction, clause comparison, redline, diligence, chronology, legal knowledge retrieval, exact dates/amounts, and a workflow that must escalate.
- Include hallucinated-looking citations, outdated/overruled authority, near-identical contract versions, conflicting amendments, missing defined term, ambiguous clause, privileged matter boundary, prompt-injected document, and unauthorized external action.
- Score citation/source correctness, legal issue recall/precision, contract field/clause accuracy, omission, version/provenance correctness, escalation, action safety, reviewer correction time, latency, and cost.
- Use qualified legal reviewers for material benchmark labels.
- Re-run after model, legal database, playbook, document schema, agent/tool, or policy changes.

## Data Boundary and Audit

- Classify matter/client/contract/evidence/research/employee/customer data and apply the appropriate approved route.
- Protect legal AI logs/traces, which can themselves contain privileged/confidential material.
- Preserve model/agent/tool/version, sources, matter/document IDs, changes/actions, approvals, and final legal artifact where audit requires it.
- Apply retention/legal hold/deletion according to the governing matter/process rather than generic chat cleanup.

## Local/Private and Hybrid Route

- Use private/self-hosted inference when privilege/confidentiality/data restrictions prohibit managed processing or organization control/economics justify it.
- Keep legal databases, DMS/CLM/matter systems, playbooks, and deterministic validation authoritative.
- A hybrid route can keep client/matter documents private while using approved hosted tools for public legal research under explicit routing rules.
- Local inference does not remove legal currentness, citation verification, prompt injection, privilege, endpoint security, or professional-review obligations.
- Escalate shared model gateway/inference to `internal-ai-platform/` when it becomes organization infrastructure.

## Cost per Accepted Legal Outcome

- Compare **total cost per accepted legal research/review/contract outcome**: legal AI seats/API, database access, document processing, attorney/paralegal review, correction, diligence sampling, integration/admin, privacy/security controls, and legal-risk/error cost.
- A legal-native assistant can be economically stronger than a cheaper general model when authoritative source linkage and workflow integration reduce validation time.
- A high-volume model can handle first-pass extraction/classification only when ambiguous/material cases are escalated reliably.
- Do not optimize on documents reviewed or drafts generated alone; measure accepted work product and qualified review burden.

## Escalation Triggers

- Move to this scenario when legal research/contract/matter operations become organization-scale AI workflows.
- Move to `high-volume-document-processing/` when generic extraction throughput dominates.
- Move to `business-knowledge-assistant/` when enterprise-wide internal search rather than legal reasoning dominates.
- Move to regulated/high-security routes when matter/data isolation requirements demand stronger controls.
- Move to `internal-ai-platform/` when centralized model/provider/gateway/runtime concerns dominate.
- Stop/narrow autonomy when source currentness, privilege, qualified review, version control, or external-action authority cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted inference target is selected and hardware materially constrains model/document/concurrency fit.
- Use `../../../hardware/sub/servers/` for shared legal inference/document infrastructure.
- Legal/DMS/CLM hardware procurement remains outside this scenario.

## Canonical Links

- Link high-volume document, business knowledge, internal-platform, regulated, and high-security concerns to their scenario owners.
- Link named legal AI/research/CLM services and exact models to canonical catalog owners when materialized.
- Do not duplicate legal database/product profiles here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Thomson Reuters CoCounsel/Westlaw, Lexis+ AI/Protégé, and Harvey legal AI documentation/material describing source-backed legal research, drafting, document/contract analysis, enterprise legal workflows, and validation/professional-use boundaries.
- Current evidence establishes legal-native generative research and contract/document workflows linked to authoritative legal or matter sources. It does not establish legal correctness, complete research coverage, privilege preservation for every configuration, or authority to make legal decisions.
- Legal databases, citators, laws/regulations, model/provider behavior, feature access, data terms, integrations, and pricing are mutable; recheck them before rendering current guidance.
- Current authoritative law/sources, exact matter/contract provenance, and qualified legal review remain the acceptance authority.

## Validation

- Qualified legal professionals remain authoritative for consequential legal judgment.
- Generated citations/cases/quotes are not accepted without source and currentness/treatment verification.
- Client/matter permissions and privilege boundaries are deterministic and prevent cross-matter leakage.
- Contract review preserves exact version, clause/source location, defined terms, amendments, and uncertainty.
- Research/drafting is separated from filing/signature/external communication authority.
- Untrusted legal documents/web/email cannot expand agent authority.
- Legal research/current law is treated as current retrieval, not model memory.
- Cost is measured per accepted legal work product including qualified review/database/validation burden.
- Internal-platform/regulated/high-security concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
