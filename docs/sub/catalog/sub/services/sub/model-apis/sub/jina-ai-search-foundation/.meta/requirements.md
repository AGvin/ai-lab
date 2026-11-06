# Documentation Requirements

## Requirements

- Identify **Jina Search Foundation API** as the managed service behind the Jina model-access domain `https://api.jina.ai`, not a separately trained model, local vector index, general cloud compute system, or Elastic's separate Inference Service.
- Distinguish the official [Jina API reference](https://docs.jina.ai/) model host (`api.jina.ai`) from its independent Reader (`r.jina.ai`) and Search (`s.jina.ai`) interfaces. Document `POST /v1/embeddings`, `POST /v1/rerank` and `GET /v1/models` as first-party supported model operations; other document/OCR and batch functions are version-sensitive.
- Authenticate model API requests using `Authorization: Bearer <JINA_API_KEY>` and protect API keys and provider quotas. Reader has limited unauthenticated access and Search requires a key; do not imply every host has identical authentication or limits.
- Preserve the historical producer relationship and its October 9, 2025 acquisition by Elastic without mislabeling Jina model API and Elastic-hosted model APIs as one product. The Jina brand still owns the provider relationship for this frozen identity's source.
- Model names, embedding modalities, availability, quotas, regional routing, costs and data processing terms change; verify per-endpoint reference and customer agreement. The `docs.jina.ai` site is an evolving published developer source, not an immutable revision.
- User inputs, fetched web content and embeddings may include private information, third-party copyrights or regulated data. Restrict authorization, retention and downstream dataset rights, and check [post-acquisition legal terms](https://jina.ai/legal/) before sending protected content.
- Require exactly one reciprocal `produced-by` / `produces` relation with `catalog/producers/j/jina-ai`; index a single Model APIs node. Avoid promising a runtime test, current-rate audit, source-weight license, full CI or whole-catalog clean pass.

## Validation

- Current Jina API reference substantiates three host categories and authentication differences.
- Canonical relation resolves both ways and new internal links/index point to a materialized README.

## Scoped original-source qualification — 2026-11-06

- Jina's first-party API reference distinguishes three service hosts: api.jina.ai for Search Foundation embeddings/reranking and model access, r.jina.ai for Reader, and s.jina.ai for Search. The Search Foundation API supports embeddings, reranking and model inventory, with modality and option support depending on the chosen trained model.
- Jina's bearer-key requirements are host-specific: the Reader has restricted unauthenticated use while Search requires authentication. The Jina-branded API remains a hosted provider service, not an Elastic inference deployment, generic vector database or automatically redistributable model.
- Verified first-party source 1: https://docs.jina.ai/
- Verified first-party source 2: https://jina.ai/
- Scope: only current provider-documented hosted service identity and endpoint/version boundaries. No new metadata or entity, reader-repair credit, independent run, complete freshness/legal/security clearance, root-wide schema/cache/CI/render, clean pass or final delivery.
