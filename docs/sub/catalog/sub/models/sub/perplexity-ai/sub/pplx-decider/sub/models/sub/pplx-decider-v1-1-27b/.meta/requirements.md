# Documentation Requirements

## Requirements

- Identify PPLX Decider V1.1 27B as Perplexity AI's the distinct updated October 6, 2026 decision checkpoint with noncausal full-attention mode and expanded decision training data.
- Preserve the original Qwen/Qwen3.8-27B base-model attribution; this model is a Perplexity post-trained derivative, not a newly trained Qwen checkpoint.
- The official model card requires the saved noncausal attention behavior and application of calibration temperature exactly once for comparable inference. It states authenticated Hugging Face access for inference; re-check repo accessibility and weights before claiming open anonymous download.
- Treat exact benchmark/index scoring, accuracy, access/visibility, package file sizes, licensing, hardware memory, calibration and compatible runtimes as mutable source-backed facts. Do not equate a class name inside checkpoint code with its training lineage.
- Keep the local PPLX 27B Portable Computer model, Perplexity Decisions API endpoint and provider service terms outside this trained-model identity.

## Validation

- The checkpoint ID matches the first-party model card.
- Its `member-of` relation is reciprocated by the PPLX Decider family `has-member` entry.
- Model revision-specific inference and calibration behavior are not conflated with another version.
