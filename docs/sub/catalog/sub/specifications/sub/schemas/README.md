# Schemas

This specifications group owns independently identifiable, versioned schema and API-description contracts: normative data models, workflow descriptions, validation vocabularies, and schema frameworks. A listing here represents a specification identity, not a guarantee of conformance by any particular parser, API, validator, or agent runtime.

## Schema specification profiles

- [Arazzo Specification](./sub/arazzo-specification/)
- [AsyncAPI Specification](./sub/asyncapi-specification/)
- [Open Agentic Schema Framework](./sub/open-agentic-schema-framework/)
- [OpenAPI Specification](./sub/openapi-specification/)
- [Overlay Specification](./sub/overlay-specification/)

## Scope and boundaries

Arazzo specifies API workflows, AsyncAPI describes message-driven APIs, OpenAPI describes HTTP APIs, Overlay defines transformations of OpenAPI descriptions, and OASF describes AI-agent records and their extensible capability taxonomy. Their normative sources, versions, and validation semantics are distinct.

Protocols and transport behavior belong under [Protocols](../protocols/); standalone serialization and file formats belong under [Formats](../formats/). Concrete SDKs, servers, tooling, registries, deployment and security decisions belong with their implementation owners. Exact compatibility and currentness require source- and version-scoped verification.
