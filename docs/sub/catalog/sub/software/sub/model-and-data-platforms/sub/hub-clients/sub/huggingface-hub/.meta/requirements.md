# Documentation Requirements

## Requirements

- Identify `huggingface_hub` as the official Python client library for interacting with Hugging Face Hub repositories, files, models, datasets, Spaces, jobs, endpoints, and related Hub resources.
- Preserve the selected identity rule that the bundled `hf` CLI is part of the same software item as `huggingface_hub`, not a duplicate catalog product.
- Preserve its primary placement under `model-and-data-platforms/hub-clients`; the client accesses hosted Hugging Face Hub services but is itself installable client software.
- Keep CLI commands, supported Hub APIs, cache/transfer behavior, authentication mechanisms, and other mutable details source-backed when expanded.
- Include current official `huggingface_hub` documentation and repository references.

## Validation

- `huggingface_hub` and `hf` CLI remain one canonical software identity.
- Hosted Hub products accessed by the client are not absorbed into the client profile.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
