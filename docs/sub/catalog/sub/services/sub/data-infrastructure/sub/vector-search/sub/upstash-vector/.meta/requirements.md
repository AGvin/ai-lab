# Documentation Requirements

## Requirements

- Identify Upstash Vector as provider-operated serverless vector storage/indexing and similarity search for retrieval applications. It is different from the Upstash Redis product, hosted model APIs, software-only search engines or raw dataset assets.
- Use official Upstash Vector documentation for vector indexing, REST/SDK operations, similarity functions and metadata filtering. Do not assume every index configuration supports the same metric, embedding-generation path or index dimension.
- Describe namespaces and searchable vector metadata, with index endpoint/token authentication. Keep the index URL, bearer token and customer metadata confidential; avoid publishing secrets from example configurations.
- Explain that storing embeddings is not the same as creating those embeddings. Use of integrated embedding providers, models and API services may entail separate data transfers and charges.
- Pricing, free quotas, fixed-tier limits, dimension caps, supported regions and SLAs are mutable. Cite the [live plan reference](https://upstash.com/pricing/vector) rather than hard-coding unverified price guarantees.
- Recommend least-privilege access, tenant isolation, data-retention/deletion review, backups/export where available, retry/backoff and budget controls. A managed service does not remove operator obligations.
- Do not claim creating an index, issuing a query, benchmarking retrieval quality, verifying vendor compliance or whole-catalog clean pass.

## Validation

- Verify the provider-owned API/product boundary and current documentation sources.
- Maintain a single catalog identity with the correct category link; never equate hosted terms with unrelated SDK or model licenses.
- Do not credit unperformed runtime, whole-site or clean-pass checks.

## Scoped original-source qualification — 2026-11-07

- Upstash Vector is a serverless managed vector index with authenticated REST/SDK access; storing embeddings does not imply their generation, and integrated embeddings are configuration-dependent.
- Publisher documentation: https://upstash.com/docs/vector/overall/getstarted
- Scoped service identity/source boundary only; no authenticated runtime, license/security assurance, whole-repository validation, clean pass or final delivery credit.
