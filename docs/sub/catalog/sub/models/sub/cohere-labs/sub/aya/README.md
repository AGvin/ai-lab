# Aya

Aya is the multilingual research-model family led by Cohere Labs. The represented branches include the original Aya 101 (13B, 101-language text model under Apache-2.0), Aya 23 (later non-commercial research weights), Aya Expanse for text, Aya Vision for text-and-image understanding, and Tiny Aya for compact multilingual text models. [Primary source](https://docs.cohere.com/docs/aya)

## Family and research initiative

The current Aya documentation highlights Expanse, Vision and Tiny Aya, while Aya 101 (13 February 2024) and Aya 23 (23 May 2024) remain separate historical trained-model releases. Aya 101 is a direct family member, whereas Aya 23 is a series with distinct 8B and 35B children. The broader initiative also covers datasets, evaluations and research. Model rights, languages, context and architecture must be selected from the concrete card, not inherited from the family. Each concrete record carries its own technical and operational facts. [Family documentation](https://docs.cohere.com/docs/aya) · [Aya initiative](https://cohere.com/research/aya)

## Selection and evaluation

Choose text-only generation, image-grounded text, or a compact regional/global model before comparing model sizes and serving routes. Evaluate the actual languages, scripts, translation directions and document types required by the application. Vendor benchmark results describe the reported evaluation setup and do not establish uniform quality across all languages or tasks. [Current model table](https://docs.cohere.com/docs/models) · [Example of task-specific multilingual evaluation](https://arxiv.org/html/2603.11510v1)

## Represented members

| Model or series | Scope from its concrete record |
| --- | --- |
| [Aya 101](sub/aya-101/README.md) | Original 13B T5-style text-to-text instruction model across 101 languages, independently released under Apache-2.0; no documented standard context size or verified current Cohere API route. |
| [Aya 23](sub/aya-23/README.md) | Historical instruction-tuned text models with separate 8B and 35B checkpoints; 23 languages, 8K context and gated CC-BY-NC-4.0 weights. |
| [Aya Expanse](sub/aya-expanse/README.md) | Text-model series containing distinct 8B and 32B releases. |
| [Aya Vision](sub/aya-vision/README.md) | Text-and-image understanding series with distinct 8B and 32B language-model ancestry. |
| [Tiny Aya](sub/tiny-aya/README.md) | Compact global/regional instruction-model series with documented merging from the Global checkpoint. |

## Relations

- Members: [Aya 101](sub/aya-101/README.md), [Aya 23](sub/aya-23/README.md), [Aya Expanse](sub/aya-expanse/README.md), [Aya Vision](sub/aya-vision/README.md), [Tiny Aya](sub/tiny-aya/README.md)
- Produced by: [Cohere Labs](../../../../../producers/sub/c/sub/cohere-labs/README.md)

## Official resources

- <https://cohere.com/blog/aya>
- <https://huggingface.co/CohereLabs/aya-101>
- <https://cohere.com/blog/aya23>
- <https://docs.cohere.com/docs/aya>
- <https://cohere.com/research/aya>
- <https://docs.cohere.com/docs/models>
- <https://arxiv.org/html/2603.11510v1>
