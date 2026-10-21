# Tiny Aya

Tiny Aya is the compact multilingual text-model series introduced on 17 February 2026. The represented instruction-tuned models are Global, Earth, Fire and Water. [Source 1](https://cohere.com/blog/cohere-labs-tiny-aya) · [Source 2](https://docs.cohere.com/docs/tiny-aya)

## Release and global/regional choice

The official launch is dated 17 February 2026; the technical paper followed on 12 March. Current documentation separates a pretrained base from the four instruction-tuned variants represented here. All four have shared language coverage, while their training emphasizes different regional tasks. Regional positioning guides evaluation; it is not a claim that a variant supports only that region's languages. [Launch date](https://cohere.com/blog/cohere-labs-tiny-aya) · [Current variants](https://docs.cohere.com/docs/tiny-aya) · [Training and evaluation](https://arxiv.org/html/2603.11510v1)

## Training lineage

The technical paper describes regional supervised fine-tuning from Tiny Aya Base and a globally balanced post-trained model. Each final regional release merges a regional checkpoint with that global checkpoint. Global is therefore a trained merge parent of Earth, Fire and Water; they remain distinct trained models with their existing series membership. [Figure 2 and model merging](https://arxiv.org/html/2603.11510v1)

## Access and deployment

The current Cohere table lists all four represented variants as live Chat models. Official weight repositories and GGUF distributions provide separate local deployment routes with their own access and license conditions. Small-model positioning does not establish that every precision, context and runtime fits every device. Compare the intended languages and tasks using the selected artifact and serving route. [Live routes](https://docs.cohere.com/docs/models) · [Access and distributions](https://docs.cohere.com/docs/tiny-aya)

## Represented members

| Model or series | Scope from its concrete record |
| --- | --- |
| [Tiny Aya Earth](sub/models/sub/tiny-aya-earth/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; West Asian and African language tasks emphasis; merged with Global. |
| [Tiny Aya Fire](sub/models/sub/tiny-aya-fire/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; South Asian language tasks emphasis; merged with Global. |
| [Tiny Aya Global](sub/models/sub/tiny-aya-global/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; global balance and regional merge parent. |
| [Tiny Aya Water](sub/models/sub/tiny-aya-water/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; European and Asia-Pacific language tasks emphasis; merged with Global. |

## Relations

- Members: [Tiny Aya Earth](sub/models/sub/tiny-aya-earth/README.md), [Tiny Aya Fire](sub/models/sub/tiny-aya-fire/README.md), [Tiny Aya Global](sub/models/sub/tiny-aya-global/README.md), [Tiny Aya Water](sub/models/sub/tiny-aya-water/README.md)
- Member of: [Aya](../../README.md)

## Official resources

- <https://cohere.com/blog/cohere-labs-tiny-aya>
- <https://docs.cohere.com/docs/tiny-aya>
- <https://arxiv.org/html/2603.11510v1>
- <https://docs.cohere.com/docs/models>
- <https://huggingface.co/CohereLabs/tiny-aya-global>
- <https://huggingface.co/CohereLabs/tiny-aya-earth>
- <https://huggingface.co/CohereLabs/tiny-aya-fire>
- <https://huggingface.co/CohereLabs/tiny-aya-water>
- <https://huggingface.co/CohereLabs/tiny-aya-base>
