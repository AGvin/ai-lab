# H3 Max by fal

**H3 Max** is a video-generation model separately **post-trained by fal Research** from the [MiniMax H3 model family](../../../minimax/sub/h3/README.md). fal announced the learned derivative on **27 August 2026**, alongside optimizations to its inference stack. The branded `minimax/h3-max` API namespace records the upstream lineage; it does not make the original MiniMax H3 model and fal's post-trained model the same learned checkpoint.

## Relations

- Produced by: [fal (Features & Labels, Inc.)](../../../../../producers/sub/f/sub/features-and-labels-inc/README.md)
- Upstream lineage: [MiniMax H3](../../../minimax/sub/h3/README.md) — family/system with multiple base components, not one concrete checkpoint.

## Access and workflows

fal exposes H3 Max through **text-to-video** and **image-to-video** hosted endpoints. A route, image input or optional end-frame control does not by itself establish a separate trained model. Publisher-reported prompt-adherence, video-quality and throughput gains are not independent AI Lab measurements. Model hosting and serving modes may change; verify the current endpoint schema and limits for the chosen route.

## Rights and security boundary

H3 Max's hosted access is subject to [fal's terms](https://fal.ai/legal/terms-of-service), including input, output and third-party material restrictions. The upstream [MiniMax H3 weights and license](https://huggingface.co/MiniMaxAI/MiniMax-H3) have separate custom distribution and geographic/commercial conditions. The available official evidence does **not** establish downloadable H3 Max weights or grant permission to redistribute them under the upstream license. Check commercial rights, source-media consent, data processing, retention and model-specific terms before use. Protect API keys and avoid embedding them in client code.

H3 Max Turbo pricing/performance labels are not treated as proof of a separate published trained checkpoint. Release date, publisher quality comparisons and access are source-specific, not a full freshness, legal, security or runtime certification.

## Navigation

- [fal model publishing view](../../README.md)

## Official sources

- [Original fal announcement (27 August 2026)](https://blog.fal.ai/introducing-h3-max-by-fal/)
- [H3 Max text-to-video API](https://fal.ai/models/minimax/h3-max/text-to-video/api)
- [H3 Max image-to-video API](https://fal.ai/models/minimax/h3-max/image-to-video/api)
- [fal H3 Max overview](https://fal.ai/minimax-h3-max)
- [fal terms](https://fal.ai/legal/terms-of-service)
- [Upstream MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
