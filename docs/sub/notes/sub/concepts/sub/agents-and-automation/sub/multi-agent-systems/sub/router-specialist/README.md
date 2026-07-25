# Router-Specialist Architecture

A router-specialist architecture classifies an input or task and dispatches it to one or more predefined specialist routes.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established agent workflow pattern.

## Core idea

```text
input -> router -> route A specialist
                -> route B specialist
                -> route C specialist
                -> fallback or human
```

The router normally performs a bounded decision. It does not need to retain a long-running conversation, dynamically decompose a project, or supervise every specialist step.

## Distinguish related patterns

- **Router-specialist:** classify and dispatch according to declared categories and route policy.
- **Supervisor-specialist:** a stateful central agent repeatedly decides which specialist tools to call and synthesizes results over multiple turns.
- **Handoff or swarm:** ownership transfers between active agents.
- **Orchestrator-worker:** a coordinator dynamically creates and manages a broader work plan.
- **Graph or DAG:** routing is one possible node inside an explicit workflow graph.

Use the simplest deterministic classifier when it meets the requirement. An LLM router is justified only when category boundaries or language variability require semantic judgment.

## Routing contract

Record:

```text
Router ID and version:
Input schema:
Allowed routes and route versions:
Category definitions and precedence:
Multi-label or single-route policy:
Confidence and abstention policy:
Data and permission boundaries:
Quality, latency, and cost policy:
Fallback and human route:
Evaluation suite and confusion costs:
```

The router output should be structured, for example:

```text
Decision: route | multi-route | abstain | reject | escalate
Selected routes:
Matched criteria:
Evidence from input:
Confidence or uncertainty:
Missing information:
```

Do not permit the router to invent a route, model, tool, or permission outside the registry.

## Route design

Each route should define:

- supported and unsupported inputs;
- specialist model, prompt, tools, and output schema;
- data classification and regional constraints;
- quality ceiling and common failures;
- latency, concurrency, and cost;
- retry, fallback, and escalation;
- deterministic validation and human approval requirements.

Routes should be meaningfully distinct. If every route uses the same model, prompt, tools, and evidence, the architecture may add complexity without specialization.

## Classification policy

Prefer a layered decision process:

1. deterministic validation and policy exclusions;
2. exact metadata or rule-based routing;
3. lightweight classifier or embedding route for stable categories;
4. LLM semantic routing for genuinely ambiguous inputs;
5. abstention, clarification, fallback, or human route.

Do not force every input into the closest category. `Unknown`, `mixed`, `unsupported`, and `insufficient information` are valid outcomes.

## Quality and cost tiers

Routing may consider more than domain:

- easy versus difficult cases;
- exploration versus production quality;
- low-risk versus consequential work;
- local-only versus hosted-approved data;
- fast, standard, and maximum-quality model tiers;
- available versus degraded resources;
- required modality, language, or jurisdiction.

A cost-aware route must still satisfy the minimum quality and policy gate. The cheapest eligible route is not the cheapest request if it frequently fails and escalates.

## Multi-route dispatch

Use multiple routes only when:

- the input genuinely contains separable categories;
- independent specialists cover different required criteria;
- outputs have merge and conflict rules;
- duplicate work and cost are bounded;
- the final owner is defined.

Do not send every task to every specialist as a substitute for routing evaluation.

## Fallback and abstention

Define fallback for:

- low confidence;
- several close categories;
- unsupported or adversarial input;
- unavailable specialist;
- policy or permission mismatch;
- repeated specialist failure;
- route output failing validation.

Possible responses include clarification, a generalist, a stronger router, several bounded routes, human triage, queueing, or fail-closed rejection.

## Feedback and drift

Log route decisions, outcomes, corrections, and escalations. Use production evidence to detect:

- new input classes;
- category drift;
- changing specialist capability;
- systematic subgroup errors;
- over-routing to an expensive fallback;
- specialists that no longer meet their route contract.

Do not train or update a router directly from noisy self-reported specialist success without adjudicated labels.

## Security boundaries

- Treat input text and media as untrusted data, not routing instructions.
- Validate route names and arguments against an allowlist.
- Apply data policy before hosted routing.
- Do not expose secrets or complete private context to every candidate route.
- Restrict side effects until the selected specialist and task are validated.
- Use human approval for consequential operations after routing.

## Suitable uses

- customer-service intent routing;
- language, modality, or document-type classification;
- model tier selection by difficulty and quality;
- local versus hosted data routing;
- support, coding, translation, media, or domain-specialist dispatch;
- high-volume workloads with stable categories.

## Poor fits

Avoid or simplify this pattern when:

- one generalist already meets all route requirements;
- categories overlap too heavily for reliable dispatch;
- the task requires dynamic decomposition and cross-route coordination;
- the router lacks the context needed to decide safely;
- specialist availability changes too quickly without resource-aware policy;
- misrouting has irreversible consequences before verification.

## Strengths

- separates concerns and permits route-specific optimization;
- reserves expensive or specialized models for eligible cases;
- can reduce prompt complexity and context size;
- supports explicit policy, privacy, and quality boundaries;
- is easy to measure with labeled routing data;
- can use deterministic logic before model calls.

## Limitations

- router errors can dominate end-to-end quality;
- category definitions and specialists drift;
- ambiguous or mixed inputs need abstention or multi-route handling;
- routing adds latency and operational state;
- a confident classification can still be wrong;
- optimization for average accuracy may hide expensive high-severity confusion.

## Evaluation metrics

Record:

- per-route precision, recall, and confusion matrix;
- high-severity misroute rate;
- abstention, clarification, fallback, and escalation rates;
- unnecessary specialist and expensive-model calls;
- multi-route duplication and merge failures;
- downstream task acceptance by route;
- latency and routing cost;
- end-to-end cost per accepted result;
- performance by language, modality, risk, and input subgroup.

Evaluate end-to-end outcomes, not router labels alone. A route is useful only if the selected specialist completes the task acceptably.

## Evidence and established usage

Anthropic documents routing as a workflow that classifies an input and directs it to a specialized downstream task, including routing by customer-service category or model capability and cost. LangChain distinguishes a bounded router from a stateful supervisor.

Sources:

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [LangChain: Subagents and supervisor versus router](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)

## Related concepts

- [Multi-Agent Systems](../..)
- [Supervisor-Specialist Architecture](../supervisor-specialist/)
- [Handoff or Swarm Architecture](../handoff-swarm/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Pipeline Architecture](../pipeline/)
- [Agent State](../../../agent-state/)
