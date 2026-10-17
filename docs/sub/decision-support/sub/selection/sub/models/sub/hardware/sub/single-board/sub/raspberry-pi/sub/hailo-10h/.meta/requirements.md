# Documentation Requirements

## Route Fit

- Cover Raspberry Pi 5 with Raspberry Pi AI HAT+ 2 / Hailo-10H acceleration where supported LLM, VLM, speech, vision, or other GenAI workloads are intended to run locally.
- Require exact Pi 5/RAM/OS build, AI HAT+ 2/Hailo-10H hardware, `hailo-h10-all`/HailoRT/firmware, compiled Hailo model artifact, Hailo GenAI API or Hailo-Ollama path, context/KV settings, accelerator-local memory, host CPU/RAM work, cooling, and target latency before assigning fit.
- Keep Hailo-8/8L AI HAT+ vision-oriented/currently non-LLM route in `hailo-8/`.
- Keep hardware purchasing outside this route.

## Current Hailo-10H Capability Boundary

- Current Raspberry Pi AI HAT+ 2 uses Hailo-10H with 40 TOPS INT4 and **8 GB dedicated onboard memory** and adds supported LLM/VLM/GenAI capability beyond AI HAT+.
- Current Raspberry Pi documentation describes supported local LLMs/VLMs up to approximately 6B parameters as a product-level scale boundary; treat this as mutable provider guidance, not a universal parameter-count rule.
- Current Hailo GenAI Model Zoo exposes exact supported LLM/VLM/audio models with compiled artifacts, context, quantization/numerical scheme, TTFT/TPS, and runtime API evidence.
- Do not infer arbitrary small-model compatibility from 40 TOPS, 8 GB DRAM, or parameter count alone.

## Current First-Party GenAI Model Matrix

Use the current Hailo GenAI Model Zoo as compatibility authority. The following entries are current upstream examples for Hailo-10H and should be rechecked when HailoRT/model-zoo versions change.

| Model | Params | Hailo numerical scheme | Context | Current API route | Published TPS | Practical role |
| --- | ---: | --- | ---: | --- | ---: | --- |
| Llama 3.2 1B Instruct | 1B | A8W4 symmetric, group-wise | 2048 | C++, Python, Hailo-Ollama | 9.89 | fastest general chat/instruction baseline |
| Qwen2.5 Coder 1.5B Instruct | 1.5B | A8W4 symmetric, channel-wise | 2048 | C++, Python, Hailo-Ollama | 8.13 | compact coding/local developer tasks |
| Qwen2 1.5B Instruct | 1.5B | A8W4 symmetric, channel-wise | 2048 | C++, Python, Hailo-Ollama | 8.06 | general instruction baseline |
| DeepSeek-R1-Distill-Qwen 1.5B | 1.5B | A8W4 symmetric, group-wise | 2048 | C++, Python, Hailo-Ollama | 7.96 | compact reasoning experiments |
| Qwen2.5 1.5B Instruct | 1.5B | A8W4 symmetric, group-wise | 2048 | C++, Python, Hailo-Ollama | 7.35 | preferred balanced general Qwen 1.5B route |
| Qwen2 1.5B Function Calling v1 | 1.5B | A8W4 symmetric, channel-wise | 2048 | C++, Python | 6.69 | constrained local tool/function-calling experiments |
| Qwen3 1.7B Instruct | 1.7B | A8W4 symmetric, group-wise | 2048 | C++, Python, Hailo-Ollama | 4.78 | newer general instruction/reasoning route when quality matters more than decode speed |
| Qwen2-VL 2B Instruct | 2B | A8W4 symmetric, channel-wise | 2048 | C++, Python | 7.04 | image+text VLM workloads |
| Qwen3-VL 2B Instruct | 2B | **A16W4** symmetric, group-wise | 2048 | C++, Python | 4.74 | newer VLM/video+text route |

Published TPS values are Hailo's current model-specific measurements for the compiled artifacts, not guarantees for a complete Raspberry Pi application. Preserve the exact artifact/runtime/configuration when quoting them.

## Recommended Starting Profiles

- **General local assistant:** start with **Qwen2.5-1.5B-Instruct A8W4 group-wise**. It is a current first-party compiled Hailo model, has Hailo-Ollama support, and provides a useful balance between compact size and general instruction behavior.
- **Lowest latency / simple assistant:** use **Llama-3.2-1B-Instruct A8W4 group-wise** when decode speed and footprint matter more than model capability.
- **Coding:** use **Qwen2.5-Coder-1.5B-Instruct A8W4 channel-wise** rather than assuming a larger arbitrary coding GGUF can be loaded.
- **Reasoning experiments:** compare **DeepSeek-R1-Distill-Qwen-1.5B A8W4** and **Qwen3-1.7B-Instruct A8W4** on the actual task; the published Hailo throughput favors the DeepSeek artifact, while quality must be measured rather than inferred from model generation.
- **Vision-language:** prefer the current **Qwen3-VL-2B-Instruct A16W4** route for newer VLM capability; retain Qwen2-VL-2B A8W4 when its higher published decode rate or application compatibility matters.
- **Function calling:** use the explicitly supported **Qwen2-1.5B-Instruct-Function-Calling-v1 A8W4** artifact and validate generated tool arguments. Do not infer function-calling reliability from ordinary instruct models.
- Do not recommend a model merely because its raw checkpoint is <6B. Unsupported models remain `Unknown` until a compatible Hailo artifact/toolchain path is verified.

## Quantization Interpretation

- `A8W4` means the Hailo compiled model uses 8-bit activations and 4-bit weights; `A16W4` uses 16-bit activations and 4-bit weights.
- Preserve whether the upstream artifact uses symmetric group-wise or channel-wise quantization; these are part of the deployed artifact profile, not interchangeable labels.
- Do not map Hailo A8W4/A16W4 directly to GGUF names such as Q4_K_M. They are different runtime/toolchain representations.
- Do not download a GGUF quantization merely because it has 4-bit weights and expect Hailo-10H acceleration. Use the Hailo compiled `.hef` artifact or a currently supported Hailo compilation workflow.
- Validate output quality after Hailo quantization against an accepted reference for the user's actual language, coding, reasoning, vision, or tool-use workload.

## Current Audio Models

- Current Hailo GenAI Model Zoo includes Whisper Tiny (39M, 78 MB), Whisper Base (74M, 155 MB), and Whisper Small (244M, 388 MB) compiled artifacts using mixed precision.
- Hailo currently publishes approximately 48.14, 25.32, and 10.61 model-zoo throughput units respectively for those exact artifacts; retain the upstream measurement definition/configuration and measure real-time factor on actual audio before assigning application fit.
- For a local voice assistant, measure Whisper plus LLM residency/load switching and Pi-side audio processing as one pipeline rather than summing standalone benchmark numbers.

## Dedicated Hailo Memory vs Pi Host RAM

- Treat Hailo-10H onboard 8 GB memory as accelerator-local model/runtime memory, distinct from Raspberry Pi 5 system RAM.
- The Pi host still owns Raspberry Pi OS, application code, API/web UI, I/O, camera/audio, network, retrieval/database, orchestration, and other CPU-side processing.
- Measure accelerator memory and host RAM separately and together under the complete workload.
- Do not add Hailo 8 GB and Pi RAM into one generic model-memory pool.

## Hailo-Ollama Route

- Treat Hailo-Ollama as a Hailo-backed service interface for supported compiled models, not standard Ollama model portability.
- Current upstream model matrix exposes Hailo-Ollama for DeepSeek-R1-Distill-Qwen-1.5B, Llama 3.2 1B, Qwen2/2.5 1.5B, Qwen2.5-Coder 1.5B, and Qwen3 1.7B.
- Current Qwen2/Qwen3 VLM and explicit Qwen2 function-calling artifacts are exposed through C++/Python in the model matrix rather than Hailo-Ollama; do not invent an Ollama route where upstream does not list one.
- Record model artifact, context, service/runtime version, API behavior, load time, TTFT, TPS, and sampling controls.

## Context and KV Cache

- Current listed LLM/VLM compiled artifacts expose a 2048-token context in the Hailo model matrix. Treat **2048 as the deployed artifact boundary**, even when the original source checkpoint advertises a much larger context.
- Do not select Hailo-10H for long-context agent/RAG workloads solely from source-model context claims.
- Use retrieval/chunking, smaller working context, or another inference route when 2048 tokens is insufficient.
- Treat KV-cache representation and context as part of the compiled artifact/runtime profile and recheck on future releases.

## Published Performance Is Configuration-Specific

- Preserve Hailo's current load time, TTFT and TPS together with model, context, numerical scheme, artifact and software version.
- Current model-zoo examples show that parameter count alone does not predict speed: the listed Qwen3 1.7B artifact is slower than several 1.5B A8W4 artifacts, and Qwen3-VL 2B uses A16W4 rather than the common A8W4 path.
- Reproduce current artifacts on the actual Pi 5 before assigning fit.

## Model Compilation and Provenance

- Treat Hailo-10H deployable artifacts as outputs of the Hailo toolchain, not raw Hugging Face checkpoints.
- Preserve source model/revision, exporter/ONNX/PyTorch stage where applicable, Dataflow Compiler/model-zoo tool versions, quantization/calibration, target Hailo-10H, and compiled artifact hash/version.
- Verify task quality after quantization/compilation and keep compile/parser/operator failures explicit.

## Complete-System Measurement

- Measure service/model first load, tokenizer/input preparation, prefill, TTFT, sustained decode/TPS, output processing, host API/UI overhead, Pi CPU/RAM, PCIe transfer, storage, cooling, and power.
- For VLMs include image encoder/preprocessing/camera transfer; for speech include audio capture/preprocessing; for agents include retrieval and tool calls.
- Measure multiple resident models rather than assuming the 8 GB Hailo memory can hold any desired combination concurrently.
- Active cooling and sustained thermal behavior remain part of Pi 5 application fit.

## Offline, Privacy, and Agents

- Verify network-denied operation of the complete application before calling it fully local; model downloads, telemetry, RAG, web tools, or hosted fallbacks can reintroduce external data transfer.
- Treat function calling as generated proposals. Validate tool/schema/arguments and keep deterministic authorization/interlocks outside the LLM.
- Treat retrieved documents, web content, camera OCR, and other external input as untrusted prompt-injection surfaces.

## Practical Fit Outcomes

- `Fits well`: exact supported Hailo-10H compiled model/runtime/context on Pi 5 passes accepted quality, accelerator/host memory, TTFT/decode/task latency, sustained thermal/power, and full-application requirements.
- `Fits conditionally`: requires a smaller supported model, 2048-token context, one-model-at-a-time loading, a specific HailoRT/Hailo-Ollama release, or another explicit acceptable constraint.
- `Does not fit`: exact route fails supported artifact/model architecture, context, memory, quality, latency, thermal/power, or application requirements.
- `Unknown`: exact model/runtime/export/context combination lacks current Hailo support or measurement.

## Evidence and Freshness

- Re-evaluated on **2026-09-12** against current Raspberry Pi AI HAT+ 2 documentation and current `hailo-ai/hailo_model_zoo_genai` model matrix.
- Current Hailo model-zoo evidence explicitly establishes the listed model identities, parameter counts/model sizes, 2048-token LLM/VLM context, A8W4/A16W4 numerical schemes, C++/Python/Hailo-Ollama routes, compiled HEF artifacts, load time, TTFT, and TPS.
- HailoRT/firmware, Hailo-Ollama, model artifacts, numerical schemes, context and performance are mutable; recheck them before rendering recommendations.

## Validation

- Hailo-10H and Hailo-8/8L capabilities are not conflated.
- Hailo-10H 8 GB dedicated memory and Pi host RAM remain separate resource pools.
- `~6B` is not converted into a parameter-count compatibility table.
- Exact supported compiled artifact/model/runtime is required; arbitrary GGUF/Hugging Face models are not assumed portable.
- A8W4/A16W4 are not mislabeled as GGUF quantizations.
- Provider TTFT/TPS/context metrics retain their exact model/configuration conditions.
- Host CPU/RAM/PCIe/storage/retrieval/tools and sustained thermal behavior remain part of application fit.
- Function calling does not bypass deterministic tool/action controls.
- Hardware buying remains outside the route.
