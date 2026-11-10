# omni-moderation

omni-moderation is OpenAI’s model for harmful-content classification over text and images. `omni-moderation-latest` is its mutable alias and `omni-moderation-2024-09-26` is a documented pinned snapshot.

## Profile

The model returns moderation flags, categories, and category scores. Its supported inputs do not include audio [Model reference](https://developers.openai.com/api/docs/models/omni-moderation-latest).

## Operating boundaries

Categories have different input-type coverage. Use category_applied_input_types when interpreting results: an unsupported category can return zero for image-only input, which is not a finding that the content is safe for that category [Moderation guide](https://developers.openai.com/api/docs/guides/moderation).

Scores and custom thresholds may need recalibration after model updates. The application defines enforcement, escalation, and review; a model score is not a complete safety policy [Moderation guide](https://developers.openai.com/api/docs/guides/moderation).

## Relations

- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [omni-moderation-latest model reference](https://developers.openai.com/api/docs/models/omni-moderation-latest).
- [Moderation guide](https://developers.openai.com/api/docs/guides/moderation).
