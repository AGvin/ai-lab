# Documentation Requirements

## Requirements

- Identify Google as the broader canonical producer organization represented by the migrated Google model, service, agent, and framework entities.
- Keep Google DeepMind as a separate canonical producer identity when official source material attributes model authorship or development specifically to Google DeepMind.
- Preserve Google DeepMind as a structural part of Google through the physically materialized `has-part` relation when the reciprocal Google DeepMind `part-of` relation resolves successfully; do not reinterpret that fact as an ownership relation.
- Keep model-family, concrete-model, service, agent, and framework details in their own canonical owners rather than duplicating them on the producer page.
- Represent the current Google `produces` edges to Gemini, Gemma, Jules, Gemini CLI, Genkit, and Google ADK with reciprocal endpoint validation.

## Content Specification

- Use `Google` as the page title.
- Describe Google concisely as the broader producer organization for the represented Google catalog entities.
- Preserve the Google model-domain view as navigation and link Gemini, Gemma, Jules, Gemini CLI, Genkit, and Google ADK from their physically materialized `produces` relations.
- Link the separate Google DeepMind producer profile from the physical `has-part` relation while preserving its distinct provenance identity.
- Include official Google AI documentation and the official Google Hugging Face organization as research references.

## Validation

- The Google/Gemini, Google/Gemma, Google/Jules, Google/Gemini CLI, Google/Genkit, and Google/Google ADK `produces` / `produced-by` relation pairs are physically present at both endpoints and semantically consistent.
- The Google/Google DeepMind `has-part` / `part-of` relation pair is physically present at both endpoints and semantically consistent.
- The page does not duplicate concrete model, service, agent, Genkit, or ADK profile details.
- Google DeepMind provenance is not silently collapsed into Google, and structural inclusion is not presented as ownership.
- All represented links resolve to canonical nodes.
