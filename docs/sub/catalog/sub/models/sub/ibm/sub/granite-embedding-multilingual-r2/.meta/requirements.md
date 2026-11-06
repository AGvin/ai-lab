# Documentation Requirements

## Identity and provenance

- Identify Granite Embedding Multilingual R2 as IBM's April 2026 multilingual embedding family with distinct 311M and 97M checkpoints.
- Preserve the source-backed lineage from the 97M model to the 311M model: the 97M card documents layer pruning and vocabulary selection from 311M.
- Keep ONNX, OpenVINO, provider endpoints and other conversions as artifacts or delivery routes rather than peer learned-model identities.

## Operational decision boundaries

- Both cards document sequence lengths up to 32,768 tokens and distinguish broad multilingual pretraining coverage from enhanced support for 52 listed languages plus programming code.
- The 311M model emits 768-dimensional embeddings and supports Matryoshka outputs at 768, 512, 384, 256 and 128 dimensions; the 97M model emits 384-dimensional embeddings and does not inherit that Matryoshka contract.
- Both reviewed weights state Apache 2.0. Retrieval quality, truncation, pooling, vector normalization and runtime performance require task-specific validation.

## Validation

- Family membership resolves exactly to the 97M and 311M nodes.
- The 97M derived-from relation and 311M has-derivative inverse resolve reciprocally.
- Producer provenance resolves to IBM.
- This assessment grants no runtime, benchmark-reproduction, cache or final-render credit.
