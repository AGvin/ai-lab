# Redis Agent Skills

Redis Agent Skills is Redis's official MIT-licensed collection of portable instructions for coding agents. The upstream repository covers Redis data structures, connections, search, semantic caching, clustering, security, observability and Iris development. These are instruction packages for working with Redis products, rather than a database deployment or a managed memory service. [Official collection](https://github.com/redis/agent-skills).

## Scope and operating boundaries

The current collection contains `redis-core`, `redis-connections`, `redis-search`, `redis-semantic-cache`, `redis-clustering`, `redis-security`, `redis-observability` and `iris-development`. The documented portable installation is `npx skills add redis/agent-skills`; client-specific plugin packaging has its own installation requirements. Pin the selected revision and confirm that the intended client supports the relevant package. [Inventory and installation](https://github.com/redis/agent-skills).

Review the instructions and database actions before enabling them. A skill cannot grant a missing credential, provision a deployment merely by being installed or guarantee that every Redis feature is available in the selected server or cloud plan. The repository's MIT license applies to these resources; the database, hosted service and connected tools retain their own licenses and permissions. [Collection scope](https://github.com/redis/agent-skills).

## Produced by

- [Redis](../../../../../producers/sub/r/sub/redis/)

## Official resources

- [Official collection](https://github.com/redis/agent-skills)
