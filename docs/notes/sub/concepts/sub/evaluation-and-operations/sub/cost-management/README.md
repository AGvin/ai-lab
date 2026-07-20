# Cost Management

Cost management measures, attributes, forecasts, and controls spending across models, infrastructure, storage, retrieval, and tools.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Cost sources

- Input, output, cached, and reasoning tokens.
- GPU or CPU runtime and idle capacity.
- Embedding and reranking operations.
- Vector storage, logs, and traces.
- External APIs and tool calls.
- Human review and operational maintenance.

## Core idea

The cheapest model request is not necessarily the cheapest successful workflow. A weak model may require more retries, human correction, or larger prompts. Cost should therefore be measured per accepted task result.

## Practical use

Tag usage by user, project, model, and workflow. Set budgets and alerts. Cache stable work, route simple tasks to smaller models, limit context, and monitor anomalous agent loops.

## Trade-offs and limitations

Aggressive cost reduction can lower quality, reliability, or privacy. Local infrastructure replaces API charges with hardware, electricity, maintenance, and capacity-planning costs.

## Common mistakes

- Counting model tokens but ignoring tool and human costs.
- Comparing local and hosted inference only by marginal request price.
- Optimizing average cost while rare failures are extremely expensive.
- Allowing unlimited output and retries.

## Related concepts

- [Evaluation and Operations](../../)
- [Quality and Cost Trade-Offs](../quality-cost-tradeoffs/)
- [Model Routing](../model-routing/)
- [Observability](../observability/)
