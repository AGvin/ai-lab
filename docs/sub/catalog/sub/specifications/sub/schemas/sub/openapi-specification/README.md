# OpenAPI Specification

## Relations

- Produced by: [OpenAPI Initiative](../../../../../producers/sub/o/sub/openapi-initiative/)

## Purpose and published contract

The OpenAPI Specification (OAS) describes HTTP APIs in a programming-language-neutral, machine-readable form. It covers operations, parameters, request and response bodies, security schemes, and Schema Objects. These descriptions support discovery, client generation, validation, and tool integration. The published version represented here is **OAS 3.2.1, dated September 10, 2026**. [Published specification](https://spec.openapis.org/oas/v3.2.1.html).

## Version and implementation boundaries

Use the versioned specification for field obligations and normative language. The rolling editors' draft, examples, and generator defaults have different roles. OAS 3.0, 3.1, and 3.2 differ in Schema Object semantics, JSON Schema dialect handling, supported HTTP methods, webhooks, and streaming metadata; a tool's claimed OAS support needs a version and feature scope.

JSON and YAML are serialization choices. JSON Schema dialects, OAuth behavior, provider-specific function adapters, and MCP tool input schemas each retain their own contracts. OAS describes an HTTP interface; it does not itself supply an invocation transport such as MCP or A2A.

Arazzo separately specifies API workflows, and Overlay separately specifies transformations of API descriptions. Generator, linter, validator, SDK, and agent-action compatibility depends on the actual implementation; publication of a standard does not establish universal support.

## Official resources

- [OAS 3.2.1 — published specification](https://spec.openapis.org/oas/v3.2.1.html)
- [Latest published specification pointer](https://spec.openapis.org/oas/latest.html)
- [OpenAPI Specification repository](https://github.com/OAI/OpenAPI-Specification)
