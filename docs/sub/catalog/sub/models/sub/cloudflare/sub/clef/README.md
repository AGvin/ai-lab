# Clef

Clef is Cloudflare's released family of decision models. It groups the independently identified Clef, Clef-flash and Clef-omni models, which score allowed answers to typed questions rather than produce unconstrained text responses. [Source 1](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/) · [Source 2](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

## Decision interface

Cloudflare's 1 October 2026 release introduced Clef and Clef-flash; its 9 October update added Clef-omni. These models accept an input state and typed questions, then return probabilities over allowed answers. The documented interface supports yes/no `noul` questions, enumerated `choice` questions and bounded ordinal `score` questions. API compatibility with Jev does not make Clef a Jev model or transfer its producer identity. [Release and typed-question interface](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/) · [Third member release](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

## Access and evaluation

Choose a member according to the input modalities, complete task context and tested decision quality. Cloudflare publishes model-specific weights and implementations; Workers AI applies its own serving limits. Define fallback outcomes when no allowed option is appropriate, measure false positives and false negatives on representative inputs, and calibrate action thresholds. Keep input documents and model probabilities separate from permission to block a request, change a record or invoke a tool. Cloudflare's speed and benchmark results remain vendor measurements. [Training and vendor evaluation scope](https://blog.cloudflare.com/clef-decision-models/) · [Serving changes without new weights](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

## Represented models

| Model | Scope from its concrete record |
| --- | --- |
| [Clef](sub/models/sub/clef/README.md) | 27B derivative of Qwen3.8-27B; typed decision probabilities; current Workers AI context 65,536 tokens. |
| [Clef-flash](sub/models/sub/clef-flash/README.md) | 9B derivative of Qwen3.5-9B; current hosted context 24,576 tokens; hosted reduction did not change weights. |
| [Clef-omni](sub/models/sub/clef-omni/README.md) | 30B total / 3B active MoE; native audio/video input; option probabilities; current hosted context 64,000 tokens. |

## Relations

- Members: [Clef](sub/models/sub/clef/README.md), [Clef-flash](sub/models/sub/clef-flash/README.md), [Clef-omni](sub/models/sub/clef-omni/README.md)
- Produced by: [Cloudflare](../../../../../producers/sub/c/sub/cloudflare/README.md)

## Official resources

- <https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/>
- <https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/>
- <https://blog.cloudflare.com/clef-decision-models/>
