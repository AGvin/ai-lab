# Documentation Requirements

## Requirements

- Present MuJoCo Playground as an independently released suite of GPU-accelerated robot-learning environments and training recipes for simulation and sim-to-real research, owned by Physical AI and Robotics.
- Distinguish the `playground` Python distribution and `mujoco_playground` import from the underlying MuJoCo, MJX, JAX, MuJoCo Warp, and external robot assets; keep locomotion, manipulation, vision environments, and training entrypoints within this identity.
- Ground release eligibility in v0.2.0, published 2026-03-16, corroborated by the independently published PyPI distribution. Use the released pyproject's Python >=3.11 requirement rather than the README's older >=3.10 wording.
- Explain the MJX interface and JAX/Warp implementation choice. The v0.2.0 changelog makes MuJoCo Warp the default for environments; keep that version-specific fact distinct from README wording about HEAD.
- Cover release-matched MuJoCo/MJX/Warp constraints, accelerator installation, training-script choice, numerical precision, and model/task/backend-specific reproducibility without treating source HEAD, a released wheel, and the paper's training script as interchangeable.
- Preserve the automatic external-asset boundary: loading locomotion or manipulation environments may fetch Menagerie assets. In v0.2.0 the loader clones a missing dependency directory and checks out commit 1b86ece576591213e2b666ebf59508454200ca97; an existing directory is only existence-checked. Account for Git/network access, writable asset storage, and the actual cached revision.
- Explain when to select Playground's environment/training stack versus Newton's engine API or robosuite's task/controller/demonstration workflow; keep physical transfer claims tied to the demonstrated robot, policy, observations, and procedure.
- Preserve Google DeepMind provenance from official package/repository evidence while retaining the project's statement that it is not an officially supported Google product.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- This is a software framework, not a duplicate MuJoCo solver, a robot model asset, or a benchmark result.
- The Google DeepMind `produces` inverse is added without replacing its existing or concurrently added relations.
- Release requirements take precedence over stale prose where sources differ; support, performance, precision, and asset-revision claims remain scoped.
- Reader links and the exact producer inverse resolve after materialization.
