# Documentation Requirements

## Requirements

- Identify Qdrant as the producer identity for Qdrant products represented in the catalog.
- Keep managed Qdrant Cloud distinct from self-managed Qdrant software when both identities are represented.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- `produces` is the inverse of Qdrant Managed Cloud `produced-by`.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Qdrant is the publishing and service brand behind the represented Qdrant Cloud offering. The official legal imprint identifies Qdrant Solutions GmbH, while the cloud documentation describes managed clusters and API access. This brand profile complements the existing legal-name producer profile used for the Qdrant engine. [Company imprint](https://qdrant.tech/legal/impressum/) · [Qdrant Cloud](https://qdrant.tech/documentation/cloud/).

Choose managed Cloud when the vendor-operated cluster and its service agreement match the workload. Confirm deployment location, account permissions and authentication before ingesting application data. The underlying Apache-2.0 engine can also be self-managed, but its license does not establish the terms, retention or availability of a paid cloud deployment. [Cloud documentation](https://qdrant.tech/documentation/cloud/) · [Engine repository](https://github.com/qdrant/qdrant).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
