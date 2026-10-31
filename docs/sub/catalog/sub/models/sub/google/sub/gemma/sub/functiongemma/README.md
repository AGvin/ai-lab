# FunctionGemma

FunctionGemma is the Gemma 3 270M-based function-calling model released as google/functiongemma-270m-it; it is intended for task-specific fine-tuning rather than direct general dialogue.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- Google recommends fine-tuning for the application's single-turn or multi-turn function-calling data. The base release is not intended to act as a direct dialogue model. [Intended-use boundary](https://ai.google.dev/gemma/docs/functiongemma/model_card).
- Generated calls are model outputs, not executed actions. The integration must validate arguments, restrict callable tools, and authorize device or account actions; a local model alone does not supply those controls. [FunctionGemma model card](https://ai.google.dev/gemma/docs/functiongemma/model_card).

## Official resources

- <https://deepmind.google/models/gemma/functiongemma/>
- <https://ai.google.dev/gemma/docs/releases>
- <https://ai.google.dev/gemma/docs/functiongemma/model_card>
- <https://huggingface.co/google/functiongemma-270m-it>
