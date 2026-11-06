# Documentation Requirements

## Identity and provenance

- North Mini Code 1.0 Eagle draft is a separately released learned speculative-decoding component under CohereLabs/North-Mini-Code-1.0-eagle. The published repository contains distinct model weights, not an FP8/W4A16 quantization of the 30B North Mini Code target or a standalone 30B coding checkpoint. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle) [Repository README](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle/blob/main/README.md).
- Public Hugging Face metadata reports approximately **79.2 million parameters** in BF16; its short official card describes **three dense transformer draft layers with sliding-window attention** and Apache-2.0 license metadata. This is a model-card/registry report, not a locally downloaded or tensor-counted model. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- The artifact is published under CohereLabs and named for a compatible North Mini Code target. Publication/compatibility alone does not prove training directly from target weights, exact development personnel, or an independent second producer; add only the North model-family inverse membership, no speculative `derived-from` or non-exclusive co-developer edge. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle) [Target model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).

## Operational decision boundaries

- This auxiliary draft predicts speculative continuation candidates which the target model must verify; the draft alone is not equivalent to the full North Mini Code 1.0 code generator or a replacement for its chat/agent/tool contracts. Correctness, acceptance rate and speedup depend on the serving runtime and target compatibility. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- Official card illustrates vLLM `--speculative_config` with `method=eagle`, the separate Eagle model ID and `num_speculative_tokens=3`, and names compatibility with FP8/W4A16 target checkpoints. It uses `--max-model-len 320000` for the **target serving configuration**, which does not prove a native 320K draft context or independently validated quality; confirm runtime/vLLM version and exact flags before deployment. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle).
- The Eagle card reports Apache-2.0 metadata. Confirm both draft and target licensing, network/asset access, parameter storage, device memory and observed end-to-end latency separately. Do not count target BF16/FP8/W4A16 files, cache formats or another publisher's EAGLE3 adaptation as new variants of this exact learned component. [Eagle draft card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-eagle) [Target model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0).
- No weights were downloaded or executed, no hardware benchmarks were run, no guaranteed speedup was established, and ownership/beneficial Russian-control review remains independent. An authenticated publisher account is not proof of all underlying corporate stakes.

## Validation

- One unique canonical model ID and North family membership reciprocal pair. Keep runtime compatibility in prose; no unsupported training lineage or additional producer relation.
- Full English reader with architecture/license/serving restrictions, linked source URLs and parent/adjacent navigation.
- No full repository schema/cache/CI, independent inference/benchmark, clean catalog research pass or final acceptance gate is credited from this scoped intake.
