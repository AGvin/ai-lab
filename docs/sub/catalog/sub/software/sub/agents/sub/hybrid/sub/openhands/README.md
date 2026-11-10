# OpenHands

OpenHands is an AI-driven software-development platform with **Agent Canvas** as its current browser interface, backed by the Software Agent SDK and Agent Server. Canvas connects to one or more backends running on a laptop, VM, self-hosted server, or OpenHands Cloud. Local and hosted agent execution make this a **Hybrid Agent**. The former Local GUI is a legacy surface, not the recommended current interface.

## Execution and licensing boundaries

The core OpenHands repositories have different responsibilities: `OpenHands/OpenHands` contains Agent Canvas and local-stack orchestration; `OpenHands/software-agent-sdk` owns the SDK, Agent Server, tools, conversation execution and backend API; automation components handle triggers and dispatch. OpenHands Cloud provides hosted execution, while Enterprise can use organization-controlled deployments. The older `OpenHands/agent-canvas` repository is archived; current Canvas lives in `OpenHands/OpenHands`.

Agent Canvas is a **client, not an execution sandbox**. Running the Agent Server directly on a computer gives its tools the permissions of that host/user. For untrusted repository code, use an isolated container or VM, review project mounts, credentials, network exposure and external tool permissions. Check current licensing in each component repository rather than extending the legacy monorepo's `enterprise/` directory terms to the whole ecosystem.

Operational use should treat filesystem and shell access, repository permissions, backend isolation, integration scopes, automation triggers, credentials, and human approval gates as explicit security boundaries.

## Official resources

- [OpenHands documentation](https://docs.openhands.dev/overview/introduction)
- [OpenHands repository](https://github.com/OpenHands/OpenHands)
- [Software Agent SDK and Agent Server](https://github.com/OpenHands/software-agent-sdk)
- [Agent Canvas setup and execution permissions](https://github.com/OpenHands/docs/blob/main/openhands/usage/agent-canvas/setup.mdx)
- [All Hands AI, Inc.](../../../../../../../producers/sub/a/sub/all-hands-ai-inc/)
