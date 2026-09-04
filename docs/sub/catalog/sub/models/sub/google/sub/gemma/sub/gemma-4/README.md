# Gemma 4

Gemma 4 is a multimodal model series within Google's Gemma open-weight family. The series contains distinct dense, unified, and Mixture-of-Experts model identities rather than one executable model.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model family

- [Gemma](../..)

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

- [Gemma 4 E2B Instruct](./sub/models/sub/e2b-instruct/) — dense instruction-tuned multimodal model with 2.3B effective parameters and 5.1B parameters including embeddings.
- [Gemma 4 E4B Instruct](./sub/models/sub/e4b-instruct/) — dense instruction-tuned multimodal model with 4.5B effective parameters and 8B parameters including embeddings.

Official Quantization-Aware Training (QAT) artifacts exist for represented local models. Exact artifact inventories and runtime/deployment implications remain on concrete model, artifact, or deployment documentation rather than this series page.

## Scope boundary

This canonical page owns Gemma 4 series identity, source-specific provenance, shared modality/context/architecture semantics, and concrete-model navigation. Exact model facts, QAT/GGUF inventories, RAM/VRAM planning, runtime compatibility, hardware fit, and selection conclusions belong to concrete model, artifact, deployment/workflow, selection, or evidence documentation.

## Official resources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 overview](https://ai.google.dev/gemma/docs/core)
- [Gemma 4 QAT guidance](https://ai.google.dev/gemma/docs/core/qat)
