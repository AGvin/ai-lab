# Documentation Requirements

## Requirements

- Teach Speech Recognition as converting spoken audio into text while distinguishing it from translation, diarization, language identification, summarization, and downstream text processing.
- Use meeting/interview transcription, voice commands, subtitles, recording search, summarization preparation, and accessibility as application examples rather than task-definition requirements.
- When consequential accuracy matters and source audio is available, retain an appropriate source long enough to verify uncertain transcript segments under applicable privacy, consent, retention, and access rules.
- Review names, numbers, dates, rare or domain-specific terms, and consequential statements instead of assuming fluent-looking text is source-faithful.
- Surface uncertain or low-confidence regions for review when the workflow can use that signal; keep domain vocabulary/prompting controls model/runtime specific.
- Do not treat automatically generated transcripts as verbatim legal or factual records solely because they are readable.

## Validation

- Downstream summarization or decisions do not silently outrun unresolved critical transcription errors.
- Model-specific vocabulary/prompt controls are not presented as universal recognizer semantics.
- Transcript verification remains linked to the original evidence when the workflow requires it.
