# Weaviate Database

Weaviate Database is self-managed vector-search infrastructure with an open-source core, used for similarity search, hybrid retrieval and vector-powered applications.

## Scope and capabilities

Its self-managed software can be deployed using supported container and orchestration options, including Docker and Kubernetes. Database indexing, filtering, schema management, integrations, backup and clustering belong to the database's implementation and release capabilities.

## Deployment, evidence and boundaries

The self-managed database must not be conflated with the separately operated Weaviate Cloud service. Check current APIs, security settings, model integration availability, hardware needs and backup support per version. SDKs, optional embedded clients and deployments are not new standalone database identities.

Source outside `wl/` is licensed under BSD-3-Clause. The `wl/` directory contains enterprise code under a separate license, with features enabled by a license key; the core's open-source license does not grant rights to those features. Check the selected release and components when assessing deployment licensing.

## Relations

- Produced by: [Weaviate](../../../../../../../producers/sub/w/sub/weaviate/)

## Official resources

- [Documentation](https://docs.weaviate.io/weaviate)
- [Source repository](https://github.com/weaviate/weaviate)
- [Component licenses](https://github.com/weaviate/weaviate/blob/main/LICENSE)
