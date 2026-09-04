# Documentation Requirements

## Requirements

- Teach agent routing as a bounded dispatch decision: inspect the task and allowed context, choose one or more eligible specialist agents/tools/handlers, and transfer work under explicit route and terminal-ownership contracts rather than turning the router into an ongoing supervisor.
- Prefer the simplest routing mechanism that satisfies the contract. Present a layered decision strategy that can use, in order: deterministic validation/policy exclusions; exact metadata or stable rules; a lightweight classifier, embedding/retrieval route, or other bounded predictor; LLM semantic routing only when language variability or ambiguous category boundaries justify it; and clarification/abstention/fallback/human triage when evidence is insufficient.
- Apply hard eligibility and policy constraints before quality/cost/latency optimization. Domain, modality/language, risk level, privacy/data boundary, tool/resource availability, and other non-negotiable constraints must filter the candidate routes before preference scoring.
- Teach explicit non-route outcomes such as `Unknown`, `mixed`, `unsupported`, `insufficient information`, clarification, or abstention instead of forcing every input into the nearest known specialist.
- Distinguish routing confidence from downstream success. A highly confident classification is not enough if the selected specialist cannot produce an accepted result, violates policy, or repeatedly falls back/escalates.
- Explain cost as accepted-result cost rather than first-hop price alone: a cheap route that fails, retries, or escalates can be more expensive than a more capable route selected initially.
- Minimize router context to the information needed for safe dispatch. Do not expose unrelated sensitive state to every specialist merely because the router can access it.
- Use multi-route dispatch only when several genuinely distinct specialists are required. Define merge/aggregation ownership, conflict resolution, duplication limits, authorization boundaries, and terminal responsibility before sending the same task to multiple routes.
- Sending every task to every specialist is not a substitute for routing quality. Use fan-out only when independent parallel work is itself part of the workflow design.
- Teach pattern fit: routing works well for high-volume workloads with relatively stable specialist categories and bounded dispatch decisions.
- Prefer a generalist when one worker already satisfies the requirement; prefer manager-worker, graph/DAG, planning/execution, or another explicit orchestration pattern when the task requires dynamic decomposition, ongoing coordination, repeated feedback, or stateful ownership after dispatch.
- Escalate or require stronger verification when misrouting could trigger irreversible or high-consequence effects before downstream validation can catch the mistake.
- Evaluate routing with route accuracy only as one signal. Also measure abstention/clarification behavior, policy/eligibility violations, downstream accepted-result rate, fallback/escalation frequency, multi-route duplication/conflict, latency/cost to accepted result, and routing drift under changing workloads/categories.
- Revalidate routing policy when specialist capabilities, supported categories, risk constraints, prices, latency, or task distribution materially changes; stable labels do not guarantee stable route quality.
- Use Anthropic and LangChain references as framework/pattern evidence. Stable Agent Routing semantics remain canonical in the concept owner; mutable framework APIs and current router/subagent interfaces remain source-backed rather than frozen as learning truth.

## Validation

- Hard policy/eligibility constraints are applied before optimization preferences.
- The learning node permits abstention/clarification and never requires forced nearest-route classification.
- Multi-route examples define merge/conflict and terminal ownership rather than broadcast by default.
- Routing is not conflated with ongoing manager-worker supervision or model routing.
- Evaluation includes downstream accepted utility/cost, not classifier accuracy alone.
- Legacy LangChain `subagents` provenance remains preserved while current router semantics may use newer framework documentation.
