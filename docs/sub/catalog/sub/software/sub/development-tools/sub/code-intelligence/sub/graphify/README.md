# Graphify

Graphify is Graphify Labs' open-source code-intelligence software that turns a software repository and supported adjacent project material into a queryable graph for developers and AI coding assistants.

## Scope and boundaries

- The profile preserves its primary product boundary: Graphify is a codebase-intelligence layer, not itself a code editor, autonomous coding agent, code-review product, general-purpose knowledge-graph platform, or standalone Agent Skill catalog item.
- The profile preserves the current package/interface identity at a source-backed level: the Python package is `graphifyy`, the CLI command is `graphify`, and assistant integration can install a `/graphify` skill or expose graph access through supported interfaces such as MCP.
- Structural code extraction remains distinct from semantic processing. Code structure is parsed locally and deterministically with tree-sitter in the normal pipeline; supported documents/media may use the configured assistant or model/backend for semantic extraction. Do not generalize the local code path into a claim that every Graphify workflow is offline, private, or model-free.
- The profile explains that Graphify builds an explicit graph of code/project entities and typed relationships that can be queried or traversed for structure, dependencies, paths, architecture, and repository context rather than presenting the product as generic vector-search RAG.

## Relations

- Produced by: [`catalog/producers/g/graphify-labs`](../../../../../../../producers/sub/g/sub/graphify-labs/)

## Official resources

- <https://graphify.com/>
- <https://graphify.com/docs>
- <https://github.com/Graphify-Labs/graphify>
