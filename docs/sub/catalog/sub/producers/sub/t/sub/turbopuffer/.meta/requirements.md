# Documentation Requirements

## Requirements

- Identify turbopuffer as the producer identity for the turbopuffer search service.
- Render the standard `entity-relations` block from validated current-entity relations.
- Preserve this source-backed identity and provenance context: turbopuffer is the producer and operator identity represented for the turbopuffer search service. The official architecture describes an API service backed by object storage and a memory/NVMe cache, with shared service operation distinct from customer data and applications.
- Explain the following operating and decision boundary: Verify the selected region, access policy and deployment agreement. The default architecture is multi-tenant; enterprise isolation and bring-your-own-cloud options require their own arrangements. Security documentation distinguishes regional data handling, encryption and contractual controls, so a producer profile or certification claim alone does not establish the controls enabled for a particular account.
- Support the producer context with these first-party sources: <https://turbopuffer.com/docs/architecture>, <https://turbopuffer.com/docs/security>.

## Validation

- `produces` is the inverse of turbopuffer `produced-by`.
