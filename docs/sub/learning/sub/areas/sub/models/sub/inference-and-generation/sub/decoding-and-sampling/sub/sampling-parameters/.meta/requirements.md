# Documentation Requirements

## Requirements

- Teach sampling parameters as evaluated controls over stochastic decoding behavior; use the canonical Sampling Parameters concept for stable semantics of temperature, top-k, top-p, penalties, composition/order caveats, and the boundary against factuality or deterministic guarantees.
- Treat sampling configuration as model/runtime/task-specific rather than a set of universal creativity/accuracy presets. Begin from a documented or intentionally chosen control configuration and compare changes against representative task cases.
- Change one major sampling dimension at a time when isolating causal configuration effects is useful; record the complete decoding configuration so hidden parameter differences are not attributed to the model itself.
- Explain the practical trade-off between lower-variance/narrower generation and broader/diverse sampling without claiming either is universally correct. Match the evaluation to whether repeatability, constrained outputs, coverage, novelty, diversity, or another outcome is actually desired.
- Fix upstream defects such as unclear instructions, missing context/evidence, invalid schema/task definition, unsupported capabilities, or authorization problems before treating sampling changes as the primary remedy.
- Avoid combining aggressive temperature, top-p, top-k, repetition/frequency/presence penalties, or provider-specific controls without measurement when the goal is to understand which change affected behavior.
- Compare candidate configurations on a stable representative test set when selecting settings for repeated use; preserve exact model/version/runtime/configuration identity with evidence/results.
- When a runtime exposes seeds or deterministic modes, teach them as scoped reproducibility aids rather than permanent guarantees. Repeatability can change with model/version, runtime, hardware, batching, kernels/provider infrastructure, or other execution-path changes.
- Distinguish seed-controlled repeatability from the underlying probability distribution and from semantic correctness. Repeating the same output does not establish factuality, quality, safety, or task validity.
- Keep provider-specific parameter names/defaults, undocumented interaction order, supported ranges, deterministic guarantees, current APIs, and measured comparisons with catalog/evidence owners.

## Validation

- Sampling values are not presented as universal task presets.
- Configuration comparisons record the complete relevant decoding setup and use representative evaluation where needed.
- Sampling is not used as a substitute for fixing missing evidence/instructions/schema/authorization defects.
- Seeds/deterministic modes are scoped reproducibility mechanisms rather than timeless output guarantees.
- Concrete provider behavior and measured results remain evidence/catalog-owned.
