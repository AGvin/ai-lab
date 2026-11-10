# Documentation Requirements

## Requirements

- Identify Nebius as the company operating AI cloud and managed inference; distinguish the organization from its hosted developer API and third-party models.
- Preserve the [official November 5, 2025 announcement](https://nebius.com/newsroom/nebius-launches-nebius-token-factory-to-deliver-production-ai-inference-at-scale) establishing **Nebius Token Factory** as the successor of Nebius AI Studio. Keep the frozen canonical API slug `nebius-ai-studio` while showing the current product name, rather than counting the previous brand as a second service.
- Use reciprocal `produces` / `produced-by` links to the single service entity. Do not infer that Nebius originally developed each model available through its catalog or that GPU cloud compute is included with hosted inference API access.
- Differentiate token-based hosted requests, dedicated deployments and supported post-training from unrelated Nebius infrastructure. Service/API access, model catalog, pricing, quotas, SLA, regional availability and data-processing terms are mutable and contract dependent.
- Protect credentials, customer prompts and fine-tuning data; verify model licenses and upstream terms before redistribution or deployment. A provider's serving role does not transfer ownership of third-party weights.
- Cite official company, announcement and product documentation. No actual API request, model execution, model benchmark, customer deployment, comprehensive privacy/license audit, full CI or whole-catalog clean pass is claimed.

## Validation

- Producer N index lists the identity exactly once, the API service reader exists, and the two entity relationship directions match.
- The historical/current naming and one frozen service identity are explicit.
