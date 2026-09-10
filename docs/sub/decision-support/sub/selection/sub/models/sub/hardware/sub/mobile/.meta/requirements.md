# Documentation Requirements

## Router Role

- Cover phones/tablets where mobile OS policy, device/SoC fragmentation, system AI models, app-owned custom models, process memory, battery/thermals, packaging/storage, offline state, and app lifecycle constrain local model selection.
- Route iPhone/iPad to `apple/` and Android to `android/`; do not classify laptops/desktops here merely because they use ARM SoCs.
- Keep this page focused on mobile constraints shared across platforms and delegate platform/runtime details to the children.
- Keep mobile-device purchasing outside this route.

## Exact Device Before Model

- Require exact device model/region, SoC, OS version/build, installed/available memory and storage, intended application route, network/offline requirements, and repeated-use workload before selecting a model.
- Do not infer mobile fit from SoC vendor/architecture alone.
- The same model family can behave differently across OS APIs, SoC backends, device cooling, app-memory limits, and model versions.
- Preserve `Unknown` when the exact device/runtime/model route is unsupported or unmeasured.

## Separate System and App-Owned Models

- Distinguish OS/system-managed foundation models from app-bundled/downloaded custom models.
- Current Apple and Android platforms both expose system-managed generative-model routes whose model distribution/update/availability are controlled by the OS/platform rather than the individual app.
- Custom models have separate conversion, packaging, storage, runtime/delegate, operator, licensing, and update obligations.
- Do not infer arbitrary custom-model accelerator access from consumer/system AI feature availability.
- Hosted/provider models remain a third distinct route.

## Mobile OS Is Part of the Runtime

- Treat iOS/iPadOS and Android process lifecycle, permissions, background execution, memory pressure, model distribution, and app-store/package rules as part of hardware fit.
- Do not transfer desktop runtime assumptions to mobile even when CPU/GPU architecture is related.
- Verify what can execute in foreground/background, how model assets are prepared/downloaded, and how the app behaves after suspension/termination.
- A persistent local service/agent that works on desktop may be invalid or unreliable on a mobile OS.

## App Memory vs Physical RAM

- Do not assign model tiers from nominal device RAM.
- Measure the app's peak working set including model/runtime, KV/cache, media inputs, compiled artifacts, UI, preprocessing/postprocessing, and concurrent system load.
- Account for OS low-memory termination/jetsam behavior and system-model memory that may be managed outside the app process.
- A model that technically fits total RAM but causes app termination or repeated model reload does not fit.

## Storage and Model Delivery

- Include model files, native runtime libraries, compiled contexts/caches, multiple revisions/quantizations/adapters, and temporary update storage.
- Separate OS-managed model assets from app-owned assets.
- Define initial download/on-demand/background asset behavior, offline readiness, integrity/versioning, cleanup, and rollback.
- Do not assume a system feature's compact app footprint means its underlying model is available to custom apps.

## Mobile Battery and Thermals

- Measure repeated/sustained use on the actual retail device rather than one cold-device benchmark.
- Record battery drain, thermal state/throttling, charge state, user-visible latency, and surface temperature/user comfort where material.
- Platform/SoC AI-efficiency claims and TOPS are candidate evidence only.
- A route that is fast for one request but degrades severely over a realistic session is conditional or non-fit according to the workload.

## Interaction Latency

- Measure time to first useful result and complete task latency including model/runtime initialization, context preparation, media preprocessing, inference, tools/retrieval, network when used, and rendering.
- For generative text, separate TTFT/prefill from sustained decode.
- For media, measure the full multi-stage pipeline.
- Do not promote accelerator subgraph timing to whole-app latency.

## Offline State

- Test airplane/no-network mode for every route described as local/offline.
- System models can require model/configuration preparation or downloads before offline inference is available.
- App-owned models must not unexpectedly depend on cloud model files, licenses, execution providers, or telemetry if offline use is required.
- Hosted/hybrid fallback must be explicit rather than silent.

## Local vs Hosted vs Hybrid

- Preserve three legitimate outcomes: local, hosted, and explicit hybrid.
- Use local when the exact supported mobile route meets quality, latency, privacy, offline, memory, and battery requirements.
- Use hosted when mobile model/context/modality/runtime limits make local execution unsuitable and the data/network boundary is acceptable.
- Use hybrid only with deterministic routing policy based on device/API availability, sensitivity, network state, workload size, quality, latency, and cost.
- Do not retry an unsuitable local route repeatedly before falling back to cloud.

## Mobile Multimodality

- Treat text, vision, speech/audio, image generation, and video as separate workload classes.
- Include camera/photo/microphone permissions and complete preprocessing/encoding/decoding pipelines.
- Prefer deterministic OCR/barcode/speech/vision APIs for exact structured tasks when they are more reliable than generative perception.
- Do not infer support for one modality from another platform AI feature.

## Compute Unit and Fallback

- CPU, GPU, NPU/Neural Engine/APU and heterogeneous execution are model/runtime specific.
- Record actual execution/partitioning for app-owned models where observable.
- System-managed model APIs can intentionally abstract hardware; do not reverse-engineer that abstraction into a claim of arbitrary NPU access.
- Include fallback and data-transfer overhead in end-to-end fit.

## Consumer Features vs Developer Contracts

- Do not use Apple Intelligence, Galaxy AI, Gemini features, OEM camera AI, or another consumer feature as proof that a developer can deploy arbitrary models on the same accelerator.
- Require current developer-facing API/runtime/toolchain evidence.
- Treat preview/OEM/private SDK access separately from public production third-party access.
- Mark inaccessible/undocumented developer routes `Unknown` rather than extrapolating from demos.

## Security and Agents

- Local processing can improve privacy but does not make model input or tool use trustworthy.
- Preserve OS permissions, app sandbox, secrets, network routing, tool allowlists, confirmation, and data minimization.
- Treat web/documents/images/messages/tool output as untrusted prompt-injection content for agentic apps.
- A locally running model does not authorize account/device/network actions.

## Evaluation and Change Management

- Maintain representative device/OS/model/runtime tests for availability, quality, memory, latency, battery/thermal, offline state, and lifecycle interruption.
- Re-run after OS, OEM firmware, system-model, runtime/delegate, compiled artifact, prompt/tool, or app changes.
- Record exact retail device/build because OTA/model updates can change behavior without hardware replacement.
- Include first-use and warm-state measurements where initialization/download/compilation is material.

## Practical Routing Outcomes

- `Fits well`: exact mobile device/OS/model route meets quality, app-memory, storage, latency, sustained battery/thermal, lifecycle, and offline/network requirements.
- `Fits conditionally`: depends on supported system API, particular custom delegate/artifact, reduced context/model, foreground-only use, limited repeated use, or explicit hosted fallback.
- `Does not fit`: exact route fails availability, compatibility, quality, memory, latency, thermals, lifecycle, modality, or data/network policy.
- `Unknown`: exact device/runtime/model behavior lacks current evidence.
- Never infer fit from installed RAM, accelerator TOPS, consumer-feature availability, or desktop support alone.

## Canonical Links

- Route platform-specific evidence to `apple/` or `android/`.
- Link exact model facts to Model Reference and platform runtimes/services to canonical software owners when materialized.
- Link user scenarios when application purpose/data requirements dominate hardware selection.
- Keep computer hardware selection under `computers/`.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** after the current Apple mobile and Android/Google/Qualcomm/MediaTek/Exynos child routes were independently re-evaluated against first-party platform/runtime evidence.
- Current evidence across both platforms supports a stable high-level distinction between OS-managed foundation models, app-owned custom models, hosted models, and explicit hybrid routing, while accelerator/delegate support remains device/platform specific.
- Mobile OS APIs, system models, delegates/runtimes, supported devices/features, firmware, quotas, app-lifecycle behavior, and hosted integrations are mutable; recheck children before rendering recommendations.
- Exact device/platform route and measured accepted-result behavior remain the fit authority.

## Validation

- Direct children remain only `apple/` and `android/`.
- Mobile support is not inferred from desktop or sibling-SoC support.
- System-managed/consumer AI capability is not treated as arbitrary custom-model accelerator support.
- App memory/lifecycle/storage/offline/battery/thermal constraints are first-class.
- Local, hosted, and hybrid routes remain legitimate outcomes.
- SoC/runtime-specific evidence stays in children rather than duplicated here.
- Hardware buying remains outside the router.
- Mutable current evidence carries the 2026-08-24 boundary.
