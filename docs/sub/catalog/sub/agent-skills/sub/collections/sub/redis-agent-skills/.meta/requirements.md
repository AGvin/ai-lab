# Documentation Requirements

## Requirements

- Identify Redis Agent Skills as Redis's official maintained collection of portable Agent Skills packages for AI coding agents working with Redis data structures, search, vector retrieval, caching, production operations and Iris/Redis Agent Memory development.
- Preserve the first-party collection as **one independent identity** owned by the `redis/agent-skills` repository. At the inspected upstream revision, its skill inventory contains fourteen directories: seven core Redis topics (`redis-core`, `redis-connections`, `redis-search`, `redis-semantic-cache`, `redis-clustering`, `redis-security`, `redis-observability`), `redis-docs-mcp`, and six Iris integrations (`add-redis-iris`, `add-agent-memory`, `add-agent-playbooks`, `add-context-gateway`, `add-intent-router`, `add-lens`). This supersedes the stale eight-skill list including `iris-development`; never turn directory names into peer collection identities.
- Distinguish Redis Agent Skills instruction packages from the Redis database/software, Redis Search and vector indexing capabilities, the separately cataloged Redis Agent Memory service, language SDKs, MCP integrations and plugin distribution packaging. An instruction package does not itself provision a Redis deployment or authorize database access.
- Document the Agent Skills format and first-party installation path (`npx skills add redis/agent-skills`) without claiming that a selected client automatically supports all bundled skills. Claude Code, Cursor and ChatGPT/Codex plugin distributions have distinct packaging and installation requirements.
- Treat current inventory, package locations, installation commands, compatibility, client versions, evaluation behavior, default security settings and Redis feature support as mutable source-owned facts.
- Distinguish local Agent Skills CLI installation (no MCP server) from Claude Code, ChatGPT/Codex and Cursor plugin packages that bundle the public, read-only Redis Docs MCP server at `https://redis.io/mcp`. The vendor states that each remote MCP `search`, `fetch` or `ask` call sends the query text to redis.io, even when no Redis credentials are required; warn against sending confidential content and explain that the server can be disabled at the client MCP configuration.
- Preserve first-party Redis producer attribution and reciprocal `produced-by` / `produces` relations.

## Validation

- Official `https://github.com/redis/agent-skills` still identifies Redis as the collection owner and contains genuine `SKILL.md` packages.
- Collection identity is independent of the already materialized Redis Agent Memory managed service; generated plugin mirrors and individual skills are not duplicated as canonical collections.
- Supported runtime/client compatibility and permissions are not inferred from a repository's installation examples alone.
- The Redis collection `produced-by` link and Redis producer inverse `produces` link resolve to canonical materialized IDs.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Redis Agent Skills is Redis's official MIT-licensed collection of portable instructions for coding agents. The upstream repository covers Redis data structures, connections, search, semantic caching, clustering, security, observability and Iris development. These are instruction packages for working with Redis products, rather than a database deployment or a managed memory service. [Official collection](https://github.com/redis/agent-skills).

The [first-party inventory at the inspected revision](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/README.md) has fourteen skills: seven Redis core topics, `redis-docs-mcp` and six `add-*` Iris integrations. The old `iris-development` title must not be presented as a current directory. Portable installation uses `npx skills add redis/agent-skills`, without bundled MCP; official plugin packages can include the Redis Docs MCP connection. Confirm current inventory and client-specific installation before deployment.

Review the instructions and database actions before enabling them. A skill cannot grant a missing credential, provision a deployment merely by being installed or guarantee that every Redis feature is available in the selected server or cloud plan. The repository's MIT license applies to these resources; the database, hosted service and connected tools retain their own licenses and permissions. [Collection scope](https://github.com/redis/agent-skills).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.

## Redis inventory and MCP disclosure reconciliation — 2026-11-08

- Confirmed the [pinned first-party Redis README](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/README.md) and its [`redis-docs-mcp` source](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/redis-docs-mcp/SKILL.md): 14 direct skills rather than the old eight, and query text goes to redis.io on MCP calls. The MIT repository license remains separate from Redis services or transmitted text.
- This bounded correction does not represent complete dependency inspection, audited client/plugin installation, privacy compliance assessment, live Redis access or independently verified runtime compatibility.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.

## Complete selected-source freshness — 2026-11-10

The entire first-party Git tree at `74708dab4b3f81a9845803c3f642a4f7d443af69` matches current upstream HEAD: **203 identical tracked file blobs**, including source skills, plugin mirrors, scripts, evaluation material and manifests. No path or blob drift was found. This inventories the complete selected repository, not the separately installed Redis products, remote MCP contents, npm packages or live runtime behavior. Detailed script/dependency, permission/data-flow, rights and independent full-profile review remain open.
