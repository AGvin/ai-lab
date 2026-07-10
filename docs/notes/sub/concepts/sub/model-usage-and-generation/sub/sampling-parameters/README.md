# Sampling Parameters

<!--
ai_content:
  managed: true
  l10n: true
-->

Sampling parameters control how a generative model chooses the next token from its probability distribution.

## Main controls

- **Temperature:** rescales token probabilities. Lower values usually make output more concentrated and repeatable; higher values increase variation.
- **Top-p:** limits sampling to the smallest token set whose cumulative probability reaches a threshold.
- **Top-k:** limits sampling to the highest-probability `k` tokens.
- **Seed:** may make runs more reproducible when the provider, model, and execution path support deterministic seeding.
- **Repetition or frequency penalties:** discourage repeated tokens or phrases.

## Practical use

Use lower-variance settings for extraction, code edits, classification, and structured output. Use moderate variation for brainstorming, creative writing, or generating diverse candidates. Change one parameter at a time and evaluate results on a stable test set.

## Trade-offs and limitations

Low temperature does not make an answer factual, and high temperature does not create genuine knowledge. Parameter names and behavior vary across runtimes. Deterministic seeds may still produce different outputs after model, hardware, or provider changes.

## Common mistakes

- Combining aggressive temperature, top-p, and top-k changes without measurement.
- Using high randomness for tasks that require exact schemas.
- Assuming temperature zero guarantees identical output.
- Tuning sampling before fixing unclear instructions or missing context.

## Related concepts

- [Model Usage and Generation](../../)
- [Tokens and Tokenization](../tokens-and-tokenization/)
- [Hallucinations](../hallucinations/)
- [Reproducibility](../../../evaluation-and-operations/sub/reproducibility/)
