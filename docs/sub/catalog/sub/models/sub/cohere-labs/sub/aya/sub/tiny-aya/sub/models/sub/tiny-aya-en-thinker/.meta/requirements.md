# Documentation Requirements

## Identity and provenance

- **Tiny Aya En-Thinker** is the independently published `CohereLabs/tiny-aya-en-thinker` (multilingual English-trace reasoning text model, 3.35B parameters). Distinct 3.35B supervised fine-tune from Base 32K. The thinking trace is in English, with multilingual user-facing answers. The different training target is not merely a serving toggle of L2-Thinker. [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-en-thinker) [Cohere research](https://cohere.com/blog/building-multilingual-bridges).

## Operating contract and limitations

- The checkpoint is text-only, with 32K combined input/output context and published language scope of 44 translated reasoning languages plus English, with broader non-reasoning-language coverage; supported prompt modes and evaluation results are model-specific, not inherited from other Aya releases. [Exact card](https://huggingface.co/CohereLabs/tiny-aya-en-thinker).
- Downloadable weights require license-gated access under CC-BY-NC-4.0 and Cohere Labs acceptable-use terms; commercial self-hosting, live API hosting, independently repeated benchmarks, actual inference, hardware fit and corporate beneficial ownership are not verified. [Weights](https://huggingface.co/CohereLabs/tiny-aya-en-thinker) [License](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Validation

- Preserve the exact independent model ID, series membership, precise Cohere co-producer and only the explicitly supported reciprocal trained-parent edges. Do not turn GGUF/quantized artifacts or hosted aliases into new learned models.
- Verify reader links and exact source card boundaries; this does not certify local runtime, benchmarks, full schema/cache or final renderer closure.
