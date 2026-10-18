# Documentation Requirements

## Requirements

- Present verl-vla as the separately released, open-source vision-language-action post-training framework built on verl, joining robot demonstration collection, supervised fine-tuning, rollout/evaluation, human intervention, and reinforcement learning.
- Keep Physical AI and Robotics as the canonical owner because embodied policy learning and environment interaction define this product; retain general LLM post-training with the existing verl profile under Model Development.
- Keep TrainCluster, actor/rollout/environment workers, Ray/FSDP execution, teleoperation, recording/replay, checkpoints, model adapters, and simulator/robot integrations within this identity. Integrated policies, datasets, simulators, and robot hardware remain distinct products or artifacts.
- Ground released eligibility in v0.1.0, published 2026-08-19 as a non-draft, non-prerelease release with its own Python package and console entrypoints; do not infer general availability, production suitability, or universal model/environment compatibility from that release flag.
- Explain when a user needs verl-vla's composed distributed workflow and compare the existing verl and LeRobot profiles without claiming either lacks overlapping training or data-collection capabilities.
- Describe actor-only training, environment-only collection/replay, environment/rollout evaluation or DAgger, and environment/actor/rollout online RL as workflow-dependent compositions. Explain that resource placement and model/environment settings are separately configured.
- Distinguish released integrations from documented runnable recipes. The full LIBERO quick start provides concrete collection-to-learning evidence; the published Piper keyboard page currently has no setup procedure. Do not present every model/algorithm/environment combination or physical-robot commissioning as validated.
- Describe the operational boundary between model workers, environment/robot workers, browser intervention, local datasets/videos, training checkpoints, and optional artifact uploads. Human intervention changes policy control; it does not by itself establish safe physical deployment.
- Preserve the documented cloud-to-robot Ray boundary: the autossh recipe keeps Ray listeners on loopback inside an encrypted SSH connection, requires identical Python and Ray versions, and uses resource labels to place robot I/O locally. Runtime environment values, including credentials, propagate to workers; use environment interpolation instead of embedding credentials in tracked configuration.
- Treat support matrices, pinned dependency versions, hardware needs, performance results, recipes, and physical-robot instructions as freshness-sensitive. Scope benchmark claims to the exact model, task, recipe, hardware, and evaluation protocol; keep developing documentation distinct from the v0.1.0 release record.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The leaf is an independently released software identity rather than a duplicate of core verl, a VLA model, or a dataset.
- Producer provenance resolves to the existing verl Project; preserve the package's ByteDance author attribution without silently replacing the project release identity.
- The producer has the exact inverse `produces` edge, and reader links resolve to the current canonical producer and peer owners.
- Decision and operational claims stay within cited released capabilities or explicitly identified current documentation; no runtime or physical safety assurance is implied by documentation review.
