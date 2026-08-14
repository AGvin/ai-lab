# Documentation Requirements

## Requirements

- Identify Ollama as Ollama Inc.'s open-source integrated inference runtime for running and serving models on user-controlled machines, with optional first-party cloud-model/API access layered onto the same client/API experience.
- Preserve the local execution boundary: local Ollama API requests are served from the local runtime and current official privacy documentation states Ollama does not receive prompt/response content processed locally.
- Distinguish local models from Ollama cloud-hosted models. Cloud-model requests require Ollama account/API authentication and use a separate hosted processing path; do not describe cloud execution as local merely because the local client/API can invoke it.
- Preserve current integration surfaces at a stable high level: CLI, local HTTP API, Python/JavaScript libraries, model creation/customization, model library/publishing, Docker/system-service deployment, and launch/integration workflows with other AI tools.
- Preserve useful legacy trust boundaries around local API/network exposure, authentication when cloud/private/publishing features are used, model provenance and licenses, model files/storage, external tool integrations, cloud credentials, and deployment permissions.
- Keep cloud pricing/limits, exact supported models/integrations, API details, hardware/platform support, release versions, and other mutable product-state claims source-backed and time-scoped when expanded.
- Link the canonical Ollama Inc. producer profile.
- Include current official Ollama site, documentation, repository, privacy, and Terms references.

## Validation

- The page does not collapse Ollama's local runtime and optional Ollama Cloud execution into one data path.
- Local prompt privacy claims are scoped to local processing.
- Cloud-model invocation through the local client/API is not described as local inference.
- CLI, API, libraries, and model-management surfaces remain one Ollama software identity.
- The producer relation resolves to Ollama Inc.
