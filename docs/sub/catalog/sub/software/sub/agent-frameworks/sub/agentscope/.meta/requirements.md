# Documentation Requirements

## Requirements

- Identify AgentScope as the independently released Python agent/multi-agent development framework from the `agentscope-ai/agentscope` first-party project, with source authorship attributed to the SysML team of Alibaba Tongyi Lab; do not conflate it with the existing AutoGen, CrewAI, Microsoft Agent Framework or Google ADK products.
- Preserve published non-prerelease **v2.0.10 (2026-10-12)** and **Apache-2.0** source license. The current project requires **Python >=3.11** and declares a **Beta** package-classifier status despite its README's production-ready language. Do not overstate maturity of every optional service/runtime surface.
- Describe model-agnostic tool-using agents, multi-agent team/pipeline orchestration, agent-service deployment, optional A2A interactions, storage/memory and sandbox workspace backends. Model providers, Kubernetes/E2B/Daytona sandboxes, speech APIs and monitoring backends are integrations/dependencies, not AgentScope-owned product clones.
- **Lifecycle and compatibility:** voice/WebRTC and SOP features are explicitly marked experimental in current release news; require per-version review before treating them as stable interfaces. Independently verify specific provider SDK, supported MCP/A2A protocol version and runtime deployment before recommending integrations.
- **Security and operation:** the framework can execute tools and connect to remote sandboxes or model APIs. Explicitly scope trusted inputs, credentials, network access, tool permissions, data transfer, logging and runtime isolation; examples or optional `service`/workspace extras are not turnkey hardening.
- Reuse the already canonical Alibaba Group producer via exact `produced-by` / `produces` inverse. Preserve the existing Higress provenance, and retain team-level authorship in text without fabricating an independent corporate producer for AgentScope or a separate SaaS identity.

- AgentScope 2.0 incorporates AgentScope Runtime capabilities; the former standalone runtime repository now recommends migration to the maintained framework and should be labeled historical, not a separately maintained deployment recommendation.
- For tool sandboxes, API deployment and experimental realtime/A2A integrations, independently review permissions, service authentication, sandbox configuration, network access, secret scopes and log retention instead of assuming the framework isolates the whole process.

## Validation

- Official repository README, release metadata, package manifest and LICENSE support release, author, Python support, license, beta-classifier and experimental-feature boundaries.
- Software link has exact reciprocal `produces` target at `catalog/producers/a/alibaba-group` without losing its existing Higress inverse.
