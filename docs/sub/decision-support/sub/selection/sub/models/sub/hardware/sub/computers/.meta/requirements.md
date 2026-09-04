# Documentation Requirements

## Router Role

- Cover interactive general-purpose laptops, desktops, gaming/creator PCs, workstations used as personal compute, and mini PCs where the machine is not primarily a dedicated inference server.
- Route by the **effective local AI compute/runtime ecosystem**, not OEM, CPU brand, or marketing category: `apple/`, `nvidia/`, `amd/`, `intel/`, `qualcomm/`, or `cpu/`.
- Keep this page focused on cross-computer constraints and delegate exact runtime/device/model support to the six children.
- Keep PC/GPU purchasing outside this journey; begin from the existing machine and expose a measured capability/resource gap if local fit fails.

## Choose the Actual Execution Path

- Identify which device/runtime will actually execute the intended model before selecting a child route.
- An Intel/AMD CPU machine using an NVIDIA GPU follows `nvidia/`; an Intel Core Ultra machine whose useful route is CPU-only follows `cpu/`; Apple-Silicon Mac unified-memory execution follows `apple/`.
- A PC can contain several accelerators while only one has a practical supported path for the selected model.
- Do not route from chassis/OEM/CPU branding when the actual inference device differs.
- Preserve hybrid CPU+GPU/NPU fallback as an explicit measured configuration rather than a second hidden route.

## Current Child Boundaries

- `apple/` owns Apple-Silicon Mac unified-memory routes such as MLX/Metal/GGUF/Core ML where applicable.
- `nvidia/` owns NVIDIA RTX/GeForce/RTX PRO local GPU routes using current CUDA/TensorRT-RTX/llama.cpp or other supported PC backends.
- `amd/` owns Radeon/Ryzen GPU and Ryzen AI NPU/iGPU routes with exact ROCm/Ryzen AI/Windows/backend support.
- `intel/` owns Intel PC CPU/iGPU/NPU routes where OpenVINO/Windows ML/other Intel-supported execution is intended.
- `qualcomm/` owns Snapdragon X Windows PC NPU/GPU/ARM64 CPU routes.
- `cpu/` owns machines where no useful supported local accelerator is the intended model route.
- Do not duplicate child support matrices here.

## Exact Machine State

- Require exact device/GPU/APU/NPU/SoC, installed RAM and accelerator memory architecture, OS/build, drivers, runtime/backend, model artifact/quantization, context, display setup, cooling/power mode, and concurrent applications before assigning fit.
- Record laptop vs desktop/workstation thermal/power envelope where it materially changes sustained inference.
- Treat eGPU, WSL, virtualized, remote-desktop, and other non-native paths as explicit configurations when used.
- Keep unsupported/unmeasured exact machine/runtime/model combinations `Unknown`.

## Memory Architecture Matters

- Distinguish dedicated VRAM from shared/unified system memory and from NPU-local/driver-managed memory.
- Do not add nominal system RAM and dedicated VRAM into one generic model capacity figure.
- Include model weights, KV/cache, runtime buffers, encoders/decoders, quantization workspaces, display/application use, OS, browser/IDE/creative tools, and other resident models.
- Measure peak memory and operational headroom under the actual workload.
- Swap/pagefile-heavy load success is not practical interactive fit unless the workflow explicitly tolerates it.

## Desktop / Interactive Contention

- Measure local inference while the machine performs its real foreground workload.
- Gaming/graphics, video editing, browsers, IDEs, containers, builds, local databases, conferencing, and display composition can consume the same GPU/CPU/RAM/power budget.
- A clean-room benchmark with all user applications closed is insufficient when AI must coexist with daily work.
- Record application responsiveness/frame-time/build latency impact where relevant.
- Preserve `Fits conditionally` when local AI is acceptable only after closing competing applications or reducing model/context.

## OS and Runtime Are Part of Fit

- Treat Windows, Linux, WSL, and macOS as distinct runtime evidence paths.
- Do not transfer Linux CUDA/ROCm/OpenVINO support to Windows/WSL or vice versa without current evidence.
- For Windows-on-ARM, include native ARM64 application/runtime/tool support and emulation overhead.
- Preserve exact driver/runtime versions and platform packages.
- Recheck mutable support matrices before current recommendations.

## Accelerator Marketing Is Not Compatibility

- Do not infer arbitrary model support from `AI PC`, `NPU`, `RTX`, `Ryzen AI`, `Core Ultra`, `Snapdragon X`, `Apple Neural Engine`, TOPS, or similar branding.
- Require exact model/export/operator/runtime support and actual device placement.
- If an unsupported operation falls back to CPU/GPU, include that fallback in latency/power/memory evidence.
- A system feature/consumer assistant running on an accelerator is not evidence that an app-owned model can use the same accelerator path.

## Model Artifact Is Runtime-Specific

- Preserve the exact deployed artifact and conversion/quantization path.
- MLX artifacts, GGUF, TensorRT engines, OpenVINO exports, QNN/compiled graphs, Ryzen AI/ONNX paths, and other formats are not interchangeable simply because they originate from the same model family.
- Record source model/revision, conversion tool/version, precision/quantization, tokenizer/adapters, and auxiliary multimodal assets.
- Evaluate quality after conversion/quantization.

## Context and KV Cache

- Include context/KV cache in every local memory-fit decision.
- Measure prompt lengths and output lengths representative of the user's real tasks.
- A model that fits at short context but fails at the required working context is conditional or non-fit.
- Separate prompt/prefill and decode performance when relevant.
- Do not use advertised maximum context as practical local capacity without memory/latency evidence.

## Sustained Power and Thermals

- Measure sustained inference rather than one short burst, especially on laptops/mini PCs and shared graphics systems.
- Record plugged-in/battery mode, OS performance mode, GPU power limit, fan/cooling state, temperature, clocks, and throttling when material.
- Include battery drain for mobile workstation/laptop use.
- A route that meets latency only for a brief turbo window is conditional fit.

## Multimodal / Media Pipelines

- Include vision/audio encoders, VAE/decoders, preprocessing, postprocessing, media buffers, and GPU/CPU transfer costs.
- Do not use text-only LLM memory/tokens-per-second results to claim VLM/diffusion/media fit.
- Verify exact runtime/model support for every stage.
- Measure complete task latency and peak working set.

## Multiple Models and Agents

- For RAG/agent/coding assistants, include embeddings/rerankers, local databases, tool processes, IDE/browser, and any guard/safety model that is concurrently resident.
- Do not size the machine from one standalone LLM process when the real workflow uses several services.
- Local tool/agent authority remains deterministic and least-privilege; model locality does not make side effects safe.
- Preserve hosted/hybrid escalation for difficult steps when approved by the data boundary.

## Privacy and Offline Boundary

- Local execution can reduce provider exposure, but verify model/runtime downloads, telemetry, license checks, update calls, remote tools, web search, and cloud fallback separately.
- For offline use, pre-stage artifacts and test startup/steady-state with network denied.
- Do not claim an app is fully local when a material stage silently calls a hosted service.
- Link high-security/regulatory constraints to the appropriate user scenario when they dominate selection.

## Quality and Accepted Result

- Evaluate each exact local artifact on representative user tasks.
- Track quality, latency, retries, correction time, failure severity, and power/resource impact.
- A smaller model may be the best existing-PC route when it produces accepted results more reliably/faster than a larger model that barely fits.
- Do not optimize tokens/s independently of task quality.

## Practical Routing Outcomes

- `Apple`: exact Apple-Silicon/macOS/runtime/artifact route owns fit.
- `NVIDIA`: exact RTX/driver/CUDA/backend/artifact route owns fit.
- `AMD`: exact Radeon/Ryzen/ROCm/Ryzen-AI/backend route owns fit.
- `Intel`: exact Intel CPU/GPU/NPU/OpenVINO/Windows backend route owns fit.
- `Qualcomm`: exact Snapdragon X/Windows/QAIRT-QNN/ARM64 route owns fit.
- `CPU`: no useful supported accelerator route is intended; CPU runtime owns fit.
- `Hosted/hybrid`: existing machine cannot meet accepted quality/context/latency or local setup economics and the data/network boundary permits escalation.
- `Unknown`: exact device/runtime/artifact behavior lacks current support or measurement.

## Canonical Links

- Route exact ecosystem evidence to the six children rather than duplicating support matrices here.
- Link exact model facts to Model Reference and runtime/software facts to their canonical owners.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Link user scenarios when workflow/data/privacy/economics become the primary decision rather than hardware fit.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after current first-party Apple MLX, NVIDIA RTX/TensorRT-RTX, AMD ROCm/Ryzen AI, Intel OpenVINO, Qualcomm Snapdragon/QAIRT-QNN, and generic CPU runtime child-route passes.
- Current child evidence confirms that consumer computers require materially different runtime/artifact/OS paths and that accelerator presence, nominal memory, or TOPS cannot establish model fit. Shared desktop workloads and OS/runtime fragmentation are common cross-route constraints.
- Drivers, OS APIs, runtime backends, NPU/GPU support matrices, model exports/quantizations, and application/tool compatibility are mutable; recheck child routes before rendering recommendations.
- Exact existing machine/runtime/artifact/context/workload measurement and accepted-result quality remain the fit authority.

## Validation

- Direct children remain `apple/`, `nvidia/`, `amd/`, `intel/`, `qualcomm/`, and `cpu/`.
- Routing follows the effective inference device/runtime rather than OEM/CPU/chassis branding.
- Dedicated, shared, and unified memory architectures are not conflated.
- Accelerator marketing/TOPS/system consumer features do not substitute for exact model/runtime support.
- OS, driver, artifact, context/KV, desktop contention, sustained power/thermals, and accepted quality are represented.
- Desktop/workstation and dedicated server routes remain distinct.
- Hardware purchasing remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
