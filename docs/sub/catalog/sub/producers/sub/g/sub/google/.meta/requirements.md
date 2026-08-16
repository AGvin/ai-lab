# Documentation Requirements

## Requirements

- Identify Google as the broader canonical producer organization represented by the migrated Google model, service, agent, and framework entities.
- Keep Google DeepMind as a separate canonical producer identity when official source material attributes model authorship or development specifically to Google DeepMind.
- Preserve Google DeepMind as a structural part of Google through the canonical `has-part` relation; do not reinterpret that fact as an ownership relation.
- Keep model-family, concrete-model, service, agent, and framework details in their own canonical owners rather than duplicating them on the producer page.
- Represent the current Google `produces` relations to Gemini, Gemma, Jules, Gemini CLI, Genkit, and Google ADK.

## Content Specification

- Use `Google` as the page title.
- Describe Google concisely as the broader producer organization for the represented Google catalog entities.
- Preserve the Google model-domain view as navigation and link Gemini, Gemma, Jules, Gemini CLI, Genkit, and Google ADK through their `produces` relations.
- Link the separate Google DeepMind producer profile through the `has-part` relation while preserving its distinct provenance identity.
- Include official Google AI documentation and the official Google Hugging Face organization as research references.

## Validation

- The page does not duplicate concrete model, service, agent, Genkit, or ADK profile details.
- Google DeepMind provenance is not silently collapsed into Google, and structural inclusion is not presented as ownership.
- All represented links resolve to canonical nodes.
