# Child Navigation Component

## Description

Reusable semantic navigation block for the current node's validated direct-child navigation projection.

## Purpose

Present materialized direct documentation children consistently when the applicable page requirements and template authorize child navigation, without duplicating child destinations in `.meta/requirements.md`.

## Inputs

The caller supplies the resolved current-node direct-child projection produced by the canonical documentation structure/navigation contract. Requirements authorize the child-navigation block or its reader-facing outcome as a whole; they do not individually approve child entries.

Each projected entry resolves to a canonical child destination and reader-facing label, with an optional short description and canonical semantic group/order when such navigation metadata is defined. The component does not derive membership from parent requirement lists or from the current rendered README.

## Rendering Rules

- include every eligible materialized direct documentation child in the standard projection;
- do not omit a projected child merely because the component independently judges it less useful;
- exclude non-navigation support paths such as `.meta/`, reader/control assets, localization mirrors, and control-only nodes before component rendering;
- preserve canonical semantic grouping and order when the navigation owner defines them;
- when no canonical grouping/order is defined, sort alphabetically by resolved reader-facing label and use canonical logical path as the deterministic tie-breaker;
- use descriptive reader-facing link text rather than raw paths or folder slugs;
- keep optional descriptions short and decision-relevant, using canonical child/navigation context rather than duplicated parent requirement wording;
- omit the block when the page contract does not authorize direct-child navigation;
- when the block is authorized but no eligible materialized direct child exists, omit it unless the applicable requirements explicitly define a meaningful empty state;
- a deliberately curated subset, cross-tree destination set, or recommendation list is not the standard direct-child projection and requires a separate canonical navigation contract.

## Does Not Own

- whether the page requires a child-navigation block;
- taxonomy classification or decisions about whether a child should exist;
- direct-child discovery rules or projection validation;
- child membership in the standard projection;
- canonical grouping or ordering rules;
- canonical entity facts, selection ranking, or cross-tree curated membership.

The component consumes only the validated current-node direct-child projection. It must not invent children from model memory, naming conventions, raw paths, requirement enumerations, or rendered prose.

## Anti-patterns

- enumerating or approving individual direct-child destinations in page requirements when the standard child-navigation block is intended;
- silently filtering eligible direct children inside the component;
- inventing children from model memory or naming conventions;
- flattening canonical meaningful groups into one list;
- copying detailed child profiles into navigation descriptions;
- using opaque labels such as `click here` or raw folder slugs when a canonical reader-facing label exists.
