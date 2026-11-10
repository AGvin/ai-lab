# Documentation Requirements

## Requirements

- Identify Pinecone as the producer identity for the Pinecone managed vector/search service.
- Keep producer identity distinct from the service entity and from third-party model/integration providers used through Pinecone.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- `produces` is the inverse of Pinecone service `produced-by`.
- Producer references are current first-party sources.

## Source-backed identity and operating scope

The reader must preserve the following boundaries and their source basis.

Pinecone is the producer and operator of the represented Pinecone managed search service. Its documentation describes indexes supporting dense, sparse and full-text retrieval for AI applications. The company identity remains separate from the service, its client libraries and external embedding-model providers. [Product overview](https://docs.pinecone.io/guides/get-started/overview).

Choose the index and deployment arrangement according to the retrieval workload, then check the account's region, access controls and applicable data terms. A client SDK running in an application does not make the managed index local, and use of an embedding model through an integration does not establish Pinecone authorship or licensing of that model. [Product overview](https://docs.pinecone.io/guides/get-started/overview).

## Reader projection

- Render every non-hidden current-entity relation in its semantic group, ordered by explicit order, canonical target display name and target ID. Preserve source/contributor, organizational and product distinctions.
- Include the official resources from canonical references as readable links. Navigation to a related catalog entry must resolve to its reader, not to metadata.
- Keep changing version, plan, availability and policy details qualified by the cited source; no general offline, license or privacy guarantee follows from producer attribution.
