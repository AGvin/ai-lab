# Ponytail

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Ponytail is Dietrich Gebert's coordinated Agent Skill collection for minimizing unnecessary implementation complexity while preserving required correctness and safety boundaries.

## Collection boundary

The collection currently includes `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, and `ponytail-help`; that inventory is mutable and should be re-verified before treating it as exhaustive. The main decision ladder questions unnecessary work first, then favors reuse, standard-library or native platform capabilities, already-installed dependencies, and the minimum implementation that satisfies the task.

Safety and correctness boundaries are explicitly non-negotiable: trust-boundary validation, data-loss-prevention error handling, security controls, accessibility basics, and requirements the user explicitly insists on must not be simplified away.

The persistent main `ponytail` mode remains distinct from one-shot review/audit/reporting skills. Delivery surfaces such as Claude Code, Codex, GitHub Copilot CLI, Pi, OpenCode, Gemini/Antigravity, Qoder, Hermes, CodeWhale, Swival, Devin, OpenClaw, Grok Build, MCP, npm, hooks, and the internal `ponytail-mcp` adapter are integration mechanisms rather than separate canonical products.

Upstream benchmark results remain producer-reported evidence. The newer 2026-10-07 Ponytail 5 study used Claude Code CLI 2.1.288 with Opus 5.5 across 39 tasks and three arms (no skill, Ponytail v4.13 and Ponytail 5), with five runs per task and arm (585 sessions). Bash was disabled. AI Lab has not independently reproduced the reported effects or safety outcomes; the June 2026 Haiku 4.5 study remains historical.

## Relations

- Produced by [Dietrich Gebert](../../../../../producers/sub/d/sub/dietrich-gebert/).

## Source interpretation

Dietrich Gebert publishes the MIT-licensed Ponytail collection for reducing unnecessary implementation complexity while retaining validation, security and accessibility. Benchmark improvements are publisher reports, not reproduced evidence. Main mode and one-shot review/audit commands remain different; current commands and integrations are revision-specific.

[Reviewed original README](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Ponytail repository](https://github.com/DietrichGebert/ponytail)
- [Ponytail npm package](https://www.npmjs.com/package/@dietrichgebert/ponytail)
- [2026-10-07 upstream Ponytail 5 benchmark](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/results/2026-10-07-agentic.md)
