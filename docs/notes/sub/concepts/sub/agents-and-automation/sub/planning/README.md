# Planning

Planning is the process of selecting and ordering actions needed to reach a goal under known constraints.

## Core idea

In agent systems, a plan may be generated once, revised after each observation, or represented as a graph of dependencies. Good plans identify prerequisites, expected outputs, validation points, and conditions that require replanning.

## Practical use

- Break a repository change into inspection, implementation, testing, and publication steps.
- Decide which information must be retrieved before answering.
- Schedule tool calls whose outputs depend on earlier results.
- Identify actions that require human approval.

## Design guidance

Prefer short, testable steps over vague goals. Separate reversible exploration from consequential execution. Attach acceptance criteria to each step and keep the current plan in explicit state. Replan when evidence invalidates an assumption instead of forcing the original sequence.

## Trade-offs and limitations

Detailed planning consumes tokens and can become obsolete quickly in dynamic environments. Models may produce plausible but impossible steps when they lack tool knowledge or current state.

## Common mistakes

- Treating the first plan as fixed.
- Planning actions the system cannot actually execute.
- Omitting validation and rollback steps.
- Generating a long plan for a task that requires one deterministic operation.

## Related concepts

- [Agents and Automation](../../)
- [Task Decomposition](../task-decomposition/)
- [Verification and Reflection](../verification-and-reflection/)
- [Agent State](../agent-state/)
