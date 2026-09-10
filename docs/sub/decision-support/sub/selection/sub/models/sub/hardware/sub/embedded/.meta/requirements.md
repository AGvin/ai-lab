# Documentation Requirements

## Router Role

- Cover MCU/deeply constrained embedded inference where SRAM/TCM/PSRAM/flash, conversion toolchains, operator coverage, real-time deadlines, power, firmware integration, and accelerator-specific runtimes define a model universe distinct from Linux SBC/server inference.
- Route current selected ecosystems to `esp32/`, `nxp/`, and `stm32/` because each has a materially different first-party deployment stack and hardware/runtime boundary.
- Do not introduce a generic `arm/`, `npu/`, or `edge/` sibling here: CPU ISA, accelerator marketing, and deployment context do not identify the complete embedded model route.
- Keep this page focused on cross-MCU selection constraints and delegate exact chip/tool/model compatibility to the children.
- Keep hardware purchasing outside this router.

## Deeply Constrained Embedded Boundary

- Use this branch when firmware-level constraints dominate: deterministic boot, static/controlled memory, MCU-class storage, real-time deadlines, low-power operation, sensor pipelines, and tightly coupled model binaries.
- Move Linux-capable application processors, SBCs, gateways, and containerized edge systems to the applicable `single-board/`, `computers/`, or `servers/` route when Linux/runtime/package behavior becomes the primary compatibility boundary.
- Do not force an i.MX/STM32/other vendor product into this branch solely because its producer also makes MCUs.
- Treat current ESP32, NXP MCU/crossover-MCU, and STM32 MCU routes as compact neural-inference routes unless a child has current explicit evidence for a materially different generative capability.
- Do not transfer desktop/SBC LLM assumptions into MCU selection.

## Exact Target Before Model

- Require exact chip/part number, CPU/DSP/NPU/instruction target, internal SRAM/TCM, external RAM/PSRAM, flash/external flash, clock/power state, RTOS/bare-metal environment, current toolchain/runtime, source/export, quantization, input shape, firmware footprint, and deadline before assigning fit.
- Family branding such as `ESP32`, `STM32N6`, or `eIQ` is not sufficient compatibility evidence.
- Preserve exact accelerator presence because related parts within one family can expose materially different CPU/NPU/vector capabilities.
- Keep unsupported or unmeasured target/runtime/model combinations `Unknown`.

## Toolchain-Specific Artifact Is Part of Compatibility

- Treat source model and deployable firmware artifact as different lifecycle objects.
- Current child routes demonstrate materially different conversion paths:
  - ESP32 uses current Espressif ESP-DL/ESP-TFLite-Micro/ESP-NN paths with target-specific kernels/operator matrices;
  - NXP MCU routes use current MCUXpresso/eIQ components and, for Neutron NPU targets, target-specific Neutron compilation;
  - STM32 uses current ST Edge AI Core/STM32Cube.AI flows and Neural-ART-specific mapping where applicable.
- Preserve source model/revision, export format/opset, converter/compiler/tool version, quantization/calibration, target chip, generated model/network artifact, and firmware integration.
- Do not equate valid ONNX/TFLite/PyTorch source with successful embedded deployment.
- Conversion/operator/memory warnings remain compatibility evidence and must not be hidden by manual graph simplification.

## CPU, DSP, Vector, and NPU Routes Are Distinct

- Record the actual execution target for every material graph stage.
- A model that runs on MCU CPU does not prove NPU/DSP acceleration.
- NPU support on one part does not imply the same graph/operator/precision support on another generation.
- Preserve CPU fallback/partitioning where a toolchain allows it and include transfer/synchronization overhead in end-to-end latency.
- Do not compare CPU frequency, SIMD/Helium/PIE capability, NPU GOPS/TOPS, and DSP capability as interchangeable performance metrics.

## Memory Hierarchy Is a Hard Constraint

- Account separately for internal SRAM/TCM, external SRAM/PSRAM/SDRAM, accelerator-local cache/workspaces where present, flash/external flash, model constants, tensor arenas, activation buffers, DMA/camera/audio buffers, stacks/heaps, RTOS tasks, and application state.
- Peak tensor/activation memory can dominate compact model deployment even when parameter storage fits flash.
- Do not use nominal RAM/flash size as a model tier.
- Treat external-memory placement as a latency/power/reliability trade-off, not free capacity.
- Preserve headroom for firmware updates, rollback images, logs, certificates, and product features outside AI.

## Static Planning and Determinism

- Prefer deterministic/static memory planning when the current toolchain supports it and the product requires predictable behavior.
- Record dynamic allocation when it cannot be avoided and test fragmentation/exhaustion over long runs.
- Measure worst-case/p95 latency, not only average or one warm invocation.
- Include interrupt load, RTOS scheduling, DMA, networking, storage, sensor acquisition, and concurrent control loops.
- A model that meets average latency but misses the real-time deadline under normal system contention does not fit.

## Input Pipeline Is Part of the Model Route

- Include sensor capture, decode, resize, normalization, feature extraction, audio framing, postprocessing, thresholding, tracking, and actuator/control logic in end-to-end measurements.
- Keep accelerator kernel timing separate from whole-application latency.
- A vendor benchmark for one operator/subgraph or pure inference loop does not establish the product deadline.
- Measure representative sensor rates and input shapes rather than a convenient synthetic input only.

## Quantization and Accuracy

- Treat quantization as both a compatibility/performance transformation and a quality change.
- Record data type, calibration dataset/method, per-tensor/per-channel strategy where relevant, and any tool-specific compression settings.
- Compare source and deployed artifacts on representative target-domain data.
- Do not accept INT8/INT16/other quantization merely because it fits memory or maps to the accelerator.
- Track task-specific metrics, hard negatives, sensor/environment variation, and false-action consequences.

## Model Zoo and Vendor Examples

- Use first-party model zoos/examples as candidate compatibility evidence for named targets/toolchains.
- Preserve exact model/configuration, input shape, quantization, target board/part, tool version, and metric conditions.
- Do not convert a model-zoo listing into a universal recommendation for that MCU family.
- Reproduce the final firmware on the exact target board/product before assigning practical fit.

## Power and Thermal Constraints

- Measure current/power under realistic duty cycle and peripheral load where battery, thermal envelope, or always-on operation matters.
- Include sensor, radio/network, external memory, accelerator, and host CPU/DSP work.
- Distinguish burst inference from continuous inference.
- Treat thermal throttling/voltage/power-state changes as performance conditions, not incidental noise.
- A route that meets latency only in an unsustainable high-power mode is conditional fit.

## Storage, Boot, and Update Lifecycle

- Include model assets in boot-time, flash-layout, secure-update, rollback, and OTA calculations.
- Version model/converter/runtime/firmware together when the deployment artifact is toolchain-coupled.
- Verify cold boot and first inference separately from steady state.
- Define safe rollback when model/tool/runtime updates fail validation.
- Do not create hidden network/model-download dependencies for devices expected to operate offline.

## Security and Supply Chain

- Treat model files, generated blobs, firmware libraries, conversion tools, and update packages as software supply-chain artifacts.
- Preserve source/version/hash/signature provenance where product policy requires it.
- Use secure boot/signed firmware/model assets, TrustZone/MPU/security features, and encrypted external storage where the threat model requires them.
- Keep credentials/keys/sensitive sensor data out of model logs/debug buffers.
- A vendor-supported model is not automatically safe to import into a controlled product build.

## Physical Actions and Safety

- Embedded inference often influences physical devices; model output must not become unbounded actuator authority.
- Use deterministic thresholds, state machines, interlocks, watchdogs, plausibility checks, fail-safe behavior, and human/manual fallback according to application risk.
- Treat sensor/network/model inputs as potentially adversarial where actions have side effects.
- Keep model confidence separate from system authorization.
- Safety certification/qualified validation remains outside model capability claims and must be handled by the appropriate engineering process.

## Practical Routing Outcomes

- `ESP32`: exact Espressif chip + ESP-DL/TFLite-Micro/ESP-NN path owns compatibility and fit.
- `NXP`: exact MCU/crossover-MCU + MCUXpresso/eIQ/Neutron or CPU/DSP path owns compatibility and fit.
- `STM32`: exact STM32 part + ST Edge AI Core/CPU/Neural-ART path owns compatibility and fit.
- `Escalate`: use a Linux-capable application processor, SBC/gateway/server, or hosted route when model/operator/memory/context/deadline requirements exceed the MCU class.
- `Unknown`: exact chip/tool/runtime/model behavior lacks current support or measurement.
- Never choose among routes from TOPS/GOPS, clock frequency, SRAM size, or vendor model-zoo count alone.

## Canonical Links

- Route ecosystem-specific evidence to `esp32/`, `nxp/`, and `stm32/`.
- Link exact reusable model facts to Model Reference and toolchains/runtimes to canonical software owners when materialized.
- Link user scenarios when industrial/IoT/safety/application requirements dominate hardware fit.
- Keep Linux SBC/server application-processor routes outside this MCU router.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after current first-party Espressif ESP-DL/TFLite-Micro, NXP MCUXpresso/eIQ Neutron, and ST Edge AI Core/STM32 child-route passes.
- Current child evidence confirms distinct target-specific conversion/runtime paths, explicit CPU/vector/NPU differences, finite operator/quantization matrices, MCU memory hierarchy constraints, and strong real-time/firmware integration requirements. None establishes a generic MCU-class LLM/VLM route.
- ESP-IDF/ESP-DL, MCUXpresso/eIQ/Neutron, ST Edge AI Core/STM32Cube.AI, supported chips/operators/models, RTOS/BSPs, and model-zoo/tool versions are mutable; recheck child routes before rendering recommendations.
- Exact chip/toolchain/artifact/memory/deadline/full-firmware measurement and accepted-result quality remain the fit authority.

## Validation

- Embedded and Linux SBC/server hardware classes remain separate.
- Direct children remain only `esp32/`, `nxp/`, and `stm32/`.
- Generic `arm/`, `npu/`, or `edge/` does not become a competing compatibility taxonomy.
- Exact chip/accelerator/toolchain/artifact is required; source-model format alone is insufficient.
- CPU/DSP/vector/NPU execution and fallback are not conflated.
- SRAM/TCM/external RAM/flash/tensor arenas/firmware/peripheral buffers remain explicit resources.
- Whole-application p95/worst-case latency, power, quantized quality, update lifecycle, and physical-action safety remain part of fit.
- TOPS/GOPS/clock rate/model-zoo presence do not replace exact compatibility and practical measurement.
- Hardware buying remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
