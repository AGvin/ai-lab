# Documentation Requirements

## Requirements

- Identify PPLX Embed V1 as Perplexity AI's current text-embedding model family exposed by the Perplexity Embeddings API.
- Preserve the family split between standard embeddings for independent texts/queries and contextualized embeddings for chunks that share document context.
- Keep concrete parameter class, dimensions, context length, quantization/output format, pooling behavior, model-card artifacts, and serving characteristics with the concrete member or current first-party service documentation.
- Keep Perplexity Embeddings API pricing, quotas, batching, endpoint behavior, and client SDKs outside intrinsic model-family identity.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The family remains distinct from the hosted Embeddings API service.
- Standard and contextualized variants are not silently conflated.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Embed V1 is Perplexity's Qwen3-derived family of standard and contextualized text embeddings. Four existing members cover the 0.6B and 4B sizes for the two input roles.
- Decision and deployment boundary: Select standard members for independent queries or texts and contextualized members for chunks grouped by document. Validate the matching query/document representation and retrieval metric. Hosted API settings, runtime code and model licenses must be checked at their respective boundaries.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://docs.perplexity.ai/docs/embeddings/quickstart>, <https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b>, <https://huggingface.co/perplexity-ai/pplx-embed-context-v1-4b>.
