# Documentation Requirements

## Route Fit

- Cover Pixel/Google-Tensor Android devices where AICore/Gemini Nano system GenAI or Google-supported custom on-device model execution materially constrains selection.
- Require exact device/Pixel model, Tensor generation, Android/API level, AICore/ML Kit GenAI feature status, Gemini Nano base-model identity when exposed, custom-runtime/export if used, memory/storage, battery/thermals, and foreground/background requirements before assigning fit.
- Keep this route scoped to Google Tensor/Pixel-specific evidence; Android devices from Qualcomm/MediaTek/Samsung follow their own SoC routes even when they can access the same high-level ML Kit GenAI API.
- Keep phone purchasing outside this route.

## System Gemini Nano vs Custom Model

- Treat AICore/Gemini Nano as a system-managed model route rather than an app-owned model artifact.
- Treat LiteRT/custom model deployment as a separate route with its own artifact, operator/delegate, packaging, memory, and quality evidence.
- Do not infer custom Tensor/TPU/NPU acceleration from the fact that Gemini Nano runs on-device.
- Do not describe an ML Kit GenAI call and a custom LiteRT model as the same model/runtime path.
- Preserve hosted Gemini/API fallback as a third separate route with a different data/network boundary.

## Current ML Kit GenAI Boundary

- Current ML Kit GenAI APIs are built on AICore and Gemini Nano and provide high-level on-device APIs for summarization, proofreading, rewriting, image description, speech recognition, and prompt-based text/multimodal generation.
- Treat each API capability as feature/device/model/version specific.
- Current documentation states that feature availability can vary with the particular device configuration and downloaded models; use `checkFeatureStatus()`/`checkStatus()` as runtime authority rather than a static device-family assumption.
- Record the exact GenAI API/artifact version and requested options/language/mode.
- Do not assume one supported ML Kit GenAI feature implies all other GenAI features are available on the same device.

## Gemini Nano Version Is Device-Dependent

- Current ML Kit documentation explicitly notes that different Gemini Nano base-model versions can run on different devices and can produce different outputs for the same prompt.
- Retrieve/record the base-model identity using the current API when available.
- Evaluate prompts against every device/model version the application supports.
- Do not write one behavioral guarantee for `Gemini Nano` without device/version evidence.
- Keep model updates through AICore/OS as a re-evaluation trigger.

## Current 2026 Model Evolution

- Current 2026 ML Kit releases add/adjust Prompt API model selection, structured output, system instructions, thinking mode, multi-image input, and larger output-token limits.
- Gemini Nano 4 is current on the newest Pixel generation and current release notes include compatibility work for Nano v4.
- Treat preview/stable models separately and record the exact selected model channel.
- Do not transfer a Pixel 11/Nano 4 capability to older Pixel/Tensor hardware without supported-device evidence.
- Re-test after AICore/model updates because API compatibility does not guarantee identical outputs.

## Runtime Availability Is Dynamic

- AICore model/configuration state can be downloading, initializing, unavailable, busy, or unsupported.
- Current documentation describes setup/reset cases where AICore needs network time to obtain current configuration/model assets before features become available.
- Check feature status before exposing UI and implement explicit unavailable/download/retry/fallback states.
- Do not promise immediate offline availability on a freshly reset/newly configured device until the required assets are present.
- Once the supported GenAI feature is prepared, current ML Kit documentation describes inference as on-device and usable without reliable connectivity; verify the exact feature/model state.

## Bootloader and Device Integrity Boundary

- Current ML Kit GenAI feature documentation states that these APIs are not supported on devices with an unlocked bootloader.
- Treat bootloader/device-integrity state as an availability constraint for the system-model route.
- Do not assume a developer/rooted device reflects production AICore behavior.
- For custom model runtimes, document any different device-integrity requirement separately.

## Foreground-Only System GenAI

- Current ML Kit GenAI documentation states that GenAI inference is permitted only while the application is the top foreground app and returns a background-use error otherwise.
- Treat this as a hard product-lifecycle constraint for AICore/ML Kit GenAI workflows.
- Do not design persistent/background summarization/indexing/agent services around system GenAI without a separately supported path.
- Model long tasks around Android lifecycle interruption and user navigation.
- Custom LiteRT/on-device models can have different background constraints; verify them separately.

## Per-App and Battery Quotas

- Current AICore/ML Kit GenAI enforces per-application inference quotas and can return `BUSY` or battery-use quota errors.
- Measure realistic repeated-use behavior rather than one successful call.
- Implement bounded backoff/retry and a user-visible degradation/fallback plan.
- Do not treat developer-preview quota bypass as production behavior.
- Include quota behavior in accepted-result availability and latency.

## Developer Preview Is Not Production Evidence

- Current AICore Developer Preview can expose preview models and quota bypass for testing.
- Google explicitly warns preview models can be slower, less accurate, consume storage, and affect system stability.
- Keep preview-model results labeled as preview and do not make production recommendations from them without stable-release revalidation.
- Record AICore preview/stable state in benchmark evidence.

## First-Inference and Warm-State Latency

- Current AICore preview documentation notes that first inference can be substantially slower because the model must initialize/load.
- Measure first invocation, subsequent invocation, long-idle reactivation, and repeated-use latency separately.
- Do not report only warm streaming performance.
- Include feature-status/model-download preparation in first-use UX when relevant.

## Prompt and Context Constraints

- Treat token/input/output limits as API/model/version-specific.
- Current feature APIs can impose short-input limits independently of the general Prompt API; for example rewriting and summarization expose bounded task-oriented inputs.
- Record prompt/instruction/image tokens and output limits for the chosen API.
- Do not substitute the cloud Gemini context window for Gemini Nano/AICore limits.
- Route document-scale/large-context work to chunking/retrieval or hosted models when local limits cannot meet the objective.

## Structured Output and Tooling

- Use current structured-output/system-instruction capabilities where they materially improve deterministic app integration.
- Validate generated structures/types/content before using them in application state.
- Do not infer correctness from schema conformance.
- ML Kit GenAI APIs are primarily model-generation surfaces; external side effects still require explicit Android app logic/permissions/confirmation.

## Multimodal Input

- Current Prompt API supports current text-and-image/multi-image routes on supported configurations.
- Measure image preprocessing, resolution/number limits, memory, latency, and battery.
- Use deterministic ML Kit/Vision-style barcode/OCR/recognition APIs for exact structured perception when they are a better fit.
- Do not infer arbitrary video/audio multimodality from image support; speech recognition has its own supported-device/mode matrix.

## Advanced Speech Route

- Treat GenAI-powered speech recognition as a separate feature route from ordinary on-device speech recognition.
- Current ML Kit documentation distinguishes broadly available basic on-device speech support from advanced GenAI mode with a much narrower device matrix.
- Verify exact Pixel/device support before routing speech to Gemini Nano.
- Do not generalize Pixel 10/current advanced-speech support to all Tensor devices.

## Custom LiteRT Route

- Use LiteRT/custom models when the application needs a known app-owned model, broader device control, a specialized task, or system Gemini Nano is unavailable/inappropriate.
- Require exact TFLite/LiteRT artifact, quantization, input shapes, operators, delegate/accelerator, Tensor-generation/device support, and Android runtime version.
- Verify whether execution is CPU/GPU/NPU/vendor delegate rather than assuming Tensor hardware automatically accelerates the model.
- Preserve model download/bundle size and app storage.
- Measure complete app pipeline and accepted quality.

## System Memory and App Pressure

- Treat Android app memory/process pressure separately from nominal device RAM.
- Include model/system service memory, app UI, images/audio, custom-model weights, runtime buffers, KV/cache, and other foreground apps.
- Measure low-memory/termination behavior under realistic device pressure.
- Do not publish fixed RAM-to-model tiers for Pixels.

## Battery and Thermal Behavior

- Measure repeated on-device generation under intended user workflow.
- Current AICore exposes a battery-use quota, reinforcing that sustained on-device generation is a device-health constraint rather than unlimited compute.
- Record thermal state, throttling, battery drain, charge state, and user-visible latency.
- A route that is responsive for one request but quota/thermal-limited during realistic use is conditional fit.

## Privacy Boundary

- Current ML Kit GenAI documentation states input/inference/output are processed locally for the supported AICore APIs and that the shared Gemini Nano model avoids app-specific duplicate downloads.
- Treat this on-device property as specific to AICore/ML Kit GenAI, not to hosted Gemini or arbitrary connected tools.
- Minimize app logs containing model inputs/outputs.
- Keep Android runtime permissions and app data-isolation controls for camera/photos/microphone/files/etc.

## Hosted/Hybrid Fallback

- Keep hosted Gemini/other provider routes explicit when the local model is unavailable, context-limited, quota-limited, or insufficiently capable.
- Do not silently fall back from local AICore to cloud for sensitive data.
- Define user/policy consent, provider/model, network error, and offline behavior.
- Compare accepted-result quality/latency/battery/privacy rather than assuming on-device is always preferable.

## Quality Evaluation

- Evaluate across all supported device/Nano versions because current documentation explicitly warns output can differ by base-model version.
- Include unsupported feature, model download/not-ready, BUSY/quota, context limit, background blocked, unlocked bootloader, image input, structured output, and offline cases.
- Track task quality, refusals, latency, correction effort, and fallback rate.
- Re-run after Android/AICore/ML Kit/model updates.

## Practical Fit Outcomes

- `Fits well`: exact Pixel/Tensor/Android/AICore/model/API route passes availability, task quality, limits, foreground lifecycle, latency, battery/thermal, and offline/privacy thresholds.
- `Fits conditionally`: depends on downloaded model state, particular Gemini Nano version, foreground-only use, quota, smaller task/context, newer Pixel generation, or hosted fallback.
- `Does not fit`: exact route fails device/API availability, quality, context/task limits, lifecycle, battery/quota, or privacy requirements.
- `Unknown`: exact device/Nano/API/custom-runtime path lacks current support or measurement.
- Do not assign fit from Tensor generation or Pixel branding alone.

## Canonical Links

- Link exact custom models to Model Reference and LiteRT/ML Kit/AICore software/services to canonical owners when materialized.
- Link Android parent/router for cross-SoC selection.
- Keep Qualcomm/MediaTek/Samsung Android hardware evidence in sibling routes.
- Link personal/mobile scenarios when user goal/data constraints dominate.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current ML Kit GenAI overview/feature documentation, current August 2026 release notes, current AICore Developer Preview documentation, current Android AI solution guidance, and current Gemini Nano 4/Pixel-generation developer material.
- Current evidence establishes system-managed Gemini Nano through AICore, feature/device-specific runtime status, differing Gemini Nano base versions across devices, foreground-only use, per-app/battery quotas, current multimodal/structured Prompt APIs, and a separate custom LiteRT route. It does not establish arbitrary custom-model Tensor NPU compatibility.
- Android/AICore/ML Kit versions, Nano models, supported devices/languages/features, quotas, API limits, model downloads, LiteRT delegates, and Pixel/Tensor generations are mutable; recheck them before rendering recommendations.
- Exact target device/runtime/model/API and measured app quality/latency/battery remain the fit authority.

## Validation

- System Gemini Nano/AICore, custom LiteRT, and hosted model routes remain distinct.
- AICore feature status at runtime is authoritative rather than a broad Pixel-generation assumption.
- Different Gemini Nano base versions/device behavior are represented.
- Foreground-only execution, quotas, battery limits, bootloader restrictions, initialization/download state, and first-run latency are first-class constraints.
- Pixel system-model support is not treated as arbitrary custom-model NPU support.
- Cloud context/capabilities are not assigned to Nano.
- App memory/battery/thermal and complete pipeline quality are measured.
- Hardware buying remains outside the route.
- Mutable current evidence carries the 2026-08-24 boundary.
