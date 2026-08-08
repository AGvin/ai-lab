# Matt Pocock Skills

> **Temporary catalog summary:** This short description is a placeholder for a future reviewed collection profile.

Matt Pocock Skills is a collection of composable engineering and productivity workflows for coding agents. It distinguishes user-invoked orchestration skills from model-invoked discipline skills.

## Producer

- [`Matt Pocock`](../../../../../producers/sub/m/sub/matt-pocock/)

## Selected skills

- [`Grill Me`](../../../skills/sub/grill-me/)
- [`Grill With Docs`](../../../skills/sub/grill-with-docs/)
- [`Grilling`](../../../skills/sub/grilling/)
- [`Domain Modeling`](../../../skills/sub/domain-modeling/)
- [`Setup Matt Pocock Skills`](../../../skills/sub/setup-matt-pocock-skills/)
- [`Writing Great Skills`](../../../skills/sub/writing-great-skills/)

## Installation and dependency graph

Selective installation is supported, but wrapper skills are not self-contained:

```text
grill-me
└── requires: grilling

grill-with-docs
├── requires: grilling
└── requires: domain-modeling
```

For engineering skills, the collection recommends installing and running `setup-matt-pocock-skills` once per repository to configure the issue tracker, labels, and domain-document layout. Installing only a wrapper without its model-invoked dependencies produces incomplete behavior.

The managed Claude Code plugin installs the whole collection; `skills.sh` can copy selected skills, so dependency selection must be explicit.

## Naming note

The current canonical skill name is `grill-with-docs`. Earlier references such as “grill-me-with-docs” resolve to this item rather than create a duplicate.

## Official resources

- [Official repository](https://github.com/mattpocock/skills)
