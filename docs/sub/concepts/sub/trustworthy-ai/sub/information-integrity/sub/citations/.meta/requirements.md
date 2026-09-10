# Documentation Requirements

## Requirements

- Use the reader-facing title `Citations`.
- Define a citation as an explicit reference/attribution from a generated, extracted, or derived statement to an identifiable source or evidence location so a reader/system can inspect the material claimed to support, contextualize, or originate that statement.
- Distinguish citation presence from citation correctness. A source can be cited while failing to support the attached claim, supporting only part of it, contradicting it, or merely discussing the same topic.
- Distinguish citation correctness from source quality/authority. A citation can faithfully point to what a low-quality, outdated, biased, or malicious source says; source evaluation remains a separate information-integrity requirement.
- Distinguish citation completeness from correctness. Every provided citation can be correct while important factual/derived claims remain unsupported; completeness asks whether the claims that require evidence have adequate citation coverage.
- Distinguish citation specificity/granularity from source identity. A document-level reference can be traceable but too broad for efficient verification; page/section/line/paragraph/record/field/timestamp/query-result identifiers can improve specificity when the source format supports them.
- Treat citation formatting as presentation rather than evidence semantics. Numbered footnotes, inline links, author-date style, source chips, file citations, database record references, timestamps, or structured citation objects can all represent the same underlying claim-to-source relation.
- Require source identity to be generated from trusted/retrieved metadata or deterministic source records where feasible rather than allowing the model to invent titles, URLs, authors, page numbers, IDs, DOIs, or timestamps from memory.
- Distinguish a cited source from the exact supporting evidence span. A stable source identifier/version plus a precise location/passage enables stronger verification than a bare homepage or document title when claim-level checking is required.
- Preserve source version/time where mutable content matters. A URL can serve different content over time; software docs, policies, database rows, API responses, web pages, inventories, and prices can require version/date/snapshot identifiers to make the citation reproducible.
- Distinguish citations from `grounding/`. Citations expose references; grounding evaluates whether evidence supports the claim. A grounded system can omit user-visible citations, while a citation-enabled system can produce unsupported or fabricated citations.
- Distinguish citations from provenance. A citation identifies a referenced source/evidence relation; provenance can additionally describe origin, custody, transformations, extraction, retrieval, and process history. One does not fully replace the other.
- Distinguish citations from quotations. A quotation reproduces source content; it still requires correct attribution/location and can be misleading if truncated or taken out of context. A citation can support paraphrased/synthesized claims without a direct quote.
- Distinguish generated/source-derived citations from post-hoc citations. A post-hoc process can find evidence supporting an already generated claim, but that does not prove the cited source was used during generation; represent support/attribution and process provenance separately when it matters.
- Treat multi-source synthesis explicitly. A claim may require several citations when no one source supports the entire conclusion; attaching only one convenient source can overstate its support.
- Treat compound claims carefully. If a sentence contains several factual clauses, comparative assertions, causal statements, or conditions, one citation should not be assumed to support every component unless the evidence does.
- Explain source-to-claim directionality. A citation should make clear which claim(s) it supports; dumping a source list at the end of a long answer can preserve bibliography but lose claim-level attribution.
- Explain citation placement and readability as a usability trade-off. More precise citation density can improve verification while excessive markers can degrade readability; choose granularity based on risk, audience, and evidence needs rather than one fixed every-sentence rule.
- Explain non-text evidence citations. Images, audio/video, source code, database records, logs, API responses, calculations, and tool outputs may need frame/timestamp/line/record/run identifiers or structured evidence references rather than conventional bibliographic citations.
- Explain derived/tool evidence. A calculated claim can cite/reference both the source inputs and the deterministic computation/tool result when verification requires reconstructing the result.
- Treat citation resolution as a system invariant. References should remain resolvable after chunking, document moves, re-indexing, PDF/page transformations, OCR changes, or data version updates; source IDs/offsets must not silently drift to unrelated content.
- Preserve access/security boundaries. A citation should not expose a protected document, signed URL, internal record ID, secret query, tenant data, or restricted evidence to a user who lacks permission merely to make the answer look verifiable.
- Explain citation verification dimensions such as entailment/support, completeness/coverage, specificity, source identity/version, resolvability, and source quality without implying that one aggregate score captures all of them.
- Treat automatic citation evaluators as evidence tools, not ground truth. NLI/judge models, lexical overlap, retrieval scores, or LLM evaluators can help assess support/coverage but have their own errors and require calibration/human review appropriate to risk.
- Allow uncertainty/conflict. When several sources disagree or evidence is insufficient, citations should expose that state rather than selecting citations that create false consensus.
- Do not claim citations eliminate hallucinations/confabulation. Citation-constrained generation can improve verifiability and may improve factual behavior, while models can still fabricate references, misattribute support, omit evidence, or make unsupported synthesis.
- Keep concrete citations/references emitted in runs, source files/records, citation IDs/offset maps, UI rendering formats, resolver implementations, provider-specific citation schemas, evaluator scores, and project-specific citation policies with their applicable evidence/project/catalog owners.
- Use the canonical entity references as research inputs for citation correctness/completeness and source/citation verification boundaries when reader-facing rendering is activated.

## Validation

- Citation presence is not equated with evidential support, source authority, completeness, factual correctness, grounding, or provenance.
- Fabricated source metadata/locations are explicitly disallowed as a citation strategy.
- Claim-level support and compound/multi-source claims can require more precise/multiple citations.
- Mutable source versions and citation resolvability remain explicit.
- Post-hoc citations do not falsely imply process provenance.
- Protected source access is not bypassed by citation rendering.
- Automatic citation scores/evaluators are not treated as authoritative ground truth.
- Concrete citation instances, offsets, provider schemas, UI formats, and project policies remain outside the reusable citation concept.
