# Graphify

Graphify is Graphify Labs' open-source code-intelligence software for turning repository code and supported project material into a queryable graph.

## Product scope

The Python package is `graphifyy`; the CLI is `graphify`. Its assistant skill and MCP interfaces provide access to graphs for codebase questions, dependency and path exploration, and explanations. Installing the local assistant skill does not itself establish an MCP connection.

Graphify produces a machine-readable graph and human-readable report and visualization. Edges distinguish directly extracted source relationships from inferred relationships; an inferred connection is a derived result to inspect, not an independent source assertion.

## Processing boundary

Normal code extraction uses local tree-sitter parsing. Semantic processing of documents and media can use the configured assistant or model backend, so review the selected provider and data path before indexing private material. A local code-only workflow does not describe every hosted, MCP or mixed-input workflow.

Hosted and enterprise offerings remain separate deployment and commercial boundaries. Product-reported benchmarks require their dataset, harness and metric context.

## Relations

- Produced by: [Graphify Labs](../../../../../../../producers/sub/g/sub/graphify-labs/)

## Official resources

- [Graphify](https://graphify.com/)
- [Documentation](https://graphify.com/docs)
- [Repository](https://github.com/Graphify-Labs/graphify)
