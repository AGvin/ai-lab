# Cloudflare Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Cloudflare Skills is Cloudflare's official Agent Skills collection for building on Workers, Agents SDK, AI products, storage, networking, security, and the broader Cloudflare Developer Platform.

## Producer

- [Cloudflare](../../../../../producers/sub/c/sub/cloudflare/)

## Collection boundary

Skills and commands remain content inside the collection rather than peer catalog identities. Cloudflare developer products, MCP servers, Workers templates, and plugin-marketplace packaging remain separate from the collection identity.

Exact skill and command inventory, plugin installation routes, supported agent clients, repository structure, and skill contents are freshness-sensitive.

## Newly documented skills and safe-use boundaries

Relative to the previously reviewed index, the [newer first-party README](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/README.md) adds:

- [`frameworks-on-cloudflare`](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/frameworks-on-cloudflare/SKILL.md) — routes Astro, SvelteKit, React Router, TanStack Start, Nuxt, Hono and SPA projects to Workers integrations. Existing Pages deployments and framework choices require contextual review.
- [`cloudflare-app-bootstrap`](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/cloudflare-app-bootstrap/SKILL.md) — configures bindings, initial data and local requests; runtime secrets must not enter public browser bundles, repository commits or logs.
- [`workers-development`](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/workers-development/SKILL.md) — uses local dev, logs, traces and Local Explorer. **Local execution can still contact live resources** when a binding has `remote: true`, so verify the actual resource scope before any write or seeding operation.

The expanded [`cloudflare-one` source](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/skills/cloudflare-one/SKILL.md) covers **Cloudflare Access service tokens** for non-browser/agent clients. Keep Access client credentials separate from Cloudflare API tokens, restricted to authorized Service Auth policies, secure storage and the intended hostname; never forward them through cross-origin redirects.

Native client plugins may bundle the Cloudflare MCP integration, whereas `npx skills add https://github.com/cloudflare/skills` installs Agent Skills instructions without that connection. Neither method grants cloud credentials, permission to alter resources, or proof of safe deployment.

## Source interpretation

Cloudflare publishes platform guidance for Workers, Agents SDK and related developer products under Apache-2.0. Native client plugins can bundle the Cloudflare MCP integration, while standalone skills are instruction files. Neither installing guidance nor a plugin supplies blanket authority to inspect an account, deploy Workers or modify resources.

[Reviewed original README](https://github.com/cloudflare/skills/blob/6eb6c781aa9b6438e0c7307bd102788a75fe1a6d/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Cloudflare Skills repository](https://github.com/cloudflare/skills)
