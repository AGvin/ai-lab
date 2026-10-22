# Granite Guardian 4.1 8B

Granite Guardian 4.1 8B is IBM's 8B-class text safety and risk-evaluation model.

The model card describes built-in and bring-your-own risk criteria, RAG groundedness/context relevance/answer relevance checks, function-call hallucination evaluation, and thinking/non-thinking operating modes. Its source model is `ibm-granite/granite-4.1-8b`; that source is not a current canonical catalog node, so no local derived-from relation is invented.

Weights state Apache 2.0. A Guardian output is a model judgment, not a policy enforcement guarantee; applications still need thresholds, access controls, escalation and representative evaluation.

The [model card](https://huggingface.co/ibm-granite/granite-guardian-4.1-8b) restricts intended use to its prescribed yes/no scoring template. Other use and adversarial inputs can produce unexpected or harmful outputs; this scoring model is not a general-purpose assistant.

## Catalog relations

- [Granite Guardian 4.1](../../../../) — family.

## Official resources

- <https://huggingface.co/ibm-granite/granite-guardian-4.1-8b>
