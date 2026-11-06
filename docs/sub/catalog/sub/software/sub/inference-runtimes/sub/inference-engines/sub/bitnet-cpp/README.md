# BitNet.cpp

**BitNet.cpp** is Microsoft's MIT-licensed open-source inference framework optimized for ternary and low-bit BitNet models. It is **runtime software**, separate from the [BitNet-b1.58-2B-4T model weights](https://huggingface.co/microsoft/BitNet-b1.58-2B-4T) and distinct from general-purpose [llama.cpp](../llama-cpp/) inference.

## Execution environment and model support

- The original README announces **BitNet.cpp 1.0 (2024-10-17)**, but the repository exposes **no published GitHub Releases entries** at the 2026-11-02 source check. This profile pins source commit `0b341e582afbf9e1011f24744b554c96a3477eb5` rather than implying a verified binary/tag.
- Optimized **x86 and ARM CPU** kernels support selected ternary/low-bit BitNet model formats, including model-dependent I2_S, TL1 or TL2. A separately documented **CUDA GPU W2A8** kernel provides an additional pathway; not all models/architectures are interchangeable. NPU support is described upstream as **planned**, not already supported.
- Original setup uses recursive Git submodules, compiler dependencies, a recommended Python 3.10 environment, a compatible checkpoint download, format conversion/setup and `run_inference.py`. This is a source build workflow, not a verified one-command install. Model formats, kernels, CPU instructions and GPU dependencies must match.

## Performance and risk boundaries

Publisher documents higher throughput and lower energy than specified higher-precision baselines on selected test hardware. These are **publisher results**, not AI Lab reproducibility measurements or guaranteed speedups on arbitrary Raspberry Pi, x86 processors or CUDA cards.

Source builds and model setup involve external dependencies, submodules, downloaded model checkpoints and executable tools. Pin and verify trusted revisions, isolate build/runtime permissions, restrict secrets and network access, and test architecture compatibility before use. Do not assume that MIT code licensing extends to weights, datasets or third-party components. Corporate beneficial ownership and indirect stakes remain unverified.

## Relations

- Produced by: [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/).
- Alternative general-purpose inference runtime: [llama.cpp](../llama-cpp/).
- Related model weights (separate catalog research candidate): [BitNet-b1.58-2B-4T](https://huggingface.co/microsoft/BitNet-b1.58-2B-4T).

## Original sources

- [Microsoft BitNet repository](https://github.com/microsoft/BitNet)
- [Source README and setup](https://github.com/microsoft/BitNet/blob/main/README.md)
- [GPU W2A8 implementation](https://github.com/microsoft/BitNet/blob/main/gpu/README.md)
- [Upstream security reporting](https://github.com/microsoft/BitNet/blob/main/SECURITY.md)
