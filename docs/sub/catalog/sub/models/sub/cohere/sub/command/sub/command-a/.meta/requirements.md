# Documentation Requirements

## Identity and provenance

- The Command A series groups the original Command A, A+, Reasoning, Translate and Vision models.
- The dated members are separate model identities. Public card metadata lists Command A as a base for Reasoning and Translate; the Vision card also explicitly identifies its Command A language component. A+ is not inferred to derive from A merely because of its name. [Command A Reasoning model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-reasoning-08-2025?blobs=true) [Command A Translate model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-translate-08-2025?blobs=true) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16).

## Operational decision boundaries

- Select by the task: original A for text and tools; Reasoning for optional thinking; Translate for translation; Vision for image understanding; A+ for its text/image, reasoning and tool interface. These descriptions do not guarantee an application’s accuracy. [Command A documentation](https://docs.cohere.com/docs/command-a) [Command A+ documentation](https://docs.cohere.com/docs/command-a-plus) [Command A Reasoning documentation](https://docs.cohere.com/docs/command-a-reasoning) [Command A Translate documentation](https://docs.cohere.com/docs/command-a-translate) [Command A Vision documentation](https://docs.cohere.com/docs/command-a-vision).
- A+ is a sparse 218B-total/25B-active model with Apache 2.0 weights. The other reviewed A members have different dense scale, context settings and CC-BY-NC research-weight terms. Quantized A+ distributions remain artifacts of one model. [Command A+ BF16 model card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-bf16) [Command A+ W4A4 distribution card](https://huggingface.co/CohereLabs/command-a-plus-05-2026-w4a4) [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) [Command A Reasoning model card](https://huggingface.co/CohereLabs/command-a-reasoning-08-2025) [Command A Translate model card](https://huggingface.co/CohereLabs/command-a-translate-08-2025) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
