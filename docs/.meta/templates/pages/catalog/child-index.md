# Catalog Child Index Page

## Description

Typed navigation page for a parent's materialized children when the child relation itself is the page's primary meaning, such as Models, Versions, or Artifacts.

## Purpose

Answer: "Which represented children of this specific type exist under this parent, and where do I inspect each one?"

## Use When

Use for structural identity indexes such as a series' `models/`, a model's `versions/`, or a model's `artifacts/` node.

## Do Not Use When

Do not use for broad conceptual categories, domain roots, alphabetical partitions, or entity profiles that own facts beyond navigation.

## Owns

- minimal parent orientation;
- explanation of the child type when it is not obvious;
- navigation to implemented children of that type.

## Does Not Own

- parent profile facts;
- full child facts;
- speculative future children;
- parameter tables, recommendations, deployment guidance, or other detail owned by profile/selection pages.

## Expected Inputs

Requirement-approved title, canonical parent link/context, child-type meaning, and the explicit materialized child entries.

## Composition

1. default header;
2. one short parent-context statement;
3. child-type explanation only when needed;
4. `child-navigation` immediately as the primary reader action.

## Variants

`models`, `versions`, and `artifacts` are semantic variants of this one family. Their wording and child descriptions come from requirements; they do not justify separate templates by themselves.

## Representative Examples

- `.../qwen3/sub/models/`
- `.../qwen3-30b-a3b/sub/versions/`
- `.../huihui-qwen3-coder-30b-a3b-instruct-abliterated/sub/artifacts/`

## Anti-patterns

- re-describing the parent entity;
- presenting children that are not materialized;
- turning the index into a comparison table without a decision-support requirement;
- confusing a version or artifact child with a distinct trained-model identity.
