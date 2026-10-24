# Documentation Requirements

## Requirements

- Represent FlowState R1 as one concrete Granite Time Series model identity with chronological version 1.0 and version 1.1 releases.
- Preserve version 1.0 as the default repository state and version 1.1 as the explicitly selected `revision="r1.1"` release.
- Keep release-specific context, architecture, hyperparameters, parameter counts, loading selectors, and other deltas on the corresponding `model-version` nodes rather than flattening them into the parent model.
- Preserve current model-wide operating boundaries from first-party guidance: FlowState currently supports zero-shot forecasting; choose temporal scaling from the actual sampling rate and seasonality; IBM recommends forecasting no more than 30 seasons because quality declines beyond that horizon.
- Preserve model-wide sampling-rate adaptation, supported-task boundaries, benchmark scope, and commercial/research release distinctions only from current first-party sources.

## Validation

- Membership resolves to Granite Time Series.
- The parent entity is type `model` and has exactly two represented `has-version` relations: version 1.0 and version 1.1.
- Each represented release has the inverse `version-of` relation to FlowState R1.
- Parent guidance does not generalize version 1.0 context/parameter values to version 1.1 or vice versa.
- Reader guidance preserves zero-shot, seasonality-aware scaling, and the 30-season recommendation without turning source-scoped guidance into a universal runtime guarantee.
