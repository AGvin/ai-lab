# Documentation Requirements

## Requirements

- Present Enterprise-Managed Authorization as the stable official Model Context Protocol authorization extension identified by `io.modelcontextprotocol/enterprise-managed-authorization`.
- Keep it distinct from MCP core authorization and from generic Cross-App Access / ID-JAG standardization work: this node owns the MCP-specific stable profile that applies the Identity Assertion JWT Authorization Grant to enterprise MCP deployments.
- Preserve the central interoperability boundary: an enterprise identity provider is the authoritative policy decision point, the MCP client obtains an ID-JAG from that IdP, and the MCP authorization server validates the grant before issuing an access token for the MCP resource.
- Treat exact OAuth grant parameters, JWT claims, discovery metadata, capability declarations, account-linking behavior, and security requirements as version-sensitive normative state that must be re-checked against the current first-party stable specification.
- Do not duplicate product-specific support matrices, vendor deployment instructions, identity-provider configuration, SDK bugs, or implementation tutorials here; keep those with the applicable software/service/learning owners.
- Do not promote the broader IETF Identity Assertion JWT Authorization Grant draft into a stable standalone specification merely because EMA depends on it; evaluate that artifact independently under the lifecycle gate.

## Validation

- The node is explicitly described as an optional MCP extension rather than MCP core.
- Stable status and normative claims remain traceable to the official Model Context Protocol extension specification.
- XAA / ID-JAG terminology is explained as related underlying identity-flow terminology without collapsing distinct specification ownership.

## Scoped original-source qualification — 2026-11-07

- MCP Enterprise-Managed Authorization is the optional stable MCP authorization extension `io.modelcontextprotocol/enterprise-managed-authorization`, distinct from the general MCP core OAuth authorization framework. An enterprise IdP enforces organization access policy while an MCP client obtains an Identity Assertion JWT Authorization Grant (ID-JAG), which the MCP authorization server validates before issuing an MCP resource access token.
- ID-JAG under the separate identity-standard work is an underlying grant mechanism, not a second canonical MCP extension or universal entitlement. Client/server support, IdP trust configuration, audience binding, token exchange, revocation, delegated authorization and logs require tenant-specific implementation checks; these are not proof of blanket connector access or compliance.
- Verified first-party source 1: https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/stable/enterprise-managed-authorization.mdx
- Verified first-party source 2: https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization
- Verified first-party source 3: https://github.com/modelcontextprotocol/ext-auth
- Existing optional extension identity and primary published source qualified only; no IdP, identity JWT, OAuth exchange, live tenant, independent security/privacy/legal certification, full schema/cache/CI/render, clean pass or final gate. Reader page absent (uncredited).
