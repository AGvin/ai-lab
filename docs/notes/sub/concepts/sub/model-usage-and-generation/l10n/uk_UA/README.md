<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:dfefba9adf44f35b87cdeb6be911bd9662c7c07b
  mode: copy-through
-->

# Model Usage and Generation



Concepts for using trained models effectively through chats, APIs, applications, and local runtimes.

## Переклади

- [English](../../)
- Українська — поточна

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`tokens-and-tokenization/`](../../sub/tokens-and-tokenization/l10n/uk_UA/) — The process of splitting input and output into the units a model reads and generates.
- [`context-window/`](../../sub/context-window/l10n/uk_UA/) — The bounded amount of tokenized information a model can consider during one request.
- [`prompting/`](../../sub/prompting/l10n/uk_UA/) — The practice of supplying instructions, context, examples, and constraints to guide a model.
- [`system-prompts/`](../../sub/system-prompts/l10n/uk_UA/) — High-priority instructions that define an assistant's role, behavior, and operational boundaries.
- [`structured-output/`](../../sub/structured-output/l10n/uk_UA/) — Model output constrained to a machine-readable structure such as JSON or a schema.
- [`hallucinations/`](../../sub/hallucinations/l10n/uk_UA/) — Unsupported or incorrect model output presented in a plausible form.

## Useful

- [`few-shot-prompting/`](../../sub/few-shot-prompting/l10n/uk_UA/) — Prompting that includes a small number of examples to demonstrate desired behavior.
- [`sampling-parameters/`](../../sub/sampling-parameters/l10n/uk_UA/) — Controls such as temperature, top-p, top-k, and seed that influence token selection.
- [`reasoning-models/`](../../sub/reasoning-models/l10n/uk_UA/) — Models optimized to spend additional computation on multi-step problem solving.
- [`model-capabilities-and-limitations/`](../../sub/model-capabilities-and-limitations/l10n/uk_UA/) — The practical strengths, boundaries, and failure modes of a specific model or deployment.

## Specialized

- [`constrained-generation/`](../../sub/constrained-generation/l10n/uk_UA/) — Generation restricted by a grammar, schema, token set, or other formal constraint.
- [`chain-of-thought/`](../../sub/chain-of-thought/l10n/uk_UA/) — Intermediate reasoning text or internal computation used to support multi-step answers.
