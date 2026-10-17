# Documentation Requirements

## Requirements

- Identify PPLX Embed V2 Late 0.6B as an independently released October 2026 Perplexity multimodal late-interaction retrieval model with 0.6B total, approximately 340M active parameters.
- Preserve the 128-dimensional vector-per-token ColBERT/MaxSim retrieval design and its support for text, images, and visual documents; do not represent it as ordinary pooled text embeddings.
- Preserve cross-size querying of an index built with the 9B sibling only as described by the compatible family model cards; do not infer identical quality or latency.
- Separate exact model weights, license, precision, Qwen3.5-derived architecture and required inference/indexing libraries from mutable Perplexity API deployment behavior.
- Treat vendor benchmark results and claims about ViDoRe/document retrieval as model-card evidence, not independent AI Lab comparative test results.
- Keep V1 standalone and contextualized embeddings, V2 Context preview and this exact V2 Late checkpoint identity separate.

## Validation

- The concrete official Hugging Face artifact/model card resolves and identifies the exact model.
- `member-of` and family `has-member` are reciprocal.
- The cross-size compatible embedding space does not imply that scores and speed are interchangeable.
