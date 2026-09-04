# Software Profile Page

## Description

Canonical profile for one installable or self-managed software product, library, framework, runtime, application, or platform.

## Purpose

Help readers understand what the software is, its primary role, relevant capabilities and interfaces, ecosystem relationships, and where to continue for practical usage.

## Use When

Use for concrete entities under `catalog/software/` whose canonical identity is installable or self-managed software.

## Do Not Use When

Do not use for hosted-only services, model identities, producer profiles, generic software categories, or full procedural installation guides.

## Owns

- software identity and primary role;
- stable capability/interface overview;
- relation-block placement and reader wording when applicable requirements authorize relation presentation;
- authoritative software resources;
- concise usage orientation sufficient to route readers to deeper setup/operations content.

## Does Not Own

- hosted-service state that belongs to a service entity;
- long step-by-step installation/configuration tutorials unless the architecture explicitly assigns them here;
- universal comparisons or selection conclusions;
- duplicated model/dataset/hardware facts;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved title/orientation, canonical software identity, stable role/capability facts, important interfaces/integrations/compatibility boundaries, authoritative resources, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. concise software identity and role;
3. `entity-relations` when applicable requirements call for relation presentation;
4. capability and interface overview;
5. important compatibility/ecosystem boundaries;
6. clear next-step links for setup, usage, or related services when materialized elsewhere;
7. `official-resources`.

## Variants

Frameworks, runtimes, libraries, developer tools, interfaces, gateways, and platforms reuse this family while the reader goal remains a canonical software profile. Richer operational details are requirements-driven and should not force empty generic sections across all software.

## Representative Examples

- Ollama;
- LangChain;
- LangGraph;
- CrewAI;
- OpenAI Agents SDK.

## Anti-patterns

- using one generic `catalog/item` contract that erases software-specific reader expectations;
- mixing hosted-only mutable service behavior into the stable software profile;
- enumerating or approving individual relation targets in page requirements when the standard relation block is intended;
- filtering visible canonical relation entries inside the template instead of using entity `hidden` controls;
- turning the profile into a long setup tutorial by default.
