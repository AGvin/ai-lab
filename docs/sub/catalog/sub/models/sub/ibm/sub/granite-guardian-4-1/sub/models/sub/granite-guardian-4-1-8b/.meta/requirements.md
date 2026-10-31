# Documentation Requirements

## Identity and provenance

- Identify Granite Guardian 4.1 8B as the concrete 8B-class safety and risk-evaluation model in the Granite Guardian 4.1 family.
- Resolve source-backed fine-tuning provenance to the canonical Granite 4.1 8B instruction-tuned model with reciprocal derived-from/has-derivative relations; keep its assistant role distinct from Guardian's scoring contract.

## Operational decision boundaries

- Preserve support for built-in and custom criteria, RAG groundedness/context relevance/answer relevance checks and function-call hallucination evaluation at exact model-card scope.
- Thinking/non-thinking modes do not create separate model identities.
- Weights state Apache 2.0. Model judgments require application-owned thresholds, policy mapping, escalation and representative false-positive/false-negative testing.
- Preserve the prescribed binary yes/no scoring template. Use outside that scoring contract or adversarial inputs may produce unexpected or harmful outputs; do not present this as a general-purpose assistant.

## Validation

- Membership resolves to Granite Guardian 4.1.
- The exact instruction-tuned source and both provenance endpoints resolve; do not link to Granite 4.1 8B Base.
- This assessment grants no runtime or benchmark-reproduction credit.
