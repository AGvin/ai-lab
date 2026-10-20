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

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Embed V2 Late 9B is the larger MIT-licensed multimodal retrieval artifact, with about 7.4 billion active parameters and a 128-dimensional vector for each token.
- Decision and deployment boundary: Use multivector encoding and MaxSim scoring, with the exact runtime and token-marker conventions in its model card. Keep text and image batches separate. Its shared space with the 0.6B member does not establish equal latency, memory use or retrieval quality.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-embed-v2-late-9b>.
