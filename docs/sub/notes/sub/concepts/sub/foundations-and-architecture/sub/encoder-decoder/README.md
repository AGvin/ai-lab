# Encoder and Decoder Architectures

Legacy residual retained for task-selection, runtime, and comparative guidance that is intentionally outside the canonical encoder-decoder architecture concept owner.

> **Migration note:** General encoder/decoder roles, encoder-decoder composition, Transformer-versus-general architecture boundaries, fixed-bottleneck and cross-attention variants, encoder-only/decoder-only distinctions, autoregressive versus other output mechanisms, and architecture-versus-training-objective boundaries are already preserved in `docs/sub/concepts/sub/models/sub/architectures/sub/encoder-decoder/`. The remaining material below stays here until its exact learning, inference, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task-selection and runtime residual

In practice, encoder-only models are commonly used for classification, retrieval, extraction, embeddings, or reranking; decoder-only models are common for autoregressive generation; and encoder-decoder models are common for transformations such as translation or summarization. These are usage patterns rather than architectural guarantees.

Choose architecture based on the operation rather than model popularity. A small encoder can be a better fit than a large generator for embeddings, reranking, or other representation-heavy tasks, while encoder-decoder models can be effective for controlled source-to-target transformations.

Different architecture roles can use context and cache memory differently, and parameter counts are not directly comparable when model roles differ. A generative decoder can emulate classification but may be slower or less deterministic than a dedicated encoder-oriented solution. Benchmark comparisons therefore need task and runtime context.

These practical consequences remain migration source material until their exact learning, inference/serving, evaluation, or decision-support owner is verified.
