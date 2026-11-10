# Documentation Requirements

## Requirements

- Identify ToolHive as a published Apache-2.0, self-managed MCP server and agent-skill management/control-plane platform across desktop/CLI and Kubernetes/registry/gateway environments, including isolated runtime and optional identity/authorization/audit controls.
- Classify under self-managed AI management platforms because its primary installed footprint is MCP server lifecycle, registry, policy, runtime isolation and fleet governance rather than a standalone hosted tool API or a generic AI model gateway. The gateway is an internal component, not a duplicate canonical model-gateway identity.
- Keep ToolHive CLI, desktop UI, registry, operator and vMCP virtualization as surfaces/components of the same product family unless separately versioned/published product ownership is demonstrable. Distinguish Stacklok Enterprise paid features and dependencies from Apache 2.0 released core.
- Only promise identity enforcement, credential isolation, network policies, signed registries and audit where the actual configured environment implements them. MCP server packages remain untrusted third-party code and require supply-chain/provenance checks.
- Pin ToolHive version, container runtime, orchestrator/operator compatibility, MCP auth transport, allowed capabilities, policies, registry sources and skill delivery model; sandboxing cannot be treated as absolute isolation.
- Keep Stacklok publisher ownership, not ownership of all software an enterprise runs through the ToolHive registry.

## Validation

- The first-party maintained source or documentation demonstrates released installable functionality and exact source/build identity.
- Version-sensitive protocol, license and hosted deployment distinctions remain explicit.
- Exact reciprocal `produced-by` / `produces` source-of-truth relation resolves to an existing or concurrently created producer.
