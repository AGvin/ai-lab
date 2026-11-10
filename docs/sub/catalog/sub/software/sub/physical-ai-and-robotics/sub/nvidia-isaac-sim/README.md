# NVIDIA Isaac Sim

NVIDIA Isaac Sim is a robotics and physical-AI simulation and testing platform with physically based simulation and synthetic-data workflows for robot development.

## Operation and compatibility

Isaac Sim combines robot and scene assets, physics, sensors, rendering and synthetic-data workflows. It can connect to ROS and robot-learning tools while remaining the simulation and testing environment.

The documented simulator environment requires a supported RTX-capable GPU and compatible drivers. Compute GPUs without RT cores, including A100 and H100, are not supported. Rendering-heavy scenes and training through Isaac Lab can need additional memory beyond the basic simulator requirements.

Containers are supported on Linux. The default online asset root and some extensions require network access; a working package installation alone does not establish asset availability. Match Isaac Lab, ROS and Newton integrations using the selected release's cross-product compatibility guidance.

## Relations

- Produced by [NVIDIA](../../../../../producers/sub/n/sub/nvidia/).

## Official resources

- [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim/)
- [Isaac Sim documentation](https://docs.isaacsim.omniverse.nvidia.com/)
- [System requirements and compatibility](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/requirements.html)
