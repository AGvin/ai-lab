# Genesis World

Genesis World is a physical-AI simulation platform combining multi-physics simulation, photorealistic rendering, compilation, and a Python API for robotics and machine-learning workflows.

## Operation and compatibility

Genesis World is a Python library installed alongside a compatible PyTorch build. Simulation can use CPU or the supported CUDA, ROCm and Metal backends; GPU execution depends on the matching platform and drivers. Physics execution and visualization have separate requirements: an Intel GPU can drive rendering, while simulation uses the CPU.

Rendering and asset import can require optional components beyond the base package. The installation guide distinguishes those dependencies and explains how to select a backend before constructing a scene.

The project credits Genesis AI support. That support provides provenance context without by itself establishing corporate ownership.

## Relations

- Produced by [Genesis World Project](../../../../../producers/sub/g/sub/genesis-world-project/).

## Official resources

- [Genesis World documentation](https://genesis-world.readthedocs.io/en/latest/)
- [What is Genesis?](https://genesis-world.readthedocs.io/en/latest/user_guide/overview/what_is_genesis.html)
- [Installation and backend requirements](https://genesis-world.readthedocs.io/en/latest/user_guide/overview/installation.html)
