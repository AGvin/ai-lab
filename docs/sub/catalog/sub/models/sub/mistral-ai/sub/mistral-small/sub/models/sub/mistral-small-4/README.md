# Mistral Small 4

Mistral Small 4 is an open-weight multimodal Mixture-of-Experts model in the Mistral Small family.

## Translations

- English

## Canonical profile

- Model repository: `mistralai/Mistral-Small-4-119B-2603`
- Architecture: Mixture of Experts (MoE), 128 experts with 4 active
- Total parameters: 119B
- Activated parameters: 6.5B per token in the current official model card
- Input modalities: text and image
- Output modality: text
- Context length: 256K tokens
- Reasoning: `reasoning_effort="none"` and `reasoning_effort="high"` with the same model weights
- License: Apache 2.0

Parameter activation is an architecture fact, not a storage or residency estimate. Exact memory use depends on the artifact, precision, runtime, context, and serving configuration.

[Mistral Small 4 weights and reasoning settings](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) documents these architecture and modality facts.

## Relations

- Family: [Mistral Small](../../../../)

## Release and access

The March 16, 2026 release uses Apache 2.0. The GA API identifier is `mistral-small-2603`. [Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)

## Official artifact repositories

Mistral publishes distinct first-party repositories around the same Mistral Small 4 base model. Keep these identities separate rather than collapsing their file/storage properties into the base model.

### Base checkpoint

- Repository: `mistralai/Mistral-Small-4-119B-2603`

### NVFP4 checkpoint

- Repository: `mistralai/Mistral-Small-4-119B-2603-NVFP4`
- Provider description: post-training activation-quantized checkpoint intended to reduce memory use and improve throughput relative to the base representation

The [Mistral artifact collection](https://huggingface.co/collections/mistralai/mistral-small-4) warns that the NVFP4 route can trade long-context performance for those efficiency goals. Treat that statement as provider evidence until measured on the target runtime and workload.

### EAGLE speculative-decoding head

- Repository: `mistralai/Mistral-Small-4-119B-2603-eagle`
- Role: trained auxiliary head for speculative decoding with the Mistral Small 4 base model

The EAGLE repository is a companion artifact for speculative decoding, not evidence of a separate Mistral Small family model identity.

Repository size is not peak RAM/VRAM or a serving requirement. Runtime precision, tensor parallelism, context, KV cache, batching, multimodal processing, and implementation remain separate deployment evidence.

## Evidence boundary

Mistral publishes coding, agentic, reasoning, throughput, latency, and artifact-efficiency claims for the model. Those claims remain provider evidence until validated for a concrete AI Lab selection task; they are not copied into reference as workload rankings.

A reasoning setting does not authorize a tool call. The application validates generated arguments and controls execution. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

## Official resources

- [Mistral Small 4 weights and reasoning settings](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
- [Mistral Small 4 NVFP4 artifact](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4)
- [Mistral Small 4 EAGLE artifact](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-eagle)
- [Mistral Small 4 release](https://mistral.ai/news/mistral-small-4/)
- [Mistral Small 4 model card](https://docs.mistral.ai/models/mistral-small-4-0-26-03)
- [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)
- [Mistral Small 4 artifact collection](https://huggingface.co/collections/mistralai/mistral-small-4)
