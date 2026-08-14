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
- primary navigation into both journeys;
- ownership boundary preventing recommendation conclusions from becoming canonical model facts.

## Does Not Own

- complete model taxonomy;
- concrete model facts;
- recommendations, rankings, benchmark conclusions, or deployment guidance;
- duplicate reference and selection indexes.

## Expected Inputs

Requirement-approved title and orientation, links and concise descriptions for `reference/` and `selection/`, and any required ownership-boundary explanation.

## Composition

1. default header;
2. one concise explanation of the two reader intents;
3. prominent navigation to Reference and Selection;
4. short ownership boundary when needed.

## Variants

The detail of each journey may grow, but this page stays concise and does not expand into either subtree's index.

## Representative Example

- `docs/sub/catalog/sub/models/`

## Anti-patterns

- mixing factual model identity with recommendation claims;
- reproducing the complete reference taxonomy;
- burying the Reference/Selection distinction below long background prose.
