# Documentation Requirements

## Requirements

- Teach Model Fundamentals as the practical vocabulary needed to reason about model identity, artifacts, families, scales, variants, parameters, inputs, tokenization, and lifecycle choices before architecture- or runtime-specific depth.
- Keep reusable classification definitions with canonical concepts and concrete model/version facts with catalog/evidence owners.
- Explain that broad-pretrained or foundation-model status does not remove the need for task-specific evaluation, freshness checks, license/provenance review, privacy constraints, or deployment-fit verification.
- Distinguish model adaptation from system-level integration: prompting, retrieval, tools, state, and orchestration can change the application without modifying model parameters; fine-tuning and PEFT change or attach model state.
- Establish an evidence-driven selection mindset rather than inferring suitability from family labels, parameter count, popularity, or a generic `LLM` designation.

## Validation

- Model family/scale labels are not treated as complete deployment or quality evidence.
- Application scaffolding is distinguished from model adaptation.
- Mutable model facts remain outside timeless learning truth.
