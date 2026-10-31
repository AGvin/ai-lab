# Documentation Requirements

## Identity and decision boundaries

- Include the stable 8B and 30B checkpoints only; preview variants and standalone adapter libraries have separate lifecycle/ownership gates.
- Explain component selection through the documented chat template and control tokens; the composition is not evidence that every backend supports every mode.
- Keep the embedded speech component revision and language claims separate from later updates to standalone TurboCTC weights.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.
- The 27 October 2026 **4.1.1** patch preserves the same stable 8B/30B model identities, bases, two-adapter composition and calling contract while refreshing the learned `decision` aLoRA weights and embedded Granite Speech 5.0 TurboCTC. Select the exact 4.1 or 4.1.1 revision; do not treat a version patch, standalone adapter update, or encoder swap as a newly accepted model identity. [IBM patch announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1) [30B revision card](https://huggingface.co/ibm-granite/granite-switch-4.1-30b) [8B revision card](https://huggingface.co/ibm-granite/granite-switch-4.1-8b).
- The 4.1.1 checkpoint cards explicitly list **seven** audio-input languages (English, French, German, Spanish, Portuguese, Italian, Japanese) with punctuation and capitalization, whereas the IBM announcement says **ten**. Treat seven as the demonstrated packaged-card scope and the three-language discrepancy as unresolved rather than inventing support; original 4.1 revision remains English-only. The speech model is not jointly trained with the language backbone, so ASR errors can affect downstream decisions. [8B checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-8b) [30B checkpoint](https://huggingface.co/ibm-granite/granite-switch-4.1-30b) [IBM announcement](https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1).

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
