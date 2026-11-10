# Documentation Requirements

## Identity and provenance

- **Tiny Aya L2-Thinker** is the independently published `CohereLabs/tiny-aya-l2-thinker` (multilingual in-language reasoning text model, 3.35B parameters). Distinct 3.35B supervised reasoning fine-tune from Base 32K. It emits a visible thinking trace in the prompt language before its final answer. Cohere reports >93% in-language reasoning over six tests and 60 languages, not independently replicated. [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker) [Cohere research](https://cohere.com/blog/building-multilingual-bridges).

## Operating contract and limitations

- The checkpoint is text-only, with 32K combined input/output context and published language scope of 44 translated reasoning languages plus English, with broader non-reasoning-language coverage; supported prompt modes and evaluation results are model-specific, not inherited from other Aya releases. [Exact card](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker).
- Downloadable weights require license-gated access under CC-BY-NC-4.0 and Cohere Labs acceptable-use terms; commercial self-hosting, live API hosting, independently repeated benchmarks, actual inference, hardware fit and corporate beneficial ownership are not verified. [Weights](https://huggingface.co/CohereLabs/tiny-aya-l2-thinker) [License](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Validation

- Preserve the exact independent model ID, series membership, precise Cohere co-producer and only the explicitly supported reciprocal trained-parent edges. Do not turn GGUF/quantized artifacts or hosted aliases into new learned models.
- Verify reader links and exact source card boundaries; this does not certify local runtime, benchmarks, full schema/cache or final renderer closure.
