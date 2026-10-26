# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-4.1-30b-base` and its Apache-2.0 weight license.
- Preserve this exact base language model for adaptation identity and its checkpoint-specific configuration.
- Preserve the reciprocal `has-derivative` relation to the exact Granite 4.2 30B post-trained model and render a canonical link without suggesting the base release is itself instruction-tuned.
- Do not infer hardware fit from the model name; account for precision, context state, batch size and architecture-specific runtime support.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
