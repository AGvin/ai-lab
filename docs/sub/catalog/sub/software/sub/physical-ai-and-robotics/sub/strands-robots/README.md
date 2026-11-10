# Strands Robots

Strands Robots is an installable open-source robotics library that connects Strands Agents to simulated and physical robots through a common `Robot()` interface. Its documented workflows cover simulation, hardware control, policy backends, recording and training, mesh or fleet coordination, and ROS 2 integration.

## Operation and scope

State-changing robot operations use a conditional consent gate. Configured allowlists can pre-approve tools, and explicit `BYPASS_TOOL_CONSENT` can bypass interactive consent. Otherwise, an out-of-band operator interrupt requests approval; the operation fails closed when no operator is available. Reads and stops remain ungated.

Strands Agents supplies the separate agent framework. Integrated robot hardware, policy or VLA models, datasets, and cloud services retain their own identities. The archived Strands Robots Sim project was folded into Strands Robots, so simulation is part of this library's current scope.

## Provenance

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [Strands Robots repository](https://github.com/strands-labs/robots)
- [Strands Robots documentation](https://strands-labs.github.io/robots/)
- [Robot-operation security](https://strands-labs.github.io/robots/learn/security/)
- [Introducing Strands Labs](https://strandsagents.com/blog/introducing-strands-labs/)
- [AWS August 2026 builder roundup](https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-august-2026/)
