# Documentation Requirements

## Requirements

- Identify MCP Toolbox for Databases as the separately runnable open-source MCP server and custom database-tool framework published from `googleapis/mcp-toolbox`. Its original project/repository name `genai-toolbox` is a historical alias, not a second software product.
- Place the server under Application Development because its primary purpose is exposing database-backed tools to AI applications and MCP clients. Do not classify it as a database storage engine, a hosted-only MCP service, or the full Google Cloud managed database product family.
- Preserve Google Cloud as the producer organization using official Google Cloud launch coverage, with one `produced-by` relation and its reciprocal `produces` relation. Google Cloud's operated managed MCP servers have a separate lifecycle and are not instances of the self-hosted Toolbox software identity.
- Distinguish Toolbox's prebuilt database-specific toolsets (`--prebuilt`), custom configuration with `tools.yaml` sources and tools, and separately released language SDKs. The project server is a single software entity; do not create duplicate entities for each database adapter, config file, original repository name, or SDK integration.
- Describe the source-reviewed `npx @toolbox-sdk/server --config tools.yaml` orientation and the prebuilt `--prebuilt=postgres` option; versions and compatibility depend on the chosen release and database adapters. Do not claim that a full MCP deployment, DB connection, query or integration test has been executed.
- Record first-party source commit `b9b96ba4c31012db51024dd7ddabf1bd83aa18d7` dated 2026-11-03. Treat mutable database-support claims, CLI options and library versions as bound to this source snapshot. Pin releases/images, adapters and client protocol versions for reproducible deployments.
- Preserve Apache-2.0 open-source licensing for the project's repository. This does not grant redistribution rights for third-party databases, credentials, user data, vendor API connectors, or external SDK dependencies.
- Explain the trust boundary: read/schema tools and generic SQL tools are not inherently safe in an authorized environment; `execute_sql` or custom tools may reveal information or mutate data. Use least-privilege database roles (read-only when appropriate), explicit SQL/tool allowlists, network isolation, authentication, credential vaulting, query timeouts and observability.
- Do not embed production database passwords in example `tools.yaml`; use environment variables or secret management. Avoid public MCP exposure or unrestricted database credentials and do not imply that supported OIDC/OAuth/IAM mechanisms auto-secure every deployment.
- Keep Google Cloud and non-Google database integrations conceptually separate, with no assumption that a Google Cloud account is needed for local/self-managed resources. Google Cloud managed MCP servers remain a distinct service option.
- Provide official source links for project identity, documentation, license, and Google Cloud provenance, with explicit distinctions between facts checked from source and unexecuted runtime claims.

## Validation

- [Pinned upstream README](https://github.com/googleapis/mcp-toolbox/blob/b9b96ba4c31012db51024dd7ddabf1bd83aa18d7/README.md) supports the software's source identity, repository rename, prebuilt and custom tool operation, and database use cases; [pinned license](https://github.com/googleapis/mcp-toolbox/blob/b9b96ba4c31012db51024dd7ddabf1bd83aa18d7/LICENSE) confirms Apache-2.0.
- [Google Cloud's announcement](https://cloud.google.com/blog/products/ai-machine-learning/mcp-toolbox-for-databases-now-supports-model-context-protocol) supports the producer provenance; [upstream FAQ](https://mcp-toolbox.dev/dev/reference/faq/) distinguishes self-hosted Toolbox from managed MCP servers.
- The canonical producer relation resolves in both directions; Application Development indexes the materialized child once and all reader links resolve.
- The profile does not claim successful runtime database tests, full CI, a full freshness audit, or full-catalog clean-pass credit.
