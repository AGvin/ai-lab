# Open Agentic Schema Framework

Open Agentic Schema Framework (OASF) is an AGNTCY schema framework for describing AI-agent attributes, skills, capabilities, interactions, and related metadata. It supplies a versioned data-description contract for agent discovery and interoperability, not a transport, executable agent, or security attestation.

## Schema contract

The framework centers on an agent **record object**. Skills and domains categorize capabilities, while modules let publishers extend records with additional structured data. OASF schema extensions may be private or separately hosted; validation and compatibility depend on the selected schema release and any installed extensions. An agent's description is an assertion, not independent proof that its capabilities or safety claims are correct. [Framework documentation](https://docs.agntcy.org/oasf/open-agentic-schema-framework/).

## Released schema and implementation boundaries

The upstream repository publishes versioned OASF schema releases, including **v1.1.0** in its current release list. Use the exact released schema when interpreting record fields, taxonomy changes, validation behavior, or compatibility; a mutable development branch or a patch-level schema image is not an interchangeable contract. [Upstream releases](https://github.com/agntcy/oasf/releases).

The separately deployed OASF schema server can browse and validate a released schema. SDKs, directory services, hosted validators, MCP-related adapters, AGNTCY Identity, and SLIM messaging have their own behavior and release lifecycles. Neither the presence of a published schema nor server validation proves that a directory entry is authentic, authorized, or safe to execute. [Schema-server documentation](https://docs.agntcy.org/oasf/oasf-server/).

## Official resources

- [OASF framework and extension model](https://docs.agntcy.org/oasf/open-agentic-schema-framework/)
- [OASF schema source and tagged releases](https://github.com/agntcy/oasf)
