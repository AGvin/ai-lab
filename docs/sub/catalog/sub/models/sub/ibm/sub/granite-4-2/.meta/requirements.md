# Documentation Requirements

## Identity and provenance

- Identify Granite 4.2 as IBM's dense decoder-only reasoning language-model family released on 25 August 2026.
- Materialize the canonical 3B, 8B, and 30B trained-model identities; keep quantized, exported, and runtime-specific distributions as artifacts unless independently qualified.
- Preserve IBM as producer and the three source-backed lineage edges from the 4.2 members to their existing Granite 4.1 Base checkpoint entities, including reciprocal derivative edges. Do not duplicate the base model identities.

## Operational decision boundaries

- The three reviewed cards document native 128K context with a long-context extension to 512K, Apache-2.0 weights, built-in thinking, tool calling, coding, and agentic workflows.
- The tested language set is English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, and Chinese; do not generalize tested quality to every language.
- Reasoning mode, tool execution, long-context quality, benchmark results, deployment support, and quantization fit remain implementation- and evaluation-sensitive.
- Tool calling produces requests; connected application software performs actions and enforces permissions.

## Validation

- Family membership resolves exactly to the 3B, 8B, and 30B nodes.
- Producer provenance resolves to IBM with the reciprocal producer edge.
- This documentation assessment grants no runtime, benchmark-reproduction, cache, or final-render credit.
