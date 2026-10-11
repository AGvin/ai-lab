# Documentation Requirements

## Requirements

- Identify Shopify Agent Skills as the released, first-party maintained/generated collection of portable skills for AI coding agents working with Shopify development APIs, schemas, themes, functions, UI extension components, Storefront/Customer GraphQL and Hydrogen.
- Preserve the collection's independent repository and distribution identity. Currently bundled skill directories such as `shopify-admin`, `shopify-functions`, `shopify-storefront-graphql`, `shopify-liquid` and `shopify-polaris-checkout-extensions` remain first-party collection content, not peer catalog entities merely because they are independently selectable.
- The official repository explicitly identifies itself as **generated upstream**, with prepackaged documentation-search and validation scripts; keep current original upstream source and generated distribution boundaries clear. An API-specific `config.json` convention for Shopify-owned skills is not a universal Agent Skills format requirement.
- Distinguish AI instruction packages from Shopify's commerce services, GraphQL API operation catalogs, Liquid templates, SDKs, checkout extensions and payment/provider integrations. Their installation and store permissions are separate.
- Supported coding agent clients, installation commands (`npx skill` versus `npx skills`), schema revisions, skill inventory, validation scripts and prompts are mutable. Do not assume the skill validation can replace live API/schema or app permissions.
- Preserve reciprocal Shopify producer provenance.

## Validation

- First-party ownership and current source repository match the canonical collection.
- No individual generated skill folder or Shopify API is duplicated as a separate collection solely for enumeration.
- Current client support and runtime security are verified separately from a package's claimed portability.
- The `produced-by` relation is inverted by producer `produces`.
