# Documentation Requirements

## Requirements

- Identify Labelbox as the producer identity for the Labelbox AI data-development platform.
- Keep producer identity separate from the managed service and from external expert/model providers integrated into Labelbox workflows.
- Render the standard `entity-relations` block from validated current-entity relations.
- Keep the organization identity distinct from customer-owned datasets and external labeling/model providers; data storage and access depend on the selected service configuration.

## Validation

- `produces` is the inverse of Labelbox service `produced-by`.
- Producer references are current first-party sources.
