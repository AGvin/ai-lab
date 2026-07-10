# Trust Boundaries

Explicit separation between trusted instructions, trusted systems, users, and untrusted data.

## Core idea

Explicit separation between trusted instructions, trusted systems, users, and untrusted data. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- A trust boundary marks where data, authority, identity, or permissions change.
- System instructions, authenticated application state, user input, retrieved documents, and tool output should have distinct trust levels.
- Crossing a boundary requires validation and often authorization.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Trust Boundaries affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Design agent architectures that do not let documents become policy.
- Identify where secrets or write permissions must be isolated.

## Example

Repository files are trusted as project data but not allowed to override owner-approved Git workflow rules.

## Trade-offs and limitations

- Implicit boundaries are easily missed as integrations grow.
- A trusted service can still return compromised or stale data.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Trust Boundaries expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Indirect Prompt Injection](../indirect-prompt-injection/)
- [Least Privilege](../least-privilege/)
