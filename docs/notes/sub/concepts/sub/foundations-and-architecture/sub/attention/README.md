# Attention

Attention is a mechanism that computes how strongly one representation should use information from other representations.

## Core idea

A query is compared with keys to produce attention scores. The scores are normalized and used to combine corresponding values. In transformers, many attention heads learn different patterns of interaction in parallel.

## Practical roles

- Connect a generated token to relevant earlier tokens.
- Align text with image regions or audio features.
- Combine encoder information during sequence generation.
- Represent long-range dependencies more directly than simple recurrence.

## Trade-offs and limitations

Standard full attention compares many pairs of positions and becomes expensive for long sequences. Attention scores are internal computation, not calibrated evidence of causal importance or human-readable reasoning.

## Common mistakes

- Interpreting the largest attention weight as the model's explanation.
- Assuming attention alone stores permanent memory.
- Ignoring masking and positional encoding.
- Treating all attention implementations as computationally identical.

## Related concepts

- [Foundations and Architecture](../../)
- [Self-Attention](../self-attention/)
- [Transformers](../transformers/)
- [FlashAttention](../../../inference-and-serving/sub/flash-attention/)
