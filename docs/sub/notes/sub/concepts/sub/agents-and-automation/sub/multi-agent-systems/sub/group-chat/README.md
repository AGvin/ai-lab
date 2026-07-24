# Multi-Agent Group Chat

A multi-agent group chat places several agents in a shared conversation context and uses a turn-selection policy to decide which participant acts next.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established multi-agent interaction pattern.

## Core idea

All participants receive some or all of the same conversation history. A group-chat manager, deterministic rule, or model selects the next speaker. Agents may have different roles, prompts, tools, models, or permissions while collaborating through one shared thread.

Common turn-selection policies include:

- round robin;
- fixed sequence;
- model-selected next speaker;
- rule-based selection;
- manual or human selection;
- termination after approval, consensus, a maximum number of turns, or an external event.

## When it fits

Use group chat when:

- collaboration depends on seeing other participants' current contributions;
- the next useful role cannot always be predetermined;
- a writer, critic, domain expert, and editor need to iteratively refine one artifact;
- a visible conversational transcript is useful for debugging or review;
- agents must negotiate or clarify responsibility dynamically.

## Shared context trade-offs

Shared context makes coordination simple but can become expensive and noisy. Every participant may receive irrelevant messages, repeated artifacts, or misleading claims from other agents.

Control context growth through:

- structured messages rather than unrestricted prose;
- role-specific context filters;
- summaries and checkpoints;
- artifact references instead of repeated full content;
- bounded turn counts;
- explicit termination conditions.

## Turn management

A turn manager should prevent:

- one agent monopolizing the conversation;
- agents repeatedly handing work back and forth;
- selection of agents that cannot contribute to the current state;
- endless discussion after acceptance criteria are met;
- accidental execution of consequential actions during an advisory discussion.

Model-based speaker selection is flexible but adds another model decision that must be evaluated for routing quality and cost.

## Strengths

- straightforward collaboration model;
- shared visibility into current reasoning artifacts and decisions;
- flexible role composition;
- supports critique and iterative refinement;
- easy to prototype in common multi-agent frameworks.

## Limitations

- usually sequential rather than truly parallel;
- context and token use grow with every turn;
- participants can reinforce incorrect assumptions;
- conversational activity can be mistaken for progress;
- shared context may violate least-privilege or information-isolation requirements.

## Established usage

AutoGen documents group chat as a core design pattern with round-robin and model-selected speaker policies. It also supports nested teams, where a participant may itself be another team.

Sources:

- [AutoGen Group Chat design pattern](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html)
- [AutoGen teams](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html)

## Related concepts

- [Multi-Agent Systems](../../)
- [Hierarchical Orchestration](../hierarchical-orchestration/)
- [Debate and Jury](../debate-and-jury/)
- [Agent State](../../../agent-state/)
