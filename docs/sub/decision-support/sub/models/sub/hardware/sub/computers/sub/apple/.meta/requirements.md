# Documentation Requirements

## Route Fit

- Cover Apple-Silicon Macs where unified memory and Apple-native/Metal-backed runtimes define the local model route.
- Require the exact M-series SoC/device generation, installed unified memory, macOS version, power mode where relevant, intended runtime/backend, exact model artifact/quantization, context, modality, and concurrent application load before making a fit claim.
- Do not route Intel Macs here merely because they run macOS; they follow the effective CPU/GPU route actually used.
- Keep Mac purchasing/memory-upgrade advice outside this page. The reader starts from an already owned/fixed Mac.

## Current Runtime Boundary

- Treat MLX as a current first-party Apple-Silicon inference/training framework, but not the only viable local runtime.
- Current MLX 0.32.1 Python packages require Apple silicon, native ARM Python 3.10+, and macOS 14+ for the Apple route. Recheck these requirements before rendering current advice.
- Current MLX documentation exposes CPU and GPU execution over shared unified memory and provides memory telemetry/control APIs such as active memory, peak memory, cache memory, memory limits, and macOS wired-memory controls.
- `llama.cpp` remains a current independent local-runtime option with first-class Apple-Silicon/Metal support and broad GGUF quantization support. Treat MLX-format and GGUF/Metal artifacts as different runtime routes rather than interchangeable files.
- Core ML or application-specific Apple frameworks may be preferable for packaged application inference; verify exact model/operator/export support rather than assuming an MLX model can be deployed through Core ML unchanged.

## Unified Memory Is Shared System Memory

- Treat unified memory as one shared pool used by macOS, applications, CPU/GPU workloads, display, model weights, KV/cache, runtime buffers, multimodal encoders/decoders, and filesystem/cache pressure.
- Do not label unified memory as dedicated VRAM.
- Record free/available memory and memory pressure under the actual workload, not only installed capacity.
- Measure runtime peak memory rather than estimating from model file size.
- Reserve headroom for the OS, IDE/browser/creative tools, model context growth, runtime cache, and transient allocations.
- Treat swap as a measurable degradation/failure boundary rather than extra model memory. A model that runs only under heavy swap may be technically loadable but practically unsuitable.

## MLX Memory Evidence

- Use MLX memory APIs where applicable to record active, peak, and cache memory separately.
- Current MLX notes that active-memory reporting can differ from total system use because cached buffers are separate.
- On macOS 15+, MLX exposes a wired-memory limit; current documentation explicitly requires the wired limit to remain below total memory and exposes the system-recommended working-set size.
- Do not increase wired-memory limits merely to force a larger model without checking overall system responsiveness and the operational reason for doing so.
- Preserve the exact MLX version because memory behavior, kernels, quantization, and supported models can change.

## Model Artifact and Quantization

- Record exact producer/model/revision, runtime-native artifact, quantization/precision, tokenizer, adapters, vision/audio encoders, and any conversion step.
- Do not infer quality from quantization bit width alone. Evaluate accepted-result quality on the target tasks.
- For converted MLX artifacts, preserve the original model identity and conversion tool/version/parameters.
- For GGUF, preserve the exact quantization and llama.cpp build/backend.
- Do not compare an MLX quantization and a GGUF quantization as equivalent solely from nominal bits per weight.

## Context and KV Cache

- Include context/KV cache in every memory fit calculation.
- Measure the context lengths the user actually needs rather than using only a short default benchmark.
- Current MLX documentation shows KV-cache implementation strategy can materially affect latency and allocation behavior as context grows; therefore runtime/model implementation matters in addition to raw memory capacity.
- Test long-context prompt ingestion and decode separately.
- If a model requires reducing context substantially to remain usable, record that as a capability constraint rather than presenting the base model's advertised context as available.

## CPU, GPU, and Neural Engine

- Distinguish MLX CPU/GPU execution from Apple Neural Engine/Core ML paths.
- Do not infer that the Neural Engine accelerates an MLX/Metal LLM merely because the Mac includes one.
- Verify exact runtime/operator/export support before attributing any workload to ANE.
- Measure hybrid CPU/GPU behavior when a runtime uses both.
- Keep unsupported/unmeasured ANE/model combinations `Unknown`.

## Prompt and Decode Performance

- Measure at minimum:
  - model load/startup time;
  - prompt-processing throughput/latency at realistic context;
  - time to first token;
  - sustained decode tokens/s or task latency;
  - peak unified-memory use and system memory pressure;
  - quality on representative tasks.
- Do not extrapolate long-prompt behavior from decode-only speed.
- Compare cold and warm runs when compilation/kernel cache/model cache materially changes latency.
- Current MLX can compile/fuse computation graphs and uses lazy evaluation, so benchmark methodology must force actual execution and avoid measuring deferred work incorrectly.

## Real Desktop Contention

- Run acceptance tests with the applications the user normally keeps open: IDE, browser, Docker/VMs, design/video tools, local databases, conferencing, or other heavy workloads.
- For creator/developer machines, verify whether display/creative workloads compete materially for unified memory/GPU time.
- Measure battery/power/thermal behavior on laptops under sustained inference where it affects use.
- Do not use a clean reboot benchmark as the only evidence for an interactive workstation recommendation.

## Multimodal and Media Workloads

- Include image/audio/video encoders, diffusion/decoder components, VAE, upscalers, and preprocessors in memory/performance measurements.
- Separate text LLM fit from image generation, multimodal VLM, speech, and video generation fit.
- A Mac that is comfortable for a quantized text model may be unsuitable for a higher-resolution media pipeline or vice versa.
- Measure complete accepted workflow latency rather than one model stage.

## Multi-Model and Agent Workloads

- Measure concurrent memory when a workflow keeps embedding, reranker, LLM, VLM, speech, or agent-support models resident together.
- Do not sum standalone peak-memory numbers blindly; measure the actual combined process/runtime behavior.
- Account for local tools/containers/browser automation and retrieved-document caches when evaluating agents.
- If concurrency causes swap or unacceptable latency, prefer sequential loading, smaller specialists, hosted/hybrid routing, or another existing target rather than pretending each model fits simultaneously.

## Distributed and Multi-Mac Use

- Treat MLX distributed/tensor-parallel capability as a separate advanced route whose network/interconnect/topology and model implementation require explicit evidence.
- Do not add unified memory across multiple Macs and call it one usable model-memory pool.
- Measure communication overhead and supported distributed execution for the exact framework/model.
- If operating several Macs becomes shared infrastructure, route platform concerns to the organization/internal-platform scenario rather than expanding this personal-computer page.

## Quality and Accepted Result

- Use device/runtime measurements only after the candidate model meets the task-quality threshold.
- Compare compact/quantized models against a stronger hosted or larger local reference on representative tasks to quantify quality loss.
- Treat provider/model benchmarks as candidate evidence, not proof that the quantized local artifact meets the user's workflow.
- Track retries and correction time; a faster local model can have worse accepted-result economics if it requires substantially more human repair.

## Practical Fit Outcomes

- `Fits well`: exact artifact/runtime/context/workload passes quality, memory-headroom, latency, and sustained-use thresholds with the normal desktop workload.
- `Fits conditionally`: requires reduced context, lower quantization, serial model loading, closing heavy applications, or other explicit constraint that remains acceptable.
- `Does not fit`: exact workload fails memory, latency, quality, modality, runtime-support, or stability thresholds.
- `Unknown`: exact device/runtime/artifact combination lacks current support or measurement.
- Do not use installed memory alone to assign any outcome.

## Hosted/Hybrid Escalation

- Keep hosted/API/hybrid routing as a valid outcome when the existing Mac cannot meet quality/context/latency needs.
- Hybrid routing can keep private preprocessing/retrieval/local drafts on the Mac while escalating approved difficult workloads to hosted models.
- Compare total cost per accepted result including local power, time, retries, and workflow friction rather than treating local inference as free.
- Link `user-scenarios/professionals/mac-developer-or-creator/` when professional workflow/data handling rather than raw hardware fit becomes primary.

## Canonical Links

- Link concrete model facts to Model Reference rather than copying model cards here.
- Link `decision-guides/local-resource-fit/` when starting from a model artifact instead of the Mac.
- Link exact runtimes/software to their canonical software entities when materialized.
- Link professional Mac context to `catalog/models/selection/user-scenarios/professionals/mac-developer-or-creator`.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Apple MLX 0.32.1 install, unified-memory, memory-management, KV-cache, compilation, and LLM-inference documentation plus current `llama.cpp` Apple-Silicon/Metal backend documentation.
- Current MLX evidence confirms the Apple route requires Apple silicon and macOS 14+ for current Python packages, uses a shared CPU/GPU unified-memory model, and exposes runtime memory/working-set controls. It does not establish that a particular model/context is practical on a particular M-series SKU.
- MLX, Metal/Core ML, llama.cpp, macOS, model conversion, quantization support, and model implementations are mutable; recheck them before rendering current recommendations.
- Exact device/runtime/artifact/context measurements and accepted-result quality remain the fit authority.

## Validation

- Unified memory is not labeled VRAM or treated as fully available to the model.
- Current OS/runtime requirements are explicit rather than assumed from Apple-Silicon branding.
- MLX, Metal/GGUF, Core ML/ANE, CPU, and GPU execution paths are not conflated.
- Peak memory includes context/KV/runtime/cache/other applications rather than weight-file size alone.
- Swap-heavy load success is not accepted as practical fit.
- Long-context and prompt/decode performance are measured separately.
- Multimodal and multi-model pipelines include all resident components.
- Hardware-fit and professional-scenario ownership remain separate.
- Buying advice remains outside the page.
- Mutable current evidence carries the 2026-08-24 boundary.
