# Gemma 4

Gemma 4 is a multimodal generation in the Gemma open-weight model family. The legacy source attributes this generation specifically to Google DeepMind.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Model family

- [Gemma](../..)

## Provenance boundary

The current catalog does not yet model Google DeepMind as a separate producer entity. The source-specific Google DeepMind attribution is therefore preserved here as provenance text rather than converted into an unverified canonical producer relation.

## Generation profile

- License: Apache-2.0
- Release forms: pre-trained and instruction-tuned variants
- Input: text and images across documented sizes; audio on E2B, E4B, and 12B; video through frame sequences
- Output: text
- Languages: trained across more than 140 languages in the documented release
- Context: 128K tokens for E2B and E4B; 256K for 12B, 26B A4B, and 31B
- Architecture: dense E2B, E4B, 12B, and 31B models plus a sparse Mixture of Experts (MoE) 26B A4B model

Google describes Gemma 4 for reasoning, coding, function calling, and general text-generation workloads. Those are provider-described capabilities rather than independent AI Lab quality evidence.

For E2B and E4B, `E` denotes effective parameters. Effective and total parameter counts are separate fields and should both be recorded when available. Likewise, MoE active parameters must not be treated as total model size or memory residency.

## Models

- [Gemma 4 E2B Instruct](./sub/models/sub/e2b-instruct/) — dense instruction-tuned multimodal model with 2B effective parameters.
- [Gemma 4 E4B Instruct](./sub/models/sub/e4b-instruct/) — dense instruction-tuned multimodal model with 4B effective parameters.

Official Quantization-Aware Training (QAT) artifacts exist for represented local models. Exact artifact inventories and runtime/deployment implications remain on concrete model, artifact, or future deployment documentation rather than this generation page.

## Scope boundary

This canonical page owns Gemma 4 generation identity, source-specific provenance, shared modalities/context/architecture semantics, and concrete-model navigation. Contextual scale classification, exact QAT/GGUF inventories, RAM/VRAM planning, runtime compatibility, hardware fit, and model-selection conclusions belong to classification/reference, artifact, deployment/workflow, decision-support, or evidence documentation.

## Official resources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/gemma_4)
- [Gemma 4 technical report](https://goo.gle/gemma4report)
- [Gemma 4 QAT guidance](https://ai.google.dev/gemma/docs/core/qat)
