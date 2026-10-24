# Documentation Requirements

## Requirements

- Present NVIDIA Isaac Sim as a robotics/physical-AI simulation and testing platform with physically based simulation and synthetic-data workflows for robot development.
- Keep synthetic-data generation, ROS integration, sensors, and robot-learning integrations as parts of the embodied simulation lifecycle rather than alternate data-generation or middleware placements.
- Treat hardware/software requirements, supported sensors/robots, release compatibility, APIs, and performance claims as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- Explain the supported RTX-capable GPU/driver environment and that GPUs without RT cores, including A100 and H100, are not supported by the documented simulator requirements. Containers are supported on Linux; default online assets and some extensions require network access. Use the applicable release's cross-product compatibility guidance for Isaac Lab, ROS and Newton rather than assuming arbitrary versions interoperate.

## Validation

- Isaac Sim remains physical-AI/robotics software rather than generic simulation, data generation, or inference-runtime ownership.
- Producer provenance resolves to NVIDIA.
