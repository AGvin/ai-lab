# Clef-flash

Clef-flash is Cloudflare's concrete 9B decision model, released on 1 October 2026 and post-trained from Qwen/Qwen3.5-9B. It scores allowed answers to typed questions from text, structured state and supported visual inputs, and is positioned by Cloudflare for lower-latency decisions. [Source 1](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/) · [Source 2](https://huggingface.co/Cloudflare/clef-flash)

## Identity and weights

The official `Cloudflare/clef-flash` card identifies a 9B model post-trained from `Qwen/Qwen3.5-9B`, with a joint schema head and Apache 2.0 licensing. It scores allowed choices from text/JSON and supported image/video input. Cloudflare's low-latency positioning is a vendor claim to test against the intended workload. [Official model and upstream backbone](https://huggingface.co/Cloudflare/clef-flash) · [Release and vendor positioning](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/)

## Hosted limit versus weight capability

On 9 October 2026, Cloudflare reduced the advertised hosted context from 64K to 24K and explicitly said the weights were unchanged. The current Workers AI page specifies 24,576 tokens; the changelog separately says the self-hosted weights support up to 256K. Questions and media consume the hosted context, and the service can truncate text state to fit. Inspect retained content and measure memory at the intended local context instead of treating the hosted limit as the model's architecture. [Context change and weight continuity](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/) · [Current hosted contract](https://developers.cloudflare.com/workers-ai/models/clef-flash/)

## Operational evaluation

For local use, pin the official weight revision, joint schema head, processor and authored loader implementation. Test option coverage, probability calibration and failure handling on real task examples, including cases where none of the listed answers fits. Decide outside the model which confidence levels require escalation or permit an action. A speed comparison or API-compatible response does not establish safe autonomous behavior. [Implementation and evaluation evidence](https://huggingface.co/Cloudflare/clef-flash)

## Relations

- Member of: [Clef](../../../../README.md)

## Official resources

- <https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/>
- <https://huggingface.co/Cloudflare/clef-flash>
- <https://developers.cloudflare.com/workers-ai/models/clef-flash/>
- <https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/>
- <https://blog.cloudflare.com/clef-decision-models/>
