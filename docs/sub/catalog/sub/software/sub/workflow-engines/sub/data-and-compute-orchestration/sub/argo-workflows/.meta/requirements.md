# Documentation Requirements

## Requirements

- Identify Argo Workflows as an open-source, container-native workflow engine for orchestrating parallel jobs on Kubernetes through Kubernetes custom resources.
- Preserve its primary placement under `workflow-engines/data-and-compute-orchestration`; ML/data processing, batch, infrastructure automation, and CI/CD are use cases of the same Kubernetes workflow engine.
- Preserve Applatix as the origin producer while keeping later Intuit involvement and current CNCF governance distinct from origin provenance.
- Preserve the distinction between Argo Workflows and other Argo projects such as Argo CD.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep CRD/API versions, artifact stores, executor behavior, Kubernetes support, governance details, and other mutable implementation details source-backed when expanded.
- Include current official Argo Workflows documentation, repository, and authoritative CNCF project-history references.

## Validation

- The page identifies Argo Workflows specifically rather than the broader Argo project family.
- Applatix origin, Intuit contribution history, and current CNCF governance are not conflated.
- Kubernetes/container-native execution remains explicit.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
