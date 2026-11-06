# Documentation Requirements

## Requirements

- Identify AgentOps SDK as the installable Python observability/instrumentation library from `AgentOps-AI/agentops`, not the hosted dashboard, the self-hosted `app/`, an agent framework, or a model API.
- Pin `f8e907b92dabe47232978023fdcb01e2a7d4b752` (June 25, 2026) for the source README, `pyproject.toml` (package `agentops`) and MIT license. This commit is an observed source snapshot, not an assertion of current published package or SaaS versions.
- Describe source-backed Python installation (`pip install agentops`), initialization and session/agent/workflow/operation decorators; framework integration behavior and OpenTelemetry dependencies are version-specific.
- Differentiate SDK instrumentation from cloud dashboard and optional separately deployed self-hosted backend. SDK installation alone neither deploys a service nor grants a dashboard account.
- Agent traces may contain prompts, responses, tool inputs, exceptions, secrets, user identifiers or regulated data. Review redaction/capture settings, collector endpoint, data retention, permissions and consent before enabling production telemetry.
- Apply MIT only to covered repository source. Third-party model APIs, dependencies, cloud terms and recorded customer content have separate contracts and rights.
- No unrelated producer, cloud product or source-repository subdirectory is counted as another frozen identity by this profile.
- Do not claim package installation, sample execution, live trace ingestion, full license/security audit, complete freshness verification, full CI or whole-catalog clean pass.

## Validation

- [Pinned README](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/README.md), [package](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/pyproject.toml), and [MIT source license](https://github.com/AgentOps-AI/agentops/blob/f8e907b92dabe47232978023fdcb01e2a7d4b752/LICENSE) support the bounded profile.
- One canonical observability platform reader is indexed; its SaaS and self-hosted backend boundaries remain explicit.
