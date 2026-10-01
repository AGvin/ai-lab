# Documentation Requirements

## Requirements

- Identify GPT-Realtime-Translate as OpenAI's dedicated streaming speech-to-speech translation model.
- Preserve its current interpreter boundary: live audio input, translated audio plus transcript output, dedicated realtime translation endpoint, and no generic assistant/tool-calling role.
- Keep supported source/target languages, latency, duration pricing, endpoint/transport behavior, context/output limits, rate limits, and transcript-event semantics freshness-sensitive.
- Keep it distinct from GPT-Realtime-2.1 voice-agent models and transcription-only models.

## Validation

- Translation is the primary trained-model job, not a generic Realtime API feature.
- Mutable service behavior remains source-scoped.
