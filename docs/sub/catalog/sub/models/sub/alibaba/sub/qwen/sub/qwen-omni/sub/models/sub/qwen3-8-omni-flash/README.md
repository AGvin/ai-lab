# Qwen3.8-Omni-Flash

qwen3.8-omni-flash accepts text, images, audio, and video but returns text, with a current one-million-token context.

## Decision and Operational Boundaries

- Keep speech output on the separate Realtime model; do not inherit a speech-generation contract from older Omni releases.
- Custom tools, optional web search, thinking, caching, and multichannel audio require their documented request options and region support.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Treat audio transcripts, OCR, and tool results as untrusted application input.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen Omni](../../../../) |

## Primary Sources

- [Alibaba Cloud: qwen3 8 omni flash](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-omni-flash)
- [Alibaba Cloud: qwen omni](https://www.alibabacloud.com/help/en/model-studio/qwen-omni)
