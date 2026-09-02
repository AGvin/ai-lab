# Speech-to-Text

Legacy residual retained for practical transcription workflows, verification, retention, and privacy guidance that is intentionally outside the canonical Speech-to-Text concept owner.

> **Migration note:** STT/ASR task identity, architecture neutrality, distinctions from translation/diarization/language ID and other audio tasks, optional timestamp/confidence outputs, deployment-mode boundaries, recognition error factors, normalization caveats, and the fact that transcripts are not guaranteed verbatim ground truth are already preserved in `docs/sub/concepts/sub/modalities/sub/audio-and-speech/sub/speech-to-text/`. The remaining material below stays here until its exact learning, workflow, governance/privacy, evaluation, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Application residual

Speech-to-text can support workflows such as:

- meeting and interview transcription;
- voice interfaces and commands;
- subtitle generation;
- search and summarization of recordings;
- accessibility workflows.

These are application examples rather than part of the canonical STT definition.

## Verification and governance residual

When the original audio is available and consequential accuracy matters, preserve or retain an appropriate source recording long enough to verify uncertain transcript segments under the applicable privacy, consent, retention, and access rules. Review names, numbers, dates, rare/domain terms, and consequential statements rather than assuming fluent-looking text is source-faithful.

Domain vocabulary or prompting can help where a concrete recognizer supports it, but such controls are model/runtime specific. Low-confidence or otherwise uncertain sections should be surfaced for review when the workflow can act on that uncertainty.

Do not treat an automatically generated transcript as a verbatim legal record merely because it is readable, and avoid summarizing or making downstream decisions from critical passages before relevant transcription errors have been resolved.

These operational, verification, retention, and privacy practices remain migration source material until their exact learning, governance/privacy, evaluation, workflow, or decision-support owners are verified.
