# kagent

**kagent** is an Apache-2.0-licensed, Kubernetes-native framework for building, deploying and operating AI agents as declarative Kubernetes resources. It is a CNCF Sandbox project.

## Architecture and lifecycle

The [pinned source README](https://github.com/kagent-dev/kagent/blob/e3b807935db59cfb161f87e898d8e203715a5b79/README.md) describes **Harness**, **AgentTemplate**, **Agent**, and **Session** resources, a controller, an optional UI, **Agent Substrate** for agent execution and a PostgreSQL-backed session store. Agents use selected model providers and MCP/tool integrations; these are dependencies, not additional instances of the kagent software identity.

The [kagent 1.x installation guide](https://kagent.dev/docs/kagent/1.x/setup/installation/) describes CLI/Helm deployment with a Kubernetes 1.37+ cluster. It expressly distinguishes 1.x from the older 0.10.x line and warns against an in-place upgrade of the old custom resources. Select a documented release and matching migration procedure before deploying or upgrading.

## Operational boundaries

Agent tools can inspect or change Kubernetes resources. Scope Kubernetes RBAC, service accounts, namespaces, network access, tool permissions, provider keys, cost limits and approval gates. The [1.x platform overview](https://kagent.dev/docs/kagent/1.x/about/what-is-kagent/) notes that the open-source gRPC API authorizes any caller who can reach the endpoint; do **not** expose this endpoint without suitable network isolation and external authentication/authorization controls. Sessions, traces, prompts and tool results may contain sensitive data.

The [Apache-2.0 source license](https://github.com/kagent-dev/kagent/blob/e3b807935db59cfb161f87e898d8e203715a5b79/LICENSE) applies to covered project code, not to model-provider contracts or third-party assets. This profile is source-backed documentation only; no cluster, agent execution, complete audit or whole-catalog clean pass was verified.

## Official resources

- [kagent repository](https://github.com/kagent-dev/kagent)
- [Pinned README](https://github.com/kagent-dev/kagent/blob/e3b807935db59cfb161f87e898d8e203715a5b79/README.md)
- [Versioned installation guide](https://kagent.dev/docs/kagent/1.x/setup/installation/)
- [Platform and security boundary](https://kagent.dev/docs/kagent/1.x/about/what-is-kagent/)
- [Pinned Apache-2.0 LICENSE](https://github.com/kagent-dev/kagent/blob/e3b807935db59cfb161f87e898d8e203715a5b79/LICENSE)
