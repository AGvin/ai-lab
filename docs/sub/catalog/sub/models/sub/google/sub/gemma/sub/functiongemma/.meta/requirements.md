# Documentation Requirements

## Requirements

- Identify FunctionGemma as Google's released 270M open Gemma model specialized for function calling and on-device agent/tool-routing workflows.
- Preserve its current function-call/chat boundary, customization/fine-tuning orientation, and local/mobile/IoT positioning only while first-party documentation supports those facts.
- Keep FunctionGemma distinct from Gemma 3 270M, general-purpose Gemma 4, agent frameworks, tool schemas, hosted Gemini function calling, and downstream device applications.
- Treat supported runtimes, quantization/precision, fine-tuning recipes, tool-call formatting, device performance, artifacts, licenses, and provider benchmark claims as freshness-sensitive.
- Attribute function-calling accuracy and on-device performance comparisons to Google/Google DeepMind or the cited evaluator.

## Validation

- The node remains a concrete specialized Gemma model rather than a generic function-calling concept.
- Tool schemas and host-agent behavior are not generalized into permanent model architecture.

## Verified identity and provenance

FunctionGemma is the Gemma 3 270M-based function-calling model released as google/functiongemma-270m-it; it is intended for task-specific fine-tuning rather than direct general dialogue.

## Source-scoped operating boundaries

- Google recommends fine-tuning for the application's single-turn or multi-turn function-calling data. The base release is not intended to act as a direct dialogue model. [Intended-use boundary](https://ai.google.dev/gemma/docs/functiongemma/model_card).
- Generated calls are model outputs, not executed actions. The integration must validate arguments, restrict callable tools, and authorize device or account actions; a local model alone does not supply those controls. [FunctionGemma model card](https://ai.google.dev/gemma/docs/functiongemma/model_card).

## Source evidence

- <https://ai.google.dev/gemma/docs/functiongemma/model_card>
- <https://huggingface.co/google/functiongemma-270m-it>
