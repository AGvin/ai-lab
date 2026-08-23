# Documentation Requirements

## Requirements

- Cover ESP32-family embedded inference using current Espressif-supported deployment stacks such as ESP-DL where applicable.
- Identify exact SoC (e.g. S3/P4-class differences), on-chip/external RAM/PSRAM/flash, accelerator/instruction support, ESP-IDF/ESP-DL version, supported operators/data types, quantization, input dimensions, and real-time deadline.
- Prefer official examples/model zoo or models demonstrably convertible to the target; do not assume TensorFlow/PyTorch source compatibility.
- Evaluate firmware + model + arena/buffers together; peak SRAM/PSRAM and flash footprint matter as much as parameter count.
- Measure task latency, real-time deadline margin, power, and accuracy after quantization/conversion.
- Keep LLM-scale assumptions out unless a future ESP32-class platform/toolchain explicitly supports a materially different generative route.

## Validation

- Exact chip/toolchain is specified.
- Memory arenas/firmware overhead are included.
- Model quality after quantization is measured, not assumed.
