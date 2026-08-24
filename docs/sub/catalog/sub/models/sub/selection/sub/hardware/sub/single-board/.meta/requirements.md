# Documentation Requirements

## Router Role

- Cover Linux-capable SBC/developer-board ecosystems where fixed board/SoC/accelerator software stacks create materially different local inference routes.
- Route current selected ecosystems to `raspberry-pi/`, `jetson/`, and `rockchip/`.
- Do not use `edge/` as the taxonomy parent: edge is a deployment context that can also describe mini PCs, industrial PCs, gateways, appliances, and servers.
- Keep this page focused on cross-SBC selection constraints and delegate runtime/model specifics to the ecosystem children.
- Keep board purchasing outside this router.

## Exact Platform Before Model

- Require exact board/module, SoC/accelerator, RAM, OS/BSP/kernel, runtime/toolkit, model artifact/export/quantization, storage/I/O, cooling/power, context, and sustained workload before assigning fit.
- Do not infer support from `ARM`, `NPU`, `CUDA`, `TOPS`, or SBC branding alone.
- The same source model can require GGUF CPU execution, HEF, RKNN/RKLLM, TensorRT, or another platform-specific artifact depending on the board.
- Keep unsupported or unmeasured combinations explicitly `Unknown`.

## Ecosystem Routing

- Route Raspberry Pi to `raspberry-pi/` when Pi OS/platform integration and CPU/Hailo paths determine fit.
- Route NVIDIA Jetson to `jetson/` when JetPack/Jetson Linux, CUDA/TensorRT, integrated GPU/DLA, shared memory, and NVIDIA edge software determine fit.
- Route Rockchip SoCs to `rockchip/` when RKNN/RKLLM, RKNPU driver/BSP, target-specific compiled artifacts, and NPU core configuration determine fit.
- Do not create duplicate board-brand branches for Radxa/Orange Pi/other Rockchip boards unless board-specific constraints consistently change model selection.

## CPU vs Accelerator Routes

- Separate CPU-only inference from GPU/NPU/accelerator-specific routes.
- CPU compatibility does not prove NPU/GPU acceleration and accelerator compatibility does not remove host CPU/RAM requirements.
- Record preprocessing/postprocessing, tokenization, camera/audio, storage, retrieval, networking, and agent/tool work that remains on the host.
- Measure complete application latency rather than one accelerator kernel/subgraph.

## Shared System Memory

- Many SBC accelerators share system RAM with the CPU/OS; do not label total board RAM dedicated VRAM/NPU memory.
- Where an accelerator has dedicated memory, such as Hailo-10H, keep it separate from host RAM.
- Include model/KV/cache/runtime buffers, camera/media buffers, containers/services, and application state in whole-system memory evidence.
- More RAM can expand feasible resident state but does not guarantee accelerator support or throughput.

## Model Conversion and Runtime Coupling

- SBC accelerators frequently require platform-specific conversion/compilation on another host machine.
- Preserve source model/revision, converter/toolkit, quantization/calibration, target platform, generated artifact, target runtime/driver/BSP, and artifact hash.
- Do not equate ONNX/PyTorch/Hugging Face source weights with deployable accelerator artifacts.
- Revalidate after toolkit/runtime/BSP/driver updates.

## ARM64 Software Ecosystem

- Verify all native application dependencies for the target Arm architecture, not only the inference runtime.
- CUDA/x86 wheels, tokenizers, vector databases, browser automation, media libraries, custom operators, and Python extensions can block an otherwise supported model.
- Record source builds/patches that become part of deployment.
- Keep missing critical dependencies as route blockers rather than model-fit optimism.

## BSP and OS Fragmentation

- Treat vendor BSP/kernel/driver versions as part of accelerator compatibility.
- Raspberry Pi OS, JetPack/Jetson Linux, and Rockchip vendor/community Linux images have materially different hardware integration models.
- Do not transfer one ecosystem's mainline/vendor-kernel assumptions to another.
- Re-test after major OS/kernel/BSP/firmware changes.

## Cooling, Power, and Sustained Operation

- Measure sustained thermal behavior at the deployed power mode/case/cooler rather than a short open-bench run.
- Record throttling, clocks, whole-board/peripheral power, and stable power-supply state.
- Cameras, NVMe/USB storage, HATs/M.2 accelerators, and radios share the board's thermal/power budget.
- A model that fits only under maximum power or unusually aggressive cooling is conditional fit when deployment cannot reproduce those conditions.

## Storage and Model Lifecycle

- Include model artifacts, compiled engines, containers/packages, caches, indexes, logs, calibration assets, and update/rollback headroom.
- Distinguish cold/warm load and mmap/page-cache behavior where startup matters.
- Prestage models/packages when offline edge operation is required.
- Do not use slow flash/removable storage swap as normal model-memory expansion for interactive workloads.

## Camera, Audio, and Physical I/O

- SBCs commonly combine AI with camera/audio/sensor/GPIO/robotics workloads; include those pipelines in fit.
- Measure capture/decode/preprocess, inference, postprocess, control/streaming/storage, and model reasoning together where they coexist.
- Keep deterministic real-time/safety loops independent from optional LLM/VLM services where consequence requires it.
- Accelerator TOPS or model benchmark FPS does not establish sensor-to-action deadlines.

## Concurrency and Shared Services

- Measure intended concurrent models, streams, sessions, containers, and background services.
- Multiple models can compete for shared memory, NPU/GPU cores, PCIe, CPU postprocessing, and storage/network.
- Report p50/p95 latency and load/unload behavior for service-style use.
- If the SBC becomes multi-user/shared infrastructure, route platform/service concerns to server/internal-platform scenarios rather than treating one-user benchmark fit as sufficient.

## Offline and Edge Reliability

- Test complete network-denied operation when offline capability is claimed.
- Avoid hidden model-hub, package, license, execution-provider, or telemetry dependencies.
- Define degraded/manual behavior if the model/runtime/accelerator fails.
- Preserve recovery/rollback for remote/unattended deployments.

## Security and Agentic Actions

- Local inference improves data locality but does not authorize tools or physical actions.
- Treat camera OCR, web/documents/messages/files/model output as untrusted when an application can execute shell/GPIO/robot/network/account actions.
- Use deterministic permissions, allowlists, argument validation, confirmations, and physical safety interlocks.
- Keep secrets out of model context/logs.

## Quality and Accepted Result

- Evaluate the exact deployed/quantized/compiled artifact on representative tasks.
- Separate official runtime compatibility from provider benchmarks and from AI Lab/user task quality.
- Track retries/correction burden with memory/latency/power.
- A model that loads/benchmarks but fails accepted quality or whole-application deadlines does not fit.

## Practical Routing Outcomes

- `Raspberry Pi`: Pi CPU or supported Hailo child route owns the decision.
- `Jetson`: exact JetPack/module/CUDA/TensorRT/other supported NVIDIA route owns the decision.
- `Rockchip`: exact SoC/BSP/RKNPU/RKNN/RKLLM compiled route owns the decision.
- `Hosted/hybrid`: no fixed SBC route meets accepted quality/context/latency and data/network policy permits escalation.
- `Unknown`: exact board/runtime/artifact behavior is unsupported or unmeasured.

## Canonical Links

- Route ecosystem-specific evidence to `raspberry-pi/`, `jetson/`, and `rockchip/`.
- Link exact model facts to Model Reference and software runtimes/toolchains to canonical software owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Link user scenarios when edge/robotics/home-lab/application requirements dominate hardware selection.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after current first-party Raspberry Pi/Hailo, NVIDIA Jetson, and Rockchip RKNN/RKLLM child-route passes.
- Current evidence confirms that the three ecosystems require materially different OS/BSP/runtime/model-artifact paths and memory/power assumptions, while sharing a common need for exact host resources, Arm dependencies, sustained edge measurements, and accepted-result validation.
- JetPack/Jetson Linux, Raspberry Pi OS/Hailo packages, Rockchip BSP/RKNPU/RKNN/RKLLM, model artifacts, Arm packages, and board firmware are mutable; recheck child routes before rendering recommendations.
- Exact board/ecosystem/runtime/artifact/full-application measurement and accepted-result quality remain the fit authority.

## Validation

- Direct children remain Raspberry Pi, Jetson, and Rockchip ecosystem routes.
- `edge/` is not introduced as a competing hardware taxonomy.
- CPU/GPU/NPU routes and host work are not conflated.
- Board RAM/TOPS/branding/load success do not replace exact runtime/artifact evidence.
- Platform-specific conversion, BSP/driver, ARM64 dependency, storage/I/O, power/cooling, offline, and whole-application constraints are represented.
- Rockchip board brands sharing one RKNN/RKLLM decision path are not duplicated without a real seam.
- Hardware buying remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
