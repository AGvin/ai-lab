# Documentation Requirements

## Requirements

- Identify Boomi Agent Control Plane as Boomi's launched enterprise AI control-plane identity for connecting, governing, observing, securing, and optimizing agentic workloads across native and third-party agents, models, tools, skills, and enterprise systems.
- Preserve its placement under `ai-management-platforms`: the product's primary identity is organization-wide control and lifecycle management even though its current surface integrates connectivity, gateway, context, orchestration, build, and runtime capabilities.
- Keep Boomi Agentstudio/Agent Garden/Control Tower, Boomi Connect, Boomi AI Gateway, Boomi Orchestrate, Meta Hub, and Boomi Runtime as component/product surfaces rather than automatically creating peer catalog identities from the umbrella control-plane page; materialize them separately only when a future task establishes an independently useful canonical boundary.
- Preserve the documented deployment breadth across public cloud, customer VPC, and on-premises without classifying the whole product as self-managed software; control-plane ownership and runtime placement are separate concerns.
- Treat provider integrations, exact governance/observability features, pricing, certifications, deployment modes, lifecycle status, and component availability as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains an enterprise AI management/control-plane service rather than a generic integration platform or an individual agent builder.
- Component-level early-access or coming-soon features are not generalized to the launched Agent Control Plane product identity.
- Producer provenance resolves to Boomi.

## Scoped original-source qualification — 2026-11-06

- Boomi's September 2026 first-party announcement places the managed Agent Control Plane around enterprise-wide agent connectivity, governance, cost control and observability across third-party and Boomi-native workloads. Its product can be deployed with Boomi-operated cloud, a customer's VPC or on premises; the location of an execution component does not automatically make the managed control-plane product independently self-hosted open-source software.
- Agentstudio's Agent Designer, Agent Garden and Agent Control Tower are established product components; Boomi AI Gateway, connectors, Orchestrate and runtimes may have distinct release/entitlement scopes. Do not count each branded subsystem as a new canonical agent-control-plane identity without a separate lifecycle decision.
- Availability, customer data residency, agent approval workflow, token custody, actual usage billing and feature-level lifecycle depend on plan, region and integration. Boomi's sovereignty/security claims are publisher claims, not independent compliance proof.
- Verified first-party source 1: https://boomi.com/resources/resources-library/boomi-infrastructure-enterprise-ai-control/
- Verified first-party source 2: https://help.boomi.com/docs/Atomsphere/Platform/Quickstart_Agentstudio
- Verified first-party source 3: https://boomi.com/blog/everything-you-want-to-know-about-the-september-2026-boomi-integration-and-automation-platform-release/
- Scope is source-backed existing governance/registry service identity and publisher-documented operational boundaries only. No new entity/metadata, independent compliance/security/runtime proof, comprehensive freshness audit, whole-repository schema/cache/CI/render, reader-repair, clean pass, final gate or merge credit.
