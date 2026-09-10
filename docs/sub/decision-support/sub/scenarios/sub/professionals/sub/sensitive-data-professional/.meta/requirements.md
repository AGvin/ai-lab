# Documentation Requirements

## Scenario Fit

- Present this scenario for one professional whose recurring AI-assisted work includes **confidential, privileged, regulated, health, financial, legal, client, security-sensitive, or otherwise high-sensitivity data** such that provider-chain, contractual, retention, residency, access, audit, and qualified-review requirements materially determine the model route.
- Keep the scenario individual-professional in scope. Organization-wide compliance architecture, vendor procurement, policy, identity, centralized platform design, data-classification programs, and enterprise deployment belong in organization scenarios when they dominate the decision.
- Distinguish this scenario from `general-knowledge-worker/`: ordinary approved internal data can stay there; this route applies when the data class or failure consequence requires stronger controls than standard workplace use.
- Distinguish it from `independent-consultant/`: multiple client boundaries alone define that scenario; this one is defined by sensitivity/regulatory/professional obligations even for a single employer/client.
- Do not treat the scenario as legal/compliance certification. It defines evidence and routing requirements; the applicable organization, counsel, privacy/security team, professional standard, regulator, contract, or qualified reviewer determines what is actually permitted.

## Approval Before Capability

- Determine the **permitted processing boundary before selecting a model**. A technically capable model is irrelevant if the workflow is not approved for the exact data class.
- Identify the governing data classification and obligations: employer/client policy, confidentiality/privilege, professional duties, contract/DPA/BAA or equivalent, privacy law, sector rule, retention requirement, residency/sovereignty requirement, audit requirement, and incident-reporting boundary where applicable.
- Do not infer approval from provider marketing, consumer privacy settings, certification logos, encryption claims, `enterprise` naming, a local desktop client, or model reputation.
- Preserve a written/observable approval basis where the organization requires one: approved product/account/project, data classes, enabled features/connectors, region, retention mode, permitted users, and prohibited workflows.
- When approval is unclear or unavailable, use public/sanitized/synthetic material or stop external processing rather than guessing.

## Route Hierarchy

- Compare only routes that are actually eligible under the data boundary:
  1. organization-approved managed enterprise/workspace;
  2. approved API/project with the required data controls;
  3. approved private cloud/managed deployment;
  4. approved local/offline/self-hosted route;
  5. hybrid routing with explicit per-data-class rules.
- Do not include consumer assistants, aggregators, generic routing proxies, browser extensions, coding clients, or third-party agent platforms as convenience fallbacks unless their complete processing chain is separately approved.
- The strongest model is not automatically the preferred route. Select from the eligible set using accepted-result quality, review burden, latency, operational reliability, data exposure, and total cost.

## Complete Provider and Subprocessor Chain

- Trace the complete path for sensitive content: endpoint application → identity/account → intermediary/gateway → model provider → cloud region/inference → storage/logging → safety/abuse systems → connected apps/tools → subprocessors → support/administrative access.
- Verify which entities can receive prompts, outputs, files, embeddings/indexes, tool results, logs, telemetry, and derived metadata.
- Treat a model router/observability proxy as an additional data recipient unless the architecture proves otherwise.
- Treat connected search, web grounding, RAG, code execution, file processing, image/audio tools, MCP/actions, and third-party apps as potentially separate data paths with different retention/residency/subprocessor behavior.
- Do not assume the contract or residency rule for the base model request automatically covers every optional feature.

## Contracted Managed Workspace Route

- Use a contracted/approved enterprise workspace when it satisfies the exact data class and the professional needs low-administration access to strong hosted models, files, research, or internal sources.
- Current OpenAI enterprise/business documentation, for example, states that organization data is not used to train models by default and documents configurable retention for eligible managed products, access controls, encryption, data-residency options, and product-specific compliance support. Treat each property as exact-product/configuration evidence rather than a universal OpenAI guarantee.
- Managed workspace administrators can have materially different access/control/audit powers from ordinary colleagues. Keep personal/private material outside a managed work account unless that administrative boundary is acceptable.
- Verify enabled connectors, apps/actions, sharing, custom assistants, code execution, web research, and export features separately because they can expand the approved boundary.
- Do not assume that an enterprise workspace approved for one sensitive class is approved for every regulated or privileged class.

## Approved API and Zero/Reduced-Retention Route

- Use a direct API/project when the professional or organization needs a controlled application, deterministic tool contract, batch processing, structured outputs, private UI, or stronger project-level data controls than a general workspace provides.
- Current OpenAI API documentation distinguishes standard API retention from eligible Zero Data Retention configurations and documents regional/data-residency options for eligible customers/endpoints. Treat ZDR eligibility and endpoint compatibility as mutable and verify the exact project/endpoint/feature before use.
- Current OpenAI business/privacy material also documents that API business data is not used for training by default unless explicitly opted in; keep data-sharing/feedback settings controlled for sensitive projects.
- Do not translate `Zero Data Retention` into `zero data processing`: content is still processed to produce the response and may traverse the approved provider infrastructure/safety systems according to the documented architecture.
- Do not assume ZDR covers application state, files, vector stores, assistants/agents, fine-tuning, batch features, third-party tools, or every endpoint. Verify each component individually.
- Isolate API projects/credentials/budgets/logs by sensitivity/workload when doing so improves least privilege, revocation, audit, and deletion.

## Residency and Processing Location

- Distinguish **storage at rest**, **processing/inference location**, **support/administrative access**, **subprocessor location**, and **connected-service location**. A residency claim for one dimension does not automatically constrain the others.
- Current OpenAI enterprise/API offerings provide eligible at-rest residency across multiple regions and selected in-region processing options; current Google Cloud documentation similarly lists residency/configuration conditions and exclusions for generative AI services. Use exact current service documentation for the chosen route.
- Record the selected project/workspace region and the features that are excluded from that regional boundary when material.
- Do not route sensitive content through web grounding, external search, third-party retrieval, or an unapproved region simply because the base model endpoint is regional.

## Healthcare and Similar Contractual Requirements

- Where a sector requires a specific contractual instrument such as a Business Associate Agreement, confirm that the provider offers it for the **exact product/workload** and that the organization's agreement is actually executed before processing covered data.
- Current OpenAI enterprise privacy documentation states that OpenAI can sign BAAs for eligible healthcare/API use cases and provides ChatGPT for Healthcare; this supports route eligibility only, not automatic HIPAA compliance for the user's workflow.
- Apply the same rule to any sector-specific certification/contract claim: provider capability can support compliance, while the customer's configuration, access, workflow, data minimization, retention, and professional controls still matter.
- Do not use general consumer health/legal/financial chat for protected professional records merely because the answer quality appears sufficient.

## Privileged and Confidential Professional Material

- Treat attorney-client/work-product privileged material, audit/accounting workpapers, M&A/strategy documents, security incidents, confidential consulting deliverables, unreleased financials, protected research, and similar materials according to their governing policy before model use.
- Minimize disclosure even on an approved route: send only the documents/pages/fields needed for the bounded task.
- Preserve client/matter/case/project separation so retrieval, memory, indexes, or agent context cannot mix unrelated protected matters.
- Do not store secrets, passwords, signing keys, recovery codes, private keys, production credentials, or authentication tokens in conversational memory or document corpora merely for convenience.

## Sensitive Documents and Multimodal Inputs

- Classify text, scans, screenshots, photos, forms, audio, and video independently. A route approved for text may not be approved for biometric/voice/image/health or other special-category data.
- Verify OCR/document parsing and multimodal accuracy separately from language reasoning. Poor extraction can invalidate an otherwise strong model answer.
- Preserve original documents and page/section/table/field references for important conclusions.
- For structured forms, dates, identifiers, amounts, doses, account numbers, clauses, or other exact values, use deterministic extraction/validation or human verification rather than relying on fluent summaries.
- Redact or locally preprocess unnecessary identifiers, pages, image regions, metadata, or audio segments when they are not needed for the task.

## Local and Offline Route

- Use local/offline inference when external processing is prohibited, a controlled endpoint materially reduces exposure, connectivity is unavailable, or the organization explicitly approves local processing.
- Local processing is not automatically compliant or secure. Verify endpoint ownership, OS/account security, disk encryption, model/runtime source, telemetry, local logs/history, caches, backups, swap/temp files, network access, updates, malware/extension risk, and deletion behavior.
- Bind every local fit claim to the exact model artifact, runtime/backend, context, modality path, usable memory, storage, latency, and measured accepted quality.
- Preserve `Phi-4 Mini Instruct`, `Qwen3 8B`, and `Qwen3 14B` only as text-oriented evaluation candidates when exact hardware/task quality supports them; preserve `Gemma 4 E2B Instruct`/`E4B Instruct` only as compact multimodal candidates when the runtime supports the complete modality.
- Remove legacy `16–32 GB RAM` or `24 GB GPU` examples as recommendation thresholds. They can be historical planning evidence only, never guaranteed fit/quality/compliance tiers.
- If local quality is inadequate for the consequence of the task, the correct result can be `no acceptable model route` rather than lowering the review standard.

## Private Cloud or Self-Hosted Deployment

- Treat self-hosting/private cloud as infrastructure that must itself be approved and operated securely, not as a synonym for privacy.
- Verify model license, artifact provenance, container/image supply chain, network isolation, IAM, encryption, logging, backups, observability, secrets, patching, inference endpoint authentication, tenancy, deletion, and incident response.
- Confirm where model weights, prompts, outputs, vector indexes, object storage, snapshots, and logs reside.
- Keep external model registries, telemetry, package repositories, monitoring SaaS, and support channels visible in the provider chain.
- If operation becomes organization-wide platform work, route to the applicable internal-platform/high-security/regulated-organization scenario instead of duplicating infrastructure governance here.

## Retrieval and Knowledge Bases

- Treat RAG/enterprise search as retrieval assistance, not a compliance or correctness layer.
- Preserve source-system permissions and matter/client/data-class boundaries in retrieval/indexes.
- Verify embedding generation/storage, vector database, chunk caches, reranking, model inference, and citations as separate data recipients where applicable.
- Keep source provenance/freshness visible and require the model to cite the authoritative source for material claims.
- Prompt injection or malicious text inside retrieved documents remains a risk even when the corpus is private and authorized.
- Do not combine protected corpora merely because a shared vector database is operationally convenient.

## Agentic and Side-Effecting Work

- Treat agents that can query systems, modify records, send communications, change permissions, create filings, submit forms, execute code, or make other external changes as a materially higher-risk route than read-only assistance.
- Use least privilege, narrow tools/scopes, deterministic policy checks, human approval for consequential actions, immutable/auditable logs where required, and rollback/reconciliation procedures.
- Authorization to read sensitive information does not imply authorization to act on it.
- Do not let model judgment alone authorize payments, medical actions, legal filings, regulated disclosures, account changes, access-control changes, deletion, production/security remediation, or other high-impact actions.
- Keep prompt-injection defenses relevant for emails, documents, websites, tickets, records, and other untrusted content that an agent reads.

## Professional Accuracy and Qualified Review

- Define failure severity before choosing the model route. A workflow with low-tolerance consequences can require qualified human review on every output or prohibit model-generated conclusions entirely.
- Use AI to organize, extract, summarize, draft, compare, or identify questions; do not substitute model output for licensed/professional judgment where the governing standard requires qualified review.
- Require source verification for legal/policy/regulatory claims and deterministic validation for calculations, dates, identifiers, formulas, doses, accounting figures, or other exact values.
- Preserve uncertainty and source gaps. Do not let the model fill missing facts with plausible professional detail.
- For domain-specific accuracy, evaluate on representative accepted cases plus adversarial/error cases before production use.
- If the model's local/hosted quality ceiling cannot meet the review burden or failure tolerance, mark the workflow unsuitable for that model route.

## Evaluation and Acceptance Suite

- Build a bounded evaluation set from permitted/sanitized representative tasks for the exact profession and data class.
- Measure extraction accuracy, factual/source support, domain terminology, omission rate, structured-output validity, numerical correctness, citation support, refusal/escalation behavior, latency, review/correction time, and total accepted-result rate.
- Include adversarial cases: ambiguous source, conflicting documents, missing page, misleading prompt-injected text, near-identical identifiers, OCR error, stale rule, unsupported question, and a request that should escalate to a professional/human decision.
- Compare eligible enterprise/API/local routes using the same acceptance criteria rather than relaxing quality because one route is more private.

## Logging, Audit, and Data Minimization

- Log only what the approved workflow requires. Debug/observability logs can become a new copy of sensitive prompts, outputs, identifiers, or tool data.
- Separate operational metadata from content logging where possible.
- Apply retention/deletion to conversation history, API logs, files, indexes, caches, checkpoints, agent traces, exported reports, and local working directories according to the governing policy.
- Verify that deletion in the UI/application actually maps to the documented backend retention/deletion behavior for the selected product.
- Keep audit evidence sufficient to explain who/what processed data and what consequential action occurred when the governing workflow requires traceability.

## Cost per Accepted Sensitive Result

- Compare **total cost per accepted sensitive-data outcome**: enterprise seat/API/private compute cost, security/compliance review, integration/admin work, source verification, qualified human review, retries, local infrastructure, incident/risk burden, and the consequence of an erroneous or unauthorized result.
- Do not choose the cheapest model when it materially increases review burden or failure exposure.
- A contracted enterprise/API route can be cheaper overall than self-hosting if it satisfies the required controls and reduces operations burden.
- A local/private route can be preferable despite higher operational cost when external processing is prohibited or data-exposure risk dominates.
- Include the cost of maintaining multiple approved environments when different data classes cannot share one route.

## Escalation Triggers

- Move from ordinary professional use to this scenario when confidentiality, privilege, regulated data, contract, residency, audit, or failure severity requires stronger controls.
- Move from managed workspace to approved API/private deployment when endpoint-level retention, integration, logging, or regional controls are materially required and supported.
- Move to local/offline when external processing is prohibited and the exact local route meets quality and security requirements.
- Move from local to a contracted hosted/private route when local quality, modality support, context, reliability, or professional-review cost is unacceptable and external processing can be approved.
- Move to organization-scale `regulated-organization`, `high-security-environment`, `internal-ai-platform`, or another applicable route when centralized compliance/security/platform architecture becomes the real problem.
- Stop AI use for a task when no route simultaneously meets data-boundary and professional-accuracy requirements.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a permitted local/private model route depends materially on exact owned/fixed hardware.
- Use `../../../hardware/sub/computers/` for a professional workstation/laptop and `../../../hardware/sub/servers/` when an approved private inference server is already the target.
- Hardware purchasing remains outside this scenario; insufficient hardware can imply hosted/private managed execution or no acceptable local route.

## Canonical Links

- Link approved managed assistant/API products to canonical service owners when named.
- Link `Phi-4 Mini Instruct`, `Qwen3 8B`, `Qwen3 14B`, `Gemma 4 E2B Instruct`, and `Gemma 4 E4B Instruct` to their exact canonical Model Reference identities when named.
- Link specialized analysis/research/coding/creative workloads to their sibling scenario/decision-guide owners rather than duplicating those full contracts.
- Link organization-scale regulated/high-security/platform routes when centralized controls determine eligibility.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI enterprise/business/API privacy, Zero Data Retention, data-residency, BAA/compliance, and subprocessor documentation; current Google Cloud generative-AI data-residency documentation; and canonical AI Lab model/service owners.
- Current OpenAI evidence establishes no-training-by-default for business/API data, product-specific retention controls, eligible ZDR API configurations, regional storage/processing options, BAA availability for eligible healthcare/API use cases, encryption/security controls, and a published subprocessor chain. Each property remains product/feature/configuration specific and does not certify the customer's workflow.
- Current Google Cloud residency documentation demonstrates that generative-AI residency eligibility can include explicit feature/model conditions and exclusions. Treat every provider's optional grounding/RAG/agent/tool feature as a separate boundary until verified.
- Provider products, endpoint/ZDR eligibility, retention behavior, residency regions, subprocessor lists, contracts, certifications, model aliases, tool/connectors, and regulatory requirements are mutable; recheck them before rendering current guidance.
- Provider evidence supports route eligibility; the organization/professional remains responsible for approval, configuration, and qualified review.

## Validation

- Approval and data classification precede model capability selection.
- The complete provider/intermediary/subprocessor/tool chain is considered before external processing.
- Training default, retention/ZDR, residency, encryption, certification, and contractual instruments remain separate properties rather than one `enterprise-safe` label.
- Consumer/aggregator convenience is not treated as approval for sensitive data.
- Local/self-hosted processing is not presented as automatic compliance/security or sufficient domain-quality evidence.
- RAG/private corpora do not remove source correctness, permission, prompt-injection, or provider-chain risks.
- Read access and side-effecting agent authority remain distinct.
- Qualified review/failure severity can make a technically available route unacceptable or prohibit AI use for the task.
- Legacy RAM/GPU examples are not used as fit tiers.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
