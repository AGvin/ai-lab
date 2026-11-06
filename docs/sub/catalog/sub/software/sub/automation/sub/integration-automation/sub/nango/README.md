# Nango

Nango is a source-available integration runtime for connecting applications and agent tools to third-party APIs with managed OAuth/API-key credentials, authenticated requests and sync workflows.

## Product scope

The platform provides authorization, token refresh, proxying, TypeScript integration functions, synchronization and event/action interfaces. Cloud, BYOC and supported self-hosted deployments are product modes rather than separate catalog identities. Nango is distinct from visual flow builders, a generic OAuth identity provider and managed third-party agent-tool marketplaces.

## Operations and boundaries

Nango's source distribution uses Elastic License 2.0 with use restrictions. Nango Cloud is vendor-operated. For enterprise BYOC, Nango operates the platform in the customer's environment; for Enterprise Self-Managed, the customer operates the deployment.

The free self-hosted edition supports Auth and Proxy with a narrower feature set. It is designed for one trusted organization: separate accounts are not hardened isolation between mutually untrusted users, and account signups are enabled by default.

Enterprise Self-Managed credential encryption depends on a configured encryption key, supplied directly or through KMS. Without a key, credentials remain unencrypted, while persisted-record storage and retrieval fail instead of falling back to plaintext. Connect UI also requires a key.

Provider credentials, OAuth scopes and integration code determine access to external data and write actions. Sync cursors, retries, stored integration state and API compatibility remain part of the selected integration and deployment.

## Relations

- Produced by: [Nango](../../../../../../../producers/sub/n/sub/nango/)

## Official resources

- [Official site](https://nango.dev/)
- [Source repository](https://github.com/NangoHQ/nango)
- [Self-hosting documentation](https://nango.dev/docs/guides/platform/self-hosting/self-hosting)
- [Enterprise BYOC](https://nango.dev/docs/guides/platform/self-hosting/byoc)
- [Enterprise Self-Managed and encryption](https://nango.dev/docs/guides/platform/self-hosting/self-managed#encryption-key)
- [Distribution license](https://github.com/NangoHQ/nango/blob/master/LICENSE)
