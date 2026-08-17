# Models Landing Page

## Description

Orientation page for the Models domain that separates canonical factual reference from task-oriented model selection.

## Purpose

Help a reader decide whether they need to learn what a model is or decide which model fits a concrete assignment.

## Use When

Use for `catalog/models/`.

## Do Not Use When

Do not use for Model Reference, Model Selection, a model producer, family, series, concrete model, version, or artifact.

## Owns

- the distinction between the `reference/` and `selection/` reader journeys;
- concise explanation of what each journey is for;
- child-navigation placement and reader wording for the materialized direct model journeys;
- ownership boundary preventing recommendation conclusions from becoming canonical model facts.

## Does Not Own

- direct-child membership or ordering, which come from the validated current-node navigation projection;
- complete model taxonomy;
- concrete model facts;
- recommendations, rankings, benchmark conclusions, or deployment guidance;
- duplicate reference and selection indexes.

## Expected Inputs

Requirement-approved title and orientation, authorization for the primary child-navigation block, the validated current-node direct-child projection, and any required ownership-boundary explanation.

## Composition

1. default header;
2. one concise explanation of the factual-reference and decision-support reader intents;
3. prominent `child-navigation` to the materialized direct model journeys using the validated direct-child projection;
4. short ownership boundary when needed.

## Variants

The detail of each journey may grow, but this page stays concise and does not expand into either subtree's index.

## Representative Example

- `docs/sub/catalog/sub/models/`

## Anti-patterns

- enumerating the direct model journeys in page requirements when the standard child-navigation block is intended;
- filtering direct model journeys inside the template instead of using the canonical navigation projection;
- mixing factual model identity with recommendation claims;
- reproducing the complete reference taxonomy;
- burying the Reference/Selection distinction below long background prose.
