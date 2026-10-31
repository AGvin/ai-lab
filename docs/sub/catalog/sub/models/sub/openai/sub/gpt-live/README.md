# GPT-Live

GPT-Live is OpenAI’s family of full-duplex voice models. It can listen and speak continuously, while supported applications delegate reasoning and actions to a backend model.

## Profile

The July 2026 system card identifies GPT-Live-1 and GPT-Live-1 mini. Results involving delegation depend on the backend model and evaluation harness [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).

## Operating boundaries

GPT-Live-1 became generally available in the API in September 2026. That release does not establish the same API availability for GPT-Live-1 mini [API changelog](https://developers.openai.com/api/docs/changelog).

Session transport, duration billing, backend selection, and concurrent-session limits belong to the service. Backend tool execution requires application authorization and server-held credentials [GPT-Live guide](https://developers.openai.com/api/docs/guides/live).

## Child pages

- [Models](sub/models/README.md).

## Relations

- Member: [GPT-Live-1](sub/models/sub/gpt-live-1/README.md).
- Member: [GPT-Live-1 mini](sub/models/sub/gpt-live-1-mini/README.md).
- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [GPT-Live system card](https://deploymentsafety.openai.com/gpt-live).
- [GPT-Live API guide](https://developers.openai.com/api/docs/guides/live).
- [API changelog](https://developers.openai.com/api/docs/changelog).
- [Voice server controls](https://developers.openai.com/api/docs/guides/voice-server-controls).
