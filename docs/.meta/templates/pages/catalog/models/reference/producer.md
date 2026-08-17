# Model Producer Page

## Description

Model-domain view for one producer, focused on the model families or lines represented in Model Reference.

## Purpose

Help a reader move from a producer name to the canonical model families represented for that producer without duplicating the producer's organization profile.

## Use When

Use for producer views under `catalog/models/reference/producers/<producer>/`.

## Do Not Use When

Do not use for the canonical producer organization profile, model family, hosted provider page, or generic producer alphabetical index.

## Owns

- model-domain navigation for the producer;
- concise context shared across the producer's represented model families when requirements explicitly place it here;
- links to canonical model families/lines;
- relation-block placement and reader wording when applicable requirements authorize relation presentation.

## Does Not Own

- company history or organization facts already owned by `catalog/producers/`;
- hosted plans, APIs, pricing, or service availability;
- detailed family/model/version facts;
- provider identity merely because it offers access to the models;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved producer-view title and summary, explicit materialized model-family destinations, any genuinely shared model-domain context, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. `entity-relations` when applicable requirements call for relation presentation;
3. concise model-domain orientation;
4. family navigation through `child-navigation`;
5. optional `official-resources` only when requirements need model-domain sources distinct from the producer profile.

## Variants

A producer may expose one or many families. Community-derived producer views may require a descriptive scope note, but that remains content-level variation.

## Representative Examples

- Alibaba -> Qwen;
- Anthropic -> Claude;
- OpenAI -> GPT and Whisper;
- Google -> Gemini and Gemma.

## Anti-patterns

- copying the canonical producer profile;
- listing hosted providers as model owners;
- enumerating or approving individual relation targets in page requirements when the standard relation block is intended;
- filtering visible canonical relation entries inside the template instead of using entity `hidden` controls;
- turning family navigation into recommendation ranking.
