# Documentation Requirements

## Requirements

- Use the reader-facing title `Instruction Tuning`.
- Define instruction tuning as fine-tuning on examples organized around instructions or task descriptions paired with desired outputs/responses so the model becomes better at mapping natural-language or other explicit task instructions to appropriate behavior across one or more tasks.
- Keep instruction tuning narrower than the repository's `supervised-fine-tuning/` concept: instruction tuning is commonly implemented as SFT on instruction-output data, while SFT also covers supervised targets that are not expressed as instruction-response tasks.
- Acknowledge that external LLM literature often uses `instruction tuning` and `SFT` interchangeably. Preserve that terminology relationship in references/reader explanation without collapsing the repository's useful broader-versus-specialized ownership boundary.
- Explain that instruction tuning can use manually authored, benchmark-derived, transformed, synthetic, self-instructed, multimodal, multilingual, or otherwise curated instruction examples; no one data-generation source is part of the universal definition.
- Distinguish instruction diversity and task diversity from mere dataset size. Generalization to unseen instructions/tasks depends on model, data composition/coverage, instruction phrasing, task relationships, optimization, and evaluation rather than a fixed minimum number of instruction examples.
- Distinguish instruction tuning from prompting. Prompting supplies instructions in the current context at inference time; instruction tuning changes learned model/adaptation parameters so instruction-following behavior persists across future contexts.
- Distinguish instruction tuning from preference optimization. SFT/instruction tuning learns from desired demonstrations/targets, whereas RLHF/DPO and related methods optimize from preferences, rankings, rewards, or comparison signals under separate objectives.
- Make clear that improved instruction following does not automatically imply factuality, safety, truthfulness, tool competence, refusal quality, or faithful interpretation of ambiguous instructions. These properties require separate data, objectives, controls, and evaluation.
- Explain that chat templates, role markers, system/user/assistant formatting, multi-turn examples, tool-call schemas, and refusal demonstrations are possible data/interface choices, not universal requirements of instruction tuning.
- Distinguish training behavior from interface authority. Learning to follow instructions does not itself establish provider-specific system/developer/user priority rules, permissions, or security boundaries.
- Keep concrete instruction datasets, synthetic-data pipelines, chat templates, data mixtures/weights, hyperparameters, checkpoints, training services, benchmark results, and assistant/model-selection recommendations with their applicable catalog, learning, evidence, engineering, or decision owners.
- Use the canonical entity references as research inputs for multi-task instruction tuning, zero-shot generalization, and current SFT/IT terminology overlap when reader-facing rendering is activated.

## Validation

- Instruction tuning is not presented as broader than all SFT or as a mandatory stage for every fine-tuned model.
- The repository-specific SFT/instruction-tuning distinction is stated while external terminology overlap is acknowledged.
- Instruction tuning is distinguished from inference-time prompting and from preference optimization/RLHF/DPO.
- Natural-language instructions, chat formatting, multi-turn dialogue, tool calls, and refusal examples are not all required by definition.
- Better instruction following is not treated as proof of factuality, safety, authorization, or general intelligence.
- One dataset size, task count, synthetic-data source, or formatting recipe is not universalized.
