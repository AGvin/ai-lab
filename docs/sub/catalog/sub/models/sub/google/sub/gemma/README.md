# Gemma

Gemma is Google's open-weight model family for local, self-hosted, edge, research, and application workflows.

## Canonical producers

- Produced by: [Google](../../../../../producers/sub/g/sub/google/)
- Produced by: [Google DeepMind](../../../../../producers/sub/g/sub/google-deepmind/)

## Family boundary

Gemma is a model family rather than one exact deployment identity. Exact series, concrete model, instruction variant, artifact, runtime, precision, and modality configuration must be recorded separately when evaluating or deploying a Gemma model.

Gemma's downloadable open-weight distributions are distinct from provider-hosted Gemini model identities.

## Model series and specialized models

- [Gemma 4](sub/gemma-4/)
- [EmbeddingGemma 2](sub/embeddinggemma-2/)
- [FunctionGemma](sub/functiongemma/)
- [TranslateGemma](sub/translategemma/)
- [MedGemma 1.5 4B](sub/medgemma-1-5-4b/)
- [ShieldGemma 2](sub/shieldgemma-2/)
- [T5Gemma 2](sub/t5gemma-2/)
- [VaultGemma](sub/vaultgemma/)
- [Gemma 3n](sub/gemma-3n/)

## Provenance boundary

Source material attributes Gemma development to Google DeepMind. The current catalog does not yet model Google DeepMind as a separate producer entity, so that source-specific provenance remains descriptive text rather than an additional canonical producer relation.

## Scope boundary

This canonical page owns Gemma family identity, broad open-weight access boundary, Google producer relation, and series navigation. Exact technical profiles, artifacts, runtime compatibility, hardware fit, model selection, and evaluation conclusions belong to series/concrete model, deployment/workflow, selection, or evidence documentation.

## Official resources

- <https://ai.google.dev/gemma/>
- <https://huggingface.co/google>
- <https://ai.google.dev/gemma/docs/core>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
- <https://ai.google.dev/gemma/docs/diffusiongemma>
- <https://developers.google.com/health-ai-developer-foundations/medgemma>

## Source-scoped operating boundaries

- Gemma 4 uses Apache-2.0, while specialized models can have different terms, including MedGemma's Health AI Developer Foundations terms. Downloadable weights do not imply one family-wide license or a privacy guarantee for the application. [Gemma 4 license](https://ai.google.dev/gemma/docs/core/model_card_4) · [MedGemma documentation](https://developers.google.com/health-ai-developer-foundations/medgemma).
- DiffusionGemma remains explicitly experimental in its current overview and stays outside this released-model intake. Keep that status distinct from the released Gemma 4 instruction checkpoints. [DiffusionGemma status](https://ai.google.dev/gemma/docs/diffusiongemma).
- Local capability, model size, artifact size, and runtime memory are different facts. Selection still requires the exact checkpoint, precision, supported modalities, context, runtime, and workload configuration. [Gemma model overview](https://ai.google.dev/gemma/docs/core).
