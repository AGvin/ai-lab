# Documentation Requirements

## Identity and provenance

- **Tiny Aya Base 32K** is the independently published `CohereLabs/tiny-aya-base-32K` (long-context pretrained text model, 3.35B parameters). Separate 3.35B pretrained research checkpoint with extended context. Exact original 8K-to-32K weight lineage is not independently established; this is the documented training base for the two separately fine-tuned Thinker checkpoints. [Exact model card](https://huggingface.co/CohereLabs/tiny-aya-base-32K) [Cohere research](https://cohere.com/blog/building-multilingual-bridges).

## Operating contract and limitations

- The checkpoint is text-only, with 32K combined input/output context and published language scope of 70+ languages; supported prompt modes and evaluation results are model-specific, not inherited from other Aya releases. [Exact card](https://huggingface.co/CohereLabs/tiny-aya-base-32K).
- Downloadable weights require license-gated access under CC-BY-NC-4.0 and Cohere Labs acceptable-use terms; commercial self-hosting, live API hosting, independently repeated benchmarks, actual inference, hardware fit and corporate beneficial ownership are not verified. [Weights](https://huggingface.co/CohereLabs/tiny-aya-base-32K) [License](https://cohere.com/cohere-labs-cc-by-nc-license) [Acceptable-use](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).

## Validation

- Preserve the exact independent model ID, series membership, precise Cohere co-producer and only the explicitly supported reciprocal trained-parent edges. Do not turn GGUF/quantized artifacts or hosted aliases into new learned models.
- Verify reader links and exact source card boundaries; this does not certify local runtime, benchmarks, full schema/cache or final renderer closure.
