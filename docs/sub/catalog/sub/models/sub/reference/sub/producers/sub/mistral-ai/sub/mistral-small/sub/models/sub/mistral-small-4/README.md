# Mistral Small 4

Mistral Small 4 is an open-weight multimodal Mixture-of-Experts model in the Mistral Small family.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical profile

- Model repository: `mistralai/Mistral-Small-4-119B-2603`
- Architecture: Mixture of Experts (MoE), 128 experts with 4 active
- Total parameters: 119B
- Activated parameters: 6.5B per token in the current official model card
- Input modalities: text and image
- Output modality: text
- Context length: 256K tokens
- Reasoning: configurable instruct/reasoning modes in the current model card
- License: Apache 2.0

Parameter activation is an architecture fact, not a storage or residency estimate. Exact memory use depends on the artifact, precision, runtime, context, and serving configuration.

## Official artifact repositories

Mistral publishes distinct first-party repositories around the same Mistral Small 4 base model. Keep these identities separate rather than collapsing their file/storage properties into the base model.

### Base checkpoint

- Repository: `mistralai/Mistral-Small-4-119B-2603`
- Hugging Face repository size verified 2026-08-11: approximately 242 GB

### NVFP4 checkpoint

- Repository: `mistralai/Mistral-Small-4-119B-2603-NVFP4`
- Hugging Face repository size verified 2026-08-11: approximately 70.8 GB
- Provider description: post-training activation-quantized checkpoint intended to reduce memory use and improve throughput relative to the base representation

The current Mistral collection warns that the NVFP4 route can trade long-context performance for those efficiency goals. Treat that statement as provider evidence until measured on the target runtime and workload.

### EAGLE speculative-decoding head

- Repository: `mistralai/Mistral-Small-4-119B-2603-eagle`
- Role: trained auxiliary head for speculative decoding with the Mistral Small 4 base model

The EAGLE repository is a companion artifact for speculative decoding, not evidence of a separate Mistral Small family model identity.

Repository size is not peak RAM/VRAM or a serving requirement. Runtime precision, tensor parallelism, context, KV cache, batching, multimodal processing, and implementation remain separate deployment evidence.

## Evidence boundary

Mistral publishes coding, agentic, reasoning, throughput, latency, and artifact-efficiency claims for the model. Those claims remain provider evidence until validated for a concrete AI Lab selection task; they are not copied into reference as workload rankings.

## Official resources

- [Mistral Small 4 model card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
- [Mistral Small 4 NVFP4 checkpoint](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-NVFP4)
- [Mistral Small 4 EAGLE head](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603-eagle)
- [Mistral Small 4 documentation](https://docs.mistral.ai/models/model-cards/mistral-small-4-0-26-03)
- [Introducing Mistral Small 4](https://mistral.ai/news/mistral-small-4/)
