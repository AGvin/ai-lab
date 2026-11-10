# Documentation Requirements

## Requirements

- Identify Cloudflare Skills as Cloudflare's official Agent Skills collection for building on Workers, Agents SDK, AI products, storage, networking, security, and the broader Cloudflare Developer Platform.
- Preserve the collection boundary rather than creating peer catalog identities for every skill/command; commands and skills remain content inside the official collection unless independently durable products exist elsewhere.
- Keep Cloudflare developer products, MCP servers, Workers templates, and the plugin marketplace packaging separate from the collection identity.
- Treat exact skill/command inventory, plugin installation routes, supported agent clients, repository structure, and skill contents as freshness-sensitive.
- Preserve three first-party README additions as collection-owned skill entries: `frameworks-on-cloudflare` (Cloudflare Workers framework integration), `cloudflare-app-bootstrap` (project bindings, secrets, initial data and local request validation) and `workers-development` (local debugging, traces and Local Explorer). The updated `cloudflare-one` also covers Cloudflare Access service tokens for non-browser agent clients.
- Local development is not necessarily confined to local resources: Cloudflare Workers bindings with `remote: true` can reach deployed services. Distinguish local/remote resources before data seeding, destructive tests or credentialed API operations, and review remote costs and permissions.
- Access service tokens are distinct from general Cloudflare API tokens. Require the application's `Service Auth` policy, use secrets storage, send credentials only to the authorized Access-protected hostname, and never paste, log, commit, or forward them across redirects.
- Distinguish native plugin routes that can bundle Cloudflare MCP from the standalone `npx skills add https://github.com/cloudflare/skills` instruction-only installation; neither route grants account permissions or authorizes a deployment.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Producer provenance resolves to Cloudflare.
- The collection is not conflated with Cloudflare Agents or Workers AI.

## Bounded upstream source reconciliation — 2026-11-09

- Compared [prior pinned index](https://github.com/cloudflare/skills/blob/1f2cd0a19588e2c6197c91dd7c71729df1fb6156/README.md) with the [newer official index](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/README.md): three new skills and a broader `cloudflare-one` scope. Confirmed the original [frameworks skill](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/frameworks-on-cloudflare/SKILL.md), [bootstrap skill](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/cloudflare-app-bootstrap/SKILL.md), [Workers development skill](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/workers-development/SKILL.md) and [Cloudflare One skill](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/cloudflare-one/SKILL.md). The root Apache-2.0 LICENSE blob was identical in both reviewed revisions.
- This is a bounded inventory and safe-use correction, not proof of full repository freshness, third-party rights clearance, installed compatibility, operational Access configuration, cloud deployments or independent security verification.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
