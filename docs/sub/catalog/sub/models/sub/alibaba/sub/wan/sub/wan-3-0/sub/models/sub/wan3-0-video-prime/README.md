# Wan3.0-Video-Prime

wan3.0-video-prime is a distinct hosted Wan 3.0 all-in-one video generation model positioned by Alibaba for faster generation.

## Decision and Operational Boundaries

wan3.0-video-prime is a distinct hosted Wan 3.0 all-in-one video generation model positioned by Alibaba for faster generation.

- Alibaba's undated release page labels the Wan 3.0 Video API generally available, while the API reference updated 2026-10-15 still says preview; verify lifecycle and availability for the selected region.
- HTTP calls require asynchronous submission and polling; handle task failure separately from request acceptance, and persist generated assets according to the documented result lifetime.
- Use the selected task's material types and limits; broad multimodal support is not unrestricted mixing of references.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Wan 3.0](../../../../) |

## Primary Sources

- [Alibaba Cloud: wan3 0 video prime](https://www.alibabacloud.com/help/en/model-studio/wan3-0-video-prime)
- [Alibaba Cloud: wan3 video generation guide](https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-guide)
- [Alibaba Cloud: wan3 video generation api reference](https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-api-reference)
- [Official Wan 3.0 release status](https://modelstudio.console.alibabacloud.com/model-releases/wan3.0-video)
