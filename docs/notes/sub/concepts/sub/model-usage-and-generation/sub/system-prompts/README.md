# System Prompts

A system prompt is a high-priority instruction layer that defines an assistant's role, operating rules, tool boundaries, and expected behavior for a session or application.

## Core idea

System prompts establish policy and behavior before ordinary user input is processed. They are commonly used to define tone, task scope, safety constraints, tool-use rules, and output conventions. They should contain stable instructions, while dynamic user data and retrieved documents should remain separate.

## Good system-prompt responsibilities

- Define the assistant's purpose and permitted scope.
- Establish which instruction sources are trusted.
- Specify when tools may or must be used.
- Require validation before consequential actions.
- Set durable output and communication conventions.

## Practical use

Keep the prompt concise, explicit, and internally consistent. Separate policy from examples. Treat retrieved web pages, emails, and documents as untrusted data even when they contain instruction-like text. For tool-using systems, pair prompt rules with actual permission checks and sandboxing rather than relying on text alone.

## Trade-offs and limitations

System prompts guide behavior but are not a security boundary by themselves. They consume context, can become difficult to maintain when overloaded, and may interact differently with model updates. Enforcement that matters for safety or data access should also exist in application code.

## Common mistakes

- Storing secrets directly in the prompt.
- Using the system prompt as the only defense against prompt injection.
- Combining stable policy with rapidly changing task data.
- Adding conflicting rules without a clear priority model.

## Related concepts

- [Model Usage and Generation](../../)
- [Prompting](../prompting/)
- [Prompt Injection](../../../safety-privacy-and-reliability/sub/prompt-injection/)
- [Trust Boundaries](../../../safety-privacy-and-reliability/sub/trust-boundaries/)
