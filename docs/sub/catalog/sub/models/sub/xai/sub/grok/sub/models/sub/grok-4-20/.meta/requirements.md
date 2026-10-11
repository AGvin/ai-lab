# Documentation Requirements

## Requirements

- Identify Grok 4.20 as the durable trained-model identity represented by xAI's current 4.20 reasoning/non-reasoning serving variants.
- Preserve the current text/image input, text output, 1M-token context, agentic tool-calling, structured-output, and long-context boundary only while first-party documentation supports those facts.
- Treat `grok-4.20-0309-reasoning` and `grok-4.20-0309-non-reasoning` as concrete serving/snapshot variants of the represented Grok 4.20 identity rather than duplicating near-identical peer catalog models.
- Treat the current `grok-4.20-multi-agent-0309` beta surface as a model-serving variant that changes the reasoning-effort control into multi-agent collaboration/agent-count behavior; do not promote it to a peer trained-model identity unless later lifecycle establishes independent weights/product identity.
- Keep aliases, beta aliases, clusters, pricing, long-context thresholds, rate limits, batch support, and multi-agent beta lifecycle freshness-sensitive.
- Keep Grok 4.20 distinct from current default/flagship Grok 4.7 and from Grok 4.6; do not infer numeric-version ordering as release recency.

## Validation

- Serving-mode/snapshot aliases are not duplicated as standalone nodes.
- Multi-agent beta is not presented as a separate trained model without stronger upstream evidence.
- Current API availability is not mistaken for default provider recommendation.
