# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-vision-3.3-2b` and its Apache-2.0 weight license.
- Describe English instruction plus image input and document-oriented image-to-text output. Newer Vision 4.1 exists; do not present this generator as the current general successor.
- Segmentation, doctags and multipage behavior are experimental. Inspect extraction correctness and hallucinations on representative documents.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
