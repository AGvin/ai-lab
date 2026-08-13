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
- child navigation;
- a short scope clarification when nearby categories are easy to confuse.

## Does Not Own

- detailed child facts;
- exhaustive taxonomy explanation;
- comparisons or rankings unless the category itself is explicitly a decision-support page;
- repeated generic sections such as resources or relations when they do not help category navigation.

## Expected Inputs

Requirement-approved title, short category definition, materialized child destinations with useful descriptions, and optional scope clarification.

## Composition

1. default header;
2. short category definition;
3. one concise explanation of the grouping when necessary;
4. `child-navigation` as the primary action;
5. optional category-boundary clarification.

## Variants

Nested categories reuse this template when their reader job is unchanged. Create another template only when the nested page serves a materially different reader task.

## Representative Examples

- `docs/sub/catalog/sub/software/sub/inference-runtimes/`
- `docs/sub/catalog/sub/services/sub/development/`
- `docs/sub/catalog/sub/services/sub/development/sub/agents/`
- `docs/sub/catalog/sub/agent-skills/sub/collections/`

## Anti-patterns

- creating one template per taxonomy level;
- mixing unrelated organizing axes among siblings;
- adding boilerplate sections merely because entity metadata contains values;
- turning navigation descriptions into duplicated mini-profiles.
