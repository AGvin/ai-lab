# Entity Relations Component

## Description

Reusable block for presenting the current entity's validated reader-facing semantic relations.

## Purpose

Present canonical relationships consistently when the applicable page requirements and template authorize a relation block, without duplicating relation targets or ordering rules in `.meta/requirements.md`.

## Inputs

The caller supplies the resolved current-entity relation projection from canonical `entity.relations` data. Requirements authorize the relation block or its reader-facing outcome as a whole; they do not individually approve relation entries.

Each visible entry is derived from a validated relation record and its resolved target. Reader-facing relation wording may be adapted by the template/component, but membership, endpoint-local visibility, and ordering remain governed by the entity schema and relation contract.

## Rendering Rules

- include every validated current-entity relation eligible for the authorized block except records with `hidden: true`;
- do not omit a visible relation merely because the component independently judges it less useful; relation membership is canonical entity/schema state;
- apply explicit relation `order` values first in ascending order; resolve equal ordered values alphabetically by target name; place relations without `order` afterward in alphabetical target-name order; use canonical target ID as the final deterministic tie-breaker;
- use reader terminology appropriate to the domain rather than raw internal relation identifiers when those identifiers would be implementation jargon;
- preserve semantically distinct relations instead of collapsing producer, maintainer, operator, owner, membership, versioning, artifact, or derivative relations into one generic `Related` list;
- grouping, heading text, and placement may follow the page-template contract so long as they do not change canonical membership, `hidden`, or `order` semantics;
- omit the block when the page contract does not authorize relation presentation;
- when the block is authorized but no visible qualifying relation remains, omit it unless the applicable requirements explicitly define a meaningful empty state.

## Does Not Own

- whether the page requires a relation block;
- relation discovery, factual validation, target resolution, or inverse materialization;
- relation membership;
- endpoint-local `hidden` or `order` values;
- inverse-endpoint presentation controls.

The component consumes only the validated current-entity projection. It must not scan unrelated entities, infer reverse edges, repair missing inverses, or mutate canonical entity data.
