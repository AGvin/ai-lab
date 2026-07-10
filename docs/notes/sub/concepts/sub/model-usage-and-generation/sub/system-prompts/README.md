# System Prompts

High-priority instructions that define an assistant's role, behavior, and operational boundaries.

## Core idea

High-priority instructions that define an assistant's role, behavior, and operational boundaries. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A system prompt provides high-priority instructions before ordinary user content in chat-oriented model APIs.
- Applications use it to define role, policies, tool rules, output standards, and boundaries that should persist across requests.
- The surrounding runtime—not the model alone—must preserve message roles and prevent untrusted content from being promoted to system authority.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

System Prompts affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Configure a reusable assistant or agent behavior layer.
- Separate application-owned policy from per-request user instructions.

## Example

A coding agent system prompt can require feature branches, tests, explicit approval before merge, and refusal to expose credentials.

## Trade-offs and limitations

- System prompts are not a complete security boundary and can still be undermined by ambiguous design or tool permissions.
- Different providers and models may follow the same system prompt with different consistency.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is System Prompts expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Model Usage and Generation](../../)
- [Prompting](../prompting/)
- [Structured Output](../structured-output/)
