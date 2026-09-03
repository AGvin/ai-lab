# Documentation Requirements

## Requirements

- Present Context Engineering as practitioner-facing teaching for deliberately constructing the model-visible context needed for a task rather than treating context as only a maximum-window-size property.
- Distinguish model-visible context from the canonical Context Window concept, persistent application memory/state, retrieval systems, caches, and complete conversation history.
- Teach context as an assembled working set that may include system/developer instructions, conversation turns, tool schemas/results, files or multimodal inputs, retrieved evidence, and capacity reserved for generation when the concrete interface requires it.
- Keep concrete provider/model token accounting, service limits, cache categories, and billing rules with their current catalog/evidence owners rather than presenting them as universal context semantics.
- Materialize and link the selected children `context-selection-and-assembly/`, `context-compression-and-summarization/`, `memory-and-persistence/`, and `retrieval-in-context/` because each has source-backed material ready for migration.
- Keep full retrieval/RAG architecture with Data and Knowledge, model-internal context/cache mechanics with Models, and agent-specific memory implementation with Agents and Automation.
- Require representative workload verification for long-context behavior rather than equating nominal context capacity with reliable effective working capacity.

## Validation

- Context Engineering does not redefine Context Window capacity semantics.
- Persistent state and model-visible context remain distinct.
- Provider-specific accounting is not generalized into universal token/context rules.
- All four materialized children have distinct learning outcomes and source-backed content.
