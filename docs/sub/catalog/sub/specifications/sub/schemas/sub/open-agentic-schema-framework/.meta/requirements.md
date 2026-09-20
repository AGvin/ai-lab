# Documentation Requirements

## Requirements

- Present Open Agentic Schema Framework (OASF) as a released, versioned schema framework for describing AI-agent attributes, skills, capabilities, interactions, metadata, and relationships.
- Keep the canonical identity with the schema/framework contract rather than with the optional OASF schema server, SDK, directory service, MCP tooling, or other AGNTCY implementations.
- Preserve the upstream record/object model, skills/domains/modules taxonomy, schema-extension mechanism, validation semantics, and version-compatibility boundaries only when supported by current AGNTCY documentation or released schema artifacts.
- Record the upstream release-stability boundary: released schema versions are intended to remain immutable except for non-breaking documentation/minor bug corrections, while structural additions/deletions belong to a subsequent schema version.
- Treat the hosted OASF schema server as an official reference/validation surface for the latest released schema, not as the canonical specification identity itself.
- Re-check the current released schema/version before adding exact fields, taxonomies, module definitions, or compatibility claims.
- Keep Agent Directory, SLIM, AGNTCY Identity, SDKs, schema-server deployment, and other AGNTCY components with their own owners if they are separately materialized.

## Validation

- OASF is not described as a transport or agent-to-agent communication protocol.
- Version-sensitive schema details are not presented without a current authoritative release boundary.
- Implementation/tooling surfaces are not duplicated as independent specification facts.
