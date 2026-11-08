# AsyncAPI Specification

## Relations

- Produced by: [AsyncAPI Initiative](../../../../../producers/sub/a/sub/asyncapi-initiative/)

## Purpose and published contract

The AsyncAPI Specification is a protocol-agnostic, machine-readable description contract for message-driven and event-driven APIs. It describes servers, channels, messages, operations, payload schemas, and protocol-specific bindings without requiring a particular message broker or transport. The latest published release verified for this page is **AsyncAPI 3.1.0 (January 31, 2026)**. [Published specification](https://www.asyncapi.com/docs/reference/specification/v3.1.0).

## Description and version boundaries

An AsyncAPI document defines which operations an application sends or receives, the channels and messages they use, and relevant servers and bindings. It can describe Kafka, AMQP, MQTT, WebSockets, HTTP and other transports, including ROS 2 bindings added in version 3.1.0. A binding describes a protocol-specific extension; it does not prove support for that transport by a particular runtime.

Use the exact published specification when interpreting version-specific fields, references, message schemas and operation semantics. The repository's mutable development branch and separately released parsers, validators, code generators, CLI, and Studio are not replacements for the normative v3.1.0 contract. AsyncAPI is not the OpenAPI HTTP interface-description contract, an MCP/A2A agent interaction protocol, or an event broker.

## Implementation boundaries

A published AsyncAPI feature does not establish that every SDK, generator, broker, gateway, or agent tool supports it. Verify protocol bindings, schema formats, reference resolution, and compatibility against the implementation and specification version in use. An API description does not itself execute or secure the described message flow.

## Official resources

- [AsyncAPI Specification v3.1.0](https://www.asyncapi.com/docs/reference/specification/v3.1.0)
- [AsyncAPI specification source and releases](https://github.com/asyncapi/spec)
