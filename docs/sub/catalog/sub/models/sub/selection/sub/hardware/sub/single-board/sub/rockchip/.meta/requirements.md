# Documentation Requirements

## Requirements

- Cover Rockchip NPU SBC routes where RKNN/RKLLM is the intended accelerator path, independent of board OEM.
- Identify exact SoC/platform series, RKNN/RKLLM toolkit/runtime version, host conversion environment, model architecture/export/quantization, device RAM, and supported operators before selection.
- Preserve current upstream RKNN-LLM platform coverage (including documented RK3588/RK3576/RK3562/RV1126B-class support) only as a mutable compatibility boundary; recheck upstream before current claims.
- Use upstream supported LLM/VLM family examples as compatibility evidence, not proof every version/quantization/checkpoint is supported or performant.
- For VLM routes, account for separate vision encoder/RKNN and language RKLLM components when the upstream design requires them.
- Do not split Radxa/Orange Pi/other board brands when they share the same SoC/runtime route unless board-specific constraints materially change model selection.
- Measure conversion success, device memory, prompt/decode/task latency, sustained thermals, and accepted-result quality.

## Validation

- Exact SoC/toolkit/runtime is pinned.
- Source weights are not equated with deployable RKLLM artifacts.
- Board branding does not duplicate one Rockchip model-selection route.
