# Qwen3-Omni 30B-A3B Instruct

The released `Qwen/Qwen3-Omni-30B-A3B-Instruct` checkpoint combines Thinker and Talker to process **text, images, audio and video**, and produce **text and speech**. Qwen dates its public release to **22 September 2025**. Thinking and Captioner are distinct checkpoints; disabling Talker is a runtime option. [Official release](https://github.com/QwenLM/Qwen3-Omni) [Model card](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct).

## Parameters and context

The technical report scopes **30B total / 3B active parameters to Thinker**, with a separate **3B / 0.3B Talker** plus other media components. The whole checkpoint is larger than the Thinker; active counts do not establish weight storage or VRAM fit. [Technical report](https://arxiv.org/html/2509.17765v1).

The published configuration has **65,536 maximum text positions** in Thinker and Talker, while other components have different budgets. This is not a guaranteed universal media duration, output length or validated long-context quality. Recheck exact processor, runtime revision, text/audio output settings, media sizes and serving limits; do not inherit mutable hosted API contracts. [Exact config](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/blob/main/config.json) [Usage examples](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct).

## License and operating boundaries

The raw Hub card uses `license: other` with `license_name: apache-2.0`; the rendered card displays Apache-2.0. The technical report explicitly releases the weights under Apache-2.0 and the official GitHub LICENSE contains its text. No standalone LICENSE was listed in the exact Hub root, so do not claim to have read one there. Hosted service terms remain separate. [Release report](https://arxiv.org/html/2509.17765v1) [Apache-2.0 text](https://github.com/QwenLM/Qwen3-Omni/blob/main/LICENSE) [Raw card](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/blob/main/README.md?code=true).

Evaluate multimodal grounding, transcription and synthesis, temporal alignment, memory, latency and authorized media use on representative inputs. Qwen's reported capability and performance results are publisher evidence. They do not establish an independent benchmark, a current recommendation, hosted account availability or authenticity of generated speech.

Qwen/Alibaba provenance follows the existing series. This review establishes no exact unpublished pretraining parent or complete beneficial-ownership finding.

## Derived decision model

Cloudflare identifies Clef-omni as post-trained from this checkpoint's **Thinker with vision/audio encoders**. The release includes unchanged Talker/code2wav weights but its decision loader does not use them. Clef-omni scores allowed options; it does not inherit this upstream interface's free-form speech/text generation contract. [Cloudflare source](https://huggingface.co/Cloudflare/clef-omni).

## Catalog relations

- [Clef-omni](../../../../../../../../../cloudflare/sub/clef/sub/models/sub/clef-omni/) — derivative.
- [Qwen Omni](../../../../) — series.

## Official resources

- [Exact model card](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct).
- [Official release repository](https://github.com/QwenLM/Qwen3-Omni).
- [Technical report](https://arxiv.org/html/2509.17765v1).
- [License text](https://github.com/QwenLM/Qwen3-Omni/blob/main/LICENSE).
