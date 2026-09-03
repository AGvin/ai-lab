# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual building hobby software, electronics, robotics, sensors, cameras, automation, DIY devices, SBC services, or embedded projects where AI can either **assist development** or **execute inside/on behalf of the device**.
- Make that distinction the first decision. `AI helps me build/debug the project` and `the project itself must run inference` are different model-selection routes with different quality, latency, hardware, safety, licensing, and deployment constraints.
- Distinguish this scenario from `ai-enthusiast/`: experimentation with models is secondary here; shipping a working personal project is the outcome.
- Distinguish it from `home-lab-owner/`: persistent service operations are only one possible maker route; many projects are single devices, robots, sensors, prototypes, or intermittent tools.
- Distinguish it from a professional embedded-engineering scenario: this page assumes individual/hobby ownership, flexible process, and personal-risk scale. Employer/customer requirements, formal safety standards, regulated product obligations, or production fleets move the reader into an applicable professional/team/organization route.

## First Split — Development Assistant vs Device Inference

- If the goal is coding, debugging, datasheet explanation, circuit/protocol reasoning, test generation, shell/firmware help, documentation, or design review, select a **development-assistant route** based on accepted code/reasoning quality and project context. The target MCU/SBC does not need to run that assistant.
- If the device must classify sensors, detect objects, transcribe speech, describe images, generate text, reason locally, or operate without a cloud round-trip, select a **deployment model** from the target hardware/runtime/operator/power constraints.
- Allow a hybrid design: a tiny on-device model can handle wake words, anomaly detection, safety gating, or simple vision while a stronger workstation/home-lab/hosted model handles complex reasoning when connectivity and data policy permit it.
- Do not force generative AI onto a microcontroller merely because the project is branded `AI`. Classical algorithms or a small narrow neural model can be the correct solution when the task is deterministic, low-power, low-latency, or memory constrained.

## Development-Assistant Route

- Use a managed assistant or direct coding/API route when it materially improves project throughput. Evaluate it on the maker's actual stack: C/C++, Rust, Python, Arduino/ESP-IDF/Zephyr/RTOS code, Linux scripts, device trees, protocols, build systems, CAD/configuration text, test logs, and datasheets as applicable.
- Prefer current task-specific coding guidance for exact model ranking; do not freeze one coding model in this scenario. Link the software-development decision guide for a fresh coding shortlist.
- For firmware/hardware questions, provide exact board/chip/SDK/toolchain/version context. Generated register addresses, pin assignments, electrical limits, peripheral behavior, or library APIs must be checked against current manufacturer documentation before flashing or wiring hardware.
- Require build/test evidence. Compile generated code, run unit/integration tests, check warnings, exercise failure paths, and validate behavior on a safe target before accepting the assistant's result.
- Treat compiler output, logic-analyzer traces, serial logs, test measurements, datasheets, and source code as stronger evidence than the assistant's confidence.
- Do not allow an agent to flash devices, change fuses/boot configuration, erase storage, operate actuators, alter network/security settings, or perform another high-impact action without a deliberate approval/recovery boundary.

## Decide the Deployment Compute Class

- Classify the device before selecting the deployed model:
  1. **MCU / deeply embedded** — kilobytes-to-megabytes memory budgets, fixed operators, hard power/latency constraints; generally narrow TinyML/vision/audio/time-series models rather than general LLMs;
  2. **Linux-capable SBC / application processor** — enough RAM/storage/OS support for broader CPU/GPU/NPU runtimes, selected compact LLM/VLM/vision/audio models, or client/gateway roles;
  3. **workstation/server companion** — a nearby PC/home-lab host performs the heavy inference while the embedded device supplies sensors/actions;
  4. **hosted API** — device sends permitted data to a managed model when network dependence, privacy, recurring cost, and failure mode are acceptable.
- Do not select a model by board brand alone. Pin exact MCU/SoC/accelerator, RAM/flash/storage, OS/RTOS, SDK/toolchain, runtime/compiler, supported operators, precision, sensor/input shape, latency target, power/thermal envelope, and connectivity.
- Route exact fixed-hardware analysis into `../../../hardware/`, especially `../../../hardware/sub/embedded/` and `../../../hardware/sub/single-board/`.

## MCU and TinyML Route

- Treat MCU deployment as a **compiled/quantized constrained inference problem**, not a smaller version of desktop LLM serving.
- Start from the narrow task and measurable signal: keyword spotting, vibration/anomaly detection, gesture/activity classification, simple vision, sensor time-series, small regression/classification, or another bounded function.
- Establish an inexpensive non-ML/classical baseline where practical. Use ML only when it materially improves accepted accuracy/robustness under the device constraints.
- Require a representative dataset that covers real sensor placement, lighting/noise, device variation, users/environments, and failure cases. A model trained only on convenient bench data is not deployment evidence.
- Include preprocessing/postprocessing memory and latency, not only neural-network inference. Signal windows, FFT/features, image resize/color conversion, camera buffers, audio buffers, and decision smoothing can dominate an MCU budget.
- Quantize/convert for the **exact vendor/runtime route** and verify every operator. A model that runs in PyTorch/ONNX on a PC can fail conversion or fall back to an impractical implementation on the MCU.
- Current Espressif ESP-DL is a lightweight inference framework for supported ESP chips; its current path uses supported operators plus quantization/conversion into the `.espdl` model format. Current documentation emphasizes ESP32-S3/ESP32-P4 as primary modern targets and requires checking operator support before deployment. Treat that as an exact ESP-DL route rather than proof that an arbitrary ONNX model runs on any ESP32.
- Current STM32Cube.AI/STM32CubeAI Studio supports model analysis, optimization, validation, and deployment to STM32 MCUs, including current Neural-ART NPU support on applicable STM32N6 devices. Keep exact device/tool version/operator support in the `hardware/embedded/stm32` owner.
- Current NXP eIQ supports ML workflows across selected NXP MCUs/application processors with inference engines, compilers, optimized libraries, BYOM/BYOD flows, and target-specific acceleration. Do not transfer support from one i.MX/MCX/RT target to another without the exact matrix.
- Do not use `TOPS` as the primary MCU model-selection measure. Usable model support depends on operator/compiler coverage, memory placement, precision, bandwidth, preprocessing, latency, sustained power, and accepted task accuracy.

## SBC and Application-Processor Route

- For Raspberry Pi, Jetson, Rockchip, and other Linux-capable boards, decide whether the board is the **inference host**, **sensor/gateway/client**, or **control node** before choosing a resident model.
- A Raspberry Pi CPU-only route and Raspberry Pi with Hailo acceleration are different model classes. Use `../../../hardware/sub/single-board/sub/raspberry-pi/` and its `cpu/`, `hailo-8/`, or `hailo-10h/` children rather than a generic `Raspberry Pi AI` claim.
- Preserve the current Hailo distinction: Raspberry Pi AI HAT+/Hailo-8/Hailo-8L are primarily vision-acceleration routes; current AI HAT+ 2/Hailo-10H adds dedicated memory and supported local LLM/VLM/GenAI routes. Do not infer LLM support from Hailo-8 TOPS or transfer Hailo-10H models to Hailo-8.
- Current Raspberry Pi documentation describes AI HAT+ 2 as an LLM/VLM-capable route with Hailo-10H and 8 GB accelerator memory, while current supported/installable model sets remain a mutable Hailo/Raspberry Pi software fact. Recheck exact supported models before recommendation.
- For Jetson, Rockchip, or another NPU/GPU board, use its exact toolkit/export/runtime and supported model formats/operators. A model that runs on a desktop NVIDIA/AMD/Intel GPU does not establish support on an embedded accelerator.
- Account for shared SBC resources: camera buffers, application processes, ROS/automation, web UI, database/RAG, storage I/O, thermal throttling, and power supply can reduce inference headroom.
- Measure sustained latency and thermals under the complete device workload, not an isolated one-shot inference demo.

## Generative AI on the Device

- Require a concrete reason for on-device generative AI: offline use, privacy, local camera/sensor context, low cloud latency, predictable local cost, educational value, or provider independence.
- Prefer compact models that meet the device task rather than forcing a desktop-class model through heavy offload. For Linux-class devices, current compact text candidates may include `Phi-4 Mini Instruct` or `Qwen3 8B` when the exact runtime/hardware supports them; current compact multimodal candidates may include `Gemma 4 E2B Instruct`/`E4B Instruct` where their exact multimodal path fits.
- Do not map these general candidates onto MCU/NPU hardware without vendor runtime evidence. Model architecture/export/operator support can be more restrictive than nominal parameter size.
- For accelerator-specific packaged model sets such as Hailo-10H, prefer the platform's currently supported compiled/package route over assuming an arbitrary GGUF/Transformers artifact can be executed.
- If the device's local generative model produces inadequate quality or latency, consider a companion PC/home-lab or hosted route before assuming new hardware must be purchased.

## Vision, Audio, and Sensor Specialists

- Prefer a dedicated narrow model when the device task is perception rather than conversation: object/pose detection, segmentation, OCR, wake word, speech recognition, audio event classification, anomaly detection, or time-series forecasting.
- Evaluate end-to-end sensor-to-decision latency and error modes. Camera frame acquisition, resize, ISP, audio buffering, filtering, feature extraction, and post-processing can dominate real-time behavior.
- For safety-relevant control, do not let an unconstrained generative model directly replace deterministic interlocks, limit switches, watchdogs, range checks, collision avoidance, emergency stop, or another required safety mechanism.
- Keep uncertain model output separate from actuation. Use confidence/validity checks and a safe fallback state appropriate to the project.
- If the project uses speech, vision, or another specialist model plus an LLM, treat each service/model as a separate resource and failure domain rather than calling the whole stack `one multimodal model`.

## Device Control and Agent Safety

- Treat physical side effects as higher consequence than ordinary chat/code generation. The model can propose or request actions, but deterministic control logic and explicit authorization must bound motors, relays, heaters, locks, pumps, power supplies, vehicles, robots, or other hazardous actuators.
- During prototyping, use simulation, mocks, current/voltage limits, safe mechanical ranges, test loads, isolated supplies, watchdogs, and accessible emergency stop/power cutoff where applicable before autonomous operation.
- Do not grant an agent unrestricted shell, serial, GPIO, Home Assistant, MQTT, SSH, or cloud credentials merely for convenience. Scope credentials/topics/devices/commands to the minimum needed and keep irreversible operations behind approval.
- Validate generated pinouts, voltages, current limits, bus addressing, fuse/boot settings, flashing commands, and component ratings against manufacturer documentation. A hallucinated hardware fact can damage equipment.
- Preserve logs/telemetry sufficient to diagnose unexpected actions without storing unnecessary secrets or private sensor data.

## Connectivity and Hybrid Architecture

- Decide whether inference must survive Internet loss. If yes, keep the minimum critical function local and treat cloud inference as optional enhancement rather than a hard dependency.
- For cloud-connected devices, define timeout/retry/backoff, offline behavior, rate limits, cost caps, and what the physical system does when the model/API is unavailable.
- Apply the data boundary before uploading camera/audio/location/household/sensor data. A hobby project can still capture bystanders, home interiors, credentials, or other sensitive information.
- Minimize transmitted data. When the cloud model only needs an event/summary, derive it locally rather than continuously streaming raw sensor/video/audio.
- A nearby home-lab server can be a useful middle route: stronger local inference without embedding a large model into every device. Move persistent server operations into `home-lab-owner/` rather than duplicating its uptime/security/TCO contract here.

## Development, Conversion, and Deployment Reproducibility

- Pin board/chip revision, firmware/OS image, SDK/toolchain, model source/version, conversion/quantization configuration, runtime/compiler, preprocessing code, and relevant build flags for a working deployment.
- Keep source model identity distinct from the compiled device artifact. An `.espdl`, vendor binary, engine, HEF, TFLite/LiteRT, ONNX-derived, or another converted artifact is not interchangeable with the upstream source model.
- Preserve conversion logs/reports and model validation results when they materially prove operator mapping, memory, or numerical accuracy.
- Test inference against a reference implementation before relying on target results. Quantization/conversion/operator differences can change predictions even when deployment succeeds.
- Revalidate after SDK/runtime/compiler/model changes. An embedded toolchain upgrade can change operator implementations, memory planning, numerical behavior, or performance.

## Measurement Contract

- For embedded/SBC inference record at minimum: exact hardware; clock/power/cooling assumptions; model and artifact identity; precision; runtime/compiler; input shape/rate; memory/flash/storage footprint; preprocessing + inference + postprocessing latency; throughput if relevant; sustained power/temperature; and accepted task accuracy/error cases.
- Separate **can compile/load** from **meets the project**. Passing conversion or loading onto the target is only compatibility evidence.
- For battery-powered devices include duty cycle and energy per inference/session, not only instantaneous power.
- For always-on sensors include idle/listening cost, wake-up behavior, and false-positive/false-negative burden.
- For generative models include first-token latency, decode speed/task latency, context limit actually usable on the target, and output correction/reliability.

## Cost and Build-vs-Buy Decision

- Compare model routes using prototype TCO: already-owned development PC/SBC/MCU, accelerator/module cost when already fixed, cloud/API usage, storage, power/battery, development/conversion time, debugging, model/data collection, and maintenance.
- Do not recommend an accelerator or new board until the current target's measured bottleneck is known and the new platform has an exact supported route for the desired model/task.
- For a one-off hobby project, a hosted API may be cheaper than weeks of embedded-model optimization; for a frequently running/privacy-sensitive/offline device, local inference may win despite setup cost.
- Treat hobby learning value as a legitimate objective, but label it separately from the economically simplest implementation.

## Escalation Triggers

- Move from a general development assistant to a specialist coding/model-selection route when code quality or project scale becomes the bottleneck.
- Move from MCU inference to SBC/application-processor inference when model/operator/memory/preprocessing requirements exceed the MCU's practical envelope.
- Move from SBC local inference to a nearby home-lab/workstation when local board latency, model quality, context, or modality support cannot meet the project.
- Move to hosted API when stronger quality/capability outweighs latency/privacy/offline/cost constraints and the device has a safe failure mode.
- Move from hosted to local when recurring cost, latency, privacy, or connectivity failure materially harms the deployed project.
- Move to `home-lab-owner/` when a companion inference server becomes persistent infrastructure; move to `privacy-first-or-offline-user/` when no-egress becomes the primary architecture constraint.
- Move out of the personal scenario family when the device becomes a product/service with customers, formal safety/regulatory obligations, or organizational operations.

## Hardware-Specific Model Selection Continuation

- Link the complete `../../../hardware/` journey when deployment hardware determines model fit.
- Use `../../../hardware/sub/embedded/` and its `esp32/`, `stm32/`, and `nxp/` routes for current selected MCU/embedded ecosystems.
- Use `../../../hardware/sub/single-board/` for Linux-capable Raspberry Pi, Jetson, and Rockchip routes; use the deeper Raspberry Pi CPU/Hailo-8/Hailo-10H children when applicable.
- Use `../../../hardware/sub/computers/` or `../../../hardware/sub/servers/` when a workstation/home server actually performs inference for the project.
- Do not reproduce platform support matrices in this scenario.

## Canonical Links

- Route exact coding-model choice to the software-development decision guide instead of freezing a coding leaderboard here.
- Link compact general local models to canonical Model Reference identities such as `catalog/models/reference/producers/microsoft/phi/phi-4/models/phi-4-mini-instruct` and `catalog/models/reference/producers/alibaba/qwen/qwen3/models/qwen3-8b` only when the target is Linux/workstation-class and current runtime evidence supports them.
- Link compact multimodal candidates to `catalog/models/reference/producers/google/gemma/gemma-4/models/e2b-instruct` and `.../e4b-instruct` when named.
- Link exact inference runtimes/software to canonical software owners when they exist; hardware-vendor toolchains named only as current platform evidence remain subordinate to their hardware route until/if canonical software identities are separately materialized.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current first-party ESP-DL, STM32Cube.AI/STM32CubeAI Studio, NXP eIQ, Raspberry Pi AI HAT/software documentation, current compact-model evidence, and canonical AI Lab hardware/model owners.
- Current ESP-DL documentation requires supported operators and conversion/quantization into its target model format; current STM32Cube.AI supports optimization/validation/deployment to STM32 including current Neural-ART NPU targets; current NXP eIQ spans selected MCUs/application processors with target-specific toolchains. Treat these as vendor-specific routes rather than cross-platform standards.
- Current Raspberry Pi documentation distinguishes vision-focused AI HAT+/Hailo-8/8L from AI HAT+ 2/Hailo-10H GenAI capability and its 8 GB accelerator memory; supported LLM/VLM packages are mutable and must be rechecked for the exact software release.
- SDK/toolchain versions, operator/compiler coverage, model packages, board support, accelerator drivers, and vendor model zoos change quickly; recheck them before rendering a current deployment recommendation.
- Vendor demo success establishes feasibility for the demonstrated hardware/model/toolchain, not independent proof of accepted accuracy, sustained latency, power, or compatibility with another model.

## Validation

- The page clearly separates `AI assists development` from `AI executes on the device`.
- MCU/TinyML, Linux SBC, companion server/workstation, and hosted API are treated as different model classes/routes.
- General LLM parameter count or accelerator TOPS is never transferred into MCU/embedded compatibility.
- Conversion/operator/runtime support is required before a model is called deployable.
- Raspberry Pi Hailo-8/8L vision routes are not mislabeled as Hailo-10H LLM/VLM routes.
- Physical side effects have deterministic safety/authorization boundaries and generated hardware facts are verified against primary documentation.
- Deployment evidence includes preprocessing/postprocessing, sustained resource use, and accepted task accuracy—not only successful compilation/loading.
- Cloud/hybrid routes define safe behavior when connectivity/API fails and classify data before upload.
- Hardware buying remains outside this scenario until a measured bottleneck and exact supported destination are established.
- Mutable current claims carry the 2026-08-23 evidence boundary.
