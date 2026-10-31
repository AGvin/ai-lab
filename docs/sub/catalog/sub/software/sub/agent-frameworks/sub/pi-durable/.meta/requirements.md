# Documentation Requirements

## Requirements

- Identify Pi Durable as the separate experimental Earendil Works TypeScript framework for constructing durable multi-conversation agent applications, not as an alternate Pi terminal CLI distribution.
- Preserve restartable task/checkpoint execution, atomic transcript and state commits, storage backends, conversation forks, reusable extensions/tools/hooks and operator-selected tool execution environments at a stable high level.
- Distinguish the Pi coding agent and the shared lower-level `pi-ai` and Chord dependencies from the Pi Durable framework product.
- Preserve explicit operational boundaries: crash recovery requires persistent storage, retry-safe tool semantics, environment access controls, correct concurrency/ownership, credentials and state protection, not just installing a package.
- Explain that the framework runs in the operator's selected JavaScript runtime and may target remote infrastructure, without implying a vendor-managed Earendil cloud-agent service.
- Keep experimental API stability, supported runtimes/backends, published versions, package dependencies and exact interface names time-scoped to official releases when expanded.
- Preserve `produced-by` Earendil Inc. with a reciprocal `produces` reference in the canonical producer.
- Render the standard `entity-relations` block and link official release announcement, package source and package manifest.

## Validation

- The framework is not confused with Pi 1.0, OMP, a model provider, or a hosted agent service.
- Experimental and operational limits are not described as enterprise production guarantees.
- Reciprocal producer relation and official references resolve to the canonical nodes and upstream sources.
