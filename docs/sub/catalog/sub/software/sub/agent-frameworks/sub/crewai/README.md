# CrewAI

CrewAI is an open-source Python framework for building agentic applications with two complementary orchestration surfaces: **Crews** for autonomous, role-based collaboration between agents and **Flows** for structured, event-driven execution with explicit state and control paths.

## Framework and platform boundary

The open-source framework can be developed and run independently with selected model providers, tools, and infrastructure. CrewAI also offers managed and enterprise platform capabilities for deployment, triggers, observability, team management, RBAC, and operational governance; those hosted capabilities are a separate adoption surface rather than an intrinsic requirement of the framework.

Operational use should account for tool permissions, delegated task boundaries, provider credentials, memory or knowledge-source data exposure, observability, execution controls, and appropriate human approval gates.

## Current project setup and execution controls

For CrewAI 1.15.x, newly created projects use JSONC-first agent and crew configuration (`agents/*.jsonc` and `crew.jsonc`). Classic YAML and the `@CrewBase` decorator remain supported; migrating an existing project is a separate decision from adopting the current default for new projects.

Agent-generated code execution is disabled by default. Enabling it with `allow_code_execution` requires reviewing `code_execution_mode`: `safe` invokes Docker, while `unsafe` executes code directly. Docker still needs restricted mounts, credentials, network access and resource limits. Delegation is disabled by default; scope available tools, iterations, run duration, and explicit human approvals where required.

## Official resources

- [CrewAI documentation](https://docs.crewai.com/)
- [Agent configuration and code execution](https://docs.crewai.com/en/concepts/agents)
- [Human-in-the-loop workflows](https://docs.crewai.com/en/learn/human-in-the-loop)
- [CrewAI repository](https://github.com/crewAIInc/crewAI)
- [CrewAI website](https://www.crewai.com/)
- [CrewAI, Inc.](../../../../../producers/sub/c/sub/crewai-inc/)
