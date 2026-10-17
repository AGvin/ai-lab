# Documentation Requirements

## Requirements

- Identify PPLX Decider V1 27B as Perplexity AI's first openly distributed October 2026 release, derived from Qwen3.8-27B by decision-head replacement and supervised adaptation.
- Preserve the original Qwen/Qwen3.8-27B base-model attribution; this model is a Perplexity post-trained derivative, not a newly trained Qwen checkpoint.
- Preserve the distinct 255-option decision head and calibrated-probability output; license and availability must follow the exact official model card and revision.
- Treat exact benchmark/index scoring, accuracy, access/visibility, package file sizes, licensing, hardware memory, calibration and compatible runtimes as mutable source-backed facts. Do not equate a class name inside checkpoint code with its training lineage.
- Keep the local PPLX 27B Portable Computer model, Perplexity Decisions API endpoint and provider service terms outside this trained-model identity.

## Validation

- The checkpoint ID matches the first-party model card.
- Its `member-of` relation is reciprocated by the PPLX Decider family `has-member` entry.
- Model revision-specific inference and calibration behavior are not conflated with another version.
