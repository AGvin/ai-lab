# Redis

Redis is the first-party producer behind the represented Redis Agent Memory service and Redis Agent Skills collection. Current documentation places Agent Memory within the broader Iris context engine and provides a managed Redis Cloud service, while the official skills repository distributes portable instructions for coding agents. [Agent Memory](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/) · [Agent Skills](https://github.com/redis/agent-skills).

## Scope and operating boundaries

The service and instructions have different deployment and licensing boundaries. Redis Cloud Agent Memory is managed; its Redis Software deployment remains a private preview. The original Agent Memory Server is preserved as a V0 research artifact rather than the supported production distribution. [Deployment documentation](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/) · [Server repository](https://github.com/redis/agent-memory-server).

The skills collection declares MIT licensing, but this neither licenses all Redis products nor provisions a database or grants access to stored memories. Review the selected database, model configuration and skill-requested actions at their own scopes. [Agent Skills](https://github.com/redis/agent-skills) · [Cloud service guide](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/).

## Produces

- [Redis Agent Memory](../../../../../services/sub/data-infrastructure/sub/memory-and-context/sub/redis-agent-memory/)
- [Redis Agent Skills](../../../../../agent-skills/sub/collections/sub/redis-agent-skills/)

## Official resources

- [Official website](https://redis.io/)
- [Documentation](https://redis.io/docs/)
- [Agent Memory](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/)
- [Cloud service guide](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/)
- [Agent Skills](https://github.com/redis/agent-skills)
- [Agent Memory Server history](https://github.com/redis/agent-memory-server)
