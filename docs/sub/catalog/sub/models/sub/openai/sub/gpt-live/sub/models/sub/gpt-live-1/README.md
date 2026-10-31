# GPT-Live-1

GPT-Live-1 is OpenAI’s released full-duplex voice model. The API identifier is `gpt-live-1`; the service supports ongoing listening and speaking and delegation to a backend model.

## Profile

The API profile lists text and audio input/output, a July 31, 2025 knowledge cutoff, and no native image or video support [Model reference](https://developers.openai.com/api/docs/models/gpt-live-1).

## Operating boundaries

The API release became generally available on September 10, 2026. Backend inference is separate from the voice session, and access and capacity are determined by the service [API changelog](https://developers.openai.com/api/docs/changelog).

Keep credentials, business rules, and action authorization on the server. A delegated action or sideband connection does not itself authorize execution [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).

## Relations

- Member of: [GPT-Live](../../../../README.md).

## Official resources

- [gpt-live-1 model reference](https://developers.openai.com/api/docs/models/gpt-live-1).
- [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).
- [GPT-Live API guide](https://developers.openai.com/api/docs/guides/live).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
