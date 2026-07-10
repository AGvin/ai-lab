# Evaluation and Operations

<!--
ai_content:
  managed: true
  l10n: true
-->

Concepts for selecting, testing, observing, and operating AI systems under real quality, cost, and reliability constraints.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`evals/`](./sub/evals/) — Repeatable tests that measure whether an AI model or system meets defined requirements.
- [`model-selection/`](./sub/model-selection/) — Choosing a model based on task quality, capabilities, cost, latency, safety, and deployment constraints.
- [`model-routing/`](./sub/model-routing/) — Selecting among models dynamically according to the request or operating policy.
- [`observability/`](./sub/observability/) — Using logs, metrics, traces, and events to understand AI system behavior.
- [`tracing/`](./sub/tracing/) — Recording the sequence of model, tool, retrieval, and workflow operations for one execution.
- [`cost-management/`](./sub/cost-management/) — Measuring and controlling model, infrastructure, storage, and tool expenses.
- [`latency-and-throughput/`](./sub/latency-and-throughput/) — Balancing response time against the amount of work completed per unit of time.
- [`quality-cost-tradeoffs/`](./sub/quality-cost-tradeoffs/) — Choosing an acceptable balance between output quality and operational expense.

## Useful

- [`benchmarks/`](./sub/benchmarks/) — Standardized tasks or datasets used to compare models or systems.
- [`evaluation-datasets/`](./sub/evaluation-datasets/) — Curated examples used to test quality, safety, retrieval, or task performance.
- [`human-evaluation/`](./sub/human-evaluation/) — People assessing model outputs against explicit criteria.
- [`fallback-models/`](./sub/fallback-models/) — Alternative models used when the preferred model fails, is unavailable, or exceeds policy limits.
- [`caching/`](./sub/caching/) — Reusing prior results or processed data to reduce repeated work.
- [`rate-limits/`](./sub/rate-limits/) — Controls that restrict request volume over a period of time.

## Specialized

- [`llm-as-a-judge/`](./sub/llm-as-a-judge/) — Using a language model to score, rank, or critique other model outputs.
- [`retrieval-evaluation/`](./sub/retrieval-evaluation/) — Measuring whether retrieval returns relevant, complete, and correctly ranked evidence.
- [`reproducibility/`](./sub/reproducibility/) — The ability to repeat an evaluation or workflow with comparable conditions and results.
