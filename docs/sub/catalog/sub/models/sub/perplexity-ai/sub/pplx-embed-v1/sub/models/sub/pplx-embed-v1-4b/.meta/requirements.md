# Documentation Requirements

## Requirements

- Identify `pplx-embed-v1-4b` as the current 4B-class standard PPLX Embed V1 model for independent texts, queries, and sentences.
- Preserve the current 2560-dimensional, 32K-context identity and supported reduced-output encodings only while first-party Perplexity documentation supports those values.
- Keep hosted pricing, quotas, batching, API response encoding, and similarity/search workflow recommendations freshness-sensitive.

## Validation

- The model remains a standard embedding member, not the contextualized 4B sibling.
- Hosted API behavior is not treated as permanent intrinsic architecture.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Embed V1 4B is the 4B-class standard member of Perplexity's Qwen3-derived V1 embedding family. Its current model card lists 2560 dimensions, a 32K context and MIT licensing.
- Decision and deployment boundary: Encode independent queries or texts with the standard model path. The documented loaders execute repository code, so pin and review the revision. Match unnormalized int8 output to cosine similarity; verify output encoding and the retrieval index together.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-embed-v1-4b>.
