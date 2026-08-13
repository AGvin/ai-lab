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
- producer/project relations when useful;
- ecosystem and compatibility relations when requirements authorize them;
- authoritative software resources;
- concise usage orientation sufficient to route readers to deeper setup/operations content.

## Does Not Own

- hosted-service state that belongs to a service entity;
- long step-by-step installation/configuration tutorials unless the architecture explicitly assigns them here;
- universal comparisons or selection conclusions;
- duplicated model/dataset/hardware facts.

## Expected Inputs

Requirement-approved title/orientation, canonical identity and relations, stable role/capability facts, important interfaces/integrations/compatibility boundaries, and authoritative resources.

## Composition

1. default header;
2. concise software identity and role;
3. producer/project relation when useful;
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
- turning the profile into a long setup tutorial by default.
