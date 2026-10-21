# Command A+

Command A+ is the May 2026 sparse mixture-of-experts model for text and image understanding, reasoning and tool workflows.

## Identity and provenance

The model card explicitly credits Cohere and Cohere Labs and reports 218B total parameters with 25B active per token. The BF16 and W4A4 repositories describe distributions of Command A+, not additional learned-model identities. [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Command A+ W4A4 distribution card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4).

The current API identity is command-a-plus-05-2026. Cohere’s launch is dated 20 May 2026; the model remains listed live. [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A+ launch article](https://cohere.com/blog/command-a-plus) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).

## Decision and operating boundaries

- Cohere documents a 128K context, a 64K output limit, 48 supported languages and text/image input with text output. Image understanding does not imply image generation. Active-parameter count does not represent total memory needed to load weights and maintain runtime state. [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The model weights state Apache 2.0. Cohere’s one-B200/two-H100 serving claim is attached to the W4A4 distribution; it must not be applied to BF16 or every context, concurrency and runtime configuration. [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Command A+ W4A4 distribution card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4) [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus).
- Reasoning, tool calling and serving controls belong to the selected implementation. Tool requests need an execution harness, and provider quality or efficiency comparisons do not establish local benchmark performance. [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16).

## Catalog relations

- [Cohere Labs](../../../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Command A](../../../../) — series or family.

## Official resources

- [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus).
- [Command A+ release](https://docs.cohere.com/v1/changelog/command-a-plus-05-2026).
- [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16).
- [Command A+ W4A4 distribution card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4).
- [Command A+ launch article](https://cohere.com/blog/command-a-plus).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
