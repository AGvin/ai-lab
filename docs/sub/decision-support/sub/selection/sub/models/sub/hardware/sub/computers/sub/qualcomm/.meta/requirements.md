# Documentation Requirements

## Route Fit

- Cover Snapdragon X-class Windows PCs where Qualcomm Hexagon NPU, Adreno GPU, or ARM64 CPU is the intended on-device inference route.
- Require the exact Snapdragon X SKU/platform, Windows build, driver/firmware stack, ARM64 runtime, QAIRT/QNN/AI Hub/Windows ML or other backend, model artifact/export, quantization/precision, context, memory configuration, and selected compute unit before making a fit claim.
- Separate Snapdragon laptop/PC execution from Android/mobile Qualcomm routes.
- Keep PC buying outside this page; the reader starts from owned/fixed Snapdragon X hardware.

## Qualcomm PC Is a Multi-Device Route

- Distinguish NPU/HTP, Adreno GPU, ARM64 CPU, and any explicit hybrid/partitioned execution.
- Do not infer that a model using the NPU for one graph stage keeps the complete application on the NPU.
- Record each material stage and actual compute unit used.
- Treat CPU/GPU fallback and preprocessing/postprocessing as part of end-to-end latency and power.
- Route hosted Copilot or other cloud-assistant features outside local hardware compatibility; a service available on a Snapdragon PC is not evidence that its model runs on the local NPU.

## Current Qualcomm AI Runtime Boundary

- Treat Qualcomm AI Runtime (QAIRT)/QNN and ONNX Runtime QNN execution-provider paths as current first-party Qualcomm deployment routes for supported Snapdragon hardware.
- Preserve exact QAIRT/QNN backend/core API versions because compiled contexts, supported operators, performance modes, and device compatibility change.
- Current Qualcomm AI Hub profile jobs from August 2026 explicitly target Snapdragon X Elite CRD / Windows 11 / SC8380XP using current QAIRT/QNN releases and identify the NPU compute unit.
- Use AI Hub as current compatibility/profiling evidence, not as proof that an arbitrary application/model is supported locally.
- Verify exact SDK/device support before every current recommendation.

## Qualcomm AI Hub Evidence Boundary

- AI Hub can compile/profile supported model components against named Qualcomm target devices and returns target device, OS/build, runtime versions, compute unit, estimated inference time, and peak memory for the profiled graph.
- Preserve the exact job/model component name, input shape, target, runtime version, and execution configuration when using AI Hub evidence.
- Do not present a profile job for `unet`, `llm`, proposal generator, encoder, decoder, or other subgraph as complete application latency.
- Current profile examples show materially different first-load, subsequent-load, inference, and memory values; include all relevant stages in application acceptance.
- Provider-hosted profiling remains provider evidence. Run the complete workflow on the user's physical PC before assigning practical fit.

## Model and Graph Coverage

- Require the exact model/export that the QNN/QAIRT path can compile and execute.
- Record unsupported operators, graph partitions, delegated subgraphs, and CPU/GPU fallback.
- A successful partial NPU compile does not prove full-model NPU execution.
- Verify preprocessing/tokenization, embeddings, KV/cache management, decoders, sampling, image/audio transforms, and postprocessing separately where they execute outside the profiled graph.
- Keep unsupported/unmeasured complete-model paths `Unknown` even when one subgraph profiles successfully.

## LLM-Specific Evidence

- Treat an LLM as a stateful multi-step application rather than one feed-forward profile invocation.
- Current AI Hub jobs can profile LLM-related graph fragments on Snapdragon X Elite using ONNX Runtime QNN and report NPU inference/memory for the supplied shapes; that evidence does not equal TTFT, prompt-processing throughput, sustained decode, or full context capacity.
- Measure tokenizer/input preparation, prefill, KV-cache allocation/update, token-by-token decode, sampling, and output processing end to end.
- Record context/input/output lengths and cache precision/layout.
- Do not infer local LLM performance from a single fixed-shape NPU graph timing.

## ARM64 Application Compatibility

- Require native ARM64 availability for the inference runtime and the surrounding application where practical.
- Record which components run native ARM64 versus Windows emulation.
- Emulated UI/helper code may be acceptable, but emulated inference/runtime dependencies can change latency, memory, compatibility, and tool integration materially.
- Verify Python/Node/native libraries, tokenizer extensions, media codecs, database/vector libraries, browser automation, and other dependencies for ARM64 when they are part of the workflow.
- Do not infer app compatibility from model-runtime compatibility alone.

## Windows and Driver Boundary

- Record Windows 11 build, Snapdragon platform/firmware/driver package, runtime version, and application architecture.
- Verify current driver/runtime support for the exact Snapdragon X SKU rather than treating all `Snapdragon X` devices as identical.
- Keep preview/dev-kit CRD evidence distinct from a retail PC unless the hardware/runtime equivalence is established.
- Re-test after Windows, OEM firmware, NPU driver, or QAIRT/QNN changes that can affect execution.

## Windows ML Route

- Treat Windows ML as a separate application API/provider-selection path when the software targets it.
- Verify the exact Qualcomm/QNN execution provider, supported model/export, Windows build, and actual device selected at runtime.
- Dynamic provider acquisition/update can create a network and version dependency; account for this in offline/high-security deployments.
- Do not assume a Windows ML API request targets the NPU simply because the device has one.
- Preserve Windows ML/provider evidence separately from direct QAIRT/QNN/AI Hub results.

## NPU/HTP Route

- Treat the Hexagon NPU/HTP as an export/operator-specific accelerator.
- Verify QNN backend configuration, precision, graph optimization, VTCM or other target options where material.
- Current AI Hub jobs expose performance mode and precision configuration; provider timings can reflect aggressive `BURST`-style settings and should not automatically be treated as battery-efficient sustained behavior.
- Measure sustained device power/temperature and battery impact on the retail machine.
- Do not treat NPU TOPS as expected application throughput.

## Adreno GPU Route

- Treat Adreno GPU acceleration separately from the NPU.
- Verify the chosen backend (for example DirectML, OpenCL/Vulkan/other runtime where actually supported), model operators, precision, and artifact.
- Current `llama.cpp` support for Qualcomm-specific Hexagon acceleration remains distinct from its other GPU/CPU backends; do not infer mature Hexagon LLM support from generic project support without current evidence.
- If using an Adreno OpenCL/Vulkan route, label it according to the exact runtime/project support and measure the complete model.
- Shared system memory and display contention apply to the integrated GPU route.

## CPU Route on Snapdragon X

- Treat ARM64 CPU inference as a legitimate bounded fallback when mature native runtimes support the model and latency/quality is acceptable.
- Record CPU SKU/core topology, ARM ISA/backend optimization, threads, RAM bandwidth, quantization, context, and concurrent PC workload.
- Measure prompt and decode/task latency separately.
- Do not assume the CPU route is impractical solely because an NPU exists; compare the exact workload.
- If no useful supported accelerator path is intended, the generic `computers/cpu/` contract owns the deeper CPU-fit logic.

## Shared System Memory

- Treat Snapdragon X NPU/iGPU/CPU execution as consumers of shared system memory, not separate pools equal to installed RAM.
- Measure available RAM under Windows/app load, model/runtime peak, KV/cache, graphics/display use, and pagefile pressure.
- Account for temporary compilation/load buffers and first-app-load memory separately from steady inference where material.
- A model that fits only with substantial paging is not practical local fit.
- Do not assign a model tier from 16/32/64 GB installed RAM alone.

## Load and Initialization Cost

- Current AI Hub job reports distinguish first application load, subsequent load, and inference; preserve that distinction.
- For interactive assistants, first-load minutes can matter even when the profiled inference graph is fast.
- Measure cold app startup, model/context creation, compiled-context load, warm request, and repeated-session behavior on the user's machine.
- Include disk/cache footprint and rebuild/recompile cost after runtime/model changes.

## Context and KV Cache

- Include KV/cache and context growth in LLM memory evidence.
- Measure representative context lengths and number of concurrent sessions.
- Verify whether cache operations remain on the NPU/runtime path or involve CPU/system-memory work.
- Do not use a fixed-shape profile as evidence for the model's maximum advertised context.
- Record any context/output restrictions required for stable on-device use.

## Prompt and Decode Measurement

- Record at minimum:
  - cold/warm model/application load time;
  - TTFT;
  - prefill/prompt-processing latency/throughput;
  - sustained decode/task latency;
  - peak total system memory and any runtime-reported device memory;
  - actual NPU/GPU/CPU stage placement;
  - power/battery/thermals;
  - accepted-result quality.
- Compare routes using the same model revision/export/quantization/context when possible.
- Do not convert provider graph timings into tokens/s or whole-app latency unless the profile actually measures the corresponding complete stage.

## Multimodal and Media Pipelines

- Separate image classification/detection, VLM, speech, Stable-Diffusion-like generation, video, and LLM workloads.
- Current AI Hub evidence includes many independent vision/media graph profiles and individual diffusion components; this demonstrates platform capability but not complete pipeline latency.
- Include text/image encoders, UNet/transformer, VAE, preprocessing/postprocessing, scheduler/iterations, decoder, and output handling as applicable.
- Measure end-to-end accepted media generation/analysis rather than one NPU kernel/graph.

## Power, Battery, and Sustained Use

- Evaluate the exact execution mode under the intended Windows power profile.
- Compare NPU, GPU, and CPU on performance-per-accepted-result, not marketing efficiency claims.
- Measure sustained thermal behavior and fan/noise on retail laptops.
- Current AI Hub profiles can use high-performance/burst configurations, so they do not by themselves establish battery-life behavior.
- If a route is acceptable only on AC/high-performance mode, record that condition explicitly.

## Model Quality After Compilation/Quantization

- Validate the deployed QNN/ONNX/other artifact against an accepted reference on representative tasks.
- Quantization/export/compiler success does not prove semantic quality.
- Track accuracy/quality deltas, retries, and human correction cost.
- Do not preserve an NPU route only because it is efficient if the accepted-result quality is below threshold.

## Agent and Developer Workloads

- Account for IDE/browser/containers/build/test/database workloads and Windows memory pressure when the PC is also a development machine.
- Verify native ARM64 availability for agent tools and local dependencies, not only the model runtime.
- An otherwise fast model route can fail a coding/agent workflow because one required tool/plugin has no useful ARM64 path.
- Link software-engineer user scenarios when workflow ownership becomes primary.

## Practical Fit Outcomes

- `Fits well`: exact Snapdragon X SKU/Windows/runtime/artifact/context/workload passes complete-model support, quality, memory, latency, battery/power, and sustained-use thresholds.
- `Fits conditionally`: requires a particular compiled export, smaller context/model, NPU-only bounded workload, GPU/CPU fallback, AC mode, or another explicit acceptable constraint.
- `Does not fit`: exact route fails full-model compatibility, latency, memory, quality, power, tooling, or stability thresholds.
- `Unknown`: only subgraphs/components are profiled or the exact retail hardware/runtime/artifact lacks current measurement.
- Do not assign fit from AI Hub availability, NPU TOPS, model family, or installed RAM alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when the existing Snapdragon PC cannot meet model/tool quality or latency needs.
- Hybrid use can keep local preprocessing/private bounded tasks on-device while escalating approved difficult workloads.
- Compare setup/compilation complexity, ARM64 compatibility, power, retries, and correction time against hosted accepted-result economics.
- Do not recommend a replacement PC from this route; expose the exact compatibility/resource gap.

## Canonical Links

- Link model facts to Model Reference and runtime/software facts to canonical owners.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Route generic CPU-only evaluation to `computers/cpu/` when appropriate.
- Keep Android/mobile Qualcomm routes separate from Snapdragon Windows PCs.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Qualcomm AI Hub profile evidence for Snapdragon X Elite CRD/Windows 11/SC8380XP with current QAIRT/QNN and ONNX Runtime QNN execution, plus current Qualcomm/Windows local execution-provider ecosystem evidence.
- Current AI Hub evidence demonstrates explicit NPU execution for named compiled graph/model components and reports load/inference/memory metrics, but those component profiles are not automatically end-to-end LLM, diffusion, VLM, or application benchmarks.
- QAIRT/QNN, AI Hub, Windows/driver builds, Windows ML execution providers, model compilation/operator coverage, supported Snapdragon X SKUs, and ARM64 application support are mutable; recheck them before rendering recommendations.
- Exact retail PC/runtime/complete-model/context measurements and accepted-result quality remain the fit authority.

## Validation

- NPU, Adreno GPU, ARM64 CPU, and hosted service routes are not conflated.
- ARM64 application/tool compatibility is evaluated alongside model runtime compatibility.
- AI Hub graph/submodel timings are not presented as complete-application or LLM latency.
- Exact Snapdragon X SKU, Windows build, runtime versions, artifact, and compute unit are pinned.
- CPU/GPU fallback and preprocessing/postprocessing are included in end-to-end results.
- Shared system RAM is not labeled dedicated NPU/GPU memory.
- NPU TOPS and profile availability do not replace complete-model quality/latency/power evidence.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
