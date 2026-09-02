# Sampling Parameters

Legacy residual retained for task-specific tuning, comparative evaluation, and reproducibility practice that are intentionally outside the canonical Sampling Parameters concept owner.

> **Migration note:** Sampling-control identity, temperature/top-k/top-p semantics, composition and implementation-order caveats, repetition/frequency/presence-penalty boundaries, greedy/search alternatives, seed-versus-distribution separation, and non-factuality/non-determinism guarantees are already preserved in `docs/sub/concepts/sub/models/sub/interaction/sub/generation-controls/sub/sampling-parameters/`. The remaining material below stays here until its exact learning, evaluation, provider-configuration, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task-specific tuning residual

Sampling settings should be treated as evaluated configuration for a concrete model, runtime, and task rather than as universal presets.

Useful tuning practices include:

- begin from the provider/runtime's documented baseline or an intentionally chosen control configuration;
- change one major sampling dimension at a time when isolating its effect is useful;
- evaluate candidate settings on a stable, representative test set rather than on one convenient example;
- prefer lower-variance candidate configurations for tasks where repeatability and narrow outputs matter, and evaluate broader sampling for tasks where diversity is part of the objective instead of assuming either class is universally correct;
- fix unclear instructions, missing context, invalid schemas, or other upstream task-definition defects before attributing failures solely to sampling.

## Interaction and comparison residual

Avoid combining aggressive temperature, top-p, top-k, penalty, or provider-specific changes without measurement when the goal is to understand which control changed behavior. Record the complete decoding configuration when comparing runs so a result is not attributed to the model while hidden sampling differences remain uncontrolled.

## Reproducibility residual

When a runtime exposes a seed or deterministic mode, treat it as a scoped reproducibility aid rather than a permanent guarantee. Recheck repeatability after changes to model/version, runtime, hardware, batching, provider infrastructure, or other execution-path inputs that can affect generation.

These tuning, comparison, and reproducibility practices remain migration source material until their exact learning, evaluation, provider-configuration, or decision-support owners are verified.
