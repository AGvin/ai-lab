# Sim AI Workspace

**Sim** is a collaborative workspace for visually building, deploying and monitoring AI agents and workflows. Its application also brings together chat, data tables, files, knowledge sources and integrations; this profile describes the **self-hostable core software**, rather than the Sim Cloud service.

## Deployment choices

The [pinned upstream README](https://github.com/simstudioai/sim/blob/f3596f0c0ee1d0a39d6f5df0480fae7703f24653/README.md) documents a setup wizard for self-hosting and a separate managed cloud/desktop experience. The [self-hosting guide](https://docs.sim.ai/platform/self-hosting) covers Docker Compose and Kubernetes deployments and their application, database, Redis, scheduled-job and storage dependencies. Choose a documented version and its matching installation toolchain rather than assuming current instructions work for historical releases.

The [official introduction](https://docs.sim.ai/introduction) distinguishes the Apache-2.0 core from enterprise features under a separate license and production-subscription terms. Do not equate source access with unlimited entitlement to every hosted or enterprise capability.

## Operations, privacy and rights

Self-hosting changes where application state runs but does not prevent workflow connectors or selected model providers from receiving data. Limit third-party API scopes, workflow tool permissions, uploaded content, logs, schedules and provider costs; encrypt and protect credentials and back up database records, file assets and required keys together. Review third-party and enterprise terms separately from the [core source license](https://github.com/simstudioai/sim/blob/f3596f0c0ee1d0a39d6f5df0480fae7703f24653/LICENSE).

This is a source-backed catalog profile. No installation, agent run, enterprise-entitlement verification, deployment security audit, or whole-catalog clean pass was performed.

## Official resources

- [Sim source repository](https://github.com/simstudioai/sim)
- [Pinned README](https://github.com/simstudioai/sim/blob/f3596f0c0ee1d0a39d6f5df0480fae7703f24653/README.md)
- [Sim documentation](https://docs.sim.ai/introduction)
- [Self-hosting guide](https://docs.sim.ai/platform/self-hosting)
- [Pinned Apache-2.0 LICENSE](https://github.com/simstudioai/sim/blob/f3596f0c0ee1d0a39d6f5df0480fae7703f24653/LICENSE)
