# Documentation Requirements

## Requirements

- Identify Factory Droid as Factory's software-development agent and runtime for development workflows across developer machines, CI, remote computers, and enterprise infrastructure.
- Preserve its end-to-end development scope at a high level, including planning, implementation, testing, review, and integration with engineering systems, without turning the catalog profile into setup guidance.
- Distinguish Factory's documented deployment patterns: cloud-managed, hybrid enterprise, and fully airgapped deployment.
- Preserve the current computer/runtime boundary at a stable high level: Droid can run on user-managed laptops, CI runners, VPS/VMs, containers, remote development environments, or Factory-managed computers.
- Do not imply that Droid requires Factory cloud, Factory-brokered model access, outbound internet, or Factory-managed compute in every supported deployment mode.
- Preserve useful legacy operational boundaries around repository and organization permissions, generated diffs, integrations, credentials/secrets, model/provider routing, session/cloud sync, remote-access relays, automation scopes, and human approval for merge/deploy/release workflows.
- Keep mutable enterprise, security/compliance, integration, pricing, managed-compute, and model-provider claims source-backed when expanded.
- Include current official Factory Droid product, CLI, and deployment documentation.
- Preserve The San Francisco AI Factory Inc. as the canonical producer through the physically materialized `produced-by` relation when the reciprocal producer `produces` relation resolves successfully.

## Validation

- The profile reflects that Droid can run on laptops, CI infrastructure, VMs/containers/Kubernetes, managed computers, and airgapped environments when configured accordingly.
- Cloud-managed and fully self-contained deployment modes are not collapsed into one execution model.
- Factory cloud/session synchronization and remote-access services are not presented as mandatory for all deployments.
- The Factory/Factory Droid `produces` / `produced-by` relation pair is physically present at both endpoints, semantically consistent, and resolves to canonical profiles.
- Official resource links match canonical entity metadata.
