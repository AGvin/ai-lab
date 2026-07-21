# Context Caching

Context caching reuses previously processed prompt prefixes so repeated requests do not recompute the same input tokens.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Many requests share a stable prefix such as a system prompt, tool definitions, a long document, or a conversation history. A runtime or provider can store the processed representation and continue from it when a later request uses an identical or compatible prefix.

## Practical use

- Repeated queries over the same document.
- Long system prompts and tool schemas.
- Multi-turn conversations.
- Batch tasks sharing a common instruction prefix.
- Agent workflows that revisit stable context.

## Trade-offs and limitations

Caching reduces prompt-processing latency and cost but consumes memory or storage. Cache keys must account for the exact model, tokenizer, prompt bytes, configuration, and sometimes position. Small changes may invalidate the cache.

## Security considerations

Cache entries must be isolated between users and tenants. Sensitive prompts require appropriate retention and encryption policies. A cache hit must never expose another user's context.

## Common mistakes

- Confusing provider prompt caching with the active request's KV cache.
- Assuming semantically similar text produces a cache hit.
- Reusing cached state after changing the model or system prompt.
- Ignoring cache invalidation and privacy boundaries.

## Related concepts

- [Inference and Serving](../../)
- [KV Cache](../kv-cache/)
- [Caching](../../../evaluation-and-operations/sub/caching/)
- [Data Privacy](../../../safety-privacy-and-reliability/sub/data-privacy/)
