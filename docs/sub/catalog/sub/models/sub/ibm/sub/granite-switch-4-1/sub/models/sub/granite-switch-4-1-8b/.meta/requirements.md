# Documentation Requirements

## Identity and decision boundaries

- Identify the exact upstream checkpoint `https://huggingface.co/ibm-granite/granite-switch-4.1-8b` and its Apache-2.0 weight license.
- Preserve the selected 8B/30B base identity and the bundled decision/guardian adapters and speech encoder.
- Use the supported runtime, processor and control-token contract for each mode; do not equate a modular checkpoint with arbitrary separately updated components.
- IBM's current **revision 4.1.1** is a backward-compatible patch of the existing 8B checkpoint. Its `decision` aLoRA is refreshed, the base model remains unchanged, and the embedded TurboCTC now lists seven languages with punctuation/capitalization. The original **4.1** revision remains English-only and should be selected by an explicit historical revision when required. A patch is not a separately credited trained model identity. [8B card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b) [IBM release](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1).
- Publisher release messaging says ten ASR languages, but both exact 4.1.1 packaged model cards list seven: English, French, German, Spanish, Portuguese, Italian and Japanese. Document the narrower source-specific set and do not extrapolate to the standalone NC TurboCTC checkpoint. Record runtime-dependent audio support and do not infer independent model-quality validation. [IBM release](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1) [30B card](https://huggingface.co/ibm-granite/granite-switch-4.1-30b) [8B card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b).

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
