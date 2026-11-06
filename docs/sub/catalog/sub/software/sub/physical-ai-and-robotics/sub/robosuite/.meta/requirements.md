# Documentation Requirements

## Requirements

- Present robosuite as an independently released MuJoCo-powered simulation framework and benchmark-environment suite for robot learning, owned by Physical AI and Robotics.
- Keep configurable robots/arenas/objects, simulation tasks, controllers, sensors, teleoperation, human demonstration recording/replay, and renderer integration within this identity; distinguish robot hardware, collected datasets, optional model packages, and learning frameworks such as robomimic.
- Ground released lifecycle in v1.5.2, published 2025-12-24, corroborated by the PyPI distribution and its source provenance. Do not substitute the website's v1.5 feature summary for the precise released package record.
- Explain robot/controller/observation configuration as part of the learning task. Action dimensions and meaning depend on the robot's composite and part controllers, control mode, reference frame, and impedance settings.
- Cover the released dependency boundary: MuJoCo >=3.3.0 and mink==0.0.5 in v1.5.2, with optional dependencies for demonstration tools, Gymnasium wrappers, additional robot models, and USD export. Separate macOS/Linux official support from Windows-specific troubleshooting and renderer requirements.
- Explain the local `demo.hdf5` artifact, its environment/model/state/action metadata, and the distinction between state replay and action playback. The official guide does not guarantee deterministic action playback across machines or platforms and recommends setting recorded states for trajectory reproduction.
- Keep simulation-to-real claims conditional on the actual task, physics/control/sensor model, and evaluation procedure; randomizing visuals, dynamics, and sensors addresses parts of the reality gap without proving safe or universally successful physical deployment.
- Resolve provenance to ARISE Initiative as the project/community producer; distinguish Stanford SVL origin, current multi-institution maintenance, individual package-author metadata, and license holders from a claim of exclusive ownership by one lab or sponsor.
- Preserve the repository's MIT license and its separate MuJoCo-derived-code notice rather than inferring a single license from GitHub's NOASSERTION classifier.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Released robot-learning software identity and concrete task/controller/data workflows substantiate both qualification gates.
- Producer provenance resolves to ARISE Initiative with the exact reciprocal edge.
- Demonstration playback, controller semantics, supported versions, and platform claims remain source- and release-scoped.
- Reader links resolve to the new producer and canonical peer profiles.
