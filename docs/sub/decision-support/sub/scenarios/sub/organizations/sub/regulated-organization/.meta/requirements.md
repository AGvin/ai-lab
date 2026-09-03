# Documentation Requirements

## Scenario Fit

- Present this scenario for an organization whose AI workloads are materially constrained by sector regulation, privacy/data-protection obligations, records requirements, model risk, audit, approved-provider controls, residency/sovereignty, or other formal governance obligations across multiple teams and use cases.
- Keep the scenario organization-scale. One professional handling sensitive data belongs in `professionals/sensitive-data-professional/`; disconnected/air-gapped/threat-sensitive isolation belongs in `high-security-environment/` when isolation rather than regulatory governance is the primary constraint.
- The defining constraints are **regulatory mapping, approved use cases/providers/models, data classification and processing purpose, retention/records, residency and cross-border processing, model risk/validation, human oversight, change control, third-party risk, audit evidence, incident response, and prohibited/restricted uses**.
- Do not present this page as legal/compliance certification. It defines the model-route and evidence requirements; the organization's counsel/compliance/privacy/security/risk owners and applicable regulators determine actual obligations.

## Regulation and Policy Before Model Choice

- Inventory the regulations, contractual commitments, internal policies, professional standards, and supervisory expectations that apply to each AI use case before selecting a model/provider.
- Map requirements to concrete controls rather than using a generic `compliant AI` label.
- Distinguish data-protection/privacy rules, sector rules, records/retention, accessibility, consumer protection, employment, financial/medical/legal professional obligations, cybersecurity, export/sanctions, AI-specific regulation, and contractual controls where material.
- Record jurisdiction, legal entity/business unit, data subjects/customers, processing purpose, effective date, and accountable owner.
- Re-evaluate when laws/guidance/contracts or the use case materially change.

## Use-Case Classification

- Maintain an inventory of AI use cases with owner, business purpose, users, affected people, data classes, provider/model, tools/actions, decision consequence, autonomy level, human oversight, environment, and current approval state.
- Classify uses by failure severity and regulatory impact rather than one organization-wide model risk score.
- Keep `experimental`, `approved`, `restricted`, `prohibited`, `suspended`, and `retired` states where lifecycle requires them.
- Do not let a generally approved enterprise model imply every new application is automatically approved.
- Require reassessment when an informational assistant gains retrieval, personalization, automated decisions, or side-effecting tools.

## Data Classification and Processing Purpose

- Identify the data classes processed by each stage: prompts, files, images/audio/video, retrieved records, embeddings, fine-tuning data, outputs, logs, traces, caches, agent tool results, and evaluation data.
- Define purpose, minimum necessary data, retention, access, approved regions/providers, and deletion requirements for each class as applicable.
- Do not send regulated/special-category/highly sensitive data merely because a provider product supports the file type.
- Use redaction, tokenization, pseudonymization, aggregation, synthetic data, local preprocessing, or restricted environments when they preserve the objective with less exposure.
- Treat derived embeddings/summaries/classifications as potentially regulated data when they encode protected source information.

## Approved Provider and Product Boundary

- Approve the **exact product/account/API/project/feature configuration**, not only the vendor name.
- Verify provider data-use/training defaults, retention, abuse/safety monitoring, human/support access, encryption, residency/processing locations, subprocessors, connected tools, logs, fine-tuning, files/vector stores, and optional features separately.
- Current OpenAI enterprise/API documentation provides current examples of business-data no-training-by-default commitments, product-specific retention controls, eligible Zero Data Retention configurations, residency options, security controls, subprocessors, and BAA support for eligible healthcare use. Treat each property as exact-product/configuration evidence rather than a universal OpenAI property.
- Current Google Cloud Vertex AI and Microsoft Azure AI/OpenAI documentation likewise expose product-specific security, privacy, regional, network, encryption, audit, and compliance controls; verify exact model/service/feature behavior before approval.
- Do not approve a consumer account, aggregator, browser extension, model router, plugin, or third-party agent merely because its upstream model provider is approved.

## Contract and Third-Party Risk

- Review the applicable customer agreement, DPA/BAA or sector-specific contract, service terms, privacy/data-processing terms, subprocessors, security documentation, incident obligations, deletion/return, audit rights, and service-location commitments as required.
- Treat provider subprocessors and embedded third-party tools as part of the processing chain.
- Re-review after material subprocessor, product, region, feature, or contract changes.
- Keep vendor questionnaires/certifications as evidence inputs, not substitutes for architecture/use-case review.
- Preserve contract/version/effective date and organizational approval owner for production routes.

## Residency, Sovereignty, and Cross-Border Processing

- Distinguish data storage at rest, inference/processing location, backup/replication, support/administrative access, telemetry/audit, safety/abuse systems, subprocessors, connected apps, and model-training/fine-tuning paths.
- A residency option for one product component does not automatically constrain every related feature or subprocessor.
- Current enterprise AI services expose regional/residency controls with feature/model/region-specific eligibility and exclusions; verify the exact selected deployment rather than product family name.
- Record approved regions and prohibited cross-border paths for each data class/use case where applicable.
- Do not enable web grounding, external search, third-party apps, or global-only preview features when they violate the approved regional boundary.

## Network and Access Controls

- Use organization identity, SSO, RBAC/ABAC, workload identities, least privilege, private networking/service perimeters, firewall/egress controls, Conditional Access, and approved endpoint/device controls where required.
- Current Vertex AI, Azure AI/OpenAI, and comparable enterprise services provide product-specific private networking/perimeter/identity controls; exact support varies by feature and model.
- Do not rely on prompt instructions for access control that deterministic infrastructure can enforce.
- Separate human user, application/service, agent, provider administrator, and support/operator access.
- Test negative access, offboarding, role changes, privileged/admin paths, and service-account boundaries.

## Retention and Records Management

- Define retention separately for user conversation/history, API request logs, provider abuse/safety logs, files, embeddings/vector stores, fine-tuning datasets/checkpoints, agent traces, local caches, exported reports, and organization audit records.
- Preserve legally/business-required records even when minimization favors deletion; use the governing retention schedule rather than generic `delete everything` guidance.
- Verify provider deletion semantics and residual retention windows for the exact product/feature.
- Distinguish operational logging from regulated business records and legal hold requirements.
- Ensure offboarding/deletion does not accidentally remove evidence that must be retained for audit or litigation.

## No-Training and Data-Use Controls

- Treat `not used to train models by default`, `opt out`, `zero data retention`, and `private endpoint` as distinct properties.
- Do not translate no-training into no retention or no processing.
- Do not translate Zero Data Retention into zero provider processing or assume every endpoint/feature is eligible.
- Control explicit data-sharing/feedback/evaluation opt-ins for regulated projects.
- Verify fine-tuning/customization data ownership, reuse, retention, and checkpoint handling separately.

## Model and Version Approval

- Maintain an approved model/version/deployment inventory with use-case scope and evidence date.
- Treat provider aliases that may change model versions as mutable dependencies.
- Require regression/validation before material production model changes, especially for regulated/high-consequence workflows.
- Preserve rollback or prior approved model where operationally required.
- Do not introduce new preview/beta models into regulated production solely for capability gains without the required risk/change process.

## Model Risk and Validation

- Define what must be validated for each use case: factual accuracy, extraction, structured output, numerical correctness, bias/fairness, robustness, refusal/escalation, hallucination, source/citation support, privacy leakage, prompt injection, tool/action safety, latency, reproducibility, and human-review burden as applicable.
- Use representative organization data/tasks within the approved data boundary.
- Maintain versioned acceptance thresholds and owners.
- Test known failure cases and out-of-distribution/ambiguous inputs, not only successful examples.
- Provider evaluations/benchmarks are candidate evidence; organization validation owns production acceptance.

## Human Oversight

- Define where humans must review, approve, override, or receive escalation based on regulation, professional duty, failure severity, data sensitivity, and action consequence.
- Make model uncertainty/source/evidence visible enough for meaningful review.
- Do not use a nominal human approval step that provides no practical ability/time/context to detect errors.
- Keep deterministic approvals where regulation/business policy requires them.
- Preserve reviewer/approver identity, result, and evidence for consequential decisions where audit requires it.

## Automated and High-Impact Decisions

- Treat decisions materially affecting people, eligibility, employment, credit/finance, health, legal rights, insurance, education, public benefits, safety, or access as a separate high-risk class.
- Do not let generative model output become the sole decision basis where law/policy requires explainability, review, deterministic criteria, or qualified judgment.
- Preserve decision inputs, policy/rule version, model output, human review, final decision, and appeal/reconsideration path as applicable.
- Evaluate disparate error and harmful outcome risk across relevant populations/use contexts.
- Keep prohibited or unacceptably risky automated decisions out of the AI route entirely.

## Agentic and Side-Effecting Workflows

- Treat agents that modify records, send communications, file reports, approve/reject, change access, move money, affect customers/patients/employees, or execute production/security actions as higher-risk than read-only assistance.
- Apply explicit workload identity, least privilege, tool allowlists, deterministic policy checks, human approvals, idempotency, audit, rollback/reconciliation, and bounded retries.
- Do not let model reasoning bypass regulated approval/segregation-of-duties/professional-review controls.
- Preserve action trace and authoritative resulting system state.
- Route common cross-system agent architecture to `enterprise-workflow-automation/` while retaining regulation-specific controls here.

## Retrieval and Knowledge Systems

- Preserve source-system permissions, provenance, effective dates, and record status for RAG/enterprise knowledge.
- Treat retrieved regulated records as untrusted instructions for prompt-injection purposes.
- Do not assume private/authorized source content is correct/current.
- Keep source citations/IDs and require qualified review for material interpretations.
- Route broad retrieval architecture to `business-knowledge-assistant/` while preserving regulatory retention/access/currentness here.

## Structured Data and Analytics

- Use deterministic SQL/code/statistical systems for calculations/metrics and preserve canonical semantic definitions, access policies, and lineage.
- Do not use free-form model arithmetic for regulated reports, financial/clinical/legal calculations, or material thresholds.
- Route platform-level analytical architecture to `enterprise-data-analysis/` where appropriate.
- Validate model-generated queries/code before execution and preserve result provenance.
- Keep reporting/filing calculations reproducible.

## Document and Record Processing

- Decompose OCR/extraction/classification/validation/human review/downstream write stages.
- Preserve document/record identity and source location for extracted regulated fields.
- Use deterministic validation for exact identifiers/dates/amounts/doses/clauses/fields where errors matter.
- Route scale-specific pipeline design to `high-volume-document-processing/`.
- Do not let a generative summary replace the source record required for audit/records management.

## Bias, Fairness, and Protected Characteristics

- Identify whether the use case can affect protected groups or uses sensitive/proxy attributes.
- Evaluate errors and outcomes on relevant groups/contexts where legally/ethically required and statistically meaningful.
- Do not infer protected attributes from free-form data merely to improve personalization/ranking.
- Separate bias/fairness analysis from general model quality.
- Preserve mitigation/approval decisions and monitoring where required.

## Transparency and Disclosure

- Define required employee/customer/public disclosures, AI-use notices, explanations, contestability/appeal, record access, or generated-content labeling based on the use case and jurisdiction.
- Keep disclosure wording and triggers controlled by approved policy/legal owners rather than generated ad hoc.
- Do not claim a model explanation exposes true internal reasoning; provide source, rules, inputs, and decision factors that are actually available.
- Preserve provenance/content credentials where required for generated media, but do not treat them as ownership/factual-authenticity certificates.

## Regulatory Change and Currentness

- Monitor authoritative regulatory/standards/guidance sources relevant to approved AI use cases.
- Record effective dates and transition periods and distinguish proposal/guidance/final/enforced status.
- Reassess affected use cases/providers/models before deadlines rather than automatically changing policy from an AI summary.
- Keep legal/compliance interpretation human/qualified-owner controlled.
- Define an emergency suspension path when a regulatory or provider change invalidates an approved route.

## Change Management

- Route changes to model/version, provider, region, prompt/policy, retrieval source, tool/action, autonomy level, data class, user population, or business purpose through a risk-based change process.
- Use canary/shadow/bounded rollout and rollback where material.
- Re-run applicable validation and update documentation/evidence before promotion.
- Do not bundle many high-risk changes so regression causes cannot be isolated.
- Preserve change approval and effective date for regulated production workflows.

## Monitoring and Periodic Review

- Monitor production quality, refusal/escalation, bias/error indicators, privacy/security incidents, prompt injection, unsupported claims, action errors, human overrides, complaints, provider/model drift, latency, and cost as relevant.
- Define periodic reapproval frequency based on risk and regulation.
- Trigger out-of-cycle review after incidents, material provider/model changes, new data/tool access, or use-case expansion.
- Do not let `approved once` become permanent authorization.

## Incident Response and Regulatory Reporting

- Define incident categories covering data exposure, unauthorized access/action, harmful output/decision, provider outage, model regression, prompt injection, cross-tenant leakage, records failure, and policy bypass.
- Preserve logs/evidence needed to investigate and meet notification/reporting obligations.
- Maintain ability to disable models/providers/tools/agents quickly.
- Coordinate AI incident response with privacy, security, legal, compliance, business, and provider processes.
- Do not rely on the affected model to determine whether an incident is reportable.

## Audit Evidence

- Preserve an auditable chain linking use-case approval, data classes, provider/product/configuration, contracts, model/version, validation, policies, identities/permissions, prompts/workflows where material, sources, human review, actions, monitoring, incidents, and changes.
- Protect audit records from inappropriate modification/deletion.
- Make evidence retrievable by use case and effective period.
- Avoid logging unnecessary sensitive content solely for audit; record identifiers/hashes/metadata where sufficient.
- Test that the organization can reconstruct a consequential AI-assisted decision/action from retained evidence.

## Shadow AI and Enforcement

- Provide approved practical routes so policy does not simply push employees toward unapproved personal tools.
- Detect/control unapproved SaaS/browser extensions/API keys/model routers where organization policy requires it.
- Separate policy education from technical enforcement.
- Offer a path for teams to request new providers/models/use cases through review rather than bypassing governance.
- Revoke/decommission unapproved routes and migrate business artifacts to approved systems where necessary.

## Local, Private, and Sovereign Routes

- Use private/self-hosted or sovereign managed routes when regulation/data boundary requires greater control than standard SaaS/API options.
- Keep the same model validation, access, audit, change, monitoring, and human-oversight requirements; `local` is not a compliance exemption.
- Verify model/runtime/artifact supply chain, network, administrators, logs, backups, updates, deletion, and exact processing locations.
- Escalate to `high-security-environment/` when disconnected/air-gapped/threat-sensitive operation becomes the dominant architecture.
- Escalate centralized model/gateway/runtime design to `internal-ai-platform/` where platform concerns dominate.

## Cost per Accepted Regulated Outcome

- Compare **total cost per accepted regulated outcome**: model/provider/platform spend, private networking/residency, legal/privacy/security/risk review, validation, human oversight, audit/records, monitoring, incident response, local infrastructure, and error/regulatory exposure.
- A more expensive contracted enterprise service can be cheaper overall when it reduces operational/compliance burden and provides required controls.
- Self-hosting can increase control but adds staffing, validation, security, lifecycle, and audit responsibility.
- Do not optimize away required human/qualified review merely to improve automation economics.

## Escalation Triggers

- Move to this scenario when AI governance must satisfy formal regulatory/audit/records obligations across multiple organization use cases.
- Move to `high-security-environment/` when isolation/sovereignty/disconnected operations dominate rather than general regulatory governance.
- Move to `internal-ai-platform/` when centralized model/provider/gateway/runtime engineering is the main problem.
- Keep domain-specific legal/finance/security/health/customer controls in their scenario owners while applying this regulatory layer.
- Prohibit or suspend a use case when no available route satisfies both regulatory and quality/action requirements.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted regulated inference target is selected and hardware materially constrains model/runtime/concurrency fit.
- Use `../../../hardware/sub/servers/` for shared organization regulated/private inference infrastructure.
- Hardware procurement remains outside this scenario.

## Canonical Links

- Link sensitive-professional, enterprise-workflow, internal-platform, high-security, legal, finance, SOC, and other domain concerns to their scenario owners rather than duplicating their full contracts.
- Link named enterprise AI providers/services and exact models to canonical catalog owners when materialized.
- Keep regulation-specific legal interpretation outside model-selection documentation.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI enterprise/API privacy, retention/ZDR, data-residency, security/compliance/BAA, and subprocessor documentation; current Google Cloud Vertex AI security/privacy/residency/network/audit documentation; and current Microsoft Azure AI/OpenAI data-privacy/security/compliance documentation.
- Current evidence establishes materially different enterprise controls across exact products/configurations, including no-training defaults, retention options, regional processing/storage, private networking/service perimeters, identity/access, encryption, audit/monitoring, contractual and sector-specific features. These controls support compliance programs but do not certify an organization's use case.
- Regulations, provider products/features, contracts, subprocessors, certifications, regions, retention/ZDR eligibility, audit capabilities, models, and AI-specific legal requirements are mutable; recheck them before rendering current guidance.
- The organization's current legal/compliance interpretation, exact provider configuration, validated use case, human oversight, and audit evidence remain the acceptance authority.

## Validation

- Regulation/policy/use-case approval precedes model capability selection.
- Provider approval is exact-product/configuration specific and includes subprocessors/features rather than vendor name alone.
- No-training, retention/ZDR, residency, encryption, compliance certifications, and contractual instruments remain separate properties.
- Use-case inventory, data classification, model/version approval, validation, human oversight, change control, monitoring, incidents, and audit form one lifecycle.
- Automated high-impact decisions and side-effecting agents have stronger deterministic/human controls than read-only assistance.
- RAG, analytics, documents, and domain workflows keep their authoritative source/validation systems.
- Local/private operation does not remove regulatory, model-risk, audit, or change-management requirements.
- No route is recommended when regulatory and accepted-quality/action requirements cannot both be met.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
