# Agentic Workflows

<!--
ai_content:
  managed: true
  l10n: true
-->

An agentic workflow combines model-driven decisions with explicit workflow structure, deterministic steps, tools, state, and validation.

## Core idea

Unlike an open-ended autonomous loop, an agentic workflow defines known stages and permits the model to make bounded decisions inside them. For example, a workflow may retrieve data, ask a model to classify it, call an approved tool, validate the result, and request human approval before publishing.

## Practical patterns

- Route tasks to different tools or models.
- Generate a plan and execute only approved steps.
- Retrieve evidence before drafting an answer.
- Review generated code before applying changes.
- Pause for human approval at consequential boundaries.

## Design guidance

Make state transitions explicit. Define inputs, outputs, retry rules, and failure states for every stage. Use deterministic validation for schemas, permissions, and side effects. Record a trace that explains which model, prompt, tool, and data produced each result.

## Trade-offs and limitations

Structured workflows are easier to operate and audit than fully autonomous agents, but they require more upfront design. Too much rigidity can reduce the benefit of model flexibility, while too little structure recreates an unpredictable agent loop.

## Common mistakes

- Hiding workflow state inside conversation history.
- Retrying non-idempotent actions blindly.
- Allowing the model to skip mandatory validation.
- Mixing planning, execution, and approval into one prompt.

## Related concepts

- [Agents and Automation](../../)
- [AI Agents](../ai-agents/)
- [Agent State](../agent-state/)
- [Human in the Loop](../human-in-the-loop/)
