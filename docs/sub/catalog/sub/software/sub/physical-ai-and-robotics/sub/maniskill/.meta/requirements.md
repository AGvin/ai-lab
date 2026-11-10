# Documentation Requirements

## Requirements

- Present ManiSkill as a robotics simulation/training framework with Gym/Gymnasium interfaces, GPU/CPU simulation, reinforcement learning, imitation learning, parallel rendering, and sim2real tooling.
- Keep SAPIEN as an underlying simulator/dependency rather than an alternate canonical placement for ManiSkill.
- Treat supported tasks/robots, simulation backends, learning-framework integrations, package versions, hardware requirements, and benchmark claims as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- Explain that SAPIEN supplies the underlying rigid-body simulation, while camera/viewer rendering requires a GPU with a working Vulkan driver. State-based simulation and rendering have different requirements. Keep release and nightly packages distinct and identify separately downloaded assets and their configurable local data directory; avoid a blanket macOS-support claim because the current installation prose and matrix conflict.

## Validation

- ManiSkill remains physical-AI/robotics software rather than a generic RL/model-development framework.
- Producer provenance resolves to the project-level ManiSkill identity.
