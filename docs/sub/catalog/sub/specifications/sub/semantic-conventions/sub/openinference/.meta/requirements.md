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

## Scoped original-source qualification — 2026-11-07

- OpenInference is an upstream AI-observability semantic-conventions specification layered on OpenTelemetry spans and OTLP-compatible traces; it is not a new wire protocol, observability backend, instrumented SDK or hosted monitoring service. It defines AI operation span kinds and attributes for LLM calls, agent runs, tool execution, retrieval, embedding, token usage and evaluation feedback.
- AI traces can contain prompts, answers and tool output with personal or confidential content. The published specification recommends masking or filtering sensitive telemetry; it does not guarantee deployed collectors, instrumentation libraries or vendors enforce those controls. Convention maturity, exact attributes and span classifications are version-sensitive.
- Verified first-party source 1: https://arize-ai.github.io/openinference/spec/
- Verified first-party source 2: https://github.com/Arize-ai/openinference
- Existing semantic-conventions identity and original source accepted only; no instrumentation, spans, collector, backend or independent privacy/security assessment executed, no whole-repository schema/cache/CI/render, clean pass or final gate.
