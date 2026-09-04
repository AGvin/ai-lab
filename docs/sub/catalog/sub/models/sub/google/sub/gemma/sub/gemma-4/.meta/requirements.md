# Documentation Requirements

## Requirements

- Identify Gemma 4 as a model series within the Gemma family, not as a second long-lived model family or one concrete model.
- Preserve source-specific Google DeepMind provenance descriptively without creating an unverified second producer relation.
- Preserve series-level technical facts that are genuinely shared across documented Gemma 4 models.
- Keep concrete-model parameter identities and artifact details on corresponding model/artifact pages.
- Keep contextual scale classes, hardware-fit conclusions, runtime behavior, and selection guidance outside the canonical series profile.

## Content Specification

- Use `Gemma 4` as the page title and link the Gemma family.
- Preserve Apache-2.0 licensing and the presence of pre-trained and instruction-tuned releases.
- Preserve text/image input across documented sizes, audio on E2B/E4B/12B, video through frame sequences, text output, and multilingual training across more than 140 languages.
- Preserve the context split: 128K for E2B/E4B and 256K for 12B/26B A4B/31B.
- Preserve architecture distinctions: dense E2B/E4B/31B, encoder-free 12B Unified, and MoE 26B A4B.
- Preserve the semantic distinction between effective parameters and total parameters including embeddings for E2B/E4B.
- Preserve the distinction between total and active parameters for MoE models.
- Link the concrete-model index containing E2B Instruct and E4B Instruct.
- Note official QAT availability without duplicating full artifact inventories.
- Include current official Gemma 4 model-card and overview references.

## Validation

- Gemma 4 is typed as `model-series`.
- E2B/E4B effective counts are not treated as complete total-parameter identity.
- MoE active parameters are not treated as total model size or memory requirement.
- Concrete model and artifact details are not duplicated unnecessarily on the series page.
