# Documentation Requirements

## Requirements

- Present NVIDIA Isaac ROS as NVIDIA's accelerated open-source ROS software suite for robotics/physical-AI perception and runtime integration on Jetson and discrete GPUs.
- Preserve the current Isaac ROS 5.0 release boundary: NVIDIA released 5.0 on 2026-09-22 with ROS Lyrical and Ubuntu 24.04 support, CUDA-backed `rosidl::Buffer` adoption, and agent-oriented development workflows; keep these version-specific facts scoped to the applicable release.
- Keep standard ROS middleware semantics outside this profile; focus on NVIDIA's independently maintained accelerated robotics packages and integrations.
- Treat supported ROS/Ubuntu/JetPack versions, packages, GPU requirements, repository availability, and performance claims as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Isaac ROS remains physical-AI/robotics software rather than generic ROS middleware or an inference runtime.
- Producer provenance resolves to NVIDIA.
