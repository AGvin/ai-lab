# Documentation Requirements

## Requirements

- Identify Vast.ai as a hosted GPU infrastructure marketplace/service for renting compute capacity and running containerized AI/ML and other GPU workloads.
- Preserve its primary placement under `services/infrastructure/`, alongside comparable hosted compute services such as Runpod rather than under self-managed software or hardware catalogs.
- Explain the marketplace model at a durable level: users search provider offers, select capacity, and create instances from available offers/contracts; pricing and hardware supply are market-driven rather than fixed catalog constants.
- Preserve Vast Serverless as a current service mode/capability for autoscaled workload execution without creating a duplicate canonical service node unless its lifecycle, ownership, or navigation later becomes independently substantial.
- Treat the `vastai` CLI, Python SDK, REST API, templates, volumes, SSH/Jupyter access, and related tooling as management interfaces/supporting capabilities of the Vast.ai service rather than separate canonical products while their primary identity remains platform access.
- Distinguish hosted compute from inference runtime. Vast.ai instances may run arbitrary containers, model servers, notebooks, or applications, but Vast.ai does not become the canonical owner of those runtimes or models.
- Treat GPU models, offer inventory, host verification state, geographic supply, market prices, bandwidth/storage charges, interruptible/on-demand/reserved terms, Serverless behavior, limits, and availability as mutable state that must be source-backed and freshness-scoped when expanded.
- Preserve billing caveats at a source-backed level: total cost can include compute, storage, bandwidth, and related resource charges; do not reduce Vast.ai pricing to one static GPU hourly number or imply that stopping an instance necessarily eliminates every charge.
- Make the provider/marketplace trust boundary visible when operational guidance discusses sensitive workloads. Do not imply that all independent hosts have identical physical security, compliance, networking, or reliability characteristics merely because they are reachable through Vast.ai.
- Treat vendor security, benchmark, performance-per-dollar, or savings claims as first-party evidence unless independently verified.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the official service site, documentation, and legal identity source from canonical entity metadata.

## Validation

- Vast.ai remains a hosted infrastructure service/marketplace rather than inference software, a model API only, or a hardware manufacturer.
- Vast Serverless, CLI, SDK, and API remain capabilities/interfaces rather than unnecessary duplicate canonical entities.
- Marketplace-driven pricing, GPU inventory, host state, limits, and availability are not frozen as timeless facts.
- Provider-host variability is not collapsed into a universal security or reliability guarantee.
- The `produced-by` relation resolves to Vast.ai Inc. and is matched by the producer's inverse `produces` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Scoped original-source qualification — 2026-11-06

- Vast.ai's first-party documentation describes a GPU compute marketplace where independent secure-cloud or community hosts advertise available instance offers, plus a separate Serverless execution mode and supporting templates, CLI, SDK and APIs. Hosting/offer choice is a capability of the marketplace identity, not a second producer or inference-runtime identity.
- Offer prices, GPU availability, geographic location, host trust level, storage/network charges, interruptions and rental types are live marketplace conditions. An advertised low hourly GPU rate is not a complete fixed total cost, and a stopped instance should not be assumed free of persistent storage or other charges.
- Provider-operated marketplace access does not give all independent hosts identical physical/data security or compliance guarantees. Sensitive workloads require host-specific trust, key/data protection, isolation and contractual review.
- Verified first-party source 1: https://docs.vast.ai/guides/get-started
- Verified first-party source 2: https://docs.vast.ai/
- Verified first-party source 3: https://docs.vast.ai/guides/instances/pricing
- Acceptance scope: present hosted infrastructure identity and publisher-documented feature/version boundaries only. No model/runtime execution, complete freshness, independent security/legal review, rights clearance, root-wide schema/cache/CI/render, clean pass, final-delivery or merge credit.
