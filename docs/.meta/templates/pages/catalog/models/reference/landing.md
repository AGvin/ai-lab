# Model Reference Landing Page

## Description

Entry page for authoritative factual model documentation.

## Purpose

Orient readers to the canonical model identity chain and make clear where different kinds of model facts belong.

## Use When

Use for `catalog/models/reference/`.

## Do Not Use When

Do not use for the broader Models landing, Model Selection, a producer view, or any concrete model identity page.

## Owns

- explanation of factual-reference scope;
- the family -> optional series -> model -> version/artifact identity boundary;
- distinction between producer ownership, provider access, and hosted-service concerns;
- child-navigation placement and reader wording for materialized direct reference indexes.

## Does Not Own

- direct-child membership or ordering, which come from the validated current-node navigation projection;
- model recommendations or rankings;
- complete descendant enumeration when a child index owns it;
- provider-side mutable capabilities presented as intrinsic model facts.

## Expected Inputs

Requirement-approved reference orientation, identity-level explanation, authorization for the primary child-navigation block, the validated current-node direct-child projection, and boundary links when needed.

## Composition

1. default header;
2. concise factual-reference orientation;
3. identity-chain explanation using reader terminology;
4. primary `child-navigation` to materialized direct reference indexes using the validated direct-child projection;
5. short provider/service boundary note where useful.

## Variants

The identity chain may omit the optional series level for some families; the template must describe this without implying that every branch uses identical depth.

## Representative Example

- `docs/sub/catalog/sub/models/sub/reference/`

## Anti-patterns

- enumerating direct reference indexes in page requirements when the standard child-navigation block is intended;
- filtering direct reference indexes inside the template instead of using the canonical navigation projection;
- implying every family has a series layer;
- embedding selection advice;
- treating hosted provider features as inherent weight/model properties.
