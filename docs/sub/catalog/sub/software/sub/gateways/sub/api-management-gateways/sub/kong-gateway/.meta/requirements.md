# Documentation Requirements

## Requirements

- Identify Kong Gateway as a cloud-native API gateway and reverse-proxy layer for managing, configuring, securing, and routing API traffic.
- Preserve its primary placement under `gateways/api-management-gateways`.
- Preserve the product boundary introduced by Kong AI Gateway 2.x: legacy AI Gateway plugins and LLM-oriented capabilities inside Kong Gateway 3.x remain extensions of this general API gateway, while the independently versioned Kong AI Gateway 2.x product has its own canonical service identity under `services/gateways/model-gateways/`.
- Preserve Kong Inc. as the product producer while distinguishing open-source/on-premises Kong Gateway software from Konnect and other separately operated Kong services or enterprise control surfaces.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep editions, licensing, plugins, deployment modes, AI-plugin support timelines, version support, and other mutable details source-backed when expanded.
- Include current official Kong Gateway documentation, repository, and company/legal references.

## Validation

- The page presents Kong Gateway as a general API-management gateway and does not treat the independently released Kong AI Gateway 2.x as merely a bundled feature set.
- Software and hosted Konnect boundaries are not conflated.
- Kong Inc. provenance does not imply hosted operation of self-managed gateway deployments.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
