# Documentation Requirements

## Requirements

- Identify the OpenAPI Specification (OAS) as a formal, programming-language-neutral HTTP API interface-description contract used for interoperable API discovery, client generation, tooling and machine-readable tool integration.
- Preserve primary placement under `specifications/schemas` because the normative artifact describes the API operations, parameters, request/response bodies, security schemes, JSON Schema-related data models and documented interfaces; it is not an invocation transport/protocol equivalent to MCP or A2A.
- The current latest published **v3.2.1** is dated **2026-09-10** by the OpenAPI Initiative. Distinguish normative release versions and schema iterations from the continuously changing editors' draft. Exact RFC keyword/field obligations must come from the official versioned published specification, not examples or generator defaults.
- Do not conflate JSON/YAML serialization, OpenAPI schemas, JSON Schema dialect constraints, OpenAPI tool/function-calling adapters, OAuth transport behavior, or MCP Tools `inputSchema` with identical normative contracts.
- Preserve version compatibility boundaries between OAS 3.0, 3.1 and 3.2; particularly, Schema Object semantics, JSON Schema dialect, API operations, webhooks, streaming metadata and documented HTTP methods can differ.
- Attribute related Arazzo workflow and Overlay documents to their own formally published specifications rather than silently folding their separate normative contracts into the OAS core.
- Treat code generation, linting, API import, AI agent action support, SDK/plugin compatibility and provider-specific limitations as implementation facts rather than standard conformance guarantees.
- Preserve OpenAPI Initiative provenance with reciprocal relation.

## Validation

- Latest-version label and authoritative HTML correspond to an actually published normative version, not an editor preview.
- Description-schema scope is distinct from a communication protocol and from an installable OpenAPI validator or SDK.
- OpenAPI Initiative `produces` inverses this `produced-by` relation.
