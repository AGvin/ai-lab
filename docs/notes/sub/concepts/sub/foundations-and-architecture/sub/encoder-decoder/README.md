# Encoder and Decoder Architectures

<!--
ai_content:
  managed: true
  l10n: true
-->

Encoders transform input into contextual representations, while decoders generate or predict output from prior context and optional encoded input.

## Main forms

- **Encoder-only:** reads the full input bidirectionally and produces representations for classification, retrieval, or extraction.
- **Decoder-only:** predicts tokens autoregressively and is widely used for general-purpose language generation.
- **Encoder-decoder:** encodes an input sequence and generates a separate output sequence, common in translation and summarization.

## Core idea

Architecture influences training objectives, inference behavior, and suitability for tasks. Decoder-only models are flexible generators, while encoder models can be efficient for embeddings and classification.

## Practical use

Choose architecture based on the operation rather than model popularity. A small encoder may outperform a large generator for embeddings or reranking. Encoder-decoder models may provide efficient controlled transformations.

## Trade-offs and limitations

Different architectures use context and cache memory differently. Parameter counts are not directly comparable when model roles differ. A generative decoder can emulate classification but may be slower and less deterministic than a dedicated encoder.

## Common mistakes

- Using a chat model for every text-processing task.
- Comparing encoder and decoder benchmark scores without task context.
- Assuming decoder-only architecture means no internal representations are learned.
- Confusing model architecture with product interface.

## Related concepts

- [Foundations and Architecture](../../)
- [Transformers](../transformers/)
- [Embeddings](../../../retrieval-and-knowledge/sub/embeddings/)
- [Large Language Models](../large-language-models/)
