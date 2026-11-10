# Documentation Requirements

## Requirements

- Identify Bolt as StackBlitz's hosted AI application and website building service represented by the canonical development-agent service profile at this path.
- Preserve the service boundary: users interact with Bolt through a hosted product and account/workspace model rather than installing Bolt as a standalone local coding agent.
- Preserve useful legacy boundaries around generated-code review, GitHub repository access, design imports, database/hosting/authentication integrations, MCP connectors, secrets, team/workspace permissions, and deployment controls.
- Mention major integration classes only at a stable high level; current official examples include GitHub, Figma, Supabase, Bolt-managed database/hosting, and MCP connectors.
- Keep token budgets, model routing, pricing, plan features, individual integration availability, platform limits, and other mutable service facts source-backed and time-scoped when expanded.
- Include current official Bolt site and help-center references.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The page describes Bolt as a hosted development service rather than local agent software.
- StackBlitz/Bolt product ownership is represented through producer provenance without treating StackBlitz itself as the Bolt service entity.
- Integration descriptions do not imply unlimited permissions or permanent availability.
- Official resource links match canonical entity metadata.
- The page contains no temporary-summary or placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Scoped original-source qualification — 2026-11-07

- Bolt is StackBlitz's hosted AI application builder, with an integrated code editor and JavaScript-based full-stack tooling. Its development environment uses StackBlitz WebContainers, while Bolt Cloud databases, hosting, deployment and connected external systems have separate storage, trust and operational boundaries.
- GitHub integration supports source-control workflows, but connecting a repository or publishing an app does not prove generated code, dependencies, database state or credentials are production-safe. Model selection, limits, pricing, connector support and publishing options are account- and date-sensitive.
- Verified first-party source 1: https://support.bolt.new/get-started/intro-bolt
- Verified first-party source 2: https://support.bolt.new/integrations/git
- Source acceptance is limited to the existing service identity, operator/integration distinctions and documentation-grounded requirements. No authenticated project, connected repository, build, deployment, security/privacy/legal audit, whole-repository clean pass or final-delivery gate was performed.
