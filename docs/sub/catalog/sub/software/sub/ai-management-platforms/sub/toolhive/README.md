# ToolHive

ToolHive is Stacklok's self-managed management and runtime platform for operating MCP servers and related agent-tool or skill integrations.

## Product scope

The Apache-2.0 core provides a common operational surface across CLI/desktop, runtime isolation, registries, Kubernetes/operator deployments, and optional gateway and governance features. Product components such as a registry, operator, virtual MCP endpoints and UI are not automatically independent catalog products. Paid Stacklok Enterprise capabilities must not be assumed to be included in the open-source distribution.

## Operations and boundaries

Pin the application version, container runtime, orchestrator, registry source and MCP transport settings. ToolHive may enforce identities, policies and secret isolation only when correctly configured; MCP servers remain third-party executable code requiring provenance checks, scoped credentials, network controls and audit/retention review. Sandboxing reduces risk but does not guarantee absolute isolation.

## Relations

- Produced by: [Stacklok](../../../../../producers/sub/s/sub/stacklok/)

## Official resources

- [Source](https://github.com/stacklok/toolhive)
- [Documentation](https://docs.stacklok.com/toolhive/)
