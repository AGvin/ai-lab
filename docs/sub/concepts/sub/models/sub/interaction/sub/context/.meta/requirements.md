# Documentation Requirements

## Requirements

- Use the reader-facing title `Context`.
- Define model context as the information made available to a model for the current computation or generation step, including model-input content and any surrounding representation or system-supplied information that the architecture/runtime exposes to that step.
- Distinguish context from pretrained model parameters: information encoded during training is not current request context merely because it influences the model's behavior.
- Distinguish context from persistent memory, external retrieval stores, conversation databases, tool state, or application state. Those sources become model context only when relevant information from them is actually supplied or exposed to the model's current computation.
- Explain that context can include instructions, user content, prior interaction turns, retrieved material, tool results, structured metadata, multimodal inputs, or other supported representations, depending on the model and surrounding system.
- Distinguish the abstract context concept from the bounded `context window`, which owns the model/runtime capacity and sequence-length boundary for simultaneously available context.
- Explain that context construction includes selection, ordering, formatting, truncation, masking, and representation choices that can materially affect behavior even when the underlying source information is unchanged.
- Keep provider-specific role hierarchies, chat schemas, product memory features, retrieval pipelines, context-cache implementations, and current model limits with their applicable system, catalog, inference, or engineering owners.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.

## Validation

- The page does not equate model context with pretrained knowledge or parameter memory.
- External state is not described as model context until it is supplied or otherwise exposed to the current computation.
- Context is distinguished from context-window capacity and from persistent application memory.
- The page does not assume one universal chat-message format, instruction hierarchy, or modality representation.
- Direct-child navigation contains only currently materialized direct children.
