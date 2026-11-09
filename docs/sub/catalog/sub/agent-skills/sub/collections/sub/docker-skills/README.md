# Docker Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Collection

Docker-authored portable instruction directories cover container build, Compose and operational workflows. Apache-2.0 covers the repository; CLI/Engine, Agent/Sandboxes and connected registries retain separate runtime and service boundaries. Pin an inspected release, check client tooling and review image/build scripts before operations that alter containers or volumes.

## Remote documentation and operational safety

Docker's pinned [installation guide](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/README.md) distinguishes skill-only installation from plugin or extension installation. Docker's plugin and extension paths also register the **hosted Docker Docs MCP server** at `https://ai-backend-service.docker.com/mcp`; the `npx skills` CLI, Docker Sandboxes skill installer and manual copies install skills without that MCP registration. Documentation queries sent through the hosted MCP are external requests, not offline local lookups. Confirm the selected client, network/data-sharing permissions and exact installation method before enabling the connection; installing an instruction package alone does not grant Docker Engine access.

The original [Docker Agent deployment skill](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/skills/docker-agent-deploy/SKILL.md) covers network listeners and OCI publication. Its server modes default to loopback (or stdio for MCP), but any externally reachable listener needs appropriate authentication, restricted access and an explicitly reviewed safety setting where supported; do not use unauthenticated overrides as an implicit deployment default. OCI sharing inlines referenced `instruction_file` content in the published artifact, so review for internal or secret-bearing instructions before pushing to a registry. The [destructive-command guardrail](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/skills/docker-destructive-guardrails/SKILL.md) separately requires an identified deletion scope and user approval before irreversible volume, image, cache, container or network cleanup, subject only to its narrow own-session test-container exception. No live Docker runtime, network service, MCP request or registry publication was tested here.

## Producer

- [Producer](../../../../../producers/sub/d/sub/docker/)

[Reviewed original README](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/README.md). No installation or execution was performed.

## Official resources

- <https://github.com/docker/skills>
