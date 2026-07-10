<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:1f11bd8669b9d8faf042f9d756bc53003e0ae1af
  mode: copy-through
-->

# Evaluation and Operations



Concepts for selecting, testing, observing, and operating AI systems under real quality, cost, and reliability constraints.

## Переклади

- [English](../../)
- Українська — поточна

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`evals/`](../../sub/evals/l10n/uk_UA/) — Repeatable tests that measure whether an AI model or system meets defined requirements.
- [`model-selection/`](../../sub/model-selection/l10n/uk_UA/) — Choosing a model based on task quality, capabilities, cost, latency, safety, and deployment constraints.
- [`model-routing/`](../../sub/model-routing/l10n/uk_UA/) — Selecting among models dynamically according to the request or operating policy.
- [`observability/`](../../sub/observability/l10n/uk_UA/) — Using logs, metrics, traces, and events to understand AI system behavior.
- [`tracing/`](../../sub/tracing/l10n/uk_UA/) — Recording the sequence of model, tool, retrieval, and workflow operations for one execution.
- [`cost-management/`](../../sub/cost-management/l10n/uk_UA/) — Measuring and controlling model, infrastructure, storage, and tool expenses.
- [`latency-and-throughput/`](../../sub/latency-and-throughput/l10n/uk_UA/) — Balancing response time against the amount of work completed per unit of time.
- [`quality-cost-tradeoffs/`](../../sub/quality-cost-tradeoffs/l10n/uk_UA/) — Choosing an acceptable balance between output quality and operational expense.

## Useful

- [`benchmarks/`](../../sub/benchmarks/l10n/uk_UA/) — Standardized tasks or datasets used to compare models or systems.
- [`evaluation-datasets/`](../../sub/evaluation-datasets/l10n/uk_UA/) — Curated examples used to test quality, safety, retrieval, or task performance.
- [`human-evaluation/`](../../sub/human-evaluation/l10n/uk_UA/) — People assessing model outputs against explicit criteria.
- [`fallback-models/`](../../sub/fallback-models/l10n/uk_UA/) — Alternative models used when the preferred model fails, is unavailable, or exceeds policy limits.
- [`caching/`](../../sub/caching/l10n/uk_UA/) — Reusing prior results or processed data to reduce repeated work.
- [`rate-limits/`](../../sub/rate-limits/l10n/uk_UA/) — Controls that restrict request volume over a period of time.

## Specialized

- [`llm-as-a-judge/`](../../sub/llm-as-a-judge/l10n/uk_UA/) — Using a language model to score, rank, or critique other model outputs.
- [`retrieval-evaluation/`](../../sub/retrieval-evaluation/l10n/uk_UA/) — Measuring whether retrieval returns relevant, complete, and correctly ranked evidence.
- [`reproducibility/`](../../sub/reproducibility/l10n/uk_UA/) — The ability to repeat an evaluation or workflow with comparable conditions and results.
