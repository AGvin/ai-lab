# Documentation Requirements

## Route Fit

- Cover Intel personal/workstation PCs where Intel CPU, integrated/discrete Intel GPU, or Intel NPU is the intended local inference path.
- Require the exact processor/platform generation, NPU/iGPU/dGPU model, OS, driver, OpenVINO/Windows ML/other runtime, model/export, precision/quantization, context, memory configuration, and selected execution device before making a fit claim.
- Route a PC using an NVIDIA/AMD accelerator through that accelerator's hardware route when it is the intended inference path.
- Keep Intel Xeon/datacenter accelerator assumptions in server routes and keep PC purchasing outside this page.

## Intel PC Is a Multi-Device Route

- Distinguish CPU, GPU, NPU, AUTO/multi-device orchestration, and any explicit heterogeneous/partitioned execution.
- Current OpenVINO 2026.3 supports Intel Core Ultra processor families and exposes separate CPU, GPU, and NPU devices with model/device-specific verification.
- Do not treat `AI PC`, `Core Ultra`, or a published platform TOPS number as proof that the intended model runs on the NPU.
- Verify the actual device selected at runtime and any fallback/partition behavior.
- Route to `cpu/` when no useful supported Intel accelerator path exists for the intended workload.

## Current OpenVINO Boundary

- Treat OpenVINO as the current first-party Intel cross-device inference route, with OpenVINO GenAI providing current generative-model pipelines.
- Current OpenVINO 2026.3 release notes add/extend specific model families independently across CPU, GPU, and NPU; model support is therefore device-specific rather than framework-wide.
- Current OpenVINO verified-model documentation reports device-level verification and precision separately for CPU/GPU/NPU. Treat `verified` as compatibility evidence, not proof of acceptable quality/latency for the user's task.
- Preserve the exact OpenVINO/OpenVINO GenAI/Optimum Intel versions because supported models, kernels, export requirements, and device behavior change between releases.

## NPU Hardware and Driver Boundary

- Treat the Intel NPU as a separate low-power accelerator introduced with Core Ultra-class platforms, not as generic GPU-equivalent compute.
- Current OpenVINO NPU documentation requires an NPU driver and documents current supported host/OS combinations; recheck exact platform and OS support before recommendations.
- Current NPU documentation names Windows 11 and Ubuntu/Linux driver requirements and notes that the NPU compiler path changed across recent OpenVINO releases.
- Record processor/NPU generation, driver version, OS/kernel, OpenVINO release, and compiler path.
- Do not transfer NPU support from one Core Ultra generation or OS release to another without current evidence.

## Model Export Is Part of NPU Compatibility

- Require a model artifact/export that the current NPU path supports.
- Current OpenVINO GenAI NPU documentation uses Optimum Intel/OpenVINO export and requires specific 4-bit weight-compression settings for current LLM NPU deployment.
- Current documentation distinguishes INT4 and NF4 support and notes that NF4 is supported on Core Ultra Series 2 NPU generations and newer rather than universally across all NPUs.
- Preserve the source model/revision, export tool/version, quantization method, group size, calibration/data-aware method where used, and resulting OpenVINO artifact.
- Do not assume an arbitrary PyTorch, GGUF, ONNX, or Hugging Face checkpoint can run efficiently on the NPU without the required export/compile path.

## Verified Model Does Not Equal Practical Fit

- Use Intel's current verified-model table as compatibility evidence only.
- Check the exact model, precision/export, inferred-with path, and CPU/GPU/NPU result instead of relying on the model family name.
- Some current LLMs are verified on CPU/GPU but not NPU; others have different supported precisions by device.
- Mark unverified combinations `Unknown` unless independent measurements establish a usable route and label those measurements separately from official support.
- Do not generalize support from a smaller/older sibling model to a larger/newer variant.

## Memory Is Shared Differently by Device

- CPU and integrated GPU/NPU paths use system memory differently from a discrete-VRAM GPU route.
- Record installed RAM, usable memory under normal applications, memory bandwidth/channel configuration where material, model/KV/runtime peak, and pagefile/swap pressure.
- Do not call total system RAM `NPU memory` or `GPU VRAM`.
- For iGPU/NPU workflows, measure complete host-memory pressure and application contention.
- Treat heavy paging or application starvation as a practical fit failure even if inference completes.

## Context and Memory Scaling

- Include context/KV cache in every LLM fit measurement.
- Current OpenVINO 2026.3 NPU guidance notes that on Core Ultra Series 2, systems may need more than 16 GB RAM for prompts over 1024 tokens with models above roughly 7B in the documented examples. Preserve this only as a provider-specific current example, not as a universal RAM tier or minimum.
- Measure the user's actual prompt and output lengths with the exact model/export/device.
- Record any context reduction required for stable execution.
- Do not present the source model's advertised maximum context as locally available when the selected Intel route cannot sustain it.

## CPU Route

- For CPU execution, identify exact CPU generation, instruction-set support, memory bandwidth/topology, OpenVINO or other CPU backend, threads, model artifact, and quantization.
- Measure prompt processing and decode separately because CPU bottlenecks can differ.
- Keep CPU performance evidence distinct from NPU/iGPU results even on the same Core Ultra processor.
- If another mature CPU runtime materially outperforms OpenVINO for the exact artifact/task, label it as an independent alternate runtime rather than assuming OpenVINO must win because the hardware is Intel.

## Intel GPU Route

- Identify exact integrated/discrete Intel GPU generation and graphics driver.
- Verify OpenVINO GPU/plugin or other backend support for the exact model/operators/precision.
- Account for shared system memory on integrated graphics and desktop/display contention.
- For discrete Intel graphics, measure actual device memory and host-memory/offload behavior rather than importing iGPU assumptions.
- Do not infer GPU support from CPU support in the verified-model table.

## NPU Route

- Evaluate NPU for low-power/local workloads only when the model/export/operator path is current and supported.
- Measure end-to-end TTFT, prompt processing, decode/task latency, host memory, NPU utilization, power, and accepted-result quality.
- Do not optimize only for NPU utilization or efficiency if the resulting model/context/quality is materially worse.
- Compare NPU against iGPU/CPU on the same machine for the real workload instead of assuming NPU is automatically the best route.

## AUTO and Multi-Device Execution

- Treat OpenVINO AUTO/multi-device orchestration as a separate route that can select or distribute work across available devices according to current runtime behavior.
- Record the actual selected device(s) and execution policy rather than writing `AUTO` as if it were a hardware identity.
- Verify whether model stages remain on one device, switch, or partition and whether fallback changes latency/power/memory materially.
- A successful AUTO result does not prove NPU execution.
- Use profiling/runtime device information to demonstrate where work actually ran.

## Fallback and Unsupported Operators

- Detect CPU/GPU fallback or unsupported subgraphs/operators where possible.
- Distinguish intended heterogeneous execution from accidental fallback.
- Measure end-to-end latency because a small unsupported stage can dominate total response time.
- Do not claim NPU fit when most material computation executes elsewhere.
- Keep unsupported/unmeasured operator combinations `Unknown`.

## Windows and Linux Are Separate Paths

- Record native Windows or Linux explicitly.
- Verify current NPU/GPU drivers, kernel requirements, OpenVINO packages, and framework integrations for the selected OS.
- Current Intel NPU guidance requires a supported NPU driver and documents Linux kernel/OS constraints independently from Windows.
- Do not transfer Windows driver/model behavior to Linux or vice versa.
- If WSL is used, treat it as a distinct host/guest runtime path and verify accelerator exposure/support instead of assuming native-Linux parity.

## Windows ML Route

- Treat Windows ML as an additional Windows execution-provider/orchestration route when the application targets that API.
- Verify exact Intel execution-provider/device support and actual provider chosen at runtime.
- Dynamic execution-provider acquisition can create network/update dependencies; account for them in disconnected/high-security scenarios.
- Do not infer that a Windows ML model uses the NPU merely because the PC has one.
- Keep OpenVINO-native and Windows ML deployment evidence separate.

## Prompt and Decode Measurement

- Record at minimum:
  - cold/warm model load;
  - TTFT;
  - prompt-processing latency/throughput at representative contexts;
  - sustained decode or task latency;
  - peak host/device memory;
  - selected device and fallback/partition behavior;
  - sustained power/thermals;
  - accepted-result quality.
- Compare devices using the same model revision/export/quantization/context/sampling where practical.
- Do not compare provider benchmark numbers that use different hardware, model precision, input size, or runtime settings as though they were device-only differences.

## Current Intel Benchmark Evidence

- OpenVINO publishes current AI-PC generative performance data across specific Core Ultra processors/models/precisions/input sizes.
- Use those measurements only as candidate/device evidence and record their exact processor, precision, input size, and metric definition.
- Do not convert a provider latency table into expected performance on another Core Ultra SKU.
- Re-benchmark locally under the user's memory/application/power conditions before assigning fit.

## Power and Battery

- Measure performance-per-watt only from the actual workload and device route.
- On laptops, compare AC and intended battery/power modes where mobile local AI matters.
- Record sustained temperature/frequency/fan behavior.
- A route that is fast but causes unacceptable battery drain or thermal throttling can be conditionally unsuitable.
- Do not use platform NPU TOPS as a substitute for measured energy/latency.

## Multimodal and Multi-Model Workloads

- Separate LLM, VLM, speech, embedding/reranker, image-generation, and other workloads because current CPU/GPU/NPU support differs by model and stage.
- Include all encoders/decoders/preprocessors and their execution devices in memory/latency evidence.
- Current OpenVINO release notes can add one model to CPU/GPU/NPU while another remains CPU/GPU-only; preserve per-model evidence.
- Measure concurrent resident models for RAG/agents rather than summing standalone memory estimates.

## Quality After Quantization/Export

- Compare NPU/GPU/CPU artifacts against an accepted quality reference on representative tasks.
- Current OpenVINO NPU export guidance describes several INT4/NF4 compression strategies with different accuracy implications; choose by measured accepted quality, not by memory alone.
- Track retry/correction rate when a smaller or more aggressively compressed model is used.
- A model that is very fast on NPU but fails the task-quality threshold does not fit.

## Practical Fit Outcomes

- `Fits well`: exact Intel platform/OS/driver/runtime/device/artifact/context/workload passes support, quality, memory, latency, power, and sustained-use thresholds.
- `Fits conditionally`: requires a specific export/quantization, smaller context/model, iGPU instead of NPU, CPU fallback, alternate runtime, or another explicit acceptable constraint.
- `Does not fit`: exact route fails device/model support, memory, latency, quality, stability, or power thresholds.
- `Unknown`: exact platform/device/runtime/artifact combination lacks current support or measurement.
- Do not assign fit from NPU presence, RAM capacity, AI-PC branding, or TOPS alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when the existing Intel PC cannot meet quality/context/latency needs.
- Compare local model conversion/driver/runtime complexity, power, retries, and human correction against hosted accepted-result economics.
- Do not recommend a replacement computer here; expose the exact capability/support/resource gap.

## Canonical Links

- Link model facts to Model Reference and runtime/software facts to their canonical owners.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Route generic CPU-only use to `computers/cpu/` when no useful accelerator path is intended.
- Link user scenarios when workflow/data requirements rather than hardware fit become primary.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current OpenVINO 2026.3 release notes, system requirements, NPU-device documentation, OpenVINO GenAI-on-NPU export/quantization guidance, current verified-model tables, and current Intel AI-PC generative-performance data.
- Current evidence confirms distinct CPU/GPU/NPU support and device-specific verified model/precision combinations; current NPU deployment requires exact export/quantization and driver/platform conditions. Provider memory/performance notes are configuration-specific rather than universal hardware tiers.
- OpenVINO, OpenVINO GenAI, Optimum Intel, NPU drivers/compiler, GPU drivers, verified-model lists, quantization formats, Windows ML providers, and Core Ultra support are mutable; recheck them before rendering recommendations.
- Exact platform/runtime/device/artifact/context measurements and accepted-result quality remain the fit authority.

## Validation

- CPU, Intel GPU, NPU, AUTO/multi-device, and fallback routes are not conflated.
- NPU presence/AI-PC branding/TOPS are not treated as model compatibility evidence.
- Exact model export/quantization is part of NPU fit.
- Verified-model status is compatibility evidence, not task-quality or latency proof.
- Provider-specific RAM/context notes are not generalized into universal memory tiers.
- Actual execution device and fallback/partition behavior are measured.
- Windows/Linux/WSL paths are not transferred without evidence.
- Prompt/decode, memory, power, thermals, and accepted quality are all measured.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
