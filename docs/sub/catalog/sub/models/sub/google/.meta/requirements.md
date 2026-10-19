# Documentation Requirements

## Requirements

- Provide model-domain navigation for Google model families represented in the migrated catalog.
- Keep canonical organization identities in the producer catalog rather than duplicating organization content here.
- Preserve both Gemini and Gemma from the legacy Google model documentation.
- Preserve Gemma provenance to Google DeepMind separately from the broader Google organization identity.
- Keep hosted access products, APIs, AI Studio, runtime/deployment guidance, and decision-support conclusions outside this model-domain view.

## Content Specification

- Use `Google models` as the page title.
- Link the canonical Google and Google DeepMind producer pages under `catalog/producers/` where provenance requires them.
- Link every represented Google model family and standalone model, including Gemini, Gemini Omni, Gemma, Lyria, Veo, AlphaFold, AlphaGenome, and WeatherNext.
- Preserve the legacy access boundary that Gemini is represented as a provider-hosted family while Gemma publishes open-weight artifacts for local, edge, self-hosted, and research use.
- Include official Gemini and Gemma documentation plus the Google Hugging Face organization as research references.

## Validation

- Gemini APIs and Google AI Studio are not treated as model-family identities.
- Gemma open-weight distributions are not conflated with hosted Gemini identities.
- Gemma provenance does not collapse Google DeepMind into Google.
- Gemini, Gemma, and producer links resolve to canonical nodes.

## Verified identity and provenance

Navigation view of Google's model portfolio; Google and Google DeepMind remain separate canonical producer identities, and hosted products are separate from models.

## Source-scoped operating boundaries

- This view groups distinct model tasks and access regimes. Hosted Gemini models, downloadable Gemma weights, scientific models, and forecast or media services require their own concrete model and distribution identity. [Google model portfolio](https://deepmind.google/models/).
- Gemma 4's Apache-2.0 license does not establish the license or permitted use of every Google model. Use the concrete model's source and terms. [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4).

## Source evidence

- <https://deepmind.google/models/>
- <https://ai.google.dev/gemini-api/docs/models>
- <https://ai.google.dev/gemma/docs/core>
