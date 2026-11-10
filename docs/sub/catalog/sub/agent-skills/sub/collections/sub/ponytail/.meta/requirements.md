# Documentation Requirements

## Requirements

- Identify Ponytail as Dietrich Gebert's coordinated Agent Skill collection for minimizing unnecessary implementation complexity while preserving required correctness and safety boundaries.
- Preserve collection ownership: document the repository and its coordinated skills through this collection page rather than creating duplicate standalone catalog nodes solely because individual skill directories are separately addressable.
- Present the current core collection inventory at a freshness-aware level: `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, and `ponytail-help`. Treat upstream additions/removals as mutable collection state that must be re-verified before claiming exhaustiveness.
- Explain the main Ponytail decision ladder accurately: question unnecessary work first, reuse existing code, prefer standard-library and native platform capabilities, prefer already-installed dependencies, then choose the minimum implementation that satisfies the task.
- Preserve the explicit non-negotiable boundaries from the main skill: do not simplify away trust-boundary validation, data-loss-prevention error handling, security controls, accessibility basics, or requirements the user explicitly insists on.
- Distinguish the main persistent `ponytail` mode from one-shot review/audit/reporting skills. Do not imply that every collection skill modifies coding behavior persistently.
- Treat Claude Code, Codex, GitHub Copilot CLI, Pi, OpenCode, Gemini/Antigravity, Qoder, Hermes, CodeWhale, Swival, Devin, OpenClaw, Grok Build, MCP, npm, hooks, and similar surfaces as delivery/integration mechanisms unless a future artifact has an independently justified product identity.
- Keep the internal/private `ponytail-mcp` server as a delivery adapter for the same ruleset rather than a separate canonical AI Lab product while upstream continues to position it as internal support for the collection.
- Present benchmark results with their methodology and limitations. Prefer the newer upstream agentic benchmark over older single-shot marketing-style figures when summarizing current evidence.
- Prefer the 2026-10-07 Ponytail 5 agentic benchmark cited by the already-pinned upstream README: Claude Code CLI 2.1.288 with Opus 5.5, 39 tasks, three arms (no skill, Ponytail v4.13, Ponytail 5), and five runs per task and arm (585 sessions). Bash was disabled. Results on code size, time, cost and test coverage are publisher-reported, not reproduced by AI Lab or general guarantees. Retain the 2026-06-18 Haiku 4.5 benchmark only as historical evidence.
- Do not use the older `ponytail-gain` single-shot scoreboard as a universal current performance claim without clearly labeling its older methodology and its narrower evidence basis.
- Preserve the collection's MIT licensing as source-backed distribution metadata when discussed.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the official repository, distribution surface, and newest source-pinned benchmark reference from canonical entity metadata; keep benchmark date and methodology consistent with the reader.

## Validation

- Ponytail remains under `agent-skills/collections/`, not software, agents, development tools, or a set of duplicated standalone skill pages.
- All currently selected Ponytail skills are represented inside the collection exactly once when inventory is rendered.
- The main minimization rules are not paraphrased into unsafe "fewest lines at any cost" guidance.
- Newer agentic benchmark evidence is not conflated with the older single-shot scoreboard, and vendor results are not presented as independent evaluation.
- Delivery adapters and the internal MCP server do not become duplicate canonical entities without new identity evidence.
- The `produced-by` relation resolves to Dietrich Gebert and is matched by the producer's inverse `produces` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Benchmark source reconciliation — 2026-11-08

- The already-pinned [upstream README](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/README.md) already promotes the [2026-10-07 Ponytail 5 benchmark](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/benchmarks/results/2026-10-07-agentic.md). The local June benchmark was stale as the primary current study.
- This is a bounded source correction, not an independent benchmark, full freshness audit, copyright clearance or runtime safety assessment.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.

## Full selected-source tree parity and hook boundary — 2026-11-10

- Compared all **216 blobs** in the complete first-party `DietrichGebert/ponytail` source tree at pinned revision `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846` to the current default `main` HEAD, which resolves to the **same commit** on this review date; no additions, removals or changed blob contents. This verifies the selected complete public repository's source currentness at that reference, not npm publication or downstream host compatibility.
- Verified all six first-party entrypoints under `skills/{ponytail,ponytail-review,ponytail-audit,ponytail-debt,ponytail-gain,ponytail-help}/SKILL.md`. Main persistent mode and five one-shot reporting skills must remain distinct; note `ponytail-gain` describes publisher benchmarks, not measured local savings. The cited 2026-10-07 benchmark has three arms × 39 tasks × five runs = 585 sessions, Bash disabled; it is upstream experimental evidence and not independently reproduced.
- The first-party [session-start hook](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-activate.js) can persist local mode flags, inject instructions into agent context and spawn a bounded codebase map. [Map helper](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-map.js) reads up to 65,536 bytes per selected source file using tracked Git paths or a directory scan. [Mode tracker](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-mode-tracker.js) can launch a **detached** past-session board import on an explicit command and write persistent mode state; review session privacy, code-context exposure and permission scope before installing hooks.
- [OpenCode plugin](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/.opencode/plugins/ponytail.mjs) persists mode in host config and injects the ruleset into contexts/compactions. This is a host integration, not a distinct core skill. Do not confuse read-only `SKILL.md` review with installation of executable session hooks; no scripts or host integrations were run.
- The upstream root [MIT LICENSE](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/LICENSE) and npm package label identify **project source rights only**, not unrestricted rights for logos/benchmark materials, host sessions or external services. The existing AI Lab **PROVENANCE/OWNERSHIP REVIEW PENDING** remains binding; a complete independent selected-rights, package/runtime/dependency, effective-control or security sign-off was not performed.
- The canonical requirements and complete reader share this bounded original-source revision comparison and explicit permission implications. Current entity/cache fingerprint and producer inverse were separately inspected; no new freshness marker, trusted-install recommendation, profile closure, Clean stage or accepted gate is earned from this partial review.


## Band webhook, session-history and lifecycle review — 2026-11-10

- The first-party [Ponytail Band registration](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/band/register.tsx) writes per-project CSV metrics and regenerates local `board.html` from all CSVs unless its `ledger` option is disabled. It processes project name, session/task title, model, cost, token totals, duration and test/reuse counts. Local board exports and screenshots may expose project and session metadata.
- With an explicitly configured `webhookUrl`, `record()` posts a metric snapshot **after each turn**, asynchronously, with an optional bearer `webhookToken`. The [webhook builder](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/band/metrics.ts) requires HTTPS except HTTP loopback. `sendNames=false` only sets `name` to empty; **project, session ID, model, cost, times and token metadata remain**. Do not advertise that option as full anonymization. Disable/avoid outbound webhook configuration unless destination, account authorization, data classification and retention are explicitly approved.
- The optional [historical band importer](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-band-import.js) enumerates Claude Code JSONL transcripts and subagent records, extracts project labels, title/first prompt truncated to 60 characters, model and usage, then writes local per-project CSV. An explicit `/ponytail band import` command starts it **detached**. This is not a full transcript copy, but it reads potentially confidential source conversation material and persists identifiable summary metadata.
- [Session start](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/hooks/ponytail-activate.js) may copy/update `.sh` or `.ps1` statusline helpers into the Claude configuration directory and propose a shell/PowerShell setup command (including Windows `-ExecutionPolicy Bypass`), but does **not** autonomously execute that suggested statusline setup. [Uninstall](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/scripts/uninstall.js) may recursively delete its mode-flag directories and edit host `settings.json` or Cursor hooks: back up shared settings and inspect the exact removal paths before running it.
- Source [package.json](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/package.json) describes `@dietrichgebert/ponytail@5.3.3`, MIT, without npm install/postinstall lifecycle scripts or declared external runtime dependencies. Runtime host APIs, bundled `claude-code` Band module behavior, npm publication parity, and operating-system integration remain **not independently executed or verified**. The source-script/supply-chain and permission/data-flow dimensions may record a bounded *static trust map*, not safety certification or independent adoption clearance.
- Preserve **PROVENANCE/OWNERSHIP REVIEW PENDING** and no automatic execution, credential access, webhook setup or remote account activation. This targeted review does not close the independent source-profile conclusion, current-HEAD CI, or Clean acceptance.
