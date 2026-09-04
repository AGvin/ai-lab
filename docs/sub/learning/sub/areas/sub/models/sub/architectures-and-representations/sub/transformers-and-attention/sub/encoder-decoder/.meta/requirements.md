# Documentation Requirements

## Requirements

- Teach encoder and decoder architectures by the role each component plays in transforming inputs into internal representations and/or generating outputs; use the canonical Encoder-Decoder concept for stable architecture semantics.
- Explain encoder-only, decoder-only, and encoder-decoder arrangements without assuming that the terms belong only to Transformers; recurrent, convolutional, attention-based, and hybrid architectures can use related role separation.
- Present common practical task associations as heuristics rather than guarantees: encoder-oriented models are often effective for classification, retrieval, extraction, embeddings, and reranking; decoder-oriented models are common for autoregressive generation; encoder-decoder systems are common for source-to-target transformation such as translation or summarization.
- Teach architecture selection from the operation and evidence rather than popularity. A smaller representation-oriented encoder can be more appropriate than a large generator for embeddings/reranking/classification, while an encoder-decoder model can be a natural fit when explicit source conditioning and target generation are central.
- Explain that a generative decoder can emulate some classification/extraction tasks, but the route can differ in determinism, latency, output validation, resource demand, and accepted-result quality from a dedicated encoder-oriented model. Treat this as a comparison to evaluate, not a universal ranking.
- Distinguish encoder-decoder architectural roles from autoregressive/non-autoregressive output mechanisms and from training objectives. Architecture role does not uniquely determine the learning objective or task.
- Explain that architecture roles can change runtime behavior: context processing, cross-attention, output length, KV/cache state, generation loops, batching, and runtime implementation can alter compute/memory/latency, so parameter counts are not directly comparable across roles without workload context.
- Require benchmark or model-selection comparisons to use task/runtime context and exact evaluated artifacts rather than assuming that higher parameter count or a more popular generative family is automatically better.
- Keep concrete model recommendations, benchmark scores, current runtime compatibility, and hardware-fit conclusions with catalog/evidence/decision owners.

## Validation

- Encoder/decoder roles are not presented as Transformer-only concepts.
- Task associations are labeled as common patterns rather than architecture guarantees.
- Architecture selection is tied to operation, runtime, and accepted-result evidence rather than popularity or parameter count.
- Comparative claims remain evaluation/decision-owned when they depend on concrete models or measurements.
