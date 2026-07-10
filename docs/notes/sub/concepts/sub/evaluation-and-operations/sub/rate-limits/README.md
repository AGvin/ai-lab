# Rate Limits

Rate limits restrict the number or volume of requests allowed during a time period.

## Core idea

Limits protect providers and applications from overload, runaway agents, abuse, and unexpected cost. They may be expressed as requests per minute, input or output tokens per minute, concurrent requests, tool actions, or monetary budgets.

## Practical use

- Bound model and tool consumption per user or tenant.
- Prevent agent loops from exhausting quotas.
- Protect downstream databases and APIs.
- Separate interactive and batch traffic.
- Enforce fair use across shared infrastructure.

## Good practice

Return clear retry information, use exponential backoff with jitter, and queue only work that remains useful after waiting. Apply limits at several layers: user, workflow, model provider, and sensitive tool.

## Trade-offs and limitations

Strict limits can reduce usability during legitimate bursts. Queues smooth load but increase latency and may process stale requests. Distributed enforcement requires shared counters or coordinated gateways.

## Common mistakes

- Retrying immediately after a rate-limit response.
- Limiting requests but not tokens or generated output.
- Sharing one quota across critical and non-critical workloads.
- Allowing model-generated loops to bypass user-level limits.

## Related concepts

- [Evaluation and Operations](../../)
- [Retries](../../../agents-and-automation/sub/retries/)
- [Cost Management](../cost-management/)
- [Model Serving](../../../inference-and-serving/sub/model-serving/)
