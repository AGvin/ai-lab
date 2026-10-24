# Documentation Requirements

## Requirements

- Identify Redis Agent Skills as Redis's official maintained collection of portable Agent Skills packages for AI coding agents working with Redis data structures, search, vector retrieval, caching, production operations and Iris/Redis Agent Memory development.
- Preserve the first-party collection as **one independent identity** owned by the `redis/agent-skills` repository. The upstream currently groups the `redis-core`, `redis-connections`, `redis-search`, `redis-semantic-cache`, `redis-clustering`, `redis-security`, `redis-observability` and `iris-development` skills; avoid treating these individual directories as peer collection entities.
- Distinguish Redis Agent Skills instruction packages from the Redis database/software, Redis Search and vector indexing capabilities, the separately cataloged Redis Agent Memory service, language SDKs, MCP integrations and plugin distribution packaging. An instruction package does not itself provision a Redis deployment or authorize database access.
- Document the Agent Skills format and first-party installation path (`npx skills add redis/agent-skills`) without claiming that a selected client automatically supports all bundled skills. Claude Code, Cursor and ChatGPT/Codex plugin distributions have distinct packaging and installation requirements.
- Treat current inventory, package locations, installation commands, compatibility, client versions, evaluation behavior, default security settings and Redis feature support as mutable source-owned facts.
- Preserve first-party Redis producer attribution and reciprocal `produced-by` / `produces` relations.

## Validation

- Official `https://github.com/redis/agent-skills` still identifies Redis as the collection owner and contains genuine `SKILL.md` packages.
- Collection identity is independent of the already materialized Redis Agent Memory managed service; generated plugin mirrors and individual skills are not duplicated as canonical collections.
- Supported runtime/client compatibility and permissions are not inferred from a repository's installation examples alone.
- The Redis collection `produced-by` link and Redis producer inverse `produces` link resolve to canonical materialized IDs.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Redis Agent Skills is Redis's official MIT-licensed collection of portable instructions for coding agents. The upstream repository covers Redis data structures, connections, search, semantic caching, clustering, security, observability and Iris development. These are instruction packages for working with Redis products, rather than a database deployment or a managed memory service. [Official collection](https://github.com/redis/agent-skills).

The current collection contains `redis-core`, `redis-connections`, `redis-search`, `redis-semantic-cache`, `redis-clustering`, `redis-security`, `redis-observability` and `iris-development`. The documented portable installation is `npx skills add redis/agent-skills`; client-specific plugin packaging has its own installation requirements. Pin the selected revision and confirm that the intended client supports the relevant package. [Inventory and installation](https://github.com/redis/agent-skills).

Review the instructions and database actions before enabling them. A skill cannot grant a missing credential, provision a deployment merely by being installed or guarantee that every Redis feature is available in the selected server or cloud plan. The repository's MIT license applies to these resources; the database, hosted service and connected tools retain their own licenses and permissions. [Collection scope](https://github.com/redis/agent-skills).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
