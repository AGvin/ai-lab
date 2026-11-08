# Superpowers

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Superpowers is a software-development methodology for coding agents built from composable skills plus bootstrap and host-integration behavior. The selected skills below represent key design, planning, testing, debugging, and verification stages of the larger collection.

## Producer

- [Prime Radiant](../../../../../producers/sub/p/sub/prime-radiant/)

## Selected skills

| Skill | Purpose | Official source |
| --- | --- | --- |
| Brainstorming | Clarify intent and design before implementation through scope-appropriate process paths. | [Source](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| Writing Plans | Turn an approved specification or multi-step requirements into an implementation plan. | [Source](https://github.com/obra/superpowers/tree/main/skills/writing-plans) |
| Test-Driven Development | Enforce a red-green-refactor loop around behavior changes. | [Source](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| Systematic Debugging | Investigate root cause before fixing technical failures. | [Source](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging) |
| Verification Before Completion | Require fresh evidence before success or completion claims. | [Source](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion) |

### Brainstorming

Brainstorming explores the user's intent and alternative approaches, then scales the design to a short document for small changes or a full document for projects. Planned implementation follows approval of that design and then Writing Plans. Explicit user opt-outs and agreed throwaway exploratory spikes are separately scoped exceptions.

### Writing Plans

Writing Plans converts an approved specification or multi-step requirements into small, explicit implementation tasks with files, interfaces, tests, verification, and execution handoff.

### Test-Driven Development

Test-Driven Development applies a red-green-refactor loop: establish a failing test first, verify the failure, write the minimum implementation, then verify the resulting test state before refactoring.

### Systematic Debugging

Systematic Debugging requires root-cause investigation and evidence gathering before fixes. During its fix phase, it delegates the implementation loop to Test-Driven Development and requires Verification Before Completion before declaring success.

### Verification Before Completion

Verification Before Completion requires running the command, test, diff, or other check that directly proves a claim and reading its fresh result before stating that work is fixed, passing, complete, or ready.

## Workflow view

```text
brainstorming
└── approved short or full design -> writing-plans

systematic-debugging
├── fix implementation -> test-driven-development
└── before success claims -> verification-before-completion
```

Full Superpowers installation is the safest default for the coordinated methodology because bootstrap behavior and downstream execution skills extend beyond this selected subset.

## Source interpretation

Prime Radiant's MIT-licensed composable development methodology includes bootstrap and harness-specific integrations. The optional visual companion loads a remote logo carrying the collection version for usage telemetry; upstream documents telemetry opt-outs. Skills do not bypass repository policy, and methodology publication does not verify a project's tests or runtime.

[Reviewed original README](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. This is not a full collection freshness audit.

## Official resources

- [Superpowers repository](https://github.com/obra/superpowers)
