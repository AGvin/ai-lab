# Jamba2

Jamba2 is AI21 Labs' model family introduced on 8 January 2026. It groups the independently identified 3B and Mini trained models; family membership does not make them interchangeable artifacts or hosted endpoints. [Primary source](https://www.ai21.com/blog/introducing-jamba2/)

## Family scope

AI21 introduced Jamba2 on 8 January 2026. The represented members are distinct trained models with different scale and deployment characteristics; downloadable artifacts and hosted aliases retain those model identities. The member pages carry their exact architecture, size, context and license facts. [Family release](https://www.ai21.com/blog/introducing-jamba2/)

## Deployment and evaluation

Choose a concrete member and an access route. The current AI21 table exposes a Mini API endpoint while marking the 3B endpoint N/A. Evaluate grounding and instruction following using representative documents, languages and prompts; vendor benchmark claims are not a substitute for deployment tests. In an agent, keep authorization and tool permissions outside model-generated text. [Provider table and limitations](https://docs.ai21.com/docs/jamba-foundation-models)

## Represented models

| Model | Scope from its concrete record |
| --- | --- |
| [Jamba2 3B](sub/models/sub/jamba2-3b/README.md) | Dense 3B hybrid model; Apache-2.0 weights and 256K documented context; AI21 API table currently says N/A. |
| [Jamba2 Mini](sub/models/sub/jamba2-mini/README.md) | Hybrid MoE with 52B total / 12B active parameters; Apache-2.0 weights; Mini API aliases resolve to a dated snapshot. |

## Relations

- Members: [Jamba2 3B](sub/models/sub/jamba2-3b/README.md), [Jamba2 Mini](sub/models/sub/jamba2-mini/README.md)
- Produced by: [AI21 Labs](../../../../../producers/sub/a/sub/ai21-labs/README.md)

## Official resources

- <https://www.ai21.com/blog/introducing-jamba2/>
- <https://docs.ai21.com/docs/jamba-foundation-models>
