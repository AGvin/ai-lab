# Documentation Requirements

## Requirements

- Present SpaceXAI Collections as SpaceXAI's managed persistent document-collection, embedding-index, and search/retrieval service for RAG and enterprise/internal knowledge-base workflows.
- Preserve its independent managed data-infrastructure boundary: users can create/manage persistent collections and documents, configure chunking/index behavior, attach metadata, and query collection content through semantic, keyword, or hybrid retrieval.
- Keep ordinary Files/message attachments, Grok model identities, the general inference/Responses API, agent tools, and external vector databases separate from the Collections service identity.
- Keep `grok-embedding-small` as a mutable collection-index implementation/model setting unless SpaceXAI establishes it as an independently documented public trained-model identity.
- Treat supported file types, file-size and account limits, embedding/index configuration, metadata/filter syntax, search modes, API endpoints, management-key permissions, pricing/credits, retention/privacy behavior, and quotas as freshness-sensitive.
- Preserve the current split between management-key collection administration and API-key collection search only while first-party documentation supports it.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Collections remains managed persistent vector/search data infrastructure rather than a generic chat-file feature.
- Internal/index model names are not promoted automatically to trained-model nodes.
- Producer provenance resolves bidirectionally to SpaceXAI.

## Scoped original-source qualification — 2026-11-07

- SpaceXAI Collections is the managed persistent file/collection embedding-index and retrieval service in the xAI API ecosystem. The first-party Collections guide explicitly distinguishes persisted cross-document search from ephemeral per-message file attachments; an internal embedding/index setting is not a separate trained model release.
- Collections support configurable chunking/embeddings, metadata, multi-collection semantic search and account-credit-gated file uploads. Dedicated Collections REST docs distinguish administrative routes on management-api.x.ai with Management API keys from search on api.x.ai with API keys. The publisher asserts Collections data are not used for training, which is not an independent contractual, privacy or retention audit.
- Verified first-party source 1: https://docs.x.ai/developers/files/collections
- Verified first-party source 2: https://docs.x.ai/developers/files/collections/api
- Verified first-party source 3: https://docs.x.ai/developers/rest-api-reference/collections
- Existing managed-data-service source/identity accepted only; no API account or credit use, upload, real search, private data handling, independent security or full-repository clean/final gate. The vector-search parent index currently omits this reader link; no navigation-repair credit.
