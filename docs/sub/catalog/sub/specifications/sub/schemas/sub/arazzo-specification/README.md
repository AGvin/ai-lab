# Arazzo Specification

## Relations

- Produced by: [OpenAPI Initiative](../../../../../producers/sub/o/sub/openapi-initiative/)

## Purpose and published contract

Arazzo is the OpenAPI Initiative's machine-readable description of workflows made from dependent API calls and their expected outcomes. **Arazzo 1.1.0, published May 17, 2026**, is the versioned contract represented here. Workflow execution belongs to tools that implement that description. [Published specification](https://spec.openapis.org/arazzo/v1.1.0.html).

## Workflow scope

The specification defines source descriptions, reusable workflows, steps, dependencies, inputs and outputs, success and failure criteria, and runtime expressions. Source descriptions can refer to supported OpenAPI and AsyncAPI descriptions within the version's stated boundaries. The workflow document expresses how operations relate and how results feed subsequent steps.

OpenAPI continues to own the HTTP API description, and Overlay owns its separate transformation contract. An Arazzo document does not incorporate every requirement of either specification into a new endpoint schema, nor does it provide a running API server or orchestration engine.

## Interpretation and tooling

Pin the published version when validating fields or interpreting an expression. An editor's draft and a vendor example are not substitutes for the released normative document. Workflow runners, validators, SDKs, and provider integrations have their own supported feature sets and release histories. Their execution, authentication, error recovery, and operational behavior need implementation-specific evidence.

## Official resources

- [Arazzo 1.1.0 — published specification](https://spec.openapis.org/arazzo/v1.1.0.html)
- [Published specification index](https://spec.openapis.org/arazzo/)
- [Arazzo Specification repository](https://github.com/OAI/Arazzo-Specification)
