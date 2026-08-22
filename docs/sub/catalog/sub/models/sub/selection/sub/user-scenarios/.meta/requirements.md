# Documentation Requirements

## Requirements

- Present `user-scenarios/` as the model-selection journey that starts from a reader's combined situation rather than model popularity or one isolated task.
- Base scenario routes on the decision maker, common tasks, existing hardware, budget, skills, privacy/data boundary, operational tolerance, and other constraints that materially change the model route.
- Preserve the practical vocabulary needed across scenarios: a managed assistant is provider-operated application access; an API is programmatic hosted access; local means inference on the user's device; self-hosted means the user or organization operates the model service; cloud GPU means rented accelerator capacity with lifecycle/billing responsibility; a quantized model is a separately evaluated lower-precision artifact; RAG retrieves source material before generation but does not guarantee correctness.
- Preserve the common data-boundary rule: public data may use any route meeting quality/cost needs; internal data uses organization-approved routes; confidential data requires an explicitly approved contracted/private/local path; regulated data requires a specifically approved compliant architecture. Evaluate the complete provider chain rather than the visible client alone.
- Treat OpenRouter or another routing intermediary as a service layer, not a model and not an automatic default. Use an intermediary only when its routing/access value justifies the additional provider and data boundary.
- Treat existing hardware as a constraint, not a reason to force local inference. Compare local, hosted, self-hosted, and hybrid routes when they materially differ for the scenario.
- Compare total cost per accepted result, including retries, human correction, administration, electricity, storage, operations, and other material costs rather than subscription/API/inference price in isolation.
- State that self-hosting is not automatically cheaper; local routes are strongest when privacy, offline operation, stable high volume, or provider independence materially justify the operational burden.
- Treat temporary cloud GPU capacity as a candidate for bounded heavy workloads when it is more appropriate than persistent generic CPU infrastructure, while accounting for startup, storage, shutdown, and idle-billing risks.
- Require stronger isolation, least privilege, approval, and independent verification for agentic execution than for conversational assistance when tools or side effects are involved.
- Do not treat multimodal capability, retrieval, or model output as a replacement for deterministic extraction, schema validation, permission enforcement, source verification, or qualified human review where those controls are material.
- Keep canonical model identity and intrinsic facts in Model Reference and task-specific model selection evidence in sibling `decision-guides/`; scenario pages link those owners rather than duplicating complete profiles.
- Link software, services, hardware, runtimes, and deployment material only when those constraints materially affect the model route. Do not turn a scenario into the canonical owner of a complete RAG, contact-center, data-platform, security, or infrastructure architecture.
- Recheck mutable prices, quotas, availability, aliases, product features, provider terms, data handling, and access conditions when they materially affect a recommendation.
- Organize direct children by decision scale: `personal/`, `professionals/`, `teams/`, and `organizations/`. Navigate only materialized scenario children; do not create empty scenario nodes merely to mirror the approved logical taxonomy.

## Validation

- Every direct child is one of the four selected audience groups.
- Every materialized scenario has a combined context that materially changes the route, constraints, escalation path, or evaluation contract rather than differing by an incidental label only.
- The page does not present a universal best-model ranking or duplicate complete model profiles.
- Data-boundary guidance evaluates the complete provider/client chain and does not imply that a local model endpoint makes an entire workflow local.
- RAG, multimodality, and agent capability are not presented as substitutes for required deterministic, permission, safety, or qualified-review controls.
- Unmaterialized approved scenarios remain absent until real source-backed or newly authored content justifies them.
