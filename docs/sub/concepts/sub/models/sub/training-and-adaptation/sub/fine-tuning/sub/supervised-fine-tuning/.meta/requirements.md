# Documentation Requirements

## Requirements

- Use the reader-facing title `Supervised Fine-Tuning (SFT)`.
- Define supervised fine-tuning as fine-tuning from an already trained model using supervised examples that pair model inputs or conditioning information with target labels, outputs, responses, actions, representations, or other desired predictions under an explicit supervised objective.
- Keep SFT broader than instruction tuning. Instruction-response demonstrations are an important LLM SFT pattern, but supervised fine-tuning can also target classification, extraction, ranking, sequence labeling, structured prediction, domain generation, multimodal tasks, or other supervised objectives without natural-language instructions.
- Acknowledge terminology overlap: some contemporary LLM literature uses `SFT` and `instruction tuning` nearly interchangeably. For this repository, use `SFT` for the broader supervised adaptation family and `instruction tuning` for the instruction-conditioned specialization selected as its sibling child under fine-tuning.
- Explain that generative-language-model SFT commonly maximizes likelihood/minimizes cross-entropy on target tokens, sometimes masking prompt/input tokens from the training loss, but do not make one loss mask, chat template, teacher-forcing convention, or sequence format universal.
- Distinguish supervised targets from preference comparisons. SFT trains against desired targets/demonstrations; RLHF, DPO, and other preference-optimization methods learn from rankings, preferences, reward signals, or pairwise comparisons under different objectives.
- Explain that SFT can update all base parameters, a subset, or added trainable components depending on the selected fine-tuning method; SFT describes the supervision/objective role rather than the parameter-efficiency strategy.
- Make clear that supervised examples teach behavior by optimizing toward provided targets and do not independently verify those targets. Incorrect, biased, unsafe, leaked, duplicated, or low-quality targets can be learned or memorized.
- Explain that target formatting, prompt/input representation, tokenizer/template compatibility, data weighting, sampling, loss construction, trainable-parameter scope, optimizer/schedule, and base checkpoint can materially affect results without becoming part of the universal definition.
- Distinguish dataset fit from generalization. Strong training loss or imitation of demonstrations does not prove task robustness, factual reliability, safety, calibration, or behavior outside the supervised distribution.
- Keep concrete datasets, chat templates, masking rules, training examples, hyperparameters, synthetic-target generation, checkpoints/adapters, experiment results, and provider fine-tuning APIs with their applicable catalog, learning, evidence, engineering, or project owners.
- Use the canonical entity references as research inputs for supervised fine-tuning and its relationship to later preference optimization when reader-facing rendering is activated.

## Validation

- SFT is not defined only as instruction-response training or chat-model alignment.
- Instruction tuning is introduced as a narrower repository taxonomy specialization while external literature overlap is acknowledged.
- SFT is distinguished from preference optimization/RLHF/DPO and from prompting/in-context learning.
- One target-token masking rule, chat template, loss, or full-parameter update strategy is not universalized.
- Demonstration labels/answers are not treated as independently verified truth merely because they are supervised targets.
- Training loss or target imitation is not presented as proof of generalization, factuality, safety, or task acceptance.
