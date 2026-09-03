# Documentation Requirements

## Route Fit

- Cover Android phones/tablets whose **actual SoC is Samsung Exynos** and where Exynos NPU/GPU/CPU execution is the intended custom on-device model route.
- Require exact retail device, Exynos SoC/NPU generation, Android/firmware build, Exynos AI Studio/ExecuTorch/other current runtime, model source/export, optimization/quantization, compiled artifact, app memory, battery/thermal envelope, and target latency before assigning fit.
- Route Galaxy devices using Snapdragon hardware to `android/qualcomm/`; Samsung/Galaxy product branding is not an execution target.
- Keep device purchasing outside this route.

## Exynos Hardware, Not Galaxy Branding

- Identify the actual SoC for the exact regional/device SKU before using this route.
- Samsung can ship different Galaxy models/regions with Exynos or Qualcomm SoCs; do not infer Exynos from the phone brand/model family alone.
- Record SoC/board/device build in benchmark evidence.
- Keep Galaxy AI consumer-feature availability separate from the custom-model hardware route.
- A Galaxy feature running locally or through cloud services does not prove an arbitrary app model can use the Exynos NPU.

## Retire Samsung Neural SDK as a Third-Party Default

- Do not present Samsung Neural SDK as the current ordinary third-party developer route.
- Samsung Developer currently states that Samsung Neural SDK download policy changed and the SDK is no longer provided to third-party developers.
- Preserve Samsung Neural SDK only as historical/legacy evidence when analyzing an existing application that already uses it.
- Do not derive new 2026 Exynos model-support claims from its 2021-era supported-device/format matrix.
- Route current custom-model work through current Exynos AI Studio, ExecuTorch, or another currently supported developer path with exact evidence.

## Current Exynos AI Studio Boundary

- Treat Exynos AI Studio as Samsung Semiconductor's current first-party custom-model optimization/toolchain route for Exynos NPUs.
- Current public Exynos Developer Society documentation identifies **Exynos AI Studio SDK 2.5** and separates a high-level toolchain (EHT) from a low-level hardware-specific toolchain (ELT).
- EHT handles model conversion, graph optimization, quantization, simulation, and related model-level processing.
- ELT performs SoC/NPU-specific lowering, optimization, compilation, runtime preparation, and generation of Exynos-executable NNC artifacts.
- Preserve the exact SDK/tool version because supported IRs, operators, quantization, NPU generations, and generated binaries can change.

## Model Lowering Is Part of Compatibility

- Record source model/framework/revision and every material lowering stage.
- Current Exynos AI Studio accepts current open model IRs such as ONNX/TFLite and is expanding/strengthening PyTorch-oriented flows for generative models.
- Preserve IR conversion, internal representation, graph optimization, quantization, hardware-specific lowering, compiler version, and final NNC artifact.
- Do not call a source PyTorch/ONNX/TFLite model `Exynos NPU supported` until the exact toolchain successfully lowers/compiles the required graph for the target NPU.
- Keep conversion/compile failures and unsupported operators visible as compatibility evidence.

## Verification at Every Lowering Stage

- Preserve numerical/semantic validation through the transformation pipeline rather than verifying only that the final binary executes.
- Current Exynos AI Studio documentation provides simulator/emulator stages that compare intermediate/final lowered outputs against the original model, including SNR-style operator comparison and NPU emulation.
- Use those tools as compatibility/numerical evidence and still run task-level accepted-quality evaluation on the physical target device.
- Do not treat acceptable SNR or compiler success as proof that an aggressively quantized generative model preserves user-task quality.
- Record tolerances/validation method with the artifact.

## Quantization Is Model and NPU Specific

- Record exact source precision, target precision, PTQ/QAT/calibration method, dataset, grouping/scales where material, and generated artifact.
- Current Exynos AI Studio documentation describes hardware-aware optimization and low-precision conversion such as INT8/INT16/FP16 for supported workflows.
- Treat supported precision as model/operator/NPU-generation specific rather than universal to all Exynos NPUs.
- Compare accepted-result quality before/after optimization.
- Do not infer fit from smaller artifact size alone.

## Exynos 2600 Current Boundary

- Current Exynos 2600 is a current Exynos mobile platform with integrated CPU/GPU/NPU and explicit on-device generative-AI positioning.
- Samsung states that its NPU improves generative-AI performance relative to Exynos 2500 and supports larger/more diverse on-device models; treat the percentage as vendor internal comparative evidence, not expected app performance.
- Current Exynos 2600 material also states support for ExecuTorch, creating a current PyTorch-oriented deployment route on Exynos-powered devices.
- Do not transfer Exynos 2600 runtime/model support to Exynos 2500/2400/older platforms without exact evidence.
- Do not use NPU generation/marketing performance as a replacement for model compile/device measurement.

## ExecuTorch Route

- Treat ExecuTorch on Exynos as a separate current deployment route from Exynos AI Studio NNC artifacts when the application/model uses it.
- Record ExecuTorch version, Samsung/Exynos backend version, export/edge artifact, quantization, supported operators, delegate/partition coverage, and target device.
- Samsung currently states it is collaborating with Meta on an Exynos ExecuTorch backend and Exynos 2600 supports ExecuTorch; verify public availability/tooling for the exact device before recommending it.
- Do not infer that all PyTorch models execute fully on Exynos NPU simply because ExecuTorch can run on the platform.
- Preserve CPU/GPU/NPU partitioning and fallback.

## AICore / Gemini Nano Is Another Route

- Samsung documents collaboration with Google on Android AICore and Gemini Nano for on-device generative AI on Exynos.
- Treat AICore/Gemini Nano as a system-managed Android model route, separate from app-owned Exynos AI Studio/ExecuTorch models.
- Use the Android/Google system-model contract for AICore feature availability, model version, quotas/lifecycle, and API constraints.
- Do not claim AICore's Exynos NPU use proves a custom model has access to the same backend or optimization path.
- Preserve hosted/cloud Galaxy AI features separately from both local routes.

## Device Farm and Physical-Device Validation

- Current Exynos Developer Society exposes device-farm tooling for validating converted models/apps against actual Exynos devices.
- Use simulator/emulator stages for early numerical/toolchain validation and physical device tests for memory, latency, thermals, battery, driver/runtime behavior, and accepted quality.
- Record exact target device/firmware/SoC and device-farm configuration.
- Do not promote simulator/emulator results directly to retail-device practical fit.
- Re-test on the actual target retail device when OEM thermal/firmware configuration differs.

## NPU, GPU, and CPU Are Distinct

- Record where each material graph stage runs.
- Do not describe an app as `Exynos NPU inference` if unsupported operators or preprocessing/postprocessing dominate on CPU/GPU.
- Verify supported operations, partition points, transfers, and fallback through runtime/tool profiling where available.
- Measure end-to-end latency including all devices.
- Keep unsupported/unobservable placement `Unknown`.

## GPU and CPU Alternatives

- Treat Exynos GPU and ARM CPU inference as separate routes when the model cannot use the NPU or another runtime targets those processors.
- Verify exact backend/operator/precision support and Android compatibility.
- Record shared system-memory/display contention for GPU execution.
- Compare complete app latency/power rather than assuming NPU is always faster or available.
- Do not import Qualcomm delegate/runtime evidence onto an Exynos device.

## App Memory and Shared RAM

- Treat Android app/process memory, compiled-model/runtime memory, and system pressure separately from nominal installed device RAM.
- Include model/NNC/edge artifact, runtime buffers, KV/cache, images/audio, preprocessing/postprocessing, UI, and other foreground/system services.
- Measure low-memory/termination behavior on the retail device.
- Do not publish RAM-to-model-size tiers for Exynos phones.
- A model that compiles but causes memory pressure/app termination does not fit.

## Storage and Artifact Delivery

- Include model/source artifacts, NNC/ExecuTorch outputs, runtime native libraries, compiled caches, multiple quantizations/adapters, and temporary update space.
- Define app-bundled versus downloaded model delivery, integrity/versioning, cleanup, rollback, and offline availability.
- Preserve source-to-final-artifact provenance and hashes.
- Do not dynamically download unverified compiled/model artifacts into a sensitive app environment.

## Startup and Compilation Cost

- Measure first model/runtime initialization, compiled artifact load, first inference, warm inference, and long-idle restart separately.
- Include any on-device graph preparation/cache build if used by the current runtime.
- Do not report only steady NPU kernel time as app responsiveness.
- Preserve cache invalidation behavior after Android/firmware/runtime/model updates.

## LLM Measurement

- For autoregressive models, measure tokenizer/input preparation, prefill, KV-cache allocation/growth, token decode, sampling, and output processing.
- Record actual input/context/output lengths and execution partitioning.
- Do not derive LLM tokens/s or context capacity from Samsung's NPU comparative generative-AI percentage or TOPS.
- Verify the exact model/toolchain/quantization on the target Exynos device.
- Keep unmeasured LLM routes `Unknown`, even if the toolchain lists a model example.

## Current Example Models Are Eligibility Evidence

- Current Exynos Developer Society exposes example/model material including compact text-generation and image-generation models such as Qwen3 0.6B, Mamba 1.4B, Stable Diffusion v1.5, and other models.
- Treat these listings as toolchain/device-development examples, not AI Lab recommendations or proof that all retail Exynos devices run them at acceptable quality/performance.
- Record the exact model artifact, target NPU/device, optimization, and toolchain when using example evidence.
- Do not infer that a listed compact model implies support for a larger sibling.

## VLM, Image, Audio, and Video

- Samsung positions modern Exynos NPUs for on-device generative AI across language, image, audio, and video, but each pipeline needs exact model/toolchain evidence.
- Include every encoder/decoder/diffusion/video stage, iterations, preprocessing/postprocessing, and CPU/GPU fallback.
- Measure complete accepted pipeline latency and peak memory.
- Do not use SoC capability marketing as exact app-model compatibility.

## Mobile Battery and Thermals

- Measure repeated inference on the actual retail device in the intended power state.
- Record battery drain, thermal state/throttling, charge state, surface temperature/user comfort, and latency after warm-up.
- Exynos 2600/other vendor efficiency claims are architecture evidence, not sustained app measurements.
- A route that is acceptable only for short bursts is conditional fit for repeated-use workloads.

## OEM Firmware and Regional Variants

- Record exact device model/region/build because Samsung phone variants can differ in SoC, memory, modem/system load, firmware, and thermal policy.
- Re-test after major Android/One UI/firmware/runtime updates.
- Do not transfer a device-farm/reference result to another Galaxy/Exynos SKU without equivalence evidence.
- Verify SoC identity again for regional variants before using this route.

## Android Lifecycle

- Verify foreground/background/service constraints for the chosen runtime and workload.
- Handle model initialization, long generation, app suspension, and process termination safely.
- Do not treat an Android phone as a persistent desktop/server inference node without a supported application architecture.
- Preserve restart/retry/idempotency where generation or agent actions can be interrupted.

## Prompt Injection and Agents

- Local Exynos execution does not make tool-capable agents safe.
- Treat documents/web/images/QR/text/tool results as untrusted inputs.
- Keep Android permissions/tool scopes outside model-controlled text, validate arguments, and require confirmation for consequential actions.
- Do not expose privileged app/device data because model input requests it.

## Quality Evaluation

- Compare the lowered/quantized Exynos artifact against the accepted source/reference model on representative tasks.
- Use toolchain simulator/emulator numerical checks plus physical-device semantic/task evaluation.
- Include hard inputs, fallback graphs, long contexts, thermal state, and device/firmware variation.
- Track correction/retry burden alongside latency and power.
- Vendor support/example lists are not accepted-result proof.

## Practical Fit Outcomes

- `Fits well`: exact Exynos device/firmware/toolchain/runtime/artifact passes developer-access, compile/operator coverage, accepted quality, app memory, latency, battery/thermal, and lifecycle thresholds.
- `Fits conditionally`: requires a specific Exynos AI Studio/ExecuTorch route, aggressive quantization, smaller model/context, partial fallback, system AICore instead of custom deployment, or another explicit acceptable constraint.
- `Does not fit`: exact route fails current developer access, lowering/compile support, memory, quality, latency, thermals, lifecycle, or app-distribution requirements.
- `Unknown`: exact Exynos generation/device/runtime/model path lacks current public/independent deployment evidence.
- Do not assign fit from Exynos NPU performance claims, Galaxy AI availability, or SoC branding alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when local Exynos execution cannot meet deployability, quality, context, or latency needs.
- Do not silently send sensitive local input to cloud fallback.
- Compare local SDK/toolchain effort, model storage, battery, retries, and correction time against hosted accepted-result economics.
- Keep phone purchasing outside the route.

## Canonical Links

- Link exact model facts to Model Reference and Exynos AI Studio/ExecuTorch/AICore software to canonical owners when materialized.
- Link Android parent router for cross-SoC selection.
- Route Snapdragon Galaxy devices to `android/qualcomm/`.
- Use the Google Android route for system AICore/Gemini Nano API behavior when that is the selected route.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Samsung Exynos AI Studio SDK 2.5 documentation, current Exynos Developer Society model/device-farm material, current Samsung Semiconductor Exynos AI Studio toolchain strategy, current Exynos on-device-AI/ExecuTorch/AICore material, current Exynos 2600 product documentation, and the current Samsung Neural SDK deprecation/download notice.
- Current evidence establishes Exynos AI Studio conversion/optimization/quantization/simulation/emulation/compilation into NPU artifacts, current Exynos/ExecuTorch work, and separate AICore/Gemini Nano collaboration. Samsung Neural SDK is no longer a current third-party download route.
- Exynos AI Studio/ExecuTorch versions, supported IRs/operators/precisions, NPU generations, device-farm targets, AICore support, Android/firmware builds, and retail Exynos device availability are mutable; recheck them before rendering recommendations.
- Exact retail device/toolchain/artifact/complete-pipeline measurement and accepted-result quality remain the fit authority.

## Validation

- Samsung/Galaxy branding is not used as a hardware route; exact Exynos SoC is required.
- Snapdragon Galaxy devices remain in the Qualcomm route.
- Legacy Samsung Neural SDK is not presented as the current third-party developer path.
- Exynos AI Studio model lowering/quantization/compile and physical-device validation are part of compatibility.
- Exynos AI Studio, ExecuTorch, AICore/Gemini Nano, GPU, CPU, and hosted routes remain distinct.
- Toolchain simulator/emulator correctness does not replace retail-device task quality/memory/latency/thermal evidence.
- Vendor examples/performance percentages and NPU capability marketing do not become AI Lab fit claims.
- App memory, storage, Android lifecycle, firmware/region variants, fallback, battery/thermals, and accepted quality are measured.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
