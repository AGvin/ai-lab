# Documentation Requirements

## Route Fit

- Cover Android phones/tablets using MediaTek Dimensity-class SoCs where MediaTek APU/NPU, GPU, or CPU acceleration through NeuroPilot/Neuron or supported Android runtimes is the intended custom on-device route.
- Require exact retail device, MediaTek SoC/platform, Android build, NeuroPilot access tier/version, runtime/entry point, model/export, supported operators/data types, execution devices, app memory, battery/thermal envelope, and target latency before assigning fit.
- Keep Dimensity Android guidance separate from MediaTek Genio/embedded Linux products even when both use NeuroPilot branding.
- Keep device purchasing outside this route.

## NeuroPilot Is an Ecosystem, Not One Runtime

- Treat NeuroPilot as the MediaTek AI tool/API/runtime ecosystem rather than one universal inference engine.
- Current NeuroPilot documentation distinguishes TFLite/MediaTek interpreter, NNAPI, Neuron Delegate, Neuron Adapter, Neuron compiler/runtime, and hardware-specific SDK paths.
- Preserve the exact app-facing entry point and developer role.
- Do not write `runs on NeuroPilot` without identifying which runtime/entry point and which target compute core actually executes the graph.
- Treat NeuroPilot Public, Basic, and Premium access tiers separately because available documentation/tools/features differ and higher tiers can require NDA/OEM/enterprise access.

## Third-Party App vs OEM Boundary

- Current MediaTek Android workflow explicitly distinguishes third-party app vendors, algorithm vendors, and OEM/platform developers.
- For an ordinary third-party APK, the documented path is TFLite/TFLite Shim with NNAPI or Neuron Delegate and on-device/online compilation.
- Current documentation states that third-party app developers cannot use the direct Neuron Runtime API because that path is restricted to vendor-partition applications.
- OEM/platform routes can use lower-level Neuron Adapter/SDK/runtime and offline-compiled `.dla` artifacts under different deployment constraints.
- Do not recommend an OEM/vendor-partition deployment method to an ordinary Play/APK application without explicit access/evidence.

## Model Preparation and Deployment Are Two Phases

- Preserve model preparation/optimization/conversion on a development machine separately from device-side deployment.
- Current NeuroPilot flow converts supported TensorFlow/PyTorch models toward TFLite or MediaTek-specific artifacts and can apply quantization/optimization before Android deployment.
- Record source model/revision, converter/tool version, TFLite/export version, quantization/calibration, shapes, and resulting artifact.
- Record whether device-side compilation is online at app load or an OEM offline-compiled artifact is used.
- Include compile/cache/startup overhead in the app acceptance test.

## Exact Platform Operator Matrix

- Require the current platform-specific supported-operations/data-type documentation for the exact Dimensity/MediaTek platform.
- Current NeuroPilot documentation states that operations can have hardware-platform-specific limitations and directs developers to each platform's hardware support specification.
- Do not infer support from a neighboring Dimensity generation or from generic TensorFlow Lite compatibility.
- A TFLite model can be functionally runnable through CPU fallback while important operators are unsupported on the APU/NPU.
- Keep unsupported/unmeasured accelerator coverage `Unknown`.

## CPU, GPU, MVPU/APU/NPU Paths Are Distinct

- Record which operations execute on CPU, GPU, MVPU/APU/NPU/MDLA-class hardware according to the exact platform generation.
- Current NeuroPilot documentation describes heterogeneous compute with different operator flexibility, data types, power, and performance characteristics by target device.
- Do not translate the older MDLA/MVPU naming or capabilities directly to newer APU generations without current platform evidence.
- Measure fallback/partition boundaries and inter-device transfer overhead.
- Do not label a partially accelerated graph `NPU inference` without reporting material CPU/GPU work.

## TFLite / LiteRT Android Route

- Treat TFLite/LiteRT as the ordinary Android application route when supported by the current MediaTek software stack.
- Current NeuroPilot public guidance states that MediaTek supports the standard TFLite Android model-development flow and provides an optimized interpreter/shim/delegates to exploit MediaTek hardware.
- Record the TFLite/LiteRT version, MediaTek interpreter/shim/delegate version, Android/NDK level, model artifact, and delegate configuration.
- Verify the actual delegated operations and target devices at runtime/profiling time.
- Do not assume every valid `.tflite` model receives APU acceleration merely because CPU execution is guaranteed by the base framework.

## NNAPI and Neuron Delegate

- Keep NNAPI and MediaTek Neuron Delegate paths separate where they expose different capabilities/performance.
- Current NeuroPilot docs describe MediaTek hardware acceleration under NNAPI and direct MediaTek delegate/runtime layers.
- Record the chosen delegate/entry point and why it is selected for the target app/device.
- Verify whether the Android version still supports/deprecates the relevant generic API and whether MediaTek's current recommended route has changed.
- Recheck this boundary before rendering because Android platform ML APIs evolve independently from MediaTek tooling.

## ONNX Runtime Route

- Treat ONNX Runtime on MediaTek Android as a separate access-controlled route.
- Current MediaTek Genio/Android AI documentation states that ONNX Runtime Android hardware-accelerated libraries/Execution Providers can require direct customer contact/access and may not have the same public samples as TFLite.
- Do not assume a generic ONNX Runtime Android package exposes the MediaTek NPU.
- Record the exact MediaTek-provided ORT library/EP, platform, version, model/op coverage, and distribution rights before recommending it.
- Keep unavailable/private SDK paths `Unknown` for ordinary users rather than inferring behavior.

## Generative AI Requires Exact Model Evidence

- MediaTek has demonstrated on-device generative AI, diffusion, LoRA, and large-model capabilities on flagship Dimensity platforms, but demonstrations are not a support matrix for arbitrary models.
- Require current vendor/runtime evidence for the exact transformer/diffusion/VLM architecture, model export, quantization, context, and target SoC.
- Do not infer support from APU generation, benchmark TOPS, or a vendor demo using a different proprietary optimized artifact.
- Treat current generative-model SDK/access limitations separately from analytical vision/TFLite support.
- Preserve `Unknown` when public documentation does not establish a deployable third-party-app path.

## Model Conversion and Quantization

- Record exact source framework/model, converter/version, quantization method, calibration data where used, target data types, and output artifact.
- Verify target-platform data-type support for every material operator.
- Evaluate semantic/task quality after conversion/quantization rather than only numerical/runtime success.
- Do not assume INT8/FP16 support is identical across CPU/GPU/NPU blocks or SoC generations.
- Preserve reproducible conversion commands/configuration for production artifacts.

## App Memory and Shared System Memory

- Treat Android app/process memory and shared system memory separately from nominal installed device RAM.
- Include model/artifact, compiled graph/cache, runtime buffers, input/output tensors, KV/cache, preprocessing/postprocessing, UI, images/audio, and concurrent system/app use.
- Measure low-memory/termination behavior on the actual OEM device.
- Do not publish fixed RAM-to-model-size tiers for Dimensity devices.
- A model that relies on heavy memory pressure or frequent recompilation/loading may fail practical mobile fit even if it executes.

## Startup and Device Compilation

- For online-compile routes, measure initial model load/compile, subsequent cached load, first inference, and steady repeated inference separately.
- Preserve cache invalidation behavior after app/runtime/OS/model changes.
- Include startup cost in user-facing latency for infrequently used features.
- Do not report only warm NPU kernel timing as application startup/perceived latency.

## Generative LLM Measurement

- Measure tokenizer/input preparation, prefill/prompt processing, context/KV-cache allocation, sustained decode, sampling, and output handling end to end.
- Record context/input/output lengths and execution-device partitioning.
- Do not extrapolate LLM performance from CNN/image benchmark throughput or APU TOPS.
- If current public NeuroPilot documentation does not establish complete third-party LLM deployment support for the exact SoC/model, keep fit `Unknown` until device evidence exists.
- Record any context/model reduction required to fit memory/thermal limits.

## VLM, Speech, Diffusion, and Video

- Treat each modality as a separate pipeline with separate operator/runtime evidence.
- For diffusion/video generation, include text/image encoders, denoiser/transformer/UNet, iteration/scheduler work, VAE/decoder, and postprocessing.
- For VLM/speech, include encoders/decoders and preprocessing.
- Do not use a vendor demonstration of one optimized component as evidence for complete application latency or third-party deployability.
- Measure accepted-result quality on the actual device and artifact.

## Profiling and Actual Device Placement

- Use NeuroPilot/platform profiling tools where available to identify operator placement, latency, memory, and target compute cores.
- Current NeuroPilot documentation explicitly includes on-target profiling as a development capability.
- Record profiler/tool version and device firmware/build.
- Verify that acceleration remains active in the production APK/configuration rather than only in an OEM sample environment.
- Keep unobservable placement claims `Unknown`.

## OEM Firmware and Device Fragmentation

- The same nominal Dimensity SoC can appear in devices with different RAM, cooling, firmware, power policy, Android version, and vendor ML stack.
- Record the exact retail device/build rather than using only SoC marketing name.
- Re-test after major OTA/firmware/runtime updates.
- Do not transfer MediaTek reference-platform measurements directly to another OEM device without equivalence evidence.

## ARM64 and Android Dependencies

- Verify all native inference/runtime/pre/post-processing libraries for Android ARM64 and the target API/NDK level.
- Record ABI/package restrictions for vendor SDKs and model-distribution artifacts.
- Do not assume Linux/desktop MediaTek/Genio examples can be packaged into a standard Android app unchanged.
- Include app-store/package-size/licensing constraints where model/runtime distribution is material.

## Storage and Model Delivery

- Include model files, compiled caches, multiple quantizations, runtime native libraries, downloadable assets, and temporary conversion/cache space.
- Define first-run/on-demand model delivery and offline availability.
- Preserve version/hash/provenance for app-downloaded models.
- Clean up superseded artifacts and define rollback when model/runtime updates can regress compatibility.

## Battery and Thermals

- Measure sustained repeated use on the actual OEM device under intended power/thermal state.
- Record battery drain, thermal throttling, surface temperature/user comfort, and latency after the device is warm.
- NeuroPilot is designed for power-efficient heterogeneous acceleration, but platform-level efficiency claims are not an application measurement.
- Do not use short reference benchmarks or APU TOPS as sustainable mobile performance evidence.

## Android Lifecycle

- Verify foreground/background/service behavior for the chosen runtime and model workload.
- Model initialization/compilation and long generation must handle activity/process interruption safely.
- Do not treat a mobile app as a persistent desktop inference daemon unless Android policy and application architecture explicitly support it.
- Preserve restart/retry/idempotency for long jobs and external actions.

## Prompt Injection and Agents

- Local APU execution does not make agents or tool use safe.
- Treat documents/web/images/QR/text/tool results as untrusted when an application can perform network/account/device actions.
- Keep Android permissions and tool allowlists deterministic outside model prompts.
- Validate arguments and require confirmation for consequential actions.

## Quality Evaluation

- Compare converted/quantized MediaTek artifacts against an accepted reference on representative tasks.
- Include unsupported/fallback operators, long inputs, warm/thermal state, and device fragmentation.
- Track retry/correction burden with latency and battery.
- Vendor demo/profile success is not accepted-result evidence.

## Practical Fit Outcomes

- `Fits well`: exact device/SoC/Android/NeuroPilot entry point/artifact passes third-party deployability, operator coverage, quality, memory, latency, battery/thermal, and lifecycle thresholds.
- `Fits conditionally`: requires OEM/private SDK access, a specific delegate/export, partial fallback, smaller model/context, reduced usage, or another explicit acceptable constraint.
- `Does not fit`: exact route fails developer-access, operator/model support, memory, latency, quality, thermals, lifecycle, or distribution requirements.
- `Unknown`: exact current SoC/runtime/model path lacks public/independent deployment evidence.
- Do not assign fit from Dimensity tier, APU generation, benchmark score, or TOPS alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when the local MediaTek path cannot meet deployability, quality, context, or latency needs.
- Do not silently send sensitive input to cloud fallback.
- Compare local SDK/access/conversion complexity, storage, battery, retries, and correction time against hosted accepted-result economics.
- Keep phone purchasing outside the route.

## Canonical Links

- Link exact models to Model Reference and NeuroPilot/TFLite/ORT tooling to canonical software owners when materialized.
- Link Android parent router for cross-SoC routing.
- Keep MediaTek Genio/embedded Linux in its applicable embedded/single-board route rather than this mobile route.
- Link user scenarios when application/data goal dominates hardware fit.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current MediaTek NeuroPilot Public documentation, current Dimensity Developer Center NeuroPilot architecture/workflow/platform-operation material, current MediaTek Android AI framework/access documentation, and current 2026 NeuroPilot SDK availability evidence.
- Current evidence establishes third-party Android TFLite/NNAPI/Neuron-Delegate paths with platform-specific operator restrictions, separate OEM/vendor-partition Neuron Runtime/offline-compiled paths, heterogeneous CPU/GPU/APU execution, and access-tier differences. It does not establish arbitrary generative-model support on every Dimensity device.
- NeuroPilot SDK/tool versions, access tiers, supported SoCs/operators/data types, Android runtimes/delegates, OEM firmware, and generative-model support are mutable; recheck them before rendering recommendations.
- Exact retail device/developer-access/runtime/artifact/full-pipeline measurement and accepted-result quality remain the fit authority.

## Validation

- Mobile Dimensity and embedded Genio/Linux product classes remain separate.
- Third-party APK and OEM/vendor-partition deployment methods are not conflated.
- TFLite/LiteRT, NNAPI/Neuron Delegate, direct Neuron runtime, ONNX Runtime, GPU, CPU, and hosted routes are distinguished.
- Platform-specific supported operators/data types and actual graph placement remain visible.
- Marketing demonstrations and APU TOPS are not treated as exact generative-model support or performance evidence.
- App memory, startup/compile, lifecycle, storage, device fragmentation, battery/thermals, and accepted quality are measured.
- Private/NDA SDK requirements remain explicit rather than assumed accessible.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
