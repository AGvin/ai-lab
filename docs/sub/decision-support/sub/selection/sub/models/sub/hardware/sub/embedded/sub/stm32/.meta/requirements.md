# Documentation Requirements

## Route Fit

- Cover STM32 MCU inference where Cortex-M CPU/Helium/DSP kernels or an ST Neural-ART accelerator is the intended local route through current ST Edge AI/STM32Cube.AI tooling.
- Require exact STM32 part/family, CPU/NPU presence, internal SRAM/TCM, external RAM, flash/external flash, ST Edge AI Core/STM32Cube.AI version, source/export, quantization, operator coverage, memory placement, firmware footprint, real-time deadline, and power state before assigning fit.
- Treat STM32N6 Neural-ART parts and ordinary STM32 CPU inference as distinct execution routes.
- Keep Linux-capable STM32MP application processors outside this deeply constrained MCU route when Linux/container/large-memory behavior dominates.
- Keep hardware purchasing outside this route.

## Exact Part Before Family Branding

- Do not infer Neural-ART presence from `STM32N6` alone.
- Current ST product data distinguishes STM32N6x7-class parts with the Neural-ART accelerator from N6x5-class variants without the NPU.
- Record the exact part number, not only `N6`, `H7`, `U5`, or another family name.
- Do not transfer NPU model support/performance from N6x7 to an N6 part without Neural-ART.
- Route CPU-only parts through the CPU/Helium/ST Edge AI path for the exact model.

## Current ST Edge AI Tool Boundary

- Treat current **ST Edge AI Core** as the active model analysis/optimization/code-generation tool in the current STM32 AI Model Zoo flow.
- Current STM32 AI Model Zoo 4.1.x supports STEdgeAI Core v4.0.0; older model-zoo releases used earlier STEdgeAI/STM32Cube.AI versions.
- Pin exact ST Edge AI Core/model-zoo/tool release because supported networks, operators, quantization, NPU mapping, generated runtime, memory placement, and deployment code change.
- Do not apply an older STM32Cube.AI validation report to a current STEdgeAI Core-generated application without revalidation.
- Preserve generated network/runtime configuration with firmware source control.

## Current Model Zoo Is Candidate Evidence

- Use the official STM32 AI Model Zoo and Model Zoo Services as current candidate/compatibility evidence for named use cases and targets.
- Current model zoo workflows support PyTorch, TensorFlow, and ONNX-oriented training/evaluation/conversion paths and deployment to named STM32 targets.
- Current releases include current N6 vision/audio workflows and models such as YOLO11/YOLO26/ST-YOLO variants and other application-oriented networks.
- Do not treat a model listed in the zoo as a universal recommendation or proof that every input size/variant/checkpoint fits the MCU.
- Record exact model/configuration, target board/part, quantization, ST Edge AI Core version, and published metric when using zoo evidence.

## Source Model to Deployable Firmware

- Preserve source framework/model/revision, exported TFLite/ONNX/ONNX-QDQ/PyTorch-related representation, input shapes, preprocessing, postprocessing, quantization, ST Edge AI Core generation settings, target part, generated network blob/code, and application firmware.
- Do not treat a source checkpoint as directly runnable STM32 firmware.
- Keep conversion/operator/memory warnings visible.
- Validate generated-model semantics/task quality after quantization and deployment.
- Version source model and generated firmware artifacts together.

## Neural-ART Route

- Treat the ST Neural-ART accelerator as an N6x7-specific model/operator execution target, not generic STM32 NPU capacity.
- Current STM32N6x7 parts expose a Neural-ART accelerator up to 600 GOPS alongside Cortex-M55/Helium and dedicated streaming/cache features.
- Do not infer model compatibility or expected latency from 600 GOPS.
- Require ST Edge AI Core to successfully map/compile the exact quantized graph to the target Neural-ART hardware.
- Preserve unsupported/fallback CPU stages and data movement.

## Cortex-M55 / Helium Route

- STM32N6 also includes a high-performance Cortex-M55 with Helium/MVE vector processing; other STM32 families use their own Cortex-M/DSP capabilities.
- Treat CPU inference as a separate measured route even on N6x7.
- Record generated CPU kernels, CMSIS-NN/Helium/DSP use where applicable, clock, cache/TCM placement, threads/RTOS scheduling, and real-time workload.
- Do not label CPU execution as NPU fit merely because the part includes Neural-ART.
- Compare CPU vs NPU only using the same deployed model/quality where possible.

## NPU + CPU Pipeline

- Record which layers/stages run on Neural-ART versus Cortex-M55/other CPU code.
- Include preprocessing, image/audio transforms, postprocessing/NMS, sensor drivers, UI/communications, and any unsupported graph stages.
- Measure complete sensor-to-result latency rather than only NPU execution time.
- A high NPU utilization number does not prove the firmware meets the real-time deadline.
- Keep partitioning/fallback explicit in the generated-network report and benchmark record.

## Current N6 Memory Architecture

- Current STM32N6 provides 4.2 MB contiguous SRAM plus TCM and external-memory interfaces; Neural-ART also has dataflow/cache mechanisms to reduce external-memory traffic.
- Treat internal SRAM/TCM, NPU cache/workspaces, external PSRAM/SDRAM, flash, external flash, frame buffers, model weights, activation buffers, and application memory separately.
- Do not call all memory NPU RAM or assume external memory has internal-SRAM latency/determinism.
- Preserve ST Edge AI Core memory-placement/optimization mode and actual peak firmware memory.
- Measure external-memory bandwidth/cache effects under the complete model.

## STM32N6 Has No General Internal Program Flash

- Current STM32N6 application documentation states that persistent firmware is stored in external flash; development can load into SRAM but that state is lost on power-off.
- Include external flash, boot flow, model/network blob, firmware, secure boot, OTA/rollback image, and temporary update space in deployment fit.
- Do not treat an SRAM-loaded dev-session demonstration as a production boot/storage solution.
- Preserve boot mode and external-memory part/configuration with performance/reliability evidence.

## ST Edge AI Optimization Modes

- Current Model Zoo deployment configuration exposes ST Edge AI optimization choices such as balanced/time/RAM for supported targets.
- Record the selected optimization mode and generated memory/performance report.
- Do not assume the fastest mode also fits SRAM/external-memory constraints or power budget.
- Compare application quality and real latency after deployment, not only host-side generation estimates.
- Re-run generation after tool/model changes.

## Quantization Is Part of Compatibility

- Current STM32N6 Model Zoo deployment examples use quantized TFLite or ONNX QDQ models for Neural-ART deployment.
- Record exact quantization scheme, calibration dataset, model precision, any per-layer exceptions, and source-to-quantized accuracy delta.
- Do not assume a float source model maps efficiently or at all to the NPU.
- Do not choose INT8/other quantization solely for memory/performance if accepted-result quality falls below threshold.
- Validate on representative target-domain data after target deployment.

## Operator and Tensor Constraints

- Require current ST Edge AI Core compatibility analysis for the exact target/model.
- Preserve unsupported operators, shape/layout restrictions, fallback, generated custom code, and preprocessing/postprocessing assumptions.
- A valid TFLite/ONNX model is not automatically Neural-ART compatible.
- Keep unverified architecture/operator combinations `Unknown`.
- Do not generalize from YOLO/image examples to arbitrary transformers or generative architectures.

## On-Device Evaluation

- Use physical-target evaluation, not only host emulation.
- Current STM32 AI Model Zoo services support `stedgeai_n6` on-device evaluation/prediction on STM32N6570-DK-class targets in addition to host and emulated STM32-kernel modes.
- Compare host source-model quality, STEdgeAI host/emulated quality, and on-device target quality when conversion/quantization can change results.
- Preserve test set, tool/board/firmware versions, and metrics.
- Do not treat successful firmware flashing as model-quality validation.

## Developer Kit vs Final Product

- Current N6 examples target STM32N6570-DK and current NUCLEO-N657X0-Q development hardware.
- Treat dev-kit camera/external RAM/flash/power/cooling as reference configuration only.
- Record the final product's exact part, external memory, camera/sensor, PCB routing, clock/power, and enclosure.
- Do not transfer a dev-kit benchmark directly to a custom board without measurement.

## Vision Pipeline

- Current STM32N6 is strongly enabled for real-time vision with camera/ISP/media hardware and Neural-ART.
- Include sensor capture, ISP, resize/color conversion, tensor preparation, NPU/CPU inference, NMS/postprocessing, display/USB/network/storage, and frame buffers.
- Measure frame-to-result latency, sustained FPS, dropped frames, and CPU load.
- Do not quote model-zoo NPU performance as complete camera pipeline FPS.
- Validate false positives/false negatives on the target camera/environment.

## Object Detection and Segmentation

- Current Model Zoo N6 workflows support object detection, image classification, segmentation, face/pose/ReID and related current use cases.
- Preserve exact input resolution, postprocessing variant, class count, dataset, and quantized model.
- YOLO family/version support is not transferable to every sibling model.
- Include postprocessing cost and memory.
- Model Zoo support is eligibility evidence, not application acceptance.

## Audio Pipeline

- Current N6 model/application ecosystem also supports audio event detection and speech-enhancement-style embedded workloads.
- Include ADC/PDM/I2S capture, windowing/features, model inference, output processing, buffering, and real-time audio deadlines.
- Do not infer general ASR/LLM speech capability from compact audio-model support.
- Preserve sample rate/window/model and power duty cycle.

## Generative / LLM Boundary

- Do not present current Neural-ART/STM32N6 support as a general-purpose local LLM/VLM route solely from 600 GOPS or large-model marketing language.
- Current first-party N6 model-zoo deployment evidence is centered on embedded vision/audio/neural workloads and target-specific quantized models.
- Require explicit current ST tool/runtime/model evidence before adding any generative architecture to this MCU route.
- Escalate high-context autoregressive LLM/VLM workloads to a larger MPU/SBC/server/hosted route when appropriate.
- Keep future support `Unknown` until measured.

## Model Size vs External Memory

- External memory can allow larger weights/activations but does not make every graph compatible or fast.
- Preserve model-weight placement, activation placement, cache behavior, bus bandwidth, and latency.
- Current N6 application updates can place some generated controller/blob content in external flash to accommodate larger supported models; treat this as storage/memory engineering, not unlimited model-size support.
- Do not turn external PSRAM/flash capacity into a parameter-count tier.

## Real-Time Deadline

- Define the actual frame/audio/control deadline before model selection.
- Measure p50/p95/p99/worst-case complete latency under concurrent RTOS/peripheral work.
- Include sensor/ISP/DMA, inference, postprocessing, communication, and display/control outputs.
- Keep deterministic safety/control loops independent from uncertain neural output where consequence requires it.
- A model that meets average FPS but misses worst-case deadline can fail the application.

## Power and Duty Cycle

- Measure whole-device energy per inference/frame/audio window and duty cycle.
- NPU efficiency claims such as TOPS/W are hardware capability evidence, not product battery-life proof.
- Record clocks/power mode, external memory, camera/display/radio activity, and sleep behavior.
- Compare CPU vs Neural-ART on actual accepted application outcomes.

## Thermal and Environment

- Measure sustained target behavior in the final enclosure/ambient where high-frequency M55/NPU/media pipelines run continuously.
- Include throttling/clock/power policies and external-memory thermal behavior where relevant.
- A dev-kit lab run does not prove industrial/sealed deployment performance.

## Firmware/Boot/OTA Budget

- Include bootloader, external-flash firmware, model network/blob, secure-boot metadata, filesystem, certificates, rollback image, logs, and update headroom.
- Version generated model/runtime together with firmware.
- Ensure power-loss-safe update/rollback for products that update models remotely.
- Do not ship multiple large model variants without a storage/update reason.

## Security and Model Assets

- Preserve secure boot, signed firmware/model assets, external-memory encryption where required, TrustZone/MPU boundaries, and access to model/sensor data.
- Model quality and hardware support do not replace product security requirements.
- Keep secrets out of model buffers/logging.
- Validate external model/update provenance.

## Physical Actions and Safety

- Neural outputs controlling motors, alarms, access, industrial machines, or medical/consumer safety functions require deterministic thresholds, validation, fail-safe logic, and safety interlocks.
- A Neural-ART inference result does not authorize a physical action by itself.
- Treat sensor/network inputs as potentially adversarial where actions have side effects.
- Define degraded/manual behavior when model/runtime or camera/sensor fails.

## Quality Evaluation

- Use target-domain test data and compare source, quantized/generated, and on-device results.
- Track class-level precision/recall/mAP/IoU/audio metrics appropriate to the task.
- Include hard negatives, sensor/environment variation, and calibration drift.
- Re-run after model, ST Edge AI Core, BSP/application code, quantization, or preprocessing changes.

## Practical Fit Outcomes

- `Fits well`: exact STM32 part/ST Edge AI Core/runtime/model/quantization/memory placement passes operator support, accepted quality, SRAM/external-memory/flash budget, p95/worst-case deadline, power, and complete firmware requirements.
- `Fits conditionally`: requires Neural-ART-capable N6x7 part, smaller input/model, aggressive quantization, external-memory placement, CPU/NPU partitioning, lower frame/sample rate, or another explicit acceptable constraint.
- `Does not fit`: exact route fails part/NPU availability, conversion/operator mapping, memory/storage, deadline, quality, power, or firmware integration.
- `Unknown`: exact target/tool/model/runtime behavior lacks current support or measurement.
- Do not assign fit from 600 GOPS, MCU family name, RAM/flash size, or a model-zoo listing alone.

## Escalation

- Use a larger STM32MP/application processor, SBC/gateway/server, or hosted route when the workload exceeds current MCU memory/context/operator/latency capability.
- Keep bounded vision/audio/sensor inference on STM32 when it meets real-time/power/privacy requirements.
- Do not turn this route into hardware purchasing guidance.

## Canonical Links

- Link exact model facts to Model Reference where reusable.
- Link ST Edge AI Core/STM32Cube.AI, Model Zoo, STM32CubeIDE/Programmer, CMSIS-NN, and N6 application software to canonical software owners when materialized.
- Link embedded/vision/industrial user scenarios when application requirements dominate hardware fit.
- Keep STM32MP/Linux deployments in the applicable non-MCU hardware route.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party STM32N6 product/datasheet material, current STM32 AI Model Zoo/Model Zoo Services 4.1.x with STEdgeAI Core v4.0.0, current N6 deployment/on-device-evaluation documentation, and current 2026 N6 application release notes.
- Current evidence establishes an exact-part split between Neural-ART-capable N6x7 and non-NPU N6 variants, 4.2 MB MCU SRAM plus external-memory/flash deployment, current quantized TFLite/ONNX-QDQ Neural-ART flows, target evaluation, and current vision/audio model-zoo support. It does not establish a general-purpose MCU LLM/VLM route.
- STM32 part matrix, ST Edge AI Core/model zoo, supported models/operators/quantization, N6 BSP/application code, external-memory placement, and tooling are mutable; recheck them before rendering recommendations.
- Exact part/tool/model/memory/deadline/full-firmware measurement and accepted-result quality remain the fit authority.

## Validation

- Exact STM32 part/CPU/NPU presence, memory/storage, ST Edge AI Core version, model/export/quantization, and deadline are pinned.
- STM32N6 family branding is not used to assume Neural-ART on every part.
- CPU/Helium and Neural-ART execution are not conflated.
- Valid TFLite/ONNX source is not treated as NPU compatibility without current target analysis/generation.
- Internal SRAM/TCM, external RAM, NPU cache/workspaces, external flash, firmware, and sensor buffers remain separate resources.
- 600 GOPS/model-zoo availability do not replace end-to-end application quality/latency/power evidence.
- Dev-kit/on-device evaluation does not replace final-board validation.
- Current MCU route is not misrepresented as generic LLM-scale inference.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
