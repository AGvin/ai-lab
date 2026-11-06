# Documentation Requirements

## Requirements

- Identify TruLens as the independently installable **MIT-licensed Python agent/RAG evaluation, tracing and observability framework** with OpenTelemetry-native traces, local/dataset evaluation, model-as-judge feedback, grounding/context relevance and agent-tool assessment. It is not exclusively the Snowflake Cortex managed evaluation service.
- Preserve provenance: originally created by **TruEra**, then incorporated into Snowflake's stewardship after the 2024 acquisition of TruEra's observability technology/team. Official `trulens.org` explicitly states the active project is shepherded by Snowflake, while its maintained GitHub remains `truera/trulens`.
- Preserve the current software/hosting boundary: a Python process using TruLens with independently configured evaluation providers and OTLP exporters is the software framework. Snowflake AI Observability can receive its traces and run agent/RAG evaluations, but that managed destination is a separate Snowflake platform capability, not another copy of the framework or owned external models.
- Distinguish step-level traces, metric scores, prompts/judge configuration, dataset-run evaluation and production collection. Vendor and self-reported benchmark numbers are not independent proof of comparative quality.
- Pin TruLens package version and modular `trulens-core`, integration/provider extras, OpenTelemetry schema/exporter, Snowflake database/catalog privileges if applicable, judge model version and dataset/ground-truth snapshot before reproducing scored runs.
- Instrumentation may capture prompts, retrieved documents, sensitive input/output and tool traces. Explicitly configure privacy, sampling, data destinations, credential security and retention to prevent inadvertent sensitive-data leakage.
- Keep the 2024 acquisition and Snowflake current `maintained-by` provenance explicit without asserting Snowflake was the original founder/producer; no duplicate defunct TruEra producer is necessary solely for the historical attribution.

## Validation

- The first-party open-source repository supplies current installable software, MIT license and evaluation/tracing scope.
- The official TruLens homepage and current Snowflake AI Observability documentation substantiate present Snowflake stewardship and integration boundary.
- The `maintained-by` relation has the exact `maintains` inverse at the current Snowflake producer.
