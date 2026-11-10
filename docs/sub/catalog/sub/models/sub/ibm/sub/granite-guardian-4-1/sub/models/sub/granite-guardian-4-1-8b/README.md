# Granite Guardian 4.1 8B

Granite Guardian 4.1 8B is IBM's 8B-class text safety and risk-evaluation model.

The model card describes built-in and bring-your-own risk criteria, RAG groundedness/context relevance/answer relevance checks, function-call hallucination evaluation, and thinking/non-thinking operating modes. Its source is the canonical Granite 4.1 8B instruction-tuned model, distinct from Granite 4.1 8B Base; reciprocal provenance relations connect the two concrete models.

Weights state Apache 2.0. A Guardian output is a model judgment, not a policy enforcement guarantee; applications still need thresholds, access controls, escalation and representative evaluation.

The [model card](https://huggingface.co/ibm-granite/granite-guardian-4.1-8b) restricts intended use to its prescribed yes/no scoring template. Other use and adversarial inputs can produce unexpected or harmful outputs; this scoring model is not a general-purpose assistant.

## Catalog relations

- [Granite Guardian 4.1](../../../../) — family.
- [Granite 4.1 8B](../../../../../granite-4-1/sub/models/sub/granite-4-1-8b/) — instruction-tuned fine-tuning source; its assistant role is separate from Guardian's scoring contract.

## Official resources

- <https://huggingface.co/ibm-granite/granite-guardian-4.1-8b>
