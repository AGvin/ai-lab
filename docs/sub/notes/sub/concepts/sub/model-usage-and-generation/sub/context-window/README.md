# Context Window

Legacy residual retained for application-level context composition, prompt/retrieval budgeting, and conversation-truncation guidance that are intentionally outside the canonical Context Window concept owner.

> **Migration note:** Context-window identity, nominal-versus-effective capacity, provider accounting boundaries, tokenization/modality effects, separation from persistent memory/retrieval/cache/history, long-context capability limits, and qualified compute/memory/latency/cost implications are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/context/sub/context-window/`. The remaining material below stays here until its exact learning, application-engineering, retrieval, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application-context composition residual

In a concrete chat, agent, or retrieval application, the supplied model context may include system/developer instructions, conversation turns, tool schemas and tool results, files or multimodal inputs, retrieved chunks, and capacity reserved for generation. Which of these items count toward which service limit depends on the concrete model, representation, runtime, and provider interface.

This application-level composition is not part of the generic context-window definition and remains migration source material until its exact application-engineering or learning owner is verified.

## Prompt and retrieval budgeting residual

Useful operational practices include:

- reserve enough generation capacity instead of filling the available request budget entirely with input when the concrete interface requires a shared or reserved budget;
- summarize or remove stale conversation material when it no longer helps the current task;
- retrieve only evidence that is relevant to the current request instead of appending every available document;
- present critical constraints clearly and avoid unnecessary repetition;
- test long-context behavior with representative documents and workloads rather than assuming the published capacity equals reliable working capacity.

## Session and truncation residual

Do not assume old conversation turns remain available to the model after an application truncates, summarizes, replaces, or otherwise compacts history. Persistent application state and model-visible context are separate concerns.

These operational context-management practices remain migration source material until their exact learning, retrieval, memory/context-engineering, or decision-support owners are verified.
