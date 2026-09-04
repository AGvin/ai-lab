# Documentation Requirements

## Router Role

- Present Android as a **routing layer**, not one homogeneous accelerator/model target.
- Start from the exact device/SoC, Android build, application AI route, model ownership, data/network boundary, and workload before selecting a child hardware path.
- Route custom accelerator-specific evidence to the SoC children:
  - `google/` for Google Tensor/Pixel-specific AICore/custom evidence;
  - `qualcomm/` for Snapdragon Android QAIRT/QNN/LiteRT-delegate evidence;
  - `mediatek/` for Dimensity/NeuroPilot evidence;
  - `samsung/` for actual Exynos hardware/Exynos AI Studio evidence.
- Do not infer the SoC from phone brand alone; some OEM/product families ship different SoCs by device/region.
- Keep device purchasing outside this route.

## Choose the AI Product Route Before the Accelerator

- Distinguish three primary Android application routes:
  - system-managed on-device generative AI through Gemini Nano/AICore/ML Kit GenAI;
  - app-owned custom on-device models through LiteRT, MediaPipe/ML Kit/custom frameworks, or vendor-specific runtimes/delegates;
  - cloud/hosted AI.
- Keep hybrid routing as an explicit combination of those routes rather than hidden fallback.
- The system-managed route abstracts hardware acceleration away from the app; the custom route requires explicit model/runtime/delegate compatibility.
- Do not interpret system Gemini Nano availability as proof that arbitrary app-owned models can access the same NPU/backend.

## Current Android Platform Guidance

- Current Android developer guidance explicitly separates on-device Gemini Nano, custom models, cloud AI, and system-level app integration.
- Current platform guidance recommends ML Kit GenAI APIs over AICore/Gemini Nano for supported production generative tasks and LiteRT for specialized app-owned custom models.
- Treat exact APIs, supported devices, feature limits, models, and delegates as mutable.
- Use the selected child route for vendor/SoC-specific runtime evidence rather than copying vendor support matrices here.

## System Gemini Nano / AICore Route

- Treat Gemini Nano as an Android OS-managed foundation-model route through AICore, not as a downloadable app-owned checkpoint.
- Current Android documentation states that AICore manages model distribution/updates, safety, and hardware acceleration and that supported prompts are processed locally.
- The app should rely on runtime feature/status APIs rather than a static assumption that an Android version or NPU means Gemini Nano is available.
- Different devices can expose different Gemini Nano versions/features; preserve the actual model/device evidence when behavior matters.
- Route Pixel/Tensor-specific AICore behavior to `google/`; do not duplicate it for other SoCs without exact support evidence.

## AICore Hardware Abstraction Is Not Custom-NPU Evidence

- AICore may choose and use appropriate device accelerators without exposing a generic custom-model NPU programming contract.
- Do not infer NPU operator coverage, memory, quantization, or custom deployment capability from a successful AICore call.
- If the objective is to deploy a known app-owned model, use the custom-model route and exact SoC/vendor evidence.
- If the objective is a supported high-level GenAI task, system Nano can remain the lower-administration route when device/API constraints are acceptable.

## Custom Model Route With LiteRT

- Treat LiteRT as Android's current official custom-ML inference runtime route, with Google Play services delivery options and hardware delegates.
- Current Android documentation describes GPU/NPU hardware acceleration through delegates and an Acceleration Service that can select a suitable configuration at runtime.
- Require exact model artifact, LiteRT version, delegate, SoC/device, supported operators, quantization, memory, and measured quality/latency.
- Do not write `LiteRT uses NPU` without identifying the delegate/provider and actual graph delegation.
- Delegate availability/performance is device and vendor specific; route to the corresponding SoC child.

## Vendor Delegates and Runtimes

- Qualcomm, MediaTek, Samsung/Exynos, and Google Tensor expose materially different developer/runtime boundaries.
- Do not transfer one vendor's delegate, compiled model, NPU operator matrix, profiling result, or deployment model to another SoC.
- Preserve developer-access restrictions: a vendor/OEM-only SDK route is not a standard third-party Android app route.
- When a vendor runtime is unavailable to the target developer/device, select a standard Android runtime, CPU/GPU fallback, system model, hosted route, or `Unknown` rather than inventing NPU support.

## CPU/GPU/NPU Placement

- Record actual execution device(s) for custom models.
- Treat partial delegation, CPU fallback, GPU fallback, and heterogeneous partitioning as normal evidence rather than hidden implementation detail.
- Measure complete end-to-end latency including preprocessing/postprocessing and transfers.
- NPU presence or SoC TOPS does not prove a custom graph will execute there.
- Keep unmeasured placement `Unknown`.

## Android Device Fragmentation

- Require exact retail device, SoC, Android build, OEM firmware, memory configuration, runtime/delegate versions, and app ABI.
- The same SoC family can appear under different thermal/power/driver policies and different OEM devices.
- Re-test after major Android/OEM firmware/vendor-runtime updates.
- Do not transfer a reference-device benchmark to another retail device solely because the SoC name matches.

## App Memory and Process Lifecycle

- Treat app/process memory and Android low-memory/termination behavior as first-class constraints.
- Include model weights/artifacts, compiled caches, KV/cache, tensors, media inputs, UI state, runtime buffers, and concurrent system/app load.
- Do not create universal installed-RAM-to-model-size tiers.
- Handle activity/process suspension, termination, model reinitialization, and long-running jobs safely.
- A route that works only in a clean benchmark but is repeatedly killed or reloaded under normal use does not fit.

## Storage and Model Distribution

- System AICore manages its own system-model distribution; app-owned models have separate bundle/download/storage/update responsibilities.
- Include APK/AAB impact, native libraries, model files, compiled contexts/caches, downloadable assets, multiple model revisions, and temporary update storage.
- Define offline availability, integrity/hash/versioning, cleanup, and rollback for app-owned models.
- Do not conflate AICore model updates with app-owned model lifecycle.

## Offline and Network Boundary

- System Gemini Nano can support local/offline inference after the required system assets/configuration are available, but first-use/model-update preparation can require network access.
- App-owned local models must be tested with network denied if offline behavior is claimed.
- Hosted routes require connectivity and a separate provider/data boundary.
- Hybrid routing must explicitly define when data leaves the device; do not silently fall back from a local route to cloud for sensitive inputs.

## Battery and Thermals

- Measure sustained repeated inference on the actual device, not only one cold-device request.
- Record battery drain, thermal state/throttling, charge state, and user-visible latency.
- NPU/edge-AI efficiency marketing is not application-level power evidence.
- Compare local, custom, and hosted/hybrid routes by accepted-result latency/quality/privacy and mobile energy/user experience.

## Prompt, Decode, and Pipeline Measurement

- For generative models, record TTFT, prompt/prefill latency, context length, KV/cache memory, sustained decode/task latency, and output length.
- For vision/media/speech, include all preprocessing, encoders/decoders, iterative diffusion/video stages, and postprocessing.
- Do not report a single delegate/NPU subgraph timing as whole-application latency.
- Measure cold/warm initialization separately where model/delegate compilation or cache is material.

## Model and Task Quality

- A compatible device/runtime does not prove the model is adequate for the task.
- Evaluate the exact deployed model/export/quantization on representative inputs.
- Compare system Nano, custom local, and approved cloud alternatives when each is technically available.
- Track retry/correction burden along with latency/battery.
- Preserve `Unknown` where exact device/model/delegate evidence is absent.

## Android Generative AI Limits

- Treat ML Kit GenAI task limits, model/device availability, quotas, foreground/background restrictions, and supported modalities/languages as exact API properties.
- Do not assign cloud Gemini context/capability to Gemini Nano.
- Do not assign one device's Nano version/feature support to all Android phones.
- Use custom or hosted routes when task/context/modality requirements exceed the supported system-model surface.

## Hybrid Inference

- Current Android guidance explicitly supports hybrid on-device/cloud design to balance reach, offline capability, cost, and model capability.
- Define deterministic routing criteria: device/API availability, data sensitivity, network state, task size/context, quality requirement, latency, and cost.
- Avoid route oscillation or repeated failed local attempts before cloud fallback.
- Preserve user/admin policy for sensitive data and offline-only modes.

## AppFunctions / System-Agent Integration

- Keep `model running in the app` separate from `system AI invoking app functionality`.
- Current Android guidance uses AppFunctions to expose app capabilities to system-level assistants; this is an agent/action integration route, not evidence that the app's custom model runs on a local accelerator.
- Treat exposed app actions as side-effecting tools with normal Android permission/confirmation/data boundaries.
- Do not fold AppFunctions into custom-model hardware fit.

## Security and Prompt Injection

- On-device inference does not make tool-capable apps/agents safe.
- Treat web pages, documents, images, emails, QR codes, and tool output as untrusted instructions.
- Keep Android permissions, tool allowlists, provider routing, secrets, and confirmation outside model-controlled content.
- Verify sensitive fallback/data export explicitly.

## Practical Routing Outcomes

- `System model`: supported AICore/ML Kit GenAI task meets device/API/quality/limit/lifecycle/privacy requirements.
- `Custom local`: exact model + LiteRT/vendor runtime/delegate meets device/operator/memory/quality/latency/power requirements.
- `Hosted`: local routes cannot meet capability/reach/context/quality needs and provider/network/data boundary is acceptable.
- `Hybrid`: explicit policy routes workloads between approved local and hosted paths.
- `Unknown`: exact device/SoC/runtime/model/delegate behavior is not currently supported or measured.
- Never choose a route from NPU TOPS or Android version alone.

## Canonical Links

- Route exact SoC custom-model evidence to `google/`, `qualcomm/`, `mediatek/`, or `samsung/`.
- Link system Gemini Nano/AICore and LiteRT software behavior to their canonical software/service owners when materialized.
- Link exact model facts to Model Reference.
- Link user scenarios when task/data/privacy requirements dominate hardware selection.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Android Developers AI solution guidance, current Gemini Nano/AICore documentation, current LiteRT Android/hardware-acceleration guidance, and current hybrid-inference/AppFunctions platform guidance, plus the separately re-evaluated 2026 Google Tensor, Qualcomm, MediaTek, and Exynos child routes.
- Current Android evidence explicitly distinguishes system on-device Gemini Nano, custom LiteRT models, cloud AI, hybrid routing, and system-agent AppFunctions. Hardware/delegate support for custom models remains device/vendor specific.
- Android/AICore/Nano/ML Kit/LiteRT versions, delegates, Acceleration Service behavior, OEM firmware, supported devices/features, and cloud/system-agent integrations are mutable; recheck them before rendering recommendations.
- Exact device/SoC/application route and measured accepted-result behavior remain the routing authority.

## Validation

- Android is a router rather than one accelerator target.
- System AICore/Gemini Nano, custom LiteRT/vendor runtime, hosted, hybrid, and system-agent integration remain distinct.
- System-model accelerator abstraction is not used as proof of arbitrary custom NPU access.
- SoC-specific custom support belongs to the four child routes and is not generalized across vendors.
- Device/firmware/runtime fragmentation, app memory/lifecycle, storage, offline state, battery/thermals, fallback, and complete-pipeline quality are represented.
- NPU TOPS, installed RAM, Android version, or consumer AI features do not replace exact runtime/model evidence.
- Hardware buying remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
