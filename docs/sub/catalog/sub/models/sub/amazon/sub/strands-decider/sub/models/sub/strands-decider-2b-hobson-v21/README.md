# Strands Decider 2B Hobson V21

Strands Decider 2B Hobson V21 is a published trained adapter and decision head on Qwen/Qwen3.5-2B-Base.

## Scope and boundaries

Concrete Hobson V21 checkpoint with a Qwen3.5-2B-Base LoRA adapter and option-scoring head; it is not the later Qwen v1 recipe. Confidence calibration was fitted on held-out short tasks and needs evaluation on the target workflow. Optional Qwen vision was not trained on images, and missing image inputs can still yield confident wrong answers. The recorded base revision was inferred rather than pinned during training. Pin artifacts and runtime separately; the local server has no authentication. Runtime state is truncated by default; strict-window mode rejects oversize input.

## Decision and operational boundaries

- The card identifies a LoRA adapter on `Qwen/Qwen3.5-2B-Base` and a decision head. V21 adds question paraphrases and teacher distillation to the earlier recipe; the published seed is representative rather than a demonstrated universal winner. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
- Calibration on short held-out tasks does not establish reliable thresholds for new question wording, rubrics or long multi-step decisions. Measure those thresholds on the application traffic. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
- Optional vision preserves the base vision tower without image training. Validate that required images are present before asking a visual question; high confidence does not detect a missing image. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
- The provenance record says the training base revision was inferred. Pin the downloadable artifacts and code, preserve that provenance limit, and configure truncation or strict-window rejection deliberately. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- The model card publishes the adapter/head under Apache-2.0 and loads the base weights separately. Preserve source-specific data terms and pin the released files and compatible code; a model license does not grant a blanket training-data redistribution right. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)

## Relations

- member-of: [`catalog/models/amazon/strands-decider`](../../../../)

## Official resources

- <https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21>
- <https://github.com/strands-labs/strands-decider>
- <https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-september-2026/>
- <https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md>
