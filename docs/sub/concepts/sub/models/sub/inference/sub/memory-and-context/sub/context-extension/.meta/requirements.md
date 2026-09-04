# Documentation Requirements

## Requirements

- Use the reader-facing title `Context Extension`.
- Define context extension as a family of techniques that enable a pretrained or previously configured model to operate over longer input/context sequences than its original training, validated, or default positional/runtime range while attempting to preserve useful behavior.
- Distinguish context extension from merely increasing a runtime `max sequence length` or allocator limit. A runtime may accept more positions without the model having learned or retained useful behavior at those lengths.
- Distinguish the model's native/training context, configured/accepted maximum sequence length, and effective context length supported by measured task performance. These values can differ materially.
- Present positional interpolation/rescaling/extrapolation, rotary-frequency/base scaling, searched/non-uniform rescaling, architectural/attention changes, longer-context continued pretraining or fine-tuning, and combinations as context-extension strategy families rather than one universal method.
- Treat RoPE-specific methods such as Position Interpolation, YaRN, NTK-aware scaling variants, and LongRoPE as examples within the broader concept. Do not create canonical descendants for the legacy method pages unless separately selected by architecture.
- Explain that some context-extension methods require training or adaptation while others can be applied through runtime/configuration changes; the existence of a no-training extension mode does not imply equal quality to trained adaptation.
- Explain that preserving short-context behavior is a separate evaluation requirement from improving long-context behavior. Extension can introduce regressions at original lengths, new positional distortions, retrieval errors, or attention degradation even when long sequences are accepted successfully.
- Make clear that longer accepted sequences do not guarantee uniform information use, perfect recall, reasoning over distant evidence, or immunity to lost-in-the-middle/position effects. Effective long-context behavior must be evaluated over representative positions, lengths, tasks, and failure cases.
- Distinguish context extension from context caching, KV-cache memory optimization, retrieval/RAG, summarization, external memory, and persistent agent memory. Those mechanisms can reduce repeated compute or select/store information without changing the model's supported positional/context regime itself.
- Explain that extending sequence length also changes runtime requirements: attention computation, KV/state memory, batch/concurrency headroom, positional state, and latency can grow or change depending on the architecture and extension method.
- Keep concrete model-specific scaling factors, RoPE bases, YaRN/NTK/LongRoPE configurations, training recipes, supported runtime overrides, exact advertised context limits, long-context benchmark results, hardware-fit measurements, and deployment recommendations with their applicable catalog, training/adaptation, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for positional-extension methods and native/configured/effective context distinctions when reader-facing rendering is activated.

## Validation

- The page does not equate a larger configured maximum sequence length with effective long-context capability.
- Native/training, configured/accepted, and empirically effective context lengths are distinguished.
- RoPE scaling/interpolation methods are presented as examples rather than universal context-extension requirements or canonical child nodes.
- Context extension is not conflated with KV caching, prefix caching, RAG, summarization, or persistent memory.
- Successful processing of a long sequence is not presented as proof of uniform recall or reasoning quality throughout that sequence.
- Short-context regression and increased runtime/memory costs remain explicit evaluation concerns.
- Legacy YaRN/NTK-aware/LongRoPE/Position-Interpolation pages are represented through their semantic method families without creating unselected descendants.
