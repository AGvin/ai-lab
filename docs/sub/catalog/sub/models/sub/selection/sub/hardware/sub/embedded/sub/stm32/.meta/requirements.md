# Documentation Requirements

## Requirements

- Cover STM32 embedded AI routes using current STM32Cube.AI/related ST tooling and Neural-ART-capable hardware where applicable.
- Identify exact MCU/MPU family, CPU/NPU presence, SRAM/external memory/flash, toolchain version, supported operators/data types/model formats, quantization, input shape, and real-time/power constraints.
- Distinguish ordinary MCU CPU inference from STM32N6/Neural-ART-style NPU routes; do not compare them only by TOPS/clock rate.
- Use ST model zoo/tool validation for compatibility but independently evaluate application accuracy/latency/memory after conversion.
- Include pre/post-processing and sensor pipeline resource cost when material.
- Split deeper STM32 families only if future content shows distinct reader routes that cannot be handled by compatibility tables/sections.

## Validation

- CPU and NPU routes are not conflated.
- Operator/tool compatibility precedes performance claims.
- Memory, latency, power, and post-quantization accuracy are explicit.
