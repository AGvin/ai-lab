# Documentation Requirements

## Requirements

- Identify NVIDIA AI Cluster Runtime (AICR) as NVIDIA's released open-source developer/operations automation software for generating version-locked, validated GPU-accelerated Kubernetes runtime configurations.
- Preserve the current stable v1.x compatibility boundary across the public CLI, REST API, Go SDK, bundle layout, and artifact schemas only while supported by current upstream release policy.
- Preserve AICR's primary identity as a configuration/validation generator: snapshot, recipe, bundle, validation, signed provenance/evidence, and deployment-artifact generation are one software product rather than separate peer tools.
- Keep AICR distinct from Kubernetes, Helm, Argo CD, Flux, Helmfile, GPU Operator, NIM, Dynamo, Kubeflow, Slurm, cloud/OEM cluster platforms, and the hardware accelerators described by recipes.
- Preserve the upstream boundary that AICR is not a cluster provisioner, lifecycle-management platform, managed control plane, or generic configuration-management system.
- Treat supported Kubernetes services, accelerators, operating systems, components, workload intents, deployment backends, recipe inventory, compatibility matrices, evidence status, packaging, and release versions as freshness-sensitive.
- Treat signed provenance/validation evidence as evidence about published artifacts and tested configurations, not proof that a deployment is secure, suitable, or correct for an untested environment.
- Preserve NVIDIA producer provenance.

## Validation

- AICR remains developer/operations automation software rather than a managed service or hardware identity.
- Recipe/component inventory is not frozen from one release snapshot.
- Signed evidence is not generalized beyond the exact tested recipe/hardware/software configuration.
- Producer provenance resolves bidirectionally.
