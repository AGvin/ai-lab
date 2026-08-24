# Documentation Requirements

## Route Fit

- Cover Raspberry Pi 5 with Raspberry Pi AI HAT+ 2 / Hailo-10H acceleration where supported LLM, VLM, speech, vision, or other GenAI workloads are intended to run locally.
- Require exact Pi 5/RAM/OS build, AI HAT+ 2/Hailo-10H hardware, `hailo-h10-all`/HailoRT/firmware, compiled Hailo model artifact, Hailo GenAI API or Hailo-Ollama path, context/KV settings, accelerator-local memory, host CPU/RAM work, cooling, and target latency before assigning fit.
- Keep Hailo-8/8L AI HAT+ vision-only/currently non-LLM route in `hailo-8/`.
- Keep hardware purchasing outside this route.

## Current Hailo-10H Capability Boundary

- Current Raspberry Pi AI HAT+ 2 uses Hailo-10H with 40 TOPS INT4 and **8 GB dedicated onboard memory** and adds supported LLM/VLM/GenAI capability beyond AI HAT+.
- Current Raspberry Pi documentation describes supported local LLMs/VLMs up to approximately 6B parameters as a product-level scale boundary; treat this as mutable provider guidance, not a universal parameter-count rule.
- Current Hailo Model Explorer exposes exact supported LLM/VLM/audio models with compiled artifacts, context, quantization, TTFT/TPS, and runtime API evidence.
- Do not infer arbitrary small-model compatibility from 40 TOPS, 8 GB DRAM, or parameter count alone.
- Keep unsupported architecture/operator/tokenizer/export combinations `Unknown` until current Hailo artifacts/toolchain evidence exists.

## Dedicated Hailo Memory vs Pi Host RAM

- Treat Hailo-10H onboard 8 GB memory as accelerator-local model/runtime memory, distinct from Raspberry Pi 5 system RAM.
- The Pi host still owns Raspberry Pi OS, application code, API/web UI, I/O, camera/audio, network, retrieval/database, orchestration, and other CPU-side processing.
- Measure accelerator memory and host RAM separately and together under the complete workload.
- Do not add Hailo 8 GB and Pi RAM into one generic model-memory pool.
- A model fitting Hailo memory can still fail because host RAM/CPU or PCIe/application work is insufficient.

## Current Raspberry Pi OS and Package Boundary

- Current Raspberry Pi AI documentation requires Raspberry Pi 5 with current 64-bit Raspberry Pi OS Trixie for the supported Hailo AI HAT setup.
- AI HAT+ 2 uses the `hailo-h10-all` package family, distinct from Hailo-8/8L `hailo-all`.
- Current Raspberry Pi documentation states the Hailo-8/8L and Hailo-10 package sets cannot coexist.
- Pin package/runtime/firmware versions and re-evaluate after updates.
- Do not transfer Hailo-8 HailoRT/toolchain assumptions or old Bookworm setup into current Hailo-10H deployment.

## Hailo GenAI API and HailoRT

- Treat HailoRT GenAI APIs as the current first-party runtime interface for supported Hailo-10H generative artifacts.
- Current Hailo-10H product documentation exposes GenAI APIs alongside vision APIs and supports C/C++/Python/REST-style integrations through the current software stack.
- Preserve exact HailoRT/firmware/model artifact/API versions because sampling, context, runtime behavior, and compatibility evolve.
- Do not assume a generic HailoRT vision inference API exposes the same semantics as LLM/VLM GenAI APIs.
- Measure host API overhead and service integration in end-to-end latency.

## Hailo-Ollama Route

- Current Raspberry Pi documentation provides a `hailo-ollama` server route for local LLM access on AI HAT+ 2, including API and web UI use.
- Treat Hailo-Ollama as a Hailo-backed service interface for supported compiled models, not standard Ollama model portability.
- Do not assume an arbitrary Ollama/GGUF model can be copied into Hailo-Ollama.
- Record supported Hailo model package, context, service version, API behavior, load time, TTFT, TPS, and sampling controls.
- Test compatibility with the actual client because current HailoRT/Hailo-Ollama sampling parameter behavior can differ by release.

## Current Model Explorer as Compatibility Evidence

- Use Hailo's current GenAI Model Explorer as the primary candidate list for supported Hailo-10H LLM/VLM/audio artifacts.
- Current examples include Qwen3 1.7B, Qwen3-VL 2B, Qwen2/2.5 1.5B, Qwen2.5-Coder 1.5B, Llama 3.2 1B, DeepSeek-R1-Distill-Qwen 1.5B, Qwen2-VL 2B, and Whisper variants.
- Treat this list as mutable provider compatibility evidence, not a permanent AI Lab ranking.
- Record exact model identity, artifact, numerical scheme, context, API, and published performance when used.
- Do not infer that a larger sibling or different architecture will compile/run because a similarly named small model is listed.

## Published Hailo Metrics Are Configuration-Specific

- Hailo's Model Explorer and technical material publish model-specific TTFT, TPS, context, memory, quantization, and power under stated configurations.
- Preserve all conditions instead of extracting a single TPS number.
- Current Qwen3 1.7B Model Explorer example reports a 2048-token context, A8W4 numerical scheme, first-load time, TTFT, and TPS; these values belong to that exact compiled model/device configuration.
- Older Hailo technical material for Qwen2 1.5B demonstrates how TTFT/TPS/KV-cache/memory/quantization/power can be characterized, but it is not a universal Hailo-10H result.
- Reproduce current artifacts on the actual Pi 5 before assigning fit.

## Parameter Count Is Not the Fit Rule

- The current Raspberry Pi `~6B` product statement is an approximate supported scale boundary, not a promise that every model below 6B runs.
- Compatibility depends on architecture, operators, tokenizer, graph decomposition, weight/activation/KV quantization, context, compiled artifact, runtime, and memory.
- A supported 2B VLM can have different memory/latency from a 2B text LLM.
- A smaller unsupported architecture is still `Unknown`/non-fit.
- Do not generate RAM/parameter lookup tables from the product marketing boundary.

## Model Compilation and Provenance

- Treat Hailo-10H deployable artifacts as outputs of the Hailo toolchain, not raw Hugging Face checkpoints.
- Preserve source model/revision, exporter/ONNX/PyTorch stage, Dataflow Compiler/model-zoo tool versions, quantization/calibration, Hailo GenAI-specific optimization, target Hailo-10H, and compiled artifact hash/version.
- Verify task quality after quantization/compilation.
- Keep compile/parser/operator failures explicit.
- Do not assume Hailo-8 HEFs or vision artifacts are interchangeable with Hailo-10H GenAI artifacts.

## LLM Pipeline Measurement

- Measure complete LLM behavior:
  - service/model first load;
  - tokenizer/input preparation;
  - prefill/prompt processing;
  - TTFT;
  - KV-cache growth;
  - sustained token decode/TPS/TPOT;
  - sampling/output processing;
  - host API/UI overhead.
- Record input/context/output lengths.
- Do not use 96-token prefill or 2048-context provider examples as proof of long-document/agent context.
- If the supported compiled artifact exposes a fixed/smaller context than the source model, the deployed context is the hardware-route limit.

## KV Cache and Context

- Treat KV-cache format/quantization and context as part of the compiled Hailo model/runtime profile.
- Measure memory/latency as context grows and under multiple sessions.
- Do not assume source model advertised context survives Hailo compilation unchanged.
- Route document-scale context to retrieval/chunking or another model/server when the current Hailo artifact cannot satisfy it.
- Mark context-dependent fit explicitly.

## VLM Route

- Current Hailo-10H supports named VLMs through current compiled artifacts and Hailo apps/Model Explorer.
- Include image encoder, language model, preprocessing, camera/image transfer, context/tokens, and output handling in complete latency.
- Current Raspberry Pi material highlights VLM workloads such as event triggering, captioning, indexing, and semantic search; treat use-case examples as candidate workflows, not guaranteed application performance.
- Measure camera-to-response latency and host CPU load for real-time pipelines.
- Do not infer VLM support from Hailo-8 vision support.

## Speech and Audio Route

- Current Hailo-10H Model Explorer includes Whisper Tiny/Base/Small-class supported audio models.
- Record exact model/artifact/audio duration/sample rate/preprocessing/runtime and real-time factor/latency.
- Combine speech + LLM only after measuring both resident models, host buffers, and sequential/concurrent execution.
- Do not infer speech capability from LLM support alone.

## Vision Workloads

- Hailo-10H also runs Hailo vision workloads and can integrate with Raspberry Pi camera applications.
- Treat vision performance separately from GenAI performance because 40 TOPS INT4/architecture/onboard memory do not map directly to Hailo-8 26-TOPS application behavior.
- Measure end-to-end camera FPS/latency and simultaneous GenAI contention where both run.
- Do not quote Hailo-8/8L model-zoo throughput as Hailo-10H evidence unless the artifact/runtime is explicitly supported and measured.

## Multiple Resident Models

- Measure actual accelerator-local memory, host CMA/driver allocations, host RAM, and latency when LLM/VLM/Whisper/vision models coexist.
- Do not sum standalone memory estimates and assume scheduling/concurrency will work.
- Record load/unload time and whether models can remain resident together in the current HailoRT release.
- Use sequential loading when it improves memory/reliability and startup cost is acceptable.
- Keep current community observations as independent evidence only; official/runtime-specific tests on the target release remain authoritative.

## Host CPU and Pi Work Remain Material

- Even when Hailo documentation describes the entire LLM inference pipeline as accelerated, the Pi still handles application orchestration, I/O, retrieval, network, tool calls, UI, storage, camera/audio, and non-Hailo components.
- Measure Pi CPU utilization/RAM under the real application.
- A low NPU inference latency can still yield a slow agent/RAG app because host/database/tool work dominates.
- Include CPU thermals and storage/network delays.

## PCIe and Data Transfer

- Record PCIe link/device status and include model input/output/camera/embedding transfers in whole-system latency.
- Do not interpret Hailo-10H accelerator-internal throughput as host application throughput.
- For high-rate camera/VLM or multi-model pipelines, monitor PCIe/host bottlenecks.
- Verify runtime/driver errors separately from model quality.

## Cooling and Power

- Current AI HAT+ 2 has its own heatsink requirement and Raspberry Pi recommends active cooling on the Pi 5 alongside the HAT heatsink.
- Measure sustained Pi/Hailo thermal behavior and full-system power under repeated GenAI use.
- Hailo technical power figures for one model are not the complete Pi+HAT application power.
- A route that is only stable/fast for short bursts is conditional fit for always-on assistants.

## Storage and Model Delivery

- Include compiled Hailo model packages, Hailo-Ollama models, runtime packages, web UI, retrieval indexes, multiple model variants, logs, and update headroom.
- Prestage models for offline use and define version/hash/rollback.
- Do not rely on model-hub downloads at request time when offline operation is claimed.
- Keep source model license and Hailo artifact distribution rights explicit.

## Offline and Privacy Boundary

- Hailo-10H is explicitly intended for fully local edge GenAI without cloud inference once the required models/software are installed.
- Test network-denied operation of the complete application, not only NPU inference.
- Retrieval, web UI, agents, model downloads, telemetry, and other services can reintroduce network dependencies.
- Do not describe an application as fully local if its tools/RAG/hosted fallback send user data externally.

## Function Calling and Agents

- Current Hailo model catalog includes function-calling-capable compact LLM artifacts.
- Treat function calling as generated tool proposals; validate tool name/schema/arguments and apply explicit permissions/confirmation.
- Hailo local execution does not authorize GPIO, shell, home automation, robotics, network, or account actions.
- Treat retrieved documents/web/camera OCR as untrusted prompt-injection content.
- Keep deterministic safety/interlock logic outside the LLM.

## Quality After Quantization

- Hailo-10H GenAI uses aggressive edge-oriented weight/activation/KV quantization in supported artifacts.
- Compare the compiled model against the source/full-precision or accepted reference on the user's tasks.
- Use provider quality metrics only as candidate evidence and validate domain-specific accuracy/refusal/tool behavior independently.
- Track retries/human correction cost with TPS/TTFT.
- A model that is fast but materially degrades reasoning/coding/language quality does not fit.

## Cost per Accepted Edge Result

- Include Pi/HAT power, model/toolchain setup, storage, runtime maintenance, retrieval/tool host work, retries, and human correction.
- Compare against Pi CPU and hosted alternatives.
- Local Hailo-10H can be attractive for privacy/offline/low recurring cloud cost, but its current compact-model capability may not match stronger hosted models.
- Do not treat zero per-token API charge as zero cost.

## Practical Fit Outcomes

- `Fits well`: exact supported Hailo-10H compiled model/runtime/context on Pi 5 passes accepted quality, accelerator/host memory, TTFT/decode/task latency, sustained thermal/power, and full-application requirements.
- `Fits conditionally`: requires a current supported compact model, smaller context, one-model-at-a-time loading, specific HailoRT/Hailo-Ollama release, reduced multimodal pipeline, or another explicit acceptable constraint.
- `Does not fit`: exact route fails supported artifact/model architecture, context, memory, quality, latency, thermal/power, or application requirements.
- `Unknown`: exact model/runtime/export/context combination lacks current Hailo support or measurement.
- Do not assign fit from 40 TOPS, 8 GB accelerator RAM, or parameter count alone.

## Escalation

- Route unsupported/larger/higher-quality generative workloads to Pi CPU, another fixed local platform, or hosted/hybrid execution.
- Route Hailo-8/8L supported vision-only workloads to `hailo-8/` when that is the existing accelerator.
- Do not recommend purchasing AI HAT+ 2 from this page; expose capability gaps only.

## Canonical Links

- Link exact model facts to Model Reference and HailoRT/Model Explorer/Dataflow Compiler/Hailo-Ollama/hailo-apps to canonical software owners when materialized.
- Link Raspberry Pi parent/router and `hailo-8/` sibling for capability separation.
- Link local assistant/VLM/home-automation/physical-AI scenarios when workflow requirements dominate hardware fit.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Raspberry Pi AI HAT+ 2/AI software documentation, current Hailo-10H product/software documentation, current Hailo GenAI Model Explorer, and current Hailo LLM technical material.
- Current evidence establishes 8 GB dedicated Hailo-10H memory, official LLM/VLM/audio/vision GenAI routes, current compiled model catalog, HailoRT GenAI APIs/Hailo-Ollama integration, and model-specific TTFT/TPS/context/quantization evidence. Raspberry Pi's approximate `~6B` scale statement remains product guidance, not a universal compatibility rule.
- HailoRT/firmware, Hailo-Ollama/GenAI APIs, Model Explorer models/artifacts, Dataflow Compiler, context/quantization, Raspberry Pi packages, and performance are mutable; recheck them before rendering recommendations.
- Exact compiled model/runtime/context/full Pi application measurement and accepted-result quality remain the fit authority.

## Validation

- Hailo-10H and Hailo-8/8L capabilities are not conflated.
- Hailo-10H 8 GB dedicated memory and Pi host RAM remain separate resource pools.
- `~6B` is not converted into a parameter-count compatibility table.
- Exact supported compiled artifact/model/runtime is required; arbitrary Hugging Face/Ollama models are not assumed portable.
- Provider TTFT/TPS/context/power metrics retain their model/configuration conditions.
- Host CPU/RAM/PCIe/storage/retrieval/tools and sustained Pi/HAT thermal behavior remain part of application fit.
- LLM/VLM/speech/vision routes are evaluated as complete pipelines.
- Function calling does not bypass deterministic tool/action controls.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
