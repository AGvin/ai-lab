# Documentation Requirements

## Requirements

- Identify Gemini as the provider-hosted multimodal model family represented under the broader Google model domain, with explicit producer provenance to both Google and Google DeepMind where current official material supports those organization views.
- Preserve family-level identity and access boundaries without duplicating concrete-model specifications.
- Keep API pricing, AI Studio behavior, service limits, deployment workflow, and selection conclusions outside the canonical family profile.
- Use the canonical `models/` collection when the optional series level is omitted.

## Content Specification

- Use `Gemini` as the page title.
- Link Google and Google DeepMind through the canonical `produced-by` relations.
- Describe Gemini as a provider-hosted multimodal model family rather than a local runtime or downloadable artifact family.
- Link Gemini 3.6 Flash through `models/` as the represented concrete model.
- Preserve the distinction between model identity and Gemini API / Google AI Studio access products.
- Include official Gemini model documentation as the primary access/model reference and preserve Google DeepMind model-card provenance through the producer relation.

## Validation

- The Google/Gemini and Google DeepMind/Gemini `produces` / `produced-by` relation pairs are physically present at both endpoints and semantically consistent.
- Concrete model IDs, context limits, modalities, pricing, and service behavior are not generalized to the whole Gemini family.
- Gemini API and Google AI Studio are not treated as model aliases.
- The model collection, producer, and Gemini 3.6 Flash links resolve to canonical nodes.
