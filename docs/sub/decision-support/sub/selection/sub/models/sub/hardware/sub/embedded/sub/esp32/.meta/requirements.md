# Documentation Requirements

## Route Fit

- Cover ESP32-family microcontroller inference where Espressif-supported embedded ML stacks such as ESP-DL or ESP-TFLite-Micro are the intended local route.
- Require exact ESP32 SoC, clock/core configuration, internal SRAM, PSRAM/external RAM, flash, ESP-IDF version, ESP-DL/TFLite-Micro/ESP-NN version, source/export, quantization, operator coverage, input dimensions, firmware footprint, real-time deadline, power mode, and accepted task quality before assigning fit.
- Treat ESP32-S3, ESP32-P4, current ESP32-S31, and older ESP32/C/S families as materially different kernel/ISA targets.
- Keep board/chip purchasing outside this route.

## Hard Workload Boundary

- Treat current ESP32 embedded AI as a tiny/embedded neural-inference route for vision, audio, wake-word/speech, OCR, anomaly/classification, sensor models, and similar bounded workloads.
- Do not present current ESP32-family support as an LLM/VLM local inference route merely because a chip is marketed for AI or exposes SIMD/vector instructions.
- Current ESP-DL and ESP-TFLite-Micro evidence centers on compact operator graphs and embedded models, not general-purpose autoregressive language-model serving.
- If a future Espressif platform/toolchain adds a materially different supported generative route, require a separate current evidence pass before changing this boundary.
- Hosted/edge-gateway inference remains a valid escalation when the model cannot fit the MCU class.

## Exact Instruction Class Before Performance

- Current ESP-DL operator support groups targets into materially different execution classes:
  - ESP32 / C2 / C3 / C5 / C6 / S2-class targets without PIE acceleration;
  - ESP32-S3 with PIE V1;
  - ESP32-P4 and current ESP32-S31 with PIE V2.
- Do not transfer S3/P4/S31 optimized-kernel results to an older/no-PIE target.
- Record exact target and compiler/runtime build so the intended optimized kernels are actually enabled.
- Treat clock differences separately from instruction-set/kernel differences.

## Current ESP-DL Boundary

- Treat ESP-DL as Espressif's current first-party deep-learning inference framework for supported ESP chips.
- Current latest tagged ESP-DL 3.x line includes v3.2.0 and current repository updates through 2026 add new models, quantization tooling, static memory planning, dual-core scheduling, and PIE-optimized operators.
- Pin exact ESP-DL release/commit because operator support, memory planning, quantization behavior, target support, and model zoo evolve.
- Do not infer support from a source framework/model name alone; require successful conversion/export into the current ESP-DL deployment form and operator set.

## Current Operator Matrix

- Use the current `operator_support_state.md` for exact target/operator/data-type evidence.
- Current ESP-DL aligns its operator interface with ONNX and recommends ONNX opset 18 for current export, but only a finite tested operator set is implemented and some operators have attribute/shape restrictions.
- Current ESP-DL supports symmetric 8-bit and 16-bit quantized operator paths and also selected float32 paths; target/kernel support still varies.
- Do not equate `ONNX model` with ESP-DL compatibility.
- Keep unsupported attributes/shapes/operators as conversion blockers or explicit fallback work rather than silently simplifying the model.

## Model Conversion Is Part of Fit

- Preserve source model/framework/revision, ONNX export/opset, input shapes/layouts, preprocessing, quantization/calibration, ESP-DL converter/tool version, target chip, generated model assets, and firmware integration.
- Validate numerical/task quality after conversion.
- Do not treat a trained PyTorch/TensorFlow checkpoint as directly runnable firmware.
- Keep conversion warnings and unsupported operator rewrites visible because they can change model semantics/performance.
- Version generated model assets alongside firmware.

## Current Quantization Route

- Treat quantization as mandatory model-quality/performance evidence, not only a size reduction.
- Current ESP-DL provides current PTQ/quantization tooling and 2026 repository updates add automated quantization search/AutoQuant-style workflows.
- Preserve quantization method, calibration dataset, tensor/weight precision, per-layer exceptions, and quality delta.
- Do not infer accuracy retention from INT8/INT16 labels alone.
- Re-run domain evaluation after quantizer/tool changes.

## Static Memory Planning

- Current ESP-DL v3.x includes a static memory planner that places layers according to user-specified internal RAM constraints to improve overall memory/performance behavior.
- Record the configured internal-memory budget and resulting allocation rather than assuming all tensors live in SRAM.
- Include PSRAM/external-memory traffic and cache behavior in latency.
- A model that technically fits only because most tensors spill to slower external memory can miss real-time deadlines.
- Preserve peak memory and planned memory placement with the benchmark.

## Internal SRAM, PSRAM, and Flash Are Distinct

- Measure firmware text/data/stack, model weights, tensor arenas, frame/audio buffers, RTOS tasks, drivers, networking, and application state separately.
- Do not add flash capacity to runtime RAM or treat PSRAM as equal-speed internal SRAM.
- Current operator benchmarks explicitly note PSRAM use and cache effects can materially change performance.
- Include DMA/camera/audio buffer constraints and alignment requirements.
- Keep enough headroom for networking/OTA/logging/sensors rather than benchmarking an inference-only firmware image.

## Dual-Core Scheduling

- Current ESP-DL supports automatic dual-core scheduling for selected compute-heavy operators such as Conv2D/DepthwiseConv2D.
- Do not infer all operators or models scale across both cores.
- Measure real end-to-end model latency and the impact on application/RTOS tasks.
- Preserve task/core affinity and scheduling configuration when deterministic deadlines matter.
- Avoid consuming both cores if it starves communications/control tasks beyond the application budget.

## ESP-NN and TFLite Micro

- Treat `esp-tflite-micro` as a separate current Espressif-supported TensorFlow Lite Micro route integrated with ESP-IDF.
- Current project support follows current ESP-IDF maintenance branches and currently lists ESP-IDF 6.0 and 5.x supported lines while older 5.0-and-below are no longer supported.
- ESP-NN optimized kernels can radically change invoke time compared with generic TFLite-Micro C kernels.
- Current first-party person-detection examples show the same TFLite-Micro workload can change from seconds to tens/hundreds of milliseconds when ESP-NN is enabled, depending on target.
- Preserve exact ESP-IDF, TFLite-Micro snapshot, ESP-NN state, target, clock, and model/input when citing performance.

## Provider Benchmarks Are Exact Configurations

- Current ESP-TFLite-Micro person-detection examples report `invoke()` latency for named targets and explicitly state the CPU frequency and whether ESP-NN is enabled.
- Do not generalize those numbers to another model/input, target clock, camera pipeline, or end-to-end application.
- Current operator-performance tables also note that raw cross-platform timing can be misleading because P4 and S3 run at different clocks and kernel/memory behavior differs.
- Benchmark the deployed firmware/application on the target board.

## ESP32-S3 Route

- Treat ESP32-S3 as a PIE V1-optimized target with mature embedded AI examples and ESP-NN/ESP-DL acceleration.
- Preserve exact PSRAM configuration, CPU frequency, camera/audio peripherals, and kernel build.
- Do not transfer P4/S31 PIE V2 operator speedups or memory behavior to S3.
- Use S3-specific model/examples only as candidate evidence for the same artifact/configuration.

## ESP32-P4 Route

- Treat ESP32-P4 as a newer PIE V2-capable high-performance MCU target with different CPU frequency, memory/IO, and AI-kernel behavior than S3.
- Current ESP-DL and ESP-TFLite-Micro directly support P4 and current examples include person detection and 2026 PP-OCRv6 on-device OCR.
- Current P4 optimization is still model/operator/tool-version specific; current TFLite-Micro documentation explicitly labels some P4 optimization work as ongoing.
- Do not infer all S3 models become faster automatically on P4 without a current P4 build/measurement.

## ESP32-S31 and New Targets

- Current ESP-DL operator matrix includes ESP32-S31 in the PIE V2 target class.
- Treat newly added targets as mutable toolchain support and require current ESP-IDF/ESP-DL board/tool evidence before production recommendations.
- Do not transfer P4 results to S31 solely because both use PIE V2.
- Preserve `Unknown` when board/tooling availability or exact model support is not yet measured.

## Older/No-PIE Targets

- ESP32/C2/C3/C5/C6/S2-class targets can still run supported compact models through C/TFLite-Micro/ESP-DL paths, but current operator documentation identifies substantially slower non-PIE kernels.
- Use them for workloads whose model and real-time deadline actually fit.
- Do not infer S3/P4 capability from shared ESP32 naming.
- Prefer smaller/simpler deterministic ML or hosted/gateway escalation when latency/memory does not meet the objective.

## Vision Pipeline

- Include camera capture, JPEG/RGB conversion, resize/crop/color conversion, tensor preparation, model invoke, postprocessing/NMS, overlay/output, and networking/storage where present.
- Current ESP-WHO/ESP-DL vision examples can guide pipeline construction, but model invoke time is not camera-to-decision latency.
- Measure frame drops, buffer memory, sensor resolution, and sustained FPS.
- Do not use a raw operator/person-detection invoke number as complete vision-system FPS.

## OCR

- Current ESP-DL 2026 updates add PP-OCRv6 OCR on ESP32-P4 across Chinese, English, and dozens of Latin-script languages.
- Treat that as a named current model/example route, not proof that arbitrary OCR/transformer models fit P4/S3.
- Measure complete image preprocessing, detection/recognition stages, vocabulary/model storage, latency, and accuracy on the target document/scene.
- Use deterministic validation when exact identifiers/numbers matter.

## Audio and Wake-Word/Speech Models

- Evaluate audio capture, windowing/features, model inference, postprocessing, and streaming deadlines as a complete pipeline.
- Current TFLite-Micro `micro_speech` examples support multiple ESP targets, but the example model does not establish arbitrary ASR or generative speech capability.
- Preserve sample rate/window/model and continuous buffer memory.
- Do not infer full speech-to-text/LLM support from wake-word/keyword examples.

## Sensor/Time-Series Models

- Small anomaly/classification/regression networks can be strong ESP32 candidates when their exact operator/memory/deadline fits.
- Prefer deterministic preprocessing and compact models over oversized general neural architectures.
- Measure false-positive/false-negative cost and power duty cycle.
- Do not choose a neural model where a simpler signal-processing/rule approach meets the requirement more reliably.

## Real-Time Deadline

- Define the deadline before model selection: sensor sample period, control-loop deadline, frame budget, wake-word response, or batch interval.
- Measure worst-case/p95/p99 latency, not average invoke time only.
- Include RTOS scheduling, interrupts, DMA, radio/network, filesystem, and other tasks.
- Keep safety/control loops deterministic and independent from uncertain neural inference where required.

## Power and Duty Cycle

- Measure active inference power/energy per decision and sleep/idle duty cycle for battery devices.
- A faster PIE/ESP-NN kernel can reduce energy by shortening active time, but verify the complete application.
- Do not extrapolate desktop-style continuous inference assumptions to MCU battery nodes.
- Record CPU frequency/power mode and radio/camera use with the benchmark.

## Thermal Behavior

- MCU thermal limits are usually less dominant than on high-power accelerators, but sustained high-frequency CPU/PSRAM/camera/radio workloads can still affect reliability/enclosure temperature.
- Measure long-run behavior for sealed/industrial/battery devices where relevant.
- Do not use short development-board results as proof of final enclosure reliability.

## Firmware and OTA Budget

- Include inference runtime, model assets, firmware, rollback OTA partition, certificates, filesystem, and logs in flash planning.
- Current ESP-IDF/TFLite-Micro examples explicitly manage flash partition layouts; do not assume all application partitions have unlimited room.
- Preserve model/firmware compatibility and rollback together.
- Avoid shipping multiple large model variants without a storage/OTA reason.

## Offline and Privacy

- Embedded local inference can operate fully offline when all firmware/model assets are local.
- Test without network for every offline claim.
- Networking/telemetry/cloud fallback can change the privacy/security boundary even if model inference is local.
- Keep secrets/keys out of model buffers/logging.

## Security and Actions

- Neural outputs controlling locks, motors, relays, alarms, industrial processes, or other physical actions require deterministic thresholds, state validation, fail-safe logic, and safety interlocks.
- Treat sensor/network payloads as untrusted input when model output can trigger actions.
- A local model classification does not authorize a physical action by itself.
- Define degraded/manual behavior when inference fails or confidence/quality is insufficient.

## Model Quality

- Build a representative target-domain validation set and compare pre/post quantization/conversion performance.
- Track class-level precision/recall or task-specific error, not only overall accuracy.
- Include sensor/camera/environment variation and hard negatives.
- Re-test after ESP-DL/TFLite-Micro/quantization/model changes.

## Practical Fit Outcomes

- `Fits well`: exact ESP chip/ESP-IDF/runtime/model/quantization/memory placement passes accepted quality, flash/RAM budget, p95 deadline, power, and whole-firmware requirements.
- `Fits conditionally`: requires a smaller model/input, PIE/ESP-NN optimized target, PSRAM with acceptable latency, lower sampling/FPS, aggressive duty cycle, or another explicit constraint.
- `Does not fit`: exact route fails operator/export support, memory/flash, deadline, quality, power, or firmware integration.
- `Unknown`: exact chip/runtime/model/toolchain behavior lacks current support or measurement.
- LLM/VLM-style general generative requests remain outside the current supported ESP32 embedded route unless a separately verified future toolchain changes that boundary.

## Escalation

- Escalate larger/generative/high-context workloads to a gateway/SBC/server/hosted route while keeping tiny sensing/preprocessing/local decisions on ESP32 when useful.
- Do not turn this page into advice to buy a different MCU/SBC.
- Compare on-device latency/power/privacy against network/off-device cost where both are valid.

## Canonical Links

- Link exact model facts to Model Reference when a reusable model entity exists.
- Link ESP-DL, ESP-TFLite-Micro, ESP-NN, and ESP-IDF to canonical software owners when materialized.
- Link embedded/IoT user scenarios when application/safety/data constraints dominate hardware fit.
- Keep larger SBC/edge accelerator routes outside this MCU page.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party `espressif/esp-dl` v3.x operator/model/quantization/performance documentation and current `espressif/esp-tflite-micro` ESP-IDF support/examples/performance material.
- Current evidence establishes distinct no-PIE, S3 PIE V1, and P4/S31 PIE V2 execution classes; current 8/16-bit ESP-DL operator matrices; static memory planning; dual-core scheduling; ESP-NN/TFLite-Micro acceleration; and current P4 OCR/vision examples. It does not establish a general LLM/VLM route.
- ESP-IDF, ESP-DL, ESP-TFLite-Micro, ESP-NN, supported targets/operators/models, quantization tools, and model zoo/examples are mutable; recheck them before rendering recommendations.
- Exact chip/toolchain/model/memory/deadline measurement and accepted-result quality remain the fit authority.

## Validation

- Exact ESP32 SoC/PIE class, ESP-IDF/runtime/model/quantization, memory, flash, and deadline are pinned.
- ESP32-S3/P4/S31 results are not transferred to older/no-PIE targets.
- ONNX/TFLite source compatibility is not treated as deployable-model compatibility without current operator/conversion evidence.
- SRAM, PSRAM, flash, tensor arenas, firmware, and peripheral buffers remain separate resource constraints.
- Provider invoke/operator timings are not presented as whole-application latency.
- Quantization quality, p95/worst-case real-time behavior, power, OTA/storage, and safety/action logic are represented.
- Current ESP32 embedded AI is not misrepresented as LLM-scale generative inference.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
