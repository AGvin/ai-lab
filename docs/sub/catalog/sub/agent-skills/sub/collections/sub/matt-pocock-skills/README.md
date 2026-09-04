# Matt Pocock Skills

Matt Pocock Skills is a collection of small, composable engineering and productivity skills for coding agents. The collection supports a managed Claude Code plugin and selective installation through the `skills` CLI.

## Producer

- [Matt Pocock](../../../../../producers/sub/m/sub/matt-pocock/)

## Selected skills

| Skill | Purpose | Official source |
| --- | --- | --- |
| Grill Me | User-invoked wrapper that starts a Grilling session. | [Source](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) |
| Grill With Docs | Runs Grilling together with Domain Modeling. | [Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) |
| Grilling | Interview discipline that works a decision tree in rounds. | [Source](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) |
| Domain Modeling | Maintains ubiquitous language, context documentation, and durable architectural decisions. | [Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling) |
| Setup Matt Pocock Skills | Configures repository conventions expected by the engineering skills. | [Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/setup-matt-pocock-skills) |
| Writing for Agents | Guidance for writing documents consumed by agents. | [Source](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents) |

### Grill Me

`grill-me` is a thin user-invoked wrapper over `grilling`. Installing the wrapper without Grilling leaves its intended flow incomplete.

### Grill With Docs

`grill-with-docs` combines the Grilling interview with Domain Modeling, so both skills are part of its explicit workflow dependency.

### Grilling

`grilling` maps a plan, decision, or idea as a decision tree. The current upstream version works in rounds: each round asks the currently unblocked frontier of questions, then recomputes the frontier from the answers.

### Domain Modeling

`domain-modeling` actively builds and sharpens a project's ubiquitous language, updates `CONTEXT.md` when terms are resolved, and records qualifying architectural decisions as ADRs. Its bundled references include `CONTEXT-FORMAT.md` and `ADR-FORMAT.md`.

### Setup Matt Pocock Skills

`setup-matt-pocock-skills` configures the issue-tracker workflow, triage-label vocabulary when applicable, and domain-document layout expected by the engineering skills. The current repository recommends running it once per project before first use of the other engineering skills.

### Writing for Agents

`writing-for-agents` covers writing documents consumed by agents, including skills and `AGENTS.md` or `CLAUDE.md` material. Upstream renamed the former `writing-great-skills` to `writing-for-agents` and removed the old name without an alias; they are not separate current skills.

## Dependency view

```text
grill-me
└── grilling

grill-with-docs
├── grilling
└── domain-modeling
```

Selective installation is supported, but dependent skills need to be installed together. The repository's current setup flow also recommends including `setup-matt-pocock-skills`.

## Official resources

- [Matt Pocock Skills repository](https://github.com/mattpocock/skills)
