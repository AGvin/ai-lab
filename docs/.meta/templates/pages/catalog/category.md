# Catalog Category Page

## Description

Reusable navigation page for a conceptual grouping inside a catalog domain.

## Purpose

Answer: "What unifies the items in this category, and which materialized child should I inspect?"

## Use When

Use when sibling children share one meaningful primary role, category, or reader-recognizable grouping. Physical depth does not matter.

## Do Not Use When

Do not use for domain roots, typed identity indexes such as `Versions` or `Artifacts`, alphabetical lookup partitions, or concrete entity profiles.

## Owns

- concise category definition;
- the organizing principle that makes the grouping useful;
- child-navigation placement and reader wording;
- a short scope clarification when nearby categories are easy to confuse.

## Does Not Own

- direct-child membership or ordering, which come from the validated current-node navigation projection;
- detailed child facts;
- exhaustive taxonomy explanation;
- comparisons or rankings unless the category itself is explicitly a decision-support page;
- repeated generic sections such as resources or relations when they do not help category navigation.

## Expected Inputs

Requirement-approved title, short category definition, authorization for the primary child-navigation block, the validated current-node direct-child projection, and optional scope clarification.

## Composition

1. default header;
2. short category definition;
3. one concise explanation of the grouping when necessary;
4. `child-navigation` as the primary action using the validated direct-child projection;
5. optional category-boundary clarification.

## Variants

Nested categories reuse this template when their reader job is unchanged. Create another template only when the nested page serves a materially different reader task.

## Representative Examples

- `docs/sub/catalog/sub/software/sub/inference-runtimes/`
- `docs/sub/catalog/sub/services/sub/development/`
- `docs/sub/catalog/sub/services/sub/development/sub/agents/`
- `docs/sub/catalog/sub/agent-skills/sub/collections/`

## Anti-patterns

- enumerating individual direct children in page requirements when the standard child-navigation block is intended;
- filtering direct children inside the template instead of using the canonical navigation projection;
- creating one template per taxonomy level;
- mixing unrelated organizing axes among siblings;
- adding boilerplate sections merely because entity metadata contains values;
- turning navigation descriptions into duplicated mini-profiles.
