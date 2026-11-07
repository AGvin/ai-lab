# Documentation Requirements

## Requirements

- Identify Braintrust as an AI observability and evaluation platform for tracing, datasets, experiments, scorers/evaluations, prompts, and production quality workflows.
- Preserve the current hybrid deployment boundary: customers may host the sensitive data plane, while Braintrust operates the control plane including the web UI, authentication, and lightweight metadata.
- Explain that customer-hosted data-plane deployment does not make the complete Braintrust product fully self-managed software under the current architecture.
- Keep current observability/evaluation features, data handling, hosting options, plans, and integration support freshness-sensitive.

## Validation

- Braintrust is not misclassified as fully self-hosted software merely because its data plane can run in customer infrastructure.
- Security/data-residency claims match current first-party deployment documentation.

## Scoped original-source qualification — 2026-11-07

- Braintrust provides hosted AI observability and evaluation workflows spanning traces, prompts, datasets, experiments, scorers and review. Official first-party guidance distinguishes fully managed SaaS from a hybrid deployment where the customer hosts the sensitive data plane while Braintrust retains its managed control plane and UI.
- The 2026-01-21 first-party hybrid architecture article identifies control-plane metadata/authentication separately from experiment logs, prompts and traces. These are provider deployment and security assertions, not independent verification of zero data transit, exact residency, SOC 2/HIPAA scope, model training or every tenant setup.
- Verified first-party source 1: https://docs.braintrust.dev/
- Verified first-party source 2: https://www.braintrust.dev/blog/security-data-control
- Scoped hosted-service/source acceptance only, without tenant deployment, authenticated instrumentation/evals, full security/privacy/legal certification audit, repository-wide schema/cache/CI/render, clean pass or final gate.
