# Documentation Requirements

## Requirements

- Cover Raspberry Pi local inference and route by materially different compute path: `cpu/`, `hailo-8/`, `hailo-10h/`.
- Identify exact Pi generation/RAM, 64-bit OS, storage/IO, power/cooling, accelerator/HAT if present, runtime packages, and intended sustained load.
- Do not mix CPU-fit with Hailo-compatible model fit; accelerator model compilation/export/runtime constraints are separate.
- Explain that Hailo-8/8L and Hailo-10H have materially different model universes; do not rank them only by TOPS.
- Account for host-side preprocessing/postprocessing, camera/media pipelines, accelerator-local memory where present, and CPU coordination cost.
- Recheck Raspberry Pi OS/package/Hailo support before current recommendations.

## Validation

- Direct children are CPU, Hailo-8/8L, Hailo-10H routes.
- Hailo acceleration is not inferred for arbitrary models.
- Cooling/power and sustained operation are included where material.
