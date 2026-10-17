# Documentation Requirements

## Requirements

- Present Snorkel Flow as Snorkel AI's self-managed enterprise data-development platform for building, labeling, curating, evaluating, and operationalizing training/evaluation data and machine-learning applications.
- Preserve the installable platform boundary: current first-party documentation supports Kubernetes deployment on AWS, Azure, GCP, and private-cloud environments, including customer-operated clusters.
- Keep exported MLflow application deployments, external model-serving infrastructure, Prompt Builder, SDK surfaces, notebooks, datasets, and labeling operators as platform capabilities rather than peer products unless upstream establishes independent durable identities.
- Treat supported Kubernetes versions, cloud infrastructure patterns, SDK APIs, labeling/modeling features, integration support, and release-version behavior as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Snorkel Flow remains dataset/data-development-first rather than generic MLOps or managed data-labeling service.
- Producer provenance resolves bidirectionally to Snorkel AI.
