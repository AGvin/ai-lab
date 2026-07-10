# Model Usage and Generation

<!--
ai_content:
  managed: true
  l10n: true
-->

Concepts for using trained models effectively through chats, APIs, applications, and local runtimes.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`tokens-and-tokenization/`](./sub/tokens-and-tokenization/) — The process of splitting input and output into the units a model reads and generates.
- [`context-window/`](./sub/context-window/) — The bounded amount of tokenized information a model can consider during one request.
- [`prompting/`](./sub/prompting/) — The practice of supplying instructions, context, examples, and constraints to guide a model.
- [`system-prompts/`](./sub/system-prompts/) — High-priority instructions that define an assistant's role, behavior, and operational boundaries.
- [`structured-output/`](./sub/structured-output/) — Model output constrained to a machine-readable structure such as JSON or a schema.
- [`hallucinations/`](./sub/hallucinations/) — Unsupported or incorrect model output presented in a plausible form.

## Useful

- [`few-shot-prompting/`](./sub/few-shot-prompting/) — Prompting that includes a small number of examples to demonstrate desired behavior.
- [`sampling-parameters/`](./sub/sampling-parameters/) — Controls such as temperature, top-p, top-k, and seed that influence token selection.
- [`reasoning-models/`](./sub/reasoning-models/) — Models optimized to spend additional computation on multi-step problem solving.
- [`model-capabilities-and-limitations/`](./sub/model-capabilities-and-limitations/) — The practical strengths, boundaries, and failure modes of a specific model or deployment.

## Specialized

- [`constrained-generation/`](./sub/constrained-generation/) — Generation restricted by a grammar, schema, token set, or other formal constraint.
- [`chain-of-thought/`](./sub/chain-of-thought/) — Intermediate reasoning text or internal computation used to support multi-step answers.
