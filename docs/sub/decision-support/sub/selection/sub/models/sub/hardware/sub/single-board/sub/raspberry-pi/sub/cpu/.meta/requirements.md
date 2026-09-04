# Documentation Requirements

## Route Fit

- Cover Raspberry Pi local inference where the Arm CPU is the primary model execution target and no Hailo/other accelerator is assumed.
- Require exact Pi generation/model, RAM variant, 64-bit OS/distribution, CPU runtime/backend/build, model artifact/quantization, context/KV cache, storage, cooling, power supply, background services, and target latency before assigning fit.
- Route Pi 5 + Hailo-8/8L or Hailo-10H through the sibling accelerator routes rather than treating accelerator memory/compute as CPU capacity.
- Keep Raspberry Pi/hardware purchasing outside this route.

## Pi Generation Is Part of Fit

- Distinguish Pi 5, Pi 4/CM4, older Pi, and other Arm boards rather than applying one Raspberry Pi benchmark universally.
- Current CPU generative-model evidence is strongest for Raspberry Pi 5; do not transfer it to Pi 4/Zero/older ARM cores without measurement.
- Record CPU architecture/microarchitecture, clock/power state, RAM variant, and board cooling.
- Preserve Pi OS kernel/userspace/runtime versions because ARM kernels and libraries change.

## Current Pi 5 CPU Evidence

- Current Raspberry Pi August 2026 guidance demonstrates CPU-side local Gemma execution on Raspberry Pi 5 using LiteRT-LM/XNNPACK and `llama.cpp`.
- The published comparison is explicitly on **Raspberry Pi 5 8 GB**, four CPU threads, 1024 prefill tokens, and 256 decode tokens.
- Published Gemma 4 E2B results show that runtime/artifact choice materially changes prefill/decode and peak memory; preserve those exact conditions when using the numbers.
- Treat this as current first-party candidate/performance evidence, not a universal recommendation for all Pi 5 RAM variants/models/contexts.
- Reproduce the target model/runtime on the user's actual board before assigning fit.

## Runtime Matters as Much as Model Size

- Compare mature Arm CPU runtimes for the exact model rather than assuming one framework is always best.
- Current Raspberry Pi evidence shows LiteRT-LM/XNNPACK and `llama.cpp` can have materially different memory/performance for the same Gemma family.
- Preserve runtime version/build, CPU feature use, threads, artifact/quantization, and benchmark command.
- Do not compare a LiteRT QAT artifact and GGUF Q4 artifact as if only the runtime differs; export/quantization can change quality and memory too.
- Evaluate accepted-result quality after every conversion/quantization.

## ARM64 Dependency Boundary

- Prefer 64-bit Raspberry Pi OS or another supported 64-bit Linux where the runtime/model requires it.
- Verify ARM64 wheels/native dependencies for tokenizer, runtime, audio/vision preprocessing, vector/database libraries, and agent tools.
- A desktop/x86 Python package or CUDA extension may block the application even when the model runtime works.
- Record any source-build patches/toolchains that become part of deployment.
- Keep unsupported dependency chains `Unknown`.

## RAM Is Only One Constraint

- Do not publish universal `Pi RAM → model parameter size` tiers.
- Include model weights, page cache/mmap, KV/cache, runtime buffers, tokenizer, embeddings/encoders, camera/audio data, OS/services, and application state in peak memory.
- Current Pi 5 exists in multiple RAM variants including 16 GB, but more RAM does not make the four-core CPU proportionally faster.
- A larger model that fits a 16 GB Pi can still be unusable interactively due to memory bandwidth/compute latency.
- Heavy swap is a conditional/non-fit route unless the workload explicitly tolerates it.

## Prompt vs Decode

- Measure prefill/prompt processing separately from decode/generation.
- Current first-party Pi 5 Gemma benchmark explicitly reports both, demonstrating why one tokens/s number is insufficient.
- Record TTFT, prefill tokens/s or time, decode tokens/s or TPOT, input/context length, output length, and end-to-end task time.
- Use realistic user prompts instead of only tiny synthetic inputs.
- A runtime can have fast prefill but mediocre decode or vice versa.

## Context and KV Cache

- Include context/KV-cache growth in RAM and latency evidence.
- Test the context length the user actually needs.
- Record cache precision/quantization if the runtime supports it.
- If practical fit requires sharply reducing context, mark it conditional rather than advertising the base model's maximum context.
- Do not extrapolate a 1024-token benchmark to long-document/agent use without measurement.

## Threads and Core Contention

- Record thread count and affinity/scheduler behavior.
- Current Raspberry Pi first-party Gemma benchmark uses four threads on Pi 5; do not assume more processes/threads improve one-model decode.
- Keep CPU capacity for OS, networking, storage, camera/audio, automation, and application orchestration.
- For background servers, measure foreground responsiveness and p95 latency while normal services run.
- Avoid pinning all resources to inference when the board has another primary control/server duty.

## Cooling and Thermal Throttling

- Treat sustained cooling as a first-class CPU-inference constraint.
- Raspberry Pi documentation states Pi 5 can throttle under long heavy CPU load and recommends active cooling for sustained high performance.
- Current thermal controls progressively reduce CPU frequency near the defined temperature limit; record temperature/throttle state during benchmarks.
- Use a sustained generation/test long enough to reveal thermal steady state.
- A short uncooled result is not evidence for a 24/7 local model server.

## Power Supply and Peripheral Budget

- Use a stable Pi-appropriate power supply and record low-voltage/throttling warnings.
- Pi 5 downstream USB/current availability can vary with power supply capability; account for SSDs/cameras/audio/HATs/peripherals.
- An undervoltage or peripheral-power problem can masquerade as model/runtime instability.
- Do not benchmark accelerator-free CPU fit while ignoring storage/camera load that will exist in deployment.

## Storage and Model Load

- Record SD/USB SSD/NVMe/model path and cold/warm load time when startup matters.
- Memory-mapped artifacts can rely heavily on OS page cache; distinguish cold boot/model load from repeated warm runs.
- Include model disk size, multiple quantizations, caches, logs, and free-space/update headroom.
- Do not use slow microSD swap as normal memory expansion for interactive inference.

## LiteRT-LM Route

- Treat LiteRT-LM/XNNPACK as a current Pi 5 CPU route for supported model artifacts.
- Current Raspberry Pi material demonstrates current Gemma 4 E2B CPU deployment using LiteRT-LM QAT artifact.
- Require the exact supported model/export/LiteRT version and measure its task quality.
- Do not infer arbitrary Hugging Face model compatibility from one Gemma integration.
- Preserve any model-specific orchestration or tokenizer requirements.

## llama.cpp Route

- Treat `llama.cpp` GGUF as another mature ARM CPU route.
- Preserve exact project build/commit, GGUF quantization, thread count, context/cache, mmap options, and model revision.
- Current Raspberry Pi first-party benchmark uses `llama-bench` on Gemma 4 E2B Q4_0 as an explicit comparison point.
- Do not use that one runtime/model result as an expected speed for Qwen/Llama/Mistral/other architectures.

## VideoCore GPU Is Not a Generic LLM Accelerator

- Do not describe Pi 5 VideoCore VII as generic CUDA-like capacity.
- Current Raspberry Pi guidance demonstrates a newer LiteRT WebGPU/Vulkan route for supported vision/audio/embedding models, but this is model/backend specific.
- If GPU acceleration is intended for one stage, record the exact LiteRT/WebGPU/Vulkan model and route it as a measured heterogeneous pipeline rather than pure CPU inference.
- Do not infer arbitrary LLM offload from vision/audio WebGPU examples.

## Camera, Audio, and Other Host Work

- Include camera capture/ISP/rpicam/Picamera2, image resize/color conversion, audio capture/resampling, network, databases, and storage in whole-system measurements.
- A model that consumes all CPU/RAM can starve camera or automation deadlines.
- For local vision + LLM pipelines, measure both simultaneous stages rather than standalone inference.
- Hailo acceleration can free CPU for orchestration, but use the Hailo route for those deployments.

## Server and Concurrency Behavior

- If exposing a local HTTP/OpenAI-compatible server, add authentication/network limits and measure concurrent requests.
- Multiple sessions multiply KV/cache and compete for four CPU cores/memory bandwidth.
- Record p50/p95 under intended concurrency.
- A Pi 5 CPU route that is acceptable for one batch task may be unsuitable as a multi-user chat server.
- Escalate shared-service concerns to server/platform scenarios when appropriate.

## Battery/UPS and 24/7 Operation

- For field/UPS use, include total board/peripheral power and inference duty cycle rather than CPU package assumptions.
- For 24/7 servers, measure sustained thermals, storage endurance, restart/recovery, and log/model update behavior.
- Do not infer always-on suitability from one desktop benchmark.

## Quality and Accepted Result

- Evaluate compact/quantized Pi candidates against an accepted stronger reference on representative tasks.
- Track hallucination/coding/reasoning/translation/etc. quality, retries, and human correction time.
- A smaller 2B-class model can be the better Pi route when it produces accepted results fast enough; parameter count alone does not determine value.
- A larger model that fits RAM but takes too long or needs more correction does not fit the intended interactive workload.

## Batch vs Interactive Work

- Define the target latency class before selection.
- CPU-local models can be practical for classification, extraction, embeddings, home automation, periodic summarization, offline fallback, or low-concurrency chat even when they are too slow for an IDE/voice agent.
- Keep slow-but-correct batch routes as conditional fit rather than labeling all CPU inference unusable.
- Compare hosted/accelerated alternatives for latency-sensitive generative workloads.

## Practical Fit Outcomes

- `Fits well`: exact Pi/OS/runtime/artifact/context/workload passes ARM compatibility, accepted quality, RAM headroom, TTFT/decode/task latency, sustained thermals, and application-contention thresholds.
- `Fits conditionally`: useful only for smaller/bounded tasks, batch workloads, reduced context, active cooling, limited concurrency, or another explicit acceptable constraint.
- `Does not fit`: exact CPU route fails RAM, latency, quality, thermal, dependency, or whole-system workload thresholds.
- `Unknown`: exact Pi generation/runtime/model artifact lacks current measurement.
- Do not assign fit from installed RAM, parameter count, or a model file loading successfully.

## Hosted/Accelerated Escalation

- Preserve hosted/API/hybrid routing when CPU latency/context/modality cannot meet the goal.
- Route Pi 5 + Hailo-8/8L vision acceleration to `hailo-8/` and Hailo-10H generative acceleration to `hailo-10h/`.
- Do not turn this page into accelerator purchasing advice.
- Compare local power/wait time/correction effort against hosted accepted-result economics.

## Canonical Links

- Link concrete model facts to Model Reference and LiteRT-LM/llama.cpp software to canonical owners when materialized.
- Link Raspberry Pi parent/router and Hailo siblings for accelerator routes.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Link user scenarios when task/data needs dominate hardware fit.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Raspberry Pi first-party Pi 5 CPU/LiteRT-LM/Gemma performance material, current Raspberry Pi 5 RAM/product guidance, and current Raspberry Pi thermal/power documentation.
- Current evidence demonstrates reproducible Pi 5 8 GB/four-thread Gemma 4 E2B CPU benchmarks with explicit prefill/decode/memory conditions and confirms sustained heavy CPU work can require active cooling to avoid throttling. These results do not establish universal Pi model tiers.
- Raspberry Pi OS/kernel, LiteRT-LM/XNNPACK, llama.cpp, model artifacts, GPU/WebGPU integrations, board firmware, and supported Pi generations are mutable; recheck them before rendering recommendations.
- Exact board/runtime/artifact/context/cooling measurement and accepted-result quality remain the fit authority.

## Validation

- No Hailo/other accelerator is assumed.
- Pi generation/RAM/64-bit OS/runtime/artifact/context are explicit.
- RAM capacity does not become a parameter-size tier.
- Current provider benchmark retains its Pi 5 8GB/four-thread/1024-prefill/256-decode conditions.
- Prompt/prefill and decode are measured separately.
- ARM64 dependencies, app/background contention, storage, power, and sustained cooling are represented.
- VideoCore/LiteRT WebGPU vision evidence is not misrepresented as generic LLM GPU acceleration.
- Load success is not practical fit.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
