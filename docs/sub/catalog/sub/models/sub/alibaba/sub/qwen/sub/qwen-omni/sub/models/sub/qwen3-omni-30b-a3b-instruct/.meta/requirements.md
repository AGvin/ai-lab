# Documentation Requirements

## Identity and provenance

- Materialize exactly one original `Qwen/Qwen3-Omni-30B-A3B-Instruct` checkpoint released on 2025-09-22 under the existing Qwen Omni series. It includes Thinker and Talker with text, image, audio and video inputs and text/speech outputs. Thinking and Captioner are separately published identities outside this bounded node; text-only output or disabling Talker is a runtime option. [Official release](https://github.com/QwenLM/Qwen3-Omni) [Exact card](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct).
- The raw Hub card uses `license: other` with `license_name: apache-2.0`; the rendered card displays Apache-2.0. The technical report explicitly releases the weights under Apache-2.0 and the official GitHub LICENSE contains its text. No standalone LICENSE was listed in the exact Hub root, so do not claim to have read one there. Hosted service terms remain separate. [Report](https://arxiv.org/html/2509.17765v1) [License text](https://github.com/QwenLM/Qwen3-Omni/blob/main/LICENSE) [Raw card](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/blob/main/README.md?code=true).

## Operational decision boundaries

- The technical report scopes **30B total / 3B active parameters to Thinker**, with a separate **3B / 0.3B Talker** plus other media components. The whole checkpoint is larger than the Thinker; active counts do not establish weight storage or VRAM fit. [Architecture report](https://arxiv.org/html/2509.17765v1).
- The published configuration has **65,536 maximum text positions** in Thinker and Talker, while other components have different budgets. This is not a guaranteed universal media duration, output length or validated long-context quality. Recheck exact processor, runtime revision, text/audio output settings, media sizes and serving limits; do not inherit mutable hosted API contracts. [Exact config](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/blob/main/config.json) [Card examples](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct).
- Cloudflare explicitly post-trains Clef-omni from this checkpoint's Thinker with vision/audio encoders. Keep the exact reciprocal derivative edge; included unchanged Talker/code2wav weights are unused by Clef's decision loader, whose option probabilities do not imply speech or free-form output. [Cloudflare card](https://huggingface.co/Cloudflare/clef-omni).
- Qwen/Alibaba provenance is inherited through the existing series. No new producer, exact unpublished pretraining parent, complete beneficial-ownership result, current indirect Russian share/control claim or sanctions tier is established here.
- Evaluate multimodal grounding, transcription, speech, synchronization, privacy and permitted media use for the workload. Publisher quality/latency/language results are not independent benchmarks or evidence that generated audio is authentic. No automatic recommendation, hardware-fit or hosted-access guarantee.

## Validation

- Resolve the exact series membership and Clef-omni derivative pairs in both directions; preserve existing identities and never recount the existing series or derivative as newly accepted.
- Render a complete English reader with the model/artifact, component-parameter, license-evidence and runtime boundaries intact.
- This is source/documentation assessment, not endpoint execution, downloaded-weight testing, full schema/cache/CI, clean-pass, final-render or publication-gate credit.
