# Gemma 4

Gemma 4 is a multimodal model series within Google's Gemma open-weight family. The series contains distinct dense, unified, and Mixture-of-Experts model identities rather than one executable model.

## Model family

- Member of: [Gemma](../../)

## Provenance boundary

Google's Gemma documentation attributes Gemma development to Google DeepMind. The current catalog does not yet model Google DeepMind as a separate producer entity, so that provenance remains descriptive rather than converted into an unverified second producer relation.

## Series profile

- License: Apache-2.0
- Release forms: pre-trained and instruction-tuned variants
- Input: text and images across documented sizes; audio on E2B, E4B, and 12B; video through frame sequences
- Output: text
- Languages: trained across more than 140 languages in the documented release
- Context: 128K tokens for E2B and E4B; 256K for 12B, 26B A4B, and 31B
- Architecture: dense E2B, E4B, and 31B models; encoder-free 12B Unified; sparse MoE 26B A4B

Google describes Gemma 4 for reasoning, coding, function calling, and multimodal understanding. Those are provider-described capabilities rather than independent AI Lab task evidence.

For E2B and E4B, `E` denotes effective parameters. Effective parameters and the larger parameter total including per-layer embeddings are separate fields and must both be recorded when available. Likewise, MoE active parameters are distinct from total parameters and do not determine storage or memory residency.

## Models

- [Gemma 4 12B Unified Instruct](sub/models/sub/12b-unified-instruct/)
- [Gemma 4 26B A4B Instruct](sub/models/sub/26b-a4b-instruct/)
- [Gemma 4 31B Instruct](sub/models/sub/31b-instruct/)
- [Gemma 4 E2B Instruct](sub/models/sub/e2b-instruct/)
- [Gemma 4 E4B Instruct](sub/models/sub/e4b-instruct/)

## Scope boundary

This canonical page owns Gemma 4 series identity, source-specific provenance, shared modality/context/architecture semantics, and concrete-model navigation. Exact model facts, QAT/GGUF inventories, RAM/VRAM planning, runtime compatibility, hardware fit, and selection conclusions belong to concrete model, artifact, deployment/workflow, selection, or evidence documentation.

## Official resources

- <https://ai.google.dev/gemma/docs/core/model_card_4>
- <https://huggingface.co/collections/google/gemma-4>
- <https://ai.google.dev/gemma/docs/core>

## Source-scoped operating boundaries

- E2B/E4B have 128K context; 12B/26B A4B/31B have 256K. Audio input belongs to E2B, E4B, and 12B; the 26B A4B and 31B variants do not support audio. All variants generate text. [Architecture and modality matrix](https://ai.google.dev/gemma/docs/core/model_card_4).
- Use the Gemma 4 chat template and supported thinking controls. Tool-call generation does not authorize execution, and published safety evaluations do not replace application-specific filtering, privacy handling, or output validation. [Configuration and risk guidance](https://ai.google.dev/gemma/docs/core/model_card_4).
