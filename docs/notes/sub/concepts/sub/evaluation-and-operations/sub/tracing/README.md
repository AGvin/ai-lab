# Tracing

Tracing records the ordered sequence of model calls, retrieval operations, tool executions, validations, and state transitions for one workflow execution.

## Core idea

A trace shows causal structure that aggregate metrics cannot. It can reveal that a poor answer began with a weak retrieval query, a tool timeout, a malformed argument, or a model decision based on stale state.

## Typical trace data

- Start and end time for each span.
- Parent-child relationships between operations.
- Model, prompt, tool, and configuration versions.
- Token, cost, latency, and status metadata.
- Source identifiers and validation outcomes.
- Redacted errors and retry history.

## Practical use

Use traces to debug agent loops, compare model versions, analyze latency, and build evaluation datasets from real failures. Retain enough context to reproduce the issue without storing unnecessary sensitive content.

## Trade-offs and limitations

High-cardinality trace data is expensive. Full prompt capture improves diagnosis but increases privacy risk. Sampling may miss rare failures, so critical errors should be retained separately.

## Common mistakes

- Logging tool calls without results or status.
- Omitting parent-child relationships.
- Storing raw credentials in trace attributes.
- Using traces as permanent memory for the agent.

## Related concepts

- [Evaluation and Operations](../../)
- [Observability](../observability/)
- [Agent State](../../../agents-and-automation/sub/agent-state/)
- [Reproducibility](../reproducibility/)
