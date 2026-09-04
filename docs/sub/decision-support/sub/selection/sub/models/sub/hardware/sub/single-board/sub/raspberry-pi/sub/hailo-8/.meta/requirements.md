# Documentation Requirements

## Route Fit

- Cover Raspberry Pi 5 with Raspberry Pi AI HAT+ Hailo-8L (13 TOPS) or Hailo-8 (26 TOPS), including the legacy AI Kit Hailo-8L path where already owned.
- Require exact accelerator variant, Raspberry Pi 5/RAM/OS build, PCIe attachment, Raspberry Pi/Hailo software packages, HailoRT/firmware, HEF artifact, model/toolchain version, camera/media pipeline, host CPU/RAM load, cooling, and target throughput/latency before assigning fit.
- Keep Hailo-10H/AI HAT+ 2 generative AI in `hailo-10h/`; Hailo-8/8L does not inherit its LLM/VLM capability.
- Keep hardware purchasing outside this route.

## Hard Capability Boundary: Vision/Neural Inference, Not GenAI LLM/VLM

- Make the official Raspberry Pi 2026 capability split explicit.
- Current Raspberry Pi AI HAT documentation states AI HAT+ with Hailo-8L/Hailo-8 supports vision/neural workloads, while **LLM and VLM support are not supported** on AI HAT+ and are provided by Hailo-10H AI HAT+ 2.
- Do not infer LLM/VLM support from 13/26 TOPS, Hailo branding, or Hailo-10H examples.
- Route generative language/VLM workloads to CPU, Hailo-10H, another fixed platform, or hosted/hybrid execution.
- Keep any experimental non-official transformer component use clearly separate from supported Pi Hailo-8/8L GenAI capability.

## Exact Hardware Variant

- Distinguish Hailo-8L 13 TOPS and Hailo-8 26 TOPS.
- The discontinued Raspberry Pi AI Kit uses Hailo-8L and is functionally equivalent in accelerator capability to the Hailo-8L AI HAT+ route, but attachment/software details can differ.
- Record board/HAT/module identity and PCIe link state.
- Do not assign one model/FPS result to both 8L and 8 unless the artifact/runtime is built and measured for both.
- TOPS is only a device-level arithmetic capability label, not model compatibility or application FPS.

## Current Raspberry Pi OS and Package Boundary

- Current Raspberry Pi AI documentation requires Raspberry Pi 5 with 64-bit Raspberry Pi OS Trixie for the current supported Hailo setup.
- Current AI HAT+/AI Kit software uses the `hailo-all` package family; Hailo-10H AI HAT+ 2 uses `hailo-h10-all`.
- Raspberry Pi documentation states these Hailo-8/8L and Hailo-10 package sets cannot coexist.
- Treat OS/package changes as compatibility changes and record exact package versions.
- Do not transfer Bookworm-era or Hailo-10H installation steps into the current Hailo-8/8L route without version evidence.

## PCIe Attachment

- Current AI HAT+ integration handles the intended PCIe configuration automatically; the older AI Kit can require explicit Pi 5 PCIe Gen 3 configuration for full speed.
- Record negotiated PCIe generation/link width/status where throughput is unexpectedly low.
- Include PCIe host transfer in application latency for high-throughput/multi-stream pipelines.
- Do not assume raw NPU throughput is reachable through a misconfigured host link.
- Treat cable/connector/power/thermal hardware faults separately from model runtime failures.

## Hailo Software Stack Is Version-Coupled

- Pin HailoRT, firmware, driver/DKMS, Model Zoo, Dataflow Compiler, TAPPAS/hailo-apps/rpicam integration, and generated HEF versions where used.
- Raspberry Pi documentation explicitly warns that models generated with particular Hailo toolchain versions require compatible runtime/device-driver packages.
- Do not update one component independently and assume an old HEF remains compatible.
- Preserve a compatibility matrix or exact known-good toolchain tuple for production artifacts.
- `Works on my HailoRT` is version evidence, not a model-family guarantee.

## HEF Is the Deployable Artifact

- Treat source ONNX/TensorFlow/PyTorch weights as inputs to a compilation workflow, not as directly runnable Hailo-8 models.
- Preserve source model/revision, ONNX/TFLite export where used, Dataflow Compiler version, quantization/calibration, model-script configuration, target `hailo8` or `hailo8l`, and resulting HEF hash/version.
- Current Hailo model flow uses the Dataflow Compiler/Model Zoo to parse, optimize/quantize, and compile networks into Hailo Executable Format (HEF).
- Do not infer Hailo compatibility from successful ONNX export alone.
- Keep parse/unsupported-op/quantization/compile failures as explicit non-fit evidence.

## Compile Environment vs Raspberry Pi Runtime

- Treat model compilation and Pi deployment as separate machines/environments where the current toolchain requires it.
- Current Hailo guidance indicates Model Zoo/Dataflow Compiler workflows are typically hosted on supported x86 Ubuntu development environments while HailoRT executes HEF on the embedded target.
- Do not assume the full compiler/model-zoo stack should run on Raspberry Pi.
- Preserve compiler host OS/version/toolchain with the HEF provenance.
- Raspberry Pi only needs the runtime/deployment stack for already compiled supported artifacts.

## Model Zoo Is Eligibility Evidence

- Use Hailo Model Zoo/precompiled Hailo artifacts as strong candidate compatibility evidence for named network/task/accelerator versions.
- Do not assume a sibling architecture/version automatically compiles because another YOLO/model variant exists in the zoo.
- Record Model Zoo version and exact model configuration.
- Validate mAP/accuracy on the target dataset after quantization.
- Treat vendor Model Zoo throughput as accelerator/kernel evidence, not the expected end-to-end Raspberry Pi camera application FPS.

## Custom Model Workflow

- For custom/retrained models, preserve training/source model, export graph, calibration dataset, Dataflow Compiler/Model Zoo version, optimization scripts, postprocessing division, HEF, and target accelerator.
- Verify unsupported operators and whether postprocessing must remain on the Pi CPU.
- Measure quantized HEF quality against the source model.
- Do not let a compiled artifact with unacceptable accuracy count as fit.
- Recompile/revalidate after toolchain/runtime changes where required.

## Vision and Camera Integration

- Current Raspberry Pi `rpicam-apps` and Picamera2 integrate supported Hailo inference into camera pipelines.
- Record camera model, resolution/FPS, ISP/capture path, resize/color conversion, Hailo model input size, postprocessing, overlays/output, and simultaneous streams.
- Measure camera-to-result latency/FPS, not only `hailortcli` raw inference.
- Include dropped frames, host CPU load, memory, and storage/network output.
- A HEF that reaches high raw throughput can still fail the end-to-end camera deadline.

## Multiple Models and Streams

- Hailo-8 can support larger/parallel vision workloads than Hailo-8L, but exact multi-network scheduling is model/runtime specific.
- Measure concurrent HEFs/streams on the actual Pi 5 pipeline.
- Include PCIe, CPU postprocessing, memory, camera, and display/network contention.
- Do not sum standalone model FPS as a concurrency guarantee.
- Record p50/p95 latency as well as average FPS for real-time systems.

## Host RAM and CPU Still Matter

- AI HAT+ Hailo-8/8L does not provide the Hailo-10H AI HAT+ 2 dedicated 8 GB GenAI memory pool.
- The Raspberry Pi host still owns application state, camera buffers, pre/postprocessing, networking, storage, UI, and any CPU models.
- Measure whole-system RAM and CPU under the complete pipeline.
- Do not call NPU offload a zero-host-cost operation.
- Keep CPU saturation/postprocessing bottlenecks visible.

## NPU Memory/Topology Is Not Pi RAM

- Do not describe Pi RAM as Hailo NPU model memory or infer HEF compatibility from Pi RAM size.
- Hailo compilation/scheduling determines whether a graph maps to the accelerator.
- More Pi RAM can help host workloads but does not make an unsupported Hailo graph executable.
- Keep model compile capacity and host memory as separate constraints.

## Prompt/Language Work Remains CPU or Another Route

- If a Raspberry Pi application includes language reasoning alongside Hailo vision, route the LLM to Pi CPU, Hailo-10H, hosted, or another model server explicitly.
- Treat the pipeline as multi-model/hybrid and measure host/network handoff.
- Do not imply the Hailo-8 vision accelerator runs the language model.
- Preserve privacy/offline boundary for whichever route owns language generation.

## Speech and Non-Vision Neural Models

- Hailo-8/8L can support some non-vision neural workloads only when the exact network compiles/runs through the current Hailo toolchain.
- Do not infer support from task name (speech, embeddings, audio) or parameter count.
- Require exact HEF/toolchain/runtime evidence and complete pipeline measurement.
- Distinguish supported neural inference from the absent official LLM/VLM GenAI route.

## Raw NPU Benchmark vs Application Benchmark

- Measure at least two layers when useful:
  - raw HEF runtime latency/throughput via HailoRT tooling;
  - end-to-end Pi application/camera latency/throughput.
- Preserve batch/input/stream count and power/thermal conditions.
- Do not quote Model Zoo/raw-chip FPS as expected Pi application FPS.
- Use the gap to identify CPU/preprocessing/postprocessing/PCIe/camera bottlenecks.

## Raspberry Pi Thermals and Power

- Hailo offload reduces host compute for supported neural work but the Pi 5 and accelerator still require stable power/cooling.
- Use current Raspberry Pi cooling/power guidance and measure sustained host temperature/throttling.
- Record AI HAT accelerator temperature/thermal guidance when exposed by the current hardware/runtime.
- Include camera, USB/SSD, HAT, and other peripheral power draw.
- A short demo run is not proof of 24/7 edge reliability.

## Storage and Offline Deployment

- Prestage HEFs/models/runtime packages for offline deployments.
- Preserve versions/hashes of deployed HEFs and configuration/postprocess files.
- Define update/rollback when HailoRT/firmware/model versions change.
- Keep logs/datasets/camera recordings from filling constrained Pi storage.
- Do not rely on model-hub/cloud download at runtime if offline operation is a requirement.

## Security and Agentic Actions

- Treat camera frames, OCR/text in scenes, network messages, and model outputs as untrusted inputs when the pipeline can trigger automation.
- Hailo detection/classification output should not directly bypass deterministic safety/access/actuation controls.
- Validate thresholds/labels and use explicit action policy.
- A local edge NPU improves data locality but does not make the control system safe by default.

## Quality Evaluation

- Measure class-level detection/segmentation/pose/etc. metrics appropriate to the actual application dataset after Hailo quantization/compilation.
- Include hard lighting, motion, camera, occlusion, false-positive/false-negative cases.
- Track postprocessing/version changes.
- Provider example model success does not establish target-domain quality.

## Practical Fit Outcomes

- `Fits well`: exact Pi 5/Hailo-8 or 8L/OS/runtime/HEF/pipeline passes supported-model compilation, quality, end-to-end latency/throughput, host headroom, power, and sustained thermal thresholds.
- `Fits conditionally`: requires a specific toolchain/runtime tuple, smaller supported model/input, reduced streams, CPU postprocessing, active cooling, or another explicit acceptable constraint.
- `Does not fit`: exact route fails compile/operator support, quality, latency/FPS, host resources, thermal/power, or runtime compatibility.
- `Unknown`: exact source model/toolchain/HEF/runtime/pipeline is unsupported or unmeasured.
- LLM/VLM requests are `Does not fit` for the current supported Hailo-8/8L AI HAT+ route, not inferred from TOPS.

## Escalation

- Route GenAI LLM/VLM acceleration to `hailo-10h/`, CPU, another fixed platform, or hosted/hybrid execution.
- Route CPU-only tasks to `cpu/`.
- Do not recommend buying a different accelerator from this page; expose the capability gap only.

## Canonical Links

- Link exact model facts to Model Reference and HailoRT/Model Zoo/Dataflow Compiler/rpicam software to canonical owners when materialized.
- Link Raspberry Pi parent/router and `hailo-10h/` sibling for capability separation.
- Link vision/physical-AI user scenarios when application requirements dominate hardware fit.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Raspberry Pi AI software/AI HAT/AI Kit documentation and current Hailo software/model-zoo/toolchain guidance.
- Current Raspberry Pi evidence explicitly separates Hailo-8L/Hailo-8 AI HAT+ vision/neural workloads from Hailo-10H AI HAT+ 2 LLM/VLM GenAI, uses current 64-bit Raspberry Pi OS Trixie and `hailo-all`, and warns about Hailo software/toolchain version compatibility.
- HailoRT/firmware/driver, Dataflow Compiler/Model Zoo/TAPPAS, HEF format/operator support, Raspberry Pi OS packages, camera integration, and example models are mutable; recheck them before rendering recommendations.
- Exact accelerator/runtime/HEF/end-to-end Pi pipeline measurement and accepted-result quality remain the fit authority.

## Validation

- Hailo-8/8L and Hailo-10H capabilities are not conflated.
- Current official Hailo-8/8L AI HAT+ route is not presented as LLM/VLM capable.
- Exact Hailo-8L vs Hailo-8 variant, Pi OS/package, HailoRT/firmware, compiler/model-zoo version, and HEF are pinned.
- Source weights are not treated as directly runnable NPU artifacts.
- Model Zoo/raw Hailo throughput is not presented as end-to-end Pi application FPS.
- Host CPU/RAM/camera/postprocessing/PCIe/power/thermal work remains part of fit.
- TOPS and Pi RAM do not replace graph/operator/toolchain compatibility evidence.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
