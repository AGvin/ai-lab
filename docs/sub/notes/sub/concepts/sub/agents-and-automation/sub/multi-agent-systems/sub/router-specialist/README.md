# Router-Specialist Architecture

Legacy residual retained for practical routing-policy/pattern-selection guidance and exact legacy LangChain evidence provenance that are intentionally outside the canonical Agent Routing concept owner.

> **Migration note:** Router-specialist identity, bounded dispatch semantics, route registry/authority, distinctions from manager-worker/handoff/model routing, ambiguity/abstention/fallback, minimized-context dispatch, multi-route boundaries, downstream-utility evaluation, and routing drift/revalidation are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/sub/agent-routing/`. The exact Anthropic source cited by the legacy page is also preserved in canonical entity metadata. The remaining material below stays here until its exact learning/decision owner and legacy LangChain evidence provenance are verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Routing-policy residual

Prefer the simplest decision mechanism that can satisfy the routing contract. A practical layered policy can attempt, in order:

1. deterministic validation and policy exclusions;
2. exact metadata or stable rule-based routing;
3. a lightweight classifier, embedding/retrieval route, or other bounded predictor;
4. LLM semantic routing only where language variability or ambiguous category boundaries justify it; and
5. clarification, abstention, fallback, or human triage when the available evidence is insufficient.

Do not force every input into the nearest category. `Unknown`, `mixed`, `unsupported`, and `insufficient information` can be valid outcomes.

Routing can incorporate domain, modality/language, quality tier, risk level, privacy/data boundary, resource availability, and latency/cost only after hard eligibility and policy constraints are satisfied. A cheaper route that repeatedly fails and escalates is not necessarily the lowest-cost accepted path.

Use multi-route dispatch only when several genuinely distinct specialists are required and the surrounding workflow defines merge/conflict ownership, duplication limits, and terminal responsibility. Sending every task to every specialist is not a substitute for routing quality.

## Pattern-fit residual

Agent routing is a strong fit for high-volume workloads with relatively stable specialist categories and bounded dispatch decisions. Prefer another pattern when one generalist already meets the requirement, categories overlap too heavily, the task requires dynamic decomposition/ongoing coordination, the router lacks enough safe context, or misrouting can create irreversible consequences before verification.

## Legacy evidence-provenance residual

The legacy source cited both Anthropic and a LangChain subagents/supervisor-versus-router document:

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [LangChain: Subagents and supervisor versus router](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)

The Anthropic reference is preserved canonically. Canonical Agent Routing now uses a current dedicated LangChain router documentation URL instead of this exact legacy `subagents` reference. Preserve the legacy link until its historical/evidence relationship is explicitly resolved.

These routing-policy, pattern-selection, and evidence-provenance fragments remain migration source material until their exact learning, decision, or research/evidence owners are verified.
