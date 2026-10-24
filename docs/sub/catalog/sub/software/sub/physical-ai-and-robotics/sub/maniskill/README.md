# ManiSkill

ManiSkill is a robotics simulation and training framework with Gym and Gymnasium interfaces, GPU and CPU simulation, reinforcement learning, imitation learning, parallel rendering, and sim2real tooling.

## Operation and compatibility

ManiSkill builds its rigid-body tasks on SAPIEN and exposes environments to learning code through Gym and Gymnasium interfaces. A compatible PyTorch installation supports its learning workflows.

State-based simulation and visual observations have different requirements. Rendering needs a GPU with a working Vulkan driver; successful state simulation does not establish that a camera or viewer will work. The project currently provides its strongest support on Linux with NVIDIA GPUs, with platform-specific limitations elsewhere.

The released package and the more frequently updated nightly package are separate installation choices. Many task assets and demonstration datasets are downloaded separately and stored under the configurable `MS_ASSET_DIR` directory. Include those assets when preparing a reproducible or offline environment.

## Relations

- Produced by [ManiSkill Project](../../../../../producers/sub/m/sub/maniskill-project/).

## Official resources

- [ManiSkill repository](https://github.com/mani-skill/ManiSkill)
- [ManiSkill quickstart](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/quickstart.html)
- [Installation, rendering and assets](https://maniskill.readthedocs.io/en/latest/user_guide/getting_started/installation.html)
