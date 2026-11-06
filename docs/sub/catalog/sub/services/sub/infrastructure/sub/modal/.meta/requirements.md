# Documentation Requirements

## Requirements

- Present Modal as a producer-operated serverless compute platform for running compute-intensive applications and AI workloads, including GPU-backed functions and endpoints.
- Explain its infrastructure role through workload execution, autoscaling/serverless operation, GPU access, scheduled/batch jobs, and sandbox capability where current first-party documentation supports those surfaces.
- Keep individual model identity and model benchmark claims with their canonical model owners rather than treating models runnable on Modal as Modal products.
- Treat exact GPU inventory, prices, quotas, cold-start behavior, regions, and limits as freshness-sensitive claims requiring current verification.
- Do not split each Modal execution primitive into a separate catalog service unless it develops an independently durable product identity.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Modal is clearly classified as hosted infrastructure rather than an installable inference runtime.
- Mutable infrastructure details are time-scoped when stated.
- Producer provenance resolves to Modal Labs, Inc.

## Scoped original-source qualification — 2026-11-06

- Modal is a hosted serverless compute platform for developer-operated functions, GPU applications, batch workloads and secured web-serving endpoints, not a pretrained model producer. Modal's current docs also offer dedicated/shared LLM Endpoints and sandbox/server primitives, which should not be misclassified as unrelated independent provider identities without a distinct ownership decision.
- Exact GPU types, server scaling and preemption, regions, deployment/authentication patterns, instance startup, project scopes, persistence, cost and usage credits are mutable plan/implementation properties. An OpenAI-compatible model endpoint deployed on Modal is still customer/model-owned code, not a Modal-authored trained model.
- Verified first-party source 1: https://modal.com/docs
- Verified first-party source 2: https://modal.com/docs/cli/latest/endpoint
- Verified first-party source 3: https://modal.com/docs/sdk/py/releases
- Scope: originally documented hosted service identity and lifecycle/usage limits only; not a complete freshness/legal/security review, independent runtime execution, full schema/cache/CI/render, clean pass or final delivery gate.
