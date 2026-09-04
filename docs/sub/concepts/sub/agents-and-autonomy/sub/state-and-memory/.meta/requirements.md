# Documentation Requirements

## Requirements

- Use the reader-facing title `State and Memory`.
- Define agent state as explicit data describing the current execution/task condition, such as progress, stage, pending/completed actions, intermediate results, approvals, errors, identifiers, or other variables needed to continue or recover the process.
- Define agent memory as mechanisms and retained information that persist, organize, select, or recall prior observations, interactions, findings, preferences, experiences, or derived knowledge so they can influence later agent decisions or interactions.
- Distinguish state from memory. Current authoritative workflow state can be persisted without becoming memory in the cognitive/retrieval sense, while memory can contain prior information that is not authoritative current execution state.
- Distinguish both from model context. State or memory affects a model invocation only when the surrounding system exposes relevant information to that computation; information can remain stored outside the active context.
- Treat `working`, `episodic`, `semantic`, `procedural`, `short-term`, and `long-term` memory labels as useful taxonomies used in parts of the literature rather than one universally standardized agent-memory schema.
- Explain that memory systems can use context-resident summaries, structured records, event histories, databases, retrieval indexes, profiles, reflective summaries, learned mechanisms, or combinations; do not define agent memory as synonymous with a vector database or RAG.
- Explain the memory lifecycle conceptually as write/select, manage/update/consolidate/forget, retrieve, and use. Storing every observation indefinitely is not a defining requirement and can harm relevance, privacy, consistency, and cost.
- Distinguish retained model-generated notes/summaries from authoritative facts. Memory entries can be wrong, stale, contradictory, or untrusted and therefore need provenance, applicability, validation, and update semantics appropriate to their use.
- Explain that persistence improves resumability only when state transitions and external side effects remain consistent. Persisting conversational text alone does not guarantee correct recovery or an authoritative execution record.
- Keep concrete state schemas, database products, retention periods, memory ranking algorithms, profile formats, privacy policies, checkpoint/recovery implementations, and project-specific persistence rules with their applicable engineering, catalog, security, learning, or project owners.
- Use the canonical entity references as research inputs for agent-memory persistence, selective recall, and implementation-diversity boundaries when reader-facing rendering is activated.

## Validation

- The page does not create separate canonical `agent-state` or `agent-memory` leaves from the merge sources.
- State, memory, current model context, conversation history, and model parameters are not treated as interchangeable stores.
- A vector database, transcript, or generated summary is not presented as the universal definition of agent memory.
- Memory entries are not assumed correct, current, authorized, or indefinitely useful merely because they were persisted.
- Cognitive-style memory categories are presented as taxonomies rather than universal mandatory architecture layers.
- Legacy recovery/privacy guidance is preserved as lifecycle and ownership boundaries rather than a product-specific persistence recipe.
