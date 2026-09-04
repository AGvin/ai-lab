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
- relation-block placement and reader wording when applicable requirements authorize relation presentation;
- collection-level purpose and organization;
- collection-level dependencies/runtime/tooling context when genuinely shared;
- navigation or inventory of represented skills/resources when requirements authorize it;
- authoritative collection resources and source paths.

## Does Not Own

- full documentation of each contained skill;
- standalone skill identity without independent publication evidence;
- duplicated producer profile facts;
- speculative skills not present in the reviewed collection;
- per-relation membership, visibility, or ordering, which come from the validated current entity projection.

## Expected Inputs

Requirement-approved collection title/orientation, collection scope, represented entries or source paths, shared runtime/dependency context, authoritative resources, and the validated current-entity relation projection when the page requirements call for the relation block.

## Composition

1. default header;
2. `entity-relations` when applicable requirements call for relation presentation;
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
- enumerating or approving individual relation targets in page requirements when the standard relation block is intended;
- filtering visible canonical relation entries inside the template instead of using entity `hidden` controls;
- presenting source-path details before explaining what the collection is.
