# robosuite

robosuite is a MuJoCo-powered simulation framework and benchmark-environment suite for robot learning. It combines configurable robot embodiments, tasks, controllers, sensors, teleoperation, and demonstration collection. [Version 1.5.2](https://github.com/ARISE-Initiative/robosuite/releases/tag/v1.5.2) was published on 24 December 2025, with a matching [PyPI distribution](https://pypi.org/project/robosuite/1.5.2/).

## Fit and scope

Use robosuite to design or compare learning tasks through combinations of robot models, arenas, objects, observations, and controllers. Its [overview](https://robosuite.ai/docs/overview.html) distinguishes simulation and demonstration utilities from related learning tools such as robomimic.

Compare [MuJoCo Playground](../mujoco-playground/) when its GPU environment suite and training recipes fit the task, or [Newton](../newton/) when direct engine and solver integration is required. [LeRobot](../hugging-face-lerobot/) provides an adjacent physical-robot, dataset, and policy workflow.

## Configuration and installation

A robot's [composite controller](https://robosuite.ai/docs/modules/controllers.html) splits actions among body-part controllers. The selected controller determines whether a policy commands joint values, end-effector targets, or other control quantities. Preserve its action layout, reference-frame and impedance settings when transferring a policy or comparing demonstrations.

The [v1.5.2 setup metadata](https://github.com/ARISE-Initiative/robosuite/blob/v1.5.2/setup.py) requires MuJoCo 3.3.0 or later and pins `mink==0.0.5`. [Optional dependencies](https://github.com/ARISE-Initiative/robosuite/blob/v1.5.2/requirements-extra.txt) add HDF5 demonstration utilities, Gymnasium integration, extra robot models, and USD export.

The [installation guide](https://robosuite.ai/docs/installation.html) identifies macOS and Linux as officially supported and provides separate Windows troubleshooting. On macOS, the default MuJoCo viewer requires the `mjpython` launcher. Choose the renderer and dependencies for the intended on-screen or headless workflow.

## Demonstration and transfer boundaries

[Collected demonstrations](https://robosuite.ai/docs/algorithms/demonstrations.html) are stored locally as `demo.hdf5`, with environment/model metadata and sequences of simulation states and actions. Observations such as images can be regenerated from states during postprocessing.

Replaying actions is different from restoring recorded states. The guide warns that deterministic action playback is not guaranteed across machines or platforms and recommends state replay for reproducing a trajectory. The [released playback script](https://github.com/ARISE-Initiative/robosuite/blob/v1.5.2/robosuite/scripts/playback_demonstrations_from_hdf5.py) restores states by default and uses action stepping only with `--use-actions`.

Visual, dynamics, and sensor [randomization](https://robosuite.ai/docs/algorithms/sim2real.html) can help address simulation-to-real differences. Preserve the exact task, control, physics, and sensor assumptions when assessing transfer; a simulation result alone does not establish physical deployment suitability.

The [license file](https://github.com/ARISE-Initiative/robosuite/blob/v1.5.2/LICENSE) contains the MIT license and a separate notice for MuJoCo-derived code.

## Relations

- Produced by: [ARISE Initiative](../../../../../producers/sub/a/sub/arise-initiative/)

## Official resources

- [Repository](https://github.com/ARISE-Initiative/robosuite)
- [Project site](https://robosuite.ai/)
- [Documentation](https://robosuite.ai/docs/overview.html)
