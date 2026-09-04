# Documentation Requirements

## Scenario Fit

- Present this scenario for one independent consultant/freelancer/advisor who serves multiple clients and therefore crosses **multiple contractual, confidentiality, data, tool, and billing boundaries without a central enterprise IT team managing them**.
- Keep the scenario individual-professional in scope. A consulting firm or shared delivery team with centrally managed workspaces, permissions, budgets, and collaboration belongs in team/organization routes when those controls dominate.
- Distinguish this scenario from `general-knowledge-worker/`: the consultant must repeatedly separate client contexts, source data, workspaces, deliverables, accounts, and provider permissions across engagements.
- Distinguish it from `sensitive-data-professional/`: ordinary confidential client work can remain here when per-client controls are sufficient; that scenario becomes the owner when legal, healthcare, accounting, fiduciary, regulated, or similarly high-sensitivity obligations dominate.
- Do not turn the page into consultancy-business management. It owns model/service route selection for the consultant's AI-assisted work.

## Client Boundary Is the Primary Constraint

- Treat each client engagement as a separate data/authorization boundary unless the client explicitly permits shared infrastructure and the consultant's own policy supports it.
- Before using AI for client work, determine the client's approved products/accounts, confidentiality terms, data-processing restrictions, subcontractor/subprocessor requirements, retention/deletion expectations, region/residency requirements, and whether external AI is allowed at all.
- Do not assume that a tool approved by one client is approved by another.
- Do not use a personal consumer account for client-confidential work merely because the provider offers an opt-out or similar model in a business product.
- When a client requires work inside its managed account/workspace, use that account for the engagement and keep personal/other-client material out of it.
- When the consultant provides the AI service/account, document the service boundary and contract/data terms that actually apply to that client.

## Separate Engagements Explicitly

- Keep client conversations, project files, connected drives/mail/calendars, research notes, embeddings/indexes, API projects/keys, local folders, caches, and generated deliverables separated enough to prevent cross-client leakage.
- Prefer one clearly named project/workspace/folder/repository per engagement where the tool supports it.
- Do not rely on conversational memory to distinguish similar client names, products, strategies, documents, or requirements.
- Verify the active account/workspace/project before uploading files, connecting sources, starting deep research, or sending a deliverable.
- Do not use one broad connected drive/mail account if a narrower client folder/source can satisfy the workflow.
- Preserve a clean handoff/export path so client-owned work can be returned/deleted at engagement end without affecting unrelated client material.

## Default Managed Route

- Use a commercially appropriate managed assistant/workspace as the default low-administration route when its data terms satisfy the current client's requirements.
- Current commercial products from OpenAI and Anthropic, for example, document that business/commercial inputs and outputs are not used for model training by default. Treat exact products, plan boundaries, retention controls, admin capabilities, and subprocessors as mutable.
- Prefer business/commercial account terms over consumer terms for client work when the consultant controls the account and the engagement permits that provider.
- Do not interpret `not used for training by default` as a complete confidentiality/compliance guarantee. Review retention, human support/access paths, connected apps, logging, region/residency, security controls, and contract terms as material.
- Evaluate products on the consultant's real workload and per-client constraints rather than maintaining several subscriptions merely for model variety.

## Managed Client Accounts

- Treat a client-provided managed account as client-controlled. Administrators may have access/retention/audit/control capabilities that differ from the consultant's own account.
- Keep unrelated personal or other-client activity out of client-managed accounts.
- Verify whether the client account permits external sharing, downloads, connectors, custom GPT/agent creation, code execution, web research, or API use before enabling those workflows.
- At engagement end, assume access can be revoked. Preserve approved deliverables/source records in the agreed client/consultant system rather than relying on continuing access to assistant chat history.

## Research and Market/Client Analysis

- Use web/deep-research modes for current market, competitor, regulatory, product, or industry research when the question requires multi-source evidence.
- Prefer primary sources for material claims and preserve publication/effective dates.
- Restrict research to approved domains/sources when the engagement requires a bounded evidence set.
- Keep public research separate from confidential client context where practical; provide only the minimum private context needed to interpret the public evidence.
- Citation presence is not proof. Verify important claims against the linked source before including them in a client deliverable.
- If specialist/subscription databases are required, use them directly or through an approved integration rather than implying open-web completeness.

## Client Documents and Deliverables

- Use AI to draft, summarize, restructure, compare, and critique documents while preserving authoritative originals.
- Track which client sources support each material deliverable claim, especially numbers, contractual statements, market facts, technical findings, dates, and recommendations.
- Do not fabricate examples, customer evidence, benchmark results, quotes, interview findings, metrics, or references to make a deliverable more persuasive.
- For final deliverables, verify client/company names, figures, dates, citations, confidential content, promised actions, and scope before sending.
- Keep the submitted/final version outside conversational memory so later revisions start from the actual delivered artifact.

## Structured Data and Analysis

- For spreadsheet, financial, survey, operational, product, or other client data, use deterministic formulas/SQL/Python/R for material calculations and preserve code/query/assumptions.
- Route sustained analytical work to `data-analyst-or-data-scientist/` for the full analysis contract.
- Minimize extracts passed to a hosted model; redact unrelated identifiers/columns and use representative/synthetic samples when sufficient.
- Verify that the client's data license/contract permits external processing even when the data seems routine.
- Never grant an AI agent authority to change client production data, financial state, CRM, contracts, permissions, or other high-impact systems merely because it can analyze them.

## Coding and Technical Consulting

- For software/technical consulting, apply coding-model selection and agent controls from the software-development/agents decision guides.
- Treat client repositories, logs, infrastructure configuration, architecture diagrams, incident data, and credentials as client-confidential unless explicitly public.
- Verify the full coding-agent path: IDE/CLI, intermediary, model provider, cloud sandbox, repository integration, telemetry, and connected tools.
- Keep client repositories isolated in their own local/worktree/account/environment boundary and do not allow an agent to index unrelated client projects.
- Final technical recommendations must be grounded in the actual client environment and verified commands/tests/evidence rather than generic model advice.

## Connected Apps and Actions

- Treat Gmail/Drive/Calendar/Slack/CRM/project-management/other connectors as extensions of the client's data boundary.
- Connect only the client/account and scopes needed for the engagement; avoid broad personal-account integration that exposes other clients.
- Distinguish read-only access from write-capable actions. Authorization to summarize mail does not imply authorization to send messages, alter files, schedule meetings, update CRM, or change project state.
- Require explicit confirmation for external communications, commitments, destructive edits, permission changes, scheduling involving third parties, or other consequential actions unless a separately agreed automation policy authorizes them.
- Verify recipient, account, workspace, destination folder, and client identity before every high-impact cross-system action.

## Direct API Route

- Use a direct API when the consultant needs repeatable automation, batch processing, a custom client tool, structured outputs, or a bounded integration not available in a managed assistant.
- Isolate API projects/keys/budgets/logs by client when doing so materially improves access control, spend attribution, revocation, and deletion.
- Do not reuse one long-lived unrestricted API credential across unrelated client systems merely for convenience.
- Apply spend/rate limits and log only what is necessary. Prompt/output logs can contain client-confidential data.
- Treat API gateways, observability proxies, vector databases, hosted sandboxes, and other intermediaries as subprocessors/data recipients in the provider chain.

## Local and Hybrid Route

- Use local inference when a client forbids hosted processing, confidential data should remain on the consultant-controlled endpoint, offline work matters, or repeated private tasks justify the operational burden.
- A compact local model such as `Qwen3 8B` can support bounded writing, extraction, code/query help, and summarization when exact task quality/hardware fit is measured.
- A compact multimodal model such as `Gemma 4 E2B Instruct` or `Gemma 4 E4B Instruct` can be evaluated for private documents/images only when the exact runtime supports the modality.
- Local inference does not remove contractual, endpoint-security, backup, disk-encryption, malware, extension, or cross-client isolation obligations.
- A hybrid route can keep the private client corpus local while using hosted models for public research or sanitized questions under an explicit routing rule.
- Do not silently fall back from local to cloud when a client's rule requires local-only processing.

## Client-Specific Knowledge Bases

- If an engagement needs persistent retrieval over client documents, keep the corpus/index/embeddings separated per client and preserve source permissions/provenance.
- Do not combine client corpora into a shared consultant knowledge base without explicit permission and a real need.
- RAG/retrieval does not make source content correct, current, or authorized. Preserve original source links/identities and freshness checks.
- At engagement end, support deletion/export of client-specific indexes/caches according to the agreed retention boundary.
- Route durable knowledge-system design to the applicable knowledge-base/team/organization owners when it becomes the primary problem.

## Confidentiality and Conflict Prevention

- Do not use one client's confidential information to advise another client, even if the model can recall or retrieve it.
- Treat prompt/history leakage, autocomplete suggestions, cached embeddings, shared files, clipboard history, agent memory, and cross-project search as practical conflict risks.
- Separate reusable public/general consultant know-how from client-owned confidential material.
- When turning an engagement-specific lesson into a reusable template, remove client-identifying/confidential details and confirm the consultant has the right to reuse the underlying knowledge.

## Billing and Cost Attribution

- Compare routes by **cost per accepted client deliverable/outcome**, including subscriptions, API usage, research credits, cloud compute, local compute, correction/review time, admin overhead, and failed/repeated work.
- Track client-attributable API/compute usage when billing, budgeting, or contractual caps require it.
- Avoid maintaining multiple paid model subscriptions unless distinct client requirements or measured workload advantages justify the fragmentation.
- A temporary premium/deep-research subscription can be rational for a bounded engagement; do not treat permanent multi-provider spend as the default.
- Include the cost of switching accounts/workspaces, source reconnection, access review, and client-specific configuration when comparing providers.

## Retention, Handoff, and Engagement Close

- Define what must be retained, delivered, archived, or deleted when the engagement ends.
- Keep final client deliverables, source references, analysis code, and agreed documentation in the client-approved handoff location rather than only in AI chat/project history.
- Revoke client-specific connectors/tokens/API keys and remove local/cloud working copies according to agreement and legal retention needs.
- Do not delete evidence needed for contractual/audit obligations merely to minimize AI data retention; follow the governing engagement policy.
- Do not preserve client data in prompts/templates or a personal assistant memory after the engagement when it is no longer authorized/needed.

## Reliability and Professional Review

- Match verification to consequence: low-stakes drafting can use normal review; factual client deliverables, financial figures, technical recommendations, contracts/policy, production changes, and external commitments need stronger evidence.
- Preserve authoritative source data and deterministic calculations.
- When evidence is incomplete, state uncertainty/gaps rather than filling them with plausible client-specific assumptions.
- The consultant remains responsible for professional judgment, representations to the client, and compliance with contract/professional obligations.

## Escalation Triggers

- Move from a personal/consumer assistant to a commercial/business route when client-confidential work becomes material.
- Use a client-managed workspace when the client requires its own governance/account boundary.
- Move to local/offline processing when hosted external processing is prohibited or the local route materially reduces acceptable risk and passes quality requirements.
- Move toward `sensitive-data-professional/` when regulated/legal/health/financial/fiduciary or similarly high-risk obligations dominate.
- Move toward `researcher/`, `data-analyst-or-data-scientist/`, software-engineering, or creative-professional scenarios when one specialized workload becomes the primary model-selection constraint.
- Move to team/organization routes when the consultant adds staff/shared delivery workflows or builds reusable multi-client infrastructure requiring central policy, quotas, access, or observability.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when local inference materially constrains an engagement route.
- Use `../../../hardware/sub/computers/` for the consultant workstation and applicable accelerator specialization when known.
- Hardware purchasing remains outside this scenario; a client requirement can instead imply hosted, client-managed, rented, or hybrid execution.

## Canonical Links

- Link commercial managed assistants to their canonical service owners when named.
- Link `Qwen3 8B` to `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link `Gemma 4 E2B Instruct` and `Gemma 4 E4B Instruct` to their exact canonical Model Reference identities when named.
- Link specialized workloads to their sibling scenario/decision-guide owners instead of duplicating their detailed contracts.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI business-data/managed-account documentation, current Anthropic commercial-product data-use documentation, and canonical AI Lab model/service owners.
- Current commercial-provider evidence confirms that business/commercial account data-handling terms differ materially from consumer accounts and that managed-account administrator/control boundaries must be treated separately from ordinary user privacy.
- Provider terms, training defaults, retention, account/workspace features, connected-app scopes/actions, subprocessors, plan pricing, model aliases, and client policy are mutable; recheck them for each engagement before rendering current guidance.
- No provider term overrides a client's contract/policy or the consultant's professional obligations.

## Validation

- Multiple client boundaries—not generic knowledge work—remain the defining scenario constraint.
- Client accounts, files, connectors, histories, indexes, API credentials, and deliverables are separated enough to prevent cross-client leakage.
- One client's approved AI route is not generalized to another client.
- Consumer privacy settings are not treated as substitutes for commercial/client approval.
- Read access and write-capable actions remain distinct authorization classes.
- Local inference is not equated with automatic contractual/security compliance.
- Final deliverables remain source-backed, reviewed, and preserved outside conversational memory.
- Engagement close includes handoff/retention/revocation/deletion boundaries.
- Specialized work routes to the appropriate sibling owner instead of becoming duplicated here.
- Mutable current claims carry the 2026-08-24 evidence boundary.
