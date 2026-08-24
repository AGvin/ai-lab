# Documentation Requirements

## Router Role

- Present Raspberry Pi as a router across three materially different local compute paths: `cpu/`, `hailo-8/`, and `hailo-10h/`.
- Require exact Pi generation/RAM/OS, installed accelerator if any, storage, cooling/power, application workload, modalities, offline requirement, and target latency before routing.
- Do not treat Raspberry Pi 5, AI HAT+, AI HAT+ 2, or a larger RAM option as a universal model tier.
- Keep hardware purchasing outside this router.

## Choose the Compute Path First

- Route to `cpu/` when no supported accelerator is present or the intended model/workload runs on the Arm CPU.
- Route to `hailo-8/` for an existing Hailo-8L/Hailo-8 AI HAT+/AI Kit where supported vision/neural inference is the objective.
- Route to `hailo-10h/` for an existing Hailo-10H AI HAT+ 2 where current supported local LLM/VLM/audio/vision GenAI is required.
- Do not choose between Hailo-8 and Hailo-10H from TOPS alone; their supported model universes and memory architecture differ.
- Hosted/hybrid execution remains a legitimate result when no owned local route meets accepted quality/context/latency.

## Current Capability Separation

- Current Raspberry Pi documentation explicitly separates Hailo-8L/Hailo-8 AI HAT+ vision/neural workloads from Hailo-10H AI HAT+ 2 GenAI capability.
- Hailo-8/8L does not inherit Hailo-10H LLM/VLM support.
- Hailo-10H has dedicated accelerator memory and a compiled current GenAI model catalog; Pi CPU-only inference instead consumes host RAM/CPU.
- Do not add Pi host RAM and Hailo accelerator memory into one generic capacity number.
- Keep each child's exact runtime/artifact compatibility in the child page.

## Exact Pi Generation and OS

- Record Pi generation/model and current 64-bit OS/distribution rather than using `Raspberry Pi` generically.
- Current Hailo software guidance targets Raspberry Pi 5 and current Raspberry Pi OS Trixie; CPU evidence for newer generative workloads is likewise strongest on Pi 5.
- Do not transfer current Pi 5/Hailo results to Pi 4/CM4/Zero/older devices without exact evidence.
- Recheck Raspberry Pi OS/kernel/firmware/runtime packages after major updates.

## Host Resources Always Matter

- Even with Hailo acceleration, the Pi host handles OS, application orchestration, camera/audio I/O, retrieval/database, networking, tool calls, preprocessing/postprocessing, and output rendering.
- Record host RAM/CPU use under the complete workload.
- Do not infer an accelerator removes all CPU/RAM bottlenecks.
- For CPU-only inference, route all model memory/context/latency constraints to `cpu/`.
- For Hailo-10H, preserve the split between dedicated accelerator RAM and Pi host RAM.

## Storage and I/O

- Record microSD, USB SSD, NVMe, camera/audio devices, network, and model/cache/index storage where they affect startup or sustained operation.
- Include model/compiled artifact size, caches, logs, retrieval indexes, and update headroom.
- Do not use slow storage/swap as ordinary model-memory expansion.
- Measure cold/warm model/application load when startup matters.

## Cooling and Power

- Treat sustained cooling and stable power as common Raspberry Pi constraints.
- Measure Pi thermal/throttle state under the actual application; HATs/cameras/SSDs/peripherals remain part of the power budget.
- Hailo acceleration can reduce host compute for supported models but does not eliminate whole-system thermal/power requirements.
- Do not use a short open-bench result as proof of always-on edge/server performance.

## Camera and Media Pipelines

- For vision/VLM applications, include camera capture/ISP, resize/color conversion, accelerator or CPU inference, postprocessing, storage/network/display, and any language stage.
- Route Hailo-8 supported vision pipelines to `hailo-8/`.
- Route Hailo-10H VLM/GenAI pipelines to `hailo-10h/` when exact current artifacts support them.
- Keep CPU-only vision/language pipelines under `cpu/` when no accelerator route is selected.
- Do not promote raw accelerator FPS/TOPS to camera-to-result latency.

## Language and Generative Work

- CPU-only Pi can run compact supported text models but practical interactive fit depends on exact runtime/artifact/context and accepted latency.
- Current Hailo-8/8L route is not the supported Pi GenAI LLM/VLM route.
- Current Hailo-10H route supports named compiled compact LLM/VLM artifacts with its own context/quantization/runtime limits.
- Unsupported/larger models remain CPU, another local platform, hosted/hybrid, or `Unknown`; do not infer support from parameter count.

## Offline and Privacy

- Test the complete application with network denied when local/offline behavior is required.
- Prestage models/compiled artifacts/runtime packages.
- Retrieval, web tools, telemetry, model downloads, or hosted fallback can make an otherwise local inference pipeline network-dependent.
- Do not silently send local camera/audio/document data to cloud fallback.

## Agents and Physical Actions

- A local Pi/Hailo/CPU model does not authorize GPIO, robotics, home automation, shell, network, or account actions.
- Treat camera OCR, documents, web/tool output, messages, and model results as untrusted input.
- Use deterministic tool allowlists, permissions, argument validation, confirmation, and safety interlocks.
- Route application/physical-AI decision logic to the applicable scenario/decision guide when it becomes primary.

## Practical Routing Outcomes

- `CPU`: exact Pi CPU/runtime/artifact/context passes accepted quality, memory, latency, cooling, and application requirements.
- `Hailo-8/8L`: exact HEF/toolchain/runtime passes supported vision/neural quality and end-to-end pipeline requirements; current LLM/VLM request is not routed here.
- `Hailo-10H`: exact supported compiled GenAI artifact/runtime/context passes accelerator+host memory, TTFT/decode/task, thermal/power, and application requirements.
- `Hosted/hybrid`: owned Pi routes do not meet accepted model/context/latency and network/data policy permits escalation.
- `Unknown`: exact Pi/accelerator/runtime/artifact combination lacks current support or measurement.

## Canonical Links

- Route exact runtime/model-fit details to `cpu/`, `hailo-8/`, or `hailo-10h/`.
- Link exact model facts to Model Reference and Raspberry Pi/Hailo software to canonical software owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Link user scenarios when application/data constraints dominate hardware selection.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after current first-party Raspberry Pi CPU, AI HAT+/AI HAT+ 2, Hailo software, and all three child-route evidence passes.
- Current evidence supports a stable three-way routing distinction: Pi CPU; Hailo-8L/Hailo-8 supported vision/neural acceleration; Hailo-10H supported compact GenAI/LLM/VLM/audio/vision acceleration with dedicated memory.
- Raspberry Pi OS/kernel/firmware, Hailo packages/runtimes/artifacts, supported models, CPU runtimes, camera integration, and product capability boundaries are mutable; recheck child routes before rendering recommendations.
- Exact Pi/compute-path/runtime/artifact/full-application measurement and accepted-result quality remain the fit authority.

## Validation

- Direct children remain `cpu/`, `hailo-8/`, and `hailo-10h/`.
- CPU and accelerator fit are not mixed.
- Hailo-8/8L and Hailo-10H GenAI capabilities are not conflated.
- Host Pi RAM and Hailo-10H dedicated memory remain separate.
- Pi generation/OS, storage/I/O, power/cooling, host work, offline state, and complete pipeline are represented.
- TOPS, installed RAM, parameter count, and load success do not replace exact child-route evidence.
- Buying advice remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
