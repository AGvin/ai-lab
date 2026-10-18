# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Link translated pages only when their destinations are materialized and resolve.

- Identify the exact Mistral Small 4 open-weight model and official repository.
- Preserve source-backed MoE structure, total/activated parameter counts, modalities, context length, reasoning-mode support, and license.
- Preserve the official NVFP4 quantized checkpoint and trained EAGLE speculative-decoding head as distinct first-party companion artifact repositories associated with the same base model.
- Keep activated parameters distinct from total parameters and from memory/storage requirements.
- Do not retain untraceable repository-size claims or equate repository size with runtime residency.
- Keep the provider claim that NVFP4 is intended to reduce memory/improve throughput and the EAGLE head to enable speculative decoding as provider evidence rather than AI Lab measured performance.
- Keep provider benchmark, throughput, latency, coding, and agentic claims as evidence inputs rather than AI Lab selection conclusions.
- Keep hosted pricing and API feature availability outside immutable model identity.

## Validation

- Mistral Small 4 is a concrete model under the Mistral Small family, not an artificial series node.
- The base, NVFP4, and EAGLE repositories are not silently collapsed into one artifact identity.
- Repository size is not presented as peak RAM/VRAM, model quality, or production-fit evidence.
- The EAGLE head is not presented as a separate Mistral Small family model without identity evidence.
- Runtime/deployment properties are not inferred from parameter counts.
- No dated recommendation is copied from the legacy page into reference.

## Source-backed profile

- Required reader orientation: Mistral Small 4 is an open-weight multimodal Mixture-of-Experts model in the Mistral Small family.
- Preserve this model-scoped fact: The model has 119B total parameters and 6.5B active per token, with 128 experts and four active experts. It accepts text and images and produces text within a 256K-token context. [Mistral Small 4 weights and reasoning settings](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
- Preserve this model-scoped fact: The March 16, 2026 release uses Apache 2.0. The GA API identifier is `mistral-small-2603`. [Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)
- Preserve this model-scoped fact: The same weights support `reasoning_effort="none"` and `reasoning_effort="high"`; these modes are not separate models. [Mistral Small 4 weights and reasoning settings](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)

## Operational and interpretation boundaries

- Explain this boundary: The NVFP4 checkpoint is a quantized representation and EAGLE is an auxiliary speculative-decoding head. Neither is a separate Mistral Small family model. [Mistral Small 4 NVFP4 artifact](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4) [Mistral Small 4 EAGLE artifact](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-eagle)
- Explain this boundary: Mistral’s artifact collection warns that NVFP4 trades lower long-context performance for its memory and throughput goals. This is a provider claim, not a deployment measurement. [Mistral Small 4 artifact collection](https://huggingface.co/collections/mistralai/mistral-small-4)
- Explain this boundary: Active parameters and repository size are not peak RAM or VRAM requirements. Precision, runtime, context, KV cache, batching and images affect residency.
- Explain this boundary: A reasoning setting does not authorize a tool call. The application validates generated arguments and controls execution. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
