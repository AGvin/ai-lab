# Documentation Requirements

## Requirements

- Identify RAGFlow as InfiniFlow's independently released open-source retrieval-augmented generation and agentic data/knowledge retrieval **software engine**, with ingestion, parsing, chunking, embedding, retrieval, reranking, citation, knowledge compilation and orchestration features. It is not a learned model, a generic RAG concept, a hosted model API or a duplicate of LlamaIndex, Haystack or Microsoft GraphRAG.
- Preserve its self-hosted server and source-code application as the canonical software identity. The separately operated `cloud.ragflow.io` service may warrant independent future service intake; do not duplicate the cloud as a second software model or imply that repository Apache-2.0 licensing automatically governs the hosted service.
- Record that the original [v0.27.3 release](https://github.com/infiniflow/ragflow/releases/tag/v0.27.3) was published **2026-10-23** as the latest reviewed non-release-candidate track and its tagged Python manifest declares **0.27.3** and **>=3.13,<3.14**. Its original current v1.0.0-rc3 tag explicitly remains a **release candidate**, even if GitHub's machine-readable `prerelease` flag is false. Do not advertise v1.0 as GA.
- Keep source and component lifecycle sensitive: indexing backends such as Infinity/Elasticsearch, external document parsers, OCR and LLM/embedding providers, Docker/Compose, data connectors, agent workflow engine and feature configuration have independent version, term, hardware and cost boundaries.
- Scope RAGFlow to the primary data-and-retrieval framework category because document/knowledge ingestion and retrieval are its distinguishing job; built-in chat UI and agents are operational features rather than alternate canonical workspace or agent-framework products.
- Differentiate publisher-stated features from reproduced performance: citation grounding, document comprehension, unlimited context, response quality and production-readiness claims have not been independently benchmarked by AI Lab.
- For self-hosting assess deployment isolation, access control, exposed ingestion endpoints, URL fetch/SSRF and prompt injection from untrusted documents, code-execution components, cross-tenant corpus access, PII/document retention, model-provider transfers, token costs, index/database backups and restore, malware-sensitive file parsers and component CVEs. Limit URL destinations and tools and require approval for outbound or state-mutating operations.
- Preserve Apache-2.0 original repository license scope without granting rights to imported documents, third-party models, datasets, cloud services, proprietary connectors or downstream generated output. Check the selected release and all dependencies separately.
- Preserve one inverse `InfiniFlow Inc. produces` / `RAGFlow produced-by` relationship. The first-party operator disclosure identifies InfiniFlow Inc., but current ultimate beneficial ownership/controlling stakes and hidden Russia-linked interests are **not independently cleared**; record provenance review pending rather than inventing affiliations.

## Validation

- RAGFlow remains one self-hosted software node and the direct child of `application-frameworks/data-and-retrieval` with matching index navigation.
- Original source, tagged package/release, Apache-2.0 license and RAGFlow-operated legal-disclosure page support its primary facts; version and provider capacities remain freshness-sensitive.
- The inverse producer relation resolves to the separately materialized `catalog/producers/i/infiniflow-inc`; no existing producer/model/service is double-counted.
