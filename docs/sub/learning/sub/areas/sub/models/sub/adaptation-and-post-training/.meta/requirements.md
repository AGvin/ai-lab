# Documentation Requirements

## Requirements

- Teach Adaptation and Post-Training as changing a pretrained model after base training while distinguishing it from prompting, retrieval, ordinary inference controls, and pretraining from scratch.
- Materialize only source-backed selected descendants needed by the current package: `fine-tuning/` and `supervised-post-training/`.
- Start from explicit target behavior and acceptance criteria, compare against lower-lifecycle-cost application techniques where relevant, and keep unchanged-base baselines for matched evaluation.
- Preserve exact base/artifact identity, tokenizer or processor assumptions, dataset lineage, training configuration, evaluation evidence, and deployment/runtime compatibility needed to reproduce or audit an adaptation.
- Evaluate target improvements together with important retained capabilities, representative failure cases, and regressions; training loss alone is not sufficient evidence.
- Keep concrete artifact facts, current runtime support, licensing details, and mutable compatibility with catalog/evidence owners.

## Validation

- Adaptation is not presented as a dependable replacement for fresh attributable knowledge retrieval.
- Training, validation, and final holdout evidence remain distinguishable where needed.
- Resulting artifacts remain traceable to their base and training/evaluation provenance.
