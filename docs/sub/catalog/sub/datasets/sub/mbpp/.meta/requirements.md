# Documentation Requirements

## Requirements

- Pin Google Research mbpp/README.md, preserve the published split and the original-versus-sanitized dataset distinction; no execution or independent coverage verification.
- Source-pinned dataset identity with distinct task data, software, model outputs and historical results; no duplicate credit or assumption of implied training/evaluation rights.
- Rights and safety: The root Google Research repository LICENSE is Apache-2.0 for covered material; any third-party dependency and code execution environment requires its own review. Generated Python is untrusted: isolate execution, limit resources/network, and prevent reference-solution or test leakage into prompts.
- Treat this as metadata-only scoped source acceptance: no data downloads, model inference, code, benchmarks, GPU workloads, audio processing or external services executed.
- Maintain canonical Datasets parent navigation and entity metadata.

## Validation

- Verify the pinned source revision, new metadata, requirements, reader and parent link.
- Do not claim unperformed whole-tree YAML schema checking, complete renderer/cache closure, full rights audit, repository-wide CI or clean-group pass.
