# Gemini

Gemini is Google's provider-hosted multimodal model family.

## Canonical producers

- Produced by: [Google](../../../../../producers/sub/g/sub/google/)
- Produced by: [Google DeepMind](../../../../../producers/sub/g/sub/google-deepmind/)

## Family boundary

Gemini models are accessed through provider-hosted products such as the Gemini API and Google AI Studio. Those access surfaces are not replacement model identities and should not be used as substitutes for exact model IDs.

## Models

- [Concrete Gemini models](sub/models/)

## Scope boundary

This canonical page owns Gemini family identity, Google producer relation, hosted-access boundary, and concrete-model navigation. Exact model IDs, context limits, supported modalities and model-specific features belong to concrete models; pricing, service limits, AI Studio behavior, deployment workflow, and selection conclusions belong to service/product, workflow, selection, or evidence documentation.

## Official resources

- <https://ai.google.dev/gemini-api/docs/models>
- <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash>
- <https://deepmind.google/models/gemini/>
- <https://ai.google.dev/gemini-api/docs/deprecations>
- <https://ai.google.dev/gemini-api/docs/function-calling>

## Source-scoped operating boundaries

- Choose and record a concrete model ID. General reasoning, image generation, embeddings, transcription, TTS, Live audio, and allowlisted cyber models do not share a universal feature matrix. [Model inventory](https://ai.google.dev/gemini-api/docs/models).
- Lifecycle routing can change the model behind an older endpoint: Gemini 3.7 Flash currently routes to 3.8 Flash. Keep routed historical identities distinguishable from independently served models. [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Function-calling support means the model can request an application function. Tool execution, permissions, and validation remain application responsibilities. Gemini API and Cloud terms, access controls, and feature availability must be evaluated for the actual serving route. [Function-calling workflow](https://ai.google.dev/gemini-api/docs/function-calling).
