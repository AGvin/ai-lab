# Documentation Requirements

## Requirements

- Identify Microsoft GraphRAG as the independently published `microsoft/graphrag` MIT-licensed Python research software for graph-based retrieval-augmented generation, not the generic graph-RAG architectural technique, a hosted Foundry service, or an official Microsoft-supported product.
- State the important first-party lifecycle warning prominently: the original repository describes itself as **largely in maintenance mode**, not accepting new feature pull requests and focusing on bug/security/dependency fixes. Do not infer product SLAs, new feature roadmaps, security certification or production support from an upstream version number.
- Use the original source GitHub v3.3.0 release (published 2026-10-08, non-prerelease), the tagged `packages/graphrag/pyproject.toml` manifest with `graphrag` package version 3.3.0 and Python **>=3.11,<3.14**, and the original MIT license as bounded lifecycle and package evidence. The monorepo root `pyproject.toml` has a private workspace version `0.0.0`, which is **not** the published library version.
- Describe original indexing and graph/community construction over text corpora, graph-aware retrieval and query workflows using configured LLMs; distinguish the repository's demonstration/research code from independent benchmarks, managed retrieval services, general graph databases and unrelated RAG frameworks such as Haystack or LlamaIndex.
- Preserve the publisher's data and rights boundary: source MIT does not authorize private-document transfer, third-party copyrighted corpora, embedding/LLM usage, paid API endpoints, deployment secrets or data residency.
- Indexing can be expensive and model-generated graphs/answers may hallucinate, propagate source bias or suffer corpus/prompt injection. Start with small representative datasets, evaluate provenance, accuracy and domain-specific prompts, isolate datasets and set inference/token/cost budgets. Do not treat claimed research evaluation or generated answers as verified AI Lab results.
- Call out breaking configuration and migration behavior. The upstream README warns that `graphrag init --root [path] --force` overwrites generated configuration and prompts; back up and compare old configuration before running it. Use the documented migration path for major versions rather than assuming re-indexing is free or safe.
- Attribute original software production to existing Microsoft, with the reciprocal `produces` / `produced-by` edge. Preserve Microsoft Research authorship, the lack of officially supported Microsoft offering status, and distinction from existing Microsoft Azure and Foundry products.

## Validation

- Exactly one software canonical entity represents the Microsoft GraphRAG Python package, in Data and Retrieval Frameworks, not a generic RAG concept or new hosted service.
- Current repository README explicitly supports the maintenance/no-official-support caveat; tagged package metadata supplies correct version and Python range.
- Parent data-and-retrieval index lists this direct child exactly once, and Microsoft producer inverse resolves.
- No new model, producer, hosted-service or final whole-catalog validation credit follows merely from this source-backed software record.
