# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual whose AI route is primarily determined by **accessible input/output, assistive-technology compatibility, interaction latency, modality fallback, and the consequence of an accessibility failure** rather than by raw benchmark quality alone.
- Keep the scope broad enough to cover blind/low-vision, Deaf/hard-of-hearing, motor/dexterity, speech, and cognitive/learning accessibility needs, but do not imply that one product/model is best for every disability or access pattern.
- Distinguish this scenario from `everyday-home-user/`: here an otherwise strong assistant is a poor fit if the reader cannot reliably perceive, control, interrupt, navigate, or recover from it through their actual assistive workflow.
- Distinguish it from `privacy-first-or-offline-user/`: local/offline accessibility can be important, especially for always-available speech/caption/vision aids, but accessibility is the primary route owner unless no-egress/offline requirements dominate the entire stack.
- Treat disability and accessibility preferences as user-specific. Do not infer medical diagnosis, capability, or preferred interface from a disability label; require testing with the person's real device, assistive technology, language, and recurring tasks.

## Select the Accessible Product Route Before the Raw Model

- Start by testing the **complete interaction surface**, not only the underlying model. Screen-reader semantics, braille navigation, keyboard focus, captions, voice interruption, dictation reliability, gesture/control reachability, transcript access, contrast/text scaling, file-picker accessibility, and error recovery can dominate the practical result.
- Treat managed assistant applications, OS-integrated accessibility features, direct APIs, and local models as separate routes. A stronger raw model behind an inaccessible UI can lose to a weaker model integrated into an accessible platform.
- Prefer native OS accessibility mechanisms when they solve the task reliably with less friction. For example, current Android TalkBack integrates Gemini-backed image/screen descriptions and follow-up questions, while Android Live Caption/Live Transcribe and Apple Live Captions provide platform-level captioning/transcription paths. These are product/OS capabilities, not evidence that one general-purpose model is universally best.
- Evaluate the route on the user's actual assistive stack: VoiceOver/TalkBack or another screen reader, braille display if used, switch/keyboard/voice control, captions/transcription, hearing devices/audio setup, magnification, and preferred input modality.
- A route is not accepted until the user can independently start it, provide input, understand output, interrupt/correct it, navigate prior output, recover from a failure, and know whether a request completed.

## Accessibility Evaluation Workload

- Build a small representative acceptance set instead of evaluating accessibility from one demo:
  - ask and navigate a multi-paragraph text answer;
  - open/upload a document or image and find the resulting response;
  - interrupt or correct a voice interaction;
  - recover after recognition or model error;
  - switch between voice and text when one modality fails;
  - inspect citations/links or structured data;
  - perform one recurring real task such as screen description, drafting, caption-assisted conversation, form interpretation, or step-by-step planning.
- Measure **time and effort to accepted outcome**, not only model response latency. Count extra taps/keystrokes, focus traps, inaccessible controls, repeated speech recognition, re-reading, correction turns, and need for sighted/hearing/manual assistance.
- Test common failure conditions: noisy room, weak network, long answer, mixed-language input, image with small text, dynamic web/app UI, Bluetooth/audio device changes, accidental interruption, and app restart.
- Verify accessibility after material product updates. UI or voice changes can regress a previously good route even when the underlying model improves.

## Blind and Low-Vision Route

- Require screen-reader/keyboard/braille compatibility for the complete application flow. Generated text being technically selectable is not sufficient if navigation, attachments, citations, tool results, modal dialogs, or settings are inaccessible.
- For image/screen descriptions, prefer a current vision-capable route with easy follow-up questions and OCR/structure handling, but keep **description confidence separate from navigation/safety**.
- Current Android TalkBack 17 documents Gemini-assisted screen/image descriptions and improved dynamic-page/braille/keyboard behavior. Treat this as a current Android accessibility integration whose model and language support can change; evaluate the exact device/version rather than generalizing it to every Android phone.
- Use `Gemma 4 E2B Instruct` or `Gemma 4 E4B Instruct` as current local multimodal candidates only when an offline/private image/document-description route is needed and the exact runtime supports the required vision/audio path. Do not assume a local VLM reproduces TalkBack/VoiceOver integration or accessible UI semantics.
- For OCR-heavy documents/screens, compare a dedicated OCR/accessibility pipeline with general VLM description. A VLM can summarize layout/context while still misreading exact numbers, labels, coordinates, or small text.
- Never present AI image/screen description as a sole safety mechanism for street navigation, medication identification/dosing, machinery, emergency signs, financial/legal document confirmation, or another high-consequence visual judgment. Require an authoritative/deterministic/accessibility-specific confirmation route where an error could cause material harm.
- Preserve output structure useful to screen readers: clear headings, short lists, descriptive link wording, explicit state changes, and minimal visually dependent phrasing such as `as shown above` without textual context.

## Deaf and Hard-of-Hearing Route

- Treat **caption/transcription availability and latency** as first-class route constraints for voice assistants. A voice feature without usable text transcript/captions may be unsuitable regardless of conversational quality.
- Current Gemini Live supports captions and caption-size/style controls on supported mobile surfaces; use this as a current product example, not a permanent provider ranking.
- Current Android Live Caption processes supported captioning locally on-device, and Live Transcribe supports real-time speech/sound transcription with offline language packs on supported devices. These OS accessibility features may be preferable to routing every conversation through a general assistant when the task is transcription rather than reasoning.
- Apple Live Captions on supported Apple-silicon Macs can feed real-time captions to VoiceOver/braille workflows and processes the captioned audio on the Mac; availability/language support remains device/region dependent.
- For AI-assisted transcription/summarization, keep `Whisper` as a canonical speech-recognition family reference when a local speech-to-text route is relevant, but do not freeze one Whisper artifact as the best current accessibility choice without task/language/device evaluation.
- Measure word/semantic errors, speaker/name/number accuracy, delay, punctuation/segmentation, non-speech sound labels where material, language/accent support, and recovery when speech is missed.
- Do not rely on automatic captions/transcription alone for emergency communication, medical instructions, legal consent, critical numbers, or another high-consequence exchange; verify critical content through an appropriate communication channel.

## Motor, Dexterity, and Speech Route

- Evaluate whether the user can operate the assistant with their preferred input method: voice, keyboard, switch access, alternative pointing, dictation, or a combination.
- Prefer conversational voice when it materially reduces typing/pointing effort, but require a reliable text/alternative fallback for noisy environments, speech-recognition mismatch, privacy-sensitive settings, temporary voice loss, or connectivity failure.
- Current ChatGPT Voice supports live conversational speech on supported plans/devices, while Gemini Live supports free-flowing speech and interruption on supported mobile surfaces. Treat model/plan/platform details as mutable and test the user's actual language and speech pattern.
- Do not assume general speech recognition works equally well for dysarthria, atypical speech, strong accents, AAC-mediated speech, or quiet/strained voice. The route must be accepted from measured user-specific recognition/correction burden.
- Minimize interaction steps for recurring actions. A model that is slightly better but requires repeated inaccessible menus, model switching, or tool confirmations can be worse than a simpler route.
- For AI agents or device-control tools, require explicit confirmation and recoverability for consequential actions. Voice control is an input method, not proof that the model correctly understood intent or that broad permissions are safe.

## Cognitive, Learning, and Information-Processing Route

- Treat response controllability as a fit dimension: concise mode, step-by-step output, stable terminology, summaries, examples, read-aloud/voice, explicit assumptions, and ability to ask follow-up questions can matter more than maximal answer breadth.
- Prefer routes that can consistently follow an agreed output structure and allow the user to reduce information density without losing essential caveats.
- Distinguish assistance with comprehension/planning from authoritative decision-making. A confident simplified answer can still be wrong; source verification and high-stakes boundaries remain unchanged.
- Avoid framing AI as diagnosis or treatment for cognitive, neurodevelopmental, mental-health, or learning conditions. This scenario concerns accessible interaction and decision support, not medical evaluation.
- Evaluate whether memory/personalization helps or harms predictability. Persistent memory can reduce repeated setup but may also introduce unexpected assumptions; the user should be able to understand/control the relevant product behavior.

## Voice, Latency, and Turn-Taking

- For real-time conversational assistance, measure end-to-end turn latency, interruption/barge-in behavior, false interruption, recognition correction, transcript availability, and how easily the user can recover when the model talks over them or misunderstands them.
- Do not evaluate a live voice route from text-model benchmark quality alone. Speech recognition, speech generation, turn detection, network latency, product UI, and accessibility controls are part of the route.
- Keep a text transcript when it materially improves verification/review and the data boundary allows storage. For privacy-sensitive voice use, separately inspect whether audio/transcripts are stored, synced, or processed remotely.
- A lower-latency model can be the better accessibility choice when slow responses break conversational turn-taking or force repeated user effort, even if a slower model scores better on abstract reasoning benchmarks.

## Multimodal Fallback Design

- Require at least one practical fallback when the primary modality fails:
  - voice → text/keyboard/AAC-compatible input;
  - audio output → captions/transcript;
  - visual output → textual description/accessible structure;
  - touch/pointing → keyboard/switch/voice access;
  - hosted route → local/offline path only when accessibility must survive connectivity loss and the device supports it.
- Do not force all modalities into one model. A general assistant plus OS captioning, dedicated speech recognition, screen reader, OCR, or local VLM may produce a better accessible system than one nominally multimodal model.
- Keep modality handoff explicit so the user can tell whether a task has switched to another provider/model or data path.

## Offline and Local Accessibility

- Use local/offline processing when connectivity loss would remove a critical access channel, when speech/screens/documents must not leave the device, or when predictable local latency is valuable and exact hardware fit is proven.
- Separate OS-provided offline accessibility from self-hosted AI. Android Live Transcribe can use downloaded offline languages on supported devices, and platform caption/accessibility features may provide a more robust fallback than operating a general local LLM.
- For local general assistance, use compact text models such as `Phi-4 Mini Instruct` or `Qwen3 8B` only after measuring latency and input/output accessibility on the exact interface. A locally fast model behind an inaccessible frontend does not satisfy the route.
- For local visual assistance, evaluate Gemma 4 E2B/E4B exact multimodal runtime support and accepted-description quality; do not claim screen-reader integration from the model alone.
- If local STT is needed, link the canonical Whisper family and evaluate current artifact/runtime/language performance. Do not assume a large speech model is practical on a mobile/low-power device merely because it can be downloaded.
- When privacy/offline becomes the dominant constraint across the whole workflow, continue into `privacy-first-or-offline-user/` instead of duplicating its complete data-path/update contract here.

## Language and Locale

- Verify the exact languages supported by the **complete accessibility path**, not just the underlying language model. Voice recognition, TTS voices, captions, screen descriptions, OS accessibility integration, and UI localization can have different language coverage.
- Do not transfer an English accessibility result to Ukrainian or another language without testing recognition, pronunciation, captions, names/numbers, and assistive-technology behavior.
- Current accessibility integrations change language support over time—for example TalkBack's Gemini-backed description features expanded beyond their earlier English-only rollout. Treat language coverage as mutable and recheck the exact device/version.
- When multilingual communication becomes the dominant task rather than accessibility itself, route toward `traveler-or-multilingual-user` or translation decision guidance once materialized.

## Privacy and Sensitive Accessibility Data

- Treat live microphone, camera/screen share, screenshots, transcripts, accessibility logs, connected apps, and assistive context as potentially sensitive data paths.
- Screen-sharing/vision assistance can expose notifications, account names, health/financial information, bystanders, private messages, or authentication data that the user did not intend to send. Minimize the captured scope before sharing.
- Do not put passwords, one-time codes, recovery keys, or other authentication secrets into an assistant simply because entering them manually is difficult. Prefer accessible password-manager/OS credential mechanisms.
- Apply the shared data-boundary rule to hosted voice/video/screen assistance and all provider/tool chains. If no-egress/offline is required, use the dedicated privacy-first route and verify that every modality component is local.

## Reliability and Human Override

- Accessibility assistance can become safety-relevant when it mediates perception or control. Preserve an easy human/alternative override whenever the model can misdescribe, mistranscribe, or trigger actions.
- State uncertainty instead of inventing inaccessible detail. For unclear images/audio/screens, the assistant should ask for another capture, closer view, repeat, or alternate input rather than fabricate confidence.
- For numbers, dates, medication labels, addresses, identity details, financial amounts, commands, consent, or other high-impact data, require source/deterministic verification.
- Do not automate irreversible external actions solely from one accessibility-model interpretation. Require confirmation proportional to the consequence and ensure the confirmation itself is accessible.

## Cost and Accepted-Accessibility Outcome

- Compare routes by **cost per independently accepted accessible outcome**, including subscription/API cost, special hardware, device/network requirements, correction attempts, extra interaction steps, caregiver/assistant dependence, and failure/recovery time.
- A free product that repeatedly forces inaccessible workarounds can be more expensive in user time/independence than a paid accessible route.
- Conversely, do not require a paid frontier assistant when OS accessibility plus a free/basic model already meets the user's recurring needs.
- Treat specialist assistive features and general AI reasoning separately: pay for the component that materially improves the user's accepted outcome rather than accumulating subscriptions for nominal model quality.

## Escalation Triggers

- Change managed assistant when UI/assistive-technology compatibility, captioning, voice control, language support, or recovery burden—not raw answer quality—is the recurrent failure.
- Add a specialist vision/STT/TTS/caption/OCR route when a general assistant's modality is the bottleneck.
- Move to local/offline processing when connectivity/privacy repeatedly breaks a necessary access channel and exact local hardware can meet latency/quality needs.
- Move from local to hosted when local latency/quality makes the accessibility aid unreliable and the data boundary permits hosted processing.
- Escalate to professional/medical/official accessibility services when the consequence or domain requires expertise that a general AI assistant cannot safely provide.
- Move toward another scenario owner when the dominant requirement becomes privacy/offline, persistent home-lab service, travel/multilingual communication, family assistance, education policy, or professional confidential-data handling.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when exact device/accelerator constraints materially determine accessible local latency/modality.
- Use `../../../hardware/sub/mobile/` for phone/tablet on-device routes, `../../../hardware/sub/computers/` for desktop/laptop/Apple-unified-memory/GPU/NPU routes, and `../../../hardware/sub/single-board/` only when a dedicated assistive/embedded local node is actually part of the workflow.
- Do not copy platform-specific runtime/support matrices into this scenario.

## Canonical Links

- Link current managed assistant examples to canonical service owners such as `catalog/services/assistant-workspaces/chatgpt` and `catalog/services/assistant-workspaces/gemini` when named.
- Link compact local text candidates to `catalog/models/microsoft/phi/phi-4/models/phi-4-mini-instruct` and `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link compact local visual/audio candidates to `catalog/models/google/gemma/gemma-4/models/e2b-instruct` and `.../e4b-instruct`.
- Link local speech-recognition discussion to the canonical `catalog/models/openai/whisper` family until/if exact current Whisper artifacts are materialized as model leaves.
- Link accessibility/OS/runtime products to their canonical owners when they exist; do not represent platform accessibility features as canonical model facts.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current first-party ChatGPT Voice, Gemini Live, Android TalkBack/Live Caption/Live Transcribe/Voice Access, Apple Live Captions documentation, current local-model sources, and canonical AI Lab service/model owners.
- Current TalkBack 17 documents Gemini-backed image/screen descriptions plus improved braille/keyboard/dynamic-page behavior; Gemini Live documents conversational voice and captions; Android/Apple platform caption/transcription capabilities have device/language requirements. Treat all such product integration details as mutable.
- Voice models, plan availability, captions, screen/video sharing, accessibility controls, language coverage, assistive-technology compatibility, retention/data behavior, and platform support can change without changing the scenario architecture; recheck them before rendering a current recommendation.
- Provider/OS claims establish documented feature support, not independent proof that the workflow works for a particular disability, speech pattern, language, device, or high-stakes task. User-specific acceptance testing remains mandatory.

## Validation

- The scenario is materialized because accessible interaction changes the decision route, not merely because the user has an accessibility preference.
- Product/OS accessibility and assistive-technology compatibility can outrank raw model benchmark quality.
- Voice, vision, captioning, screen-reader/braille, keyboard/switch/voice control, and fallback paths are evaluated as separate capabilities.
- Accessibility is verified through the user's actual device, language, and assistive technology; disability labels do not imply one interface preference.
- AI screen/image descriptions and captions are not treated as infallible safety systems.
- Critical numbers/labels/actions require stronger verification and accessible human override.
- Local/offline accessibility routes require exact runtime/hardware/modality evidence and do not duplicate the full privacy-first contract.
- The complete language path is tested rather than inferring accessibility from LLM multilingual support alone.
- Data captured through microphones, screens, cameras, transcripts, and connected tools remains subject to the shared data boundary.
- Mutable current claims carry the 2026-08-23 evidence boundary.
