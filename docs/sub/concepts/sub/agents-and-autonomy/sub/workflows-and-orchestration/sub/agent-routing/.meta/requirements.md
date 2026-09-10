# Documentation Requirements

## Requirements

- Use the reader-facing title `Agent Routing` and introduce `router-specialist` as the legacy/common pattern name for routing to specialized agents.
- Define agent routing as a bounded orchestration decision that classifies or interprets an input/current task state and selects one or more declared specialist agents, teams, or workflow routes according to an explicit routing policy.
- Keep the router's primary responsibility narrow: determine destination(s) and pass the permitted task/context. It need not retain ongoing ownership, repeatedly supervise specialists, integrate many sub-results, or manage the complete conversation after dispatch.
- Distinguish agent routing from `manager-worker-orchestration/`. A manager remains the overall task owner and can repeatedly delegate/integrate work; a router is normally a limited dispatch/classification stage even when a model performs the decision.
- Distinguish agent routing from `coordination-and-communication/handoffs/`. Routing decides where work should go; a handoff specifically transfers active task/conversation/control ownership from one agent/configuration to another. A router can initiate a handoff, invoke a specialist as a bounded subtask, or route into another workflow depending on the surrounding control model.
- Distinguish agent routing from `ai-engineering/architectures-and-patterns/model-routing/`. Model routing selects a model/provider/backend execution route; agent routing selects a specialist role/agent/team/workflow participant. A specialist agent can itself use model routing internally.
- Distinguish agent routing from generic request/API routing. The AI-specific concept is relevant when destinations represent semantically different agents/roles/capabilities and the routing decision depends on task intent, state, capabilities, policy, or model-assisted classification rather than ordinary network addressing alone.
- Support deterministic, rule-based, classifier/model-assisted, embedding/retrieval-based, policy-based, or hybrid routing. No one routing mechanism is required by the concept.
- Define the route registry/allowed destination set outside unconstrained model generation where practical. A model may recommend a route but must not create arbitrary agent identities, capabilities, permissions, endpoints, or escalation destinations merely by naming them.
- Record route identity and capability metadata at the appropriate concrete owner: supported task classes, data/tenant scope, required tools/permissions, model/runtime dependencies, side-effect authority, latency/cost envelope, availability, and known limitations can all affect safe routing.
- Treat route descriptions and capability advertisements as claims whose authority depends on source/registry guarantees. A specialist label such as `legal`, `security`, or `billing` does not prove expertise, permissions, jurisdictional suitability, or current availability.
- Define routing inputs explicitly enough to prevent accidental leakage. A router can classify using a minimized summary/metadata first and send only the context/data needed by the selected specialist rather than broadcasting complete conversation history or secrets to all candidate routes.
- Preserve data and authorization boundaries during dispatch. Routing to a specialist does not expand the user's or workflow's authority; downstream agents receive only permitted data/tools/actions for the current task/tenant/environment.
- Treat user-supplied and retrieved routing hints as untrusted input. Embedded instructions must not select privileged routes, bypass policy, alter the allowed destination registry, or grant stronger permissions solely through prompt text.
- Define ambiguous/low-confidence behavior. A router may request clarification, choose a safe generalist, route to several independent specialists, defer to deterministic policy/human triage, or return `unknown`; forcing a confident route is not required.
- Define multi-route dispatch only when needed. Routing can select one destination, several parallel specialists, a ranked fallback sequence, or a workflow branch; the join/aggregation semantics then belong to the surrounding workflow/manager rather than the routing decision alone.
- Define fallback separately from routing. A fallback route can be selected after unavailable/failed/unsupported handling, but repeated retries to the same unsuitable specialist or silent escalation to broader authority are not valid fallback policies.
- Track routing decisions for consequential systems: input/task class or safe feature summary, selected route(s), policy/model/version, confidence where meaningful, rejected/filtered destinations, fallback/escalation, and terminal outcome can support debugging and evaluation without exposing unnecessary sensitive content.
- Evaluate routing on downstream utility rather than classifier accuracy alone. Useful measures include correct specialist selection, unsupported/misrouted tasks, clarification rate, unnecessary fan-out, route availability failures, privacy/permission violations, downstream task success, latency/cost, and accepted-result quality.
- Treat routing models/scores as evidence, not ground truth. Calibrate thresholds and abstention/escalation against representative workloads and re-evaluate when specialists, task distribution, models, descriptions, or policies change.
- Keep concrete router prompts/classifiers, route registries, model/provider routes, specialist agents, current availability, platform APIs, embeddings/indexes, measured routing results, thresholds, and project-specific routing policy with their applicable catalog/evidence/project owners.
- Use the canonical entity references as research inputs for bounded specialist dispatch and for the router-versus-supervisor distinction while keeping implementation-specific APIs and routing measurements outside concept ownership.

## Validation

- Agent routing is a bounded specialist/route selection decision, not a synonym for ongoing manager supervision, handoff ownership transfer, model/provider routing, or generic network routing.
- Allowed destinations and permissions are not created from unconstrained model text.
- Routing does not silently widen data/tool/side-effect authority.
- Ambiguity/abstention/clarification and fallback semantics are explicit where material.
- Routing quality is evaluated by downstream task/decision outcomes as well as classification metrics.
- Concrete route registries, prompts/models, thresholds, specialist implementations, and measured results remain outside the reusable concept owner.
