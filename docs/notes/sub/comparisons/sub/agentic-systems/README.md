# Agentic Systems Comparison

Cross-category comparison of standalone agents, agent orchestration systems, coding-agent control centers, and adjacent agentic AI tools.

## Scope

Use this page when the decision question is practical adoption rather than taxonomy placement.

Canonical resource pages remain under their natural documentation category. This page summarizes adoption signals and links back to those canonical pages instead of duplicating full resource descriptions.

Included resource categories:

- standalone agent-like AI systems;
- agent orchestration frameworks and runtimes;
- coding-agent control centers;
- adjacent tools when agentic behavior is central to the adoption decision.

## Evidence policy

Comparison values should come from the canonical resource pages. The comparison should stay concise, reader-facing, and focused on adoption decisions.

Use `Unknown` only when the signal has not been evaluated or the canonical page does not support a stronger value.

## Comparison design

This page is a decision-support matrix, not a metadata dump.

Do not include columns that have the same value for every row. If an important adoption signal is shared by all compared resources, move it to [`Shared assumptions`](#shared-assumptions) instead of repeating it across the table.

Use separate matrices when a single table would mix unrelated decisions. For agentic systems, adoption usually requires at least three views:

1. workflow fit;
2. control and autonomy model;
3. operational review focus.

## Shared assumptions

For the current resource set, the following adoption signals are effectively shared:

| Signal | Shared value | Why it is not a table column |
| --- | --- | --- |
| Deployment | Hybrid | All listed systems mix local, self-hosted, hosted, external API, model-provider, cloud, or integration components depending on configuration. |
| Data exposure | High | All listed systems may handle prompts, repositories, files, tool outputs, credentials, browser sessions, terminals, automations, or production-like context. |
| Risk level | High | All listed systems require sandboxing, permission boundaries, credential review, and human approval gates before sensitive use. |

These shared values still matter for adoption. They are omitted from the main comparison tables only because they do not differentiate the current options.

## Decision summary

| Resource | Best when you need | Avoid as first choice when | Primary trade-off |
| --- | --- | --- | --- |
| [Hermes Agent](../../../../../software/sub/agents/sub/hermes-agent/) | A persistent personal or workflow agent with memory, skills, automations, channels, terminal tooling, and subagents. | You only need a deterministic application workflow or narrow coding-agent UI. | Powerful persistent agent behavior versus broad trust boundary around memory, channels, tools, and automations. |
| [OpenClaw](../../../../../software/sub/agents/sub/openclaw/) | A local-first personal assistant connected to devices, messaging channels, workspace skills, companion surfaces, and device nodes. | You need a general multi-agent programming framework rather than a personal assistant control plane. | Strong personal-agent fit versus large channel, daemon, workspace, and device-node exposure. |
| [AutoGen](../../../../../software/sub/agent-orchestration/sub/autogen/) | Researching or prototyping multi-agent conversations, tool use, code execution, and human-in-the-loop workflows. | You need production-oriented durable state, explicit graph execution, or a coding-agent operations UI. | Flexible research framework versus package-line, migration-path, and execution-sandbox review. |
| [CrewAI](../../../../../software/sub/agent-orchestration/sub/crewai/) | Role-based crews, task delegation, tools, flows, and business-process-like multi-agent automation. | You need low-level graph control or direct repository automation as the main surface. | Higher-level crew/task abstraction versus open-core platform and managed-service boundaries. |
| [LangGraph](../../../../../software/sub/agent-orchestration/sub/langgraph/) | Stateful, graph-structured, long-running agent workflows with persistence, streaming, and human oversight. | You want a ready-made personal assistant or coding-agent control center instead of a framework/runtime. | Strong control and production architecture versus more engineering effort and ecosystem decisions. |
| [OpenHands](../../../../../software/sub/agent-orchestration/sub/openhands/) | A coding-agent control center connected to repositories, shells, development environments, and engineering tools. | Your main goal is personal messaging automation or general multi-agent research. | Direct developer productivity surface versus high-impact repository, shell, backend, and integration permissions. |

## Workflow-fit matrix

| Resource | Primary workflow | User surface | Agent shape | Best fit | Adoption |
| --- | --- | --- | --- | --- | --- |
| [Hermes Agent](../../../../../software/sub/agents/sub/hermes-agent/) | Persistent assistant and workflow agent. | CLI, terminal UI, messaging gateways, skills, scheduled automations, subagents. | Standalone adaptive agent. | Personal or project-specific autonomous assistant experiments. | Popular |
| [OpenClaw](../../../../../software/sub/agents/sub/openclaw/) | Personal always-on assistant across devices and channels. | Gateway daemon, CLI onboarding, messaging channels, companion apps, live Canvas, device nodes. | Local-first personal agent. | Browser-use, workspace, messaging, and device-adjacent personal automation. | Mainstream |
| [AutoGen](../../../../../software/sub/agent-orchestration/sub/autogen/) | Multi-agent conversation prototyping. | Python framework, conversable agents, tools, code execution, optional Studio. | Conversation-oriented agent framework. | Researching and prototyping multi-agent patterns. | Popular |
| [CrewAI](../../../../../software/sub/agent-orchestration/sub/crewai/) | Role-based collaborative automation. | Python framework, crews, agents, tasks, flows, knowledge sources, optional platform services. | Crew/task orchestration framework. | Business-process-like multi-agent workflows with controlled flows. | Popular |
| [LangGraph](../../../../../software/sub/agent-orchestration/sub/langgraph/) | Stateful agent runtime and workflow graphs. | Python/JavaScript framework, graph runtime, persistence, streaming, human-in-the-loop points. | Graph-based orchestration runtime. | Long-running stateful agents and production-oriented control flow. | Mainstream |
| [OpenHands](../../../../../software/sub/agent-orchestration/sub/openhands/) | Repository and engineering automation. | Browser-based Agent Canvas, local/remote/cloud/enterprise backends, GitHub and work-tool integrations. | Coding-agent control center. | Software development tasks, repository automation, and engineering agent operations. | Mainstream |

## Control and autonomy matrix

| Resource | Control style | Autonomy level | Human oversight model | State and memory focus | Engineering fit |
| --- | --- | --- | --- | --- | --- |
| [Hermes Agent](../../../../../software/sub/agents/sub/hermes-agent/) | Agent-led execution with skills, memory, automations, channels, and terminal tools. | High | Requires explicit approval gates around tools, shell, credentials, scheduled tasks, and subagents. | Strong persistent memory and skill-improvement focus. | Good for personal agent experiments; needs hard boundaries before sensitive project use. |
| [OpenClaw](../../../../../software/sub/agents/sub/openclaw/) | Gateway-centered personal assistant with channels, workspace skills, and device nodes. | High | Requires pairing, allowlisting, channel restrictions, daemon review, and workspace/device permission control. | Strong local-first workspace and assistant context focus. | Good for personal automation; less suited as a general software architecture runtime. |
| [AutoGen](../../../../../software/sub/agent-orchestration/sub/autogen/) | Developer-composed agent conversations and tool/code execution loops. | Medium to high | Human-in-the-loop patterns exist, but sandboxing and approval semantics are project-designed. | Depends on application design and selected tools. | Good for experiments, research, and prototypes; production requires extra architecture work. |
| [CrewAI](../../../../../software/sub/agent-orchestration/sub/crewai/) | Role, task, crew, tool, and flow abstractions. | Medium to high | Controlled flows can add deterministic structure, but tool and delegation boundaries need review. | Supports knowledge sources and workflow context depending on setup. | Good for business-style agent workflows; review platform/service boundary for production. |
| [LangGraph](../../../../../software/sub/agent-orchestration/sub/langgraph/) | Explicit graph execution with state, persistence, streaming, and interrupt points. | Configurable | Strong fit for explicit human-in-the-loop and stateful control points when designed correctly. | Strong persistence, checkpoints, and state management. | Strongest fit for engineered stateful agent systems. |
| [OpenHands](../../../../../software/sub/agent-orchestration/sub/openhands/) | Developer control plane for coding agents and execution backends. | Medium to high | Best used with repository review, shell approval, integration scopes, and backend isolation. | Focuses on coding sessions, repository context, and execution backends. | Strongest fit for engineering automation and coding-agent operations. |

## Adoption and cost matrix

| Resource | Use rights | Cost model | Source / platform model | Commercial review focus |
| --- | --- | --- | --- | --- |
| [Hermes Agent](../../../../../software/sub/agents/sub/hermes-agent/) | Permissive core | BYO cost | Open-source package with bring-your-own or hosted model/provider access. | Model/provider terms, messaging gateways, hosted infrastructure, and third-party services. |
| [OpenClaw](../../../../../software/sub/agents/sub/openclaw/) | Permissive core | BYO cost | Open-source package with local-first gateway and companion/node surfaces. | Model providers, channels, companion apps, app stores, third-party skills, and device nodes. |
| [AutoGen](../../../../../software/sub/agent-orchestration/sub/autogen/) | Permissive core | BYO cost | Open-source framework with related Microsoft research tooling. | Microsoft trademarks, docs/content license, model providers, tools, and cloud services. |
| [CrewAI](../../../../../software/sub/agent-orchestration/sub/crewai/) | Permissive core | Open core | Open-source framework with commercial platform services. | Cloud, enterprise console, managed deployment, connectors, support, and platform terms. |
| [LangGraph](../../../../../software/sub/agent-orchestration/sub/langgraph/) | Permissive core | Open core | Open-source core with optional LangChain/LangSmith ecosystem services. | LangSmith, deployment, observability, hosted services, and enterprise terms. |
| [OpenHands](../../../../../software/sub/agent-orchestration/sub/openhands/) | Permissive core | Open core | Open-source core with cloud and enterprise surfaces. | Cloud, enterprise directory license, managed infrastructure, third-party agents, and provider terms. |

## Scenario recommendations

| Scenario | Shortlist | Why |
| --- | --- | --- |
| Personal always-on assistant | OpenClaw, Hermes Agent | Both focus on persistent assistant behavior, channels, tools, and personal workflows. OpenClaw is more gateway/device/channel oriented; Hermes is more memory/skills/subagent oriented. |
| Multi-agent research prototype | AutoGen, CrewAI | AutoGen is closer to conversation-pattern research and tool/code-execution experiments. CrewAI gives a higher-level crew/task abstraction. |
| Business workflow automation | CrewAI, LangGraph | CrewAI is stronger for role/task/process framing. LangGraph is stronger when explicit graph state, control, persistence, and human checkpoints matter. |
| Production stateful agent architecture | LangGraph | Its core value is explicit graph control, durable execution, persistence, streaming, and human-in-the-loop architecture. |
| Coding-agent operations | OpenHands | It is the most directly aligned with repository, shell, backend, GitHub, and engineering-tool automation. |
| Maximum autonomy experiment | Hermes Agent, OpenClaw | Both expose broad personal-agent capabilities, but require the strongest safety boundaries before sensitive use. |

## Operational review checklist

Before adopting any option in this comparison, review:

- where prompts, files, traces, state, memory, and outputs are stored;
- which model providers or hosted services receive sensitive data;
- whether shell, browser, repository, messaging, device, or automation access is enabled;
- how credentials are stored, scoped, rotated, and isolated;
- whether human approval gates exist before irreversible tool actions;
- how third-party skills, tools, integrations, and plugins are pinned and reviewed;
- whether local, container, VM, cloud, or enterprise backends are isolated enough for the intended data;
- what license, cloud, enterprise, provider, or marketplace terms apply to the actual deployment path.

## Reading the comparison

Use these matrices as a triage surface, not as a final procurement or deployment decision.

- Start with `Decision summary` to eliminate tools that are clearly not a workflow fit.
- Use `Workflow-fit matrix` to distinguish assistant, framework, runtime, and coding-agent surfaces.
- Use `Control and autonomy matrix` to decide how much explicit orchestration and oversight the project needs.
- Check `Adoption and cost matrix` before personal, revenue-generating, or company use.
- Treat the shared `Hybrid`, `High data exposure`, and `High risk` assumptions as baseline safety requirements for every listed resource.
- Open the canonical resource page for detailed notes, references, and context before adopting the resource.
