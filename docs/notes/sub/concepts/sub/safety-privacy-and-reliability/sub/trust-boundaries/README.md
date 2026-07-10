# Trust Boundaries

<!--
ai_content:
  managed: true
  l10n: true
-->

A trust boundary separates components, identities, instructions, and data that have different levels of authority or reliability.

## Core idea

AI systems should distinguish application policy, authenticated user intent, tool results, retrieved documents, public web content, and model-generated text. Crossing a trust boundary requires validation rather than assuming all context is equally authoritative.

## Examples

- System policy versus user input.
- Authenticated account data versus public documents.
- Read-only retrieval versus write-capable tools.
- Model proposals versus executed operations.
- One tenant's data versus another tenant's context.

## Practical use

Represent trust in architecture and code, not only prompt wording. Attach identity and provenance to data. Perform authorization at tool execution time. Strip or isolate instruction-like content when a component needs only facts.

## Trade-offs and limitations

More boundaries increase implementation complexity and can reduce workflow convenience. Poorly designed boundaries may still leak data through logs, caches, or shared state.

## Common mistakes

- Treating all retrieved content as trusted.
- Letting the model decide authorization.
- Passing raw tool output between tenants.
- Combining public data and secrets in one prompt without isolation.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Least Privilege](../least-privilege/)
- [Prompt Injection](../prompt-injection/)
- [Data Privacy](../data-privacy/)
