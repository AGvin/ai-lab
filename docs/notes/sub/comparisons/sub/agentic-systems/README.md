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

Comparison values must come from the canonical resource pages. Update a canonical page first, then update this table.

Use `Unknown` only when the signal has not been evaluated or the canonical page does not support a stronger value.

## Comparison design

This page is a decision-support matrix, not a metadata dump.

Do not include columns that have the same value for every row. If an important adoption signal is shared by all compared resources, move it to [`Shared assumptions`](#shared-assumptions) instead of repeating it across the table.

## Shared assumptions

For the current resource set, the following adoption signals are effectively shared:

| Signal | Shared value | Why it is not a table column |
| --- | --- | --- |
| Deployment | Hybrid | All listed systems mix local, self-hosted, hosted, external API, model-provider, cloud, or integration components depending on configuration. |
| Data exposure | High | All listed systems may handle prompts, repositories, files, tool outputs, credentials, browser sessions, terminals, automations, or production-like context. |
| Risk level | High | All listed systems require sandboxing, permission boundaries, credential review, and human approval gates before sensitive use. |

These shared values still matter for adoption. They are omitted from the comparison table only because they do not differentiate the current options.

## Comparison dimensions

Use a compact set of fields so the table remains readable in GitHub Markdown.

| Field | Meaning |
| --- | --- |
| Resource | Canonical documentation page for the resource. |
| Best fit | Practical adoption scenario where the resource is most likely to be useful. |
| Operating model | How the resource is normally used or integrated. |
| Use rights | Personal and commercial usage signal for the documented core resource. |
| Cost model | Main cost pattern or payment trigger. |
| Adoption | Rough maturity and ecosystem signal. |
| Main review focus | The first thing to review before using the resource for personal, private, or business work. |

## Controlled values

Prefer stable labels over free-form prose when a field is categorical.

### Use rights

- `Permissive` — personal and commercial use appear broadly allowed by the documented license or terms.
- `Permissive core` — the documented core appears permissive, but optional hosted, enterprise, marketplace, managed, provider, or third-party services need separate review.
- `Commercial review` — business or revenue-generating use requires explicit license, pricing, or terms review.
- `Restricted` — important use cases are limited by license, terms, geography, or access model.
- `Unknown` — current usage rights have not been confirmed.

### Cost model

- `Free` — no payment expected for normal documented use.
- `Freemium` — free tier with paid limits, seats, hosted features, or usage tiers.
- `Open core` — open-source or source-available core with paid platform, cloud, enterprise, or managed features.
- `Paid` — payment required for normal useful operation.
- `BYO cost` — tool may be free, but useful operation requires paid model/API/infrastructure/channel credentials or self-managed runtime costs.
- `Unknown` — cost model has not been confirmed.

### Adoption

- `Mainstream` — widely adopted, highly visible, or explicitly production-positioned in its category.
- `Popular` — visible adoption and active ecosystem.
- `Growing` — meaningful momentum but still evolving.
- `Niche` — narrow or specialized adoption.
- `Unknown` — adoption has not been evaluated.

## Comparison matrix

| Resource | Best fit | Operating model | Use rights | Cost model | Adoption | Main review focus |
| --- | --- | --- | --- | --- | --- | --- |
| [Hermes Agent](../../../../../software/sub/agents/sub/hermes-agent/) | Personal or project-specific autonomous assistant experiments. | Standalone agent using external models, tools, and integrations. | Permissive | BYO cost | Popular | Source trust, runtime permissions, and tool access boundaries. |
| [OpenClaw](../../../../../software/sub/agents/sub/openclaw/) | Browser-use personal agent workflows and task automation. | Standalone browser-focused agent with local and external dependencies. | Permissive core | BYO cost | Mainstream | Browser/session access, credential handling, and site-side effects. |
| [AutoGen](../../../../../software/sub/agent-orchestration/sub/autogen/) | Researching and prototyping multi-agent conversations and workflows. | Framework for composing agents, tools, models, and conversation patterns. | Permissive core | BYO cost | Popular | Model/API configuration, experiment isolation, and orchestration complexity. |
| [CrewAI](../../../../../software/sub/agent-orchestration/sub/crewai/) | Role-based multi-agent workflows with optional managed platform features. | Open-core framework plus optional hosted or managed services. | Permissive core | Open core | Popular | Boundary between open-source core, paid services, and third-party integrations. |
| [LangGraph](../../../../../software/sub/agent-orchestration/sub/langgraph/) | Stateful, controllable, production-oriented agent graphs. | Runtime/framework for graph-based agent state, control flow, and integrations. | Permissive core | Open core | Mainstream | State persistence, observability, deployment architecture, and managed-service terms. |
| [OpenHands](../../../../../software/sub/agent-orchestration/sub/openhands/) | Coding-agent control center for repository and development-environment tasks. | Developer-facing agent control plane connected to repositories, shells, and tools. | Permissive core | Open core | Mainstream | Repository write access, shell permissions, sandboxing, and approval gates. |

## Reading the matrix

Use this matrix as a triage surface, not as a final procurement or deployment decision.

- Start with `Best fit` to decide whether the resource matches the intended workflow.
- Use `Operating model` to distinguish standalone agents, browser agents, orchestration frameworks, stateful runtimes, and coding-agent control centers.
- Check `Use rights` and `Cost model` before personal, revenue-generating, or company use.
- Treat the shared `Hybrid`, `High data exposure`, and `High risk` assumptions as baseline safety requirements for every listed resource.
- Open the canonical resource page for detailed notes, references, and context before adopting the resource.

## Maintenance rules

- Update canonical pages before updating this comparison matrix.
- Prefer concrete values when the canonical page already supports them.
- Use `Unknown` only when the signal has not been evaluated or the canonical page does not support a stronger value.
- Keep table cells short enough to scan.
- Do not repeat identical values across every row; move shared signals into `Shared assumptions`.
- Put detailed license, pricing, provenance, security, and operational notes on canonical resource pages.
