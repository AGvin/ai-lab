# Documentation Requirements

## Route Fit

- Cover Snapdragon Android devices where Qualcomm Hexagon NPU/HTP, Adreno GPU, or CPU is the intended custom on-device inference route.
- Require exact retail device, Snapdragon SoC/part number and generation, Android build, QAIRT/QNN/LiteRT/delegate version, model/export, precision/quantization, graph coverage, app memory, battery/thermal envelope, and target latency before assigning fit.
- Keep Snapdragon X Windows PCs in `hardware/computers/qualcomm/`; Android app lifecycle, SDK/delegate packaging, and mobile thermals are materially different.
- Keep device purchasing outside this route.

## Current Runtime Paths

- Separate direct QAIRT/QNN deployment, LiteRT with Qualcomm QNN delegate, ONNX Runtime QNN where used, GPU/CPU alternatives, and hosted model routes.
- Do not label every Qualcomm Android local workload simply `QNN`; preserve the actual app-facing runtime and backend.
- Current Qualcomm AI Hub August 2026 profiles include both direct QNN and LiteRT + QNN delegate executions on current Snapdragon Android devices.
- Treat API/runtime availability as exact version/device evidence rather than a permanent SoC-family property.

## Exact SoC and Device Evidence

- Record the full Snapdragon target identity rather than a marketing family name alone.
- Current AI Hub jobs explicitly identify retail devices, Android version, Snapdragon part/configuration, QAIRT/QNN versions, and compute unit.
- Current examples on Galaxy S26 use Snapdragon 8 Elite Gen 5 for Galaxy / SM8850-AD with Android 16 and current QAIRT/QNN 2.45-era tooling.
- Do not transfer those results to another 8-series part, OEM thermal design, Android build, or older/newer QAIRT release without measurement.
- Keep OEM-specific firmware/driver effects visible where they affect delegate/runtime behavior.

## AI Hub Is Compatibility/Profiling Evidence

- Use AI Hub compile/profile results as provider-documented evidence that a named graph can execute on a named Qualcomm target/configuration.
- Record target, input shape, runtime/delegate, precision, performance mode, first/subsequent app load, inference time, memory range, and compute unit.
- Do not convert a provider profile into an AI Lab endorsement or whole-application benchmark.
- Reproduce the final compiled/exported artifact on the actual retail device before assigning practical fit.

## Subgraph vs Complete Application

- Many AI Hub jobs profile a single detector, encoder, decoder, diffusion component, or other graph stage.
- Treat model/application fit as the sum of preprocessing, graph(s), inter-stage transfers, runtime initialization, postprocessing, and UI/application logic.
- A subgraph that profiles on NPU does not prove every stage runs on NPU.
- Preserve CPU/GPU fallback and graph partitioning explicitly.
- Keep complete-model fit `Unknown` when only partial graph evidence exists.

## LiteRT + QNN Delegate

- Current AI Hub evidence demonstrates LiteRT 1.4.x with QNN TfLite Delegate on current Snapdragon Android hardware.
- Record LiteRT/delegate versions, delegate backend, thread settings, precision, graph partition, and unsupported operators.
- Do not assume a LiteRT model automatically uses HTP/NPU because the delegate is installed.
- Verify delegated-node coverage and any CPU fallback through profiling/logging.
- Include delegate initialization and compiled-context load in app startup measurements.

## Direct QAIRT/QNN Route

- For direct QNN/QAIRT apps, preserve backend API/core API version, target backend, graph/context options, precision, and compiled artifact.
- Current provider profiles often use HTP `BURST` performance mode and aggressive optimization settings; treat them as performance-test configurations rather than default sustained battery behavior.
- Measure a production power mode and workload duration separately.
- Do not assume direct QNN and LiteRT delegate produce identical memory/latency for the same model.

## NPU/HTP Model Compatibility

- Treat Hexagon NPU/HTP as model/operator/export specific.
- Verify supported operators, shapes/dynamic-shape restrictions, quantization/precision, and graph compilation for the exact QAIRT release.
- Preserve unsupported operators and partition points.
- Do not infer arbitrary LLM/VLM/diffusion compatibility from NPU TOPS or successful CNN profiles.
- Mark unsupported/unmeasured model families `Unknown`.

## Quantization and Precision

- Record exact source model, export path, calibration where applicable, graph precision, input/output quantization, and runtime/compiler version.
- Current QNN profiles can use FP16 or quantized graph I/O depending on the model/runtime path; preserve the actual configuration.
- Evaluate task quality after conversion/quantization.
- Do not select a lower precision only for speed if accepted-result quality falls below threshold.
- Do not compare model artifacts as equivalent from nominal bit width alone.

## Android App Memory

- Treat app/process memory and system pressure as separate from installed device RAM.
- Include compiled graph/model assets, runtime/context memory, input/output tensors, KV/cache, images/audio, preprocessing/postprocessing, UI, and concurrent app/system load.
- Current AI Hub profiles expose ranges that can differ materially between first load, subsequent load, and inference; preserve those stages.
- Test low-memory/termination behavior on the retail device.
- Do not publish RAM-to-model tiers for Snapdragon phones.

## Startup and Cached Execution

- Measure first app/model load, subsequent load, first inference, and steady repeated inference separately.
- Current provider jobs show first-load overhead from sub-second to seconds/minutes depending on graph/model; this can dominate mobile UX.
- Define whether compiled context/cache persists across app launches/updates.
- Include artifact download/install preparation and cache invalidation after runtime/model upgrades.

## LLM and Stateful Generative Workloads

- For LLMs, measure tokenizer/preprocessing, prefill/prompt processing, KV-cache creation/growth, decode, sampling, and output handling end to end.
- Do not extrapolate LLM tokens/s from generic NPU vision graph throughput.
- Record context/input/output lengths, cache precision, model partition, and execution devices.
- Verify full-model graph/operator support rather than only a decoder/prefill component.
- Treat context reduction needed for stable memory/thermals as a conditional fit.

## VLM, Speech, Image, and Video

- Evaluate each modality separately because graph structure/operator support and preprocessing differ.
- Current AI Hub profiles demonstrate broad vision/media components on NPU, but this is candidate compatibility evidence only.
- For image generation, include text encoder, denoiser/transformer/UNet, scheduler iterations, VAE, and output postprocessing.
- For VLM/speech/video, include all encoders/decoders and data movement.
- Do not present one component's milliseconds as final media-generation latency.

## Adreno GPU Alternative

- Treat Adreno GPU as a separate execution route using the exact supported backend/runtime.
- Verify model/operator/precision support and measure shared-memory/display contention.
- GPU fallback can outperform NPU on unsupported models but may consume more battery/thermal budget; measure instead of assuming.
- Keep Vulkan/OpenCL/other community runtime evidence labeled independently from official QNN support.

## CPU Fallback

- Record CPU fallback explicitly, including which stages and how much latency they contribute.
- A functionally correct result with substantial CPU fallback can still fail battery/latency requirements.
- Compare bounded CPU-local alternatives when the NPU graph is fragmented.
- Do not describe a partially delegated graph as `NPU inference` without qualification.

## Battery and Thermals

- Measure sustained production configuration on the actual OEM device.
- Record battery drain, thermal state, throttling, charge state, and user-visible latency after repeated calls.
- Provider `BURST` profile settings do not establish sustainable mobile power behavior.
- Test representative session length rather than one cool-device run.
- A route that becomes slow or thermally limited under normal repeated use is conditional/does-not-fit depending on the target.

## Android Lifecycle and Background Use

- Verify the app/runtime behavior under foreground/background/suspend/termination states.
- Long model initialization or generation must tolerate activity/process lifecycle changes safely.
- Do not model Android as a persistent desktop inference daemon unless the application architecture explicitly supports a service and platform policy permits it.
- Preserve restart/idempotency for generated outputs/actions.

## Storage and Packaging

- Include app/APK/AAB assets, native ARM64 libraries, compiled QNN contexts, model downloads, multiple precision variants, and caches in storage evidence.
- Define initial download/on-demand model delivery/cleanup behavior.
- Preserve artifact hashes/version and rollback if models are updated independently from the app.
- Do not download arbitrary model/compiler components dynamically in a high-security/offline route without approved staging.

## ARM64 Native Dependencies

- Verify all native inference libraries and critical preprocessing/postprocessing dependencies for Android ARM64.
- Record NDK/API level/ABI requirements where material.
- Do not infer that a Python/desktop Qualcomm sample translates directly into an Android app deployment.

## OEM and Android-Version Drift

- Treat OEM firmware, Android update, driver, and thermal-policy changes as possible performance/compatibility changes.
- Re-run tests after major OS/runtime/firmware updates.
- Do not generalize Samsung AI Hub device evidence to a non-Samsung Snapdragon phone without explicit equivalence/measurement.
- Preserve device build fingerprint/version in benchmark records where reproducibility matters.

## Prompt Injection and Agents

- Local NPU inference does not make tool-capable agents safe.
- Treat files/web/QR/text/images as untrusted inputs when the app can perform actions.
- Restrict Android permissions/tools, validate arguments, and require confirmation for consequential network/account/device actions.
- Keep model/runtime hardware fit separate from agent authority.

## Quality Evaluation

- Compare compiled/quantized NPU artifacts with the accepted reference model on representative tasks.
- Include hard/edge cases, long inputs, unsupported/fallback graphs, and repeated-use conditions.
- Track correction/retry rate alongside latency and battery.
- Provider profile success is not semantic-quality evidence.

## Practical Fit Outcomes

- `Fits well`: exact device/SoC/Android/runtime/export graph passes complete-workflow support, quality, app memory, latency, battery/thermal, and lifecycle thresholds.
- `Fits conditionally`: requires particular QNN/LiteRT version, partial fallback, smaller model/context, reduced frequency, AC/cool conditions, or another explicit acceptable constraint.
- `Does not fit`: exact route fails graph support, memory, latency, quality, thermals, lifecycle, or stability thresholds.
- `Unknown`: only subgraph/provider evidence exists or exact device/runtime/export lacks current measurement.
- Do not assign fit from NPU TOPS or Snapdragon marketing generation alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when local Snapdragon execution cannot meet model quality/context/latency needs.
- Do not silently send sensitive local input to cloud fallback.
- Compare battery, local setup/compilation, model storage, retries, and correction time against hosted accepted-result economics.
- Keep phone purchasing outside the route.

## Canonical Links

- Link exact models to Model Reference and QAIRT/QNN/LiteRT tooling to canonical software owners when materialized.
- Link Android parent router for cross-SoC routing.
- Keep Snapdragon X Windows evidence in `computers/qualcomm/`.
- Link user scenarios when application/data goal dominates hardware fit.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Qualcomm AI Hub August 2026 profile evidence on Snapdragon 8 Elite/8 Elite Gen 5 Android devices, current QAIRT/QNN direct execution, and current LiteRT + QNN TfLite Delegate profiles.
- Current provider evidence explicitly shows named Android device/SoC/build/runtime/delegate/NPU configurations and separate load/inference/memory metrics. It does not establish complete application, LLM/VLM/diffusion quality or sustainable mobile power behavior.
- Qualcomm AI Hub, QAIRT/QNN, LiteRT delegate, supported devices/SoCs/operators/precisions, Android/OEM firmware, and runtime performance modes are mutable; recheck them before rendering recommendations.
- Exact retail device/runtime/artifact/full-pipeline measurement and accepted-result quality remain the fit authority.

## Validation

- Android Qualcomm and Windows Snapdragon X routes remain separate.
- Direct QNN, LiteRT+QNN delegate, GPU, CPU, and hosted routes are not conflated.
- Exact retail device/SoC/Android/runtime/export is pinned.
- AI Hub subgraph timings are not presented as complete app or generative-model latency.
- HTP/NPU graph coverage and CPU/GPU fallback remain visible.
- Provider burst-mode profiles are not treated as sustained battery/thermal evidence.
- App memory, startup, Android lifecycle, storage, quality, and sustained thermal behavior are measured.
- NPU TOPS/load success do not replace accepted-result fit.
- Hardware purchasing remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
