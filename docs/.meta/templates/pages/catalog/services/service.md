# Service Profile Page

## Description

Canonical profile for one hosted or externally operated product whose primary identity is a service.

## Purpose

Explain what the service is, who operates it, how readers access or use it at a high level, and where its service-specific capabilities and constraints belong.

## Use When

Use for concrete entities under `catalog/services/` whose primary canonical identity is hosted or externally operated.

## Do Not Use When

Do not use for installable/self-managed software, intrinsic model identity, producer profiles, or detailed procedural setup guides.

## Owns

- service identity and stable purpose/access model;
- relation-block placement and reader wording when applicable requirements authorize relation presentation;
- service-specific capabilities, interfaces, and boundaries when source-backed;
- service-specific authoritative resources;
- mutable state only when requirements explicitly scope and date it.

## Does Not Own

- intrinsic model facts already owned by Model Reference;
- installable software identity merely because the service exposes software-like interfaces;
- durable duplication of mutable pricing, limits, availability, or terms without freshness requirements;
- complete procedural tutorials better owned by workflow/setup documentation;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved display values, stable service description, access/interface context, explicit mutable-state boundaries, authoritative resources, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. `entity-relations` when applicable requirements call for relation presentation;
3. concise service identity and primary purpose;
4. access/interface orientation;
5. capabilities and service-specific boundaries;
6. mutable-state caveats when required;
7. `official-resources`.

## Variants

Hosted development agents, model APIs, infrastructure services, and AI-asset services reuse this family when they share the hosted-service reader job. Detailed operational procedures may link outward.

## Representative Examples

- Devin;
- other materialized hosted service profiles.

## Anti-patterns

- classifying self-managed software as a service solely because hosted access exists;
- copying model architecture/specs into a provider page;
- enumerating or approving individual relation targets in page requirements when the standard relation block is intended;
- filtering visible canonical relation entries inside the template instead of using entity `hidden` controls;
- presenting mutable pricing or availability as timeless fact.
