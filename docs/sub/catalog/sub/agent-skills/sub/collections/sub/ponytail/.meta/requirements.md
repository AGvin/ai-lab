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
- When citing the 2026-06-18 agentic benchmark, preserve that it used Claude Code with Haiku 4.5, a pinned real repository, 12 feature tasks, a separate small safety set, and `n=4` per task/arm; describe reported LOC/token/cost/time effects as upstream producer-reported results, not independent AI Lab measurements or guarantees for arbitrary repositories/models.
- Do not use the older `ponytail-gain` single-shot scoreboard as a universal current performance claim without clearly labeling its older methodology and its narrower evidence basis.
- Preserve the collection's MIT licensing as source-backed distribution metadata when discussed.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the official repository, distribution surface, and benchmark reference from canonical entity metadata.

## Validation

- Ponytail remains under `agent-skills/collections/`, not software, agents, development tools, or a set of duplicated standalone skill pages.
- All currently selected Ponytail skills are represented inside the collection exactly once when inventory is rendered.
- The main minimization rules are not paraphrased into unsafe "fewest lines at any cost" guidance.
- Newer agentic benchmark evidence is not conflated with the older single-shot scoreboard, and vendor results are not presented as independent evaluation.
- Delivery adapters and the internal MCP server do not become duplicate canonical entities without new identity evidence.
- The `produced-by` relation resolves to Dietrich Gebert and is matched by the producer's inverse `produces` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
