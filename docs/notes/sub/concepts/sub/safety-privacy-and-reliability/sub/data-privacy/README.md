# Data Privacy

<!--
ai_content:
  managed: true
  l10n: true
-->

Data privacy governs how personal, confidential, or sensitive information is collected, processed, retained, shared, and deleted.

## Core idea

An AI workflow can expose data through prompts, model-provider logs, embeddings, caches, traces, training datasets, or tool results. Privacy must therefore be designed across the full data path rather than evaluated only at the model endpoint.

## Practical controls

- Minimize data before sending it to a model.
- Remove or tokenize identifiers where possible.
- Define retention and deletion rules.
- Separate tenants and permission scopes.
- Document provider data-use policies.
- Keep sensitive workloads local when requirements justify it.

## Trade-offs and limitations

Removing detail may reduce model usefulness. Local processing improves control but adds operational responsibility. Anonymization can fail when remaining attributes allow re-identification.

## Common mistakes

- Embedding confidential documents without access controls.
- Treating pseudonymized data as anonymous.
- Retaining prompts indefinitely by default.
- Sending full records when a small subset is sufficient.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Data Residency](../data-residency/)
- [Secret Handling](../secret-handling/)
- [Agent Memory](../../../agents-and-automation/sub/agent-memory/)
