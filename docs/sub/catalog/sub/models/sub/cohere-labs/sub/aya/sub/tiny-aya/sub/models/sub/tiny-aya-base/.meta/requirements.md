# Documentation Requirements

## Identity and provenance

- **Tiny Aya Base** is the independently published `CohereLabs/tiny-aya-base` (original pretrained text model, 3.35B parameters). Original 3.35B pretrained base for multilingual downstream training, distinct from the separately instruction-tuned Global and regional weights. Its 8K context does not imply a live Cohere Chat endpoint or chat-template alignment. [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-base) [Cohere research](https://cohere.com/blog/cohere-labs-tiny-aya).

## Operating contract and limitations

- The checkpoint is text-only, with 8K input context and published language scope of 70+ languages; supported prompt modes and evaluation results are model-specific, not inherited from other Aya releases. [Exact card](https://huggingface.co/CohereLabs/tiny-aya-base).
- Downloadable weights require license-gated access under CC-BY-NC-4.0 and Cohere Labs acceptable-use terms; commercial self-hosting, live API hosting, independently repeated benchmarks, actual inference, hardware fit and corporate beneficial ownership are not verified. [Weights](https://huggingface.co/CohereLabs/tiny-aya-base) [License](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Validation

- Preserve the exact independent model ID, series membership, precise Cohere co-producer and only the explicitly supported reciprocal trained-parent edges. Do not turn GGUF/quantized artifacts or hosted aliases into new learned models.
- Verify reader links and exact source card boundaries; this does not certify local runtime, benchmarks, full schema/cache or final renderer closure.
