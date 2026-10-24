# Documentation Requirements

## Identity and provenance

- Command A+ is the May 2026 sparse mixture-of-experts model for text and image understanding, reasoning and tool workflows.
- The model card explicitly credits Cohere and Cohere Labs and reports 218B total parameters with 25B active per token. The BF16 and W4A4 repositories describe distributions of Command A+, not additional learned-model identities. [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Command A+ W4A4 distribution card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4).
- The current API identity is command-a-plus-05-2026. Cohere’s launch is dated 20 May 2026; the model remains listed live. [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A+ launch article](https://cohere.com/blog/command-a-plus) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).

## Operational decision boundaries

- Cohere documents a 128K context, a 64K output limit, 48 supported languages and text/image input with text output. Image understanding does not imply image generation. Active-parameter count does not represent total memory needed to load weights and maintain runtime state. [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The model weights state Apache 2.0. Cohere’s one-B200/two-H100 serving claim is attached to the W4A4 distribution; it must not be applied to BF16 or every context, concurrency and runtime configuration. [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Command A+ W4A4 distribution card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4) [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus).
- Reasoning, tool calling and serving controls belong to the selected implementation. Tool requests need an execution harness, and provider quality or efficiency comparisons do not establish local benchmark performance. [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
