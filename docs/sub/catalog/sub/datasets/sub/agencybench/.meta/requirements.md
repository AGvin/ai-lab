# Documentation Requirements

## Requirements

- Present AgencyBench as a released benchmark/dataset for evaluating autonomous agents on long-horizon, real-world workflows across multiple capability classes.
- Cover task/scenario breadth, tool-use depth, user simulation, Docker execution, and visual/functional evaluation only where useful for distinguishing AgencyBench from narrower research, operations-research, or memory/learning benchmarks.
- Keep benchmark harnesses, evaluation scripts, and sample runs as surfaces of the same dataset identity unless an independently durable product identity emerges.
- Treat task counts, scenario counts, capability coverage, evaluation implementation, and released versions as freshness-sensitive.

## Validation

- The entity remains a dataset/benchmark rather than an agent framework, sandbox platform, or workflow engine.
- Its canonical role remains broader cross-domain long-horizon agency evaluation rather than duplicating Horizon, ORAgentBench, or AIRS-Bench.

## Scoped original-source qualification — 2026-11-08

- **AgencyBench** is GAIR-NLP's original long-horizon autonomous-agent benchmark. The source explicitly distinguishes the September 2025 V1 **10-task** preview from the January 2026 **V2 with 138 tasks, 32 scenarios and six capability areas** (Game, Frontend, Backend, Code, Research and MCP). Average 90 tool calls, roughly one-million-token contexts and hours of execution describe the publisher's evaluated tasks, not every task or every model run.
- Rubric evaluation combines user-simulation feedback, Docker-based execution, visual and functional checks. Code, third-party scenario assets and model-scaffold configurations have separate operational and rights risks; an MIT root repository label is not independent authorization to publish every embedded task asset. The paper's relative model performance is not an independently reproduced score.
- First-party source: https://github.com/GAIR-NLP/AgencyBench ; https://agencybench.opensii.ai/
- Source-gate acceptance covers this existing original V2 benchmark identity, public task/scenario release, V1/V2 distinction and evaluator boundaries only. No agent runs, untrusted task execution, underlying data rights/security/legal review, schema/cache/CI/render, clean or final delivery.
