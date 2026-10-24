# Documentation Requirements

## Requirements

- Identify NVIDIA NeMo Agent Toolkit as the released, independently installable, framework-agnostic agent workflow integration, instrumentation, evaluation and optimization toolkit `nvidia-nat`, not the NeMo model framework, NeMo Guardrails, NeMo RL, NVIDIA Dynamo or hosted NVIDIA NIM.
- Preserve published non-prerelease **v1.9.0 (2026-09-10)**, official NVIDIA-maintained Apache-2.0 project identity, and **Python >=3.11,<3.14** support in the current `pyproject.toml`; validate the pinned published version separately from the evolving `main` branch.
- Describe connecting third-party agent frameworks (including LangChain, CrewAI, Agno, ADK, AutoGen and Strands), end-to-end tracing/observability, workflow evaluation/profiling, tool/runtime integrations and optional workflow publishing through FastMCP. The optional `nvidia-nat-*` integration packages are components of one toolkit family, not dozens of independent catalog products.
- **Lifecycle:** latest release notes include breaking removal of `local_sandbox`, identity-resolution changes, authentication preflight and human-in-the-loop middleware. Do not assume examples, tools, framework adapters or profiling features are universally compatible with every installed framework version. Dynamo latency sensitivity is explicitly experimental.
- **Security and cost:** workflow plugins and connectors can access model providers, tools, private datasets and external endpoints. Require pinned dependency constraints, workload isolation, identity/secret management, scope-limited credentials, tracing redaction, approved evaluation datasets and explicit model/token budgets before deployment.
- Attribute the maintained toolkit to the existing `catalog/producers/n/nvidia` with exact `produced-by` / `produces` reciprocity. Do not duplicate NVIDIA's existing provenance for NeMo Guardrails, NIM, Dynamo, hardware and unrelated NeMo modules.

## Validation

- Official NVIDIA source README, published v1.9.0 release, `pyproject.toml`, project `LICENSE.md` and documentation corroborate product identity, release, Python range, license and optional integration scope.
- The existing NVIDIA producer gains exactly one inverse target while preserving all previously materialized relations.
