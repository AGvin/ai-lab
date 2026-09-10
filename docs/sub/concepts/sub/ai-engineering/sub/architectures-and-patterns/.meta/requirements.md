# Documentation Requirements

## Requirements

- Use the reader-facing title `AI System Architectures and Patterns`.
- Present this domain as reusable system-level arrangements for composing models, retrieval, tools, control logic, state, verification, routing, and other components into AI-enabled systems.
- Distinguish system architectures/patterns from intrinsic model architectures such as Transformers, MoE, attention, or encoder-decoder structures; both use the word `architecture` but have different ownership levels.
- Explain that a pattern describes roles, interactions, control/data flow, and trade-offs rather than mandating one vendor, framework, programming language, or deployment topology.
- Keep RAG, agentic RAG, model routing, and fallback architectures as distinct selected descendants; do not infer unlisted children from those patterns.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete implementations, product-specific orchestration graphs, infrastructure topology, benchmark evidence, and project decisions with their applicable catalog, engineering, evidence, or project owners.

## Validation

- System patterns are not confused with neural/model architectures.
- The page does not turn reusable patterns into vendor-specific reference implementations.
- Direct-child navigation contains only currently materialized selected descendants.
- No unselected pattern leaf is inferred from general architecture terminology.
