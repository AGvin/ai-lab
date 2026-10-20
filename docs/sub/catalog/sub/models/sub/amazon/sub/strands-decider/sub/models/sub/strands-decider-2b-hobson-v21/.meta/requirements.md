# Documentation Requirements

## Requirements

- Identify this exact released 2B-class Hobson V21 Strands Decider checkpoint under the official StrandsAgents Hugging Face distribution, distinct from earlier V19 checkpoint and from the Strands Decider inference package.
- Preserve the base model and checkpoint-specific weight/adaptor format, calibration, source license, tokenizer, deployment methods and evaluation recipe only as documented by the exact first-party model card.
- Its primary application is typed option choice, confidence/rating and lightweight local decision steps inside agents rather than conversational free-form generation.
- Treat advertised local milliseconds, CUDA/MPS/CPU/MLX support and agent integration as runtime/model/version-specific, not universal guaranteed performance.
- Do not equate vendor-calibrated probabilities with certainty, a validated safety decision, or the absence of wrong answers.

## Validation

- Exact model artifact exists and remains separately identifiable.
- `member-of` reciprocates the Strands Decider family `has-member` relation.
- Product and model-service compatibility statements have current primary-source evidence.

## Decision and operational boundaries

- Preserve this canonical boundary: Concrete Hobson V21 checkpoint with a Qwen3.5-2B-Base LoRA adapter and option-scoring head; it is not the later Qwen v1 recipe. Confidence calibration was fitted on held-out short tasks and needs evaluation on the target workflow. Optional Qwen vision was not trained on images, and missing image inputs can still yield confident wrong answers. The recorded base revision was inferred rather than pinned during training. Pin artifacts and runtime separately; the local server has no authentication. Runtime state is truncated by default; strict-window mode rejects oversize input.
- The card identifies a LoRA adapter on `Qwen/Qwen3.5-2B-Base` and a decision head. V21 adds question paraphrases and teacher distillation to the earlier recipe; the published seed is representative rather than a demonstrated universal winner. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
- Calibration on short held-out tasks does not establish reliable thresholds for new question wording, rubrics or long multi-step decisions. Measure those thresholds on the application traffic. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
- Optional vision preserves the base vision tower without image training. Validate that required images are present before asking a visual question; high confidence does not detect a missing image. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
- The provenance record says the training base revision was inferred. Pin the downloadable artifacts and code, preserve that provenance limit, and configure truncation or strict-window rejection deliberately. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- The model card publishes the adapter/head under Apache-2.0 and loads the base weights separately. Preserve source-specific data terms and pin the released files and compatible code; a model license does not grant a blanket training-data redistribution right. [Strands Decider 2B Hobson V21 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v21)
