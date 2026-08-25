# Documentation Requirements

## Requirements

- Use the reader-facing title `Context Window`.
- Define the context window as the bounded amount of model-native sequence/context information that can be simultaneously available to a model computation, commonly reported in tokens for language models but potentially involving modality-specific representations in multimodal systems.
- Distinguish the model/runtime capacity limit from the actual context supplied in one request and from the model's effective ability to use information anywhere within that allowed range.
- Explain that a nominal or advertised maximum context length is a capacity boundary, not a guarantee of uniform recall, reasoning quality, instruction adherence, or task performance across all positions and lengths.
- Keep provider-specific accounting separate from the generic concept: some interfaces constrain combined input and generated output within one sequence budget, while others expose separate input/output limits or reserve generation capacity. Do not encode one service convention as the universal definition.
- Explain that tokenization and representation determine how external content consumes context capacity. Equal character, word, image, audio, or document sizes need not consume equal model-native context units across models.
- Distinguish context-window capacity from persistent memory, external retrieval/storage, context caching, and application history. Those mechanisms can preserve or reintroduce information but do not automatically enlarge the model's simultaneously usable context window.
- Explain that long-context support depends on architecture, positional representation, training/evaluation regime, runtime implementation, memory/cache behavior, and other model-specific factors; loading or accepting a long sequence does not by itself prove effective long-context use.
- Qualify cost/performance statements: longer active sequences can increase computation, memory traffic, cache/storage requirements, latency, or monetary cost, but the scaling depends on architecture, attention pattern, runtime, hardware, caching, and provider pricing.
- Keep exact current context limits, input/output quotas, modality accounting, provider pricing, runtime memory formulas, context-extension methods, and model-specific long-context benchmark results with their applicable catalog, inference, evidence, or decision owners.
- Use the canonical entity references as research inputs for nominal-versus-effective context and long-context evaluation boundaries when reader-facing rendering is activated.

## Validation

- The page distinguishes nominal maximum context capacity from actual supplied context and effective long-context performance.
- The page does not assume one universal provider rule for whether input and generated output share the same published limit.
- Context window is not equated with persistent memory, retrieval storage, conversation history, or context caching.
- The page does not promise reliable recall or reasoning merely because content fits within the advertised context length.
- Computational or memory scaling claims are scoped to the architecture/runtime rather than generalized from standard full-attention Transformers to every model.
- Legacy prompt-sizing, retrieval, cost, and model-selection recommendations are not duplicated into this canonical concept owner.
