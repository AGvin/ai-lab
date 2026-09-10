# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale batch/stream processing of large document corpora such as forms, invoices, contracts, correspondence, scanned archives, claims, applications, reports, statements, IDs, emails/attachments, or mixed business records.
- Keep the scenario organization-scale. Occasional document analysis belongs in personal/professional/team routes; organization-wide knowledge search over already processed content belongs in `business-knowledge-assistant/`.
- The defining constraints are **throughput, document diversity, OCR/layout quality, structured extraction, validation, review routing, cost per accepted document, data boundary, retries/idempotency, and downstream system integrity**.
- Do not reduce this route to `use a multimodal LLM`. Production document processing is a pipeline with independently testable stages.

## Decompose the Processing Pipeline

- Model the workflow explicitly: intake → file validation/normalization → document classification/splitting → OCR/layout parsing → entity/table/field extraction → normalization → deterministic validation → confidence/error routing → redaction/enrichment where needed → human review → downstream storage/action → audit/archive.
- Choose specialized processors, deterministic parsers, and generative models by stage rather than forcing one model to own the whole pipeline.
- Preserve original input, page/document identity, processing version, extracted structured output, validation result, and downstream record ID for traceability.
- Make failed/partial states explicit; do not mark a document complete because one model returned syntactically valid JSON.

## Specialized Document-AI Route

- Prefer a production document-processing service when OCR, layout, form/table extraction, classification/splitting, schemas, validation, review tooling, throughput, and operational APIs matter more than open-ended conversational reasoning.
- Current Google Document AI is an example: current documentation separates OCR, Form Parser, Layout Parser, custom extraction, classification, and splitting processors and supports document-review/evaluation workflows. Treat exact processors/versions/features/regions/pricing as mutable.
- Current Document AI custom extractor versions increasingly use foundation/generative models while retaining structured extraction/validation contracts; treat this as evidence for hybrid specialized+generative pipelines rather than replacing validation.
- Evaluate exact processor/version on representative organization documents rather than provider aggregate accuracy claims.

## OCR and Layout Are Separate Evidence

- Measure OCR text accuracy, reading order, page boundaries, table/figure/list/header structure, handwritten/low-quality scans where applicable, and document image quality before evaluating extraction/reasoning.
- Current Document AI layout parsing explicitly combines OCR with structure-aware parsing for headings, tables, figures, and lists; this does not establish perfect extraction on the organization's layouts.
- Treat skew, blur, compression, rotation, handwriting, stamps, overlapping marks, low contrast, unusual fonts, multilingual text, and multi-column pages as explicit test cases where relevant.
- Preserve page coordinates/bounding boxes or equivalent source references when later validation/audit requires them.
- Do not let an LLM hallucinate text for unreadable regions; return uncertain/unreadable state.

## Classification and Splitting

- Classify document type before extraction when different schemas/rules/processors apply.
- For multi-document PDFs/scans, verify split boundaries so pages are not attached to the wrong record.
- Include unknown/unsupported document classes and mixed-version templates in evaluation.
- Do not force low-confidence inputs into the nearest known class; route to review or generic extraction where appropriate.
- Preserve classifier version and confidence/decision evidence sufficient for debugging recurring routing errors.

## Structured Extraction Contract

- Define explicit schemas with field names, types, required/optional state, cardinality, normalization, and source-reference expectations.
- Keep exact identifiers, dates, amounts, currencies, units, addresses, account/order/reference numbers, clauses, tables, and line items separate from free-form summaries.
- Require structured-output validation; valid JSON/schema syntax does not prove field correctness.
- Distinguish absent field, unreadable field, not applicable, ambiguous candidates, and inferred value rather than mapping all uncertainty to null or a plausible value.
- Preserve source page/region/text for important extracted fields so reviewers can trace errors.

## Deterministic Validation and Business Rules

- Apply deterministic checks after extraction where possible: type/range, checksum, totals, date ordering, currency/unit consistency, field dependencies, reference lookup, schema constraints, reconciliation, duplicate detection, and policy rules.
- Current Document AI offers validation/correction capabilities for custom extraction in current preview versions; regardless of product, validation rules remain separate from generative extraction.
- Do not allow the same model to both invent a value and certify that value without independent evidence.
- Route validation failures to reprocessing, alternate extraction, or human review according to defined policy.
- Preserve which validation rule failed and the original extracted value.

## Generative Extraction and Enrichment

- Use a generative/multimodal model where document variation or semantic interpretation makes fixed OCR/rules insufficient: free-form clauses, narrative classification, semantic normalization, summaries, cross-field interpretation, or complex unstructured extraction.
- Keep exact model/version/prompt/schema/runtime in reproducibility records when generative output becomes production data.
- Ground generative extraction in the actual document/OCR content and require source spans/pages for high-value fields where practical.
- Do not use model world knowledge to fill missing document fields unless the workflow explicitly requests a separately labeled inference.
- Evaluate generative extraction independently from OCR/layout so improvements/regressions can be localized.

## Tables and Line Items

- Treat table detection, row/column boundaries, merged cells, multi-page continuation, headers, repeated sections, totals, units, and footnotes as separate acceptance concerns.
- Reconcile extracted totals/subtotals with line items where arithmetic relationships exist.
- Preserve row identity and source page/region so downstream corrections are traceable.
- Do not flatten a table into prose and reconstruct values through language-model memory when structured parsing is available.
- Include irregular tables and empty/missing rows in evaluation.

## Duplicate and Document Identity

- Define exact duplicate, near duplicate, revision/version, resend, corrected copy, and legitimate recurring document semantics.
- Use hashes/identifiers/metadata plus content similarity where appropriate; do not deduplicate solely from model semantic similarity.
- Preserve canonical document ID and version lineage.
- Ensure retries/idempotency do not create duplicate downstream records.
- Do not delete source documents merely because an AI process classifies them as duplicates without a deterministic retention rule.

## Human Review and Confidence Routing

- Route ambiguous/high-risk/low-confidence documents or fields to trained human review.
- Define review threshold from actual error cost and field/document class rather than a universal confidence number.
- Sample high-confidence automated outputs too, because model confidence can be miscalibrated.
- Capture corrections as labeled evaluation data and use them to identify document types/fields requiring pipeline changes.
- Preserve reviewer identity/time/change history where audit requires it.

## Redaction and Sensitive Data

- Treat redaction as a deterministic/security-sensitive workflow, not merely visual black boxes generated by a model.
- Detect/redact the intended data categories, then verify the underlying exported content cannot expose supposedly removed text/metadata/layers.
- Keep original and redacted versions separated with access controls.
- Use human/qualified review for high-risk redaction classes where a miss can cause material disclosure.
- Do not feed an unredacted source to downstream providers whose data boundary only permits redacted content.

## Downstream Writes and System Integrity

- Separate extraction from actions such as creating/updating CRM/ERP/claims/case/accounting/database records, triggering payments, sending communications, or approving workflows.
- Validate document identity, target record, field values, totals, authorization, and idempotency before writes.
- Use transactional/reconciliation patterns where duplicate/partial writes can cause business harm.
- Keep write actions behind deterministic policy and human approval according to consequence.
- Preserve downstream record/action IDs for audit and rollback/reconciliation.

## Batch, Queue, and Retry Semantics

- Design ingestion around explicit job/document/page states, bounded retries, dead-letter/error queues, timeouts, and backpressure.
- Distinguish transient provider/runtime failure from bad/unsupported document and validation failure.
- Do not retry deterministic extraction failures indefinitely.
- Preserve idempotency across provider/API retries and worker restarts.
- Define behavior for partial multi-page processing so a single page failure does not silently produce incomplete accepted output.

## Throughput and Capacity

- Measure pages/documents per unit time, average/peak pages per document, file size, OCR/extraction latency, batch size, concurrency, queue depth, rate limits, and downstream write capacity.
- Test sustained throughput, not only single-document latency.
- Include provider quotas, autoscaling/warmup, model/API rate limits, storage/network transfer, and human-review capacity.
- Define SLA/processing deadline by document class where required.
- Track p50/p95/p99 completion time and failure/review rates for production workflows.

## Cost per Accepted Document

- Compare **total cost per accepted document/record**, including OCR/layout/classification/extraction API charges, generative tokens, storage/egress, retries, review labor, validation, infrastructure, downstream correction, and error/incident burden.
- Current Document AI pricing separates OCR, extraction, layout parsing, and other processors, illustrating why stage-level cost should be measured rather than one `AI request` cost.
- A cheaper extraction model can be more expensive when review/reprocessing rate is high.
- Use specialized deterministic extraction where it reduces cost/variance without sacrificing acceptance.
- Model human review capacity/cost as part of scaling, not an external afterthought.

## Evaluation Dataset

- Build a versioned representative dataset stratified by document class, template/version, source channel, scan quality, language, length, table complexity, and sensitivity.
- Maintain field-level ground truth for critical structured extraction and document-level labels for classification/splitting.
- Include unknown/out-of-distribution documents, corrupted files, blank pages, repeated documents, adversarial/prompt-injected text, and documents that require review.
- Score OCR/layout, classification/split, field precision/recall/exact match, table accuracy, validation pass, review rate, downstream correctness, latency, and cost.
- Re-run regression after processor/model/prompt/schema/OCR/runtime changes.

## Prompt Injection and Embedded Instructions

- Treat document text as untrusted content. Instructions embedded in PDFs, email attachments, forms, or images must not override extraction/system policy or trigger external actions.
- Keep extraction schemas/tools fixed outside document-controlled text.
- Isolate action-capable agents from raw untrusted document instructions.
- Test visible/hidden prompt-injection patterns when generative models process external documents.
- Do not expose secrets or broader system context because a document asks for them.

## Data Boundary, Retention, and Residency

- Classify document sources and fields before selecting managed/self-hosted processing.
- Verify storage, processing region, retention/logging, training/data-use terms, OCR/generative processor differences, human-review surfaces, and subprocessors for the exact service/version.
- Current Document AI release notes demonstrate that processor versions can have different region/data-residency characteristics, including preview models using global endpoints; never infer residency from product family name alone.
- Apply retention/deletion to original files, normalized images, OCR text, extracted JSON, indexes, logs, review copies, and downstream staging.
- Escalate regulated/high-security documents to applicable stronger-control scenarios.

## Self-Hosted and Hybrid Route

- Use self-hosted/private OCR/extraction/generation when external processing is prohibited or scale/control economics justify infrastructure.
- Keep pipeline stages independently replaceable and evaluated.
- Bind model/runtime/hardware claims to exact document workload, batch/concurrency, context, modality, memory, and measured output quality.
- Hybrid routes can keep raw sensitive documents/OCR local while sending only approved extracted/sanitized context to hosted models.
- Local hosting does not remove model/license, security, OCR quality, validation, review, observability, or action-safety requirements.

## Observability and Audit

- Record processor/model/schema/prompt version, source document ID/hash, timestamps, stage outcomes, retries, validation failures, review corrections, and downstream writes.
- Monitor drift by document class/field and sudden shifts in review/failure rate.
- Keep enough diagnostic artifacts to investigate extraction errors while respecting sensitive-data retention.
- Alert on queue backlog, quota/provider failure, OCR quality degradation, high validation failure, and downstream mismatch.

## Escalation Triggers

- Move from ad hoc file analysis to this scenario when document volume, structured extraction, validation, automation, or operational SLAs become first-order.
- Move toward `business-knowledge-assistant/` after processing when the primary use becomes search/Q&A over the resulting corpus.
- Move to legal/finance/customer-service specialized organization scenarios when domain-specific review/action controls dominate.
- Move to `internal-ai-platform/` when shared model/document APIs, gateways, budgets, observability, and cross-team platform ownership become primary.
- Move to regulated/high-security routes when document data requires materially stronger isolation/compliance.
- Stop straight-through automation for a class/field when validation/review evidence cannot reach the required accuracy threshold.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after a self-hosted/private processing target is selected and exact hardware materially constrains OCR/multimodal/generation fit.
- Use `../../../hardware/sub/servers/` for shared batch processing/inference infrastructure.
- Document-processing hardware procurement remains outside this scenario.

## Canonical Links

- Link exact document/OCR services and software to canonical catalog owners when named/materialized.
- Link exact multimodal/generation models only to canonical Model Reference owners after stage-specific evidence justifies them.
- Link downstream knowledge/platform/domain scenarios rather than duplicating their complete contracts.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Google Document AI overview, processor/release-note, layout parser, validation/correction, and pricing documentation.
- Current evidence establishes specialized OCR/layout, extraction, classification/splitting, generative custom extraction, validation/correction, review/evaluation, and stage-specific pricing; processor versions can have different preview/GA and region/residency behavior.
- Processor/model versions, regions, limits, pricing, OCR/layout features, generative extraction, validation, and data terms are mutable; recheck them before rendering current guidance.
- Provider capability claims do not replace organization-specific ground truth and field/document acceptance testing.

## Validation

- The workflow is decomposed into independently testable document-processing stages rather than one monolithic multimodal LLM.
- OCR/layout quality is separated from extraction/reasoning quality.
- Structured fields preserve schema, source traceability, uncertainty, and deterministic validation.
- Human review is risk/field/class driven and high-confidence outputs are still sampled.
- Retries are bounded/idempotent and do not duplicate downstream records.
- Embedded document instructions cannot expand model/tool authority.
- Residency/data terms are verified per exact processor/version rather than product label.
- Cost is measured per accepted document/record including review and correction.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
