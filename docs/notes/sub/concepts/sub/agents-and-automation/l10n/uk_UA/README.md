<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5b1e2a6d4c74fcbcfbd8348387fcd0a9a601687c
  mode: copy-through
-->

# Agents and Automation

Concepts for configuring AI systems that plan, use tools, maintain state, and perform controlled actions.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Переклади

- [English](../../../../l10n/uk_UA/)
- Українська — поточна

## Essential

- [`ai-agents/`](../../sub/ai-agents/l10n/uk_UA/) — AI systems that pursue goals through model decisions, tools, state, and iterative actions.
- [`agentic-workflows/`](../../sub/agentic-workflows/l10n/uk_UA/) — Controlled multi-step processes that combine model decisions with deterministic workflow logic.
- [`tool-calling/`](../../sub/tool-calling/l10n/uk_UA/) — A model selecting a registered external operation and producing arguments for its execution.
- [`agent-state/`](../../sub/agent-state/l10n/uk_UA/) — The explicit working data that tracks progress, decisions, and intermediate results.
- [`agent-memory/`](../../sub/agent-memory/l10n/uk_UA/) — Mechanisms that preserve useful information beyond the immediate model request.
- [`planning/`](../../sub/planning/l10n/uk_UA/) — Selecting and ordering actions needed to reach a goal.
- [`verification-and-reflection/`](../../sub/verification-and-reflection/l10n/uk_UA/) — Checking results, identifying errors, and revising an approach when needed.
- [`human-in-the-loop/`](../../sub/human-in-the-loop/l10n/uk_UA/) — Requiring human review, approval, or intervention at selected workflow points.
- [`idempotency/`](../../sub/idempotency/l10n/uk_UA/) — Designing actions so safe repetition does not create unintended duplicate effects.
- [`failure-recovery/`](../../sub/failure-recovery/l10n/uk_UA/) — Restoring progress safely after tool, model, network, or workflow failures.

## Useful

- [`function-calling/`](../../sub/function-calling/l10n/uk_UA/) — A structured tool-calling interface where model output selects a function and arguments.
- [`task-decomposition/`](../../sub/task-decomposition/l10n/uk_UA/) — Breaking a large task into smaller, verifiable units of work.
- [`retries/`](../../sub/retries/l10n/uk_UA/) — Repeating eligible failed operations under bounded and observable rules.
- [`autonomy-levels/`](../../sub/autonomy-levels/l10n/uk_UA/) — The degree of independent decision-making and action granted to an AI system.

## Specialized

- [`multi-agent-systems/`](../../sub/multi-agent-systems/l10n/uk_UA/) — Systems in which multiple agents coordinate, compete, review, or specialize.
