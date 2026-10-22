# Documentation Requirements

## Requirements

- Represent FlowState R1 as a series-level release surface rather than a single checkpoint.
- Preserve the official default r1.0 state and the materially updated r1.1 revision as revision-sensitive members of that release surface; loading r1.1 requires an explicit `revision="r1.1"` selector.
- Do not invent separate child identities solely from revision names until a later intake establishes that those trained checkpoints need durable catalog nodes.
- Preserve current operating boundaries from first-party guidance: FlowState currently supports zero-shot forecasting; choose temporal scaling from the actual sampling rate and seasonality; IBM recommends forecasting no more than 30 seasons because quality declines beyond that horizon.
- Preserve sampling-rate adaptation, context, parameter count, benchmark claims, and commercial/research release distinctions only from current first-party sources.

## Validation

- Membership resolves to Granite Time Series.
- The canonical ID is unchanged and the taxonomy correction adds no Model denominator node.
- Reader guidance distinguishes default r1.0 loading from explicit r1.1 selection.
- Reader guidance preserves zero-shot, seasonality-aware scaling, and the 30-season recommendation without turning source-scoped guidance into a universal runtime guarantee.