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

## Scoped original-source qualification — 2026-11-07

- Open Agentic Schema Framework (OASF) defines an extensible, versioned data model for describing agent attributes, skills, domains, modules, relationships and capabilities. Its record-object schema is not the SLIM transport, Agent Directory lookup service, A2A/MCP wire protocol, or an agent runtime.
- AGNTCY first-party documentation distinguishes the upstream schema artifacts from its separately versioned OASF schema server, SDKs and hosted reference validator. A published schema does not certify the truth of an agent's asserted capabilities or guarantee that a directory entry is safe to execute; extensions and exact fields must be interpreted against the selected schema release.
- Verified first-party source 1: https://docs.agntcy.org/oasf/open-agentic-schema-framework/
- Verified first-party source 2: https://docs.agntcy.org/oasf/oasf-server/
- Verified first-party source 3: https://github.com/agntcy/oasf
- Existing schema identity/source acceptance only; no agent registry instance, schema validation, end-to-end transport, runtime security audit, whole-repository clean pass or final gate. Existing reader page is absent and has no repair credit.

## Scoped published-schema check — 2026-11-08

- The official AGNTCY OASF repository currently lists a tagged **v1.1.0** release; the published release distinguishes schema artifacts from patch-level image builds and the separately deployed OASF server. [Upstream releases](https://github.com/agntcy/oasf/releases).
- Current schema fields, taxonomy and compatibility must be pinned to a selected release; this bounded tag/source check is not a complete freshness audit, a schema-validation run, or an independent verification of any hosted agent description.
