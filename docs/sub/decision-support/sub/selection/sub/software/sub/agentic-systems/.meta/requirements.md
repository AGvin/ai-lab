# Documentation Requirements

## Purpose

- Help a reader choose among agentic software when the practical adoption question crosses factual software categories.
- Compare standalone/personal agents, agent frameworks/runtimes, coding-agent control centers, and adjacent automation platforms only where agentic behavior is central to the decision.
- Link canonical software pages instead of duplicating full resource profiles.

## Compared canonical software

- `catalog/software/agents/local/hermes-agent`
- `catalog/software/agents/local/openclaw`
- `catalog/software/agent-frameworks/autogen`
- `catalog/software/agent-frameworks/crewai`
- `catalog/software/agent-frameworks/langgraph`
- `catalog/software/agents/hybrid/openhands`
- `catalog/software/automation/integration-automation/n8n`

## Required decision views

Preserve the legacy comparison as a decision-support matrix with distinct views rather than one metadata dump:

1. decision summary;
2. workflow fit;
3. control and autonomy;
4. adoption and cost;
5. scenario recommendations;
6. operational review checklist;
7. guidance for reading the comparison.

Omit non-differentiating signals from row-level matrices and state shared assumptions once. For the currently compared set, preserve the shared baseline that deployment can be hybrid, data exposure can be high, and operational risk can be high depending on configuration; require concrete deployment verification before presenting these as universal facts.

## Decision summary to preserve

- Hermes Agent: strongest when a persistent personal/workflow agent with memory, skills, automations, channels, terminal tooling, and subagents is desired; trade-off is a broad trust boundary around those capabilities.
- OpenClaw: strongest for a local-first personal assistant spanning devices, messaging channels, workspace skills, companion surfaces, and device nodes; not the first choice for a general multi-agent programming framework.
- AutoGen: strongest for researching/prototyping multi-agent conversations, tool use, code execution, and human-in-the-loop workflows; production durable-state/control requirements need additional architecture.
- CrewAI: strongest for role-based crews, task delegation, tools, flows, and business-process-like multi-agent automation; lower-level graph control is not its primary abstraction.
- LangGraph: strongest for stateful graph-structured long-running agent workflows with persistence, streaming, and explicit human oversight; trade-off is greater engineering effort and ecosystem choice.
- OpenHands: strongest for coding-agent operations tied to repositories, shells, development environments, and engineering tools; requires strict repository/shell/backend/integration permission boundaries.
- n8n: strongest for integration-heavy business automation combining deterministic workflow steps and agent decisions; trade-offs include licensing/commercial boundaries plus a broad credential/data surface across connected systems.

## Workflow-fit distinctions to preserve

- Hermes Agent: persistent assistant/workflow agent; CLI/TUI, messaging, skills, scheduled automation, subagents; standalone adaptive agent.
- OpenClaw: always-on personal assistant; gateway/CLI/channels/companion/device surfaces; local-first personal agent.
- AutoGen: multi-agent conversation prototyping; Python framework/tools/code execution/optional Studio; conversation-oriented framework.
- CrewAI: role-based collaborative automation; crews/agents/tasks/flows/knowledge and optional platform services; crew/task orchestration.
- LangGraph: stateful agent runtime/workflow graphs; Python/JavaScript graph runtime, persistence, streaming, human-in-the-loop; graph orchestration runtime.
- OpenHands: repository/engineering automation; Agent Canvas plus local/remote/cloud/enterprise backends and integrations; coding-agent control center.
- n8n: integration/business-process automation mixing deterministic nodes, custom logic and AI agents; visual workflow canvas with self-hosted/cloud operation; workflow-embedded agents.

## Control/autonomy distinctions to preserve

- Hermes Agent and OpenClaw can expose high-autonomy personal-agent capabilities and therefore require explicit shell/tool/channel/device/credential approval boundaries.
- AutoGen and CrewAI provide developer-composed or role/task orchestration where oversight and sandbox semantics depend materially on application design.
- LangGraph emphasizes explicit state, persistence, graph control, interrupt points, and engineered human-in-the-loop checkpoints.
- OpenHands is a developer control plane whose repository/shell/integration scopes and backend isolation are primary review points.
- n8n offers configurable autonomy inside explicit workflow logic, but connected credentials and agent tools still require deliberate scopes and guardrails.

## Adoption/cost distinctions to preserve

- Hermes Agent, OpenClaw, AutoGen: permissive/open-source core with bring-your-own model/provider or adjacent service costs; review provider/integration terms.
- CrewAI, LangGraph, OpenHands: open-source/permissive core with optional managed/open-core commercial surfaces; review hosted/enterprise/platform boundaries separately from core software.
- n8n: source-available/fair-code self-hosted plus managed cloud/enterprise surfaces; explicitly review the applicable license and connected-service terms for the intended use.

## Scenario shortlist to preserve

- Personal always-on assistant: OpenClaw or Hermes Agent.
- Multi-agent research prototype: AutoGen or CrewAI.
- Business workflow automation: n8n, CrewAI, or LangGraph depending on integration/deterministic-workflow, role/task, or explicit state-graph emphasis.
- Production stateful agent architecture: LangGraph as the strongest fit among this set when explicit durable graph/state control is primary.
- Coding-agent operations: OpenHands.
- Maximum-autonomy experiment: Hermes Agent or OpenClaw, with the strongest safety boundaries before sensitive use.

## Operational review checklist

Before recommending adoption, require review of:

- storage of prompts, files, traces, state, memory, and outputs;
- model/provider or hosted-service exposure of sensitive data;
- shell, browser, repository, messaging, device, and automation access;
- credential storage, scope, rotation, and isolation;
- human approval gates before irreversible actions;
- third-party skills/tools/integrations/plugins and their pinning/review model;
- local/container/VM/cloud/enterprise backend isolation;
- applicable core license, cloud, enterprise, provider, marketplace, and connected-service terms.

## Evidence and freshness policy

- Treat the matrices as triage, not final procurement/deployment advice.
- Resolve detailed current facts through the seven canonical software pages and their references.
- Use `Unknown` when a differentiating signal has not been evaluated or is not supported by canonical evidence.
- Re-verify mutable adoption, licensing, deployment, hosted-service, and security claims before changing recommendations.
- Do not treat popularity/adoption labels from the legacy comparison as timeless facts unless current evidence explicitly supports them.

## Validation

- The page remains decision support, not a duplicate factual software catalog.
- Every compared software identity resolves to its canonical catalog owner.
- Cross-category comparison is justified by one software-adoption decision.
- Mutable claims are bounded by evidence and verification date at render time.
