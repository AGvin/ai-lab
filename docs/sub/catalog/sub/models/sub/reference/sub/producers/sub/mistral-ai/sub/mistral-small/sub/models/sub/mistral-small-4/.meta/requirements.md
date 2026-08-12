# Documentation Requirements

## Requirements

- Identify the exact Mistral Small 4 open-weight model and official repository.
- Preserve source-backed MoE structure, total/activated parameter counts, modalities, context length, reasoning-mode support, and license.
- Preserve the official NVFP4 quantized checkpoint and trained EAGLE speculative-decoding head as distinct first-party companion artifact repositories associated with the same base model.
- Keep activated parameters distinct from total parameters and from memory/storage requirements.
- Record current repository-size evidence only with explicit source/date and never equate repository size with runtime residency: the base repository is approximately 242 GB and the NVFP4 repository approximately 70.8 GB in the verified 2026-08-11 Hugging Face trees.
- Keep the provider claim that NVFP4 is intended to reduce memory/improve throughput and the EAGLE head to enable speculative decoding as provider evidence rather than AI Lab measured performance.
- Keep provider benchmark, throughput, latency, coding, and agentic claims as evidence inputs rather than AI Lab selection conclusions.
- Keep hosted pricing and API feature availability outside immutable model identity.

## Validation

- Mistral Small 4 is a concrete model under the Mistral Small family, not an artificial series node.
- The base, NVFP4, and EAGLE repositories are not silently collapsed into one artifact identity.
- Repository size is not presented as peak RAM/VRAM, model quality, or production-fit evidence.
- The EAGLE head is not presented as a separate Mistral Small family model without identity evidence.
- Runtime/deployment properties are not inferred from parameter counts.
- No dated recommendation is copied from the legacy page into reference.
