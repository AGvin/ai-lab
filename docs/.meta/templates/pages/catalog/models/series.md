# Model Series Page

## Description

Canonical profile for one model generation, line, or series inside a family.

## Purpose

Explain what is shared by this series, how it relates to its parent family, and which concrete models belong to the represented branch.

## Use When

Use where the architecture materializes a distinct series/generation level such as Qwen3.

## Do Not Use When

Do not use for the family itself, a concrete parameter-size model, a chronological release revision, or an artifact repository.

## Owns

- series identity and family membership;
- relation-block placement and reader wording when applicable requirements authorize relation presentation;
- facts shared across the represented series;
- series-level lineage/history;
- series-wide capabilities/boundaries with correct source scope;
- navigation to concrete model identities.

## Does Not Own

- facts true only of one concrete model;
- revision-specific changes;
- artifact identity;
- selection/hardware-fit conclusions;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved series orientation, series-scoped facts, concrete-model index navigation, authoritative series resources, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. `entity-relations` when applicable requirements call for relation presentation;
3. concise series identity and shared characteristics;
4. important series-level distinctions and boundaries;
5. navigation to concrete models, often through a child-index node;
6. `official-resources`.

## Variants

Dense-only, MoE-only, or mixed series can reuse this family. Technical sections vary with requirements and evidence rather than generating empty placeholders.

## Representative Example

- Qwen3 within Qwen.

## Anti-patterns

- collapsing concrete models into the series identity;
- treating version-specific facts as series-wide;
- inferring a series level solely from naming;
- enumerating or approving individual relation targets in page requirements when the standard relation block is intended;
- filtering visible canonical relation entries inside the template instead of using entity `hidden` controls.
