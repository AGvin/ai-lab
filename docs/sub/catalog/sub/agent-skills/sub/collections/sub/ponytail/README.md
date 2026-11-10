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

## Source revision and host execution boundaries

The complete first-party [Ponytail source tree](https://github.com/DietrichGebert/ponytail/tree/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) contains **216 tracked files** and matches the inspected upstream default `main` revision exactly. This verifies source-tree parity as of the review, not installation safety, current npm-package parity or a complete provenance/ownership assessment.

The six core `skills/*/SKILL.md` files primarily contain **instructions**, but connected host integrations do more. The [session-start hook](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-activate.js) can write mode state and inject context. Its [codebase mapper](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-map.js) reads selected project source files for function/class summaries. The [mode tracker](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-mode-tracker.js) can start a **detached** importer for earlier Claude sessions when explicitly requested, including usage metrics. The [OpenCode adapter](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/.opencode/plugins/ponytail.mjs) persists host-mode settings and injects rules into new contexts.

These optional hooks and extension adapters are not read-only documentation. Before installing, review workspace access, persistent flags, session-history privacy and code-context visibility under the target agent's permissions. The publisher's root [MIT license](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/LICENSE) does not by itself complete separate asset, third-party, effective-ownership or host-service rights checks. **Provenance/ownership review remains pending.** No package, hook, script or external service was executed during this static inspection.


## Band privacy, webhook and maintenance boundaries

The first-party [Band adapter](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/band/register.tsx) can write a local per-project CSV ledger and rebuild `board.html`, with session IDs, task and project names, model/cost/token usage and timing. An optional configured `webhookUrl` causes **a JSON metric export after every turn**. The [webhook implementation](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/band/metrics.ts) restricts the destination to HTTPS or loopback HTTP and may attach a bearer token. **`sendNames=false` removes only the task title**, not the project label, session identifier or other metrics. It is not full anonymization. Approve the destination, retention, data classification and permissions before enabling export.

An explicitly invoked [`/ponytail band import`](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-band-import.js) may run detached, read historical Claude Code and subagent JSONL transcripts, and store titles/first-prompt fragments and usage in a local per-project CSV. Do not share resulting boards or exported images without checking for internal project identifiers.

The [session-start hook](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-activate.js) may copy statusline scripts into host configuration and suggest setup; the proposed Windows PowerShell command is **not executed automatically**. The shipped [uninstaller](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/scripts/uninstall.js) can remove persistent mode flags and edit shared host settings; review and back them up before uninstalling.

The [source package manifest](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/package.json) has no install/postinstall script or declared runtime dependency list. This says nothing about independent published npm tarball integrity or safe execution of host APIs. **Provenance/ownership review remains pending**, and these findings are static first-party code review, not installed-plugin or webhook testing.
