# Documentation Requirements

## Requirements

- Identify Gemma 4 as a Gemma generation of open-weight multimodal models.
- Preserve the legacy source attribution to Google DeepMind as provenance text without creating an unverified canonical producer relation.
- Preserve generation-level technical facts that are shared across documented Gemma 4 models.
- Keep concrete-model parameter identities and artifact details on the corresponding concrete model pages.
- Keep contextual scale classes, hardware-fit conclusions, runtime behavior, and model-selection guidance outside the canonical generation profile.

## Content Specification

- Use `Gemma 4` as the page title.
- Link the canonical Gemma family.
- State that the legacy source attributes Gemma 4 specifically to Google DeepMind and that the current catalog has not yet modeled Google DeepMind as a separate producer entity.
- Preserve Apache-2.0 licensing and the presence of pre-trained and instruction-tuned variants.
- Preserve the generation-level description as general-purpose multimodal language models with provider-documented reasoning, coding, function-calling, and text-generation capabilities.
- Preserve text and image input across documented sizes; audio support for E2B, E4B, and 12B; video through frame sequences; text output; and multilingual training across more than 140 languages.
- Preserve the context split: 128K tokens for E2B and E4B; 256K for 12B, 26B A4B, and 31B.
- Preserve the architecture split: dense E2B, E4B, 12B, and 31B models plus the sparse Mixture of Experts (MoE) 26B A4B model.
- Preserve the semantic rule that `E` in E2B/E4B denotes effective parameters and that effective and total parameter figures should both be recorded when available.
- Preserve the semantic rule that MoE total and active parameters are separate dimensions and active parameters do not determine storage or memory residency.
- Link a concrete-model index containing Gemma 4 E2B Instruct and Gemma 4 E4B Instruct.
- Note that official Quantization-Aware Training (QAT) artifacts exist for represented local models without duplicating concrete artifact inventories on the generation page.
- Include the official Gemma 4 model card, technical report, and QAT guidance.

## Excluded Residual Content

Preserve outside this canonical generation profile:

- contextual `SLM`/`LLM` classification and comparison conventions;
- exact QAT/GGUF file inventories and multimodal projection files;
- RAM/VRAM, context-cache, runtime-buffer, encoder, concurrency, and hardware-fit conclusions;
- runtime compatibility and local deployment procedures;
- model-selection or workload-suitability recommendations.

## Validation

- No `produced-by Google DeepMind` relation is created until Google DeepMind has a canonical producer identity and validated relationship model.
- E2B/E4B effective parameters are not treated as complete total-parameter identity.
- MoE active parameters are not treated as total model size or memory requirement.
- Concrete model and artifact details are not duplicated unnecessarily on the generation page.
- The Gemma family and concrete-model index links resolve to canonical nodes.
