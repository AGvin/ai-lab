# FLUX 3 Image Klein Base

FLUX 3 Image Klein Base is Black Forest Labs' 5.6-billion-parameter undistilled base image-generation and editing model, released on 2026-10-15 under the FLUX Kommunity license. The generator count excludes the text encoder and separate prompt-upsampling stage. [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein) [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein).

## Identity and scope

The released base and step-distilled image models are distinct learned objects. BF16, FP8, INT8 and NVFP4 builds of the same learned checkpoint are distribution artifacts rather than automatic new model identities. [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein) [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein).

The documented pipeline takes a detailed prompt and up to ten reference images, with optional layout boxes. It uses a separate Qwen3-VL-4B-Instruct text encoder; the 9B Prompt Upsampler is a separately fine-tuned Qwen3.5-9B vision-language model, not that text encoder or another FLUX image generator. [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein distilled model card](https://huggingface.co/black-forest-labs/flux-3-image-klein) [FLUX 3 Image Klein Prompt Upsampler card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup).

## Use and limitations

Use the base sampling workflow, documented at 50 steps. The card and reference code show different example guidance values, so pin the selected runtime and settings rather than presenting one example as an intrinsic constant. [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein).

BFL requires detailed prompt upsampling for the intended generation, editing and layout workflow. The reference CLI loads BFL's separate 9B upsampling model by default; other runtimes may require an explicit captioning step. The upsampling stage is part of the intended workflow, while the exact BFL 9B implementation is replaceable: BFL documents using another LLM with its supplied system prompts. Verify the actual prompt route, including any remote service, before claiming that processing stays local. [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein distilled model card](https://huggingface.co/black-forest-labs/flux-3-image-klein) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein) [FLUX 3 Image Klein Prompt Upsampler card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup).

Weights use FLUX Kommunity v1.0; code and the separate prompt upsampler use Apache 2.0. The commercial-output exception applies only to qualifying users below US$5 million aggregate annualized revenue with the agreement's additional conditions; it is not a blanket grant for commercial weight use. [FLUX Kommunity License v1.0](https://huggingface.co/black-forest-labs/flux-3-image-klein-base/blob/main/LICENSE.md) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein) [FLUX 3 Image Klein Prompt Upsampler card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup).

Generator-file size is not total runtime memory. BFL's published peak-memory results exclude or separately account for prompt upsampling and depend on precision, resolution and hardware; NVFP4 specifically requires a compatible runtime and GPU. [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein distilled model card](https://huggingface.co/black-forest-labs/flux-3-image-klein) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein).

Bounding boxes guide placement and scale, not hard pixel masks; edits may affect surrounding areas and text can be inaccurate. The current reference CLI leaves safety checks off unless enabled, so verify active output review or filtering rather than assuming every loader enables it. [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein distilled model card](https://huggingface.co/black-forest-labs/flux-3-image-klein) [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX 3](../../../../README.md) | `model-series` |
| `has-derivative` | [FLUX 3 Image Klein](../flux-3-image-klein/README.md) | `model` |

## Sources

- [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein)
- [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base)
- [FLUX 3 Image Klein reference code](https://github.com/black-forest-labs/flux-3-image-klein)
- [FLUX 3 Image Klein distilled model card](https://huggingface.co/black-forest-labs/flux-3-image-klein)
- [FLUX 3 Image Klein Prompt Upsampler card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup)
- [FLUX Kommunity License v1.0](https://huggingface.co/black-forest-labs/flux-3-image-klein-base/blob/main/LICENSE.md)
