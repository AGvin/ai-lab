# Superpowers

> **Temporary catalog summary:** This short description is a placeholder for a future reviewed collection profile.

Superpowers is an opinionated software-development skill collection that coordinates design clarification, planning, isolated implementation, test-driven development, debugging, review, and verification across supported coding-agent hosts.

Its canonical identity in AI Lab is a skill collection, not a software product or agentic-development system.

## Producer

- [`Prime Radiant`](../../../../../producers/sub/p/sub/prime-radiant/)

## Selected skills

- [`Brainstorming`](../../../skills/sub/brainstorming/)
- [`Writing Plans`](../../../skills/sub/writing-plans/)
- [`Test-Driven Development`](../../../skills/sub/test-driven-development/)
- [`Systematic Debugging`](../../../skills/sub/systematic-debugging/)
- [`Verification Before Completion`](../../../skills/sub/verification-before-completion/)

## Installation and dependency graph

Superpowers is designed as a coordinated collection with host-specific bootstrap behavior. Full collection installation is the safest default.

Relevant dependencies in the selected subset include:

```text
brainstorming
└── requires next step: writing-plans

systematic-debugging
├── requires during fix: test-driven-development
└── requires before completion: verification-before-completion
```

`writing-plans` also hands implementation to additional Superpowers execution skills that are not yet selected as separate catalog items. Installing isolated files may therefore omit required bootstrap behavior, downstream skills, bundled references, or host adapters.

## Official resources

- [Official repository](https://github.com/obra/superpowers)
