# Documentation Requirements

## Requirements

- Identify Runpod, Inc. as the producer/operator organization behind the Runpod infrastructure service.
- Preserve the legal company form only as supported by current official Runpod legal documents; do not generalize unrelated subsidiaries, partners, data-center operators, or marketplace hosts into the producer identity.
- Keep the producer profile distinct from the Runpod service and from third-party compute providers participating in Community Cloud or marketplace capacity.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep funding, headcount, customer counts, hardware inventory, data-center partner lists, and other mutable company details outside this concise producer profile unless materially relevant to represented catalog entities.
- Include the current official site and legal identity source from canonical entity metadata.

## Validation

- The page distinguishes Runpod, Inc. from the Runpod hosted service and from third-party infrastructure suppliers.
- The `produces` relation resolves to Runpod and is matched by Runpod's inverse `produced-by` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Runpod, Inc. is the service operator identified in Runpod's terms updated March 24, 2026. Its platform offers compute and related infrastructure through product surfaces such as Pods and Serverless. The company record remains distinct from the Runpod service and from third-party capacity suppliers participating in its marketplace. [Terms](https://www.runpod.io/legal/terms-of-service) · [Platform overview](https://docs.runpod.io/overview).

Choose the compute surface and storage arrangement for the workload, then assess region, instance lifecycle, access policy and the model or container you intend to run. Marketplace participation does not establish that Runpod owns every underlying machine, and renting compute does not license customer-supplied model weights or software. [Terms](https://www.runpod.io/legal/terms-of-service) · [Platform overview](https://docs.runpod.io/overview).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
