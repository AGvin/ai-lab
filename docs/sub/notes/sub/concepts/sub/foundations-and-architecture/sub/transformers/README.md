# Transformers

A transformer is a neural network architecture built around attention, feed-forward layers, residual connections, and normalization.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Transformers process token representations in parallel during training and prompt processing. Attention lets each position combine information from other relevant positions, while feed-forward layers transform each position independently. Positional information preserves sequence order.

## Common forms

- Encoder-only models for representation and classification.
- Decoder-only models for autoregressive generation.
- Encoder-decoder models for sequence-to-sequence tasks.
- Multimodal transformers that integrate visual or audio tokens.

## Practical use

Transformers underlie most modern language models and many vision, audio, and multimodal systems. Runtime requirements are influenced by number of layers, hidden dimensions, attention configuration, vocabulary size, and context length.

## Trade-offs and limitations

Standard attention cost grows strongly with sequence length. Long contexts therefore require substantial computation and KV-cache memory. Transformers can also learn statistical shortcuts and do not inherently provide factual verification or persistent memory.

## Common mistakes

- Treating transformer as synonymous with LLM.
- Assuming attention weights provide a complete explanation.
- Ignoring architecture variants when comparing parameter counts.
- Expecting longer context to guarantee better recall.

## Related concepts

- [Foundations and Architecture](../../)
- [Attention](../attention/)
- [Self-Attention](../self-attention/)
- [Encoder and Decoder Architectures](../encoder-decoder/)
