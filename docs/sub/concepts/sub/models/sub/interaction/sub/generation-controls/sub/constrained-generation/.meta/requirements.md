# Documentation Requirements

## Requirements

- Use the reader-facing title `Constrained Generation`.
- Define constrained generation as inference-time generation in which the decoding process restricts the set of allowed continuations or complete outputs according to an explicit constraint language, grammar, schema, vocabulary/value set, automaton, parser state, or another machine-checkable rule.
- Present token masking/logit filtering against valid next tokens as a common implementation pattern, while avoiding the claim that every constrained-generation system operates at exactly one token granularity or uses the same parser/automaton technique.
- Explain that constraints can enforce membership in the supported output language or candidate set to the extent implemented by the decoder, but they do not by themselves establish factual correctness, semantic intent, business validity, authorization, or safety of the allowed output.
- Distinguish constrained generation from ordinary prompting: a prompt asks or conditions the model to follow a format, while constrained decoding mechanically removes or rejects generation paths that violate the implemented constraint.
- Distinguish constrained generation from `structured-output/`: constrained generation is a mechanism; structured output is a desired machine-readable result contract that may or may not use constrained decoding.
- Explain tokenizer/constraint interaction: a character-, byte-, grammar-, schema-, or value-level rule must be translated into valid model-generation continuations, and token boundaries can affect implementation complexity and performance.
- Explain that real constraint languages can contain features beyond what a given decoder supports. Guarantee statements must therefore identify the exact grammar/schema subset, runtime, model/tokenizer compatibility, and failure behavior rather than assuming complete standards coverage.
- Acknowledge operational trade-offs such as additional decoding work, parser/state overhead, reduced candidate freedom, dead-end handling, or quality changes without promising one universal latency or accuracy effect.
- Keep concrete grammar syntax, provider schema support, runtime implementations, repair/fallback policies, business validation, tool authorization, and application-specific constraints with their applicable catalog, engineering, trustworthy-AI, or learning owners.
- Use the canonical entity references as research inputs for grammar-constrained decoding and practical coverage/quality boundaries when reader-facing rendering is activated.

## Validation

- The page does not define constrained generation as prompting alone.
- Token masking is presented as a common mechanism, not the only possible implementation form.
- Syntax/constraint compliance is not equated with factual, semantic, authorization, or safety validity.
- Constraint guarantees are scoped to the exact supported constraint language/subset and implementation.
- Constrained generation is distinguished from the broader structured-output result contract.
- The page does not imply every JSON Schema, grammar feature, tokenizer, or provider is supported equivalently.
- Legacy implementation advice is preserved only as qualified conceptual boundaries rather than universal deployment guidance.
