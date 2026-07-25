# Choosing Speech and Conversation Models and Workflows

Select an exact model, service, deployment, or smallest practical workflow for speech recognition, transcription, diarization, speech synthesis, or real-time voice interaction.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Guidance verified on 2026-07-25. Language coverage, endpoints, prices, latency, licenses, and provider data controls change; verify the complete assignment before adoption.

## Define the assignment

Separate:

- automatic speech recognition and plain transcription;
- timestamped or subtitle transcription;
- speaker diarization and transcript-to-speaker alignment;
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

[Whisper](../../../../../../../software/sub/models/sub/openai/sub/whisper/) is the current local ASR family candidate. Select and record an exact checkpoint and runtime; family-level claims do not establish target-language quality or hardware fit.

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

Use local Whisper, Community-1, and exact TTS artifacts when privacy, offline operation, or provider independence matters. Measure model load, peak VRAM and RAM, real-time factor, concurrency, storage, and failure recovery.

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
- [Combined Workloads](../combined-workloads/)
- [Reliability Profiles](../reliability-profiles/)
- [Models](../../../../../../../software/sub/models/)
- [General repository disclaimer](../../../../../../../disclaimer/)

## Sources

- [OpenAI Whisper repository](https://github.com/openai/whisper)
- [pyannote Community-1 model card](https://huggingface.co/pyannote/speaker-diarization-community-1)
- [pyannote.audio repository](https://github.com/pyannote/pyannote-audio)
