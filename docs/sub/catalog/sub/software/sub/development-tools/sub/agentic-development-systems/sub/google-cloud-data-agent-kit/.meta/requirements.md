# Documentation Requirements

## Requirements

- Present Google Cloud Data Agent Kit as Google's generally available installable agent-development/data-work toolkit that connects existing coding agents to Google Data Cloud through MCP tools, Google-authored Agent Skills, an IDE extension, and agent-plugin packaging.
- Preserve the product boundary separately from Google Agent Development Kit (ADK), Google Agents CLI, Google Antigravity, the generic Google Skills collection, Google Cloud CLI, and the individual BigQuery/Spanner/AlloyDB/Bigtable/Spark/Airflow services it accesses.
- Keep the bundled skills and MCP servers as components of Data Agent Kit rather than automatically creating one peer catalog identity per skill, tool, or supported data service.
- Preserve its user-permission boundary: tools operate with the authenticated user's or impersonated service account's Google Cloud IAM permissions; do not imply unrestricted access merely because the plugin is installed.
- Treat supported services, plugin/IDE clients, installation commands, bundled skill inventory, MCP tools, telemetry behavior, IAM/security controls, extension features, and Cloud Shell/Workstations preinstallation state as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Data Agent Kit remains an installable agent-development/data toolkit rather than a hosted agent service.
- It is not conflated with Google ADK despite the similar abbreviation.
- Bundled skills/MCP tools are not duplicated as peer entities without independent lifecycle evidence.
- Producer provenance resolves bidirectionally to Google.
