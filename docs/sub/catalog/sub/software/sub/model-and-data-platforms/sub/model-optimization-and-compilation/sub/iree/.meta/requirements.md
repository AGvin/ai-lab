# Documentation Requirements

## Requirements

- Present IREE as an MLIR-based end-to-end compiler/runtime whose canonical catalog identity is driven by model/program import, compilation, lowering, target-specific code generation, and deployable compiled modules.
- Keep the runtime as an execution component of the compiled IREE artifact workflow rather than moving the project to serving-first inference-runtime ownership.
- Treat supported ML frontends, deployment targets, accelerators/APIs, compiler/runtime packages, experimental targets, and platform support as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- IREE remains compiler/optimization-first despite including a runtime.
- Producer provenance resolves to the IREE Project.
