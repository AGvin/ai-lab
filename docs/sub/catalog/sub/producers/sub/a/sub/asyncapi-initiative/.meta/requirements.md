# Documentation Requirements

## Requirements

- Identify the AsyncAPI Initiative as the first-party maintainer and publisher of the AsyncAPI Specification for machine-readable descriptions of message-driven and event-driven APIs.
- Preserve the distinction between the initiative, its normative specification, the open-source AsyncAPI tools/ecosystem and individual protocol transports such as MQTT, AMQP, Kafka, WebSockets and ROS 2. Do not treat the organization as the vendor of those messaging protocols.
- Attribute the published normative AsyncAPI Specification to this producer and preserve its reciprocal `produces` / `produced-by` relation.
- Verify changes to initiative ownership, maintenance, official URLs, and release publication from its official website and the `asyncapi/spec` repository instead of inferring lifecycle from tooling releases.

## Validation

- First-party ownership and official specification repository are current.
- The AsyncAPI Specification relation resolves and reciprocates from its own canonical specification entity.
- Related ecosystem tools or bindings are not silently materialized as separate normative specifications.
