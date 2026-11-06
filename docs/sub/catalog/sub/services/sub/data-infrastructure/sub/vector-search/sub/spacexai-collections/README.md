# SpaceXAI Collections

SpaceXAI Collections is the managed persistent document-collection and retrieval service produced by SpaceXAI LLC, whose current public name is SpaceXSI. It supports document indexes and search for retrieval-augmented generation and internal knowledge workflows.

## Persistent data and API boundary

Collections maintain documents, chunking/index configuration and metadata, with supported semantic, keyword or hybrid retrieval. Ordinary message attachments, the general inference API and external databases remain distinct. Index implementation names are not automatically separate trained-model identities.

The REST reference updated on 15 October 2026 separates collection administration on `management-api.x.ai` using a Management API key from collection search on `api.x.ai` using an API key. Verify current permissions, file and account limits, supported formats, retention, pricing and index configuration before storing or querying private material.

## Relations

- Produced by: [SpaceXAI LLC](../../../../../../../producers/sub/x/sub/xai/)

## Official resources

- [Collections guide](https://docs.x.ai/developers/files/collections)
- [Collections REST API reference](https://docs.x.ai/developers/rest-api-reference/collections)
- [API base URLs and key types](https://docs.x.ai/developers/rest-api-reference/inference)
