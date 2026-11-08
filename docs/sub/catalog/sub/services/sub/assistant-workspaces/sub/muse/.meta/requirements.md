# Documentation Requirements

## Requirements

- Identify Muse as Meta's hosted personal AI agent product launched in September 2026, distinct from the Muse model family and from the Meta AI assistant product surface.
- Keep the hosted-service classification explicit: Muse runs on Meta-operated Muse Secure VM infrastructure and can continue delegated tasks after the user closes the client, while users interact through Muse apps/web and supported messaging surfaces.
- Cover the current product boundary at a durable level: goal/task planning, browser-mediated actions, connected apps, background work, memory/personal context, user approvals, credentials/payment integrations, and auditability are product capabilities rather than separate catalog entities unless later independently materialized.
- Preserve the security/privacy architecture only to the depth supported by current first-party sources, including dedicated Muse Secure VM, Sentinel mediation, user approval for sensitive actions, credential isolation, connection permissions, and audit trails.
- Treat Muse Confidential VM, additional payment/login integrations, AI-glasses support, international rollout, plan limits/pricing, supported apps, and other announced future or mutable surfaces as freshness-sensitive; do not present coming-soon features as currently released.
- Keep underlying Muse Spark model identities with the model catalog; product model routing/version changes belong here only as mutable access context.
- Keep availability explicitly scoped: initial first-party launch rollout is in the United States on iOS, Android, and web, with broader surfaces/regions subject to current verification.
- Include producer relations and official resources during scoped reader reconciliation. Repository-wide final rendering and cache/freshness certification remain separate final gates.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- Muse service and Muse model family are not collapsed into one identity.
- Roadmap features such as Confidential VM or future client/integration availability are not presented as already released.
- Hosted execution/security claims stay tied to current Meta documentation rather than generalized to all personal agents.

## Scoped original-source qualification — 2026-11-08

- **Muse** is Meta's separately published personal hosted AI agent introduced **September 8, 2026**, distinct from Meta AI assistant and the Muse Spark model. Meta's original launch describes a **dedicated Muse Secure VM**, browser, connected tools and background task continuation after clients close, with rollout in the US on iOS, Android and web at launch.
- Meta's independent in-depth engineering disclosure states that an isolated agent runtime cell is separated from credential and privileged connector workers; **Sentinel mediates network egress and connected-app actions**, with narrowly scoped approvals, audit trails and separate credential storage. These are **vendor design and enforcement claims**, not proof of absolute attack resistance, independent security validation or absence of agent mistakes.
- As of the launch publication, Confidential VM, additional payment/login integrations and AI-glasses support were presented as upcoming and must not be silently described as GA. Current pricing, app/region eligibility, user data processing, opt-out/training controls, memory and connected account permissions require rechecking for a particular deployment.
- First-party original product and security sources: https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ ; https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse .
- Scoped original-source acceptance qualifies one already materialized hosted service, original publisher, launch, deployment and permission-risk boundaries. No live Muse session, user records or credentials touched, independent safety/privacy/legal audit, full source freshness, global schema/cache/CI/render, clean or final gates.
