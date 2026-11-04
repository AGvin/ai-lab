# Documentation Requirements

## Requirements

- Identify Sim as a self-hostable integrated AI workspace for authoring and running agents and workflows, knowledge, files and monitoring. Visual workflows are a feature; the canonical owner is the Integrated Workspaces category.
- Pin upstream commit `f3596f0c0ee1d0a39d6f5df0480fae7703f24653` (2026-11-03) and the first-party README and Apache-2.0 LICENSE; avoid unsupported claims about pricing, runtime benchmarks or every deployed component's licensing.
- Distinguish Sim Cloud (vendor-operated), self-hosted core (Docker Compose or Kubernetes), desktop client, and separately licensed enterprise features. Do not infer that Apache-2.0 covers all enterprise functions in production.
- Reference official [self-hosting](https://docs.sim.ai/platform/self-hosting) guidance and note the operational dependencies on database, Redis, secrets, storage, scheduled jobs and external model integrations. Match CLI examples and requirements to an explicitly pinned release at installation time.
- Treat model/API credentials, connected third-party systems, uploaded documents, workflow logs, user identities, encrypted state, database/volume backups and resource/cost budgets as deployment concerns. A self-hosted control plane does not make external integrations private.
- Do not claim live deployment, self-host setup, application testing, model requests, legal audit, full CI, or whole-catalog clean pass.

## Validation

- First-party source, documentation and license confirm software identity and its self-hosted versus cloud/enterprise boundaries.
- Exactly one canonical Sim profile is indexed under Integrated Workspaces and no hosted service is silently added.
