# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify this checkpoint as the Apache-2.0 Mistral Large 3 instruct release from the Mistral 3 generation.
- Preserve the upstream 675B-total/41B-active MoE and multimodal/general-purpose positioning only at exact checkpoint scope.
- Treat quantizations, deployment requirements, benchmarks, hosted aliases, and provider availability as freshness-sensitive.

## Validation

- Membership resolves to Mistral Large.

## Source-backed profile

- Required reader orientation: Mistral Large 3 675B Instruct 2512 is Mistral AI’s December 2025 multimodal Mixture-of-Experts instruct checkpoint.
- Preserve this model-scoped fact: Mistral reports 675B total and 41B active parameters, with a 256K-token context. The released FP8 instruct weights use Apache 2.0. [Mistral Large 3 model card](https://docs.mistral.ai/models/mistral-large-3-25-12) [Mistral Large 3 weights and limitations](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)
- Preserve this model-scoped fact: The hosted `mistral-large-2512` release remains listed as GA. Its released weights are distinct from the newer Large 4 preview. [Mistral Large 3 model card](https://docs.mistral.ai/models/mistral-large-3-25-12)

## Operational and interpretation boundaries

- Explain this boundary: Mistral explicitly describes limitations in dedicated reasoning, vision-specialist tasks and deployment complexity. The model’s 41B active count does not mean that only 41B parameters need storage. [Mistral Large 3 weights and limitations](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512)
- Explain this boundary: Use the model-specific tokenizer and tool parser; function output and JSON structure do not validate the correctness or authorization of an action. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
