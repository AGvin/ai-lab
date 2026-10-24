# TruLens

TruLens is an independently installable MIT-licensed Python framework for evaluation, tracing and observability of LLM, RAG and agent applications.

## Evaluation role and boundaries

Its open-source instrumentation produces traces and model-graded feedback for retrieval grounding, relevance and agent behavior. Originally created by TruEra, TruLens is now shepherded by Snowflake. Snowflake AI Observability may receive traces, but the hosted destination is distinct from the local framework.

## Reproducibility and operational safeguards

Pin package/integration versions, OpenTelemetry exporter and schema, judge model, dataset snapshot and permissions. Traces may contain prompts, documents, tool calls and sensitive outputs: define sampling, exporter destinations, secrets and retention explicitly. Scores are not portable across different judges or datasets.

## Relations

- Maintained by: [Snowflake](../../../../../../../producers/sub/s/sub/snowflake/)

## Official resources

- [Official project](https://www.trulens.org/)
- [Source](https://github.com/truera/trulens)
