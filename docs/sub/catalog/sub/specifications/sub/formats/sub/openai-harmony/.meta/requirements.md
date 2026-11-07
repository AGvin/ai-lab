# Documentation Requirements

## Requirements

- Identify OpenAI Harmony as OpenAI's response/chat format for the gpt-oss open-weight model series, not as a generic replacement for arbitrary chat APIs or model formats.
- Explain that gpt-oss was trained on Harmony and that direct inference must apply the Harmony format correctly; provider/runtime integrations may handle this formatting on the user's behalf.
- Preserve the format's structural role at a stable level: message roles, channels, recipients/tool calls, instruction hierarchy, and serialization/parsing boundaries may be described only as supported by the current official format specification.
- Keep the Harmony format identity distinct from the `openai-harmony` reference implementation/library and from the gpt-oss model identities themselves.
- Treat encoding details, package versions, supported runtime integrations, token sequences, and implementation APIs as version-sensitive facts requiring current upstream verification.
- Render the standard `entity-relations` block from validated current-entity relations and preserve OpenAI as the producer.
- Include current official specification, implementation repository, and gpt-oss model-card references.

## Validation

- The page remains a format/specification profile rather than a gpt-oss model profile or Python/Rust library tutorial.
- Direct-inference requirements are not generalized to hosted providers that already apply Harmony internally.
- Reasoning/tool/channel details do not imply compatibility with models that were not trained for the Harmony format.
- The `produces` / `produced-by` relation pair resolves consistently to OpenAI.

## Scoped original-source qualification — 2026-11-07

- OpenAI Harmony is the serialized conversation/response format used to train and serve the gpt-oss open-weight models. Message roles, channels, tool recipients, delimiters and turn-end semantics belong to this format; it is not an interchangeable arbitrary chat API schema or an independent model release.
- OpenAI's official response-format guide says direct gpt-oss inference must use Harmony while API/runtime providers can implement the formatting themselves. This does not imply every model, tool dispatcher, parser or third-party gateway accepts identical token conventions or exposes hidden internal reasoning.
- Verified primary source 1: https://developers.openai.com/cookbook/articles/openai-harmony
- Verified primary source 2: https://github.com/openai/harmony
- Existing format/producer reciprocal identity gate only; no token stream validated, direct gpt-oss inference performed, compatibility benchmark, full security/legal audit, root-wide schema/cache/CI/render, clean pass or final gate.
