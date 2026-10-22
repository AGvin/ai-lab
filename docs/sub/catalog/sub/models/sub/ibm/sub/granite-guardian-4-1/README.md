# Granite Guardian 4.1

Granite Guardian 4.1 is IBM's safety and risk-evaluation family represented by the 8B checkpoint.

## Decision and operating boundaries

The model card describes built-in and bring-your-own risk criteria, RAG groundedness/context relevance/answer relevance checks, function-call hallucination evaluation, and thinking/non-thinking use patterns. These outputs support policy decisions but do not themselves enforce application permissions or guarantee safety.

The concrete checkpoint is fine-tuned from `ibm-granite/granite-4.1-8b`. That exact source model is not materialized in the current catalog, so the lineage remains source-documented rather than represented by a broken relation.

The weights state Apache 2.0. Safety thresholds and error tradeoffs require evaluation on the intended policy and traffic.

The [model card](https://huggingface.co/ibm-granite/granite-guardian-4.1-8b) restricts intended use to its prescribed yes/no scoring template. Other use and adversarial inputs can produce unexpected or harmful outputs; this scoring model is not a general-purpose assistant.

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite Guardian 4.1 8B](sub/models/sub/granite-guardian-4-1-8b/) — member.

## Official resources

- <https://huggingface.co/ibm-granite/granite-guardian-4.1-8b>
