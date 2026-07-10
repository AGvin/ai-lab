# Tool Calling

A model selecting a registered external operation and producing arguments for its execution.

## Core idea

A model selecting a registered external operation and producing arguments for its execution. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- The application registers tools with names, descriptions, and argument schemas.
- The model selects a tool and proposes structured arguments instead of directly performing the external action.
- Application code authorizes, validates, executes, and returns the result to the model.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Tool Calling affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Connect models to search, databases, calendars, code execution, or business APIs.
- Separate natural-language decisions from deterministic side effects.

## Example

A model chooses `searchIssues` and supplies a repository and query, while the host checks access before calling GitHub.

## Trade-offs and limitations

- A valid tool call can still be inappropriate or unsafe.
- Tool descriptions, schemas, and returned data become part of the model’s attack surface.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Tool Calling expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Agents and Automation](../../)
- [Agentic Workflows](../agentic-workflows/)
- [Agent State](../agent-state/)
