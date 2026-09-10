# Documentation Requirements

## Route Fit

- Cover iPhone/iPad-class Apple devices where exact device/OS eligibility, app memory, battery/thermals, local model APIs, packaging/storage, and mobile interaction latency constrain model selection.
- Require exact iPhone/iPad model/SoC, iOS/iPadOS version, available system-model APIs, chosen local/custom/cloud model route, context/modalities, app deployment method, storage, and real app memory budget before assigning fit.
- Keep Apple-Silicon Mac execution in `hardware/computers/apple/`; mobile OS/process constraints materially differ.
- Keep device purchasing outside this route.

## Current Apple Mobile Routes

- Separate at least:
  - Apple `SystemLanguageModel` / Foundation Models framework using the system-provided Apple Foundation Model;
  - Apple Foundation Models using Private Cloud Compute/server model routes where supported;
  - app-bundled/custom on-device models through current Core AI/Core ML paths;
  - third-party/on-device runtimes where independently supported;
  - ordinary hosted model APIs.
- Do not use `Apple Intelligence` as one model identity or one execution location.
- Current Foundation Models framework now exposes a common `LanguageModel` protocol for Apple on-device/server models and compatible local/server providers; preserve the actual model/provider behind that API.

## SystemLanguageModel Is OS-Managed

- Treat `SystemLanguageModel` as an OS-provided model whose identity/behavior can change with OS updates.
- Current Apple documentation states that the on-device system model has distinct versions aligned to OS releases and explicitly tells developers to re-test prompts when the model changes in iOS/iPadOS updates.
- Record OS version and system-model version/evidence date for behavioral claims.
- Do not pin a long-lived application guarantee to an undocumented internal model name/parameter count.
- Preserve fallback/error behavior for devices or configurations where the system model is unavailable.

## iOS 26 vs iOS 27 Boundary

- Keep OS-generation changes explicit.
- Current 2026 Foundation Models updates add iOS/iPadOS 27-era multimodal prompts, dynamic profiles, common `LanguageModel` protocol use, and new on-device/system-model behavior.
- Do not transfer an iOS 27 API/model capability to iOS 26 devices without compatibility evidence.
- Current Foundation Models adapter toolkit version 26.0.0 is specifically tied to OS 26 and is not compatible with OS 27+; this demonstrates why adapter/model assumptions must be versioned.

## Context Is an API Property

- Query/record the current model context rather than assuming a generic LLM context window.
- Current Foundation Models APIs expose token counting and model context-size information for the system model.
- Measure the actual prompt, instructions, conversation history, image/tool context, and expected response within the available context.
- Implement explicit context trimming/summarization/retrieval strategy where sessions can grow.
- Do not claim the Private Cloud Compute/server model context applies to the on-device system model; they are distinct routes.

## On-Device Multimodality

- Current iOS/iPadOS 27 Foundation Models can accept image input and can combine the model with on-device Vision tools such as OCR/barcode reading.
- Distinguish direct multimodal model input from deterministic Vision/OCR tool calls.
- Use deterministic OCR/barcode/structured extraction where exact text/codes matter rather than relying solely on free-form visual reasoning.
- Include image preprocessing, memory, latency, and battery in mobile fit.
- Do not infer audio/video support from image support without current evidence.

## Core AI / Bring-Your-Own Model

- Treat Core AI as the current Apple OS-level path for bringing supported custom models on-device on Apple Silicon.
- Current Apple documentation positions Core AI for local models and exposes integration with Foundation Models sessions, including specialized/open models when the system model is not suitable or available.
- Require exact source model, Core AI export/optimization artifact, supported device/OS, model precision/quantization, context, and runtime feature coverage.
- Do not assume an arbitrary Hugging Face/PyTorch checkpoint can run directly inside an iOS app without conversion/packaging/runtime evidence.
- Preserve model license and redistribution rights for app-bundled/downloaded models.

## Core ML Route

- Use Core ML for supported converted/domain-specific models when it remains the suitable deployment path.
- Current Core ML documentation supports on-device execution using CPU, GPU, and Neural Engine as appropriate and emphasizes local operation without network dependency.
- Treat compute-unit choice as model/operator/runtime-specific rather than assuming every Core ML model runs fully on Neural Engine.
- Record model conversion/tool version, deployment target, compute units, precision, preprocessing/postprocessing, and performance.
- Keep Core ML and Core AI artifacts/routes distinct when their capabilities differ.

## Neural Engine, GPU, and CPU

- Do not infer Neural Engine execution from device marketing or Apple Intelligence eligibility.
- Verify the chosen runtime/model's actual compute-unit support.
- Record fallback/partitioning when unsupported operators execute on CPU/GPU.
- Measure end-to-end latency rather than only accelerated subgraph latency.
- Keep unsupported/unmeasured compute paths `Unknown`.

## App Memory Is Not Installed Device RAM

- Treat app/process memory as an operational mobile constraint independent of nominal system memory.
- Measure peak resident memory for model weights, KV/cache, images, runtime buffers, tool results, UI state, and concurrent app work.
- Handle memory warnings/termination behavior under realistic device pressure.
- A model that can theoretically fit total device RAM but causes jetsam/app termination does not fit.
- Do not publish model tiers from nominal iPhone/iPad RAM capacity.

## Storage and Model Delivery

- Account for app bundle size, on-demand/background assets, model downloads, adapters, caches, and versioned model duplication.
- Current Foundation Models custom adapters can be packaged as asset packs/background assets and are tied to exact system-model versions.
- Verify offline availability after installation/update.
- Define cleanup/rollback for superseded custom artifacts.
- Do not require large re-downloads on every launch or silently consume excessive user storage.

## Foundation Models Adapters

- Treat custom adapters as an advanced, version-coupled specialization route rather than a generic fine-tuning switch.
- Current Apple adapter guidance states each adapter is compatible with one specific system model version and can require separate training/toolkit versions for different OS/model versions.
- Adapter deployment requires current entitlement/process requirements; recheck them before recommending production use.
- Measure whether prompt/tool/retrieval engineering can solve the use case before accepting adapter lifecycle burden.
- Evaluate adapter quality separately on every supported OS/system-model version.

## Private Cloud Compute / Server Route

- Keep Apple Foundation Model on Private Cloud Compute distinct from on-device execution.
- Current WWDC26 material describes a larger reasoning/server model with a 32K context route through Private Cloud Compute for eligible developer/app scenarios.
- Treat current eligibility, pricing/program requirements, model identity, quotas, and privacy guarantees as mutable service properties.
- Do not call this route `local` merely because it uses the Foundation Models API.
- Map network dependency and sensitive-data policy before using server fallback.

## Third-Party Hosted Providers

- Current Foundation Models framework can use compatible server providers through the common language-model interface.
- Preserve provider identity, data path, API/account terms, retention, model version, region, and cost even when the application API looks the same.
- Do not let a framework abstraction hide that prompts/images leave the device.
- Require explicit routing/fallback policy so a failed on-device request does not silently cross to an unapproved provider.

## Offline Behavior

- Test airplane/offline mode explicitly for every route claimed to be local.
- System/model asset availability can depend on device/OS/user state; handle unavailable/downloading/not-ready states.
- Custom on-device model routes must not require hidden runtime/model downloads after the app is deployed if offline operation is required.
- Server/PCC/hosted routes should fail clearly or fall back only according to approved policy.

## Battery, Power, and Thermal Behavior

- Measure sustained inference under intended mobile use, not only one short request on a cool device.
- Record battery drain, thermal state, throttling, device temperature/user comfort, and foreground/background limitations where relevant.
- Compare on-device versus server/hybrid route by accepted-result latency and energy/user experience.
- A fast initial model that thermally throttles during repeated use is a conditional fit.

## Interaction Latency

- Measure time to first useful response and total task completion for the actual UI interaction.
- Include image capture/decoding, model/tool initialization, context preparation, local retrieval, network when applicable, and rendering.
- For streaming text, record TTFT and sustained generation separately.
- Do not use isolated token-generation or Core ML prediction timing as complete app latency.

## Background Execution

- Treat background processing limits as a separate mobile constraint.
- Verify whether model execution, downloads, indexing, or long-running generation can legally/reliably run in the intended iOS/iPadOS lifecycle state.
- Do not design a persistent local server/agent as if iOS were a desktop daemon environment.
- Handle app suspension/termination and resume/retry safely.

## Agent and Tool Use

- Foundation Models can invoke app-defined tools; treat tool-capable local agents as side-effecting even when the model itself is on-device.
- Restrict tools to app-scoped capabilities and validate arguments/destinations deterministically.
- Keep permission-protected resources behind native OS authorization.
- Do not let untrusted documents/web content expand tool authority through prompt injection.
- Require explicit confirmation for consequential external/network/account actions.

## Privacy and Sensitive Data

- Distinguish on-device processing from PCC/third-party server processing in UI/policy where material.
- Minimize logging of prompts/images/tool results containing sensitive user data.
- Preserve iOS privacy permissions for photos, camera, microphone, contacts, location, files, and other resources.
- Do not infer that all Foundation Models framework providers inherit Apple on-device/PCC privacy guarantees.

## Model Updates and Evaluation

- Treat OS updates as possible model behavior changes.
- Current Apple guidance explicitly instructs developers to test prompts with new system-model versions after OS updates.
- Maintain a representative evaluation set across supported device/OS/model versions.
- Include unsupported/unavailable model state, context overflow, safety refusal, tool error, multimodal input, and offline cases.
- Re-run after OS, system model, adapter, Core AI/Core ML artifact, prompt/tool, or provider changes.

## Quality and Task Fit

- Evaluate the actual educational/assistant/coding/creative/etc. task rather than assuming the system model is adequate because it is built in.
- Current Apple documentation positions custom local models and server models for capabilities the system model may not cover.
- Compare on-device model, custom model, and approved hosted/PCC alternatives by accepted-result quality, latency, battery, privacy, and implementation burden.
- Preserve `Unknown` for capabilities not measured on the target device/OS.

## Practical Fit Outcomes

- `Fits well`: exact device/OS/model route passes availability, task quality, context, app-memory, latency, thermal/battery, and offline/network-policy thresholds.
- `Fits conditionally`: requires a newer OS/device, smaller custom model, reduced context, network/PCC fallback, limited repeated use, or another explicit acceptable constraint.
- `Does not fit`: exact route fails device/API availability, memory, quality, latency, thermal, modality, or privacy/network requirements.
- `Unknown`: exact device/OS/model/runtime combination lacks current support or measurement.
- Do not assign fit from Apple Intelligence eligibility or SoC generation alone.

## Canonical Links

- Link concrete custom model facts to Model Reference.
- Link Core AI/Core ML/Foundation Models framework/service details to canonical software/service owners when materialized.
- Link personal/mobile user scenarios when user goal/data constraints rather than hardware fit dominate.
- Keep Mac/MLX hardware selection in `computers/apple/`.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current Apple Foundation Models updates and WWDC26 iOS/iPadOS/machine-learning documentation, current `SystemLanguageModel` documentation, current Core AI integration material, Core ML documentation, and current Foundation Models adapter training guidance.
- Current Apple evidence establishes an OS-managed on-device system model whose behavior/version changes with OS updates, current iOS/iPadOS 27 multimodal/common-provider Foundation Models APIs, separate Private Cloud Compute/server routes, and current custom on-device Core AI/Core ML routes. These do not establish practical fit on every iPhone/iPad.
- Foundation Models APIs/models, PCC eligibility/service terms, Core AI/Core ML features, adapters/entitlements, OS/device eligibility, app lifecycle behavior, and third-party provider integrations are mutable; recheck them before rendering recommendations.
- Exact target device/OS/model route and measured app quality/memory/latency/battery remain the fit authority.

## Validation

- System-provided on-device, PCC/server, custom Core AI/Core ML, third-party local, and hosted-provider routes remain distinct.
- Apple Intelligence availability is not treated as arbitrary custom-model NPU support.
- OS/system-model version is part of every system-model behavior claim.
- App process memory/termination is measured rather than total device RAM used as a model tier.
- Neural Engine/GPU/CPU execution is model/runtime specific and fallback is represented.
- Context, multimodal assets, storage/model delivery, offline state, battery/thermals, and app lifecycle are first-class constraints.
- Adapter version coupling and lifecycle are explicit.
- Network/provider abstractions do not hide data leaving the device.
- Hardware purchasing remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
