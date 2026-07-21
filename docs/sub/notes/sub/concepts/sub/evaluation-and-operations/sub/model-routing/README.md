# Model Routing

Model routing dynamically selects a model or configuration for each request according to task type, risk, cost, latency, or capability requirements.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A router may use explicit rules, user choices, classifiers, confidence estimates, or staged escalation. Simple tasks go to a fast inexpensive model, while difficult or high-risk tasks use a stronger model or human review.

## Practical patterns

- Route images only to multimodal models.
- Send extraction to a small structured-output model.
- Escalate failed or low-confidence tasks.
- Prefer local models for sensitive data.
- Use a fallback provider during outages.

## Trade-offs and limitations

Routing adds classification errors and operational complexity. A cheap model may incorrectly judge a task as easy. Different models can produce inconsistent style, schemas, or safety behavior.

## Good practice

Log routing decisions and outcomes. Evaluate the complete policy against a single-model baseline. Define hard capability constraints before cost optimization and prevent sensitive requests from crossing prohibited boundaries.

## Common mistakes

- Routing only by prompt length.
- Letting an untrusted prompt choose a privileged model or toolset.
- Measuring cost reduction without quality regressions.
- Omitting version and availability handling.

## Related concepts

- [Evaluation and Operations](../../)
- [Model Selection](../model-selection/)
- [Fallback Models](../fallback-models/)
- [Autonomy Levels](../../../agents-and-automation/sub/autonomy-levels/)
