# KernelBench

**KernelBench** — GPU kernel code generation with correctness and speedup evaluation.

## Data and evaluation boundary

The pinned publisher describes 100 level-1 single operators, 100 level-2 fusion patterns, 50 level-3 architectures and an extensible level-4 set of hosted model architectures. The fast_p metric counts kernels that pass correctness and exceed a speedup threshold against a PyTorch baseline. Repository v0 and v0.1 and hardware or runtime setups are not automatically comparable.

The [pinned first-party source](https://github.com/ScalingIntelligence/KernelBench/blob/423217d9fda91e0c2d67e4a43bf62f96f6d104f1/README.md) establishes the benchmark identity and version. Source data, trained models, scoring software, external service dependencies and leaderboard results are separate, version-dependent artifacts.

## Rights, limitations and safety

The pinned root LICENSE contains MIT code terms. Source model architectures, separately hosted datasets and generated CUDA or other kernels may have their own provenance. Never run untrusted generated kernels on production GPU devices; use isolated environments, resource limits and reproducible hardware/runtime settings.

This is a source-backed metadata profile only. No benchmark input, model run, generated program, audio recording, private data or unsafe code was executed or downloaded, and no repository-wide validation or complete rights audit was performed.

## Official source snapshot

- [Repository](https://github.com/ScalingIntelligence/KernelBench)
- [Pinned README](https://github.com/ScalingIntelligence/KernelBench/blob/423217d9fda91e0c2d67e4a43bf62f96f6d104f1/README.md)
- [Pinned LICENSE](https://github.com/ScalingIntelligence/KernelBench/blob/423217d9fda91e0c2d67e4a43bf62f96f6d104f1/LICENSE)
