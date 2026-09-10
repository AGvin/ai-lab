# Documentation Requirements

## Requirements

- Use the reader-facing title `Language Models (LMs)`.
- Define a language model broadly as a model of statistical structure in language that assigns probabilities or scores to linguistic sequences or units, predicts linguistic units from context, or otherwise represents distributional relationships needed for language modeling.
- Explain the classical probabilistic view of a language model while allowing modern neural language-model objectives and parameterizations that do not all expose the same whole-sequence probability interface.
- Distinguish autoregressive next-token or next-unit prediction as an important modern language-model form rather than a universal definition. Acknowledge masked and other contextual language-model objectives when clarifying the category boundary.
- Make clear that a language model need not be large, Transformer-based, generative in its user-facing use, instruction-tuned, conversational, or a foundation model.
- Keep language-model identity separate from the `SLM`/`LLM` scale dimension owned by `language-model-scale/`; do not define the category by one parameter threshold or by large scale.
- Keep foundation-model role, multimodal status, model architecture, training/post-training, prompting, tool use, retrieval, deployment, frontier status, and assistant/system behavior as separate dimensions or owners.
- Explain that text generation is one use of language modeling but is not the only reason to model linguistic distributions; scoring, representation, ranking, completion, recognition, and other language tasks can also use language models.
- Preserve only the general language-model semantic core from the legacy `large-language-models` source here. LLM-scale semantics belong to `language-model-scale/`; instruction tuning and preference optimization belong to training/adaptation; hallucinations and other behavior belong to their behavior/failure-mode owners; application scaffolding and model-selection guidance remain outside this node.
- Use the canonical entity references as research inputs for generic and current language-model terminology when reader-facing rendering is activated.

## Validation

- The page does not define every language model as an LLM, Transformer, foundation model, assistant, or autoregressive next-token generator.
- The page does not move scale-specific `large` semantics out of `language-model-scale/`.
- The page does not treat instruction tuning, preference optimization, retrieval, tool calling, or prompting as part of the intrinsic language-model definition.
- The page distinguishes a language model from the larger application or AI system that may wrap it.
- LLM-specific model-selection, deployment, and failure guidance from the split legacy source is not duplicated into this canonical classification node.
