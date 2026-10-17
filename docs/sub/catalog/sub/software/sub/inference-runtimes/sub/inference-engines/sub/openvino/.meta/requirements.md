# Documentation Requirements

## Requirements

- Identify OpenVINO as the independently released, open-source toolkit for converting, optimizing, compiling, and executing neural-network inference, with primary catalog placement under `inference-runtimes/inference-engines`.
- Preserve the runtime's CPU, Intel GPU, and Intel NPU device/backend boundaries; support for non-Intel CPU architectures and specific operating systems is device- and release-dependent.
- Distinguish OpenVINO Runtime and model-compilation components from the separately catalogued NNCF compression software. Treat the GenAI libraries, tokenizers, backend plugins, and SDK APIs as ecosystem components rather than duplicating the toolkit as multiple peer entities by default.
- Treat OpenVINO Model Server as a potentially distinct distributed serving product only after separately qualifying its released independent identity and canonical owner; do not conflate its API/deployment behavior with the local runtime.
- Ground conversion support (ONNX, PyTorch, TensorFlow, supported quantization methods), model coverage, precision, CPU/GPU/NPU acceleration, driver dependencies, supported releases, and platform compatibility in current official documentation.
- Attribute efficiency and throughput claims to the exact model, device, toolkit and plugin versions, quantization, batch/context configuration, and measurement methodology.
- Use the upstream OpenVINO project as the catalog producer, consistent with existing NNCF provenance; keep Intel's corporate relationship distinct from that project's canonical identity.
- Treat current releases, deprecations and driver/runtime installation details as mutable.

## Validation

- One canonical OpenVINO toolkit identity exists under inference engines, not a duplicate model, managed service, or NNCF entry.
- Supported hardware, precision and operating-system claims are version and device scoped.
- Official documentation/repository links resolve to the OpenVINO upstream.
- `produced-by` and upstream producer `produces` links are reciprocal.
