# Documentation Requirements

## Requirements

- Identify Factory Droid as Factory's software-development agent and runtime for development workflows across developer machines, CI, remote computers, and enterprise infrastructure.
- Preserve its end-to-end development scope at a high level, including planning, implementation, testing, review, and integration with engineering systems, without turning the catalog profile into setup guidance.
- Distinguish Factory's documented deployment patterns: cloud-managed, hybrid enterprise, and fully airgapped deployment.
- Preserve the current computer/runtime boundary at a stable high level: Droid can run on user-managed laptops, CI runners, VPS/VMs, containers, remote development environments, or Factory-managed computers.
- Distinguish persistent Factory-provisioned Droid Computers (managed cloud agent execution with session state, auto-pause/resume and SSH) from Remote Control connecting to operator-owned VPS, workstations or servers via Factory relay; vendor does not provision or manage the latter.
- Do not imply that Droid requires Factory cloud, Factory-brokered model access, outbound internet, or Factory-managed compute in every supported deployment mode.
- Preserve the Factory App desktop interface for macOS/Windows as a distinct visual session/review surface alongside CLI, web/mobile, without treating the app itself as the location of every agent execution.
- Preserve useful legacy operational boundaries around repository and organization permissions, generated diffs, integrations, credentials/secrets, model/provider routing, session/cloud sync, remote-access relays, automation scopes, and human approval for merge/deploy/release workflows.
- Keep cloud-managed, hybrid and fully airgapped enterprise deployment data boundaries separate; higher-autonomy runs require hardened containers or isolated VMs, least-privilege CI credentials, and restricted network/filesystem access.
- Keep mutable enterprise, security/compliance, integration, pricing, managed-compute, and model-provider claims source-backed when expanded.
- Include current official Factory Droid product, CLI, and deployment documentation.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The profile reflects that Droid can run on laptops, CI infrastructure, VMs/containers/Kubernetes, managed computers, and airgapped environments when configured accordingly.
- Cloud-managed and fully self-contained deployment modes are not collapsed into one execution model.
- Factory cloud/session synchronization and remote-access services are not presented as mandatory for all deployments.
- Factory-managed Droid Computers are not conflated with operator-owned Remote Control machines; enterprise deployment options and desktop review interfaces are not treated as security isolation guarantees.
- Official resource links match canonical entity metadata.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
