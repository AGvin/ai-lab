# Documentation Requirements

## Identity and provenance

- Identify Granite Guardian 4.1 as IBM's safety and risk-evaluation family represented by the 8B checkpoint.
- Preserve the source-backed fine-tuning lineage from the canonical Granite 4.1 8B instruction-tuned checkpoint to Guardian 4.1 8B, with reciprocal model relations. Do not substitute the distinct 8B Base identity.
- Keep safety-model identity separate from application policy engines, moderation services and hosted inference routes.

## Operational decision boundaries

- The 8B card documents built-in and bring-your-own risk criteria, RAG groundedness/context relevance/answer relevance checks, and function-call hallucination evaluation.
- Thinking and non-thinking behavior are model operating modes, not separate trained identities.
- Weights state Apache 2.0. Safety judgments are probabilistic model outputs; deployment policy must validate thresholds, false positives/negatives and failure handling.
- Preserve the prescribed binary yes/no scoring template. Use outside that scoring contract or adversarial inputs may produce unexpected or harmful outputs; do not present this as a general-purpose assistant.

## Validation

- Family membership resolves to Granite Guardian 4.1 8B.
- Producer provenance resolves to IBM.
- The concrete member's derived-from relation resolves to Granite 4.1 8B and its reciprocal has-derivative edge resolves back to the Guardian member.
- This assessment grants no runtime, benchmark-reproduction, cache or final-render credit.
