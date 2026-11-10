# Tiny Aya

Tiny Aya is the compact multilingual text-model series introduced on 17 February 2026. The four original instruction-tuned models are Global, Earth, Fire and Water. The series also now represents two distinct pretrained bases and two separately trained reasoning models. [Source 1](https://cohere.com/blog/cohere-labs-tiny-aya) · [Source 2](https://docs.cohere.com/docs/tiny-aya)

## Release and global/regional choice

The official launch is dated 17 February 2026; the technical paper followed on 12 March. Current documentation separates a pretrained base from the four instruction-tuned variants represented here. All four have shared language coverage, while their training emphasizes different regional tasks. Regional positioning guides evaluation; it is not a claim that a variant supports only that region's languages. [Launch date](https://cohere.com/blog/cohere-labs-tiny-aya) · [Current variants](https://docs.cohere.com/docs/tiny-aya) · [Training and evaluation](https://arxiv.org/html/2603.11510v1)

## Training lineage

Original [Tiny Aya Base](sub/models/sub/tiny-aya-base/README.md) has an 8K input window and is the pretrained origin of Global. A separate [Tiny Aya Base 32K](sub/models/sub/tiny-aya-base-32k/README.md) is explicitly the upstream for [L2-Thinker](sub/models/sub/tiny-aya-l2-thinker/README.md) and [En-Thinker](sub/models/sub/tiny-aya-en-thinker/README.md). The current evidence does not establish an exact 8K Base-to-32K Base weight derivation. [First-party research](https://cohere.com/blog/building-multilingual-bridges) [Base card](https://huggingface.co/CohereLabs/tiny-aya-base) [32K card](https://huggingface.co/CohereLabs/tiny-aya-base-32K).

The technical paper describes regional supervised fine-tuning from Tiny Aya Base and a globally balanced post-trained model. Each final regional release merges a regional checkpoint with that global checkpoint. Global is therefore a trained merge parent of Earth, Fire and Water; they remain distinct trained models with their existing series membership. [Figure 2 and model merging](https://arxiv.org/html/2603.11510v1)

## Access and deployment

Base checkpoints are not instruction-tuned chat models. L2-Thinker produces reasoning traces in the prompt language, while En-Thinker uses English thinking and multilingual final answers; both expose model-specific templates and a 32K combined context. Their gated CC-BY-NC research rights are distinct from the original four live Tiny Aya Chat routes and require their own runtime, task and safety evaluation. Publisher results across 60 languages are not independent quality certification. [Cohere research](https://cohere.com/blog/building-multilingual-bridges) [License](https://cohere.com/cohere-labs-cc-by-nc-license).

The current Cohere table lists all four represented variants as live Chat models. Official weight repositories and GGUF distributions provide separate local deployment routes with their own access and license conditions. Small-model positioning does not establish that every precision, context and runtime fits every device. Compare the intended languages and tasks using the selected artifact and serving route. [Live routes](https://docs.cohere.com/docs/models) · [Access and distributions](https://docs.cohere.com/docs/tiny-aya)

## Represented members

| Model or series | Scope from its concrete record |
| --- | --- |
| [Tiny Aya Earth](sub/models/sub/tiny-aya-earth/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; West Asian and African language tasks emphasis; merged with Global. |
| [Tiny Aya Fire](sub/models/sub/tiny-aya-fire/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; South Asian language tasks emphasis; merged with Global. |
| [Tiny Aya Global](sub/models/sub/tiny-aya-global/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; global balance and regional merge parent. |
| [Tiny Aya Water](sub/models/sub/tiny-aya-water/README.md) | 3.35B text model; 70 languages; 8K context; live Chat route; European and Asia-Pacific language tasks emphasis; merged with Global. |
| [Tiny Aya Base](sub/models/sub/tiny-aya-base/README.md) | 3.35B original pretrained text model; 8K input; gated research weights. |
| [Tiny Aya Base 32K](sub/models/sub/tiny-aya-base-32k/README.md) | 3.35B long-context pretrained text model; 32K combined input/output; gated research weights. |
| [Tiny Aya L2-Thinker](sub/models/sub/tiny-aya-l2-thinker/README.md) | 3.35B multilingual in-language reasoning text model; 32K combined input/output; gated research weights. |
| [Tiny Aya En-Thinker](sub/models/sub/tiny-aya-en-thinker/README.md) | 3.35B multilingual English-trace reasoning text model; 32K combined input/output; gated research weights. |

## Relations

- Members: [Tiny Aya Earth](sub/models/sub/tiny-aya-earth/README.md), [Tiny Aya Fire](sub/models/sub/tiny-aya-fire/README.md), [Tiny Aya Global](sub/models/sub/tiny-aya-global/README.md), [Tiny Aya Water](sub/models/sub/tiny-aya-water/README.md)
- Additional members: [Tiny Aya Base](sub/models/sub/tiny-aya-base/README.md), [Tiny Aya Base 32K](sub/models/sub/tiny-aya-base-32k/README.md), [Tiny Aya L2-Thinker](sub/models/sub/tiny-aya-l2-thinker/README.md), [Tiny Aya En-Thinker](sub/models/sub/tiny-aya-en-thinker/README.md)
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
- <https://huggingface.co/CohereLabs/tiny-aya-base-32K>
- <https://huggingface.co/CohereLabs/tiny-aya-l2-thinker>
- <https://huggingface.co/CohereLabs/tiny-aya-en-thinker>
- <https://cohere.com/blog/building-multilingual-bridges>
- <https://arxiv.org/abs/2609.10445>
