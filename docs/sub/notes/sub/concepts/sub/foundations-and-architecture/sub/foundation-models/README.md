# Foundation Models

Legacy residual retained for practical adaptation/integration workflow, model-selection, licensing, and deployment guidance that is intentionally outside the canonical foundation-model classification owner.

> **Migration note:** Foundation-model identity, reusable downstream role, broad-pretraining context, classification boundaries, model-versus-system distinction, adaptation semantics, and non-guarantees around downstream quality/safety are already preserved in `docs/sub/concepts/sub/models/sub/classification/sub/foundation-models/`. The remaining material below stays here until its exact learning, evidence, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Workflow and model-selection residual

A foundation model can be used through zero-shot or few-shot prompting, system prompts, and structured outputs. Downstream systems may also add retrieval, tool execution, or agent orchestration; those are system-integration techniques rather than model adaptation. Fine-tuning, LoRA, and other parameter-efficient methods are model-adaptation options.

Before fine-tuning, test whether prompting, retrieval, or another system-level technique already satisfies the task. Model selection should consider demonstrated capability, task-specific evaluation, license and dataset constraints, privacy requirements, deployment options, inference-resource needs, and dependence on an external provider.

Broad pretraining does not remove the need to evaluate domain accuracy or data freshness, and licensing or provenance constraints can materially affect deployment suitability. These practical workflow and selection consequences remain migration source material until their exact owners are verified.
