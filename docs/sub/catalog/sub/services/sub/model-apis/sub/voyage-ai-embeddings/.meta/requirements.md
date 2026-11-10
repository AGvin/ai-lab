# Documentation Requirements

## Requirements

- Identify the provider-hosted Voyage embeddings service rather than a separately downloadable model, local Python/TypeScript SDK or vector database.
- Ground the main interface in `POST https://api.voyageai.com/v1/embeddings` with JSON `input`, `model` and optional `input_type`, authenticated by `Authorization: Bearer <VOYAGE_API_KEY>`.
- For text retrieval, document that `input_type=query` and `input_type=document` can alter embedding prompts to suit query/document roles. Inputs without a type are supported; never assert identical behavior or guarantee cross-model vector dimensions.
- Model IDs, context/tokens, quotas, batch sizes, billing, retention and support change. Read the current official API reference for the chosen model; avoid copying one snapshot's mutable numeric limits into timeless claims.
- Warn against disclosing API keys, sending copyrighted/private texts without authorization, confusing embedding representations with an automatic search index, or treating a commercial endpoint as an Apache-licensed tool.
- No authenticated request, embedding generation, accuracy evaluation, cross-region data audit or whole-catalog clean pass is claimed.

## Validation

- Verify the provider-owned API/product boundary and current documentation sources.
- Maintain a single catalog identity with the correct category link; never equate hosted terms with unrelated SDK or model licenses.
- Do not credit unperformed runtime, whole-site or clean-pass checks.

## Follow-up original-source review — 2026-11-06 (no additional gate)

- Voyage's managed text-embedding endpoint is POST https://api.voyageai.com/v1/embeddings with input, a specific model and optional input_type=query/document; official documentation distinguishes retrieval query/document behavior and model-specific dimensions, context and input data options.
- The hosted embeddings API is not a vector database or trained-model redistribution license. Voyage 4-series compatibility and its separate published open-weight voyage-4-nano identity must not become claims that all model generations share identical vector spaces, licenses, input limits, pricing or retention guarantees.
- Verified first-party source 1: https://docs.voyageai.com/reference/embeddings-api
- Verified first-party source 2: https://docs.voyageai.com/docs/embeddings
- Scope: only current provider-documented hosted service identity and endpoint/version boundaries. No new metadata or entity, reader-repair credit, independent run, complete freshness/legal/security clearance, root-wide schema/cache/CI/render, clean pass or final delivery.
- Existing source gate was already accepted in Enrichment Batch 016; this follow-up adds **zero** identity, metadata or scoped-source acceptance credit. Avoid duplicate counting.
