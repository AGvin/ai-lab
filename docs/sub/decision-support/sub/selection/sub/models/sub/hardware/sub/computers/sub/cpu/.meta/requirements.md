# Documentation Requirements

## Route Fit

- Cover general-purpose computers where no useful supported GPU/NPU accelerator is intended for the target model/workload and CPU inference is the primary local route.
- Require exact CPU architecture/microarchitecture, instruction-set support, physical cores/threads, memory channels/capacity/bandwidth, OS, runtime/backend/build flags, model artifact/quantization, context/KV cache, concurrency, and target latency before assigning fit.
- Do not route a machine here merely because it has a CPU; if an NVIDIA/AMD/Intel/Qualcomm/Apple accelerator is the intended inference path, use that route.
- Keep CPU/PC purchasing outside this page. The reader starts from owned/fixed compute.

## Mature CPU Runtime First

- Prefer a runtime with mature kernels for the exact CPU ISA and model artifact rather than a generic framework path chosen by habit.
- Current `llama.cpp` provides current x86 AVX/AVX2/AVX512/AMX and ARM NEON support, broad GGUF quantization, CPU feature coverage, and local server/CLI use.
- Other runtimes such as OpenVINO/ONNX Runtime/optimized BLAS or model-specific engines can outperform `llama.cpp` on particular CPUs/models; evaluate the exact route rather than preserving one permanent default.
- Record exact runtime commit/release and compiled CPU features because binary packages can target different instruction sets.
- Do not assume a binary that runs is using the best kernels available for the processor.

## CPU ISA and Build Compatibility

- Identify x86-64, ARM64, or another architecture and the available SIMD/matrix instructions.
- Current `llama.cpp` explicitly documents x86 AVX/AVX2/AVX512/AMX and ARM NEON support; current feature support differs by CPU backend and quantization.
- Verify that the runtime binary was built for instructions actually present on the CPU.
- Do not use a newer-ISA optimized binary on older hardware unless dispatch/fallback is documented.
- Compare generic versus optimized builds if CPU kernels materially change performance.

## Core and Thread Topology

- Record physical cores, SMT/hyper-threading, heterogeneous performance/efficiency cores where applicable, sockets, NUMA nodes, and OS scheduler behavior when material.
- Do not assume maximum logical-thread count is the fastest setting.
- Current `llama.cpp` performance guidance explicitly warns that excessive thread count can oversaturate CPUs and degrade token generation; tune threads empirically around physical core/topology behavior.
- Measure prompt-processing and decode thread settings independently when the runtime supports separate controls.
- Preserve the chosen thread configuration with benchmark evidence.

## Memory Capacity Is Not a Model Tier

- Use RAM capacity only as one feasibility constraint.
- Include model weights, mmap/page cache behavior, KV/cache, runtime/temp buffers, embeddings/vision/audio components, concurrent sessions, OS, applications, and filesystem cache in peak memory evidence.
- Do not publish universal rules such as `16 GB → 7B`, `32 GB → 14B`, or similar model tiers.
- A quantized model can fit in RAM and still be unusably slow because memory bandwidth or compute is the bottleneck.
- Heavy swapping/pagefile pressure is a practical fit failure for interactive use unless the workflow explicitly tolerates it.

## Memory Bandwidth and Locality

- Treat sustained memory bandwidth/cache behavior as first-class CPU inference constraints, especially for quantized autoregressive decode.
- Record memory channels/speed/topology where available and compare realistic measured throughput rather than DIMM capacity alone.
- On multi-socket/NUMA workstations, bind threads/memory according to runtime guidance and measure cross-node penalties.
- Do not add RAM bandwidth from multiple sockets/channels without understanding NUMA placement and model allocation.
- Use runtime/OS counters or controlled benchmarks to distinguish compute versus bandwidth bottlenecks where useful.

## Model Artifact and Quantization

- Record exact producer/model/revision, GGUF or other runtime artifact, quantization, tokenizer, adapters, and auxiliary components.
- Current `llama.cpp` supports a wide range of integer quantizations and documents that some quantization families are slower on particular CPU feature paths.
- Do not choose the lowest-bit artifact solely for RAM fit; compare quality and kernel performance.
- Preserve conversion/quantization tool/version and source model provenance for locally produced artifacts.
- Treat quantization quality loss as part of accepted-result fit.

## Prompt vs Decode

- Measure prompt ingestion/prefill separately from token generation/decode.
- CPU configurations can show very different bottlenecks for matrix-heavy prompt processing versus memory-bound autoregressive decode.
- Record time to first token, prompt tokens/s at representative context, and sustained decode tokens/s or task latency.
- Do not report one tokens/s number without defining which phase it measures.
- Use realistic input/output lengths rather than tiny synthetic prompts as the only evidence.

## Context and KV Cache

- Include context/KV cache memory and compute cost in every LLM fit result.
- Test the context lengths the user actually needs.
- Use KV-cache quantization only after measuring memory/quality/latency effects for the exact runtime/model.
- If the model is usable only at substantially reduced context, record that as a conditional fit.
- Do not present advertised model maximum context when local CPU latency/memory makes it impractical.

## Cold Load and Storage Effects

- Measure cold model load and warm/repeated-run behavior separately.
- Memory-mapped models can rely heavily on OS page cache; a warm run can hide storage/load costs.
- Record SSD/HDD/storage path where model startup materially affects workflow.
- Do not treat a fully cached benchmark as representative of an infrequently launched local assistant without labeling it.
- Include model disk footprint and duplicate quantization/artifact storage in operational fit where relevant.

## Interactive Latency Threshold

- Define what `usable` means for the intended workflow: interactive chat, IDE assistance, batch summarization, overnight processing, classification, or another target.
- A model generating 1–2 tokens/s may be acceptable for unattended batch work but poor for an interactive coding assistant.
- Record TTFT and end-to-end task completion alongside throughput.
- Compare against the user's tolerance and alternative hosted route rather than applying one global minimum.

## Concurrency

- Measure single-session and intended concurrent-session performance.
- Multiple sessions can multiply KV/cache memory and contend for cores/bandwidth.
- Test server batching/parallel request settings where the runtime supports them.
- Record p50/p95 latency under realistic concurrency instead of extrapolating from one user.
- A CPU model that is acceptable for one user can fail quickly as a shared service; route shared infrastructure to server/platform owners when that becomes primary.

## Background Application Contention

- Test with the computer's normal applications: IDE, browser, office tools, local databases, Docker/VMs, builds, media software, or other heavy CPU/RAM users.
- Record responsiveness impact on the primary workstation workload.
- Avoid pinning all cores to inference if it makes the machine unusable for its actual purpose.
- For background assistants, measure a constrained thread/power configuration as well as maximum throughput.

## Heterogeneous CPU Cores

- On hybrid performance/efficiency-core CPUs, verify scheduler/thread affinity behavior if it changes latency or efficiency.
- Do not assume all logical cores deliver equal inference performance.
- Benchmark sensible affinity/thread configurations and preserve the OS power mode.
- A configuration optimized for throughput may be worse for foreground responsiveness or battery life.

## Power and Thermals

- Measure sustained package power, clocks, temperature, fan/noise, and throttling on laptops/mini PCs where long inference matters.
- Test intended AC/battery/performance modes.
- Do not use a short benchmark that ends before the cooling system reaches steady state.
- Track energy/time per accepted task when local power economics matter.

## Multimodal and Media Workloads

- Treat VLM, speech, embedding, image generation, and video as separate pipelines from text LLM decode.
- Include image/audio encoders, preprocessors, VAE/decoder/diffusion steps, resampling, and postprocessing.
- CPU-only media generation can be technically supported but operationally poor; measure complete accepted workflow latency.
- Do not infer multimodal fit from text-only LLM RAM capacity.
- Preserve hosted/hybrid escalation where one specialist stage dominates CPU time.

## Mixture-of-Experts and Specialized Architectures

- Evaluate MoE/sparse architectures on actual CPU/runtime behavior rather than parameter count alone.
- Current `llama.cpp` CPU feature matrix includes MoE support, but active-parameter count does not directly determine RAM bandwidth, total model storage, routing overhead, or quality.
- Measure prompt/decode and peak memory for the exact artifact.
- Do not use `active parameters` as a shortcut for dense-model equivalence.

## CPU+GPU Hybrid Is Another Route

- If a supported accelerator is intentionally used for layer offload, the route is no longer pure CPU fit and should be evaluated under the corresponding accelerator/hybrid hardware route.
- Current `llama.cpp` supports CPU+GPU hybrid inference, but offload performance depends on GPU support, PCIe, host CPU/RAM, layer placement, and context.
- Do not use partial offload to hide that the CPU-only route fails the latency threshold.
- Preserve CPU-only baseline and hybrid result separately.

## Benchmark Method

- Use a reproducible benchmark command/configuration and record:
  - CPU model/topology;
  - RAM configuration;
  - OS/power mode;
  - runtime build and CPU features;
  - model artifact/quantization;
  - context/input/output;
  - threads/affinity;
  - batch/concurrency;
  - cold/warm state.
- Measure load, prompt, decode/task latency, peak RAM, CPU utilization, power/thermals where relevant, and accepted-result quality.
- Repeat enough times to distinguish stable performance from one warm-cache outlier.

## Quality and Accepted Result

- Compare compact/quantized CPU candidates against an accepted stronger reference on representative tasks.
- Track retries and human correction time.
- A smaller model can be the best CPU choice even if it is less capable in isolation when it produces accepted results much faster.
- A larger model that requires minutes of waiting and repeated correction can have worse accepted-result economics despite higher benchmark scores.
- Do not optimize tokens/s independently of quality.

## Practical Fit Outcomes

- `Fits well`: exact CPU/runtime/artifact/context/workload passes quality, memory, latency, concurrency, and sustained-system-impact thresholds.
- `Fits conditionally`: acceptable only for batch work, reduced context, smaller quantization/model, limited threads/concurrency, or another explicit constraint.
- `Does not fit`: exact route fails memory, latency, quality, stability, thermals, or system-responsiveness thresholds.
- `Unknown`: exact CPU/runtime/artifact combination lacks current support or measurement.
- Do not assign fit from RAM capacity, parameter count, or nominal core count alone.

## Hosted/Hybrid Escalation

- Preserve hosted/API/hybrid routing when CPU-local accepted-result latency/quality is poor.
- Compare token/API spend with local wait time, power, system contention, retries, and human correction.
- Local CPU can remain useful for privacy-sensitive snippets, classification, embeddings, preprocessing, or offline fallback even when a larger hosted model owns difficult work.
- Do not recommend a new GPU/PC from this page; expose the measured gap.

## Canonical Links

- Link model facts to Model Reference and runtime/software facts to canonical owners.
- Link `decision-guides/local-resource-fit/` when starting from a model artifact.
- Route supported intended GPU/NPU use to Apple/NVIDIA/AMD/Intel/Qualcomm computer routes.
- Link user scenarios when workflow/data requirements rather than CPU fit become primary.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current `llama.cpp` project/feature-matrix/performance guidance for x86 AVX/AVX2/AVX512/AMX, ARM NEON, broad GGUF quantization, CPU features, KV-cache quantization, and thread tuning.
- Current evidence confirms mature CPU inference and quantization across multiple CPU ISA paths while also showing that quantization families and thread counts can materially affect performance. It does not establish a universal RAM-to-model-size rule or expected speed for a specific CPU.
- `llama.cpp`, OpenVINO/ONNX/BLAS backends, model support, quantization kernels, ISA optimizations, and OS scheduling behavior are mutable; recheck them before rendering recommendations.
- Exact CPU/runtime/artifact/context/concurrency measurement and accepted-result quality remain the fit authority.

## Validation

- CPU route is used only when no relevant supported accelerator route is intended.
- CPU ISA/build flags, physical topology, threads, memory capacity, and bandwidth are explicit.
- RAM capacity does not become a universal model-size tier.
- Maximum logical threads are not assumed optimal.
- Prompt processing and decode are measured separately.
- Cold/warm model loading and realistic background contention are represented.
- Quantization is evaluated for both kernel performance and accepted-result quality.
- Media/multimodal fit is not inferred from text LLM behavior.
- Hosted fallback remains a legitimate outcome.
- Buying advice remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
