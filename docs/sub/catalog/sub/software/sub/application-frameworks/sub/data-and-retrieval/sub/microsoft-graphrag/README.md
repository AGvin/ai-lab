# Microsoft GraphRAG

**Microsoft GraphRAG** is the [open-source MIT-licensed Python research toolkit](https://github.com/microsoft/graphrag) for building graph-enhanced retrieval workflows from text corpora. It indexes documents into entities and relationships, constructs graph/community context, and supports LLM-backed discovery and question answering. This is a **specific Microsoft Research software package**, not the broader graph-RAG design pattern or a Microsoft Foundry cloud service.

## Lifecycle and deployment

**Maintenance-mode warning:** the original publisher states that GraphRAG is largely in **maintenance mode**; it is not accepting new feature contributions, and its code is a research demonstration **rather than an officially supported Microsoft product**. It may receive fixes and dependency/security updates, but an upstream release is not a production SLA.

[Release v3.3.0](https://github.com/microsoft/graphrag/releases/tag/v3.3.0) was published on **2026-10-08** as a non-prerelease; its packaged `graphrag` manifest requires Python **>=3.11,<3.14**. The monorepo root's private `0.0.0` workspace version is not the package version. Pin versions, model provider, data stores and configuration. Estimate indexing/token charges from a small representative corpus before full processing.

## Risk and operating boundaries

Graph extraction and retrieval depend on configured model inference, prompt quality and corpus quality. Private-data transfer, injection, hallucinations, source provenance and evaluation must be addressed separately from source-code licensing. Human review is necessary for decision-relevant findings. The upstream README warns that `graphrag init --root [path] --force` overwrites configuration and prompts: back them up and review migration instructions before invoking it. No AI Lab runtime or cost benchmark has been performed.

## Relations

- Produced by: [Microsoft](../../../../../producers/sub/m/sub/microsoft/)

## Official resources

- [Microsoft GraphRAG repository and maintenance warning](https://github.com/microsoft/graphrag)
- [Documentation and getting started](https://microsoft.github.io/graphrag/)
- [v3.3.0 release](https://github.com/microsoft/graphrag/releases/tag/v3.3.0)
- [Published Python package manifest](https://github.com/microsoft/graphrag/blob/v3.3.0/packages/graphrag/pyproject.toml)
- [Responsible AI FAQ](https://github.com/microsoft/graphrag/blob/main/RAI_TRANSPARENCY.md)
