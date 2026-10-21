# Clef

Clef is Cloudflare's concrete 27B decision model, released on 1 October 2026 and post-trained from Qwen/Qwen3.8-27B. It uses a joint schema head to score predefined answers from text, structured state and supported visual inputs, without free-form text generation. [Source 1](https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/) · [Source 2](https://huggingface.co/Cloudflare/clef)

## Identity and lineage

Cloudflare's official card identifies this as a 27B model post-trained from `Qwen/Qwen3.8-27B`. It adds a joint schema head and scores every allowed option in one forward pass. Text/JSON, images and video are documented inputs; the output is a probability distribution over the supplied choices, not a chat response. Cloudflare publishes the release under Apache 2.0. [Official model card](https://huggingface.co/Cloudflare/clef) · [Training method](https://blog.cloudflare.com/clef-decision-models/)

## Hosted context and inputs

The current `@cf/cloudflare/clef` page gives a 65,536-token context. Questions and tokenized media count against that limit. If those exceed the context, the request fails; otherwise, the text `state` is truncated to fit. Measure the retained evidence for long records instead of assuming the whole document was scored. The October serving speedup changed the deployment while leaving the model weights unchanged. [Current hosted contract](https://developers.cloudflare.com/workers-ai/models/clef/) · [Serving update](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

## Local operation and decisions

Use the authored model-card workflow, including the backbone weights, joint head, processor and `joint_schema_model.py` loader. Pin and review that implementation and validate the intended runtime; a generic text-generation integration does not exercise the documented decision interface. Evaluate option coverage, calibration and false-positive costs on representative tasks. Keep fallback decisions and permissions in the application before turning a score into a block, workflow transition or tool call. [Release files and supported workflow](https://huggingface.co/Cloudflare/clef)

## Relations

- Derived from: [Qwen3.8-27B](../../../../../../../alibaba/sub/qwen/sub/qwen3-8/sub/models/sub/qwen3-8-27b/README.md)
- Member of: [Clef](../../../../README.md)

## Official resources

- <https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/>
- <https://huggingface.co/Cloudflare/clef>
- <https://blog.cloudflare.com/clef-decision-models/>
- <https://developers.cloudflare.com/workers-ai/models/clef/>
- <https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/>
