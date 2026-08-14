# Agent Skill Collection Page

## Description

Canonical profile for a published or curated collection of Agent Skills.

## Purpose

Explain what the collection is, who publishes or maintains it, what scope it covers, and how readers reach the useful skills/resources without treating the collection as one individual skill.

## Use When

Use for collection entities under `catalog/agent-skills/collections/`.

## Do Not Use When

Do not use for an independently published single skill, a generic Agent Skills domain/category page, or a producer profile.

## Owns

- collection identity and scope;
- producer/publisher relation;
- collection-level purpose and organization;
- collection-level dependencies/runtime/tooling context when genuinely shared;
- navigation or inventory of represented skills/resources when requirements authorize it;
- authoritative collection resources and source paths.

## Does Not Own

- full documentation of each contained skill;
- standalone skill identity without independent publication evidence;
- duplicated producer profile facts;
- speculative skills not present in the reviewed collection.

## Expected Inputs

Requirement-approved collection title/orientation, producer/publisher relation, collection scope, represented entries or source paths, shared runtime/dependency context, and authoritative resources.

## Composition

1. default header;
2. producer/publisher relation;
3. concise collection purpose/scope;
4. represented skills/resources or grouped navigation;
5. shared dependencies/runtime/tooling only when collection-wide;
6. `official-resources`.

## Variants

Collections with richer internal structure may use grouped navigation; small collections remain concise. Differences in publisher ecosystem do not by themselves require new templates.

## Representative Examples

- Anthropic Skills;
- Matt Pocock Skills;
- NVIDIA Skills;
- OpenAI Skills;
- Superpowers.

## Anti-patterns

- materializing collection-owned skills as standalone entities without evidence;
- copying every skill's full documentation into the collection page;
- presenting source-path details before explaining what the collection is.
