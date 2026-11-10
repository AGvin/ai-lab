# Documentation Requirements

## Requirements

- Identify SkyPilot as the released open-source AI compute orchestration platform for launching, scheduling, scaling, and managing AI jobs/services across Kubernetes, Slurm, on-prem, and multiple clouds.
- Preserve its primary data/compute orchestration identity across task/job-as-code, managed jobs, clusters, services/endpoints, batch, scheduling, autostop, failover, multi-cluster/cloud placement, resource/cost controls, and API-server operation.
- Keep SkyPilot distinct from the underlying cloud/Kubernetes/Slurm providers, inference engines, model servers, model registries, workflow systems that integrate with SkyPilot, and managed infrastructure services.
- Treat supported clouds/clusters, accelerator catalog, scheduler modes, job/service APIs, storage backends, authentication/team features, release versions, cost logic, Helm/Kubernetes deployment, and compatibility as freshness-sensitive.
- Preserve the BYOC/control-boundary distinction: SkyPilot can orchestrate resources inside user infrastructure without making those resources a SkyPilot-hosted cloud service.
- Keep preview/early-access features such as a currently non-GA sandbox surface out of the stable contract until their lifecycle changes.
- Attribute utilization/cost/performance comparisons to SkyPilot or the cited evaluator and preserve exact infrastructure/workload setup.

## Validation

- SkyPilot remains orchestration software rather than a cloud provider or one model-serving engine.
- Preview-only feature identities are not materialized as stable peer products.
- Producer provenance resolves to SkyPilot Team.
