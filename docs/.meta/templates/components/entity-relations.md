# Entity Relations Component

## Description

Reusable block for a small, explicit set of reader-relevant semantic relationships such as canonical producer, parent family, parent series, version-of, artifact-of, or related canonical owner.

## Purpose

Expose relationships that materially help a reader orient the current entity without dumping the complete internal relation graph.

## Inputs

The caller supplies requirement-approved relation entries with a reader-facing relation label, target label, and canonical destination.

## Rendering Rules

- render only relationships useful to the page's reader journey;
- use reader terminology appropriate to the domain rather than raw internal relation identifiers when the identifiers would be implementation jargon;
- keep canonical ownership links near the orientation portion of profile pages when they materially answer "what does this belong to?";
- preserve semantically distinct relations instead of collapsing producer, publisher, provider, family membership, versioning, and artifact derivation into one generic `Related` list;
- omit the block when no relation is required by the page contract.

## Does Not Own

The component does not discover, validate, infer, or mutate entity relations. Canonical relation semantics remain owned by entity metadata and applicable requirements.
