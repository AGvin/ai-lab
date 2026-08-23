# Documentation Requirements

## Requirements

- Present `user-scenarios/` as the decision-support journey that starts from a reader's combined real-world situation rather than entity popularity or one isolated task.
- Base scenario routes on the decision maker, common tasks, existing hardware, budget, skills, privacy/data boundary, operational tolerance, and other constraints that materially change the route.
- Treat route examples inherited from the migrated practical-user-scenarios source as legacy evidence last verified there on **2026-07-27** unless a migrated requirement or canonical owner records a later verification. Recheck mutable model/service availability, pricing, limits, terms, and runtime support before presenting those examples as current recommendations.
- Preserve the practical vocabulary needed across scenarios: a managed assistant is provider-operated application access; an API is programmatic hosted access; local means inference on the user's device; self-hosted means the user or organization operates the model service; cloud GPU means rented accelerator capacity with lifecycle/billing responsibility; a quantized model is a separately evaluated lower-precision artifact; RAG retrieves source material before generation but does not guarantee correctness.
- Preserve the common data-boundary rule: public data may use any route meeting quality/cost needs; internal data uses organization-approved routes; confidential data requires an explicitly approved contracted/private/local path; regulated data requires a specifically approved compliant architecture. Evaluate the complete provider chain rather than the visible client alone.
- Treat OpenRouter or another routing intermediary as a service layer, not a model and not an automatic default. For public data, use it only after checking the selected provider and current terms; for internal data, require organization-approved downstream providers and applicable routing/logging/data-retention controls; for confidential data, require approval of both intermediary and downstream provider; for regulated data, use an intermediary only when the complete chain is explicitly approved and otherwise prefer an approved direct/private/local architecture.
- Treat existing hardware as a constraint, not a reason to force local inference. Compare local, hosted, self-hosted, and hybrid routes when they materially differ for the scenario.
- Compare total cost per accepted result, including retries, human correction, administration, electricity, storage, operations, and other material costs rather than subscription/API/inference price in isolation.
- State that self-hosting is not automatically cheaper; local routes are strongest when privacy, offline operation, stable high volume, or provider independence materially justify the operational burden.
- Treat temporary cloud GPU capacity as a candidate for bounded heavy workloads when it is more appropriate than persistent generic CPU infrastructure, while accounting for startup, storage, shutdown, and idle-billing risks.
- Require stronger isolation, least privilege, approval, and independent verification for agentic execution than for conversational assistance when tools or side effects are involved.
- Do not treat multimodal capability, retrieval, or model output as a replacement for deterministic extraction, schema validation, permission enforcement, source verification, or qualified human review where those controls are material.
- Keep canonical model identity and intrinsic facts in `catalog/models/reference/`; keep model-specific task, constraint, and portfolio decision evidence in `catalog/models/selection/decision-guides/` until that owner is separately reviewed. Scenario pages link those owners rather than duplicating complete model profiles or model-specific rankings.
- Link canonical software, services, hardware, runtimes, and deployment material only when those constraints materially affect the route. Do not turn a scenario into the canonical owner of a complete RAG, contact-center, data-platform, security, or infrastructure architecture.
- Recheck mutable prices, quotas, availability, aliases, product features, provider terms, data handling, and access conditions when they materially affect a recommendation.
- Organize direct children by decision scale: `personal/`, `professionals/`, `teams/`, and `organizations/`. Navigate only materialized scenario children; do not create empty scenario nodes merely to mirror the approved logical taxonomy.

## Validation

- Every direct child is one of the four selected audience groups.
- Every materialized scenario has a combined context that materially changes the route, constraints, escalation path, or evaluation contract rather than differing by an incidental label only.
- The page does not present a universal best-model ranking or duplicate complete canonical entity profiles.
- Model-specific decision-guide content remains with `catalog/models/selection/decision-guides/` and is linked rather than duplicated here.
- Data-boundary guidance evaluates the complete provider/client chain and does not imply that a local model endpoint makes an entire workflow local.
- Routing intermediaries are not treated as privacy-neutral or automatically acceptable for internal, confidential, or regulated data.
- Legacy route examples retain the 2026-07-27 evidence boundary until separately revalidated.
- RAG, multimodality, and agent capability are not presented as substitutes for required deterministic, permission, safety, or qualified-review controls.
- Unmaterialized approved scenarios remain absent until real source-backed or newly authored content justifies them.
