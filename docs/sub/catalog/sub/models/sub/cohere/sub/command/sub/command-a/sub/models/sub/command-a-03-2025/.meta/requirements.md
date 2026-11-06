# Documentation Requirements

## Identity and provenance

- Command A is the March 2025 111B text-generation model for multilingual conversation, grounded generation and tool use.
- The model card identifies c4ai-command-a-03-2025 and explicitly credits Cohere and Cohere Labs. The canonical dated node represents the learned model, separately from its API route, local precision builds and derived models. [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025).
- The API identifier is command-a-03-2025 and is listed live. The source-backed derivative relations point to A Reasoning, A Translate and A Vision; each retains its own identity. [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command A Reasoning model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-reasoning-08-2025?blobs=true) [Command A Translate model card public metadata](https://huggingface.co/api/models/CohereLabs/command-a-translate-08-2025?blobs=true) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025).

## Operational decision boundaries

- Cohere documents 111B parameters, a 256K supported context and 23 languages; the current API table lists an 8K maximum output. The public weight card ships a 128K configuration and explains how to configure the larger supported context, so 256K is not asserted for every default local load. [Command A documentation](https://docs.cohere.com/docs/command-a) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025).
- The public research weights state CC-BY-NC 4.0 and an additional acceptable-use policy. Commercial weight use needs the applicable permission; availability through a paid API does not change the downloaded-weight terms. [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) [Cohere Labs CC-BY-NC license](https://cohere.com/cohere-labs-cc-by-nc-license) [Cohere Labs acceptable-use policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy).
- Use the matching chat, grounding and tool templates. Retrieval sources and tool execution come from the application; generated citations and calls still require task-specific validation. Hardware and throughput claims in the release documentation were not reproduced. [Command A model card](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) [Command A documentation](https://docs.cohere.com/docs/command-a).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
