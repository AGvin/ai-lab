# Documentation Requirements

## Requirements

- Use the reader-facing title `Grounding`.
- Define grounding as the relationship/process by which generated or derived claims are constrained by and traceably supported by evidence available to the system for the current task, such as retrieved passages, structured records, authoritative APIs, tool results, calculations, code execution, sensors, or other verified inputs.
- Require claim-level support rather than context presence. Putting a document, web page, database result, or tool output into the model context does not make every generated statement grounded; the evidence must actually support the specific claim, value, inference, or conclusion being presented.
- Distinguish grounding from factual correctness. A claim can be grounded in a source that is wrong, outdated, malicious, incomplete, or outside scope; conversely, a model can produce a factually correct statement from parametric knowledge without a traceable grounding relation to the evidence available in the current interaction.
- Distinguish grounding from citations. Grounding is the support relation; `citations/` owns the explicit reference/attribution mechanism used to expose or identify supporting sources. A system can be internally grounded without showing citations, and a citation can exist without actually supporting the attached claim.
- Distinguish grounding from retrieval. Retrieval is an evidence-acquisition mechanism; grounding additionally requires the generation/derivation to stay within what the retrieved or tool-produced evidence supports.
- Distinguish grounding from source authority. A source can support what it explicitly says yet still be a poor authority for the user's question. Grounding evaluation should therefore be complemented by source-quality/freshness/authority checks when the task requires them.
- Distinguish grounding from provenance. Provenance records where evidence came from and how it changed; grounding records whether that evidence supports a particular output claim. Provenance helps verify grounding but does not imply it automatically.
- Support multiple evidence forms. Text passages are common but grounding can rely on database rows/fields, structured records, source code, executable tests, calculator outputs, query results, sensor measurements, images/audio/video evidence, logs, specifications, or combinations.
- Explain direct versus derived grounding. A claim may be directly stated by a source, computed deterministically from sourced values, inferred from several sources, or synthesized across evidence. The support type and intermediate assumptions should remain distinguishable when verification matters.
- For calculations and tool execution, require grounding of both the operation and its inputs. A correct arithmetic procedure applied to a wrong unit, stale record, or misidentified entity does not produce a well-grounded result.
- For multi-source synthesis, require that the combined conclusion follows from the cited/supplied evidence and does not introduce unsupported bridge assumptions. Several individually supported facts do not automatically entail a causal, comparative, or policy conclusion.
- Treat contradiction/conflict explicitly. When available evidence conflicts, grounding should not mean selecting whichever source supports the generated answer; the system should surface the disagreement or apply a documented authority/version policy.
- Treat insufficient evidence as an allowed outcome. A grounded system should be able to state that the evidence is insufficient, qualify a claim, ask for additional data, or abstain rather than fill gaps with plausible unsupported detail.
- Preserve evidence scope and qualifiers such as entity identity, units, dates, jurisdiction, population, version, modality, uncertainty, exceptions, and conditions. A passage can look relevant while failing to support a claim after these qualifiers are considered.
- Explain granularity. Whole-document/topic relevance is weaker than support from a specific passage, field, record, result, timestamp, or calculation. Use the smallest practical evidence unit needed by the verification/risk level without requiring one universal granularity.
- Explain completeness. A response can contain some grounded claims and some unsupported claims; grounding should be assessed at the relevant claim units rather than assigned as a binary property to an entire answer solely because one source was used.
- Explain entailment/support versus contradiction and mere relevance. Retrieved content can be about the same topic yet neither support nor contradict the claim; relevance alone is not grounding.
- Explain that summaries and generated intermediates can become evidence only with clear status. A model-generated summary is a derived artifact whose own grounding depends on its underlying sources; using it downstream must not erase that dependency.
- Explain RAG grounding carefully. RAG provides external context but does not guarantee that generation follows it, that retrieval found the correct evidence, or that the indexed corpus is authoritative/current. Grounding must be evaluated beyond `retrieval succeeded`.
- Explain database/API grounding carefully. Structured sources can reduce ambiguity but still require correct query semantics, permissions, field interpretation, version/time scope, entity resolution, and freshness.
- Explain code/tool grounding as execution evidence. Tests, compilers, calculators, validators, and deterministic tools can provide strong evidence for specific properties, but their result is scoped to the inputs, environment, tool correctness, and execution conditions.
- Explain grounding of recommendations separately from grounding of facts. Evidence can establish product capabilities, constraints, or measured outcomes while a recommendation additionally depends on user goals, trade-offs, preferences, risk tolerance, and decision criteria.
- Do not equate a model's detailed rationale with grounding. Reasoning text can contain unsupported intermediate assertions; grounding requires external/available evidence support where the claim depends on such evidence.
- Explain temporal grounding. Current-state questions require evidence current enough for the requested time; a historically correct source cannot ground a claim about `now` without evidence that the state persists.
- Explain security/trust boundaries. Untrusted retrieved content can supply facts/evidence while also containing malicious instruction-like text; evidence grounding must not grant that content authority to change system instructions or permissions.
- Require critical-value validation outside generative interpretation where feasible. Exact financial totals, identifiers, permissions, legal/policy requirements, transactions, safety-critical values, or other consequential data may warrant deterministic parsing/query/validation in addition to model-based synthesis.
- Keep concrete retrieved passages, run-level evidence maps, tool outputs, grounding scores, evaluator prompts/models, source authority lists, thresholds, and project-specific evidence policies with their applicable evidence/project owners.
- Use the canonical entity references as research inputs for grounded-data and claim-to-evidence support boundaries when reader-facing rendering is activated.

## Validation

- Context/retrieval/citation presence is not treated as proof that a claim is grounded.
- Grounding and factual correctness/source authority/provenance/citation formatting remain distinct dimensions.
- Direct, computed, inferred, and synthesized claims can preserve different support paths.
- Relevance is distinguished from entailment/support, and source conflicts/insufficient evidence remain valid outcomes.
- RAG/tool/database access does not automatically guarantee grounding.
- Concrete evidence artifacts, scores, thresholds, and project trust policies remain outside the reusable grounding concept.
