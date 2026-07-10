# Instruction Tuning

Instruction tuning trains a model on diverse instruction-and-response examples so it becomes better at following natural-language tasks.

## Core idea

A pretrained language model is optimized mainly to continue text. Instruction tuning reshapes that behavior toward responding to requests, respecting task descriptions, and generalizing across many instruction formats. It is usually implemented through supervised fine-tuning and may be followed by preference optimization.

## Practical use

- Create general assistant behavior from a base model.
- Improve zero-shot task following.
- Teach response formats and refusal patterns.
- Adapt a model to a domain's common instructions.

## Trade-offs and limitations

Instruction tuning can reduce raw completion behavior and introduce the biases or limitations of the instruction dataset. A model may learn superficial response patterns without becoming more factually reliable.

## Common mistakes

- Using a narrow instruction set and expecting broad generalization.
- Confusing helpful tone with correctness.
- Omitting difficult or ambiguous examples.
- Ignoring the tokenizer and chat template expected by the model.

## Related concepts

- [Training and Adaptation](../../)
- [Supervised Fine-Tuning](../supervised-fine-tuning/)
- [Preference Optimization](../preference-optimization/)
- [Prompting](../../../model-usage-and-generation/sub/prompting/)
