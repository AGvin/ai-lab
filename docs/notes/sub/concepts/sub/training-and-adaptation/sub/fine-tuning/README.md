# Fine-Tuning

Fine-tuning continues training an existing model on targeted data to modify its behavior, domain performance, style, or task specialization.

## Core idea

A pretrained model already contains broad representations. Fine-tuning adjusts some or all parameters using a smaller task-specific dataset. This is different from retrieval: fine-tuning changes behavior encoded in model weights, while retrieval supplies external information at inference time.

## Practical use

- Improve consistent task formatting or domain behavior.
- Teach specialized terminology or interaction patterns.
- Adapt a base model for classification, extraction, or instruction following.
- Reduce the size of prompts needed to demonstrate recurring behavior.

## Design considerations

Start with a clear baseline using prompting, tools, and retrieval. Build separate training, validation, and test datasets. Track the base model, dataset version, hyperparameters, and resulting checkpoint. Evaluate both target improvement and regressions on general tasks.

## Trade-offs and limitations

Fine-tuning requires data curation, compute, evaluation, and model lifecycle management. It can overfit, forget useful capabilities, or memorize sensitive examples. It is not a reliable way to inject frequently changing facts.

## Common mistakes

- Fine-tuning to solve a knowledge-retrieval problem.
- Training on low-quality generated examples without review.
- Evaluating on examples included in training.
- Assuming the adapted model remains compatible with every runtime or quantization.

## Related concepts

- [Training and Adaptation](../../)
- [Supervised Fine-Tuning](../supervised-fine-tuning/)
- [Parameter-Efficient Fine-Tuning](../parameter-efficient-fine-tuning/)
- [RAG](../../../retrieval-and-knowledge/sub/rag/)
