# Documentation Requirements

## Route Fit

- Cover deeply embedded NXP MCU/crossover-MCU inference where MCUXpresso/eIQ and an Arm CPU, DSP, or eIQ Neutron NPU are the intended local execution path.
- Prioritize current MCX N and i.MX RT-class routes such as MCX N94x/N54x and i.MX RT700 where current first-party eIQ Neutron NPU enablement exists.
- Require exact MCU/SoC, CPU/DSP/NPU target, internal SRAM/TCM, external memory, flash, MCUXpresso SDK version, current eIQ/Neutron software version, model/export, quantization, operator coverage, firmware/memory footprint, real-time deadline, and power state before assigning fit.
- Keep Linux-capable i.MX application processors such as i.MX 8/9-class deployments in the more appropriate SBC/server/embedded-Linux hardware route when the system no longer behaves like a deeply constrained MCU.
- Keep hardware purchasing outside this route.

## eIQ Is an Ecosystem, Not One Runtime

- Do not use `eIQ` as a single compatibility label.
- NXP eIQ spans model-conversion/quantization tools, TensorFlow Lite Micro/other inference engines, MCUXpresso middleware/examples, DSP/CPU paths, and eIQ Neutron NPU-specific compiler/runtime components.
- Pin the exact execution path and target device.
- A model running through eIQ/TFLite on CPU does not prove Neutron acceleration.
- A Neutron-supported model on one target does not prove support on another NXP MCU/NPU generation.

## Current Tooling Lifecycle

- Treat the former monolithic `eIQ Toolkit` as legacy rather than current authority.
- Current NXP FAQ states that tools formerly bundled in eIQ Toolkit are now released as standalone packages and eIQ Toolkit itself stopped receiving updates after v1.17 in Q3 2025.
- Use the current eIQ AI Toolkit/standalone conversion tools, eIQ Neutron SDK, MCUXpresso SDK middleware, and current Learning Hub documentation as the active software boundary.
- Preserve exact tool versions because operator support, conversion, profiling, and NPU libraries evolve independently.
- Do not cite old eIQ Toolkit screenshots/version assumptions as current deployment behavior.

## Current Neutron SDK Boundary

- Current August 2026 NXP documentation identifies **eIQ Neutron SDK 3.2.1** as the current Neutron software release for MCU projects.
- The tool formerly named `Neutron Converter` was renamed **Neutron Compiler** in August 2026; functionality remains the target-specific model-conversion step.
- Preserve the compiler/SDK version and matching target runtime libraries.
- Do not mix older `neutron-converter` command/document names with current compiler/version claims without labeling them as earlier terminology.
- Recheck the current Neutron SDK before rendering current recommendations.

## Neutron NPU Route Requires Specialized Conversion

- For current Neutron-NPU targets, start from a supported quantized TensorFlow Lite model and run the current Neutron Compiler/eIQ AI Toolkit conversion for the exact target.
- Current NXP Learning Hub explicitly documents an additional Neutron-specific conversion step for MCX N, i.MX RT700, i.MX95/i.MX943-class Neutron devices.
- The resulting target-specific TFLite/Neutron representation is part of compatibility.
- Do not infer that a standard `.tflite` file automatically executes on the Neutron NPU.
- Keep conversion target and generated artifact tied to the exact device family.

## Exact Neutron Target

- Record the current Neutron target rather than only `NXP NPU`.
- Current Neutron Compiler supports target-specific conversion and exposes target selection; conversion/scheduling can differ according to NPU memory/core architecture.
- MCX N and i.MX RT700 use the embedded Neutron NPU family, while newer Linux application processors can use different Neutron/Neutron-S flows.
- Keep Linux Neutron-S/i.MX95/943 application-processor behavior outside this MCU route unless the taxonomy explicitly routes that system here.
- Do not transfer compiler output, operator support, memory, or performance between Neutron and Neutron-S.

## Current MCX N Boundary

- Current MCX N94/N54-class devices include Cortex-M33 cores, on-chip accelerators, flash/SRAM, and an integrated eIQ Neutron NPU.
- Current NXP product documentation describes the MCX N Neutron N1-16 NPU as a low-power embedded accelerator and current MCUXpresso/eIQ lab guides provide target-specific conversion/runtime workflows.
- Record the exact MCX N part because memory/peripherals/core count and target support differ across N94/N54/N53/N52/N24 variants.
- Do not transfer an N947 benchmark to another MCX N part without exact model/runtime/memory evidence.
- Keep NPU throughput marketing as hardware capability only, not model/application latency.

## Current i.MX RT700 Boundary

- Current i.MX RT700 is a crossover MCU with Cortex-M33 cores, HiFi DSPs, integrated eIQ Neutron NPU, and substantial but still embedded-class onboard SRAM.
- Current NXP app notes/lab guides provide exact RT700 Neutron conversion/runtime/performance workflows.
- Treat RT700 CPU, DSP, and Neutron NPU as distinct execution resources.
- Record SRAM placement/external memory, model/operator partitioning, audio/sensor workload, and power domain use.
- Do not extrapolate MCX N memory/performance from shared Neutron branding.

## CPU, DSP, and NPU Are Separate Routes

- Record which model stages execute on Cortex-M, HiFi DSP/PowerQUAD/other DSP accelerator, Neutron NPU, or CPU fallback.
- Do not describe a heterogeneous pipeline as `NPU inference` when preprocessing/postprocessing/unsupported layers dominate elsewhere.
- Include inter-core/accelerator data movement and synchronization in deadline measurements.
- A model supported by TFLite Micro on Cortex-M does not prove Neutron compatibility.
- Preserve `Unknown` for unmeasured placement or fallback.

## TensorFlow Lite Micro Route

- Treat TFLite Micro/MCUXpresso eIQ middleware as a current CPU/accelerator integration route for supported embedded models.
- Current MCUXpresso SDK repositories include eIQ examples/middleware and NXP-maintained downstream Neutron integration components.
- Record the exact TFLM snapshot, resolver/operator set, tensor arena, target kernels, Neutron custom/delegate path where used, and MCUXpresso release.
- Do not infer upstream TFLite Micro support means the NXP-specific Neutron backend is present in every TFLM build.
- Measure full firmware memory and latency.

## Model Format and Conversion Chain

- Preserve source model/framework/revision, PyTorch→ONNX or TensorFlow source, quantized TFLite intermediate, Neutron-specific conversion where used, quantization method/calibration, target, and final application asset.
- Current eIQ Learning Hub supports conversion/quantization pipelines from TensorFlow or PyTorch/ONNX toward quantized TFLite and then target-specific NPU formats.
- Do not equate source framework compatibility with target deployment compatibility.
- Keep every conversion stage reproducible and versioned.
- Validate semantics after each material quantization/target-lowering step.

## Quantization Is Required Evidence

- Current NXP Neutron guidance starts from quantized TFLite and the NPU supports target-specific low-precision execution.
- Record full-int8, int8-weight/int16-activation, or another supported scheme, calibration dataset, and quality delta.
- Current NXP documentation notes that higher-precision activation modes can improve accuracy while increasing latency/memory and reducing supported-kernel coverage.
- Do not pick precision only from model size or nominal NPU throughput.
- Re-evaluate the target operator matrix for the exact precision.

## Operator Support Is Device Specific

- Use current MCUXpresso/eIQ documentation for the exact Neutron target's supported TFLite operators and constraints.
- Do not infer operator support from generic TFLite availability.
- Preserve unsupported operators, fallback, tensor layouts/shapes, and memory implications.
- A successful conversion with unexpected CPU execution can fail a real-time deadline.
- Keep unlisted/unverified model graphs `Unknown`.

## On-Device Profiling

- Use actual target profiling after conversion.
- Current eIQ AI Hub on-device profiling can measure real device latency, layer-by-layer execution, memory-bandwidth/platform bottlenecks, and compare current NXP targets.
- Current boardfarm examples include MCX N94x/N54x and i.MX RT700 Neutron devices.
- Treat remote boardfarm results as target evidence and reproduce on the final board/firmware when power/memory/peripherals differ.
- Do not substitute simulator/compiler estimates for actual deadline proof.

## eIQ AI Hub Model Boundary

- Current AI Hub on-device profiling accepts TFLite model inputs for current boardfarm profiling; exact target conversion can occur through the NXP flow.
- Preserve exact source/quantized model, target board, runtime/SDK version, and profiling configuration.
- Do not treat an AI Hub-compatible model as automatically production-ready firmware.
- Include firmware integration, sensor pipeline, power, and task quality separately.

## Internal SRAM, External Memory, and Flash

- Treat code/flash, internal SRAM/TCM, external PSRAM/SDRAM, tensor arena, NPU workspace, stacks, DMA buffers, sensor/audio/image buffers, and application data separately.
- Do not add flash capacity to inference RAM or assume external memory has internal-SRAM latency/determinism.
- Current MCX N and RT700 memory architectures differ materially; preserve target-specific placement.
- Measure worst-case memory high-water marks under the full firmware.
- Keep headroom for OTA, RTOS, communications, security, and control tasks.

## Firmware + Model Are One Resource Budget

- Include RTOS, networking, crypto, filesystem, sensor drivers, displays, audio, ML middleware, and update/rollback in flash/RAM planning.
- A model that fits an isolated demo can fail once the actual product firmware is linked.
- Track map-file/heap/stack/tensor-arena usage and NPU allocations.
- Avoid using every byte of internal RAM for model tensors when real-time tasks require deterministic buffers.

## Real-Time Deadline

- Define sensor/frame/audio/control deadline before model selection.
- Measure p95/p99/worst-case end-to-end latency including preprocessing, NPU/CPU/DSP inference, postprocessing, RTOS scheduling, DMA/interrupts, and communication.
- Do not use average model invoke time alone for safety/control decisions.
- Preserve deadline margin under worst expected concurrent firmware load.
- Keep deterministic control/safety loops independent from uncertain neural inference where required.

## Sensor and Vision Pipelines

- Include camera/sensor acquisition, resize/normalization/features, inference, postprocessing, and actuation/network/reporting.
- Current NXP examples such as MCX N face detection or RT700 wearable/smart-device demos are candidate pipeline evidence only.
- Measure the final sensor configuration and domain dataset.
- Do not infer end-to-end FPS from NPU-only speedup claims.

## Audio/DSP Pipelines

- RT700-class devices include DSPs intended for audio/sensor work alongside the NPU.
- Decide whether DSP preprocessing/features, CPU orchestration, and NPU model inference are partitioned intentionally.
- Measure complete stream latency/power rather than one accelerator stage.
- Do not reserve every core/accelerator for AI if the product requires continuous audio/control tasks.

## Power and Duty Cycle

- Embedded fit includes energy per inference, awake time, sleep state, accelerator power-domain behavior, and sensor/radio duty cycle.
- Current NXP product positioning emphasizes lower active time/power from Neutron acceleration; verify this on the actual model/firmware.
- Do not convert vendor CPU-vs-NPU speedup into battery-life improvement without whole-device measurement.
- Record clock/power modes with every benchmark.

## Thermal and Industrial Limits

- Measure sustained behavior for sealed, wearable, industrial, or high-temperature environments when relevant.
- Include specified operating-temperature range, clock/power policy, and enclosure thermal design.
- A lab EVK result does not prove deployment reliability at the target ambient/voltage conditions.

## Current Model Examples Are Eligibility Evidence

- Use MCUXpresso/eIQ model/example applications as current compatibility anchors for exact tasks such as face/person/audio/classification.
- Do not infer a larger/sibling architecture fits because one MobileNet or compact CNN example runs.
- Preserve exact model input, quantization, toolchain, board, and quality metric.
- Model-zoo/example availability is not a permanent ranking.

## LLM/Generative Boundary

- Keep general LLM/VLM-scale inference outside the current MCX N/i.MX RT700 MCU route unless current NXP tooling explicitly supports a materially different generative artifact and target.
- Neutron NPU support for matrix/neural workloads and a high relative speedup does not imply autoregressive transformer/context support.
- Escalate generative/high-context workloads to an NXP application processor, SBC/server/gateway, or hosted model when needed.
- Do not infer generative capability from `AI`/NPU branding.

## ExecuTorch and Other New Runtimes

- Current MCUXpresso eIQ middleware includes evolving ExecuTorch-related components; treat them as a separate runtime path only when the exact target/backend/model is currently supported.
- Do not merge future/experimental ExecuTorch backend support into the Neutron TFLite route.
- Record exact runtime/backend/partitioning and keep unsupported current MCU combinations `Unknown`.

## Offline and Security

- Embedded NXP inference can run offline once firmware/model/runtime assets are local.
- Test network-denied operation when offline behavior is required.
- Preserve secure boot/update/signature/EdgeLock or other platform security requirements separately from model quality.
- Keep sensitive sensor/model data out of logs and external telemetry where policy requires it.

## Physical Actions and Safety

- Neural outputs affecting motors, locks, medical/wearable alerts, industrial control, or safety functions require deterministic policy, thresholds, sensor validation, fail-safe state, and human/control-system oversight where appropriate.
- A local NPU result does not authorize a physical action by itself.
- Treat incoming sensor/network data as untrusted when AI output can cause side effects.
- Define degraded operation when inference or NPU runtime fails.

## Model Quality

- Evaluate the target-domain model before and after TFLite quantization and Neutron conversion.
- Track class-level precision/recall, false-positive/false-negative cost, or task-specific error rather than only benchmark accuracy.
- Include sensor/environment variation and hard negatives.
- Re-run after quantizer/compiler/SDK/model updates.

## Practical Fit Outcomes

- `Fits well`: exact NXP MCU/MCUXpresso/eIQ runtime/model/quantization/Neutron target passes operator support, accepted quality, flash/RAM budget, p95/worst-case deadline, power, and full-firmware requirements.
- `Fits conditionally`: requires NPU-specific target conversion, smaller model/input, external memory with acceptable latency, CPU/DSP partitioning, lower rate, or another explicit acceptable constraint.
- `Does not fit`: exact route fails operator/conversion support, memory/flash, deadline, quality, power, or firmware integration.
- `Unknown`: exact MCU/runtime/model/toolchain combination lacks current support or measurement.
- Do not assign fit from GOPS/TOPS, NPU presence, flash/RAM capacity, or a demo model alone.

## Escalation

- Move Linux-capable i.MX application processors to the appropriate embedded-Linux/SBC/server route when Linux/container/large-memory behavior dominates.
- Move general generative/high-context workloads to a gateway/SBC/server/hosted route.
- Keep compact sensing/preprocessing/local decisions on the MCU where they meet the deadline/power/privacy objective.
- Do not turn this page into hardware purchasing advice.

## Canonical Links

- Link exact model facts to Model Reference when reusable.
- Link MCUXpresso SDK, eIQ AI Toolkit, eIQ Neutron SDK/compiler, TFLite Micro, and ExecuTorch software to canonical owners when materialized.
- Link embedded/IoT/safety user scenarios when application constraints dominate hardware fit.
- Keep i.MX Linux application-processor deployment in the applicable non-MCU hardware route.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party NXP eIQ FAQ/Learning Hub, eIQ Neutron SDK 3.2.1 migration guidance, MCUXpresso eIQ middleware/examples, current MCX N and i.MX RT700 product/application documentation, and current eIQ AI Hub on-device profiling guidance.
- Current evidence establishes the post-v1.17 standalone eIQ tool lifecycle, August 2026 Neutron Compiler naming/current SDK, target-specific quantized-TFLite→Neutron conversion, current MCX N/RT700 Neutron routes, and on-device profiling. It does not establish a general MCU LLM/VLM route.
- MCUXpresso SDK/eIQ middleware, eIQ AI Toolkit/Neutron SDK, Neutron target/operator support, model conversion, boardfarm availability, and MCU product revisions are mutable; recheck them before rendering recommendations.
- Exact target/toolchain/model/memory/deadline/full-firmware measurement and accepted-result quality remain the fit authority.

## Validation

- Exact MCU/SoC, CPU/DSP/NPU target, MCUXpresso/eIQ/Neutron versions, model format/quantization, memory, flash, and deadline are pinned.
- eIQ branding does not collapse materially different device/runtime classes.
- Legacy monolithic eIQ Toolkit is not presented as the current actively updated tool bundle.
- Neutron Compiler target conversion is part of NPU compatibility.
- Standard TFLite/source model support is not equated with Neutron execution.
- CPU/DSP/NPU placement, operator coverage, internal/external memory, firmware overhead, real-time/power, and post-conversion quality are represented.
- Linux i.MX application processors are not silently mixed into the deeply constrained MCU route.
- NPU throughput/speedup is not misrepresented as generative-model or whole-application fit.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
