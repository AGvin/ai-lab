# Multi-Agent Systems

A multi-agent system coordinates several agents that may specialize, collaborate, compete, delegate, or review one another.

## Core idea

Multiple agents are useful when tasks have genuinely different roles, tools, permissions, or parallel workstreams. Examples include a research agent gathering evidence, an implementation agent producing changes, and a reviewer checking the result. The agents still require a shared protocol, state model, and conflict-resolution mechanism.

## Practical use

- Parallelize independent document or repository analysis.
- Separate generation from review.
- Assign domain-specific tools and prompts to specialized roles.
- Simulate alternative proposals before selecting one.

## Trade-offs and limitations

Multi-agent systems multiply model calls, coordination overhead, and failure modes. Agents can reinforce one another's errors because they share similar models or context. More agents do not automatically produce independent evidence.

## Common mistakes

- Using multiple agents for a task that can be a simple loop.
- Giving every agent the same role and information.
- Allowing agents to modify shared state without coordination.
- Treating agent agreement as proof of correctness.

## Related concepts

- [Agents and Automation](../../)
- [Task Decomposition](../task-decomposition/)
- [Agent State](../agent-state/)
- [Verification and Reflection](../verification-and-reflection/)
