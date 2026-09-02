# Orchestrator-Worker Architecture

Legacy residual retained for broader orchestrator-worker pattern-fit guidance and exact legacy implementation/evidence provenance that are intentionally outside the canonical Manager-Worker Orchestration concept owner.

> **Migration note:** The manager-retains-ownership invariant, dynamic decomposition/delegation, worker contracts, context/permission isolation, dependency/parallelism rules, result integration, validation, terminal responsibility, bounded retries/escalation, deterministic authorization, trade-offs, and system-level evaluation are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/sub/manager-worker-orchestration/`. The remaining material below stays here until its exact learning/decision owner and legacy evidence provenance are verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Variant-fit residual

Use the broader orchestrator-worker variant when the coordinating owner must dynamically decompose an open-ended objective into heterogeneous subtasks, choose workers/tools/models, manage dependencies or artifacts, run independent work in parallel where safe, and synthesize a terminal result after validating worker evidence.

Prefer a narrower supervisor-specialist pattern when one user-facing supervisor repeatedly calls a stable set of bounded specialists, or a deterministic graph/pipeline when the work structure is already known and does not benefit from model-directed decomposition.

The orchestrator does not need to be the strongest model for every worker task, but it must reliably preserve requirements, dependency state, acceptance criteria, worker capability boundaries, and terminal responsibility. Weak decomposition or synthesis can waste otherwise capable workers.

## Legacy evidence-provenance residual

The legacy source cited:

- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [LangChain multi-agent patterns](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/)

Canonical Manager-Worker metadata currently uses other supporting references, including Anthropic `Building effective agents`, OpenAI Agents SDK, and current LangChain multi-agent documentation. Preserve these exact legacy links until their historical/evidence relationship is explicitly resolved.

These variant-selection and evidence-provenance fragments remain migration source material until their exact learning, decision, or research/evidence owners are verified.
