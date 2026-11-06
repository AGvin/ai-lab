# NVIDIA OpenShell

NVIDIA OpenShell is an open-source, self-managed control and execution layer for applying runtime policy to autonomous AI-agent workloads.

## Product scope

Its control plane includes gateways, supervisors, sandboxes, compute drivers, policy enforcement and credential routing. These are components of one installable software product, not independent managed services. NemoClaw is a separate agent environment using OpenShell; Claude Code, Codex and other agent harnesses are integrations rather than OpenShell-owned products.

## Operations and boundaries

A declared sandbox or sample configuration is not a complete isolation guarantee. Verify supported drivers and OS/runtime versions, configure least-privilege credentials, audit network and file access, review policy enforcement and log retention, and evaluate releases against current first-party documentation. NVIDIA's broader Open Agent Safety Platform is a reference architecture, not an alias for the OpenShell product.

## Relations

- Produced by: [NVIDIA](../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Official repository](https://github.com/NVIDIA/OpenShell)
- [Runtime policy overview](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/)
