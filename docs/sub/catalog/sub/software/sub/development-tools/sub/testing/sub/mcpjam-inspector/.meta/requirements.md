# Documentation Requirements

## Requirements

- Identify MCPJam Inspector as the released third-party MCP server/client testing and debugging product `@mcpjam/inspector`, distinct from the official MCP Inspector, A2A Inspector and vulnerability scanners.
- Preserve the first-party **v3.16.0 (2026-10-13)** non-prerelease boundary; its published Inspector package requires Node.js >=22 for the terminal launcher. Hosted web, local CLI, desktop and source-built Docker modes are delivery options for one product, not separate canonical software identities.
- Describe tool/prompt/resource and JSON-RPC inspection, OAuth diagnostics, client behavior simulation, MCP app/widget debugging and available CLI/SDK/CI evaluation workflows without claiming these amount to formal security certification.
- **Licensing:** the root repository LICENSE grants Apache-2.0 for ordinary code but explicitly excludes designated evaluation/server files governed by the separate MCPJam Enterprise Edition license at `mcpjam-inspector/server/evals/LICENSE`; production EE evaluation usage requires a subscription. Do not label the entire evaluation stack uniformly open source or imply every hosted feature is free.
- **Security:** local inspection can handle server credentials, OAuth flows, tool arguments and model transcripts. Keep local interfaces bound to trusted hosts, protect the launcher session URL, verify any cloud/evaluation data-sharing terms and avoid exposing tokens in telemetry or logs.
- Record MCPJam Inc as the publisher with exact `produced-by` / `produces` reciprocity. Do not duplicate the separate hosted app, terminal launcher, CLI, SDK, or paid feature gates as product peers.

## Validation

- Official MCPJam release metadata, package manifest and README support version, Node engine, distribution modes and scope.
- First-party root LICENSE and the separate enterprise license support the mixed license/production boundary.
- Software relation has an exact inverse in `catalog/producers/m/mcpjam`.
