# Documentation Requirements

## Requirements

- Use the reader-facing title `AI Information Integrity` and introduce `information integrity` as the shorter general term.
- Define AI information integrity as the trustworthy handling of information used, transformed, retrieved, inferred, attributed, or produced by AI systems so claims and decisions preserve appropriate source identity, provenance, meaning, context, support, freshness, uncertainty, and transformation history for the intended use.
- Distinguish this concept from the narrower information-security use of `integrity` meaning protection against unauthorized modification. Security integrity is important, but AI information integrity also concerns provenance loss, unsupported synthesis, stale evidence, source conflicts, misleading transformations, fabricated attribution, and incorrect interpretation even when no attacker modified the bits.
- Distinguish information integrity from factual truth alone. A statement can be factually correct by coincidence while lacking traceable support/provenance, and a statement can faithfully reproduce a source that is itself wrong, outdated, manipulated, or outside its scope.
- Distinguish source authenticity from source reliability and claim support. Authenticating that a document/record came from a named source does not prove that source is authoritative for the claim, current, unbiased, complete, or correctly interpreted.
- Treat information lineage as end-to-end where required: original observations/documents/records, ingestion, parsing/OCR, chunking, extraction, summarization, graph/index construction, embeddings, retrieval, tool/database results, model synthesis, post-processing, and citation formatting can each alter or lose relevant context.
- Preserve source identity/version/time boundaries when information is mutable. A URL, document title, database record, API response, policy, software documentation, price, inventory value, or organizational fact can change while retaining a similar name.
- Explain provenance as evidence about origin/history/transformation rather than proof of truth. Provenance can make a claim auditable and help assess authority/conflicts while still tracing back to a bad or malicious source.
- Distinguish direct evidence from derived/inferred/synthesized claims. A source can state a fact directly, several sources can jointly support a conclusion, or a tool/calculation/model can derive a result; the system should preserve which support path applies rather than representing all outputs as direct quotations/facts.
- Treat semantic scope and qualifiers as integrity-relevant. Negation, modality, uncertainty, units, time ranges, jurisdiction, entity identity, populations, conditions, exceptions, and source assumptions can be lost during summarization/retrieval and materially change a claim's meaning.
- Explain source conflict as a valid information state. When credible sources disagree, differ by version/date/scope, or cannot be reconciled, the system should preserve/report the conflict or select according to an explicit authority policy rather than synthesizing false consensus.
- Explain insufficiency as a valid outcome. If available evidence does not support a requested conclusion with the required confidence/specificity, the system should be able to abstain, qualify, request more evidence, or surface uncertainty instead of fabricating support.
- Treat retrieval quality and information integrity as related but distinct. A retriever can return topically relevant material that does not entail the generated claim, and a high-recall retrieval set can contain stale, contradictory, poisoned, or low-authority sources.
- Treat transformations as potentially lossy. OCR, extraction, chunking, table parsing, summarization, translation, normalization, deduplication, entity resolution, graph construction, and generative rewriting can introduce errors or detach evidence from context/provenance.
- Explain that generated intermediates are not automatically authoritative evidence. Model-generated summaries, synthetic labels, extracted graph edges, generated queries, or self-critiques should preserve their generated/derived status and source dependencies.
- Treat tool/database/calculation outputs as evidence according to their contract. Deterministic calculation can strongly support a computed value when inputs and units are correct, while API/database results still depend on source freshness, permissions, schema interpretation, and identity resolution.
- Explain evidence granularity. Whole-document relevance can be insufficient for a sentence-level factual claim; evidence should identify the smallest practical supporting passage, field, record, calculation, timestamp, or other unit when verification requirements justify that precision.
- Explain evidence completeness at the appropriate claim level. Supporting one clause does not automatically support a conjunction, causal explanation, comparative claim, recommendation, or synthesized conclusion containing additional assertions.
- Distinguish content provenance from process provenance. Knowing where source content originated differs from knowing which retrieved/tool/model artifacts actually influenced a particular generated output; systems may need one or both depending on audit requirements.
- Distinguish information integrity from censorship/content moderation. Integrity concerns trustworthy origin/support/context and faithful interpretation; whether content is allowed, harmful, or policy-compliant is a separate safety/governance question.
- Explain adversarial information risks without inferring their missing child concepts. Poisoned retrieval content, prompt-like instructions inside data, deceptive provenance, fabricated citations, altered records, and malicious sources can undermine integrity, while detailed retrieval-poisoning/prompt-injection/provenance concepts remain separate architecture decisions.
- Keep `grounding/` and `citations/` as the currently selected direct children. Grounding owns claim-to-evidence support; citations own explicit reference/attribution mechanics and quality. Do not collapse them into the parent or into each other.
- Do not infer a `provenance/` child merely because provenance is a core cross-cutting property; the legacy provenance concept remains architecture-gapped until separately selected.
- Keep concrete source documents/records, trust/authority lists, run-level retrieval evidence, generated citations, source rankings, incident findings, project-specific evidence policies, and compliance requirements with their applicable evidence/project/governance/catalog owners.
- Render direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Use the canonical NIST entity reference as a research input for lifecycle information-integrity, grounded-data, citation/source-verification, and provenance boundaries when reader-facing rendering is activated.

## Validation

- AI information integrity is not reduced to cybersecurity bit-integrity, factuality, source authenticity, provenance, grounding, or citations alone.
- Provenance/authenticity is not treated as proof that a claim is true, current, authoritative, or correctly interpreted.
- Retrieval relevance is not treated as claim-level evidential support.
- Direct, derived, synthesized, conflicting, insufficient, and generated information states remain distinguishable where relevant.
- Lossy transformations and mutable source/version boundaries are represented as integrity risks.
- `grounding/` and `citations/` remain distinct selected descendants.
- Unselected provenance/security/injection/poisoning leaves are not inferred or materialized.
- Concrete evidence, trust policies, run traces, source records, and governance requirements remain outside the reusable domain owner.
