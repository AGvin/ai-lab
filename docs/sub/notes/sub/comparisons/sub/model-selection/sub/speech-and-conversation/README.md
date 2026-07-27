# Choosing Speech and Conversation Models and Workflows

Select the smallest practical speech workflow that reaches the required transcription, speaker, synthesis, latency, privacy, and rights target for batch or real-time use.

## Translations

- English
- [Українська](./l10n/uk_UA/)

**Status:** Specialist and compact multimodal speech routes updated on 2026-07-27. Language coverage, endpoints, prices, latency, licenses, and provider data controls change; verify the complete assignment before adoption.

## Quick picks

| Need | Start with | AI or model type | Language-model scale where applicable | Route | Main reason |
| --- | --- | --- | --- | --- | --- |
| Private local transcription | [Whisper](../../../../../../../software/sub/models/sub/openai/sub/whisper/) with an exact checkpoint and runtime | Speech recognition model | Not applicable | Local or self-hosted | Mature open ASR family, offline operation, and reproducible local processing |
| Compact short-audio understanding or translation experiment | [Gemma 4 E2B](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e2b-instruct/) or [E4B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e4b-instruct/) | Multimodal general-purpose instruct model | SLM | Local or self-hosted | Combines short audio, text, image, multilingual reasoning, and official compact local artifacts |
| Local speaker diarization | [pyannote Community-1](../../../../../../../software/sub/models/sub/pyannote/sub/speaker-diarization/sub/community-1/) | Speaker diarization model | Not applicable | Local or self-hosted | Purpose-built speaker segmentation and local control over recordings |
| Managed batch transcription | Approved hosted speech endpoint | Speech recognition service | Not applicable | Hosted | Fast adoption, scaling, language support, timestamps, and provider-managed operations |
| Low-latency voice assistant | Streaming ASR, fast reasoning model, streaming TTS, and explicit interruption control | Multi-component voice workflow | Not applicable | Hosted or hybrid | End-to-end latency depends on the complete turn, not one component |
| Sensitive conversational workflow | Local ASR and diarization, approved reasoning route, and rights-cleared TTS | Hybrid speech workflow | Not applicable | Local, self-hosted, or hybrid | Keeps raw audio local while allowing controlled escalation of sanitized text |

These are starting routes, not universal rankings. The exact checkpoint, language, recording conditions, voice, streaming configuration, and data path are part of the evaluated assignment.

## Economical specialist and compact candidates

Speech selection is usually specialist-first rather than language-model-scale-first. ASR, diarization, TTS, short-audio multimodal understanding, and conversational reasoning are distinct roles.

| Candidate | Model type | Language-model scale where applicable | Access | Best fit | Main limitation | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| [Whisper](../../../../../../../software/sub/models/sub/openai/sub/whisper/) exact checkpoint | Automatic speech recognition model | Not applicable | Open-source model family | Private transcription, subtitles, multilingual ASR, and local batch processing | Family-level claims do not establish language quality, speed, memory, or timestamp behavior for a specific checkpoint and runtime | [Official repository](https://github.com/openai/whisper) |
| [Gemma 4 E2B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e2b-instruct/) | Multimodal general-purpose instruct model with audio input | SLM; 2.3B effective, 5.1B including embeddings | Open-weight; Apache-2.0 | Short private audio transcription or translation experiments combined with text, image, or reasoning context | Audio input is limited to short clips; not a dedicated long-form, streaming, timestamped, or diarization system | [Official model card](https://ai.google.dev/gemma/docs/core/model_card_4) · [Hugging Face](https://huggingface.co/google/gemma-4-E2B-it) |
| [Gemma 4 E4B Instruct](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/sub/e4b-instruct/) | Multimodal general-purpose instruct model with audio input | SLM; 4.5B effective, 8B including embeddings | Open-weight; Apache-2.0 | Stronger compact short-audio understanding, transcription, speech translation, and multimodal follow-up experiments | Stored model and multimodal components exceed the effective count; still lacks dedicated streaming, timestamp, and diarization guarantees | [Official model card](https://ai.google.dev/gemma/docs/core/model_card_4) · [Hugging Face](https://huggingface.co/google/gemma-4-E4B-it) |
| [pyannote Community-1](../../../../../../../software/sub/models/sub/pyannote/sub/speaker-diarization/sub/community-1/) | Speaker diarization model | Not applicable | Gated local model | Speaker segmentation and transcript alignment | Does not transcribe or establish real-world identity; access, license, dependencies, overlap, and correction effort require review | [Model card](https://huggingface.co/pyannote/speaker-diarization-community-1) |

Do not force one scale table across incompatible speech roles. Use SLM or checkpoint size only within comparable model classes and only when it improves the actual selection decision.

## Broader route comparison

| Route | Component type | Best fit | Main limitation | Evidence to recheck |
| --- | --- | --- | --- | --- |
| Local Whisper pipeline | ASR model plus runtime | Offline, private, reproducible transcription and subtitles | Hardware, checkpoint, runtime, language, timestamps, and long-recording behavior vary | Exact checkpoint, runtime, precision, language, real-time factor, memory, and error profile |
| Gemma 4 E2B or E4B short-audio route | Compact multimodal general-purpose model | Bounded audio clips that need transcription or translation plus text, image, document, or reasoning context | Short clip limit and no dedicated streaming, timestamps, diarization, or long-recording contract | Exact artifact, runtime audio support, clip duration, language, formatting, memory, and word-error evidence |
| Hosted ASR endpoint | Managed speech recognition service | Fast integration, elastic throughput, streaming, timestamps, and provider features | Mutable pricing, quotas, region, retention, language support, and vendor dependency | Exact model ID, language, timestamps, diarization, streaming, region, data terms, quota, and current price |
| Local pyannote pipeline | Speaker diarization model | Private speaker segmentation, overlap analysis, and transcript alignment | Gated access, specialist dependencies, speaker-count assumptions, and correction effort | Exact checkpoint, license, dependencies, long-recording behavior, overlap, and DER evidence |
| Hosted TTS endpoint | Managed speech synthesis service | Broad voice catalog, streaming, low setup cost, and production scaling | Voice rights, retention, region, mutable price, and provider availability | Exact voice and model, language, first-audio latency, streaming, license, permitted use, and price |
| Local TTS artifact | Speech synthesis model | Offline or private synthesis, provider independence, and controlled deployment | Voice quality, language support, hardware, license, and operational burden vary widely | Exact artifact, runtime, voice rights, language, latency, memory, quality, and maintenance status |
| Real-time voice stack | VAD, ASR, reasoning, tools, TTS, and interruption control | Interactive assistants and live workflows | Tail latency, turn detection, cancellation, duplicated responses, and tool delays compound | Complete p50/p95/p99 latency, failure modes, data route, concurrency, and accepted-turn quality |

## Workload view

| Workload | Prefer | Escalate or reject when |
| --- | --- | --- |
| Plain batch transcription | Exact local Whisper checkpoint or approved hosted ASR | Language, omissions, names, numbers, long recordings, or throughput miss the target |
| Short multimodal audio clip | Gemma 4 E2B or E4B for bounded experiments | Clip length, streaming, timestamps, speaker attribution, word accuracy, or latency exceeds the compact route's evidence |
| Subtitle transcription | ASR route with validated segment boundaries and timestamps | Reading speed, line length, timing, omissions, or synchronization fail |
| Speaker diarization | pyannote Community-1 or another exact diarization model | Overlap, short turns, speaker count, long recordings, or ASR alignment are unreliable |
| Batch TTS | Approved hosted or exact local TTS artifact | Pronunciation, consistency, rights, long-form continuity, or correction effort are unacceptable |
| Streaming TTS | Streaming endpoint or measured local artifact | First-audio latency, cancellation, jitter, or concurrency misses the target |
| Real-time voice agent | Separately validated VAD, ASR, reasoning, tools, and TTS components | End-to-end tail latency, interruption, tool delay, privacy, or recovery cannot meet requirements |
| Multilingual or code-switched speech | Route evaluated for every language, accent, and switch pattern | Language identification, mixed segments, terminology, or fallback behavior is unreliable |
| Confidential or regulated recordings | Local or explicitly approved contracted route | Complete retention, transfer, consent, access, and deletion controls are not proven |

## Define the assignment

Separate:

- automatic speech recognition and plain transcription;
- timestamped or subtitle transcription;
- speaker diarization and transcript-to-speaker alignment;
- short-audio multimodal understanding or speech translation;
- speaker identification only where separately authorized;
- batch text-to-speech;
- streaming speech synthesis;
- real-time voice-agent interaction;
- multilingual or code-switched speech;
- offline, private, or regulated recordings.

Record exact model or checkpoint, endpoint, region, runtime, hardware, precision, language, channel, codec, sample rate, speaker count assumptions, terminology, timestamps, segmentation, streaming settings, voice, latency target, privacy, retention, consent, quality tier, and verification date.

Do not transfer results between checkpoints, runtimes, languages, accents, audio channels, recording conditions, voices, or hosted and local deployments.

## Quality gates

| Tier | Minimum gate |
| --- | --- |
| Exploration | Rough transcript or synthetic sample for feasibility; not authoritative |
| Concept draft | Useful for discussion with visible uncertainty and manual correction |
| Working result | Declared accuracy, timing, speaker, audio, and latency thresholds met |
| Production quality | Independent review, privacy controls, complete workflow validation, and documented limitations |
| Exceptional quality | Additional domain adaptation, editorial correction, voice direction, and specialist review |

## ASR and transcription

Evaluate:

- word or character error rate on the target language and domain;
- omissions, unsupported insertions, repetitions, and silence handling;
- names, numbers, terminology, punctuation, casing, and formatting;
- segment boundaries, timestamps, subtitle constraints, and long-recording stability;
- accents, dialects, noise, music, overlapping speech, telephony, and channel variation;
- real-time factor, peak memory, queueing, concurrency, and cost per accepted minute or hour.

Freeze a representative audio suite and reference policy. Report no-output and failed-provider cases rather than silently rerunning them away.

[Whisper](../../../../../../../software/sub/models/sub/openai/sub/whisper/) is the current local dedicated ASR family candidate. Select and record an exact checkpoint and runtime; family-level claims do not establish target-language quality or hardware fit.

Gemma 4 E2B and E4B are separate compact multimodal candidates for bounded short-audio workflows. They must not inherit Whisper's long-form, timestamp, subtitle, or ecosystem assumptions.

## Speaker diarization

Diarization answers who spoke when within a recording. It does not produce the transcript and does not establish real-world identity by itself.

Evaluate diarization error rate, overlap, short turns, speaker-count assumptions, segment stability, long recordings, alignment with the exact ASR output, runtime, memory, and correction effort.

[pyannote Community-1](../../../../../../../software/sub/models/sub/pyannote/sub/speaker-diarization/sub/community-1/) is the current local candidate. Verify gated access, license, dependencies, and data controls before adoption.

Use neutral labels such as `SPEAKER_00` unless a separate authorized identity process exists.

## Speech synthesis

Evaluate:

- intelligibility and pronunciation;
- language, accent, terminology, numbers, abbreviations, and names;
- naturalness, prosody, pace, emotion, and style control;
- speaker consistency and long-form continuity;
- clipping, noise, breaths, silence, loudness, and output format;
- first-audio latency, streaming stability, cancellation, and total synthesis time;
- voice license, permitted use, consent, retention, and disclosure.

A pleasant sample does not prove consistent production behavior across long text, rare words, or real-time load.

## Real-time voice agents

Measure the complete turn:

1. voice activity detection and end-of-turn detection;
2. network and input buffering;
3. partial and final ASR;
4. model reasoning and tool calls;
5. TTS first audio and streaming;
6. interruption, barge-in, cancellation, and recovery.

Report p50, p95, and p99 end-to-end latency plus false starts, cutoffs, interruptions, duplicated responses, missed turns, and tool-call delays.

A fast ASR or TTS component does not guarantee a fast conversation. Keep long reasoning, cold model loads, and slow tools outside the critical path where possible.

## Multilingual and Ukrainian evaluation

Evaluate every language, direction, accent, and code-switch pattern separately. Test language identification, mixed-language segments, transliterated names, terminology, punctuation, and fallback behavior.

For Ukrainian, include regional and speaker variation, technical terminology, names, numerals, dates, abbreviations, code-switching, grammatical normalization, and natural TTS stress and pronunciation. Use proficient native reviewers for production claims.

## Local, hosted, and hybrid routes

### Local

Use local Whisper, Gemma 4 E2B or E4B, Community-1, and exact TTS artifacts when privacy, offline operation, or provider independence matters. Measure model load, required encoders or projections, peak VRAM and RAM, real-time factor, concurrency, storage, and failure recovery.

### Hosted

Evaluate exact current speech endpoints from approved providers only after checking model ID, language and voice support, region, retention, training use, price unit, streaming, timestamp, diarization, and quota behavior.

### Hybrid

A practical route may keep ASR and diarization local, send only approved transcript text to a hosted reasoning model, and use local or hosted TTS according to latency, voice rights, and privacy. Classification and sanitization must be deterministic and verified.

## Privacy, identity, and safety

Audio can contain personal, confidential, biometric, and bystander data. Record lawful basis, consent, collection purpose, storage, retention, access, transfer, and deletion rules.

Voice cloning or identity-conditioned synthesis requires explicit authorization and purpose limits. Do not use generated voices for deception, authentication bypass, impersonation, or implied endorsement.

Do not confuse speaker diarization with speaker identification or authentication.

## Retry, fallback, and degraded operation

Retry transient transport, timeout, or recoverable decoding failures. Escalate repeated language, quality, latency, overlap, terminology, voice, or capability failures to a different assignment.

A fallback must pass the same language, privacy, quality, latency, output, and rights gates. During provider or network failure, continue only local modes that were explicitly validated and label unavailable capabilities honestly.

## Outcome record

```text
Assignment, language, channel, domain, quality tier, and risk:
Exact ASR, diarization, reasoning, and TTS models or endpoints:
Runtime, hardware, region, codecs, sample rates, and streaming settings:
Terminology, speaker-count assumptions, voice, consent, privacy, and retention:
Evaluation audio, references, reviewers, and eligibility rules:
Error, timing, speaker, audio-quality, latency, throughput, and cost outcomes:
Retry, stop, escalation, fallback, degraded-operation, and deletion rules:
Evidence, limitations, verified date, and re-evaluation triggers:
```

## Related pages

- [AI Model Selection and Team Design](../..)
- [Generative Media](../generative-media/)
- [Perception and Evaluation](../perception-and-evaluation/)
- [Translation and Localization](../translation-and-localization/)
- [Combined Workloads](../combined-workloads/)
- [Reliability Profiles](../reliability-profiles/)
- [Gemma 4](../../../../../../../software/sub/models/sub/google/sub/gemma/sub/gemma-4/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)

## Sources

- [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)
- [Gemma 4 E2B Instruct](https://huggingface.co/google/gemma-4-E2B-it)
- [Gemma 4 E4B Instruct](https://huggingface.co/google/gemma-4-E4B-it)
- [OpenAI Whisper repository](https://github.com/openai/whisper)
- [pyannote Community-1 model card](https://huggingface.co/pyannote/speaker-diarization-community-1)
- [pyannote.audio repository](https://github.com/pyannote/pyannote-audio)
