# Documentation Requirements

## Requirements

- Identify Docker Skills as Docker's official first-party Agent Skills collection of portable `SKILL.md` guidance for building, containerizing, debugging, securing, and operating Docker applications and Docker Agent workflows.
- Treat official release/tag snapshots and the rolling main-branch skill catalog distinctly. Do not claim all skill contents or supported clients remain constant across releases.
- Preserve collection-level identity rather than materializing a new canonical entity for every skill; Dockerfile, Compose, Agent and Sandboxes skill groups are collection-owned content.
- Keep Docker CLI/engine tools, Docker Agent runtime, container registry, plugin distribution, MCP servers, agent-client install paths and external marketplace releases separate from this guidance collection.
- Verify source authenticity, workflow safety, current product support, required host tooling and destructive-action guardrails before offering runnable operational instructions; skill documentation does not replace validation or approval.
- Attribute Docker-owned collection provenance to the canonical Docker producer.

## Source-specific data and operation boundaries

- Explain that Docker CLI/manual/sandbox skill installation does not itself register a remote MCP, while plugin/extension installation additionally configures the hosted Docker Docs MCP endpoint `https://ai-backend-service.docker.com/mcp`. Describe network queries as remote data flow, not local-only execution.
- State that Docker Agent network serving requires reviewed listener exposure and authentication; `--insecure-no-auth` must not be treated as a default. Distinguish serve modes with and without `--safety`, and evaluate authorization before pushing an agent to an OCI registry because `instruction_file` text is inlined.
- Distinguish reversible stopping from irreversible deletion. Review explicit Docker resource targets and data-loss impact before cleanup such as `docker system prune`, `docker compose down -v` or `docker volume prune`; follow source-specific confirmation exceptions, not a blanket deletion entitlement.
- Ground these warnings in the pinned original [installation guidance](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/README.md), [agent deployment skill](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/skills/docker-agent-deploy/SKILL.md) and [destructive-command guardrail](https://github.com/docker/skills/blob/9f04a05d5fcdbfac0f6088bc711e930a75896482/skills/docker-destructive-guardrails/SKILL.md). A bounded documentation review is not installation/runtime/retention/privacy verification.

## Validation

- The first-party curated/produced collection resolves through the named producer without erasing upstream authorship.
- The current collection/release inventory and install compatibility are source-backed rather than assumed permanent.
- Bundled skill directories are not duplicated as canonical peers merely for enumeration.
- The inverse `produces` relation matches the collection's `produced-by` relation.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
