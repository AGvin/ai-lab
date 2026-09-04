# Documentation Requirements

## Requirements

- Use the reader-facing title `Generation Controls`.
- Present generation controls as mechanisms that influence or restrict how a generative model selects and emits outputs at inference time.
- Distinguish probabilistic sampling controls from structural constraints and output-format contracts. Temperature/top-p/top-k alter candidate selection probabilities; constrained generation restricts the allowed output space; structured output describes a machine-readable result contract that may be implemented through several mechanisms.
- Keep generation controls separate from prompting, model training/adaptation, tokenizer design, architecture, and post-generation business validation even when those concerns interact operationally.
- Explain that control names, availability, defaults, ordering, and exact mathematical behavior can vary by model, runtime, or provider; do not treat one API surface as the universal contract.
- Explain that generation controls can change diversity, determinism, syntax compliance, or search behavior but do not by themselves guarantee factual correctness, safety, task quality, or semantic validity.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep provider-specific parameter ranges, default values, pricing/performance trade-offs, benchmark-tuned settings, and application recipes with their applicable catalog, evidence, learning, or decision owners.

## Validation

- Sampling, constrained decoding, and structured-output contracts are not treated as interchangeable mechanisms.
- The page does not claim one provider's parameter names/defaults are universal.
- Generation controls are not presented as factuality, safety, or semantic-validation guarantees.
- Direct-child navigation contains only currently materialized direct children.
