# Documentation Requirements

## Requirements

- Identify Vercel Agent Skills as Vercel's official repository-backed collection of Agent Skills for AI coding agents.
- Preserve the collection boundary rather than materializing every contained skill as a peer canonical entity unless a later intake establishes independent durable identity and material value.
- Keep the current skill inventory, discovery index, immutable release artifacts, installation commands, scripts/references, and compatibility with Agent Skills hosts freshness-sensitive.
- Preserve current repository-defined workflows such as Vercel optimization/deployment and React/web/design/writing guidance as collection inventory rather than a permanent exhaustive list.
- Keep the separate `skills`/skills.sh registry tooling, Vercel AI SDK, Vercel Connect, AI Gateway, hosting platform, and product docs with their own canonical identities.
- Preserve trust boundaries for skills that can deploy projects, inspect metrics, modify code, or transmit project content: installation does not itself authorize external writes or data transfer.
- Preserve repository licensing and first-party status without treating publication as a blanket quality/security endorsement.
- For `deploy-to-vercel`, distinguish Git-triggered production deployments from the preview default, project/team linking, and no-login `vercel deploy --temporary` uploads with sensitive claim URLs. Require explicit authorization and source/secrets review before remote writes.
- For `vercel-cli-with-tokens`, warn that the pinned source's token-discovery examples print `VERCEL_TOKEN` or `.env` values; never expose live credentials in agent-visible output, shell history or tracked files, and use scoped secret storage and rotation.

## Validation

- The entity remains a skill collection rather than the skills.sh registry or the Vercel platform.
- Producer provenance resolves to Vercel Inc.
- Mutable skill counts and contained workflows are not frozen from one repository snapshot.
- Individual skill directories are not automatically duplicated as standalone canonical entities.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
