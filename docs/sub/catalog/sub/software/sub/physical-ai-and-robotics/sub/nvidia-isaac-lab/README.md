# NVIDIA Isaac Lab

NVIDIA Isaac Lab is a robot-learning framework and environment centered on reinforcement learning, imitation learning, data generation, and policy development in physically simulated environments.

## Operation and compatibility

The standard Isaac Sim-based workflow requires a compatible Isaac Sim installation and the same Python version used by that simulator build. Match the simulator, driver and learning-framework environment to the selected Isaac Lab release.

The source checkout supplies training and example scripts. The pip-only layout is intended for external extensions with custom runners and omits those scripts. Robot and environment assets are fetched from remote storage; a prepared local cache supports repeated or offline use.

Newton integration is a separate experimental path on the develop branch as part of Isaac Lab 3.0 Beta. Its current supported tasks and APIs are narrower and can change; they should not be inferred from the standard installation or from Newton's standalone release status.

## Relations

- Produced by [NVIDIA](../../../../../producers/sub/n/sub/nvidia/).

## Official resources

- [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab)
- [Isaac Lab documentation](https://isaac-sim.github.io/IsaacLab/main/)
- [Installation and dependency choices](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html)
- [Newton integration status](https://isaac-sim.github.io/IsaacLab/main/source/experimental-features/newton-physics-integration/index.html)
