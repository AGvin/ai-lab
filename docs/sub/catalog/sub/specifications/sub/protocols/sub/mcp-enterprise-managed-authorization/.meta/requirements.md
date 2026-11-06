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
