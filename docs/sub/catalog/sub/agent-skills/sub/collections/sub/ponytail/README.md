# Ponytail

Ponytail is Dietrich Gebert's coordinated Agent Skill collection for minimizing unnecessary implementation complexity while preserving required correctness and safety boundaries.

## Collection boundary

The collection currently includes `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, and `ponytail-help`; that inventory is mutable and should be re-verified before treating it as exhaustive. The main decision ladder questions unnecessary work first, then favors reuse, standard-library or native platform capabilities, already-installed dependencies, and the minimum implementation that satisfies the task.

Safety and correctness boundaries are explicitly non-negotiable: trust-boundary validation, data-loss-prevention error handling, security controls, accessibility basics, and requirements the user explicitly insists on must not be simplified away.

The persistent main `ponytail` mode remains distinct from one-shot review/audit/reporting skills. Delivery surfaces such as Claude Code, Codex, GitHub Copilot CLI, Pi, OpenCode, Gemini/Antigravity, Qoder, Hermes, CodeWhale, Swival, Devin, OpenClaw, Grok Build, MCP, npm, hooks, and the internal `ponytail-mcp` adapter are integration mechanisms rather than separate canonical products.

Upstream benchmark results remain producer-reported evidence. The 2026-06-18 agentic benchmark used Claude Code with Haiku 4.5, a pinned real repository, 12 feature tasks, a small safety set, and `n=4` per task/arm; its LOC, token, cost, and time effects are not independent AI Lab measurements or universal guarantees.

## Relations

- Produced by [Dietrich Gebert](../../../../../producers/sub/d/sub/dietrich-gebert/).

## Official resources

- [Ponytail repository](https://github.com/DietrichGebert/ponytail)
- [Ponytail npm package](https://www.npmjs.com/package/@dietrichgebert/ponytail)
- [2026-06-18 upstream agentic benchmark](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)
