# Pi Durable

Pi Durable is Earendil Works' **experimental** TypeScript framework for building long-running, crash-resumable agent applications. Released alongside Pi 1.0 in October 2026, it is a separately published runtime/library, not a new version of the [Pi terminal coding agent](../../../agents/sub/local/sub/pi/) and not a first-party managed cloud-agent service.

## Runtime and durability

Pi Durable stores conversation transcripts, tasks and application state in atomic commits before exposing them. With a persistent backend, interrupted work can resume after a process restart. It supports multiple conversations and forks, customizable extensions, tools, hooks, and execution environments chosen by the application operator.

Durability depends on correct storage, retry-safe side effects, task ownership, and process recovery configuration. Tools can access files, shell commands, credentials, and external services through their assigned execution environment; neither checkpointing nor an experimental package API provides an isolation or production-readiness guarantee.

## Related product

- [Pi](../../../agents/sub/local/sub/pi/) — distinct minimal interactive coding agent sharing underlying ecosystem components, not superseded by Pi Durable.

## Official resources

- [Pi Durable announcement](https://earendil.com/posts/pi-durable/)
- [Pi 1.0 and Pi Durable launch](https://earendil.com/posts/pi-1-0/)
- [Pi Durable source and documentation](https://github.com/earendil-works/pi/tree/main/packages/durable)
- [Pi Durable package manifest](https://github.com/earendil-works/pi/blob/main/packages/durable/package.json)
