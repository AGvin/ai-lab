# MCP Enterprise-Managed Authorization

**MCP Enterprise-Managed Authorization (EMA)** is the official optional stable Model Context Protocol authorization extension identified by `io.modelcontextprotocol/enterprise-managed-authorization`. It defines a protocol-specific enterprise authorization profile, distinct from ordinary core MCP OAuth flows and from the separate underlying Identity Assertion JWT Authorization Grant standardization work. [Stable EMA specification](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/stable/enterprise-managed-authorization.mdx).

## Authorization and trust boundary

An enterprise identity provider (IdP) governs the organization's access policy. An MCP client obtains an Identity Assertion JWT Authorization Grant (ID-JAG), and the MCP authorization server validates that grant before issuing a scoped access token for the MCP resource. The IdP policy and the resource-server authorization contract remain separate from a client application's tool intentions.

Exact grant parameters, audience binding, JWT claims, metadata/discovery, account linking, OAuth exchange, revocation and capability negotiation are governed by the active stable extension revision. This page does not duplicate the IETF ID-JAG draft as a separate established MCP standard.

## Security and implementation limits

Extension compatibility does not grant default access to enterprise connectors or bypass tenant consent, access restrictions or audit requirements. IdP trust configuration, token storage, replay controls, delegated permissions and real product interoperability must be validated for the actual environment. A vendor's support statement is not independent security certification.

## Official resources

- [MCP Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)
- [Stable EMA specification](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/stable/enterprise-managed-authorization.mdx)
- [MCP authorization extension repository](https://github.com/modelcontextprotocol/ext-auth)
