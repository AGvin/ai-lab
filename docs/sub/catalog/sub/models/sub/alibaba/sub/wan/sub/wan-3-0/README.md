# Wan 3.0

Wan 3.0 is the released hosted all-in-one video generation line containing standard Video and accelerated Video-Prime identities.

## Decision and Operational Boundaries

- The HTTP video API is asynchronous: create a task and poll for its result; successful submission is not a completed output.
- Use exact task-mode material combinations and limits; do not treat multimodal input support as permission to mix every reference type in one request.
- Keep Prime as the named video-model variant rather than conflating it with the general Model Studio Prime inference mode.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Wan](../../) |
| Produced by | [Wan Team](../../../../../../../producers/sub/w/sub/wan-team/) |
| Includes | [Wan3.0-Video](./sub/models/sub/wan3-0-video/) |
| Includes | [Wan3.0-Video-Prime](./sub/models/sub/wan3-0-video-prime/) |

## Primary Sources

- [Alibaba Cloud: wan3 video generation guide](https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-guide)
- [Alibaba Cloud: wan3 video generation api reference](https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-api-reference)
- [Alibaba Cloud: wan3 0 video prime](https://www.alibabacloud.com/help/en/model-studio/wan3-0-video-prime)
- [Alibaba Cloud: wan3 0 at general availability capabilities benchmarks pricing and the workflows it changes_603505](https://www.alibabacloud.com/blog/wan3-0-at-general-availability-capabilities-benchmarks-pricing-and-the-workflows-it-changes_603505)
