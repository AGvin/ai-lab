# Documentation Requirements

## Requirements

- Identify the AsyncAPI Specification as an independently published, protocol-agnostic, machine-readable description contract for message-driven and event-driven APIs, covering servers, channels, messages, operations, schemas and protocol bindings. Its relevance to AI/agent integration does not turn it into an agent execution protocol.
- Preserve the published **v3.1.0** normative release as the latest tagged version identified in the official `asyncapi/spec` repository; distinguish released specification revisions from the mutable `master` draft, validators, and generator releases. Recheck latest-version claims against official sources when refreshing the entity.
- Keep the specification under `specifications/schemas` as an independently useful event/API description contract. Distinguish it from OpenAPI's HTTP API description contract, MCP/A2A agent interaction protocols, JSON/YAML serialization, embedded JSON Schema dialects, and transports or protocol bindings such as Kafka, MQTT, AMQP, WebSockets and ROS 2.
- Treat channel/operation/message semantics, reference resolution, version migration, and binding compatibility as version-specific normative constraints. Do not infer that a parser, generator or AI tool supports every published feature, protocol binding or specification revision.
- Distinguish the normative AsyncAPI Specification from AsyncAPI CLI, Studio, Parser, Generator, registry tools and any implementation libraries, which have separate release lifecycles and applicable software/service ownership.
- Preserve authoritative AsyncAPI Initiative provenance and reciprocal `produced-by` / `produces` relations.

## Validation

- Latest-release claim and normative document correspond to an explicitly published version at `https://github.com/asyncapi/spec`, not an untagged editor draft.
- Canonical schema specification identity is independent of OpenAPI, transports, concrete tooling and client-specific adapters.
- The AsyncAPI Initiative `produces` relation inverts this specification's `produced-by` relation.
