# Redis Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Redis Agent Skills is Redis's official MIT-licensed collection of portable instructions for coding agents. The upstream repository covers Redis data structures, connections, search, semantic caching, clustering, security, observability and Iris development. These are instruction packages for working with Redis products, rather than a database deployment or a managed memory service. [Official collection](https://github.com/redis/agent-skills).

## Scope and operating boundaries

At the [inspected first-party revision](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/README.md), the collection lists **14 skills**: seven Redis topics (`redis-core`, `redis-connections`, `redis-search`, `redis-semantic-cache`, `redis-clustering`, `redis-security`, `redis-observability`), `redis-docs-mcp`, and six Iris integration skills (`add-redis-iris`, `add-agent-memory`, `add-agent-playbooks`, `add-context-gateway`, `add-intent-router`, `add-lens`). The earlier `iris-development` entry is not in the current inspected directory list. Counts and names are mutable, not enduring guarantees.

The documented portable installation is `npx skills add redis/agent-skills`; this does **not** install the Redis Docs MCP server. The Claude Code, ChatGPT/Codex and Cursor plugin packages can bundle the public, read-only server at `https://redis.io/mcp`. **Every MCP search/fetch/ask query sends its text to redis.io**. Avoid including confidential content or credentials in those queries; disable `redis-docs` in the client's MCP settings if data policy forbids this transmission. Read-only documentation retrieval is not database authorization, nor does it guarantee absence of transferred data.

Review the instructions and database actions before enabling them. A skill cannot grant a missing credential, provision a deployment merely by being installed or guarantee that every Redis feature is available in the selected server or cloud plan. The repository's MIT license applies to these resources; the database, hosted service and connected tools retain their own licenses and permissions. [Collection scope](https://github.com/redis/agent-skills).

## Produced by

- [Redis](../../../../../producers/sub/r/sub/redis/)

## Source interpretation

Redis's MIT collection provides Redis instruction resources and client plugin packaging. Client plugins include a public documentation MCP server; standalone Agent Skills CLI installation does not carry that MCP component. Documentation access requires no Redis credentials, while database commands still need scoped access and version-appropriate review.

[Reviewed original README](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Official collection](https://github.com/redis/agent-skills)
