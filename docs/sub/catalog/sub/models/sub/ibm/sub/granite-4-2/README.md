# Granite 4.2

Granite 4.2 is IBM's dense reasoning language-model family released on 25 August 2026. The catalog materializes the 3B, 8B, and 30B post-trained reasoning models as distinct trained-model identities.

## Decision and operating boundaries

All three reviewed model cards document native 128K context with a supported long-context extension to 512K, Apache-2.0 weights, built-in thinking modes, tool calling, coding, and agentic workflows. They list twelve tested languages: English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese.

The model cards name corresponding Granite 4.1 base checkpoints. Those source-only dependencies are not materialized as new catalog nodes in this package. Quantized and serving-specific distributions likewise remain artifacts of the 3B, 8B, or 30B identity.

Tool requests still require an execution harness, and advertised context or benchmark results do not guarantee application quality across every prompt or runtime.

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite 4.2 3B](sub/models/sub/granite-4-2-3b/) — member.
- [Granite 4.2 8B](sub/models/sub/granite-4-2-8b/) — member.
- [Granite 4.2 30B](sub/models/sub/granite-4-2-30b/) — member.

## Official resources

- <https://huggingface.co/blog/ibm-granite/granite-4-2>
- <https://huggingface.co/collections/ibm-granite/granite-42-language-models>
- <https://huggingface.co/ibm-granite/granite-4.2-3b>
- <https://huggingface.co/ibm-granite/granite-4.2-8b>
- <https://huggingface.co/ibm-granite/granite-4.2-30b>
