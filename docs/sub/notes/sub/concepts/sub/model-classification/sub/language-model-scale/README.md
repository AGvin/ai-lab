# Small and Large Language Models

Legacy residual retained for operational deployment tendencies, model-selection workflow, portfolio strategy, and classification practice that are intentionally outside the canonical SLM/LLM scale concept owner.

> **Migration note:** SLM/LLM relative-scale semantics, the absence of one universal parameter threshold, scale-versus-deployment separation, quantization non-reclassification, dense/MoE independence, modality/frontier independence, and the need to qualify resource/capability comparisons are already preserved in `docs/sub/concepts/sub/models/sub/classification/sub/language-model-scale/`. The remaining material below stays here until its exact learning, deployment, model-selection, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Operational-pattern residual

In practice, relatively smaller language models are often considered when memory pressure, latency, cost, offline operation, constrained-device deployment, or high request volume matters. Relatively larger models are often considered when broader capacity or stronger measured task performance justifies additional memory, computation, serving infrastructure, or provider cost.

These are deployment and decision tendencies rather than SLM/LLM definitions. A smaller model may be provider-hosted, and a larger model may run locally when the concrete artifact, representation, runtime, and hardware make that feasible.

Ecosystem maturity is also independent from scale: either class may be experimental, emerging, mainstream, or legacy.

## Selection-workflow residual

A practical selection workflow is to:

1. define the task, acceptance threshold, failure cost, privacy boundary, latency target, and budget;
2. test the smallest plausible model on representative inputs in the real target environment;
3. retain it when measured accepted-result quality is sufficient;
4. escalate difficult or uncertain cases to a stronger model only when the measured improvement justifies the additional cost or constraints;
5. validate the complete route rather than assuming parameter count or a scale label predicts success.

Possible portfolio patterns include one generalist larger model, one specialized smaller model, or a cascade in which a smaller model handles routine work and a stronger model handles exceptions.

This workflow and portfolio guidance remain decision-support material rather than scale-concept truth.

## Classification-practice residual

When a concrete comparison uses `SLM` or `LLM`:

- classify the exact model version or artifact rather than only the provider;
- state the comparison context when the scale label could be ambiguous;
- use `Unclear` rather than inventing a threshold that the evidence does not support;
- record parameter counts separately when known and useful;
- for MoE models, distinguish total from active parameters when both matter;
- do not infer local feasibility, runtime cost, or task quality from the scale label alone.

These operational classification practices remain migration source material until their exact model-reference, learning, or decision-support owner is verified.
