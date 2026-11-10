# Documentation Requirements

## Requirements

- Identify BitNet.cpp as Microsoft's independently distributed MIT-licensed **inference engine**, not the BitNet model family, the `BitNet-b1.58-2B-4T` trained weights, a general model-serving API, a CPU/GPU device or a cloud service. Distinguish its source/submodule dependencies and optimized low-bit kernels from unrelated `llama.cpp` inference.
- Source-pin the exact inspected original Microsoft Git `main` commit `0b341e582afbf9e1011f24744b554c96a3477eb5`. The README calls version **1.0** released 2024-10-17, while the official GitHub Releases API exposes no releases for the repository as of 2026-11-02. Do **not** invent a tagged release/version artifact, package registry or universal stable support guarantee.
- Explain the original low-bit/ternary model execution role, primarily x86 and ARM CPU kernels with I2_S/TL1/TL2 formats, and a separately implemented **CUDA GPU W2A8** component. The original supported-model matrix is model- and architecture-specific. Avoid claiming universal CPU/GPU/NPU compatibility; README calls NPU support *upcoming*, not delivered.
- Preserve version-specific build/run context: original README recommends an environment with Python **3.10** (not evidence of a package-wide formal Python version constraint), git clone with recursive submodules, dependency installation and model download/conversion/setup before inference. GPU separate requirements and prerequisites must be checked against its own guide; do not present arbitrary vendor GPU as supported.
- Treat speed/energy, 100B-on-one-CPU and model-quality numbers as **publisher-reported hardware/test-specific comparisons** with unverified benchmark baselines, not independent measured AI Lab results or universal performance claims.
- Security: the build and setup process includes compiler/toolchain/submodules, external dependencies, downloaded checkpoint artifacts and execution scripts. Use signed/pinned commits or trusted source revisions, isolated/nonprivileged builds, checksum/rights review, hardware-specific testing, bounded runtime input and memory. Never execute upstream scripts or unfamiliar model weights against production systems as part of catalog discovery.
- Separate software's MIT grant from distribution and use rights for original or third-party model weights, quantized variants, datasets, CUDA/runtime dependencies and other incorporated components. Microsoft original code publisher is established, but full ultimate beneficial ownership, external licenses and possible indirect Russian shareholdings were not independently audited.
- Maintain exactly one software `produced-by` relation to existing `catalog/producers/m/microsoft` and reciprocal `produces`; do not create or accept the separate BitNet model candidate within this software package.

## Validation

- Source repository, LICENSE, CPU README, GPU README and Git source identity support the stated scope; model and software do not share canonical identity.
- Child index and producer inverse resolve, README relative links are materialized and security caveats actionable. No compiled binary, model execution, speed/energy benchmark, NPU support verification, supply-chain audit, global schema/cache/render/CI or owner merge asserted.
