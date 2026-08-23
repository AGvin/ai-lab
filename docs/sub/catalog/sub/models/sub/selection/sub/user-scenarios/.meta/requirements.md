# Documentation Requirements

## Requirements

- Present `user-scenarios/` as the model-selection journey that starts from a reader's combined situation rather than model popularity, one isolated task, or one hardware target.
- Base scenario routes on decision maker, common tasks, existing hardware, budget, skills, privacy/data boundary, operational tolerance, and other constraints that materially change the model route.
- Treat migrated route examples as legacy evidence last verified on **2026-07-27** unless a migrated requirement or canonical owner records a later verification; recheck mutable model/service availability, pricing, limits, terms, and runtime support before presenting them as current recommendations.
- Preserve practical vocabulary: managed assistant = provider-operated application access; API = programmatic hosted access; local = inference on the user's device; self-hosted = user/organization-operated model service; cloud GPU = rented accelerator capacity with lifecycle/billing responsibility; quantized model = separately evaluated lower-precision artifact; RAG retrieves source material before generation but does not guarantee correctness.
- Preserve the data-boundary rule: public data may use any route meeting quality/cost needs; internal data uses organization-approved routes; confidential data requires an explicitly approved contracted/private/local path; regulated data requires a specifically approved compliant architecture. Evaluate the complete provider chain.
- Treat routing intermediaries as service layers, not models or automatic privacy defaults; approve the intermediary and downstream provider chain appropriate to the data class.
- Treat existing hardware as a constraint, not a reason to force local inference. Compare local, hosted, self-hosted, and hybrid routes when materially different.
- When fixed/owned hardware becomes the primary selection question, link the sibling `../hardware/` journey and its most relevant group/specialization rather than duplicating detailed fit analysis in the scenario.
- Compare total cost per accepted result, including retries, human correction, administration, electricity, storage, operations, and other material costs.
- State that self-hosting is not automatically cheaper; local routes are strongest when privacy, offline operation, stable high volume, or provider independence materially justify operational burden.
- Treat temporary cloud GPU capacity as a candidate for bounded heavy workloads when more appropriate than persistent infrastructure, while accounting for startup, storage, shutdown, and idle-billing risks.
- Require stronger isolation, least privilege, approval, and independent verification for agentic execution than conversational assistance when tools or side effects are involved.
- Do not treat multimodality, retrieval, or model output as a replacement for deterministic extraction, schema validation, permission enforcement, source verification, or qualified human review where controls are material.
- Keep canonical model identity/facts in Model Reference and task-specific evidence in sibling `decision-guides/`; scenario pages link those owners rather than duplicating profiles.
- Link software, services, hardware, runtimes, deployment material, and sibling hardware selection only when they materially affect the model route. Do not turn a scenario into canonical solution architecture.
- Organize direct children by decision scale: `personal/`, `professionals/`, `teams/`, `organizations/`. Navigate only materialized scenario children; do not create empty nodes merely to mirror the logical taxonomy.

## Validation

- Every direct child is one of the four selected audience groups.
- Every materialized scenario has combined context that materially changes route, constraints, escalation, or evaluation rather than an incidental label.
- The page does not present a universal best-model ranking or duplicate complete model/hardware profiles.
- Data-boundary guidance evaluates the complete provider/client chain.
- Legacy route examples retain the 2026-07-27 evidence boundary until separately revalidated.
- Hardware-specific fit is delegated to `../hardware/` when hardware itself becomes the primary question.
- Unmaterialized approved scenarios remain absent until substantive source-backed/newly authored content justifies them.
