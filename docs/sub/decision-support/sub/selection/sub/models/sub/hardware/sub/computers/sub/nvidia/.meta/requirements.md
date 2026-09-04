# Documentation Requirements

## Route Fit

- Cover personal/workstation PCs where an NVIDIA GeForce/RTX/RTX PRO-class GPU is the intended local inference accelerator.
- Require the exact GPU SKU and architecture/compute capability, VRAM, OS, driver, CUDA/runtime backend, model artifact, precision/quantization, context/KV cache, modality, display load, and concurrent applications before making a fit claim.
- Keep datacenter HGX/DGX/accelerator assumptions in server routes unless the exact software explicitly supports the PC GPU.
- Keep GPU purchasing outside this page. The user starts from an already owned/fixed GPU.

## Current Runtime Boundary

- Distinguish at least three current local paths:
  - CUDA-backed general frameworks/runtimes;
  - TensorRT/TensorRT-RTX optimized deployment for supported models/operators;
  - lightweight local runtimes such as `llama.cpp` CUDA/GGUF.
- Current TensorRT for RTX documentation supports RTX-family hardware from Turing RTX 2000 through Ampere RTX 3000, Ada RTX 4000, and Blackwell RTX 5000 families, subject to its exact current support matrix.
- Current TensorRT-RTX packages are available for Windows and Linux and require matching CUDA/toolkit/driver combinations; current prerequisites list CUDA 12.9 Update 1 or CUDA 13.4 packages and architecture-specific driver requirements.
- Treat these versions as mutable evidence boundaries, not evergreen requirements.
- `llama.cpp` remains a current alternative with CUDA kernels, broad GGUF quantization support, CPU+GPU hybrid offload, and current multi-GPU CUDA support. It is a separate artifact/runtime route from TensorRT engines or PyTorch checkpoints.

## GPU and OS Matrix

- Record native Windows, Linux, or WSL explicitly.
- Do not infer that a CUDA/PyTorch/TensorRT workflow documented on Linux is supported identically on Windows or WSL.
- Verify the exact NVIDIA driver branch, CUDA toolkit/runtime, Python/framework/runtime version, and GPU compute capability.
- Distinguish packaged runtimes that bundle CUDA dependencies from development stacks that require a local toolkit.
- If WSL is used, include host Windows driver, WSL kernel/distribution, filesystem/data path, and runtime support in the evidence.

## VRAM Is a Peak Working-Set Constraint

- Measure peak VRAM instead of estimating from weight-file size.
- Include model weights, KV/cache, CUDA/runtime buffers, kernels/workspaces, attention/temp buffers, vision/audio encoders, VAE/diffusion components, adapter weights, batch/concurrency, allocator fragmentation, and display/application VRAM.
- Reserve operational headroom; a model that reaches near-total VRAM in a clean benchmark can fail or thrash under desktop use.
- Record host RAM too because CPU offload, model loading, pinned memory, and hybrid execution can consume substantial system memory.
- Treat out-of-memory/repeated allocator eviction as a practical failure boundary, not a tuning success.

## Display and Graphics Contention

- Measure inference with the actual desktop/gaming/creator load where the GPU also drives displays or graphics.
- Current TensorRT-RTX explicitly supports simultaneous compute and graphics but documents architecture-specific constraints and resource trade-offs; therefore an inference-only benchmark is not sufficient for a gaming/creator recommendation.
- Include foreground 3D rendering, video encoding/decoding, browser GPU use, creative applications, and multi-monitor/display memory where relevant.
- Record frame-time or application-responsiveness impact when local AI must coexist with interactive graphics.
- Do not reserve all VRAM for AI on a machine whose primary workload still needs the GPU.

## Architecture and Precision

- Record the exact GPU architecture because Tensor Core features, supported precision modes, kernel availability, and optimized runtimes differ by generation.
- Do not infer FP8/INT4/other acceleration from generic `RTX` branding; verify the exact runtime/model/operator support matrix for the selected architecture.
- A quantized artifact that fits memory but falls back to slow kernels or unsupported operators is not automatically a good fit.
- Keep unsupported or partially supported model/operator/precision combinations `Unknown` until verified.

## Model Artifact and Conversion

- Record exact model producer/family/revision, source checkpoint, runtime-native artifact, precision/quantization, tokenizer, adapters, and auxiliary components.
- For TensorRT/TensorRT-RTX engines, preserve framework/export source, ONNX or other intermediate where used, build configuration, optimization profiles, runtime version, and GPU architecture.
- Do not assume a TensorRT engine built for one architecture/runtime can be reused safely on another without documented compatibility.
- For GGUF/llama.cpp, preserve the exact quantization and llama.cpp build/backend.
- For PyTorch/safetensors, preserve framework/CUDA dependency versions and any quantization library/kernel requirements.

## Context and KV Cache

- Include context/KV cache in every fit calculation.
- Measure prompt-processing at the actual required context lengths, not only short prompts.
- Test decode separately from prompt ingestion.
- If KV-cache quantization or reduced context is required, record the quality/latency/memory trade-off explicitly.
- Do not advertise the base model's maximum context if the existing GPU cannot run that context with acceptable headroom and latency.

## CPU Offload and Hybrid Execution

- Treat CPU+GPU offload as a separate measured route rather than `extra VRAM`.
- Current `llama.cpp` supports CPU+GPU hybrid inference, but practical performance depends on layer placement, host RAM bandwidth, PCIe transfer, CPU capability, model architecture, and context.
- Record the GPU-resident proportion, host RAM peak, PCIe generation/link state where material, prompt/decode speed, and total accepted latency.
- Do not infer that a model larger than VRAM remains interactive merely because offload makes it load.

## Multi-GPU on Personal Workstations

- Treat multiple GPUs as a topology/runtime problem rather than summing VRAM.
- Verify whether the selected runtime/model supports tensor/data/pipeline parallelism or layer splitting on the exact GPU mix.
- Record PCIe topology, peer access, GPU architecture compatibility, per-GPU memory, display ownership, and communication overhead.
- Mixed GPU generations/capacities can constrain kernels, load balancing, or usable memory; measure rather than assuming additive capacity.
- If multi-GPU operation becomes shared infrastructure, route platform/serving concerns to server/internal-platform owners.

## Prompt and Decode Measurement

- Record at minimum:
  - cold/warm model load time;
  - time to first token;
  - prompt-processing tokens/s or task latency at representative contexts;
  - sustained decode tokens/s or task latency;
  - peak VRAM and host RAM;
  - GPU utilization/power/temperature;
  - quality on representative tasks.
- Use enough generation duration to expose sustained power/thermal behavior.
- Do not compare runtime performance with different context, batch, quantization, sampling, or model revision without labeling the difference.

## Thermal and Power Limits

- Measure sustained clocks/power/temperature on laptops and compact desktops where thermal limits can change throughput after the first minute.
- Record laptop AC/battery/power profile and external GPU/power constraints where applicable.
- Treat throttled sustained performance as the real operating result.
- Do not use a short burst benchmark as proof of long-running agent/media workload performance.

## Multimodal and Media Pipelines

- Separate text LLM, VLM, speech, image generation, video, and embedding/reranker workloads.
- Include all auxiliary model components and resolution/batch settings in VRAM measurement.
- For diffusion/video pipelines, measure complete generation latency and peak memory across text encoder, denoiser/transformer, VAE, upscaler/interpolator, and other stages.
- Do not infer media fit from LLM VRAM behavior.

## Runtime Compilation and Engine Build Cost

- Account for model conversion/engine-build time, disk footprint, cache, and rebuild requirements when using TensorRT/TensorRT-RTX or compiled kernels.
- Distinguish first-run compilation from steady-state inference.
- Preserve engine/artifact cache version and invalidate/rebuild after incompatible runtime/driver/model changes.
- Include build failures or unsupported operators in route evaluation; do not hide them behind a theoretical hardware-support claim.

## Agent and Developer Workloads

- For coding/agent workflows, measure model inference concurrently with IDE, browser, containers/VMs, build/test jobs, local databases, and display use.
- A GPU that fits a model in isolation may be a poor developer route if system responsiveness, Docker/VM memory, or build workload is degraded.
- Link the relevant software-engineer/local-GPU user scenario when workflow ownership becomes primary.

## Quality and Quantization Acceptance

- Evaluate quantized/local artifacts on the user's representative tasks against an accepted reference.
- Track factual/coding/reasoning/media quality, retry rate, and human correction effort.
- Do not preserve a quantization only because it enables memory fit if accepted-result quality falls below the threshold.
- Compare cost per accepted result, not tokens/s alone.

## Practical Fit Outcomes

- `Fits well`: exact GPU/runtime/artifact/context/workload passes quality, VRAM/headroom, latency, sustained-thermal, and desktop-contention thresholds.
- `Fits conditionally`: requires reduced context, lower quantization, partial CPU offload, closing GPU-heavy applications, reduced resolution/batch, or another explicit acceptable constraint.
- `Does not fit`: exact route fails support, memory, latency, quality, thermals, modality, or stability thresholds.
- `Unknown`: exact GPU/OS/runtime/artifact combination lacks current official/independent measurement.
- Do not assign any outcome from VRAM size or `RTX` generation alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when the existing GPU cannot meet quality/context/latency needs.
- Compare local power, engineering/tuning time, model-download/storage, retries, and desktop contention against hosted accepted-result economics.
- Do not recommend a replacement GPU from this route; identify the resource/capability gap and hand hardware procurement elsewhere if the owner later asks.

## Canonical Links

- Link model facts to Model Reference and runtime/software facts to their canonical owners.
- Link `decision-guides/local-resource-fit/` for model-first evaluation.
- Link local-GPU gamer/developer/creator scenarios when user workflow rather than hardware fit is the primary question.
- Keep server/datacenter NVIDIA routes separate.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current NVIDIA TensorRT for RTX 1.6 installation/prerequisite/simultaneous-compute-and-graphics documentation and current `llama.cpp` CUDA/backend/feature documentation.
- Current TensorRT-RTX evidence explicitly supports RTX hardware families from Turing through current Blackwell with exact CUDA/driver prerequisites and documents graphics/inference coexistence constraints. Current `llama.cpp` evidence supports CUDA, quantized GGUF, CPU+GPU hybrid inference, and current multi-GPU CUDA capability.
- TensorRT/TensorRT-RTX, CUDA, drivers, GPU support matrices, precision/operator support, llama.cpp kernels/features, and model artifacts are mutable; recheck them before rendering recommendations.
- Exact GPU/runtime/artifact/context/contention measurements and accepted-result quality remain the fit authority.

## Validation

- Nominal VRAM/load success does not equal practical fit.
- Exact GPU architecture, OS, driver, CUDA/runtime, artifact, context, and desktop contention are pinned.
- TensorRT-RTX hardware support is not misrepresented as automatic model/operator support.
- Datacenter/server assumptions are not imported to GeForce/RTX PCs without evidence.
- Simultaneous graphics/inference contention is measured for shared desktop GPUs.
- CPU offload and multi-GPU are measured routes rather than additive-memory shortcuts.
- Prompt processing, decode, peak memory, thermals, and accepted quality are all measured.
- Buying advice remains outside model-selection ownership.
- Mutable current evidence carries the 2026-08-24 boundary.
