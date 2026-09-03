# Documentation Requirements

## Requirements

- Teach Context Compression and Summarization as reducing model-visible context while preserving information that remains necessary for the current task, constraints, evidence, and continuation state.
- Summarize or remove stale conversation material when it no longer improves the current task rather than retaining history only because it exists.
- Preserve critical requirements, unresolved decisions, source/provenance boundaries, and information needed to verify the next action; compression must not silently erase governing constraints.
- Treat summarization as a lossy transformation that requires proportionate verification when omitted detail could materially change the outcome.
- Keep persistent storage/history ownership separate: this topic teaches what is kept model-visible, not how complete durable conversation or application history is stored.

## Validation

- Compression is not described as lossless.
- Critical constraints and evidence are not discarded merely to reduce token count.
- Persistent history and current model-visible summary remain distinct.
