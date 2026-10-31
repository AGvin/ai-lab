# Documentation Requirements

## Requirements

- Identify **Aya 101** as Cohere Labs' original **13 February 2024** instruction-tuned generative multilingual model, exact repository `CohereLabs/aya-101`. It is one concrete trained-model identity, not an Aya 23/Expanse/Vision variant or API mode. [Cohere announcement](https://cohere.com/blog/aya) [Original model card](https://huggingface.co/CohereLabs/aya-101).
- Report the producer-published approximately **13 billion parameters**, instruction following in **101 languages**, text input and generated text output. The model card gives **Apache-2.0** weights, in contrast to the later noncommercial gated Aya 23/Expanse releases. [Model card](https://huggingface.co/CohereLabs/aya-101).
- Architecture uses the same design as **mT5-XXL** with T5/JAX training and documented multilingual instruction fine-tuning. Do not infer an exact model-checkpoint `derived-from` relation solely from architecture equivalence. Avoid labeling this model as a causal-only chat decoder: follow the official `AutoModelForSeq2SeqLM` usage. [Model architecture and usage](https://huggingface.co/CohereLabs/aya-101).
- Do not borrow a context window from Aya 23/Expanse: the original Aya 101 card does not publish a standard supported context-window length. No current official Cohere hosted API route, guaranteed production maintenance, quality advantage, Russian corporate control or independent hardware/inference benchmark is established by these sources.
- Contrast the historical open-weight model against newer Aya models; deployment still requires checking weights, tokenizer, supported inference framework, version, license obligations and real target-language performance before adoption.

## Validation

- One unique `member-of` / `has-member` reciprocal pair with Aya; canonical model entity, scoped requirements and complete English reader.
- Validate sibling and producer navigation, official source URLs and lineage boundaries; do not award whole-catalog schema/cache CI, independent execution, clean full-catalog cycles or final publication gates.
