# Documentation Requirements

## Requirements

- Identify Helicone, Inc. as the first-party named company that produced the represented software, separately from the product and any hosted service.
- Preserve the following source-limited lifecycle boundary: Helicone's March 3, 2026 announcement reports its acquisition by Mintlify and says the team is joining Mintlify. Helicone services remain live in maintenance mode, including security, model, bug and performance updates. Historical direct production, the acquisition announcement and current service availability are separate facts; do not infer a different software producer or a legal ownership/current-maintainer graph edge.
- Render the standard `entity-relations` block from validated current-entity relations.
- Include official company terms, the software repository and the lifecycle announcement or statement. Do not invent a shutdown date, successor, legal status or support commitment.

## Validation

- `produces` resolves exactly to `catalog/software/gateways/model-gateways/helicone` and reciprocal `produced-by` resolves to `catalog/producers/h/helicone-inc`.
- Company identity, historical production, current maintenance and service operation are not conflated.
- The relation block matches validated canonical relations and every destination resolves.
