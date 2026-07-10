# Secret Handling

Secret handling covers the storage, delivery, use, rotation, and redaction of credentials, tokens, keys, and other sensitive operational values.

## Core idea

Models should receive only the minimum secret-derived capability needed for a task, not raw long-lived credentials. The execution layer can use a credential without exposing it in prompt context or tool output.

## Good practice

- Store secrets in a dedicated secret manager.
- Use short-lived, scoped credentials.
- Redact logs, traces, errors, and tool results.
- Prevent secrets from entering prompts or embeddings.
- Rotate credentials after suspected exposure.
- Separate production and development credentials.

## Trade-offs and limitations

Secret brokers and short-lived tokens add infrastructure and integration work. Redaction must balance security with enough diagnostic information for operators.

## Common mistakes

- Placing API keys in system prompts.
- Including `.env` files in model context.
- Logging complete HTTP headers or connection strings.
- Assuming a private model provider makes secret exposure harmless.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Least Privilege](../least-privilege/)
- [Data Privacy](../data-privacy/)
- [Tracing](../../../evaluation-and-operations/sub/tracing/)
