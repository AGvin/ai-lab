# Documentation Requirements

## Requirements

- Identify PPLX Embed V2 Late 9B as an independently released October 2026 Perplexity multimodal late-interaction retrieval model with 9B-class total and approximately 7.4B active parameters.
- Preserve the 128-dimensional vector-per-token ColBERT/MaxSim retrieval design, not ordinary pooled dense embeddings, and its text/image/visual-document support.
- This higher-capacity model shares an embedding space with the 0.6B sibling; that cross-size compatibility does not establish equivalent quality, memory use or speed.
- Distinguish the model's exact weights, license, precision, Qwen3.5-derived architecture and indexing dependencies from mutable hosted Perplexity API terms.
- Treat vendor benchmark scores and ViDoRe results as model-card evidence rather than independent AI Lab tests.
- Keep PPLX Embed V1 standard/contextualized models, V2 Context preview and this exact V2 Late artifact distinct.

## Validation

- The official artifact/model card identifies this exact checkpoint.
- `member-of` and family `has-member` are reciprocal.
- Cross-size interoperability is not presented as benchmark equivalence.
