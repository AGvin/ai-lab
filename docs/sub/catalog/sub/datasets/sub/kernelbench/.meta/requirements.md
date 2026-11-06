# Documentation Requirements

## Requirements

- Preserve four-level task taxonomy and v0/v0.1 distinction; separate correctness from speed, code from data, and generated GPU kernels from verified production software.
- Source-pinned dataset identity with distinct task data, software, model outputs and historical results; no duplicate credit or assumption of implied training/evaluation rights.
- Rights and safety: The pinned root LICENSE contains MIT code terms. Source model architectures, separately hosted datasets and generated CUDA or other kernels may have their own provenance. Never run untrusted generated kernels on production GPU devices; use isolated environments, resource limits and reproducible hardware/runtime settings.
- Treat this as metadata-only scoped source acceptance: no data downloads, model inference, code, benchmarks, GPU workloads, audio processing or external services executed.
- Maintain canonical Datasets parent navigation and entity metadata.

## Validation

- Verify the pinned source revision, new metadata, requirements, reader and parent link.
- Do not claim unperformed whole-tree YAML schema checking, complete renderer/cache closure, full rights audit, repository-wide CI or clean-group pass.
