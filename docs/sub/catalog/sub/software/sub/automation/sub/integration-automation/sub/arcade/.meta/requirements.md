# Documentation Requirements

## Requirements

- Identify Arcade as an enterprise tool/action execution runtime and governance platform for agents and MCP clients: authorized tool calling, per-user OAuth handling, token/scopes, MCP gateways, policy/audit and hosted tool execution across third-party applications.
- Preserve one **Arcade platform** product identity across Arcade Cloud, vendor-operated cloud marketplace installs and vendor-supported full self-host Helm deployments. The first-party deployment documentation distinguishes those full platform modes from an Arcade Deploy tool-server workflow and hybrid MCP servers; neither subordinate feature is a second platform.
- Classify under integration automation software because the platform is deployable into a customer's own Kubernetes cluster via documented Helm chart (OIDC, PostgreSQL/Redis, workers, gateways and RBAC). Do not imply the entire proprietary commercial platform code is licensed under the same MIT terms as its publicly released SDK/framework.
- Keep the separately maintained open-source `Arcade MCP` server development framework as a distinct software identity because it is an installable, MIT-licensed library for authoring MCP tool servers, not the full OAuth/policy/runtime control plane.
- Auth must be scoped to the actual end user; do not hand the LLM raw OAuth tokens, grant broad reusable scopes, or assume a connected service authorizes arbitrary write actions. Audit permissions and human approval on mutating operations.
- Treat integrated-tool count, hosted plan availability, marketplace availability, chart/API version, quotas, OAuth vendor coverage and feature licensing as release-sensitive. Keep integrated third-party tool/connector authors separate from the canonical Arcade publisher.

## Validation

- First-party published documentation and/or repository demonstrates an existing usable product, with install/deployment boundary correctly distinguished.
- Exact reciprocal producer relation resolves to one canonical organization rather than any evaluated integration/tool provider.
- Source-available/managed feature and licensing claims are versioned, never silently generalized.
