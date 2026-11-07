# Documentation Requirements

## Requirements

- Identify the OpenTelemetry GenAI Semantic Conventions as the dedicated OpenTelemetry semantic-convention specification for generative-AI clients, agents, MCP-related telemetry, and provider-specific GenAI telemetry.
- Preserve span, metric, event, attribute, provider, agent, and MCP semantics only from current authoritative OpenTelemetry material.
- Preserve stability labels and migration/deprecation boundaries because the GenAI conventions evolve independently from the core OpenTelemetry semantic-conventions repository.
- Treat language instrumentation and observability products as implementations/consumers of the conventions rather than duplicate specification identities.
- Keep OpenInference distinct as a separate AI observability semantic-convention specification.

## Validation

- The entity is classified as a semantic-convention specification, not as an SDK, telemetry backend, or observability service.
- Experimental, moved, deprecated, and stable convention surfaces are not conflated.

## Scoped original-source qualification — 2026-11-07

- The OpenTelemetry GenAI Semantic Conventions provide OpenTelemetry-specific attributes and semantic guidance for generative-AI client calls, agents, evaluation and MCP-related operations. They are a specification vocabulary, not an SDK, runtime service, transport protocol, automatic model evaluation or substitute for independently maintained OpenInference conventions.
- The previous OpenTelemetry semantic conventions GenAI documentation route now explicitly says **Moved**: the source-of-truth content is maintained in the dedicated `open-telemetry/semantic-conventions-genai` repository. Follow versioned status and stabilization/migration labels at the authoritative source; the old URL is historical navigation, not fresh normative authority. Prompts, responses and tool telemetry require account-specific content controls.
- Verified first-party source 1: https://github.com/open-telemetry/semantic-conventions-genai
- Verified first-party source 2: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- Existing semantic-conventions identity/source accepted with moved-repository boundary only. No generated spans, collector integration, compatibility matrix or independent security/privacy/license review, full schema/cache/CI/render, clean pass or final gate. Reader page is missing, uncredited.
