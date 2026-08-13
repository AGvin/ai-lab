# Catalog Domain Page

## Description

Landing page for one canonical catalog domain such as Software, Services, Producers, Agent Skills, Hardware, or Datasets.

## Purpose

Answer: "What belongs to this domain, what does not, and where should I go next?"

## Use When

Use for a domain root whose main reader job is ownership orientation plus navigation to its primary categories or indexes.

## Do Not Use When

Do not use for the overall Catalog landing, a conceptual subcategory, a lookup-only alphabetical partition, or a concrete entity profile.

## Owns

- concise definition of the domain;
- its canonical ownership boundary;
- navigation to materialized direct areas;
- minimal cross-domain links needed to resolve common classification ambiguity.

## Does Not Own

- detailed child profiles;
- exhaustive descendant trees;
- facts owned by another catalog domain;
- recommendation or workflow guidance merely related to the domain.

## Expected Inputs

Requirement-approved title, short domain orientation, ownership-boundary explanation, materialized primary destinations, and optional boundary links.

## Composition

1. default header;
2. concise domain orientation;
3. ownership boundary in normal page prose;
4. primary navigation through `child-navigation`;
5. optional adjacent-domain clarification only when useful.

## Variants

A thin domain with no concrete entities still uses this template. It should honestly explain its scope without rendering empty sections or claiming nonexistent coverage.

## Representative Examples

- `docs/sub/catalog/sub/software/`
- `docs/sub/catalog/sub/services/`
- `docs/sub/catalog/sub/producers/`
- `docs/sub/catalog/sub/datasets/`
- `docs/sub/catalog/sub/hardware/`

## Anti-patterns

- treating physical depth as a reason to invent another template;
- listing every descendant instead of the domain's primary navigation;
- hiding classification boundaries until the bottom of the page;
- filling thin domains with speculative placeholder content.
