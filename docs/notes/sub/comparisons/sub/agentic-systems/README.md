# Agentic Systems Comparison

Cross-category comparison of standalone agents, agent orchestration systems, coding-agent control centers, and adjacent agentic AI tools.

## Scope

Use this page when the decision question is practical adoption rather than taxonomy placement.

Canonical resource pages remain under their natural documentation category. This page should summarize adoption signals and link back to those canonical pages instead of duplicating full resource descriptions.

Included resource categories:

- standalone agent-like AI systems;
- agent orchestration frameworks and runtimes;
- coding-agent control centers;
- adjacent tools when agentic behavior is central to the adoption decision.

## Comparison dimensions

Use a compact set of fields so the table remains readable in GitHub Markdown.

| Field | Meaning |
| --- | --- |
| Resource | Canonical documentation page for the resource. |
| Category | Practical resource category used for comparison. |
| Use rights | Personal and commercial usage signal for the documented core resource. |
| Cost model | Main cost pattern or payment trigger. |
| Deployment | Local, self-hosted, hosted, or hybrid operation. |
| Data exposure | Expected exposure of prompts, repositories, files, credentials, or tool outputs. |
| Risk level | Compact adoption risk signal for sensitive personal or business use. |
| Adoption | Rough maturity and ecosystem signal. |

## Controlled values

Prefer stable labels over free-form prose.

### Use rights

- `Permissive` — personal and commercial use appear broadly allowed by the documented license or terms.
- `Permissive core` — the documented core appears permissive, but optional hosted, enterprise, marketplace, or managed services need separate review.
- `Commercial review` — business or revenue-generating use requires explicit license, pricing, or terms review.
- `Restricted` — important use cases are limited by license, terms, geography, or access model.
- `Unknown` — current usage rights have not been confirmed.

### Cost model

- `Free` — no payment expected for normal documented use.
- `Freemium` — free tier with paid limits, seats, hosted features, or usage tiers.
- `Open core` — open-source or source-available core with paid platform, cloud, enterprise, or managed features.
- `Paid` — payment required for normal useful operation.
- `BYO cost` — tool may be free, but useful operation requires paid model/API/infrastructure credentials.
- `Unknown` — cost model has not been confirmed.

### Deployment

- `Local` — runs on a local workstation.
- `Self-hosted` — runs on owned or controlled infrastructure.
- `Hosted` — provider-operated service.
- `Hybrid` — mixes local/self-hosted components with hosted services, external APIs, model providers, messaging channels, or integrations.
- `Unknown` — deployment model has not been confirmed.

### Data exposure

- `Low` — local-only or self-hosted use with no expected third-party data transfer.
- `Medium` — external model/API calls or hosted features may receive prompts, files, state, or outputs.
- `High` — resource may access repositories, browser sessions, credentials, tools, terminals, messaging channels, files, or production-like systems.
- `Unknown` — exposure has not been confirmed.

### Risk level

- `Low` — reasonable candidate for low-sensitivity use after normal review.
- `Medium` — needs configuration review before sensitive personal or business use.
- `High` — needs sandboxing, permission boundaries, credential review, and human approval gates.
- `Unknown` — insufficient information for a useful risk signal.

### Adoption

- `Mainstream` — widely adopted and mature in its category.
- `Popular` — visible adoption and active ecosystem.
- `Growing` — meaningful momentum but still evolving.
- `Niche` — narrow or specialized adoption.
- `Unknown` — adoption has not been evaluated.

## Comparison table

| Resource | Category | Use rights | Cost model | Deployment | Data exposure | Risk level | Adoption |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Hermes Agent](../../../../../software/sub/agents/sub/hermes-agent/) | Standalone agent | Permissive | BYO cost | Hybrid | High | High | Unknown |
| [OpenClaw](../../../../../software/sub/agents/sub/openclaw/) | Standalone browser-use agent | Permissive | BYO cost | Hybrid | High | High | Unknown |
| [AutoGen](../../../../../software/sub/agent-orchestration/sub/autogen/) | Agent orchestration framework | Permissive | BYO cost | Hybrid | High | High | Unknown |
| [CrewAI](../../../../../software/sub/agent-orchestration/sub/crewai/) | Agent orchestration framework | Permissive core | Open core | Hybrid | High | High | Unknown |
| [LangGraph](../../../../../software/sub/agent-orchestration/sub/langgraph/) | Stateful agent orchestration runtime | Permissive core | Open core | Hybrid | High | High | Unknown |
| [OpenHands](../../../../../software/sub/agent-orchestration/sub/openhands/) | Coding-agent control center | Permissive | BYO cost | Hybrid | High | High | Unknown |

## Reading the table

Use the table as a triage surface, not as a final procurement or deployment decision.

- Start with `Use rights` and `Cost model` to identify whether personal, revenue-generating, or company use is likely acceptable.
- Check `Deployment`, `Data exposure`, and `Risk level` before connecting a resource to private files, repositories, browsers, terminals, credentials, messaging channels, or business systems.
- Use `Adoption` only when it has been explicitly evaluated; do not treat popularity as a substitute for security or license review.
- Open the canonical resource page for detailed notes, references, and context before adopting the resource.

## Maintenance rules

- Prefer concrete values when the canonical page already supports them.
- Use `Unknown` only when the signal has not been evaluated or the canonical page does not support a stronger value.
- Keep table cells short enough to scan.
- Put detailed license, pricing, provenance, security, and operational notes on canonical resource pages.
- Update this comparison only when the corresponding canonical page has enough information to support the comparison signal.
