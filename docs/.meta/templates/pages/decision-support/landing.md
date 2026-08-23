# Decision Support Landing Page

## Description

Reusable landing page for the top-level decision-support domain.

## Purpose

Orient readers to selected decision journeys without turning the domain into a duplicate catalog, evidence store, or catch-all recommendation index.

## Use When

Use for the canonical `decision-support/` root.

## Do Not Use When

Do not use for a concrete user scenario, an audience-group scenario index, a canonical catalog entity, or a model-specific decision guide.

## Owns

- concise decision-support orientation;
- the boundary between decision journeys and canonical entity ownership;
- placement of validated child navigation.

## Does Not Own

- the direct-child set or ordering outside validated navigation inputs;
- canonical entity facts;
- detailed scenario recommendations;
- evidence, concepts, implementation guidance, or risk/governance content owned elsewhere.

## Expected Inputs

- applicable requirements;
- validated direct-child projection.

## Composition

1. standard header/orientation;
2. concise scope and ownership boundary;
3. child navigation for materialized selected journeys.

## Variants

None currently required.

## Representative Examples

- `docs/sub/decision-support/`

## Anti-Patterns

- materializing unresolved decision-support branches merely because the parent exists;
- duplicating canonical catalog profiles;
- presenting the root as a universal recommendation page;
- inventing children or recommendations not authorized by canonical inputs.
