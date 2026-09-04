# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual whose recurring AI use crosses **languages, scripts, speech, images, and changing local context**, especially while travelling, living abroad, communicating with people who use other languages, or working with multilingual personal information.
- Make the exact language pair/direction and modality part of model selection. `English → Ukrainian text`, `Ukrainian → Spanish live speech`, `Japanese sign/menu image → Ukrainian`, and multilingual trip research are materially different routes.
- Distinguish this scenario from `everyday-home-user/`: multilingual/travel behavior is not an occasional feature here; language coverage, voice/OCR, offline fallback, and current local information repeatedly determine whether the route works.
- Distinguish it from the task-first `translation-and-localization` decision guide: this scenario owns the **combined traveller/user context**—network reliability, mobile device, live conversation, privacy, current places/times/rules, and mixed modalities—while the guide owns deep translation-model evaluation by pair/direction/domain/quality tier.
- Distinguish it from `accessibility-first-user/`: captions/voice can overlap, but accessibility becomes the owner when assistive-technology compatibility and disability-related access are the first-order decision.
- Distinguish it from `privacy-first-or-offline-user/`: offline packs/local models can be critical on a trip, but that scenario becomes the owner only when no-egress/offline processing dominates the whole workflow.

## Separate the Travel Workloads

- Classify the recurring need before selecting one assistant/model:
  - general trip planning and current local research;
  - text translation and rewriting;
  - live two-way conversation;
  - camera/OCR translation of signs, menus, tickets, forms, labels, and notices;
  - speech transcription/captioning;
  - multilingual drafting/messages;
  - local cultural/context explanation;
  - document understanding for bookings, visas, transport, insurance, or other travel paperwork.
- Do not force every workload into one general LLM. A managed multimodal assistant, dedicated translation service, OS accessibility/translation feature, local STT, local VLM, and web/search tool can each be the right component.
- For recurring translation-quality decisions, link the task-specific translation/localization guide and evaluate exact pair/direction separately.

## Default Connected Route

- Use a current managed multimodal assistant as the default broad route when Internet access and the data boundary allow it, because travel tasks frequently mix text, voice, image/screenshot, files, and current web information.
- Current canonical assistant-workspace examples include ChatGPT and Gemini; evaluate exact language, voice, image/file, web/search, and mobile-device behavior rather than ranking the providers globally.
- Current ChatGPT Voice supports live conversational interaction on supported product surfaces and can use current product tools such as web search according to plan/mode availability. Treat model/plan/tool details as mutable.
- Current Gemini Live supports conversational speech, interruption, and captions on supported mobile surfaces. Language/feature/device rollout remains mutable and must be tested for the traveler's exact languages.
- Choose one primary connected assistant after a representative trip-language evaluation rather than constantly switching services. Add a specialist only for a recurring gap such as translation quality, offline use, OCR, or voice latency.

## Language Pair and Direction Are Mandatory

- Never use `multilingual` as a translation-quality claim. It establishes only that a model can plausibly process multiple languages.
- Evaluate each important **pair and direction** separately. A model that is good at English → Ukrainian can perform differently at Ukrainian → English or Ukrainian ↔ another lower-resource language.
- Include dialect, register, code-switching, script, transliteration, names, addresses, numbers, dates, honorifics, and domain terminology in representative tests.
- For travel conversation, test realistic speech: background noise, non-native pronunciation, local accents, short fragments, interruptions, repeated numbers, station/airport names, and proper nouns.
- Preserve ambiguity instead of inventing one meaning. For a short sign, menu item, colloquial phrase, or ambiguous instruction, the assistant should ask for context or show alternatives when needed.
- Route production/high-quality linguistic evaluation to `decision-guides/language-and-research/translation-and-localization/`, which requires semantic accuracy, omissions/additions, terminology, structure, reviewer effort, and accepted-result cost rather than multilingual benchmark transfer.

## Current Local Text Candidates

- Use `Phi-4 Mini Instruct` as a compact local/offline text candidate when the required languages are within its supported multilingual scope and exact user testing confirms acceptable translation/explanation quality. Its official current model evidence includes Ukrainian among supported languages, but this is not proof of quality for every pair/direction.
- Use `Qwen3 8B` as a current broader local multilingual text/reasoning candidate when the mobile/laptop hardware can support its exact artifact/runtime with useful latency. Its broad multilingual support is eligibility evidence only.
- Use `Qwen3 14B` only when the target laptop/workstation has enough measured resources and its pair-specific quality gain justifies higher memory, power, and latency.
- Do not name a local model as `best translator` without direct pair/direction evaluation. A dedicated translation model/service may outperform the general LLM for fixed translation tasks.

## Image, Sign, Menu, and Document Route

- For camera/screenshot translation, distinguish **OCR/extraction** from translation/reasoning. Wrong extracted text can produce a fluent but wrong translation.
- Use a managed multimodal assistant when convenient and permitted, or evaluate `Gemma 4 E2B Instruct` / `Gemma 4 E4B Instruct` as current compact local multimodal candidates when offline/private image/document understanding is needed and the exact runtime supports the modality path.
- For small print, stylized signs, handwriting, receipts, tickets, tables, or dense forms, require the user to inspect/confirm critical extracted numbers/names/dates/addresses before acting.
- Preserve the original image/document so important translations can be rechecked or shown to a human.
- Do not use a general VLM as sole authority for medication labels/dosage, immigration/legal documents, safety warnings, allergen information, financial amounts, or other high-consequence text.

## Live Conversation Route

- Measure end-to-end interaction rather than text benchmark quality: speech recognition, language identification, translation, response generation, speech output, turn detection, interruption, latency, transcript/caption access, and correction burden.
- Prefer a route that lets the user **show the text transcript** when speech output is misunderstood. Text can act as a cross-check for names, addresses, prices, dates, and numbers.
- Test both conversation directions with the same people/languages expected in practice. Do not infer recognition of local accent/noisy speech from clean English demos.
- Keep the original utterance accessible when possible so the user can replay/retry or switch to typed text.
- For critical medical, legal, police, emergency, immigration, consent, or other high-stakes conversations, use a qualified human interpreter/official channel when available. AI translation can assist but should not be the sole communication authority.

## Offline and Weak-Connectivity Route

- Assume that roaming, underground transit, rural areas, border crossings, overloaded event networks, or exhausted data plans can remove cloud access at the worst moment.
- Before travel, stage the **minimum offline capability** needed for critical recurring tasks: local language/translation packs where available, maps/reference material, essential documents, local STT/caption tools, or a compact local model when exact device fit is proven.
- Test offline mode **before the trip** with mobile data/Wi-Fi disabled. Do not discover hidden model/runtime/download/account dependencies while travelling.
- Do not make a full local LLM mandatory when platform-native offline translation/transcription already solves the critical task with lower battery/resource cost.
- If an offline local general assistant is justified, prefer the smallest model that meets the user's important language/task quality and latency; a larger model that drains the battery or responds too slowly may be worse travel fit.
- When strict no-egress/offline behavior, staged updates, local RAG, or complete local data-path control dominates the route, continue into `privacy-first-or-offline-user/`.

## Mobile Hardware, Battery, and Thermal Fit

- Treat mobile inference as a sustained device-use problem. Include RAM/unified memory, NPU/GPU/CPU runtime support, storage, battery consumption, thermal throttling, camera/audio processing, and other apps/navigation running concurrently.
- A model that launches on a phone/tablet is not automatically practical during travel. Measure response latency and battery/thermal effect over repeated use.
- For laptop travel, include usable memory after normal browser/maps/productivity apps, charger availability, power profile, and whether CPU/GPU inference is practical away from mains power.
- Route exact device analysis to `../../../hardware/`, especially `../../../hardware/sub/mobile/` and `../../../hardware/sub/computers/`; do not create generic `phone can run X parameters` rules here.

## Current Information vs Language Generation

- Separate **translation** from **current local facts**. A model can translate perfectly while hallucinating that a train runs, a restaurant is open, a visa rule applies, or an address is correct.
- For opening hours, transport disruptions, tickets/fares, border/visa rules, safety alerts, weather, events, local laws, health requirements, and other changing facts, use a current authoritative source/search route and verify the source date/location.
- Treat generated itinerary recommendations as hypotheses until availability, booking conditions, location, and current price are checked.
- When translating a current authoritative page, preserve the original source link and distinguish `what the source says` from additional model advice.

## Names, Addresses, Numbers, and Structured Data

- Treat proper nouns and structured travel information as high-error-impact fields: passenger names, passport details, booking references, flight/train numbers, gates, addresses, phone numbers, dates/times/time zones, currency amounts, and medication/allergy terms.
- Ask the model to preserve/transliterate names carefully and verify against the original document or local script.
- Never let the model silently convert dates, times, currencies, units, or addresses without showing the original value when error consequences are material.
- For bookings/forms, copy critical structured data from the source or use deterministic form validation rather than accepting a conversational paraphrase.

## Travel Documents and Privacy

- Minimize uploaded personal data. Passports, visas, tickets, insurance, medical records, payment documents, location history, hotel reservations, and messages can reveal a high-value personal profile.
- Crop/redact an image or provide only the necessary field when the model does not need the whole document.
- Do not upload passwords, payment-card secrets, recovery codes, private keys, or one-time authentication codes to a general assistant.
- For hosted voice/camera/screen use, consider bystanders and surrounding private information, not only the traveler's own data.
- Apply the provider-chain rule to hosted assistants, translation services, routing intermediaries, and connected tools. A translation task can expose the same sensitive content as the original document.

## Cultural and Pragmatic Assistance

- Allow the model to explain tone, politeness, register, local idioms, or cultural context as **guidance**, but avoid presenting broad cultural stereotypes as fact.
- When drafting messages, specify audience, relationship, formality, country/region, and intended effect; literal translation can be inappropriate even when semantically accurate.
- For sensitive social/legal/official contexts, ask for alternatives and explain uncertainty rather than manufacturing confidence about etiquette or norms.

## Learning and Pronunciation Use

- A traveler learning/practising a language can use voice conversation, role play, corrections, and explanations as a secondary route.
- Distinguish `natural enough for travel practice` from qualified language instruction or pronunciation assessment. The model can give useful feedback without being an authoritative phonetics teacher.
- Ask for corrections that preserve the user's intended meaning and explain why a phrase sounds unnatural rather than only replacing it.
- If language learning rather than travel/multilingual task completion becomes the primary objective, route into future learning content rather than growing this scenario into a course.

## Cost and Accepted Multilingual Outcome

- Compare **cost per accepted multilingual/travel outcome**, including subscription/API cost, roaming/data, retries, correction/human-interpreter effort, battery/power, offline setup/storage, and the consequence of wrong information.
- A free hosted assistant can be the best default if it reliably handles the needed languages/modalities and connectivity is stable.
- A paid assistant is justified when limits/voice/image/web capability or quality savings are recurring; do not maintain multiple paid assistants merely for nominal language coverage.
- A local model is justified by offline/privacy/control needs and measured language quality—not by avoiding a small subscription while incurring poor latency, battery drain, and correction burden.
- A specialist translation service/human interpreter can be lower total cost for a critical task than correcting a general LLM's mistakes.

## Escalation Triggers

- Move from one managed assistant to a dedicated translation route when pair-specific translation quality is the recurring bottleneck.
- Move to local/offline packs/models when connectivity repeatedly blocks essential communication and the device has verified fit.
- Move from local to hosted when local pair quality, speech/OCR accuracy, or latency is inadequate and the data boundary permits it.
- Add a multimodal model only when camera/document understanding is a recurring need; do not pay resource cost for modalities that are not used.
- Move toward `accessibility-first-user/` when captioning, assistive technology, or an accessibility-related modality determines the route.
- Move toward `privacy-first-or-offline-user/` when no-egress/offline behavior dominates the entire workflow.
- Move toward professional translation/localization review when production/legal/business linguistic quality rather than personal travel communication is required.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when offline/local multilingual model fit depends on the exact device.
- Use `../../../hardware/sub/mobile/` for phone/tablet on-device routes and `../../../hardware/sub/computers/` for laptop/local workstation routes.
- Use another hardware class only when the traveler actually relies on a separate edge/home device; do not make travel AI require a server by default.

## Canonical Links

- Link current managed assistant examples to canonical service owners such as `catalog/services/assistant-workspaces/chatgpt` and `catalog/services/assistant-workspaces/gemini` when named.
- Link current compact local text candidates to `catalog/models/microsoft/phi/phi-4/models/phi-4-mini-instruct`, `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b`, and `.../qwen3-14b` when named.
- Link compact local multimodal candidates to `catalog/models/google/gemma/gemma-4/models/e2b-instruct` and `.../e4b-instruct`.
- Link deep model translation evaluation to `decision-support/selection/models/decision-guides/language-and-research/translation-and-localization` instead of reproducing pair-specific model rankings here.
- Dedicated translation applications/services remain outside this model-scenario owner unless/until their canonical catalog entities are explicitly used.

## Evidence and Freshness

- Re-evaluated on **2026-08-23** using current canonical assistant/model owners, current ChatGPT/Gemini voice-product evidence, official multilingual model evidence, and the selected translation/localization decision-guide contract.
- The translation guide already establishes the canonical rule that exact language pair, direction, domain, content type, terminology, privacy boundary, and quality tier must be tested separately; multilingual/model support alone is eligibility evidence.
- Voice/caption/image/web features, language support, plan limits, model aliases, regional product availability, mobile OS offline capabilities, and local runtime support are mutable; recheck them before rendering current advice.
- Provider multilingual benchmark/model-card claims do not replace pair-specific independent/user acceptance testing, especially for speech, dialect, OCR, colloquial language, and high-stakes content.

## Validation

- The route is distinct because multilingual travel combines pair/direction quality with voice, OCR, mobile hardware, network/freshness, privacy, and current local information.
- `Multilingual support` is never presented as universal translation-quality evidence.
- Connected assistant, dedicated translation, local/offline model, OS feature, and human interpreter remain distinct routes.
- Current local facts are verified from current sources and are not inferred from the model's translation ability or training memory.
- Structured travel values/names/numbers/dates are verified against originals.
- Offline readiness is tested before travel and does not require a general local LLM when a narrower offline tool solves the task.
- Voice/OCR/local routes include exact language and real environment tests.
- High-stakes medical/legal/emergency/immigration communication preserves qualified human/official verification.
- Sensitive travel documents and surrounding camera/screen data remain subject to the shared data boundary.
- Mutable current claims carry the 2026-08-23 evidence boundary.
