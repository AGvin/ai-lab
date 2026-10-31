# Documentation Requirements

## Requirements

- Identify PPLX Decider V1 27B as Perplexity AI's V1 release, derived from Qwen3.8-27B by decision-head replacement and supervised adaptation.
- Preserve the original Qwen/Qwen3.8-27B base-model attribution; this model is a Perplexity post-trained derivative, not a newly trained Qwen checkpoint.
- Preserve the typed decision outputs and calibrated probabilities; license and availability must follow the exact official model card and revision.
- Treat exact benchmark/index scoring, accuracy, access/visibility, package file sizes, licensing, hardware memory, calibration and compatible runtimes as mutable source-backed facts. Do not equate a class name inside checkpoint code with its training lineage.
- Keep the local PPLX 27B Portable Computer model, Perplexity Decisions API endpoint and provider service terms outside this trained-model identity.

## Validation

- The checkpoint ID matches the first-party model card.
- Its `member-of` relation is reciprocated by the PPLX Decider family `has-member` entry.
- Model revision-specific inference and calibration behavior are not conflated with another version.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Decider V1 27B is Perplexity's Qwen3.8-27B-derived decision checkpoint. Its published card declares Apache-2.0 and provides a download/inference example for typed choices and calibrated probabilities.
- Decision and deployment boundary: Review and pin the inference code, exact weights and dependencies. The card describes a CUDA setup with substantial memory needs; evaluate the real workload before choosing hardware. Reported benchmark results use Perplexity API evaluation and are not an independent local reproduction.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-decider-v1-27b>.
