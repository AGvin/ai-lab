# Qwen3-Embedding-0.6B

Qwen3-Embedding-0.6B is an Apache-2.0 text-embedding checkpoint with 32K context and selectable output dimensions from 32 to 1024.

## Decision and Operational Boundaries

- Use the documented instruction-aware query format and compatible document preprocessing; preserve the selected dimension and normalization throughout the index.
- Vectors encode similarity for retrieval/classification/clustering; they do not generate answers or provide standalone reranker scores.
- Changing the embedding model or representation settings can require re-embedding the corpus; protect embedded content with the same access controls as its source documents.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen3-Embedding](../../../../) |

## Primary Sources

- [Official model card or license: Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- [Official repository: QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)
