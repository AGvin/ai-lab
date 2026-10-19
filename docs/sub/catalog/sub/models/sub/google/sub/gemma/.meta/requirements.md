# Documentation Requirements

## Requirements

- Identify Gemma as Google's open-weight language and multimodal model family.
- Preserve family-level identity and access boundaries without duplicating series or concrete-model specifications.
- Keep exact parameter counts, modalities, context lengths, licenses, artifacts, runtime behavior, and deployment fit on series/concrete model/artifact pages.
- Preserve explicit Google and Google DeepMind producer provenance through the validated canonical relations.

## Content Specification

- Use `Gemma` as the page title.
- Link Google through the current canonical `produced-by` relation.
- Describe Gemma as an open-weight family distinct from provider-hosted Gemini identities.
- Link Gemma 4, its five represented instruction variants, and the independently represented specialized Gemma models and series, including EmbeddingGemma 2.
- Link the current independently useful specialized/open variants FunctionGemma, TranslateGemma, MedGemma 1.5 4B, ShieldGemma 2, T5Gemma 2, VaultGemma, and Gemma 3n while keeping experimental-only DiffusionGemma outside stable intake.
- Preserve the family-level instruction that exact series, concrete model, variant, artifact, runtime, precision, and modality configuration must be recorded for evaluations.
- Include official Gemma documentation and the Google Hugging Face organization.

## Validation

- Gemma is not treated as one exact deployment identity.
- Gemini hosted products are not conflated with Gemma open-weight models.
- Gemma 4 is not typed as a second long-lived model family.
- EmbeddingGemma 2 remains a concrete specialized Gemma model rather than a generic embedding concept or a Gemma 4 alias.
- Specialized Gemma variants remain distinct by task/architecture/lifecycle and are not flattened into Gemma 4 or into generic capability concepts.
- Google/Google DeepMind producer, Gemma 4, and EmbeddingGemma 2 links resolve to canonical nodes.

## Verified identity and provenance

Google and Google DeepMind's open-weight model family; exact model variants, licenses, artifacts, and deployment configurations must be recorded separately.

## Source-scoped operating boundaries

- Gemma 4 uses Apache-2.0, while specialized models can have different terms, including MedGemma's Health AI Developer Foundations terms. Downloadable weights do not imply one family-wide license or a privacy guarantee for the application. [Gemma 4 license](https://ai.google.dev/gemma/docs/core/model_card_4) · [MedGemma documentation](https://developers.google.com/health-ai-developer-foundations/medgemma).
- DiffusionGemma remains explicitly experimental in its current overview and stays outside this released-model intake. Keep that status distinct from the released Gemma 4 instruction checkpoints. [DiffusionGemma status](https://ai.google.dev/gemma/docs/diffusiongemma).
- Local capability, model size, artifact size, and runtime memory are different facts. Selection still requires the exact checkpoint, precision, supported modalities, context, runtime, and workload configuration. [Gemma model overview](https://ai.google.dev/gemma/docs/core).

## Source evidence

- <https://ai.google.dev/gemma/docs/core>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
- <https://ai.google.dev/gemma/docs/diffusiongemma>
- <https://developers.google.com/health-ai-developer-foundations/medgemma>
