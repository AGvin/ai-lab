# Qwen3-Reranker-8B

Qwen3-Reranker-8B is an Apache-2.0 text reranker with 32K context for instruction/query/document relevance scoring.

## Decision and Operational Boundaries

- Score supplied candidates using the documented yes/no token scoring contract; do not treat it as a vector embedding or a calibrated probability of factual truth.
- Allocate context to the instruction, query, and candidate together and document truncation; runtime generation APIs alone do not ensure correct reranker scoring.
- Restrict candidate inputs to authorized material and enforce result access independently of relevance.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-Reranker](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-Reranker-8B](https://huggingface.co/Qwen/Qwen3-Reranker-8B)
- [Official repository: QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)
