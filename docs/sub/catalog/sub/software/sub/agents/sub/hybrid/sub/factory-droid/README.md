# Factory Droid

Factory Droid is Factory's software-development agent and runtime for development workflows across developer machines, CI, remote computers, and enterprise infrastructure. It can participate in planning, implementation, testing, review, and automation while integrating with repositories and other engineering systems.

## Deployment and trust boundary

Factory documents cloud-managed, hybrid enterprise, and fully airgapped deployments with distinct data and network boundaries. Droid runs on user-managed laptops, CI runners, VMs/containers and remote development environments, or on Factory-managed cloud computers. **Droid Computers** are persistent machines provisioned by Factory, retaining files and installed dependencies across sessions with SSH access and idle pause/resume. **Remote Control** connects an operator-owned VPS, workstation or server through a Factory relay; Factory does not maintain that machine. Neither managed computers nor outbound Factory connectivity are required by every deployment.

The Factory App for macOS and Windows is a visual session, diff, preview and review interface alongside the CLI and browser; it does not imply the agent runs on the same machine as the viewer.

Treat repository and organization permissions, generated diffs, integrations, credentials and secrets, model/provider routing, session synchronization, remote access, automation scopes, and merge/deploy/release actions as explicit trust and approval boundaries. For high-autonomy work, Factory recommends hardened containers or isolated VMs, short-lived credentials in CI, and tightly limited network and filesystem access.

## Official resources

- [Factory Droids](https://factory.ai/product/droids)
- [Droid CLI overview](https://docs.factory.ai/cli/getting-started/overview)
- [Network and deployment configuration](https://docs.factory.ai/enterprise/network-and-deployment)
- [Factory App](https://docs.factory.com/factory-app/overview)
- [Factory-managed Droid Computers](https://docs.factory.com/droid-computers/overview)
- [Remote Control for operator-owned machines](https://docs.factory.com/remote-control)
- [The San Francisco AI Factory Inc.](../../../../../../../producers/sub/f/sub/san-francisco-ai-factory-inc/)
