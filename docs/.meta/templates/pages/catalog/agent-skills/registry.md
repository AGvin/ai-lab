# Agent Skill Registry Page

## Description

Canonical profile for an Agent Skills registry, directory, marketplace, discovery index, or installer-backed aggregation service.

## Purpose

Explain what the registry is, what sources or skills it indexes or distributes, how discovery and installation work, and which mutable trust, ranking, telemetry, compatibility, or governance behaviors readers should verify before use.

## Use When

Use for registry entities under `catalog/agent-skills/registries/` whose primary role is discovering, indexing, ranking, scanning, distributing, or installing skills from multiple independent sources.

## Do Not Use When

Do not use for a publisher-owned Agent Skill collection, an independently published single skill, the abstract Agent Skills concept, or a generic software/service profile whose primary identity is not an Agent Skills registry.

## Owns

- registry identity and scope;
- discovery, indexing, aggregation, ranking, marketplace, or distribution behavior;
- installation interfaces when they are part of the registry product;
- supported clients/agents when current and source-backed;
- registry-specific scanning, trust, provenance, telemetry, and governance features;
- authoritative registry resources and source/repository links;
- freshness boundaries for mutable registry behavior.

## Does Not Own

- generic third-party skill trust guidance;
- portable Agent Skills authoring or maintenance guidance;
- duplicated profiles for every indexed skill or collection;
- immutable claims about volatile inventory, popularity, client support, ranking, scanning, or CLI behavior without current evidence;
- collection-specific content that belongs to `catalog/agent-skills/collections/`.

## Expected Inputs

Requirement-approved registry title/orientation, registry scope and source model, discovery/distribution/install behavior, source-backed mutable operational facts with freshness boundaries, and authoritative resources.

## Composition

1. default header;
2. concise registry identity and scope;
3. discovery/index/marketplace behavior;
4. installation or distribution workflow when applicable;
5. supported clients and operational behavior when current and relevant;
6. trust/security/telemetry/governance characteristics with appropriate caveats;
7. freshness-sensitive limitations;
8. `official-resources`.

## Variants

A registry may be primarily a public index, marketplace, CLI-backed installer, governance service, or multi-source aggregator. These differences belong in page requirements and do not require separate templates by default.

## Representative Examples

- skills.sh;
- agentskills.codes;
- AgentSkills.to;
- GuildSkills;
- SkillsRegistry.net;
- SkillHub.

## Anti-patterns

- using the Agent Skill collection template for a registry;
- treating registry presence or scanning as proof of trustworthiness;
- copying the registry's complete volatile inventory into the page;
- turning every indexed skill into a duplicated canonical entity;
- presenting mutable rankings, client support, commands, or telemetry behavior without a freshness boundary.
