# Prompting

The practice of supplying instructions, context, examples, and constraints to guide a model.

## Core idea

The practice of supplying instructions, context, examples, and constraints to guide a model. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A prompt combines the requested task with instructions, context, examples, constraints, and completion criteria.
- Clear separation between instructions and untrusted data reduces ambiguity and prompt-injection risk.
- Good prompts specify what a successful result looks like and what the model should do when information is missing.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Prompting affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Turn an informal request into a reproducible task definition.
- Control tone, scope, format, assumptions, and verification behavior without changing model weights.

## Example

A repository-review prompt can define the target branch, allowed files, required tests, prohibited actions, and expected final summary.

## Trade-offs and limitations

- Prompting cannot make an incapable model reliably perform a task or know unavailable facts.
- Very long or contradictory instructions can reduce compliance rather than improve it.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Prompting expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Model Usage and Generation](../../)
- [Context Window](../context-window/)
- [System Prompts](../system-prompts/)
