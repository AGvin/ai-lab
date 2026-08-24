# Documentation Requirements

## Route Fit

- Cover Rockchip-based SBCs where an integrated Rockchip RKNPU is the intended local accelerator, independent of board OEM/brand.
- Require the exact Rockchip SoC/platform, board/BSP/kernel/NPU driver, RKNN or RKLLM toolkit/runtime version, host conversion environment, model architecture/revision, export/quantization, device RAM, context, NPU-core configuration, cooling, and target latency before assigning fit.
- Keep board brands such as Radxa, Orange Pi, Firefly, FriendlyElec, and others in one Rockchip route when they share the same SoC/runtime behavior; split only when board-specific power/cooling/PCIe/memory/BSP constraints materially change model selection.
- Keep SBC purchasing outside this route.

## Current Upstream Source Boundary

- Use the current `airockchip` repositories as the first-party Rockchip software source.
- The former `rockchip-linux/rknn-toolkit2` repository is explicitly marked unmaintained and moved to `airockchip/rknn-toolkit2`; do not use its older 1.6.0 state as current compatibility evidence.
- Current RKNN-Toolkit2 reports version **v2.3.2** and current RKNN-LLM reports **v1.3.0** as of the 2026-08-24 evidence boundary.
- Preserve exact repository/release/tool versions because supported platforms, models, operators, quantization, and runtime behavior evolve independently.
- Recheck upstream before rendering any current support claim.

## RKNN and RKLLM Are Separate Routes

- Treat **RKNN-Toolkit2/RKNN Runtime** as the current Rockchip route for supported conventional neural networks, vision, detection, segmentation, OCR, and other RKNN-compatible graphs.
- Treat **RKLLM-Toolkit/RKLLM Runtime** as the separate current route for supported LLM and multimodal language-model families.
- Do not infer LLM support from RKNN transformer/operator improvements alone.
- Do not treat an `.rknn` and `.rkllm` artifact as interchangeable or assume one runtime can load the other format.
- For a mixed VLM application, preserve every RKNN and RKLLM component and their handoff explicitly.

## Current Platform Matrix

- Pin the exact supported Rockchip platform in the current toolkit release.
- Current RKNN-Toolkit2 supports current platform families including RK3588, RK3576, RK3566/RK3568, RK3562, RV1103/RV1106, RV1103B/RV1106B, RV1126B, and RK2118, with older NPUs routed to older Rockchip toolchains.
- Current RKLLM v1.3.0 lists RK3588, RK3576, RK3562, and RV1126B as supported LLM platforms.
- Do not transfer RKNN support to RKLLM or assume every RKNN-supported SoC can run current RKLLM models.
- Do not transfer a model/runtime result from RK3588 to RK3576/RK3562/RV1126B without exact support and measurement.

## Exact SoC Before Board Brand

- Record the exact SoC and NPU generation/core topology rather than only the board product name.
- RK3588-class boards can expose multi-core NPU execution while other Rockchip platforms have different NPU resources and runtime behavior.
- Current RKLLM multimodal examples explicitly use `num_npu_core=3` for RK3588; treat that as an exact platform/example configuration rather than a generic Rockchip value.
- Verify core-mask/core-count options and runtime defaults for the selected SoC/model.
- Do not infer practical throughput from published SoC TOPS.

## BSP, Kernel Driver, and Userspace Runtime Are Coupled

- Treat the board's kernel/RKNPU driver and userspace RKNN/RKLLM runtime libraries as part of compatibility.
- Record kernel/BSP version, RKNPU driver version, `librknnrt`/RKNN Runtime or `librkllmrt` version, firmware where applicable, and distribution image.
- Different board vendors can ship different BSP/kernel/NPU-driver combinations for the same SoC; verify the actual image rather than assuming SoC equivalence guarantees runtime equivalence.
- Re-test after kernel/BSP/runtime updates.
- Keep driver/runtime mismatches as compatibility failures rather than model-quality failures.

## Host Conversion and Board Runtime Are Separate

- Current RKNN flow requires model conversion on a development computer with RKNN-Toolkit2, followed by board inference through RKNN Runtime C/C++ or RKNN-Toolkit-Lite2 Python APIs.
- Current RKLLM flow similarly converts/quantizes the source model on a host computer with RKLLM-Toolkit and then deploys the `.rkllm` artifact through RKLLM Runtime on the Rockchip target.
- Record host OS/Python/toolkit version separately from target Linux/Android runtime.
- Do not assume the complete conversion toolchain should or can run on the SBC itself.
- Preserve the source model and conversion environment as part of the deployed artifact provenance.

## Current Host Toolkit Requirements

- Current RKNN-Toolkit2 v2.3.2 supports a broad Python 3.6–3.12 host-toolkit range according to current upstream documentation; exact supported host OS/package combinations remain release specific.
- RKLLM model conversion has model-specific Python/dependency constraints; for example current upstream notes that RWKV conversion requires a specific Python version.
- Treat converter requirements as artifact-build constraints, not target-board runtime requirements.
- Pin Python, PyTorch/Transformers/ONNX dependencies where the conversion path depends on them.
- Do not upgrade host dependencies independently without revalidating conversion output.

## RKNN Deployable Artifact

- Treat `.rknn` as the Rockchip-deployable result of model parsing, optimization, quantization, and target-platform compilation.
- Preserve source framework/model/revision, ONNX/TFLite/other intermediate where used, input shapes, preprocessing configuration, target platform, quantization method/calibration dataset, toolkit version, and final RKNN artifact hash.
- Do not equate successful ONNX/PyTorch export with NPU compatibility.
- Unsupported operators, graph partitioning/custom operators, dynamic-shape limits, and conversion warnings remain explicit fit evidence.
- Validate task quality after conversion/quantization.

## RKLLM Deployable Artifact

- Treat `.rkllm` as a separate compiled/quantized LLM artifact produced for a named target platform.
- Preserve exact source Hugging Face model/revision, tokenizer/chat template, RKLLM-Toolkit version, target platform, selected NPU core count, quantized data type/algorithm, calibration data, context-related options, and artifact hash.
- Current upstream conversion examples explicitly build target-specific `.rkllm` files such as RK3588 W8A8 artifacts rather than loading source weights directly on the board.
- Do not infer portability of an `.rkllm` artifact to another SoC or RKLLM Runtime version without current compatibility evidence.
- Evaluate the compiled artifact semantically against the source/reference model.

## Current RKLLM Model Families

- Use the current RKLLM upstream supported-model list only as candidate compatibility evidence.
- Current v1.3.0 support includes families such as Llama/TinyLlama, Qwen2/Qwen2.5/Qwen3/Qwen3.5, Phi2/Phi3, Gemma2/Gemma3/Gemma3n/Gemma4, MiniCPM, InternLM, DeepSeek-R1-Distill, RWKV7, and current multimodal families such as Qwen2-VL/Qwen3-VL and InternVL/SmolVLM-class models.
- Do not infer every checkpoint, parameter size, context, tokenizer variation, quantization, or fine-tune in a named family is supported.
- Record the exact supported architecture/checkpoint used by the converter.
- A larger sibling or new revision remains `Unknown` until conversion/runtime evidence exists.

## Current RKLLM v1.3.0 Changes

- Treat RKLLM v1.3.0-specific capabilities as current mutable evidence.
- Current v1.3.0 adds support for newer families including Qwen3.5, Gemma4, and SmolLM3 and improves multimodal input, cache reuse, long-context decode on selected platforms, tokenizer/embedding callbacks, OpenAI-compatible server behavior, and inference sampling controls.
- Current release notes also include RK3588-specific numerical-overflow fixes, demonstrating why runtime version belongs in the compatibility key.
- Do not apply v1.3.0 behavior to an older board image shipping an earlier RKLLM Runtime.

## GGUF Conversion Does Not Mean llama.cpp Runtime

- Current RKLLM release notes include conversion support from selected GGUF inputs such as FP16/Q4_0.
- Treat GGUF here as a possible **source/import format for RKLLM conversion**, not evidence that the board executes that GGUF through RKLLM directly or that RKLLM is llama.cpp-compatible.
- Preserve the final `.rkllm` artifact and conversion options.
- If `llama.cpp` is separately used on the Arm CPU/GPU, evaluate it as a different runtime path and do not mix its model-performance evidence with RKLLM NPU execution.

## Quantization and Quality

- Record weight/activation quantization such as W8A8/W4A16 or current supported schemes, algorithm, calibration dataset, and mixed/grouped quantization options.
- Current RKLLM release evolution explicitly adds/changes quantization algorithms to improve low-bit quality; preserve the release/tool configuration.
- Compare generated answers, coding/reasoning quality, multilingual behavior, tool calls, and VLM quality against an accepted reference.
- Do not select the lowest-bit artifact solely because it fits memory or is faster.
- Track retry/correction burden together with decode performance.

## Conventional RKNN Operator Coverage

- For non-LLM RKNN models, verify exact current operator/ONNX-opset/dynamic-shape/data-type support in the selected RKNN-Toolkit2 release.
- Current v2.3.2 improves graph optimization/einsum/norm and mixed precision while platform-specific operator restrictions still apply.
- Do not infer arbitrary transformer or diffusion support from the presence of MatMul/LayerNorm/GELU improvements.
- Use custom CPU/GPU operators only when their deployment/runtime cost is measured and acceptable.
- Keep material CPU fallback/host postprocessing visible.

## Multimodal VLM Is a Multi-Artifact Pipeline

- Current RKLLM upstream multimodal examples demonstrate split pipelines in which an image encoder is deployed as an `.rknn` model and the language component as an `.rkllm` model.
- Current Qwen2-VL example converts the language model for RK3588 and runs a separate vision RKNN encoder, then passes image features into the RKLLM runtime.
- Preserve exact vision encoder, language model, image-token generation, embedding/features, context settings, NPU-core allocation, and handoff.
- Do not present VLM latency as only the language decode time.
- Include image preprocessing, RKNN encoder time, host transfers, RKLLM prefill/decode, and output processing.

## Context and KV Cache

- Record the deployed RKLLM maximum context and runtime parameters, not only the source model's advertised context.
- Current multimodal examples explicitly require `max_context_len` to exceed text tokens + image tokens + requested new tokens; preserve this complete token budget.
- Measure memory and latency across representative context lengths.
- Current RKLLM release notes include context/cache-specific bug fixes and long-context optimization, so context behavior is version/platform specific.
- If context must be reduced substantially for stable memory/latency, mark fit conditional.

## Prompt and Decode Measurement

- Measure at minimum:
  - model/runtime initialization;
  - tokenizer/input preparation;
  - prompt/prefill latency and TTFT;
  - sustained decode/TPS or TPOT;
  - input/context/output lengths;
  - peak host/system memory;
  - NPU utilization/core configuration where observable;
  - thermals/power;
  - accepted-result quality.
- Do not report one decode tokens/s result as complete interactive latency.
- Compare exact same artifact/runtime/context when evaluating board/BSP differences.

## Board Memory Is Shared System Memory

- Treat RK3588/RK3576 SBC RAM as host/system memory shared by Linux/Android, CPU, GPU, NPU runtime buffers, model files/caches, VLM features, applications, and other services.
- Do not call total board RAM NPU VRAM.
- Measure peak whole-system memory under the complete model/application.
- Larger RAM variants can increase feasible resident state/context but do not guarantee faster NPU execution.
- Heavy swap is not a normal substitute for practical memory fit.

## NPU Core Configuration on RK3588

- RK3588 exposes multiple NPU cores and current RKNN/RKLLM APIs can use explicit core configuration.
- Preserve selected core mask/core count and whether the model is partitioned or scheduled across cores.
- Do not multiply single-core throughput by three without measurement.
- Multi-core execution can change memory, scheduling, and latency and remains model/toolkit specific.
- Keep core-selection differences explicit in benchmark records.

## CPU, GPU, and NPU Work Split

- Record preprocessing/postprocessing, tokenizer, sampling, image/audio transforms, custom operators, and other host CPU/GPU work separately from NPU inference.
- A successful RKNN/RKLLM output does not mean every stage was accelerated on RKNPU.
- Measure complete application latency and CPU utilization.
- For mixed vision + language + retrieval/agent applications, include database/network/tool work as well.
- Avoid describing an NPU benchmark as whole-board application performance.

## Board/OEM BSP Fragmentation

- Different RK3588/RK3576 SBC vendors can ship different kernels, RKNPU driver versions, device trees, GPU drivers, thermal governors, power policies, and userspace libraries.
- Record exact board image/BSP build.
- Re-test after vendor OS or kernel upgrades.
- A model artifact can be valid for the SoC yet fail due to a stale/incompatible NPU driver/runtime on one board image.
- Board branding does not justify a separate model-selection route unless those constraints consistently change decisions.

## Mainline vs Vendor Kernel Boundary

- Verify current RKNPU driver/runtime availability before selecting a mainline/community Linux image.
- Do not assume a general Linux kernel with working CPU/GPU automatically exposes the Rockchip NPU to current proprietary/userspace RKNN/RKLLM runtime.
- Preserve vendor BSP or tested mainline integration as part of the deployment evidence.
- Keep unsupported community NPU stacks separate from official RKNN/RKLLM support.

## ARM64 Application Dependencies

- Verify all native libraries on the board for aarch64: RKNN/RKLLM runtime, tokenizer, image/audio libraries, vector databases, browsers, automation, Python extensions, and application dependencies.
- Current upstream demos provide Linux-aarch64/Android deployment paths; preserve the actual OS/runtime target.
- Do not assume an x86 host package can be copied to the board.
- Keep missing critical Arm dependencies as route blockers even when model conversion succeeds.

## Linux and Android Are Separate Targets

- Current RKLLM demos include Linux-aarch64 and Android deployment builds; record the actual target OS.
- Verify library paths, runtime binaries, NPU driver, permissions, JNI/NDK integration, and application lifecycle separately.
- Do not transfer Linux performance/compatibility directly to Android.
- For Android, include process memory/lifecycle and OEM system integration.

## OpenAI-Compatible Server Is an Interface, Not Model Portability

- Current RKLLM v1.3.0 improves `rkllm_server_demo` compatibility with OpenAI-style APIs.
- Treat this as an API/service wrapper around supported RKLLM artifacts, not evidence that arbitrary OpenAI/Ollama/GGUF models are portable to RKNPU.
- Add authentication/network limits before exposing a board inference server beyond localhost/trusted LAN.
- Measure concurrent sessions, KV-cache/memory, and p50/p95 latency.
- A one-user demo is not a multi-user service benchmark.

## Cooling and Power

- Measure sustained inference on the exact SBC/case/cooler/power supply.
- RK3588 boards can throttle under sustained CPU/NPU/GPU workloads depending on board cooling/power policy.
- Record SoC/NPU temperature, frequency, throttling, and long-run throughput where tooling permits.
- Include NVMe/USB/camera/peripheral power and host CPU work.
- Do not use an open-bench short run as proof of 24/7 server/edge performance.

## Storage and Artifact Lifecycle

- Include source/converted model packages, `.rknn`/`.rkllm` artifacts, runtime libraries, calibration assets, caches, retrieval indexes, logs, and update headroom.
- Preserve artifact hashes and source/converter/runtime version provenance.
- Define rollback after toolkit/runtime/BSP updates.
- Prestage artifacts for offline use and avoid hidden model-hub downloads where network-independent operation is required.
- Do not use slow removable-storage swap as ordinary model memory expansion.

## Vision/Media Pipelines

- RK3588-class SoCs include powerful media/ISP/GPU blocks in addition to RKNPU, but treat those as separate pipeline resources.
- Include camera/video decode/resize/color conversion, NPU inference, CPU postprocessing, overlays/streaming/storage in end-to-end measurements.
- Do not infer model FPS from hardware codec or NPU TOPS alone.
- For multiple camera streams, measure actual concurrent throughput and dropped-frame/p95 latency.

## Multiple Models and Concurrency

- Measure actual resident memory and NPU scheduling when multiple RKNN/RKLLM models or sessions coexist.
- Do not sum standalone model throughput as a concurrency guarantee.
- Record core assignment, host RAM, context/KV per session, and CPU/GPU support work.
- Sequential load/unload can be preferable when memory is constrained; include startup/reload cost.
- Shared-service use should report p50/p95 rather than one-session average throughput.

## Prompt Injection and Edge Actions

- Local Rockchip inference does not make tool-capable agents safe.
- Treat web/documents/camera OCR/messages/files/model output as untrusted when the application can control GPIO, robotics, automation, shell, network, or accounts.
- Use deterministic tool allowlists, argument validation, permissions, confirmation, and safety interlocks.
- A local VLM/LLM result does not authorize physical or account actions.

## Quality and Accepted Result

- Evaluate converted artifacts on representative task data after quantization and toolchain lowering.
- Track model quality, VLM perception, refusals, function-call/tool accuracy, retries, and human correction time.
- Vendor-supported architecture and successful conversion are compatibility evidence, not accepted-result proof.
- Compare compact NPU models against CPU and hosted alternatives when those are viable.

## Practical Fit Outcomes

- `Fits well`: exact Rockchip SoC/BSP/driver/toolkit/runtime/artifact/context/core configuration passes supported-model conversion, accepted quality, memory headroom, TTFT/decode/task latency, sustained thermals, and whole-application requirements.
- `Fits conditionally`: requires a specific BSP/runtime tuple, supported compact model, lower quantization, reduced context, explicit core count, CPU/GPU postprocessing, active cooling, or another acceptable constraint.
- `Does not fit`: exact route fails platform/model support, conversion/operator coverage, runtime/driver compatibility, memory, latency, quality, or sustained deployment constraints.
- `Unknown`: exact SoC/toolkit/runtime/model/BSP combination lacks current upstream or independent measurement.
- Do not assign fit from NPU TOPS, board RAM, parameter count, or successful model load alone.

## Hosted/Hybrid Escalation

- Preserve CPU, hosted/API, other local accelerator, and hybrid routing when the existing Rockchip NPU cannot support the required model/context/quality.
- Do not silently send sensitive local inputs to hosted fallback.
- Compare conversion/toolchain effort, board power, runtime maintenance, retries, correction time, and network dependence against hosted accepted-result economics.
- Keep board/accelerator purchasing outside this page.

## Canonical Links

- Link exact model facts to Model Reference and RKNN-Toolkit2/RKLLM software to canonical owners when materialized.
- Link `decision-guides/local-resource-fit/` for model-first selection.
- Link user scenarios when robotics/vision/home-lab/server/application requirements dominate hardware fit.
- Keep board-brand-specific documentation outside this model-selection route unless a real board-specific decision seam emerges.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party `airockchip/rknn-toolkit2` v2.3.2 and `airockchip/rknn-llm` v1.3.0 repositories, changelogs, demos, and multimodal conversion/deployment examples.
- Current evidence establishes separate RKNN and RKLLM conversion/runtime stacks, current supported platform families, current LLM/VLM family lists, target-specific `.rknn`/`.rkllm` artifacts, RK3588 multi-core configuration, multimodal split RKNN-vision/RKLLM-language pipelines, and version-specific quantization/context/runtime behavior. The former `rockchip-linux/rknn-toolkit2` repository is not current authority.
- RKNN/RKLLM toolkits/runtimes, supported SoCs/models/operators/precisions, RKNPU drivers, board BSPs, quantization, context behavior, and upstream examples are mutable; recheck them before rendering recommendations.
- Exact SoC/BSP/driver/toolkit/runtime/artifact/context/core configuration and measured accepted-result quality remain the fit authority.

## Validation

- Exact SoC/platform, BSP/kernel/RKNPU driver, toolkit/runtime, model artifact, context, quantization, and core configuration are pinned.
- Current `airockchip` repositories are used instead of the moved/unmaintained `rockchip-linux` toolkit source.
- RKNN conventional-model and RKLLM generative-model routes are not conflated.
- Source Hugging Face/ONNX weights are not treated as directly runnable NPU artifacts.
- Current RKLLM supported family names are not generalized to every checkpoint/size/revision.
- GGUF import/conversion support is not misrepresented as native llama.cpp runtime compatibility.
- VLM pipelines preserve separate RKNN vision and RKLLM language stages where required.
- Board RAM is not labeled NPU VRAM; multi-core NPU execution is not treated as linear throughput multiplication.
- Board/OEM BSP fragmentation, ARM64 dependencies, Linux/Android differences, host work, thermals, and concurrency are represented.
- TOPS, parameter count, artifact size, and load success do not replace practical-fit evidence.
- Hardware purchasing remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
