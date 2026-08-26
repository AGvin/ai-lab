# Documentation Requirements

## Requirements

- Use the reader-facing title `Trustworthy AI`.
- Present trustworthy AI as the socio-technical domain concerned with making AI systems worthy of justified reliance by managing context-specific risks, requirements, controls, evidence, and trade-offs across the full lifecycle rather than declaring a model or product intrinsically `trustworthy`.
- Make clear that trustworthiness is multi-dimensional and context-dependent. Validity/reliability, safety, security/resilience, privacy, fairness/bias, information integrity, uncertainty/calibration, explainability/interpretability, alignment/control, accountability/transparency, and other applicable properties can reinforce or trade off with one another; one strong property does not compensate automatically for a critical weakness in another.
- Distinguish trustworthy-AI characteristics from user trust, confidence, popularity, provider reputation, certification labels, or model self-description. Trust should follow evidence and controls appropriate to the use/risk rather than persuasive behavior or brand identity.
- Distinguish model-level properties from complete-system trustworthiness. Data, prompts/context, retrieval, tools, permissions, human oversight, software, infrastructure, deployment, monitoring, operators, policies, and affected stakeholders can materially determine risks and outcomes even when the underlying model is unchanged.
- Require the context of use and affected parties to shape the trustworthiness question. A system acceptable for low-stakes drafting can be unacceptable for autonomous or consequential decisions without stronger correctness, oversight, privacy, security, accountability, or human-control requirements.
- Treat trustworthiness as lifecycle-aware. Risks and controls can arise during data collection, model training/adaptation, evaluation, deployment, operation, updates, incident response, retirement, and downstream reuse; predeployment evaluation alone is not proof of continuing trustworthiness.
- Distinguish intrinsic capability evidence, empirical evaluations, deterministic controls, process/governance evidence, and operational monitoring. No single benchmark, policy statement, red-team result, or guardrail establishes the whole trustworthiness claim.
- Explain defense in depth. Model training/alignment, prompts/policies, validators, access controls, least privilege, sandboxing, data minimization, monitoring, human oversight, incident recovery, and other controls can address different failure modes; model behavior alone must not be used as the only protection for secrets, permissions, side effects, or safety-critical operations.
- Keep `privacy/` and `alignment-and-control/` as currently materialized selected descendants. Other selected broad trustworthy-AI areas remain architecture-owned but should appear in generated navigation only after they gain substantive canonical material.
- Do not infer or materialize legacy-named child nodes such as prompt injection, indirect prompt injection, trust boundaries, least privilege, sandboxing, secret handling, retrieval poisoning, guardrails, data residency, provenance, content moderation, jailbreaking, or data poisoning until the architecture explicitly selects their exact destinations.
- Distinguish risk management from risk elimination. Controls can reduce likelihood/impact or improve detection/recovery, while residual risk, uncertainty, unknown failure modes, adversarial adaptation, model/provider change, and contextual trade-offs remain and require explicit acceptance/escalation decisions.
- Require evidence scope and currency. Trustworthiness claims should identify the model/system/version, conditions, population/workload, evaluation/control evidence, assumptions, limitations, and date/version when mutable components matter.
- Keep legal/regulatory/compliance obligations distinct from generic concept semantics. Jurisdictional requirements can impose stronger duties or definitions and belong with governance/legal owners rather than being silently universalized.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete incidents, policies, provider terms, regulatory requirements, audit records, evaluation results, red-team findings, system threat models, risk acceptances, and product/project-specific controls with their applicable governance/evidence/project/catalog owners.
- Use the canonical entity references as research inputs for contextual, lifecycle-wide, multi-characteristic trustworthy-AI boundaries when reader-facing rendering is activated.

## Validation

- `Trustworthy AI` is not presented as a binary intrinsic model property, provider badge, popularity signal, or guarantee.
- Model behavior is not treated as sufficient protection for permissions, secrets, privacy, or consequential side effects.
- Trustworthiness claims are scoped to context/use, affected parties, system/version, evidence, and residual risk.
- Trade-offs among trustworthiness properties remain explicit rather than implying that maximizing one characteristic solves the others.
- Architecture-gap legacy leaves are not inferred/materialized from broad selected parents.
- Concrete policies, legal requirements, incidents, evaluation outcomes, and project risk decisions remain outside the reusable domain owner.
- Direct-child navigation contains only currently materialized selected descendants.
