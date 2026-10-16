# NVIDIA NeMo Agent Toolkit

NVIDIA NeMo Agent Toolkit (`nvidia-nat`) is an open-source **Apache-2.0** toolkit for integrating, profiling, tracing and evaluating agent workflows. It is framework-agnostic rather than a hosted agent service.

## Integrations and lifecycle

It connects frameworks including LangChain, CrewAI, Agno, Google ADK, AutoGen and Strands, and supports evaluation, observability, profiling and optional FastMCP workflow publishing. The `nvidia-nat-*` integration packages are components of one toolkit family.

The canonical record lists non-prerelease **v1.9.0 (2026-09-10)** and current source metadata **Python >=3.11,<3.14**. Breaking changes include removal of `local_sandbox` and changes to identity, authentication and human-in-the-loop middleware. Verify selected release/adapters; latency-sensitive integrations can be experimental.

This toolkit is distinct from NeMo training, NeMo Guardrails, NeMo RL, Dynamo and NIM.

## Security

Connected tools may touch confidential datasets, model-provider credentials, networks and telemetry sinks. Use least-privilege identities, pinned dependencies, approved data, trace redaction and explicit token/cost budgets.

## Relations

- Produced by: [NVIDIA](../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Documentation](https://docs.nvidia.com/nemo/agent-toolkit/latest/)
- [Repository](https://github.com/NVIDIA/NeMo-Agent-Toolkit)
- [Releases](https://github.com/NVIDIA/NeMo-Agent-Toolkit/releases)
