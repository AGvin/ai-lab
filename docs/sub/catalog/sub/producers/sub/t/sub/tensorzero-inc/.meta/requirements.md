# Documentation Requirements

## Requirements

- Identify TensorZero, Inc. as the first-party named company that produced the represented software, separately from the product and any hosted service.
- Preserve the following source-limited lifecycle boundary: As checked on October 17, 2026, the official TensorZero website states that the software is no longer maintained, while its code remains available on GitHub and the first-party repository is archived. Historical product provenance and enterprise terms do not establish current upstream updates, security fixes, support or a hosted service. This software lifecycle evidence does not establish the company's legal dissolution.
- Render the standard `entity-relations` block from validated current-entity relations.
- Include official company terms, the software repository and the lifecycle announcement or statement. Do not invent a shutdown date, successor, legal status or support commitment.

## Validation

- `produces` resolves exactly to `catalog/software/gateways/model-gateways/tensorzero` and reciprocal `produced-by` resolves to `catalog/producers/t/tensorzero-inc`.
- Company identity, historical production, current maintenance and service operation are not conflated.
- The relation block matches validated canonical relations and every destination resolves.
