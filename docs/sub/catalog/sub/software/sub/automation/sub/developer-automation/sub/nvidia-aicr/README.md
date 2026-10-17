# NVIDIA AI Cluster Runtime (AICR)

NVIDIA AI Cluster Runtime (AICR) is open-source developer and operations automation software for generating version-locked and verifiable configurations for GPU-accelerated Kubernetes clusters.

## Product scope

AICR provides configuration snapshots, recipes, bundles, validation and evidence/provenance artifacts through supported CLI, REST and Go SDK surfaces. It is a configuration and validation generator; it does not itself provision clusters, manage an entire deployment lifecycle, replace Kubernetes/Helm/Argo CD or operate as a cloud control plane.

## Operations and boundaries

Check the selected version's recipe inventory, accelerator and component compatibility, bundle formats and supported environments. Signed evidence establishes provenance or validation for specified artifacts and tested configurations, not universal deployment security or production suitability. Treat release availability, platform support and recipe compatibility as version-dependent.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Source repository](https://github.com/NVIDIA/aicr)
- [AICR overview](https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration/)
