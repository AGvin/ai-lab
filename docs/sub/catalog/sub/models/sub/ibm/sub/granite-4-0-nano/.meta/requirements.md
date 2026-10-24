# Documentation Requirements

## Identity and decision boundaries

- Organize the eight materialized trained checkpoints by dense versus H hybrid architecture and base versus instruct role.
- Nano targets constrained and on-device use cases; compact weights alone do not guarantee a particular device memory budget or latency.
- Verify architecture-specific runtime and kernel support; do not treat dense and hybrid checkpoints as interchangeable or mirror quantized variants as models.
- The selected member weights use Apache-2.0; retain member-specific runtime and task boundaries.

## Validation

- Resolve identity, family membership and declared inverse relations to canonical entities.
- Keep downloaded-weight licensing separate from hosted terms and runtime-specific artifacts.
- Pin the selected checkpoint and runtime before deployment; measure memory, latency and task quality on representative inputs.
- Published benchmark results are producer claims; this documentation does not establish runtime or benchmark reproduction, cache freshness or final-render validation.
