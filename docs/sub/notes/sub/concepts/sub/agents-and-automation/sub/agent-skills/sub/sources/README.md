# Agent Skills Sources and Collections

Agent Skills can come from official vendor catalogs, open standards, community repositories, installation indexes, or platform-specific plugin marketplaces. These sources solve different problems and should not be treated as equivalent trust signals.

Last verified: 2026-07-19.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Source types

| Source type | Main role | What it does not guarantee |
|---|---|---|
| Specification | Defines the portable format and behavior model | Quality, safety, maintenance, or client support for a particular skill |
| Vendor catalog | Publishes skills maintained or curated by a platform or technology vendor | Suitability for every environment or permission policy |
| Community collection | Packages an author's workflows and opinions | Independent review, long-term compatibility, or organizational approval |
| Installer or leaderboard | Helps discover and copy skills into clients | That popularity means correctness or safety |
| Plugin marketplace | Distributes a host-specific managed package | Portability to another host or transparency of every runtime behavior |

Before adopting a skill, inspect the source revision, complete `SKILL.md`, scripts, dependencies, license, network use, writable paths, credentials, and update model.

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

## Anthropic Skills repository — residual decision guidance

Recommended use:

- study simple and complex skill structures;
- inspect production-scale use of scripts, references, and assets;
- use the template as a starting point;
- compare standalone skills with Claude Code plugin packaging.

## NVIDIA verified skills — residual decision guidance

Recommended use:

- NVIDIA CUDA-X and AI platform guidance;
- studying signed skill distribution and provenance;
- studying skill cards, evaluation artifacts, and governance controls;
- organization-level allow-listing based on verified revisions.

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

### Complete skills list

#### Testing

- `test-driven-development` — enforce a red-green-refactor implementation loop.

#### Debugging

- `systematic-debugging` — investigate root causes through a structured multi-phase process.
- `verification-before-completion` — require evidence that a fix or task is actually complete.

#### Collaboration and delivery

- `brainstorming` — refine an idea through questions and design validation.
- `writing-plans` — produce detailed, small implementation tasks with verification steps.
- `executing-plans` — execute approved plans in batches with checkpoints.
- `dispatching-parallel-agents` — coordinate independent tasks concurrently.
- `requesting-code-review` — prepare and request a structured review.
- `receiving-code-review` — evaluate and respond to review feedback.
- `using-git-worktrees` — create isolated workspaces for feature work.
- `finishing-a-development-branch` — verify completion and select the branch disposition.
- `subagent-driven-development` — execute tasks with fresh subagents and staged review.

#### Meta

- `writing-skills` — create and test skills using the collection's methodology.
- `using-superpowers` — bootstrap and explain the Superpowers workflow.

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

### Complete skills list

#### Engineering: user-invoked

- `ask-matt` — route a situation to an appropriate workflow.
- `grill-with-docs` — interview the user while building domain documentation and architectural decisions.
- `triage` — move issues through a structured triage process.
- `improve-codebase-architecture` — identify and discuss architectural deepening opportunities.
- `setup-matt-pocock-skills` — configure repository-specific issue tracking, labels, and documentation paths.
- `to-spec` — turn the current discussion into a durable specification.
- `to-tickets` — decompose a plan or specification into dependency-aware tasks.
- `implement` — implement an accepted specification with TDD seams and review.
- `wayfinder` — plan a body of work too large for one agent session as investigation tickets.

#### Engineering: model-invoked

- `prototype` — build a disposable prototype to answer a design question.
- `diagnosing-bugs` — reproduce, minimize, hypothesize, instrument, fix, and regression-test.
- `research` — investigate primary sources and save cited findings.
- `tdd` — implement one vertical slice at a time through red-green-refactor.
- `domain-modeling` — maintain project terminology, edge cases, and architectural decisions.
- `codebase-design` — design deep modules behind small, testable interfaces.
- `code-review` — review a diff independently for standards and specification fidelity.
- `resolving-merge-conflicts` — resolve conflicts by tracing the intent of both sides.

#### Productivity: user-invoked

- `grill-me` — interview the user until a plan or decision is sufficiently resolved.
- `handoff` — compact the current session into a continuation document.
- `teach` — manage a multi-session learning workflow.
- `writing-great-skills` — explain principles for predictable skill authoring.

#### Productivity: model-invoked

- `grilling` — reusable interview discipline behind the explicit grilling workflows.

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

## Adoption checklist

For every source or collection:

- [ ] Identify whether it is a standard, catalog, installer, collection, or plugin marketplace.
- [ ] Record repository, revision, license, and maintainer.
- [ ] Review all selected skills and bundled scripts.
- [ ] Confirm supported clients and installation roots.
- [ ] Define whether updates are pinned, copied, forked, or managed.
- [ ] Test positive and negative activation prompts.
- [ ] Resolve overlapping workflow ownership.
- [ ] Restrict tools, credentials, and writable paths.
- [ ] Verify removal and rollback.

## References

- Agent Skills: https://agentskills.io/
- OpenAI Skills: https://github.com/openai/skills
- Anthropic Skills: https://github.com/anthropics/skills
- NVIDIA Skills: https://github.com/NVIDIA/skills
- skills.sh: https://skills.sh/
- skills.sh CLI: https://www.skills.sh/docs/cli
- Superpowers: https://github.com/obra/superpowers
- Matt Pocock skills: https://github.com/mattpocock/skills
- Plugins: ../../../plugins/
