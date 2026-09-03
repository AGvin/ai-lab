# Documentation Requirements

## Route Fit

- Cover personal/workstation PCs where AMD Radeon discrete GPU, Ryzen integrated GPU, or Ryzen AI NPU is the intended local inference path.
- Require the exact GPU/APU/NPU SKU and architecture, OS, driver/software stack, runtime/backend, model artifact/export, precision/quantization, context, memory configuration, and intended compute unit before making a fit claim.
- Keep AMD Instinct/datacenter accelerator assumptions in the server route.
- Keep hardware purchasing outside this page. The reader starts from owned/fixed AMD client hardware.

## AMD Is Several Distinct Runtime Routes

- Separate at minimum:
  - Radeon/Radeon PRO GPU through ROCm/HIP-supported frameworks;
  - Ryzen AI integrated GPU through supported GPU runtimes such as `llama.cpp`/DirectML where documented;
  - Ryzen AI XDNA NPU through Ryzen AI Software/ONNX Runtime GenAI/Windows ML where supported;
  - hybrid NPU+iGPU execution where the current Ryzen AI stack supports it;
  - CPU fallback.
- Do not label all of these `ROCm` or assume an AMD AI PC uses the same software path as a discrete Radeon GPU.
- Current Ryzen AI Software 1.8 explicitly documents NPU-only, hybrid NPU+iGPU, GPU, and CPU LLM execution modes with different frameworks/compute allocation.
- Current Ryzen AI Software uses ONNX Runtime/VitisAI or related Windows ML paths for NPU workflows and `llama.cpp` for current GPU-only LLM acceleration in its documented execution-mode comparison.

## Exact ROCm Support Matrix First

- For Radeon GPU routes, verify the exact current ROCm/Radeon support matrix before selecting a framework/model.
- Current AMD ROCm documentation explicitly states that GPUs absent from the current support table are not officially supported.
- Current Linux matrices include selected RDNA3/RDNA4 Radeon and Radeon PRO devices; support is SKU- and OS-release-specific rather than architecture-wide.
- Current Windows matrices support only selected Radeon/Ryzen hardware and explicitly note that PyTorch-on-Windows packages include ROCm components while the entire ROCm stack is not supported on Windows.
- Do not transfer support from Linux to Windows/WSL, from one ROCm release to another, or from a supported neighboring SKU to an unlisted device.

## Linux, Windows, and WSL Are Separate Evidence Paths

- Record native Linux, native Windows, or WSL explicitly.
- Verify distribution/kernel/driver compatibility on Linux.
- Verify Windows version, AMD driver/HIP SDK or Ryzen AI Software, framework version, and supported SKU on Windows.
- Verify host driver, WSL distribution/kernel, ROCm release, and exact supported GPU when using WSL.
- Do not cite a working community HIP/Vulkan build as official ROCm support; label community/independent evidence separately.

## Current Radeon GPU Route

- Bind a Radeon recommendation to exact GPU architecture/LLVM target, current ROCm/HIP support, framework/runtime, precision, and model kernels.
- Current ROCm matrices distinguish `supported`, `deprecated`, and `unsupported`; preserve that status in fit evidence.
- A HIP runtime that starts on unsupported hardware does not prove prebuilt ROCm libraries/frameworks are supported.
- Measure model-level operator/kernel behavior because framework installation success is not task fit.
- Keep Vulkan/DirectML/other non-ROCm GPU routes distinct and label their support/performance evidence independently.

## Current Ryzen AI NPU Route

- Treat the XDNA NPU as a model/export-specific accelerator, not generic extra compute.
- Current Ryzen AI Software provides NPU model quantization, compilation/deployment, ONNX Runtime GenAI flows, supported-operator documentation, and LLM execution paths.
- Current documented LLM support is family/configuration-specific; older Ryzen AI generations are not automatically supported by the latest OGA/NPU path. Recheck the current Supported Configurations table for the exact processor.
- Require the exact model prepared/optimized for the current Ryzen AI execution mode rather than assuming an arbitrary PyTorch/GGUF model runs on the NPU.
- Keep unsupported model/operator/NPU combinations `Unknown`.

## NPU-Only vs Hybrid NPU+iGPU

- Current Ryzen AI Software 1.8 documents both NPU-only and hybrid NPU+iGPU LLM modes through ONNX Runtime GenAI.
- Treat these as separate performance/memory/power routes.
- Current documentation describes hybrid execution as dynamically splitting work across NPU and iGPU for prefill/decode performance; verify exact processor/model support before relying on it.
- Record which stages execute on NPU versus iGPU and any CPU fallback.
- Measure end-to-end TTFT, prompt processing, decode, host memory, iGPU memory/shared-memory pressure, NPU utilization, and power.
- Do not infer that hybrid mode is supported because both devices exist physically.

## Windows ML Route

- Treat Windows ML as another current execution-provider management route for supported ONNX models on Ryzen AI PCs.
- Current AMD Windows ML documentation requires current Windows 11/Windows App SDK/driver combinations and can dynamically obtain compatible execution providers.
- Record the selected execution-provider policy and verify the actual device used.
- Dynamic execution-provider download is an operational/network dependency; do not assume it works in disconnected/high-security environments without a separate deployment plan.
- A Windows ML API call that chooses `NPU` still requires exact model/operator/export compatibility.

## GPU Route on Ryzen AI APUs

- For integrated Radeon graphics, identify whether the chosen runtime uses ROCm/HIP, DirectML, Vulkan, or `llama.cpp` GPU backend and whether the exact APU is supported.
- Shared system memory is not dedicated VRAM; account for OS/app/model/KV/runtime allocations and memory bandwidth contention.
- Measure memory pressure, prompt/decode performance, battery/power, and concurrent display/application load.
- Do not transfer discrete-Radeon benchmark expectations to an APU iGPU.

## VRAM and Shared-Memory Accounting

- For discrete Radeon, measure peak VRAM including weights, KV/cache, runtime buffers, multimodal components, batch/concurrency, fragmentation, and display use.
- For APUs, measure peak shared system memory and bandwidth contention rather than inventing an equivalent VRAM capacity.
- Include host RAM for model loading, CPU fallback, NPU/iGPU hybrid use, and concurrent applications.
- A model that loads but drives heavy paging or unusable desktop contention is not practical fit.

## Model Artifact and Export

- Record exact producer/model/revision and runtime-native representation:
  - safetensors/PyTorch/ROCm stack;
  - GGUF/llama.cpp GPU route;
  - ONNX/quantized/compiled Ryzen AI NPU artifact;
  - Windows ML ONNX/QDQ or other supported export.
- Preserve conversion/quantization/compiler/tool versions and settings.
- Do not compare different export formats/quantizations as equivalent solely from parameter count or bit width.
- Validate accepted-result quality after quantization/conversion.

## Context and LLM-Specific Limits

- Include context/KV cache in memory and latency evidence.
- Current Ryzen AI documentation differentiates NPU LLM artifact types/execution modes with different context capabilities; treat those limits as exact artifact/runtime properties.
- Measure the user's actual prompt lengths and output lengths.
- Do not advertise the source model's maximum context when the NPU/GPU artifact/runtime supports less.
- Record any context reduction required for stable interactive performance.

## CPU/GPU/NPU Fallback and Partitioning

- Record where every material model stage executes.
- Measure unexpected CPU fallback because it can dominate latency/power while appearing functionally successful.
- Distinguish intended hybrid execution from unsupported-operator fallback.
- Use runtime profiling/device telemetry where available to prove accelerator use.
- Do not infer accelerator utilization from NPU/GPU presence in Task Manager alone.

## Prompt and Decode Measurement

- Record at minimum:
  - model/compiled-artifact load time;
  - TTFT;
  - prompt-processing latency/throughput at representative context;
  - sustained decode/task latency;
  - peak VRAM/shared RAM/host RAM;
  - device utilization and fallback;
  - sustained power/thermals;
  - accepted-result quality.
- Compare execution modes using the same model revision, effective quantization, context, sampling, and workload where possible.
- Do not compare vendor profile numbers from different model fragments/stages as full application latency.

## Power and Battery

- Treat NPU value as a measured performance-per-watt/availability result, not a marketing TOPS claim.
- Test laptop battery/AC power modes where on-device inference is intended during mobile use.
- Measure sustained temperature/frequency behavior on thin laptops and compact systems.
- Record whether hybrid/GPU modes materially affect battery life or fan noise compared with NPU-only.

## Multimodal and Media Workloads

- Separate text LLM, VLM, speech, image generation, and video workloads.
- Verify every encoder/decoder/model stage has a supported execution route.
- A model may partition across NPU/iGPU/CPU differently than a text LLM.
- Include complete pipeline latency/memory rather than one optimized NPU subgraph.

## Community and Alternative Backends

- Community-supported Vulkan/HIP/DirectML builds can be valuable when official ROCm/NPU support does not cover the device, but label them as independent/community routes.
- Do not upgrade community success to official AMD support.
- Record exact project/build/driver and regression risk.
- Prefer `Unknown` to claiming stable fit from one anecdotal run.

## Practical Fit Outcomes

- `Fits well`: exact AMD SKU/OS/runtime/device/artifact/context/workload passes support, memory, latency, power, quality, and sustained-use thresholds.
- `Fits conditionally`: requires a specific supported OS/runtime, reduced context, alternate GPU backend, NPU artifact, hybrid mode, CPU fallback, or another explicit acceptable constraint.
- `Does not fit`: exact route fails official/runtime support, memory, latency, quality, stability, or power thresholds.
- `Unknown`: exact hardware/runtime/artifact combination lacks current support or measurement.
- Do not assign a fit outcome from VRAM, system RAM, AI TOPS, or `Ryzen AI` branding alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when the existing AMD hardware cannot meet quality/context/latency needs.
- Compare local setup complexity, model conversion, driver/runtime constraints, correction time, and power against hosted accepted-result economics.
- Do not recommend replacement hardware here; expose the exact capability/resource/support gap.

## Canonical Links

- Link model facts to Model Reference and runtime/software facts to canonical owners.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Keep Instinct/server AMD routes separate.
- Link user scenarios when workflow/data needs rather than raw hardware fit become primary.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current AMD ROCm Linux/Windows Radeon/Ryzen support matrices, current ROCm release documentation, and current Ryzen AI Software 1.8/Windows ML/ONNX Runtime GenAI LLM documentation.
- Current AMD evidence confirms that client GPU support is exact-SKU/OS/release-specific; current Windows documentation explicitly distinguishes partial ROCm/PyTorch component support from the full ROCm stack. Current Ryzen AI documentation separately supports NPU-only, hybrid NPU+iGPU, GPU, and CPU LLM execution modes with model/configuration-specific requirements.
- ROCm, Radeon/Ryzen matrices, Ryzen AI Software, Windows ML execution providers, drivers, supported processor generations, model artifacts, and execution modes are mutable; recheck them before rendering recommendations.
- Exact hardware/runtime/artifact/context measurements and accepted-result quality remain the fit authority.

## Validation

- OS/hardware/runtime matrices are explicit.
- Radeon GPU, Ryzen iGPU, Ryzen AI NPU, hybrid NPU+iGPU, and CPU paths are not conflated.
- Linux support is not transferred to Windows/WSL and Instinct/server support is not transferred to consumer hardware.
- Windows PyTorch/ROCm component support is not described as the full ROCm stack.
- NPU presence/TOPS is not equated with arbitrary model compatibility.
- Shared-memory APUs are not treated as having dedicated VRAM equal to system RAM.
- Fallback/partition behavior is measured rather than inferred.
- Load success does not replace latency/power/quality evidence.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
