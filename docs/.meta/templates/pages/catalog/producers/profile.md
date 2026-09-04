# Producer Profile Page

## Description

Canonical profile for one stable producing, publishing, maintaining, or operating identity such as an organization, team, or individual.

## Purpose

Help a reader understand who the producer is, what canonical identity is represented here, and where its authoritative resources and related catalog entities live.

## Use When

Use for canonical producer entities under `catalog/producers/`.

## Do Not Use When

Do not use for a producer-specific model-domain view, a hosted service, software product, or model family.

## Owns

- producer identity and concise stable description;
- authoritative producer resources;
- relation-block placement and reader wording when applicable requirements authorize relation presentation;
- minimal context needed to distinguish the producer from similarly named entities.

## Does Not Own

- detailed model-family facts;
- hosted product state, pricing, plans, or mutable service availability;
- full software/service profiles merely because the producer owns them;
- duplicated facts already owned by child or related canonical entities;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved display title and summary, canonical producer identity, explicit authoritative resources, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. concise producer identity/orientation;
3. `entity-relations` when applicable requirements call for relation presentation;
4. focused navigation to important represented entities when requirements call for it;
5. `official-resources`.

## Variants

Organizations, teams, and individuals reuse this family. Differences in legal form or organizational role remain content-level distinctions unless they produce a materially different reader journey.

## Representative Examples

- `docs/sub/catalog/sub/producers/sub/n/sub/nvidia/`
- canonical OpenAI, Anthropic, Qwen Team, and other producer profiles when materialized.

## Anti-patterns

- duplicating model or product catalogs in the producer profile;
- treating provider access as producer identity;
- enumerating or approving individual relation targets in page requirements when the standard relation block is intended;
- filtering visible canonical relation entries inside the template instead of using entity `hidden` controls;
- allowing mutable commercial state to dominate a stable identity page.
