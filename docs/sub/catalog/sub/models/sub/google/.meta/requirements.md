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
- Link Gemini and Gemma as separate model families.
- Preserve the legacy access boundary that Gemini is represented as a provider-hosted family while Gemma publishes open-weight artifacts for local, edge, self-hosted, and research use.
- Include official Gemini and Gemma documentation plus the Google Hugging Face organization as research references.

## Validation

- Gemini APIs and Google AI Studio are not treated as model-family identities.
- Gemma open-weight distributions are not conflated with hosted Gemini identities.
- Gemma provenance does not collapse Google DeepMind into Google.
- Gemini, Gemma, and producer links resolve to canonical nodes.
