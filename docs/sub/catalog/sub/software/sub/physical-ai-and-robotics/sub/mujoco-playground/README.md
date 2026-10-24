# MuJoCo Playground

MuJoCo Playground is a suite of GPU-accelerated robot-learning environments and training recipes covering locomotion, manipulation, and vision-based tasks. It is published as the `playground` Python distribution and imported as `mujoco_playground`. [Version 0.2.0](https://github.com/google-deepmind/mujoco_playground/releases/tag/v0.2.0) was released on 16 March 2026 and is available on [PyPI](https://pypi.org/project/playground/0.2.0/).

## Fit and scope

Choose Playground when its environment suite and training recipes match the robot-learning task. It uses MuJoCo MJX interfaces with JAX and MuJoCo Warp implementations; its own identity is the environment and learning workflow built around those components. The [project site](https://playground.mujoco.org/) describes state- and pixel-based learning and specific simulation-to-robot demonstrations.

Compare [Newton](../newton/) when building an application around direct physics and solver APIs, and [robosuite](../robosuite/) for configurable simulation tasks, controllers, and demonstration collection. Their overlap does not imply interchangeable environments or reproducible results across engines.

## Release and compute choices

The [v0.2.0 package metadata](https://github.com/google-deepmind/mujoco_playground/blob/v0.2.0/pyproject.toml) requires **Python 3.11 or later**, despite older Python 3.10 wording in the README. It requires MuJoCo and MuJoCo MJX 3.6.0 or later and Warp 1.11 or later, and provides an optional CUDA JAX dependency group.

Version 0.2.0 made MuJoCo Warp the default implementation for environments. Select and record the implementation explicitly when reproducing a run; source-HEAD instructions and previous releases may have different defaults or dependencies.

The released package supplies JAX PPO and RSL-RL training entrypoints. The [release README](https://github.com/google-deepmind/mujoco_playground/blob/v0.2.0/README.md) documents numerical-precision concerns and distinguishes its current training script from the script used in the original paper. Preserve the algorithm, environment, backend, asset revision, hardware, and precision settings when comparing results.

## External assets and operational boundaries

The first load of a locomotion or manipulation environment can download robot assets from MuJoCo Menagerie. The [v0.2.0 loader](https://github.com/google-deepmind/mujoco_playground/blob/v0.2.0/mujoco_playground/_src/mjx_env.py) clones a missing asset directory and checks out commit `1b86ece576591213e2b666ebf59508454200ca97`. This requires Git, network access, and writable dependency storage.

An existing Menagerie directory is only checked for existence. An upgrade therefore does not by itself establish that previously cached assets match the release's expected revision. Record and verify the asset revision alongside the Python environment.

Google DeepMind is the package's named author. The project explicitly states that it is **not an officially supported Google product**; its released research software and demonstrated transfer results do not imply a support contract or universal robot-deployment result.

## Relations

- Produced by: [Google DeepMind](../../../../../producers/sub/g/sub/google-deepmind/)

## Official resources

- [Repository](https://github.com/google-deepmind/mujoco_playground)
- [Project site](https://playground.mujoco.org/)
- [Release changelog](https://github.com/google-deepmind/mujoco_playground/blob/v0.2.0/CHANGELOG.md)
