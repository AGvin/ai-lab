# LoRA

Low-Rank Adaptation (LoRA) is a parameter-efficient fine-tuning method that learns compact low-rank updates while keeping the original model weights frozen.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

A full fine-tune updates a large portion of a model's parameters. LoRA instead represents the update for selected layers as the product of two much smaller trainable matrices. The base model remains unchanged, while the adapter stores only the learned difference.

This allows one base model to support multiple compact task, domain, character, or style variants.

## How it works

1. Select target modules, commonly attention or projection layers.
2. Freeze the original model weights.
3. Attach trainable low-rank matrices to the selected modules.
4. Train only the adapter parameters on the adaptation dataset.
5. Keep the adapter separate or merge it into compatible base weights for deployment.

Important settings include rank, scaling factor, target modules, learning rate, dropout, dataset quality, and training duration.

## Practical uses

- Adapt a language model to a domain, output convention, or recurring task.
- Add a visual style, subject, character, or product concept to an image model.
- Maintain several small variants without storing a full model copy for each one.
- Share adaptation artifacts while requiring users to obtain the compatible base model separately.

## Example

A team can keep one general-purpose coding model and train separate LoRA adapters for an internal framework, documentation style, and review workflow. The runtime loads the base model once and activates the adapter needed for the current task.

## Compatibility

A LoRA adapter is tied to assumptions about the training setup. Verify:

- exact base model family and revision;
- tokenizer or text encoder compatibility;
- target layer names and architecture;
- adapter format and runtime support;
- whether deployment loads adapters dynamically or requires merged weights.

An adapter created for one checkpoint should not be assumed to work correctly with another model that merely has a similar name.

## Trade-offs and limitations

- Low-rank capacity may be insufficient for large behavioral changes.
- Poor training data can introduce artifacts, regressions, or memorized errors.
- Multiple adapters may interact unpredictably when combined.
- Merging simplifies deployment but removes independent adapter switching.
- LoRA changes behavior; it is not a dependable replacement for RAG when facts must remain current or traceable.

## Practical checklist

- Can prompting, tools, structured output, or RAG solve the problem without training?
- Is the exact base model recorded and available?
- Are training, validation, and holdout examples separated?
- Which target modules and rank fit the intended change?
- How will the adapter be evaluated against the unchanged base model?
- Will it remain separate, be combined with others, or be merged for deployment?

## Related concepts

- [Training and Adaptation](../../)
- [Parameter-Efficient Fine-Tuning](../parameter-efficient-fine-tuning/)
- [QLoRA](../qlora/)
- [Fine-Tuning](../fine-tuning/)
- [RAG](../../../retrieval-and-knowledge/sub/rag/)
