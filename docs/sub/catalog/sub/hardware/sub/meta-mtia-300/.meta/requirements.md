# Documentation Requirements

## Requirements

- Identify Meta MTIA 300 as the production Meta Training and Inference Accelerator generation documented by Meta in March 2026.
- Preserve its production status and initial ranking/recommendation-training focus without projecting future-generation GenAI claims backward onto MTIA 300.
- Keep MTIA 400, 450, and 500 outside the stable catalog until first-party evidence establishes production/deployment status that clears the lifecycle gate; roadmap/test/scheduled deployment is not equivalent to current production.
- Treat hardware specifications, rack/network topology, software-stack compatibility, workload coverage, deployment scale, and performance comparisons as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains a concrete hardware product rather than a generic accelerator concept.
- Producer provenance resolves to Meta.

## Scoped original-source acceptance — 2026-11-06

- Meta states MTIA 300 is in production for ranking/recommendation training, distinct from later MTIA 400/450/500 and their GenAI-oriented claims. Its first-party August 2026 technical report describes 216 GB HBM3E, integrated NIC chiplets and 16 offload message engines; Meta's interconnect and benchmark comparisons are its own workload-specific findings, not an independent general LLM training result.
- Official source 1: https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
- Official source 2: https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/
- This scoped qualification does not establish full freshness, general stock, vendor-neutral benchmarks, framework support, ownership/legal clearance, schema/CI/cache/render or physical hardware testing.
