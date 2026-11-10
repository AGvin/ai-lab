# Redis Agent Memory

Redis Agent Memory is Redis's managed memory service for AI applications and agents. It provides session state and longer-term memory, with extraction, summarization and retrieval features exposed through a service API. Current Redis documentation places it within the Iris context engine while giving Agent Memory its own service setup and SDK/API surface. [Agent Memory overview](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/) · [Cloud service guide](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/).

## Scope and operating boundaries

The Redis Cloud deployment is managed; the Redis Software deployment is documented as private preview. Choose the available deployment and model configuration before planning production use, and define which events or memories may persist, who may retrieve them and when they should expire or be deleted. Memory extraction is an application data-processing step, so its configured model and access boundaries matter. [Deployment and model guidance](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/) · [Service administration](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/).

The original Agent Memory Server now lives under the upstream repository's V0 research material and is not the supported production distribution. Its Apache-2.0 repository license does not establish the managed service's contract. Redis also distinguishes its published research evaluation configurations from the shipping service; benchmark results require the exact provider version, models and protocol. [Repository and V0 boundary](https://github.com/redis/agent-memory-server).

## Produced by

- [Redis](../../../../../../../producers/sub/r/sub/redis/)

## Official resources

- [Product page](https://redis.io/agent-memory/)
- [Agent Memory overview](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/)
- [Cloud service guide](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory/)
- [Agent Memory Server and V0 history](https://github.com/redis/agent-memory-server)
