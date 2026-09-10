# Documentation Requirements

## Requirements

- Identify Graphify as Graphify Labs' open-source code-intelligence software that turns a software repository and supported adjacent project material into a queryable graph for developers and AI coding assistants.
- Preserve its primary product boundary: Graphify is a codebase-intelligence layer, not itself a code editor, autonomous coding agent, code-review product, general-purpose knowledge-graph platform, or standalone Agent Skill catalog item.
- Preserve the current package/interface identity at a source-backed level: the Python package is `graphifyy`, the CLI command is `graphify`, and assistant integration can install a `/graphify` skill or expose graph access through supported interfaces such as MCP.
- Distinguish structural code extraction from semantic processing. Code structure is parsed locally and deterministically with tree-sitter in the normal pipeline; supported documents/media may use the configured assistant or model/backend for semantic extraction. Do not generalize the local code path into a claim that every Graphify workflow is offline, private, or model-free.
- Explain that Graphify builds an explicit graph of code/project entities and typed relationships that can be queried or traversed for structure, dependencies, paths, architecture, and repository context rather than presenting the product as generic vector-search RAG.
- Preserve provenance/confidence semantics for automatically created relationships at a high level: directly extracted, inferred, and ambiguous relationships must remain distinguishable when the product exposes those states. Do not treat inferred graph edges as source assertions merely because they appear in the graph.
- Preserve useful output/query boundaries without freezing incidental UI details: Graphify exposes a machine-readable graph plus human-oriented report/visualization surfaces and supports graph-oriented query, path, and explain workflows.
- Treat assistant/editor integrations as Graphify capabilities. Do not create duplicate canonical entities for bundled/platform-specific skill adapters unless a future artifact has an independently published identity and inclusion rationale.
- Keep the hosted/enterprise product boundary separate. The existence of Graphify accounts, early-access platform surfaces, paid plans, or self-hosted enterprise functionality does not by itself justify a distinct `catalog/services/` entity; materialize one only after its independent product/service identity is verified.
- Treat package versions, supported-language counts, assistant/integration counts, popularity/download metrics, benchmark scores, pricing, and similar mutable state as freshness-sensitive and source-backed when expanded.
- Treat Graphify-produced benchmark results as vendor/self-reported evidence. Preserve material dataset size, harness/model constraints, comparison limitations, and the difference between retrieval metrics and answer-quality metrics when citing them.
- Preserve the current open-source licensing boundary as source-backed product metadata when discussed; do not infer licensing of hosted or enterprise offerings from the OSS repository license.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the current official site, documentation, and source repository from canonical entity metadata.

## Validation

- Graphify remains under `development-tools/code-intelligence/` rather than Agents, Code Review Tools, Agent Skills, or generic Knowledge Graph tooling.
- Local deterministic code parsing is not conflated with semantic processing of non-code material.
- Automatically inferred relations are not presented as equivalent to directly extracted source facts.
- Mutable counts, releases, benchmarks, pricing, and hosted-product state are not frozen as timeless facts.
- No separate hosted-service entity is implied without independent service-identity evidence.
- The `produced-by` relation resolves to Graphify Labs and is matched by the producer's inverse `produces` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
