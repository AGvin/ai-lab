# RAGFlow

[RAGFlow](https://github.com/infiniflow/ragflow) is an open-source Apache-2.0 retrieval-augmented generation (RAG) engine and application framework. It connects document parsing and ingestion to indexing, knowledge organization, retrieval, citations and agent workflows. Its canonical identity here is **self-hosted software**, not the distinct provider-operated RAGFlow Cloud service, a model family or the generic RAG design pattern.

## Lifecycle and operating boundary

The original [v0.27.3 release](https://github.com/infiniflow/ragflow/releases/tag/v0.27.3) was published on **2026-10-23**; its tagged package manifest declares Python **>=3.13,<3.14** for the application. The newer `v1.0.0-rc3` is still a **release candidate**, not a verified general-availability 1.0. Version, Docker/Compose, search backend and model-provider requirements vary by release; inspect the tagged deployment instructions rather than assuming the latest development branch matches a production image.

RAGFlow provides document parsing, chunking, embedding and reranking, knowledge compilation, citation-oriented answers and agentic retrieval. The local stack may use databases, search engines, external OCR/parsers, hosted or local models, and connectors. Publisher performance and grounding statements are **not independent AI Lab evaluation**. A cloud offering at [cloud.ragflow.io](https://cloud.ragflow.io/) has separate service operation, terms and security responsibilities.

## Risk and provenance

Untrusted pages and uploaded documents can introduce prompt injection, privacy exposure, parser and URL-fetch hazards, or cross-corpus leakage. Audit access rules, outbound URL limits, model-provider data transfers, agent/code-execution privileges, credentials, rate limits, component vulnerabilities, logging, backup/restore and indexing/token cost before use. Apache-2.0 source rights do not automatically clear third-party materials or hosted services.

The first-party [operator disclosure](https://ragflow.io/about-service) identifies **InfiniFlow Inc.**; it does not establish a complete beneficial-ownership or control audit. Source-driven ownership review remains pending. Neither missing ownership data nor an author's name proves Russian connections.

## Relations

- Produced by: [InfiniFlow Inc.](../../../../../../../producers/sub/i/sub/infiniflow-inc/)

## Official resources

- [Original source and self-hosting](https://github.com/infiniflow/ragflow)
- [RAGFlow documentation](https://ragflow.io/docs/dev/)
- [v0.27.3 release](https://github.com/infiniflow/ragflow/releases/tag/v0.27.3)
- [Tagged application manifest](https://github.com/infiniflow/ragflow/blob/v0.27.3/pyproject.toml)
- [Repository license](https://github.com/infiniflow/ragflow/blob/v0.27.3/LICENSE)
- [First-party operator disclosure](https://ragflow.io/about-service)
