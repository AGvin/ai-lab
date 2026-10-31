# NVIDIA NeMo Relay

NVIDIA NeMo Relay is an open-source runtime/observability layer for recording and controlling agent execution scopes, tool/LLM calls and lifecycle events.

## Scope and product boundaries

Relay provides nested execution scopes, event lineage, middleware, plugins and telemetry integrations for applications and agent frameworks. Its primary catalog role is cross-agent observability with supporting runtime-policy primitives. It does not replace the agent framework, tracing backend, evaluation platform or model provider. OpenTelemetry and trajectory formats remain external conventions and outputs.

## Deployment and operations

Relay instrumentation may capture prompts, tool arguments, responses and sensitive run context. Isolate per-request scopes, audit middleware privileges, restrict credentials and telemetry destinations, apply redaction/retention and verify cleanup. Supported language bindings, transport formats, exporters and integration APIs depend on the selected released version; tracing does not provide a secure execution sandbox.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Official repository](https://github.com/NVIDIA/NeMo-Relay)
- [Scope documentation](https://docs.nvidia.com/nemo/relay/about-nemo-relay/concepts/scopes)
