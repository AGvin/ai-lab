# Cohere Model Vault

Cohere Model Vault is Cohere's managed **dedicated, single-tenant inference deployment** offering. Organizations provision supported model capacity on isolated managed infrastructure and invoke it through Cohere-compatible APIs without managing the serving stack themselves. [Model Vault overview](https://docs.cohere.com/docs/model-vault).

## Hosting and security boundaries

Standard Vault and Encrypted Vault are deployment/security configurations of the same service, not automatically independent canonical products. Confidential-computing and remote-attestation assertions apply to supported **Encrypted Vault** hardware and configurations, not to every deployment. Single tenancy does not alone establish independently audited confidentiality, universal retention guarantees or zero-trust security.

Model Vault is distinct from the public shared Cohere Platform SaaS API, customer-operated on-premises installations, Cohere North workspace and the underlying Cohere model families. A supported third-party model hosted in a Vault keeps its original producer identity. [Deployment options](https://docs.cohere.com/docs/welcome).

## Operational boundaries

Verify current supported models, versions, GPUs, deployment geographies, quota/capacity availability, isolation configuration, encryption/attestation support, authentication, retention, billing and scaling. Use the actual tenant/environment contract for regulated data rather than inferring protections from the product name.

## Relations

- Produced by [Cohere](../../../../../producers/sub/c/sub/cohere/).

## Official resources

- [Model Vault documentation](https://docs.cohere.com/docs/model-vault)
- [Encrypted Vault](https://docs.cohere.com/docs/model-vault/encrypted)
- [Supported Standard Vault models](https://docs.cohere.com/docs/model-vault/standard/supported-models)
