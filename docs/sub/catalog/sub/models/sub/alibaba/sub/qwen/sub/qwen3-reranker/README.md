# Qwen3-Reranker

Released query-document relevance-scoring checkpoints at 0.6B, 4B, and 8B, distinct from embedding models.

## Decision and Operational Boundaries

- Preserve the exact member's input/output and license contract; do not turn toolkit options, quantizations, or hosted aliases into peer model identities.
- Scores order supplied candidates; they are not embeddings, factual confidence, or a replacement for first-stage retrieval.
- Apply access control before exposing candidates to the model and before returning results.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3-Reranker-0.6B](./sub/models/sub/qwen3-reranker-0-6b/) |
| Includes | [Qwen3-Reranker-4B](./sub/models/sub/qwen3-reranker-4b/) |
| Includes | [Qwen3-Reranker-8B](./sub/models/sub/qwen3-reranker-8b/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)
