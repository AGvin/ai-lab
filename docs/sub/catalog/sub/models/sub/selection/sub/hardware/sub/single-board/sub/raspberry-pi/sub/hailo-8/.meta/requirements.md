# Documentation Requirements

## Requirements

- Cover Raspberry Pi 5 with AI HAT+/AI Kit-class Hailo-8L or Hailo-8 acceleration.
- Make the current official capability boundary explicit: Hailo-8L/Hailo-8 AI HAT+ is primarily supported for vision/neural workloads and does **not** inherit Hailo-10H LLM/VLM support merely because both are Hailo NPUs.
- Identify exact accelerator variant, Raspberry Pi OS/package (`hailo-all` or current successor), Hailo runtime/model export, supported model/operator/precision, camera/media pipeline, and host RAM.
- Use Hailo-supported model zoo/custom compiled artifacts as compatibility evidence; arbitrary ONNX/PyTorch source weights are not directly runnable proof.
- Measure end-to-end latency/throughput including host preprocess/postprocess and sustained thermals/power.
- Route generative LLM/VLM needs to `../hailo-10h/`, CPU, another platform, or hosted execution rather than implying unsupported Hailo-8 capability.

## Validation

- Hailo-8/8L and Hailo-10H capabilities are not conflated.
- TOPS is not used as architecture compatibility evidence.
- Exact compiled/runtime artifact scope is visible.
