# Documentation Requirements

## Requirements

- Cover MCU/deeply constrained embedded inference where SRAM/flash/PSRAM, operator coverage, conversion toolchains, real-time deadlines, power, and accelerator-specific runtimes define a model universe distinct from SBC/Linux inference.
- Route initial ecosystems to `esp32/`, `stm32/`, and `nxp/` because each has a distinct supported deployment toolchain.
- Do not create generic `arm/` as a sibling: CPU ISA alone does not identify the complete target/runtime route.
- Require exact chip, memory hierarchy, accelerator/core, supported operators/data types, quantization, input dimensions, firmware footprint, and latency/power deadline before model recommendation.
- Prefer task-specific tiny model classes and official model-zoo/tool support; do not transfer desktop LLM assumptions into this branch.

## Validation

- Embedded and single-board remain separate hardware classes.
- Direct children are only the three currently selected ecosystems.
- Generic TOPS/clock-rate comparisons do not replace operator/runtime compatibility.
