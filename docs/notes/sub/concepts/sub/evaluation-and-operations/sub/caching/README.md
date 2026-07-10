# Caching

Caching reuses previously computed results or processed data to reduce latency, cost, and repeated work.

## Common cache targets

- Complete model responses.
- Prompt-prefix or context state.
- Embeddings and document chunks.
- Retrieval results.
- Tool and API responses.
- Model-loading artifacts or compiled kernels.

## Core idea

A cache key must include every input and configuration detail that changes the correct result. For AI systems, this may include model version, system prompt, user permissions, retrieval index version, temperature, locale, and tool state.

## Practical use

Cache deterministic or low-variance requests with stable data. Define expiry and invalidation rules before deployment. Isolate user and tenant data, and avoid caching sensitive content when the risk exceeds the benefit.

## Trade-offs and limitations

Caching can return stale or unauthorized results. Large cache keys and low hit rates add complexity without benefit. Generative output caching also reduces variation, which may or may not be desirable.

## Common mistakes

- Omitting user identity or permissions from the key.
- Reusing results after prompt or model changes.
- Caching error responses indefinitely.
- Treating cache invalidation as an afterthought.

## Related concepts

- [Evaluation and Operations](../../)
- [Context Caching](../../../inference-and-serving/sub/context-caching/)
- [Data Privacy](../../../safety-privacy-and-reliability/sub/data-privacy/)
- [Cost Management](../cost-management/)
