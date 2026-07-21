# Indirect Prompt Injection

Indirect prompt injection occurs when malicious or conflicting instructions are embedded in external content that an AI system reads, such as web pages, emails, documents, code comments, or retrieved knowledge.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

The user may ask an agent to summarize a page, but the page can contain text telling the model to reveal data or call a tool. Because the model sees both task instructions and page content as tokens, it may follow the untrusted content unless the application constrains its behavior.

## High-risk scenarios

- Browser and email agents.
- RAG over user-controlled documents.
- Repository agents reading issues or comments.
- Document-processing pipelines with tool access.
- Multimodal systems reading instructions from images.

## Mitigation

Label external content as untrusted data, minimize tools available during reading, enforce authorization outside the model, filter retrieved content, and require approval before side effects. Separate content extraction from action execution.

## Common mistakes

- Trusting a source because it came from an internal index.
- Allowing documents to redefine the agent's role.
- Giving a summarization task write access.
- Hiding injection text visually and assuming image models will ignore it.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Prompt Injection](../prompt-injection/)
- [Retrieval Poisoning](../retrieval-poisoning/)
- [Trust Boundaries](../trust-boundaries/)
