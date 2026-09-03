# Documentation Requirements

## Journey Purpose

- Present this journey for readers whose hardware is **already owned, fixed, deployed, or otherwise non-negotiable** and who need to determine which models/runtime routes are practical on it.
- Answer `Given this exact hardware, what can I run usefully?`, not `What hardware should I buy?`.
- Route first by hardware class: `mobile/`, `computers/`, `single-board/`, `embedded/`, `servers/`.
- Keep hardware procurement, product shopping, upgrade recommendations, and canonical hardware catalog ownership outside this journey.
- Preserve `decision-guides/local-resource-fit/` as the complementary **model-first** route for readers starting from a specific model/artifact and asking what resources it needs.

## First Decision: Hardware Class

- `mobile/` — phones/tablets where mobile OS policy, system models, app lifecycle, battery/thermals, and SoC-specific runtimes dominate.
- `computers/` — interactive laptops/desktops/workstations/mini PCs where user applications, display/desktop contention, OS, and the effective accelerator/runtime dominate.
- `single-board/` — Linux-capable SBC/developer boards where board/SoC/BSP/accelerator ecosystems such as Raspberry Pi/Hailo, Jetson, or Rockchip define distinct routes.
- `embedded/` — MCU/deeply constrained inference where firmware, SRAM/flash, operator conversion, real-time deadlines, and low-power execution dominate.
- `servers/` — dedicated CPU/accelerator serving hosts where topology, concurrency, KV cache, service SLOs, and sustained operations dominate.
- Do not use `edge`, `local`, `offline`, `ARM`, `NPU`, `GPU`, or `AI PC` as first-level hardware classes; they are contexts/attributes that cut across multiple classes.

## Practical Fit Definition

- Define practical fit as the intersection of:
  - exact hardware target and memory architecture;
  - exact OS/BSP/driver/firmware state;
  - supported runtime/backend and model artifact/export;
  - operator/model architecture support;
  - precision/quantization support and quality;
  - usable memory plus KV/cache/runtime/application headroom;
  - modality and complete pipeline requirements;
  - measured latency/throughput under the intended workload;
  - power/thermals and sustained behavior;
  - concurrency/topology where applicable;
  - accepted-result quality and failure severity.
- A route fits only when the complete required intersection is supported and measured strongly enough for the intended use.

## Evidence States

- Distinguish at minimum:
  - `official support` — current first-party support matrix/tool/runtime/model documentation;
  - `provider benchmark` — vendor/provider measurements under named conditions;
  - `independent measurement` — reproducible external measurement with sufficient configuration detail;
  - `AI Lab measurement` — measurement actually reproduced/owned by AI Lab;
  - `inference` — reasoned expectation not yet measured;
  - `Unknown` — unsupported, unverified, or insufficiently measured exact combination.
- Do not upgrade provider compatibility/benchmark evidence into independent AI Lab measurement.
- Keep `Unknown` explicit rather than filling gaps from adjacent hardware families.

## Exact Identity Before Recommendation

- Record the exact device/SoC/GPU/NPU/CPU/module/accelerator generation and variant.
- Record exact OS/build/BSP, driver/firmware, runtime/backend, model producer/revision, artifact/export, precision/quantization, tokenizer/adapters, and auxiliary encoders/decoders.
- Family or product branding alone is insufficient when variants have different accelerators/memory/runtime support.
- Keep mutable identity/version claims date-bounded and recheck before current recommendations.

## Do Not Use Nominal Metrics as Compatibility

- Successful model loading, conversion, compile, or one demo run does not establish practical fit.
- Published artifact file size does not equal peak working-set memory.
- Parameter count does not establish memory, latency, quality, or hardware support.
- Nominal RAM/VRAM/HBM capacity does not establish usable model memory.
- TOPS/GOPS/TFLOPS, accelerator branding, NPU presence, or benchmark marketing do not establish operator/model compatibility.
- Aggregate multi-device memory is not one usable pool without supported topology/sharding.

## Memory Model

- Distinguish dedicated accelerator memory, shared/unified system memory, accelerator-local memory, host RAM, MCU internal SRAM/TCM, external RAM/PSRAM, and storage/flash.
- Do not add unlike memory pools into one generic capacity figure.
- Include weights, KV/cache, runtime workspaces, attention/temp buffers, encoders/decoders, adapters, batch/concurrency, preprocessing/postprocessing, OS/firmware/applications, and fragmentation/headroom.
- Measure peak working set on the actual route.
- Treat swap/pagefile/storage-backed memory as a performance/reliability trade-off, not free capacity.

## Context and KV Cache

- Treat context/KV cache as part of practical memory and latency fit for generative models.
- Record configured context and representative p50/p95 input/output lengths rather than only the advertised model maximum.
- Include concurrency because per-session KV growth can dominate serving/mobile/local memory.
- Measure prompt/prefill and decode separately where applicable.
- If the hardware requires materially reducing context to remain usable, record `Fits conditionally` rather than full model capability.

## Model Artifact and Conversion

- Preserve source model/revision and the exact deployed runtime-native artifact.
- GGUF, MLX, TensorRT engines, OpenVINO IR, RKNN/RKLLM, HEF, QNN/compiled contexts, STM32/NXP/Espressif generated artifacts, and other formats are not interchangeable.
- Record conversion/compiler/tool versions, target, quantization/calibration, supported operators, and artifact provenance.
- A source PyTorch/ONNX/TFLite/Hugging Face checkpoint is not proof of deployability on a target accelerator.
- Keep conversion/operator failures visible.

## CPU / GPU / NPU / Accelerator Separation

- Record which compute unit executes each material stage.
- Do not infer that a platform NPU/GPU accelerates the intended model merely because the hardware includes one.
- Preserve CPU/GPU fallback/graph partitioning and include it in latency/power/memory measurements.
- Keep system-managed model APIs separate from custom app-owned model deployment where platforms abstract the accelerator.
- Unsupported accelerator paths remain `Unknown` even if CPU execution works.

## OS / BSP / Driver Boundary

- Treat OS, kernel/BSP, driver, firmware, package/runtime and platform API as part of the hardware target.
- Do not transfer Linux support to Windows/WSL/macOS/Android/iOS or vice versa without current evidence.
- For embedded/SBC/mobile platforms, firmware/OEM/BSP fragmentation can materially change operator/runtime availability.
- Recheck exact support matrix after upgrades.
- A neighboring device or OS version is not a compatibility guarantee.

## Workload and Modality

- Define the actual task before ranking model candidates: text generation, coding, embeddings/reranking, speech, vision/VLM, OCR, image/video generation, classification, sensor inference, agent/tool use, or another workload.
- Include all pipeline components, not only the headline model.
- Do not use text LLM performance to infer VLM/diffusion/speech/vision fit.
- Preserve modality-specific preprocessing, encoders, decoders, memory, and runtime support.

## Interactive vs Batch vs Real-Time

- Record the workload timing contract.
- Interactive user devices prioritize TTFT/responsiveness and coexistence with foreground applications.
- Servers can prioritize service p95/p99, throughput, concurrency, and availability.
- Embedded systems can require deterministic/worst-case real-time deadlines.
- Batch workflows may accept high single-request latency when throughput/economics are favorable.
- Do not apply one universal latency threshold across hardware classes.

## Concurrency and Topology

- Measure real concurrency where the intended workload serves multiple sessions/models/streams.
- For multi-device servers, record TP/PP/DP/EP/disaggregation and interconnect rather than aggregate memory.
- For multi-model personal/SBC workflows, include simultaneously resident embedding/reranker/guard/media components.
- For embedded vision/audio, include concurrent sensor/control pipelines.
- Do not infer linear scaling from device/core count.

## Power and Thermals

- Measure sustained workload behavior, not only burst performance.
- Mobile/laptops/SBC/embedded routes must include battery/power modes, cooling and throttling where material.
- Server routes should include power/thermal constraints when they affect sustained SLO/economics.
- A route that works only briefly before throttling is conditional fit.
- Preserve the tested power/cooling mode with benchmark evidence.

## Storage and Model Lifecycle

- Account for model artifacts, containers/runtimes, conversion outputs, caches, indexes, calibration/evaluation assets, current+rollback versions, firmware, and update headroom.
- Measure cold startup/model load where operationally relevant.
- Preserve artifact version/hash/provenance.
- Define rollback when runtime/model updates can invalidate compatibility.
- Avoid hidden downloads for offline-required routes.

## Offline / Data Boundary

- Distinguish local computation from truly network-independent operation.
- Verify model/package downloads, telemetry, license callbacks, hosted fallback, web/search/tools, remote embeddings/OCR, and external services.
- For offline/air-gapped use, pre-stage artifacts and test startup/steady-state with denied egress.
- Link full high-security/regulatory controls to the relevant user scenario rather than duplicating organization policy here.

## Agent / Tool Side Effects

- Hardware/model locality does not make agents safe.
- Keep tool permissions, allowlists, argument validation, authentication, confirmation gates, sandboxing, safety interlocks, and audit outside model-controlled text.
- Embedded/robotics/automation routes need deterministic physical safety controls.
- Treat retrieved/imported content as untrusted instructions.
- Hardware fit is separate from authorization/safety fit.

## Quality After Optimization

- Evaluate exact converted/quantized/compiled artifacts on representative tasks.
- Track accepted-result quality, retries, correction effort, refusals, structured/tool-call accuracy, perception metrics, or task-specific scores.
- A smaller or more quantized model can be the best fixed-hardware route if accepted results are faster/reliable enough.
- A faster artifact that misses quality thresholds does not fit.

## Total Cost per Accepted Result

- Compare local operation by power, storage, tuning/engineering, administration, idle capacity, retries, human correction/review, and incident burden where material.
- Existing hardware has sunk acquisition cost but can still have poor marginal latency/energy/operations economics.
- Hosted/rented/hybrid execution remains a valid outcome when local accepted-result economics are worse and the data boundary permits it.
- Do not turn this analysis into procurement advice.

## Practical Fit Outcomes

- `Fits well` — exact hardware/runtime/artifact/context/workload passes current support, resource headroom, latency/throughput/deadline, quality, and sustained-use thresholds.
- `Fits conditionally` — acceptable only with an explicit constraint such as reduced context/concurrency, particular quantization/runtime/OS, alternate compute path, limited duty cycle, or specific topology.
- `Does not fit` — exact route fails compatibility, resource, latency/throughput/deadline, quality, reliability, or operational thresholds.
- `Unknown` — exact combination lacks current official support or sufficient measurement.
- Never collapse `Unknown` into `Does not fit` or vice versa.

## Escalation

- When the fixed hardware cannot meet requirements, identify the **gap**: unsupported runtime/operator, insufficient memory/context, unacceptable latency, modality gap, power/thermal limit, quality failure, or topology/service issue.
- Escalate to another existing hardware class/pool, hosted API/service, rented accelerator, or hybrid execution as the user scenario permits.
- Do not recommend a product purchase from this journey.
- If the owner later asks what hardware to acquire, route to a separate procurement/buying decision surface.

## Baseline Measurement Contract

- Every practical model-fit measurement should record, as applicable:
  - exact hardware identity and memory architecture;
  - OS/BSP/driver/firmware;
  - runtime/backend/build/container;
  - model/revision/artifact/quantization;
  - context/input/output dimensions;
  - execution device/fallback/parallelism;
  - batch/concurrency/threading/topology;
  - power/cooling/application contention;
  - cold/warm state.
- Measure relevant peak memory, TTFT/prefill, decode/task latency, throughput/FPS, p50/p95/p99 or worst-case deadline, power/thermals, and accepted-result quality.
- Do not compare measurements whose material conditions differ without stating those differences.

## Research / Freshness Contract

- Recheck mutable driver/OS/toolkit/runtime versions, device/operator/model support, API availability, exports/quantizations, and platform packages before current recommendations.
- Prefer current first-party support matrices and tooling documentation for compatibility.
- Add independent measurements when they materially improve practical realism, but preserve their exact conditions.
- Unsupported or unmeasured claims remain `Unknown`.
- Current provider evidence is not automatically an AI Lab benchmark.

## Canonical Ownership

- Link concrete model identity/capability facts to Model Reference instead of copying full model cards here.
- Link runtime/software identities to their canonical owners when materialized.
- Keep hardware-specific decision requirements in this journey and user/workflow/privacy/economics requirements in user scenarios.
- Cross-navigation between hardware and scenarios is requirement-owned unless a genuinely factual stable entity relation is demonstrated.
- Do not create a hardware catalog here.

## Model-First Inverse Route

- Link `decision-guides/local-resource-fit/` when the reader begins with a specific model/artifact and asks whether/where it can run.
- The two journeys should converge on the same exact hardware/runtime/artifact measurement contract rather than duplicate conflicting compatibility claims.
- Device-first hardware pages own the platform/runtime boundaries; Model Reference owns model identity; decision guides synthesize from their own starting question.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after completing current-source depth passes across all selected mobile, computer, single-board, embedded, and server execution routes and reconciling their router contracts.
- The cross-hardware evidence supports a stable common rule: practical model fit is exact target + current runtime/artifact support + real resource/context headroom + measured workload performance + accepted quality, never nominal metrics alone.
- OS/BSP/drivers, runtimes/toolchains, accelerator/model support matrices, quantization/export formats, platform APIs, and model artifacts are mutable; recheck the selected child route before rendering recommendations.
- Exact hardware/runtime/artifact/workload measurement and accepted-result quality remain the final fit authority.

## Validation

- Exactly five first-level groups remain materialized: `mobile/`, `computers/`, `single-board/`, `embedded/`, `servers/`.
- `edge`, `local`, `cloud`, CPU ISA, and accelerator type do not become competing first-level hardware classes.
- Every materialized child route has a distinct runtime/compatibility decision seam and no empty placeholder is introduced.
- No page becomes a hardware catalog or buying guide.
- Runtime/platform support is not transferred between OS/device/vendor generations without evidence.
- Dedicated/shared/unified/local memory pools and multi-device capacity are not collapsed into simple sums.
- Load/compile success, parameter count, artifact size, RAM/VRAM/TOPS do not replace measured practical fit.
- Official support, provider/independent/AI Lab measurement, inference, and `Unknown` remain distinct evidence states.
- Model-first `local-resource-fit/` remains complementary rather than duplicated.
- Mutable current evidence carries the 2026-08-24 boundary.
