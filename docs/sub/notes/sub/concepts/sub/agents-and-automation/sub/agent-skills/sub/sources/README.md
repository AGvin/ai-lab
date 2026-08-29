# Agent Skills Sources and Collections

Legacy residual for Agent Skills source material that has not yet been fully assigned to the final documentation structure. Generic source-trust/adoption guidance and selected collection facts have moved to existing canonical learning/catalog owners.

Last verified: 2026-07-19.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Agent Skills standard

The portable specification is published at `agentskills.io`.

Use it as the canonical source for:

- the required directory and `SKILL.md` entrypoint;
- YAML frontmatter fields;
- naming and description constraints;
- progressive disclosure;
- optional `scripts/`, `references/`, and `assets/` directories;
- client implementation guidance;
- validation expectations.

A skill that follows the specification can be portable, but a client may still differ in installation paths, invocation syntax, permissions, optional metadata, and supported tools. See [Platform support](../platform-support/).

## skills.sh

Website and CLI: `skills.sh` and `vercel-labs/skills`

`skills.sh` is a discovery index, leaderboard, and installer for public Agent Skills repositories. A common command is:

```bash
npx skills@latest add owner/repository
```

The CLI discovers skill directories in the source and asks which clients should receive them.

Important operational notes:

- the CLI copies skills into selected client roots;
- copied skills can be edited locally;
- updates require another installation or a managed process;
- popularity is based partly on aggregated installation telemetry;
- telemetry can be disabled with `DISABLE_TELEMETRY=1`;
- registry presence and security scanning do not guarantee quality or safety.

Recommended use:

- discover public collections;
- install the same skill into several compatible clients;
- compare popularity and ecosystem adoption;
- bootstrap editable project-local copies.

For consequential workflows, pin a reviewed commit instead of blindly following the latest repository state.

## `obra/superpowers`

Repository: `obra/superpowers`

Superpowers is an opinionated software-development methodology implemented as composable skills plus bootstrap instructions. It emphasizes clarification before implementation, detailed planning, isolated worktrees, test-driven development, reviews, and verification before completion.

It supports multiple agent harnesses through a mixture of plugins, marketplaces, native skills, and host-specific installation instructions. Install it separately for every harness you use and verify which components are host adapters versus portable skills.

### Basic workflow

1. `brainstorming`
2. `using-git-worktrees`
3. `writing-plans`
4. `subagent-driven-development` or `executing-plans`
5. `test-driven-development`
6. `requesting-code-review`
7. `finishing-a-development-branch`

### Recommended starting set

Start with these skills rather than enabling the entire methodology blindly:

- `brainstorming` — high value when requirements are incomplete;
- `writing-plans` — converts an accepted design into testable work;
- `test-driven-development` — adds a rapid evidence loop during implementation;
- `systematic-debugging` — reduces speculative fixes;
- `verification-before-completion` — prevents unsupported completion claims;
- `requesting-code-review` — adds an explicit review gate.

Add worktree, subagent, and branch-finishing skills only when the selected client and repository workflow support their assumptions.

## `mattpocock/skills`

Repository: `mattpocock/skills`

This collection provides small, composable engineering and productivity workflows. It explicitly distinguishes:

- **user-invoked skills** — orchestration flows reached only when the user selects them;
- **model-invoked skills** — reusable disciplines that the model may select automatically when relevant.

The distinction is a collection convention, not a required field in the open Agent Skills specification.

Install editable copies through `skills.sh`:

```bash
npx skills@latest add mattpocock/skills
```

The collection also provides a managed Claude Code plugin:

```text
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```

### Recommended starting set

For documentation and software engineering:

- `grill-me` — clarify an idea without assuming a repository workflow;
- `grill-with-docs` — clarify architecture while preserving decisions in documentation;
- `grilling` — reusable questioning behavior for other skills;
- `domain-modeling` — establish and maintain shared terminology;
- `diagnosing-bugs` — investigate before changing code;
- `tdd` — implement with an immediate executable feedback loop;
- `code-review` — verify both engineering standards and specification fidelity;
- `to-spec` — preserve an agreed solution before implementation;
- `implement` — connect an approved specification to implementation and review.

Install `setup-matt-pocock-skills` before the repository-dependent workflows when following the collection's documented setup model.

## Choosing between the two engineering collections

| Need | Superpowers | Matt Pocock skills |
|---|---|---|
| End-to-end prescribed development methodology | Strong fit | Compose selected workflows manually |
| Small independently adoptable practices | Available, but methodology-oriented | Primary design goal |
| Explicit requirement interviews | `brainstorming` | `grill-me`, `grill-with-docs`, `grilling` |
| Domain vocabulary and ADR maintenance | Indirect | `domain-modeling`, `grill-with-docs` |
| TDD | `test-driven-development` | `tdd` |
| Debugging | `systematic-debugging` | `diagnosing-bugs` |
| Review | requesting/receiving review pair | two-axis `code-review` |
| Subagent execution | Core workflow option | `implement` may orchestrate supporting disciplines |
| Large multi-session planning | Detailed plans and execution | `wayfinder`, tickets, specifications |

Do not install both complete methodologies and allow overlapping workflows to activate automatically without testing precedence. Prefer a small reviewed subset with clear ownership of each stage.

## References

- Agent Skills: https://agentskills.io/
- skills.sh: https://skills.sh/
- skills.sh CLI: https://www.skills.sh/docs/cli
- Superpowers: https://github.com/obra/superpowers
- Matt Pocock skills: https://github.com/mattpocock/skills
- Plugins: ../../../plugins/
