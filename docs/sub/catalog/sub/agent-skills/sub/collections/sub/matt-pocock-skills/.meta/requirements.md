# Documentation Requirements

## Requirements

- Identify Matt Pocock Skills through the official `mattpocock/skills` repository and link the canonical Matt Pocock producer profile.
- Present the collection as small, composable engineering and productivity skills that can be installed as a managed Claude Code plugin or selectively through the `skills` CLI, using current upstream wording rather than the older RC description.
- Present the selected collection-owned skills with one compact overview followed by concise per-skill detail sections; do not create duplicate standalone catalog pages for them.
- Selected skills are Grill Me, Grill With Docs, Grilling, Domain Modeling, Setup Matt Pocock Skills, and Writing for Agents.
- Treat the selected skills as a curated AI Lab subset rather than an exhaustive mirror of the upstream repository. The upstream collection is mutable and currently contains additional engineering/productivity skills plus separate deprecated, in-progress, and miscellaneous areas; link the official repository for the current complete inventory instead of copying a point-in-time full list into AI Lab.
- When mentioning non-selected skills, do so only when needed for a dependency, setup flow, comparison, or other substantive context; upstream presence alone does not select a skill as a local catalog entity.
- Grill Me is a user-invoked wrapper that starts a `grilling` session and therefore depends on the Grilling skill being available.
- Grill With Docs is a user-invoked wrapper that runs Grilling with Domain Modeling; preserve those two explicit skill dependencies.
- Grilling is the reusable interview discipline. Reflect the current upstream behavior: work a decision tree in rounds and ask the currently unblocked frontier of questions in each round; do not preserve the stale RC claim that it always asks exactly one question at a time.
- Domain Modeling actively maintains a project's ubiquitous language, `CONTEXT.md`, and relevant ADRs; preserve the bundled `CONTEXT-FORMAT.md` and `ADR-FORMAT.md` references.
- Setup Matt Pocock Skills configures the repository issue-tracker choice, triage-label vocabulary when applicable, and domain-document layout and is intended to run once before first use of the other engineering skills.
- Writing for Agents is the current upstream skill for writing documents consumed by agents, including skills and `AGENTS.md`/`CLAUDE.md` material. Record that the former `writing-great-skills` was renamed upstream to `writing-for-agents` and removed without an alias; do not expose the retired name as a second current skill.
- Preserve collection guidance that selective installation is supported but dependencies must be selected together and `setup-matt-pocock-skills` is recommended by the current repository setup flow.

## Selected Skill Sources

- Grill Me: `https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me`
- Grill With Docs: `https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs`
- Grilling: `https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling`
- Domain Modeling: `https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling`
- Setup Matt Pocock Skills: `https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills`
- Writing for Agents: `https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents`

## Dependency View

```text
grill-me
└── grilling

grill-with-docs
├── grilling
└── domain-modeling
```

## Validation

- The six current selected skills are represented exactly once.
- `writing-great-skills` appears only when needed to explain the upstream rename and is never presented as an active alias or separate skill.
- Grilling behavior matches the current frontier-by-round source rather than the stale RC one-question description.
- The page does not present a copied point-in-time list as the complete current Matt Pocock Skills inventory; current full inventory is delegated to the official repository.
- No selected skill is linked as a local standalone catalog node.
