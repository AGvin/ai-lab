# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-wide or broadly shared employee question answering/search over internal policies, procedures, products, support material, project/customer context, documents, messages, tickets, repositories, and other enterprise knowledge sources.
- Keep the scenario organization-scale. A personal corpus belongs in `personal-knowledge-base-user/`; a bounded research team belongs in `teams/research-and-insights-team/`; a small-team connected workspace belongs in its team scenario when enterprise-wide retrieval architecture is not required.
- The defining constraints are **permission-aware retrieval, source provenance/citations, freshness/versioning, multi-source conflict handling, retrieval quality, employee scale/concurrency, data boundary, administration, and escalation**.
- Do not turn the page into a complete RAG/vector-database architecture guide. It owns the model/route decision and the evidence required before an internal knowledge assistant is trusted.

## Start With Knowledge Sources and Questions

- Inventory the authoritative source systems and content classes before selecting a model: document stores, wiki/knowledge bases, email/chat, tickets, CRM, code/repositories, policies, structured systems, and approved external sources where applicable.
- Define representative employee questions by function and failure severity: factual lookup, cross-source synthesis, procedure explanation, policy question, project/account briefing, current-state lookup, comparison, and a question whose answer must escalate.
- Record which source owns each fact class and what freshness/effective-date semantics apply.
- Do not build a broad enterprise index merely because sources can be connected; exclude data that the use case does not need or whose permission/compliance boundary is not approved.

## Default Managed Company-Knowledge Route

- Prefer an organization-approved managed company-knowledge/enterprise-search assistant when existing connector permissions, citations, admin controls, data terms, and source coverage satisfy the use case and lower operational burden is valuable.
- Current ChatGPT Company Knowledge is an example: current Business/Enterprise/Edu documentation describes search/fetch across eligible enabled apps, per-user app authentication or managed connections, enterprise RBAC/admin controls, preservation of existing source permissions, and citations/links back to source material.
- Current ChatGPT Company Knowledge specifically separates its retrieval-oriented mode from write actions: enabled app write actions are not available through the Company Knowledge mode itself and require selecting the app/action surface separately. Preserve this read-vs-write separation as a useful safety pattern.
- Treat exact eligible apps/plugins, sync support, platforms, RBAC behavior, residency support, model behavior, and product limits as mutable.
- Evaluate the managed route on the organization's own permission graph and source mix, not vendor demos.

## Permission Preservation

- The assistant must not expose source content the requesting user cannot access in the authoritative system.
- Verify direct users, groups, inherited permissions, private channels, restricted folders/sites, repository access, guest/external users, disabled/offboarded accounts, and permission changes.
- Current ChatGPT sync/company-knowledge documentation states that existing permissions are respected and kept updated; treat this as exact-product evidence and test it against the organization's real edge cases.
- Do not copy protected content into a globally readable vector index, cache, summary, prompt template, or model memory that bypasses source permission checks.
- Test negative access: users who should **not** see a source must not obtain the fact through direct questions, paraphrases, cross-source synthesis, citations, autocomplete, or related-answer leakage.

## Source Provenance and Citations

- Require important answers to expose enough source identity for verification: document/message/ticket/repository/page link or stable ID, title/context, and date/version where material.
- Citation presence is not correctness. Verify that the cited source actually supports the claim and that the assistant did not mix facts from unrelated documents.
- Preserve per-claim provenance when an answer synthesizes several sources.
- Do not generate quotations unless they can be verified in the exact source.
- If the retrieval system cannot expose the underlying source for a high-consequence claim, treat the answer as insufficiently grounded and escalate.

## Freshness and Versioning

- Define freshness requirements by source class: policy/procedure, project status, product documentation, customer/account state, incident/runbook, HR/legal, and historical reference can require different update semantics.
- Current sync-based products can index source data and update permissions/content over time, but exact sync cadence/mechanism differs by connector; verify it rather than assuming real-time freshness.
- Prefer authoritative current versions and surface superseded/archived status.
- When sources conflict, present the conflict, source dates/owners, and escalation path rather than selecting the newest-looking or most fluent text automatically.
- Record reindex/sync failures and stale-source indicators as operational health signals.

## Retrieval Pipeline Is More Than the Generator

- Evaluate ingestion/parsing, chunking/segmentation, metadata, embeddings, retrieval, filters/permissions, reranking, context assembly, generator, citation mapping, and post-answer policy separately where those components materially affect quality.
- Do not infer RAG quality from the generation model alone.
- Measure retrieval recall for answer-supporting sources before blaming the generator for missing evidence.
- Measure precision/noise and reranking/context-selection behavior before solving every poor answer with a larger model or longer context.
- For multimodal/scanned sources, treat OCR/perception/extraction as a separate uncertain stage and validate exact values/tables/forms through deterministic extraction or human review where consequence warrants it.

## Search vs Synthesis

- Distinguish `find the source` from `answer from sources` and from `compare/synthesize sources`.
- A retrieval/search result can be useful even when the model should not synthesize a high-consequence answer.
- For policies/procedures, provide source link/section and clarify whether the assistant is quoting, summarizing, or interpreting.
- Do not let model memory fill gaps when no approved source supports the requested organizational fact.
- Explicitly return `not found`, `conflicting sources`, `access unavailable`, or `requires owner review` when appropriate.

## Structured and Transactional Data Boundary

- Do not treat document RAG as the canonical route for live transactional facts such as current inventory, balance, entitlement, order state, production metrics, or other structured system-of-record data when a deterministic query/API exists.
- Use approved structured tools/queries for such facts and keep schema/auth/filter logic explicit.
- Combine structured results with document context only when the provenance of both remains visible.
- Do not cache volatile structured answers as reusable knowledge without an explicit freshness contract.

## Managed Connectors and Apps

- Treat every app/connector as a distinct data boundary with its own OAuth/admin setup, permissions, indexing/sync behavior, residency support, retention, and terms.
- Enable the minimum source set needed for the use case.
- Current ChatGPT Company Knowledge requires eligible enabled apps with search/fetch and lets users select included apps for a research interaction; preserve source selection as a useful control when available.
- Recheck connectors after vendor changes, especially when a previously read-only integration gains write/action capabilities.
- Keep connection/offboarding processes so revoked employee/source access propagates correctly.

## Custom Managed RAG/API Route

- Use a custom managed RAG route when organization-specific retrieval logic, source coverage, metadata, ranking, evaluation, UI, policy, data locality, or integration requirements exceed the managed workspace's capabilities.
- Separate generator selection from embedding/retrieval/reranking selection; use exact models/components only after current evidence and evaluation justify them.
- Define ingestion and permission-sync ownership, index rebuild/backfill, deletion propagation, schema/metadata contracts, source IDs, retry/failure handling, observability, and evaluation before production rollout.
- Treat model gateways, managed vector databases, OCR/document services, rerankers, and observability systems as additional data recipients in the provider chain.
- Avoid a custom architecture if the managed route meets acceptance; include engineering/operations burden in total cost.

## Self-Hosted/Private RAG Route

- Use self-hosting when external processing or managed-index boundaries are unacceptable, organization control/offline/sovereign operation is required, or repeated scale/economics justify infrastructure.
- Bind local generation fit to exact model artifact/runtime/context/concurrency/hardware and separately validate embedding/retrieval/reranking/perception components.
- Do not preserve a specific local generator such as `Qwen3 14B` as a permanent default here; consume current candidate models from canonical model-selection/reference owners and evaluate them on the organization's answer suite.
- Local/private hosting does not automatically solve permissions, deletion, security, endpoint authentication, backups, observability, prompt injection, source poisoning, or operator access.
- Keep unsupported/unmeasured model/runtime/hardware combinations `Unknown`.

## Multimodal Knowledge

- Treat images, scans, forms, diagrams, screenshots, audio, and video as separate ingestion/perception paths when the knowledge base includes them.
- Validate OCR/transcription/perception quality before answer generation.
- Preserve source page/frame/time/field references where practical.
- Do not let a multimodal model substitute for deterministic form parsing, schema validation, or exact extraction when a wrong value has material consequence.
- Keep a text-only fallback/source path when the authoritative structured/text representation exists.

## Prompt Injection and Knowledge Poisoning

- Treat retrieved documents/messages/tickets/web pages as untrusted content, even inside authenticated systems.
- Retrieved text must not override system/organization policy, reveal secrets, expand tools, or instruct the agent to ignore source/access boundaries.
- Test direct and indirect prompt injection, malicious links, poisoned documents, hidden text, adversarial instructions, and cross-source contamination.
- Apply source trust/risk controls and isolate action-capable tools from retrieval-only answers.
- Maintain an incident/removal/reindex process for poisoned or compromised knowledge sources.

## Human Escalation and High-Consequence Answers

- Define categories requiring source-owner/qualified review: HR/employee, legal/compliance, finance, safety/security, medical/health, regulated policy, contractual commitments, access/permissions, or other high-consequence areas.
- For these categories, use the assistant to retrieve and summarize approved sources, while preserving human/professional ownership of interpretation/decision where required.
- Do not silently answer from a secondary internal summary when the authoritative policy/source is available.
- Escalate when the source is missing, stale, conflicting, permission-sensitive, or ambiguous.

## Evaluation Suite

- Build a versioned enterprise evaluation set from representative questions and permission configurations.
- Include simple lookup, multi-source synthesis, stale/current conflict, synonym/terminology variation, no-answer case, restricted source, offboarded/revoked user, multimodal source if used, structured/live fact, and prompt-injected/poisoned document.
- Score retrieval recall/precision, grounded-answer correctness, citation support, permission leakage, freshness, conflict handling, no-answer calibration, latency, concurrency, escalation rate, and human correction effort.
- Evaluate by user/permission persona; one administrator's results do not prove an ordinary employee's access behavior.
- Run regression evaluation after source/connector/index/chunking/reranker/generator/model changes.

## Concurrency and Operational Reliability

- Measure representative concurrent users/queries, p50/p95 latency, retrieval/index service capacity, timeouts/retries, provider rate limits, queueing, failure modes, and source-connector outages.
- Define degraded behavior when one source/provider is unavailable; do not silently answer from incomplete sources as though coverage were complete.
- Monitor index freshness, permission-sync errors, retrieval miss rates, citation failures, and escalations.
- If a managed service lacks observability required for the consequence/scale, a more controlled architecture may be justified.

## Read vs Action Boundary

- Keep enterprise knowledge retrieval/read assistance separate from write-capable actions unless an explicitly approved agent workflow requires both.
- A correct answer about a policy or project does not authorize changing a ticket, file, permission, calendar, CRM record, or business system.
- Use separate action tools/scopes, confirmations, deterministic validation, and audit where actions are introduced.
- Prefer a retrieval-only knowledge assistant when the business problem is finding/understanding knowledge.

## Cost per Accepted Knowledge Answer

- Compare **total cost per accepted grounded answer**: workspace/API fees, connector/index/storage, embedding/rerank/generation, ingestion/OCR, infrastructure, source administration, permission sync, evaluation, human review/escalation, and incident risk.
- Managed company knowledge can be cheaper despite higher seat price when it removes custom ingestion/permissions/operations.
- Custom/self-hosted RAG can win at scale or under strict boundaries, but include engineering, on-call, upgrades, security, and quality evaluation.
- A stronger generator can be wasted spend when retrieval/permission/freshness is the bottleneck.
- Track accepted grounded answers and employee task time rather than query volume alone.

## Escalation Triggers

- Move from a bounded team knowledge route to this organization scenario when source/permission coverage and shared employee scale become organization-wide concerns.
- Move from managed company knowledge to custom managed RAG when retrieval quality, source integration, data policy, observability, or evaluation requires custom control.
- Move to private/self-hosted when the approved data boundary prohibits managed processing/indexing and the organization can operate the system safely.
- Move to `internal-ai-platform/` when centralized model gateway/routing, budgets, shared workers, provider abstraction, or platform SLOs become the primary concern.
- Move to regulated/high-security routes when the knowledge corpus/operation requires materially stronger governance/isolation.
- Stop answering a category autonomously when source or permission correctness cannot meet the required threshold.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when self-hosted/private inference is already selected and exact fixed infrastructure constrains model choice.
- Use `../../../hardware/sub/servers/` for shared organization inference/retrieval hosts and applicable accelerator specializations.
- Hardware purchasing remains outside this scenario; managed/API/private-cloud routes remain valid alternatives.

## Canonical Links

- Link exact managed workspace/company-knowledge services to canonical service owners when named.
- Link exact embedding/reranking/generation models to canonical Model Reference owners only when current pipeline evidence justifies them.
- Link vector stores/retrieval software/data platforms to their canonical software/service owners rather than duplicating profiles here.
- Link platform-wide concerns to `decision-support/scenarios/organizations/internal-ai-platform`.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party ChatGPT Company Knowledge and apps-with-sync documentation plus canonical AI Lab retrieval/model owners.
- Current evidence establishes multi-source company retrieval with source citations, existing-permission enforcement, per-app admin/connection controls, synced-source permission updates, and a retrieval-oriented Company Knowledge mode that does not expose enabled write actions directly.
- Eligible plugins/apps, connector sync behavior, platform availability, RBAC/residency, indexing mechanisms, model aliases, rate/usage limits, and provider terms are mutable; recheck them before rendering current guidance.
- Managed-service documentation establishes product behavior, not independent retrieval/grounded-answer quality on the organization's corpus.

## Validation

- Organization-wide source coverage and permission-aware retrieval distinguish this route from personal/team knowledge use.
- Existing source permissions are tested including negative-access cases.
- Citations/provenance and freshness/version conflict handling are required controls.
- RAG quality is decomposed into ingestion/retrieval/reranking/context/generation rather than attributed solely to the generator.
- Structured live facts use deterministic query paths when appropriate.
- Prompt injection/knowledge poisoning remain relevant even for authenticated internal sources.
- Read-only knowledge access does not imply action authority.
- Custom/self-hosted routes include permissions/deletion/operations rather than `private = safe` shorthand.
- Cost is measured per accepted grounded answer including retrieval/index/admin/review burden.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
