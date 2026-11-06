# Documentation Requirements

## Requirements

- Identify `pplx-embed-context-v1-0.6b` as the current 0.6B-class contextualized PPLX Embed V1 model for document chunks that share context.
- Preserve the current 1024-dimensional, 32K-context identity and supported reduced-output encodings only while first-party Perplexity documentation supports those values.
- Keep hosted pricing, batching/context grouping, quotas, API response encoding, and retrieval workflow recommendations freshness-sensitive.

## Validation

- The model remains the contextualized 0.6B member and is not conflated with standard embeddings.
- Hosted API behavior is not treated as permanent intrinsic architecture.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Embed Context V1 0.6B is the 0.6B-class contextualized member of Perplexity's Qwen3-derived V1 embedding family. Its current model card lists 1024 dimensions, a 32K context and MIT licensing.
- Decision and deployment boundary: Preserve document boundaries when grouping chunks for contextualized encoding. The documented loaders execute repository code, so pin and review the revision. Match unnormalized int8 output to cosine similarity; verify output encoding and the retrieval index together.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-embed-context-v1-0.6b>.
