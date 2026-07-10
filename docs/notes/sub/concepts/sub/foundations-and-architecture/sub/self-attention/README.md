# Self-Attention

Self-attention is attention in which queries, keys, and values are derived from positions in the same sequence or representation set.

## Core idea

Each position can combine information from other positions according to learned relevance scores. In causal language models, masking prevents a token from attending to future tokens during generation. Bidirectional encoders may allow attention in both directions.

## Practical significance

Self-attention lets models connect pronouns with earlier nouns, relate code references across a function, or combine distant parts of a document. Multiple layers progressively transform these relationships into higher-level representations.

## Trade-offs and limitations

Full self-attention becomes expensive as sequence length grows. Sparse, sliding-window, or grouped mechanisms reduce cost but change which positions interact directly. Attention may also focus on statistically useful patterns that are not semantically trustworthy.

## Common mistakes

- Forgetting the difference between causal and bidirectional masking.
- Assuming every token attends equally to the full advertised context.
- Treating attention maps as definitive interpretability.
- Confusing self-attention with cross-attention between modalities or sequences.

## Related concepts

- [Foundations and Architecture](../../)
- [Attention](../attention/)
- [Transformers](../transformers/)
- [Context Window](../../../model-usage-and-generation/sub/context-window/)
