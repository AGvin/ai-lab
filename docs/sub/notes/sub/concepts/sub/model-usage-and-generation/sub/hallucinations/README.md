# Hallucinations

Legacy residual retained for diagnostic, mitigation, evaluation, evidence-handling, and coverage trade-off guidance that are intentionally outside the canonical Hallucinations concept owner.

> **Migration note:** Hallucination/confabulation identity and terminology, factuality-versus-source-faithfulness boundaries, differentiation from retrieval/data/application failures and intentional non-factual generation, multi-causal boundaries, affected output types, and non-guarantees from confidence, low temperature, schema validity, RAG, citations, or visible reasoning are already preserved in `docs/sub/concepts/sub/models/sub/behavior-and-failure-modes/sub/hallucinations/`. The remaining material below stays here until its exact trustworthy-AI, evaluation, retrieval, application-engineering, evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Diagnostic residual

When unsupported or incorrect generated content appears, investigate the complete evidence and system path rather than attributing the observation automatically to one model cause. Relevant factors can include missing or ambiguous task evidence, stale or contradictory retrieval, unavailable authoritative sources, exact-string or identifier requests without source access, context-selection failures, prompt pressure to answer despite uncertainty, decoding configuration, and application-side data handling.

Separate model-generation failure from retrieval failure, bad source data, deterministic computation bugs, or application corruption before selecting a mitigation.

## Mitigation residual

Useful mitigation practices include:

- use retrieval, tools, or authoritative data sources when the task requires externally verifiable claims;
- require citations or evidence references that can actually be checked instead of accepting citation-shaped text;
- distinguish supplied evidence, inference, and uncertainty in outputs where that distinction matters;
- validate calculations, URLs, identifiers, code/API claims, and structured values with appropriate deterministic or authoritative systems;
- design the application to abstain, escalate, or ask for missing evidence when unsupported guessing would create unacceptable failure cost.

These are risk-reduction techniques, not guarantees that hallucinations are eliminated.

## Evaluation and trade-off residual

Measure hallucination or faithfulness failure rates on representative tasks under the actual retrieval, prompting, tool, and model configuration rather than inferring reliability from a single example or generic benchmark.

Mitigations can introduce their own failure modes: retrieval can surface incorrect or poisoned evidence, stricter refusal/abstention policies can reduce answer coverage, and more validation can add latency or operational cost. Evaluate the complete quality-versus-coverage-versus-cost trade-off for the target workflow.

These diagnostic, mitigation, and evaluation practices remain migration source material until their exact trustworthy-AI, evaluation, retrieval, engineering, evidence, or decision-support owners are verified.
