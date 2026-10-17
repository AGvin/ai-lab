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
