# Documentation Requirements

## Requirements

- Identify Superpowers through the official `obra/superpowers` repository, link the canonical Prime Radiant producer profile, and describe it as a software-development methodology built from composable skills plus bootstrap/integration behavior.
- Present the selected collection-owned skills with one compact overview followed by concise per-skill detail sections; do not create duplicate standalone catalog pages.
- Selected skills are Brainstorming, Writing Plans, Test-Driven Development, Systematic Debugging, and Verification Before Completion.
- Treat the selected skills as a curated AI Lab subset rather than an exhaustive mirror of the upstream repository. Link the official collection for the current complete inventory and do not copy a mutable full skill list into AI Lab merely to preserve a point-in-time catalog snapshot.
- When mentioning non-selected Superpowers skills, do so only when needed to explain a workflow dependency, installation boundary, or comparison; their presence in the upstream collection does not by itself select them as local catalog entities.
- Preserve the current collection-level basic workflow as a methodology sequence, not as a requirement to materialize every participating skill as its own catalog node: `brainstorming` -> `using-git-worktrees` -> `writing-plans` -> `subagent-driven-development` or `executing-plans` -> `test-driven-development` -> `requesting-code-review` -> `finishing-a-development-branch`.
- Explain that installation is harness-specific and that users operating more than one supported harness install/configure Superpowers separately for each one. Treat concrete marketplace/CLI commands as freshness-sensitive upstream facts rather than timeless AI Lab instructions.
- Brainstorming must reflect current upstream intent discovery, approach selection, short designs for small changes versus full designs for projects, and approval of either design before planned implementation. Separately scope user opt-outs and agreed throwaway spikes; do not preserve the obsolete Spike/Bounded/Architectural classification or imply that only one path uses Writing Plans.
- Writing Plans converts an approved specification or multi-step requirements into a detailed implementation plan and hands execution to the appropriate Superpowers execution workflow.
- Test-Driven Development enforces a red-green-refactor cycle with a failing test before implementation code for behavior changes covered by that workflow.
- Systematic Debugging requires root-cause investigation before fixes and, during implementation, delegates the fix loop to Test-Driven Development and requires Verification Before Completion before success claims.
- Verification Before Completion requires fresh evidence from the command or check that proves the claimed result before completion, passing, fixed, or readiness assertions.
- Explain that full Superpowers installation is the safest default when using the coordinated methodology because bootstrap rules and downstream workflow skills extend beyond this selected subset.

## Selected Skill Sources

- Brainstorming: `https://github.com/obra/superpowers/tree/main/skills/brainstorming`
- Writing Plans: `https://github.com/obra/superpowers/tree/main/skills/writing-plans`
- Test-Driven Development: `https://github.com/obra/superpowers/tree/main/skills/test-driven-development`
- Systematic Debugging: `https://github.com/obra/superpowers/tree/main/skills/systematic-debugging`
- Verification Before Completion: `https://github.com/obra/superpowers/tree/main/skills/verification-before-completion`

## Dependency and Workflow View

```text
brainstorming
└── approved short or full design -> writing-plans

systematic-debugging
├── fix implementation -> test-driven-development
└── before success claims -> verification-before-completion
```

## Validation

- All five selected skills are represented exactly once.
- Brainstorming behavior matches the current upstream short/full design contract and its expressly scoped opt-out and throwaway-spike exceptions.
- The collection-level basic workflow includes the current upstream sequencing without converting non-selected workflow participants into standalone AI Lab skill entities.
- Harness-specific installation wording is freshness-bound to upstream rather than copied as permanent command truth.
- Dependency wording distinguishes workflow transitions from hard runtime dependencies.
- The page does not present a copied point-in-time list as the complete current Superpowers inventory; current full inventory is delegated to the official repository.
- No selected skill is linked as a local standalone catalog node.

## Source reconciliation — 2026-11-08

- Rechecked [the original Brainstorming skill at pinned Superpowers revision](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) and [the original repository workflow](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md). The local three-path wording was an inaccurate reading of the same pinned source, not an independently established upstream change.
- The upstream skill distinguishes a short versus full design by scope, with design approval before planned implementation. It separately permits agreed exploratory spikes and explicit opt-outs. This corrects one bounded source-interpretation defect; it is not a full collection freshness, dependency or security audit.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.
