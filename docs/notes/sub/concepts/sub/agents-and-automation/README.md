# Agents and Automation

<!--
ai_content:
  managed: true
  l10n: true
-->

Concepts for configuring AI systems that plan, use tools, maintain state, and perform controlled actions.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`ai-agents/`](./sub/ai-agents/) — AI systems that pursue goals through model decisions, tools, state, and iterative actions.
- [`agentic-workflows/`](./sub/agentic-workflows/) — Controlled multi-step processes that combine model decisions with deterministic workflow logic.
- [`tool-calling/`](./sub/tool-calling/) — A model selecting a registered external operation and producing arguments for its execution.
- [`agent-state/`](./sub/agent-state/) — The explicit working data that tracks progress, decisions, and intermediate results.
- [`agent-memory/`](./sub/agent-memory/) — Mechanisms that preserve useful information beyond the immediate model request.
- [`planning/`](./sub/planning/) — Selecting and ordering actions needed to reach a goal.
- [`verification-and-reflection/`](./sub/verification-and-reflection/) — Checking results, identifying errors, and revising an approach when needed.
- [`human-in-the-loop/`](./sub/human-in-the-loop/) — Requiring human review, approval, or intervention at selected workflow points.
- [`idempotency/`](./sub/idempotency/) — Designing actions so safe repetition does not create unintended duplicate effects.
- [`failure-recovery/`](./sub/failure-recovery/) — Restoring progress safely after tool, model, network, or workflow failures.

## Useful

- [`function-calling/`](./sub/function-calling/) — A structured tool-calling interface where model output selects a function and arguments.
- [`task-decomposition/`](./sub/task-decomposition/) — Breaking a large task into smaller, verifiable units of work.
- [`retries/`](./sub/retries/) — Repeating eligible failed operations under bounded and observable rules.
- [`autonomy-levels/`](./sub/autonomy-levels/) — The degree of independent decision-making and action granted to an AI system.

## Specialized

- [`multi-agent-systems/`](./sub/multi-agent-systems/) — Systems in which multiple agents coordinate, compete, review, or specialize.
