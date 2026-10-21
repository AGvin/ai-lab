# turbopuffer

turbopuffer is the producer and operator identity represented for the turbopuffer search service. The official architecture describes an API service backed by object storage and a memory/NVMe cache, with shared service operation distinct from customer data and applications.

## Operating boundary

Verify the selected region, access policy and deployment agreement. The default architecture is multi-tenant; enterprise isolation and bring-your-own-cloud options require their own arrangements. Security documentation distinguishes regional data handling, encryption and contractual controls, so a producer profile or certification claim alone does not establish the controls enabled for a particular account.

## Relations

- Produces: [turbopuffer](../../../../../services/sub/data-infrastructure/sub/vector-search/sub/turbopuffer/)

## Official resources

- <https://turbopuffer.com/>
- <https://turbopuffer.com/docs/architecture>
- <https://turbopuffer.com/docs/security>
