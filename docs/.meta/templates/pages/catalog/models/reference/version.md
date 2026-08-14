# Model Version Page

## Description

Canonical profile for one chronological release, revision, or checkpoint that retains the same concrete-model identity.

## Purpose

Show what changed in this release relative to the parent model without duplicating the complete model profile.

## Use When

Use for represented revisions such as an initial release or a dated update like `2507`.

## Do Not Use When

Do not use when the child is actually a different parameter-size model, family/series, hosted alias, or artifact package.

## Owns

- version/release identity;
- canonical `version-of` orientation;
- release-specific naming, behavior, context, capability, or source changes;
- release-specific authoritative references;
- explicit source-coverage limitations when facts are incomplete.

## Does Not Own

- unchanged model-wide architecture and parameter facts;
- generic family/series capabilities;
- artifact packaging/quantization;
- selection or deployment conclusions.

## Expected Inputs

Requirement-approved release title/orientation, parent model relation, supported release-specific delta, authoritative release resources, and any source-coverage boundary.

## Composition

1. default header;
2. parent model relation;
3. concise release identity;
4. release-specific changes/delta;
5. evidence or source-coverage boundary when material;
6. sibling/version-index navigation when useful;
7. `official-resources`.

## Variants

A release with very small delta remains concise. A richer release may have multiple delta sections, but unchanged parent facts are linked rather than copied.

## Representative Example

- Qwen3 30B-A3B Instruct 2507.

## Anti-patterns

- presenting a revision as a different concrete model without identity evidence;
- restating the full parent profile;
- inventing exact values when the release source only supports qualitative change.
