# Newton

Newton is an open-source physics simulation engine and Python SDK for robotics and robot learning. It is built on NVIDIA Warp and provides a common model and state representation for multiple solver backends. [Version 1.7.0](https://github.com/newton-physics/newton/releases/tag/v1.7.0) was published on 14 October 2026.

## Fit and scope

Use Newton when an application needs direct control of physics models, solver choice, contacts, sensors, and the simulation loop. It supports robot-learning workflows, including a documented [Isaac Lab locomotion-training and transfer example](https://developer.nvidia.com/blog/train-a-quadruped-locomotion-policy-and-simulate-cloth-manipulation-with-nvidia-isaac-lab-and-newton/). The current [FAQ](https://newton-physics.github.io/newton/stable/faq.html) still identifies the Isaac Lab integration as experimental.

For an environment suite with training recipes, compare [MuJoCo Playground](../mujoco-playground/); for configurable simulation tasks and demonstration collection, compare [robosuite](../robosuite/). [Isaac Lab](../nvidia-isaac-lab/) supplies a broader robot-learning workflow around simulation backends.

## Integration and compatibility

A Newton application builds or imports a model, allocates state/control/contact data, steps a selected solver, and consumes sensor or visualization outputs. URDF, MJCF, and USD imports are supported. Consult the [solver guide](https://newton-physics.github.io/newton/stable/solvers/index.html) for the required bodies, joints, contacts, coordinate representation, and differentiation support. The engine's differentiation capability does not extend uniformly to every solver; Kamino and VBD are explicitly experimental in that guide.

The [installation guide](https://newton-physics.github.io/newton/stable/guide/installation.html) requires Python 3.10 or later and distinguishes the base package from simulation, importer, and example extras. macOS uses CPU execution. NVIDIA GPU and driver requirements depend on the installed Warp wheel, so resolve Newton and Warp together against the release's compatibility guidance.

Newton's [version policy](https://newton-physics.github.io/newton/stable/guide/compatibility.html) permits breaking changes in minor releases and actively maintains only the latest minor line. Preserve an application's resolved dependencies and review migration notes when upgrading; the project's development lockfile is not automatically the environment a downstream wheel install resolves.

## Operational boundaries

Newton runs inside the caller's Python process. Its [security policy](https://github.com/newton-physics/newton/blob/v1.7.0/SECURITY.md) assigns sandboxing, network restrictions, and tenant isolation to the embedding application. Asset references can load other files or network resources, and extensions execute with the process's privileges.

For v1.7.0, importing USD-referenced Torch checkpoints requires explicit `allow_unsafe_torch_checkpoints=True` for trusted assets. Direct neural-drive construction remains a separate loading path. Treat serialized policies and checkpoints as executable inputs.

The same policy warns that `ViewerViser` inherits an unauthenticated listener on all interfaces, including when `share=False` and the printed URL says localhost. Restrict viewer reachability and protect intentional remote access.

## Relations

- Produced by: [Newton Project](../../../../../producers/sub/n/sub/newton-project/)

## Official resources

- [Repository and releases](https://github.com/newton-physics/newton)
- [Documentation](https://newton-physics.github.io/newton/stable/)
- [Project governance](https://github.com/newton-physics/newton-governance)
