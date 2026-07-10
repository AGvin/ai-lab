# Observability

<!--
ai_content:
  managed: true
  l10n: true
-->

Observability is the ability to understand an AI system's internal behavior from logs, metrics, traces, events, and recorded state.

## Core idea

AI failures are often distributed across prompts, retrieval, model calls, tools, validation, and external services. Observability connects these stages so operators can determine what happened, why it happened, and which component requires correction.

## Useful signals

- Request volume, latency, cost, and token usage.
- Model and prompt versions.
- Retrieval queries, candidate counts, and source IDs.
- Tool calls, arguments, results, and failures.
- Validation outcomes and retry counts.
- User feedback and quality metrics.

## Practical use

Assign a correlation ID to each workflow execution. Record structured events rather than relying only on free-form logs. Build dashboards for operational health and alert on unusual error, cost, latency, or refusal patterns.

## Trade-offs and limitations

Detailed telemetry can be expensive and may expose sensitive prompts or data. Redaction, sampling, retention, and access controls are required. Observability explains recorded behavior but cannot reconstruct data that was never captured.

## Common mistakes

- Logging full secrets and personal data.
- Recording model output without model or prompt version.
- Monitoring API uptime but not answer quality.
- Aggregating metrics without preserving per-request traces for diagnosis.

## Related concepts

- [Evaluation and Operations](../../)
- [Tracing](../tracing/)
- [Cost Management](../cost-management/)
- [Data Privacy](../../../safety-privacy-and-reliability/sub/data-privacy/)
