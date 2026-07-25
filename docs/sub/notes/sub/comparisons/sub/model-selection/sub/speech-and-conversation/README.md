# Choosing Speech and Conversation Models and Workflows

Use this guide to select an exact model, service, deployment, or smallest practical workflow for automatic speech recognition, transcription, speaker diarization, speech synthesis, or real-time voice interaction.

## Translations

- English

## Status

Initial canonical guidance verified on 2026-07-25. Speech models, language coverage, endpoints, pricing, regional availability, latency, licenses, and provider data controls change; verify the complete assignment before adoption.

## Define the workload first

Speech and conversation are several connected but independently measurable tasks:

- offline or batch automatic speech recognition (ASR);
- low-latency streaming transcription;
- verbatim, clean, normalized, caption, subtitle, meeting, interview, call, or dictation transcripts;
- speech-to-English translation or another explicit speech-translation route;
- language identification and multilingual or code-switching recognition;
- voice activity detection, endpointing, and end-of-turn detection;
- speaker diarization: determining who spoke when using anonymous speaker labels;
- speaker identification or verification against enrolled identities, which is distinct from diarization;
- word, phrase, sentence, and speaker timestamps;
- punctuation, capitalization, inverse text normalization, and domain-term adaptation;
- stock or designed text-to-speech (TTS);
- permitted custom voices or voice cloning;
- real-time voice agents combining audio transport, ASR, turn detection, reasoning or tools, and TTS;
- speech-quality and conversation-quality evaluation.

Do not select a single product from a generic speech leaderboard and assume that every stage is solved. A strong batch recognizer may be unsuitable for streaming. A low-latency ASR model may produce unstable partials, weak timestamps, poor code-switching, or unusable diarization. A natural TTS voice does not prove acceptable interruption behavior or complete voice-agent latency.

## Freeze the assignment unit

Treat a recommendation as a claim about one complete speech assignment. Record:

- exact downloadable artifact and revision, or exact API service, model ID, endpoint, region, and snapshot when exposed;
- provider, SDK or protocol version, runtime, hardware, weight format, quantization, prompts, parameters, tools, and permissions;
- batch, streaming, realtime, telephony, browser, device, edge, or embedded mode;
- input container, codec, sample rate, bit depth, channels, packet size, transport, clock, and resampling path;
- source language, locale, dialect, accent, code-switch pattern, domain, vocabulary, and expected speaker population;
- recording environment, microphone distance, channel topology, noise, reverberation, overlap, crosstalk, compression, clipping, and packet loss;
- transcript type, normalization rules, punctuation policy, redaction, timestamps, speaker labels, and output schema;
- TTS language, voice, style, pronunciation, speed, output format, and disclosure requirements;
- voice-agent turn-taking, interruption, tool, response, safety, escalation, and maximum-latency requirements;
- quality tier and risk classification;
- privacy, retention, residency, biometric, consent, copyright, and permitted-use boundaries;
- evaluation suite, reference creation, reviewers, evidence, limitations, and verification date.

Create a separate assignment when any material field changes. Do not transfer results between batch and streaming, studio and telephony audio, one language or accent and another, monologue and overlapping conversation, local and hosted deployment, or one TTS voice and another without evidence.

## Set task-specific acceptance gates

Use the repository's five [quality tiers](../combined-workloads/#quality-tiers) and translate the selected tier into observable speech gates.

| Tier | Speech and conversation gate |
| --- | --- |
| Exploration | Produce a labeled transcript, voice sample, or conversational prototype quickly; omissions, timing defects, and manual correction are acceptable, but output is not approved for consequential use |
| Concept draft | Preserve the central spoken meaning and conversation flow well enough for stakeholder review; disclose uncertain words, speakers, timings, and synthetic speech |
| Working result | Meet declared semantic, speaker, timing, technical, and latency thresholds; pass required validators and disclose known limitations |
| Production quality | Pass all pre-registered accuracy, latency, privacy, consent, accessibility, reliability, and independent review gates required for deployment |
| Exceptional quality | Add stricter multilingual, domain, acoustic, prosody, interruption, continuity, editorial, and specialist review where the extra value justifies the cost |

A low average word error rate, pleasant demo voice, or successful sample call is not enough. Define the failure classes that matter for the actual use: numbers, names, commands, obligations, safety instructions, speaker attribution, late endpointing, false interruption, or unsupported language changes.

## Select the smallest complete workflow

Start with constraints that can eliminate candidates:

1. Reject models or services whose language, locale, mode, license, region, privacy, retention, or permitted use does not cover the assignment.
2. Reject routes that cannot accept the real codec, channel layout, streaming protocol, duration, concurrency, or latency requirement.
3. Separate deterministic audio preparation, validation, formatting, redaction, and caption packaging from model inference where practical.
4. Evaluate eligible candidates on a frozen representative audio suite.
5. Compare total cost and latency per accepted minute, file, speaker-attributed transcript, synthesized utterance, or completed conversation.
6. Choose the least expensive assignment that consistently reaches the tier, then define a separately validated fallback.

The smallest complete system may contain:

- audio capture, echo cancellation, denoising, resampling, and voice activity detection;
- one ASR model or service;
- a separate diarizer or speaker-reconciliation step;
- deterministic normalization and schema validation;
- a terminology or phrase-hint layer;
- a language model for explicitly bounded cleanup, summarization, or response generation;
- a TTS model or service;
- transport and interruption control;
- independent human review for consequential transcripts or public synthetic speech.

Do not add a language model to silently rewrite a transcript unless the raw recognition output is preserved and every allowed transformation is explicit. Fluency correction can hide omissions, unsupported additions, wrong numbers, or wrong speaker attribution.

## Automatic speech recognition and transcription

### Define the transcript contract

Specify whether output must be:

- verbatim, including fillers, repetitions, false starts, and disfluencies;
- clean verbatim with a documented edit policy;
- normalized for numbers, dates, currency, measurements, acronyms, and punctuation;
- segmented for captions or subtitles under reading-speed and line-length constraints;
- aligned at word, phrase, sentence, or speaker-turn level;
- translated, summarized, redacted, or otherwise transformed after recognition.

Keep raw audio, raw ASR hypotheses, normalized output, reviewed output, and derived summaries as distinguishable artifacts. A polished downstream transcript must not erase uncertainty or make unsupported text appear spoken.

### Evaluate recognition errors by consequence

Measure overall WER or CER where appropriate, but also stratify by:

- language, locale, accent, dialect, speaker, age range, and speaking style;
- clean, noisy, reverberant, clipped, compressed, distant, and packet-loss conditions;
- monologue, dialogue, overlap, interruption, whispering, shouting, singing, and non-speech events;
- ordinary vocabulary, names, addresses, product terms, commands, code, numbers, dates, units, medication, legal clauses, and safety phrases;
- short utterances, long-form context, topic changes, silence, and music-only segments;
- first-pass streaming partials, stabilized partials, and final transcripts.

Track substitutions, deletions, insertions, hallucinated speech during silence or music, repeated text, language drift, normalization errors, and unsupported cleanup separately. A model with similar WER can be materially worse if its errors concentrate on high-value entities or commands.

### Terminology and prompting

Evaluate phrase hints, custom vocabulary, context prompts, or custom models as part of the complete assignment. Record:

- the exact term list and version;
- whether biasing creates false positives on similar-sounding words;
- behavior for inflected, declined, abbreviated, or code-switched forms;
- whether the provider exposes term-level or phrase-level controls;
- whether context persists safely across sessions;
- the accuracy gain and any regression outside the target terms.

Do not claim domain adaptation from one favorable example. Test both target terms and confusable negative cases.

## Speaker diarization and attribution

Speaker diarization answers **who spoke when** using anonymous labels such as `SPEAKER_00`. It does not establish a real identity. Speaker identification or verification compares speech with enrolled identities and introduces additional biometric, consent, security, and false-match risks.

Evaluate diarization independently from ASR:

- speaker-count accuracy;
- missed speech, false alarm, and speaker-confusion time;
- boundary error and turn fragmentation;
- overlap handling;
- short interjections and rapid speaker changes;
- same-gender, similar-voice, remote, quiet, or distorted speakers;
- channel-aware versus mono mixed audio;
- stability of labels within one recording;
- reconciliation between diarization segments, ASR words, punctuation, and captions.

Use diarization error rate (DER), its components, and a declared collar and overlap policy when appropriate. Report word-level speaker-attribution accuracy separately because a low segmentation DER does not guarantee that the transcript words were assigned correctly.

Do not assume speaker labels remain meaningful across files or sessions unless the system explicitly performs validated enrollment or cross-recording clustering. Never convert an anonymous diarization label into a person's name from guesswork or conversation context alone.

## Speech synthesis and voice output

Evaluate each exact voice, language, model, and mode separately. Measure:

- intelligibility and pronunciation, especially names, numbers, abbreviations, URLs, commands, and domain terms;
- language, accent, dialect, code-switching, and phoneme coverage;
- pacing, pauses, emphasis, emotion, prosody, and instruction or SSML adherence;
- stability across sentences, sessions, styles, and long-form output;
- noise, clipping, discontinuities, breath artifacts, repeated or skipped text, and edit points;
- sample rate, channels, codec, loudness, duration, and decode validity;
- time to first audio, real-time factor, streaming continuity, and cancellation behavior;
- listener understanding, comfort, accessibility, misleading identity, and disclosure.

Use ASR back-transcription, pronunciation dictionaries, acoustic metrics, and model judges only as diagnostic signals. Calibrate them with human listening for the exact language, voice, content, device, and risk. See [Generative Media](../generative-media/) for voice-cloning, rights, consent, provenance, and synthetic-media controls.

## Real-time voice agents

A real-time voice agent is an end-to-end interactive system, not an ASR score plus an LLM score plus a TTS score. Freeze the full pipeline:

```text
capture -> echo control -> VAD or end-of-turn -> streaming ASR -> reasoning and tools -> response text -> streaming TTS -> playback -> interruption
```

Record whether the provider supplies a unified speech-to-speech model, a managed cascaded agent, or separately selected components. Unified models may reduce latency and preserve paralinguistic context; cascaded systems may provide clearer transcripts, modular replacement, deterministic controls, and inspectable boundaries. Evaluate the actual system rather than assuming one architecture is universally superior.

### Measure the complete latency path

At minimum record:

- microphone or network capture buffering;
- transport and packetization delay;
- time to first partial transcript;
- partial stabilization and finalization delay;
- end-of-turn decision delay;
- reasoning, retrieval, tool, and safety-check time;
- time to first synthesized audio;
- playback buffering;
- user-perceived silence from end of speech to first agent audio;
- interruption-detection and audio-stop delay.

Report distributions and tail latency, not only an average. A fast ASR stage cannot compensate for slow endpointing, tool calls, TTS startup, or playback buffering.

### Evaluate turn-taking

Test:

- false endpointing while the user is pausing mid-sentence;
- late endpointing that creates dead air;
- backchannels, fillers, hesitation, and unfinished clauses;
- barge-in while the agent is speaking;
- overlapping user and agent audio;
- echo and recognition of the agent's own voice;
- explicit cancellation, correction, and topic change;
- network degradation, reconnect, duplicate messages, and reordered events;
- tool-call delay, failure, timeout, and confirmation;
- multilingual turns and language switches;
- handoff to a person or another agent.

The agent should not execute a consequential action from an unstable partial transcript. Define which intents require a final transcript, explicit confirmation, read-back, or human approval.

## Multilingual and code-switching evaluation

Evaluate every required language, locale, direction, and acoustic condition independently. Test:

- automatic language detection versus an explicitly supplied language;
- language changes between files, sessions, turns, and within one utterance;
- names, borrowed words, product terminology, abbreviations, and mixed scripts;
- punctuation, casing, transliteration, and normalization for each locale;
- TTS pronunciation when text contains another language or script;
- fallback behavior when a language is unsupported or confidence is low.

Do not infer Ukrainian quality from Russian, Polish, another Slavic language, or a provider-level multilingual claim. For Ukrainian, include native speakers, dialect and accent variation, inflection, proper names, numerals, abbreviations, code-switching, and current orthography. Require proficient native review before a production-quality claim.

## Report measurable outcomes

Pre-register the eligible unit: audio segment, utterance, minute, file, speaker turn, synthesized utterance, or conversation. Keep provider failures, no-output cases, policy blocks, abandoned calls, and failed retries in the denominator when they occur under deployed conditions.

| Outcome | Numerator / denominator |
| --- | --- |
| Terminal transcript acceptance | Eligible files or utterances meeting every declared semantic, formatting, timing, and review gate after permitted correction or escalation / all eligible files or utterances |
| Word or character error | Insertions + deletions + substitutions under the frozen normalization and tokenization policy / reference words or characters; report undefined and empty-reference cases separately |
| Critical-content accuracy | Correct applicable high-value names, numbers, commands, obligations, warnings, or domain terms / all applicable reference items |
| Hallucination rate | Eligible silence, music-only, or no-speech regions containing unsupported recognized speech / all eligible no-speech regions, with unsupported inserted duration or words also reported |
| Timestamp accuracy | Eligible words, boundaries, or segments within the declared tolerance / all eligible aligned units |
| Speaker-count accuracy | Eligible recordings with the accepted speaker count / all eligible diarized recordings |
| DER and speaker attribution | Missed speech + false alarm + speaker confusion duration / total reference speaker time under the declared collar and overlap policy; separately report correctly attributed transcript words / all eligible aligned transcript words |
| First-pass synthesis acceptance | Eligible TTS utterances accepted without regeneration, pronunciation repair, editing, or escalation / all eligible synthesized utterances |
| Speech intelligibility and pronunciation | Correctly understood or pronounced applicable units under the human-listening rubric / all applicable reviewed units |
| End-of-turn quality | Correct end-of-turn decisions within the accepted timing window / all eligible user turns; report false and late endpoints separately |
| Interruption success | Eligible barge-in events where playback stopped and the user turn was preserved within thresholds / all eligible barge-in events |
| Conversation task success | Eligible conversations satisfying every declared task and safety criterion / all eligible conversations |
| Latency | Capture-to-partial, capture-to-final, end-of-turn-to-first-audio, interruption-to-stop, and end-to-end terminal latency for every eligible event, with percentiles and failure groups |
| Cost per accepted result | Total model, service, transport, infrastructure, correction, review, and escalation cost / accepted terminal minutes, files, utterances, or conversations |

Reference transcripts and speaker annotations require a documented annotation policy, trained annotators for material work, disagreement handling, and adjudication. Do not compare WER, CER, DER, latency, or acceptance rates produced from different normalization, segmentation, collar, overlap, exclusion, or review policies as if they were equivalent.

## Candidate assignments

These candidates are starting points for evaluation, not quality rankings. Product facts below were rechecked against primary sources on 2026-07-25; verify current model IDs, endpoints, language coverage, launch stage, limits, terms, and pricing before deployment.

### OpenAI speech and realtime APIs

**Candidate role:** Hosted transcription, diarized transcription, TTS, and realtime voice interaction through separately selected API models.

OpenAI's current [model catalog](https://platform.openai.com/docs/models) lists `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize`, `gpt-4o-mini-tts`, audio models, and realtime models. The [Audio API](https://platform.openai.com/docs/api-reference/audio) exposes transcription and speech endpoints; current custom-voice creation requires a consent recording and is limited to eligible customers. Realtime interfaces have separate session, transport, voice, interruption, and event behavior.

Before evaluation:

- record the exact model ID or dated snapshot, endpoint, organization or project, region behavior, data controls, retention, moderation, and rate limits;
- evaluate ordinary transcription, diarized transcription, timestamps, prompts, streaming or realtime input, and speech translation as separate assignments;
- test every required language, codec, file length, speaker count, and acoustic condition;
- evaluate built-in and permitted custom voices separately, including pronunciation, disclosure, consent, and deletion;
- measure WebRTC or WebSocket transport, turn detection, interruption, tool calls, and full conversational latency;
- record current price and policy assumptions with their verification date.

Do not use ChatGPT product behavior as evidence for an API assignment. Do not infer that a realtime audio model exposes the same transcript, control, or audit properties as a cascaded ASR and TTS pipeline.

### Google Cloud Speech-to-Text and Text-to-Speech

**Candidate role:** Managed batch, streaming, multilingual, adaptation, and TTS workflows requiring Google Cloud project, location, IAM, storage, quota, and regional controls.

Google Cloud's current [Speech-to-Text documentation](https://docs.cloud.google.com/speech-to-text/docs) and [Cloud Text-to-Speech documentation](https://docs.cloud.google.com/text-to-speech/docs) expose multiple recognizers, models, voices, operations, regions, and launch stages. Streaming synthesis is currently documented for Chirp 3: HD voices; exact speech-recognition model, feature, region, and language support must be queried for the selected assignment.

Before evaluation:

- name the exact API version, recognizer or model, endpoint, project, location, region, storage path, and client-library version;
- verify batch, streaming, diarization, adaptation, language detection, timestamps, normalization, and quota support for the exact model and locale;
- verify TTS voice family, voice ID, streaming, SSML or control support, output format, region, and launch stage;
- record IAM, logging, retention, residency, and data boundary;
- measure actual language quality, latency, concurrency, quota, and cost rather than assuming provider-wide behavior.

Do not collapse legacy and current API versions, recognizers, Chirp generations, Gemini TTS, Chirp TTS, and other voice families into one unnamed Google candidate.

### Azure Speech

**Candidate role:** Managed real-time, fast, batch, custom, diarized, translated, synthesized, or live-voice workflow for Microsoft cloud and enterprise environments.

Microsoft's current [Azure Speech documentation](https://learn.microsoft.com/azure/ai-services/speech-service/) covers real-time, fast, and batch speech-to-text, diarization, custom speech, text-to-speech, and Voice Live. The current speech-to-text REST version, region, model, language, and feature support must be pinned because retired and preview versions differ.

Before evaluation:

- record the Speech resource, endpoint, region, API or SDK version, base or custom model, locale, and output format;
- evaluate real-time, fast, batch, diarized, translated, and custom speech routes separately;
- verify channel, duration, speaker-count, timestamp, language-identification, and data-retention constraints;
- evaluate each neural or custom TTS voice and Voice Live model separately;
- record storage, Entra or key authentication, private networking, logging, training-data, and deletion controls;
- test regional availability, quota, concurrency, latency, and price assumptions.

Do not assume a preview feature, retired REST version, one regional resource, or one locale represents Azure Speech generally.

### Deepgram speech and Voice Agent APIs

**Candidate role:** Hosted streaming or batch transcription, diarization, TTS, or managed voice-agent pipelines with explicit model-family and endpoint selection.

Deepgram's current documentation distinguishes [Nova and Flux speech-to-text assignments](https://developers.deepgram.com/docs/voice-agent-stt-models), versioned [speaker diarization](https://developers.deepgram.com/docs/diarization), Aura and Flux [TTS families](https://developers.deepgram.com/docs/voice-agent-tts-models), and a WebSocket [Voice Agent API](https://developers.deepgram.com/docs/voice-agent). Some Flux functionality is early access; Nova and other routes expose different formatting, terminology, language, and diarization features.

Before evaluation:

- pin the model family, model ID, version, endpoint and region, SDK, language settings, keyterms, diarizer version, and audio format;
- evaluate batch, conventional streaming, conversational end-of-turn, diarization, and managed-agent assignments separately;
- record launch stage and do not treat early-access behavior as stable or generally available;
- measure interim stability, endpointing, speaker labels, TTS first-byte latency, interruption, and full conversation behavior;
- verify retention, model-improvement settings, regional endpoint, self-hosted availability, quota, and current pricing.

### OpenAI Whisper open weights

**Candidate role:** Local or self-hosted multilingual transcription and speech-to-English translation baseline where offline control and MIT-licensed weights are useful.

The official [Whisper repository](https://github.com/openai/whisper) publishes code and model weights under MIT. Its current table lists multilingual models from `tiny` through `large` plus `turbo`, with approximate VRAM and relative-speed guidance. The repository states that `turbo` is an optimized `large-v3` transcription model and is not intended for speech translation; use an appropriate multilingual non-turbo model for translation evaluation.

Before evaluation:

- pin the repository release or commit, exact checkpoint, runtime, dependency versions, device, precision, quantization, decoding parameters, prompts, and audio preprocessing;
- test each required language and acoustic condition because performance varies materially by language, accent, noise, and domain;
- measure hallucinated text in silence or music, long-form repetition, timestamps, segmentation, and terminology errors;
- add and evaluate a separate diarization component when speaker labels are required;
- measure actual RAM, VRAM, load time, real-time factor, concurrency, and energy on the target device.

Do not treat third-party faster runtimes or quantizations as behaviorally identical to the official implementation without evaluation.

### pyannote Community-1 diarization

**Candidate role:** Local speaker-diarization component for batch recordings where offline operation, anonymous speaker labels, and separate ASR are acceptable.

The official [`pyannote/speaker-diarization-community-1`](https://huggingface.co/pyannote/speaker-diarization-community-1) model card identifies a CC-BY-4.0 pipeline that can run locally after accepting access conditions. It emits ordinary and exclusive diarization; the latter is intended to simplify reconciliation with transcription timestamps. The official [`pyannote.audio` repository](https://github.com/pyannote/pyannote-audio) documents local GPU use and versioned pipelines.

Before evaluation:

- pin the pipeline and internal model revisions, `pyannote.audio` version, runtime, device, and telemetry setting;
- record gating, attribution, license, download, caching, and offline-deployment requirements;
- test speaker count, overlap, short turns, similar voices, noisy audio, boundary accuracy, and ASR reconciliation;
- measure DER and transcript-word attribution under the frozen policy;
- do not treat anonymous labels as verified identities.

### NVIDIA Riva

**Candidate role:** GPU-accelerated self-hosted speech stack where streaming, offline, diarization, TTS, deployment control, and NVIDIA infrastructure justify the operational cost.

NVIDIA's current [Riva ASR documentation](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/public/asr/asr-overview.html) covers offline and streaming recognition, timestamps, confidences, language-model integration, and offline or streaming diarization with model-specific constraints. The [Riva TTS documentation](https://docs.nvidia.com/deeplearning/riva/user-guide/docs/tts/tts-overview.html) distinguishes streaming and offline synthesis.

Before evaluation:

- pin the Riva release, NGC artifacts, ASR and TTS models, diarizer, language packs, TensorRT or deployment configuration, GPU, container, and client protocol;
- verify which ASR models support the selected streaming diarizer and whether any feature is beta;
- measure GPU memory, startup, throughput, concurrency, partial and final latency, speaker attribution, TTS first audio, and failure recovery;
- record license, NGC access, infrastructure, scaling, observability, and maintenance costs;
- compare the complete self-hosted cost with hosted accepted-result cost, not raw inference speed alone.

## Choose local, hosted, or hybrid deployment

| Dimension | Local | Hosted | Hybrid |
| --- | --- | --- | --- |
| Privacy and residency | Can keep approved audio offline; still requires local access, logs, caches, backups, and deletion controls | Must satisfy provider processing, retention, region, support, and training-use terms | Classify and route audio explicitly; redaction after transcription does not protect already uploaded raw audio |
| Capability | Can combine exact ASR, diarizer, VAD, and TTS components | May provide current managed models, language features, scaling, and unified realtime APIs | Define which transcript, speaker, language, and latency properties change on fallback |
| Operations | Measure device support, RAM or VRAM, loading, realtime factor, concurrency, packaging, and updates | Measure upload, queue, network, quotas, rate limits, endpoint changes, and outages | Measure routing, duplicate processing, state transfer, and failure of either path |
| Cost | Include hardware occupancy, energy, storage, maintenance, review, and idle capacity | Include audio duration, requests, output characters or tokens, concurrency, storage, transfer, retries, and review | Include both stacks and routing overhead |
| Offline behavior | Can continue if all artifacts and dependencies are local | Requires connectivity unless a provider offers an edge or container route | Define queued, reduced-quality, local-only, and fail-closed modes |
| Fallback | Validate a smaller model, CPU path, alternate device, queue, or human transcription | Validate another endpoint, region, provider, queue, or human service | Test combined outages and return-to-primary behavior |

Compare total cost per accepted transcript minute, synthesized utterance, or completed conversation, not nominal per-minute price or isolated model throughput.

## Reliability, retry, and fallback

Give every production assignment a [reliability profile](../reliability-profiles/) that binds the complete deployment and evidence.

Define:

- bounded retry rules for transient upload, stream, timeout, decode, and provider errors;
- whether a low-confidence segment permits same-model decoding changes, a stronger ASR model, another provider, or human review;
- repeated hallucination, language, speaker, timestamp, or endpointing signatures that require rerouting rather than repetition;
- idempotency, stream sequence, duplicate event, reconnect, and partial-result replacement rules;
- separate acceptance gates for raw ASR, normalized transcript, diarization, TTS, and the complete conversation;
- fallback behavior for network loss, GPU loss, quota exhaustion, unsupported language, failed diarization, unavailable voice, or tool timeout;
- return-to-primary criteria and state reconciliation after recovery.

Never treat a successful API response as proof that the audio was fully processed. Verify expected duration, channels, transcript coverage, terminal job state, output decode, and artifact persistence.

## Safe-use boundaries

- Obtain and retain appropriate authorization before recording, transcribing, identifying, cloning, analyzing, or publishing speech. Consent and notice requirements vary by jurisdiction and context.
- Treat enrolled speaker recognition, voiceprints, and cross-session identity matching as biometric processing with stronger access, retention, security, false-match, and deletion controls.
- Do not infer protected, medical, emotional, demographic, credibility, intoxication, intent, or identity attributes from speech unless a separately validated and permitted high-risk process explicitly requires it.
- Consequential medical, legal, financial, employment, immigration, accessibility, emergency, and safety transcripts require qualified human control appropriate to the use.
- Do not silently add, remove, weaken, or strengthen warnings, permissions, obligations, numbers, names, deadlines, or commands.
- Minimize raw audio, transcripts, speaker embeddings, prompts, logs, and conversational context; separate secrets and credentials from model-visible content.
- Disclose synthetic speech where a reasonable listener could believe a real person spoke it, and apply the consent and provenance controls in [Generative Media](../generative-media/).
- Design voice agents to confirm consequential actions, respect interruption and cancellation, expose human handoff where required, and fail closed when the recognized intent is materially uncertain.
- Do not represent a transcript as verbatim, complete, speaker-verified, human-reviewed, certified, or production-approved unless the required process occurred and evidence is retained.

## Compact decision record

Use this record or equivalent structured data:

```text
Assignment ID:
Speech tasks and intended use:
Languages, locales, accents, code-switch patterns, domain, and speaker population:
Input devices, channels, codec, sample rate, transport, and acoustic conditions:
Transcript, diarization, timestamps, normalization, redaction, and output schema:
TTS voice, style, pronunciation, output format, disclosure, and consent:
Voice-agent transport, turn, interruption, tool, confirmation, and handoff rules:
Quality tier and risk:
Model, service, endpoint, region, artifact, and revision:
Runtime, hardware, quantization, prompts, vocabulary, parameters, SDK, and tools:
Privacy, retention, residency, biometric, license, consent, and permitted use:
Evaluation suite, references, eligible units, exclusions, and annotation policy:
ASR, critical-content, hallucination, timestamp, diarization, and speaker-attribution outcomes:
TTS intelligibility, pronunciation, quality, and latency outcomes:
Endpointing, interruption, task-success, tail-latency, and conversation outcomes:
Correction, review, retry, stop, escalation, degraded-operation, and fallback rules:
Cost per accepted minute, utterance, file, or conversation:
Evidence provenance and limitations:
Verified date and re-evaluation triggers:
```

The selection process, gates, workflow design, and record fields in this page are repository-authored operational guidance. They organize established speech-recognition, diarization, synthesis, conversational, evaluation, and safety practices and make no claim of novelty.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Generative Media](../generative-media/)
- [Perception and Evaluation](../perception-and-evaluation/)
- [Choosing Model Portfolios for Combined Workloads](../combined-workloads/)
- [Defining Model Reliability Profiles](../reliability-profiles/)
- [Models](../../../../../../../software/sub/models/)
- [Benchmarks](../../../../../benchmarks/)
- [Disclaimer](../../../../../../../disclaimer/)
