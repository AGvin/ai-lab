# PII-Tracer

PII-Tracer is Perplexity AI's separately released **personally identifiable information (PII) masking model** for conversational data. It uses the [PPLX Embed V1 0.6B](../pplx-embed-v1/sub/models/sub/pplx-embed-v1-0-6b/) backbone as an approximately 600M-parameter bidirectional Qwen3 encoder, with a token-classification head and a conversation-level sensitivity head.

## Model and processing boundaries

PII-Tracer is a trained model, distinct from the similarly named **PII-TRACE** dataset or benchmark. The checkpoint is published under the **MIT license**. Label definitions, token decoding, error rates and sensitive-data handling must be checked against the official card and target data; automated masking can miss or over-mask identifiers.

MLX, vLLM and GGUF repositories are distribution or runtime variants of this model unless their weights diverge in trained semantics. They are not automatically separate model identities.

## Producer and official source

- [Perplexity AI model catalog](../../)
- [Official PII-Tracer checkpoint](https://huggingface.co/perplexity-ai/PII-Tracer)
