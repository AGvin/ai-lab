# Documentation Requirements

## Requirements

- Identify CAMEL (`camel-ai`) as the independently released, community-maintained Python multi-agent simulation, role-playing and synthetic-data generation framework, not a CAMEL research paper, hosted service, benchmark dataset or alias of AgentScope, CrewAI or AutoGen.
- Preserve latest first-party published non-prerelease **v0.2.90 (2026-03-22)** while noting that the checked `master` branch package manifest advertises an **unreleased 0.2.91a7** development version. Do not present the latter as a GA release. The canonical software is distributed as `camel-ai`, requires **Python >=3.10,<3.15**, and carries Apache-2.0 licensing.
- Describe communicating agents, role-play/workforce orchestration, simulated environments, stateful agent memory, synthetic-data generation, model and tool integration, and research/scaling scenarios. Clearly distinguish aspirational million-agent scale statements from verified production throughput or benchmark evidence.
- **Compatibility:** the current source manifest constrains the MCP Python dependency to **>=1.3,<2**, so runtime transport/protocol and optional model, RAG, storage or browser tool packages must be pinned and validated for the chosen published edition. Individual tools, community simulations, datasets, prompt templates, plugins and third-party hosted APIs are not separate CAMEL-owned product identities.
- **Security and operations:** agent tools can invoke code, browsers, network APIs and external providers; isolate simulated environments, scope credentials and workloads, and account for model/token cost, reproducibility, data sensitivity and permission boundaries before use.
- Attribute the `camel-ai/camel` first-party community publisher to `catalog/producers/c/camel-ai`, with exact `produced-by` / `produces` inverse; do not invent corporate affiliations from paper citations.

## Validation

- Official repository, published v0.2.90 release, source `pyproject.toml`, README and LICENSE support lifecycle, runtime floor, research purpose and producer identity.
- Producer/software relation IDs match exactly.
