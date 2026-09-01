# Transformers

Legacy residual retained for Transformer runtime/resource and model-selection guidance that is intentionally outside the canonical architecture concept owner.

> **Migration note:** Transformer identity, attention-centered architecture structure, encoder/decoder family variants, positional-information requirements, architecture-versus-objective boundaries, scoped attention complexity, and non-guarantees around factuality, interpretability, memory, and long-context quality are already preserved in `docs/sub/concepts/sub/models/sub/architectures/sub/transformers/`. The remaining material below stays here until its exact inference, AI-engineering, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Runtime and model-selection residual

Runtime requirements can vary materially with layer count, hidden dimensions, attention configuration, vocabulary size, context length, architecture variant, and runtime implementation. Longer contexts can substantially increase computation and KV-cache memory for architectures and runtimes that use such caching.

When comparing or selecting models, parameter counts alone can obscure architectural differences and should not be treated as a complete proxy for runtime cost or deployment fit. These practical consequences remain migration source material until their exact inference/serving or decision-support owner is verified.
