# Documentation Requirements

## Requirements

- Identify Strands Robots as the installable open-source robotics/physical-AI library that connects Strands Agents to simulated and physical robots through a common `Robot()` interface.
- Preserve current support for simulation, physical hardware, policy backends, recording/training, mesh/fleet coordination, ROS 2, and safety gates only within current upstream release/documentation evidence.
- Keep Strands Agents as a separate agent-framework identity and keep concrete robot hardware, VLA models, datasets, policy models, cloud services, and the preview Model Hardware Standard with their own canonical owners.
- Record Amazon Web Services as current producer provenance based on AWS/Strands first-party launch material; do not infer that every Strands Labs contributor or integrated vendor is a co-producer.
- Treat supported robots, drivers, policy providers, optional dependencies, cloud integrations, package compatibility, and security controls as freshness-sensitive release state.
- Do not restore archived Strands Robots Sim as a separate current software identity: upstream states its simulation capability was folded into Strands Robots.

## Validation

- Strands Robots remains a separate physical-AI/robotics software identity rather than a feature of Strands Agents.
- Producer provenance resolves bidirectionally to Amazon Web Services.
- Archived Robots Sim is not materialized as a current peer.
- Integrated models, runtimes, hardware, and standards are not misclassified as parts owned by Strands Robots.
