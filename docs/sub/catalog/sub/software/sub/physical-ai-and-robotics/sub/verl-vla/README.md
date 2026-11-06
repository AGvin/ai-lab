# verl-vla

verl-vla is an open-source vision-language-action post-training framework built on verl. It connects robot demonstration collection, supervised fine-tuning, policy evaluation, human intervention, and reinforcement learning. Its [v0.1.0 release](https://github.com/verl-project/verl-vla/releases/tag/v0.1.0), published on 19 August 2026, is a separate Python distribution with its own commands and integrations.

## Fit and scope

Use verl-vla when one workflow needs to coordinate policy training, rollout, simulator or robot interaction, and operator corrections across local or distributed resources. The product's primary identity is embodied policy learning. General LLM post-training remains with [verl](../../../model-and-data-platforms/sub/model-development/sub/verl/).

[LeRobot](../hugging-face-lerobot/) is an adjacent choice for robot interfaces, datasets, policies, and training/deployment workflows. Compare the concrete recipe and device support needed for the task: verl-vla's distinction here is its composition of those stages through verl-based distributed execution, while it also reuses LeRobot recording formats.

## Workflow and requirements

The [quick start](https://verl-vla.readthedocs.io/en/latest/getting-started/index.html) records and replays LIBERO demonstrations, trains and evaluates an ACT policy, optionally collects intervention trajectories, and performs a further policy update. The full example needs a CUDA-capable NVIDIA GPU; its teleoperation and collection steps can use OSMesa CPU rendering. Recorded datasets and videos, model checkpoints, and evaluation metrics are separate outputs.

[TrainCluster](https://verl-vla.readthedocs.io/en/latest/framework-overview/train-cluster.html) manages actor, rollout, and environment workers. The [resource configuration](https://verl-vla.readthedocs.io/en/latest/framework-overview/resource-and-configuration.html) selects the needed composition:

| Workflow | Roles |
| --- | --- |
| Offline supervised training | Actor |
| Teleoperation, recording, replay | Environment |
| Evaluation, autonomous collection, DAgger | Environment and rollout |
| Interactive online reinforcement learning | Environment, actor, and rollout |

Actor and rollout work can share resources or use separate pools; resource labels place environments with the machines that provide rendering or robot access. Match the workflow's pinned dependencies and upstream model/environment recipe before selecting hardware or scaling it. The v0.1.0 package requires Python 3.10 or later and pins core verl 0.7.1; developing documentation may describe later combinations.

## Operational boundaries

Browser intervention can interrupt policy actions, collect corrections, and return control to the policy. These controls are part of the learning workflow, not evidence of safe physical deployment. Piper is listed among the v0.1.0 integrations, but the published [Piper keyboard guide](https://verl-vla.readthedocs.io/en/latest/data-collection/piper/keyboard.html) contains no setup procedure. The concrete LIBERO walkthrough should not be read as a complete physical-robot commissioning guide.

For a cloud model cluster and a local robot host, the [Ray over autossh guide](https://verl-vla.readthedocs.io/en/latest/troubleshooting/distributed-execution/ray-over-ssh.html) keeps Ray traffic inside encrypted SSH with loopback listeners. Both machines need identical Python and Ray versions. Placement labels keep robot I/O local. This protects the documented Ray connection; assess the browser observation/control endpoint separately.

Ray runtime environment values reach distributed workers, including any configured artifact credentials. The resource guide uses environment interpolation rather than credentials stored in tracked YAML. Recording writes datasets and video locally; the quick start presents Hugging Face upload as a separate action.

## Relations

- Produced by: [verl Project](../../../../../producers/sub/v/sub/verl-project/)

## Official resources

- [Repository](https://github.com/verl-project/verl-vla)
- [v0.1.0 release and capability record](https://github.com/verl-project/verl-vla/releases/tag/v0.1.0)
- [v0.1.0 package metadata](https://github.com/verl-project/verl-vla/blob/v0.1.0/pyproject.toml)
- [Documentation](https://verl-vla.readthedocs.io/en/latest/)
