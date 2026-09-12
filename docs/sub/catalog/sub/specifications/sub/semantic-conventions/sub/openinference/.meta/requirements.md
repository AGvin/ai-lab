# Documentation Requirements

## Requirements

- Identify OpenInference as the open semantic-convention specification for AI/LLM application telemetry built on OpenTelemetry primitives.
- Preserve its upstream role as a common set of traces/spans and attributes for AI observability rather than describing it as a transport protocol, telemetry backend, or observability product.
- Preserve span-kind and attribute semantics only from current authoritative specification material and retain upstream stability labels where applicable.
- Treat OpenInference instrumentation packages and language implementations as implementations of the specification rather than duplicate specification identities.
- Keep OpenTelemetry as the underlying general telemetry ecosystem; OpenInference adds AI-specific semantic conventions rather than replacing OpenTelemetry.

## Validation

- OpenInference is classified as a semantic-convention specification, not as a schema, broad standard, SDK, or observability service.
- Experimental and stable convention surfaces are not conflated.
- Vendor/platform integrations are not represented as intrinsic specification requirements.
