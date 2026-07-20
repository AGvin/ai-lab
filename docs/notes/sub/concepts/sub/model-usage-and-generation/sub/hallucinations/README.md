# Hallucinations

A hallucination is unsupported, incorrect, or fabricated model output presented in a plausible form.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Language models generate likely token sequences; they do not automatically verify every statement against a trusted source. Hallucinations can appear as invented facts, citations, API methods, quotations, file paths, numerical results, or claims that overstate uncertain evidence.

## Common causes

- The requested information is absent, ambiguous, or outside the model's reliable knowledge.
- The prompt encourages an answer even when evidence is missing.
- Retrieved context is incomplete, outdated, or contradictory.
- The model is asked for exact identifiers or quotations without access to a source.
- A long context hides the most relevant evidence.

## Mitigation

- Use retrieval, tools, or authoritative data sources for verifiable claims.
- Require citations that can be checked, not merely citation-shaped text.
- Ask the model to distinguish evidence, inference, and uncertainty.
- Validate calculations, URLs, code, and structured values with deterministic systems.
- Evaluate hallucination rates on representative tasks.

## Trade-offs and limitations

Lower temperature may improve consistency but does not guarantee truth. RAG can reduce unsupported answers but may introduce retrieval errors or poisoned evidence. Refusal-heavy policies can lower hallucinations while reducing answer coverage.

## Common mistakes

- Assuming confident wording indicates correctness.
- Treating a valid JSON response as verified data.
- Asking the model to “never hallucinate” without supplying evidence or validation.

## Related concepts

- [Model Usage and Generation](../../)
- [Grounding](../../../retrieval-and-knowledge/sub/grounding/)
- [Citations](../../../retrieval-and-knowledge/sub/citations/)
- [Evals](../../../evaluation-and-operations/sub/evals/)