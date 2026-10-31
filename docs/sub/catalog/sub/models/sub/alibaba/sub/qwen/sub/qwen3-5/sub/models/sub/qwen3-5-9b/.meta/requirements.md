# Documentation Requirements

## Requirements

- Preserve the exact current-node identity, sourced training-stage boundary and canonical owner.
- Render every visible entity relation with resolving canonical links and preserve ordering.
- Separate model identity from precision packages, modes, hosted routes and runtime behavior.
- Treat publisher benchmarks as publisher evidence, not independent AI Lab measurements.

## Architecture and modalities

The [exact configuration](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/config.json) identifies Qwen3_5ForConditionalGeneration / qwen3_5, a 32-layer language stack, hidden size 4096 and FFN intermediate size 12288, with groups of three linear-attention layers followed by one full-attention layer and a separate vision encoder. This is the dense 9B member; a generic series sparse-MoE highlight does not establish MoE experts for this configuration. The model supports text/image/video input and text output. The 9B label describes language-model scale; it is not an active-parameter MoE or a peak-memory estimate.

## Training and operating boundary

The [official card and metadata](https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/README.md) distinguish post-training from the separately released pretrained Base. Thinking/non-thinking settings are modes of this checkpoint. Qwen3-VL-4B-Instruct is another architecture and component, not this model or the Prompt Upsampler's parent. Use the matching processor/chat template and pin the exact weight/runtime revision; native or extended context claims do not prove feasible memory or all-runtime support.

## License and limitations

Weights use Apache-2.0. Benchmark/capability statements on the [publisher card](https://huggingface.co/Qwen/Qwen3.5-9B) are publisher evidence, not reproduced AI Lab measurements. A downloadable checkpoint does not define hosted API privacy, lifecycle or retention. Model-generated commands/tool arguments do not authorize execution; the application owns tool permissions, validation and isolation. No inference or independent beneficial-owner audit was performed.

## Validation

- Keep source-attributed limitations, licenses and model lineage explicit in the complete reader.
- Do not infer tool-execution permission, hardware fit or source freshness from a model name.
- Do not advance a freshness marker without a complete mutable-fact audit.
