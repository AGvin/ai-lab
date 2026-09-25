# Documentation Requirements

## Requirements

- Present Gretel Platform as the synthetic-data platform currently owned by NVIDIA, centered on generating, transforming, evaluating, and operationalizing privacy-aware synthetic data for AI/ML workflows.
- Preserve its service/control-plane boundary: Gretel Cloud is fully managed, while Gretel Hybrid runs the data plane in customer-controlled Kubernetes on AWS, Azure, or GCP but continues to use Gretel control-plane APIs for scheduling and metadata.
- Keep Gretel Data Designer, Safe Synthetics, Navigator, Evaluate, Workflows, connectors, SDK/CLI surfaces, and model suites as platform capabilities/product surfaces unless current upstream establishes independently durable peer identities.
- Preserve NVIDIA acquisition provenance from 2025 without rewriting historical Gretel product authorship.
- Treat deployment modes, current product/module names, supported clouds/connectors, models, privacy controls, and API behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Gretel remains data-generation/curation-first rather than generic MLOps or analytics.
- Hybrid deployment is not misreported as fully standalone self-managed software because current control-plane coordination remains part of the product.
- Producer provenance resolves bidirectionally to NVIDIA.
