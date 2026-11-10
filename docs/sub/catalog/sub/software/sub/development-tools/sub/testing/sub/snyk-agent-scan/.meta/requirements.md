# Documentation Requirements

## Requirements

- Identify Snyk Agent Scan as an independently published Apache-2.0 local CLI/security evaluation tool for discovering and assessing MCP servers, AI agent harnesses and Agent Skills for prompt injection, tool poisoning, sensitive-data exposure and other configuration risks.
- Preserve publication lineage: originally Invariant Labs `MCP-Scan` research tooling, incorporated into Snyk after Snyk's public June 2025 acquisition of Invariant Labs; the actively maintained official product repository is `snyk/agent-scan`. Do not duplicate historical `mcp-scan` forks or experimental Snyk platform features as separate canonical products.
- Official release **v0.6.8 (2026-09-29)** supports `uvx snyk-agent-scan` or a signed/released standalone binary and requires a Snyk API token. No first-party standalone npm Agent Scan package is published; the older v0.5 issue-code output is slated for deprecation, and v0.6 risk-based CLI output remains experimental/unstable despite enterprise platform integrations.
- **Security**: scanning discovered local MCP stdio configurations may execute their configured commands, and remote MCP checks may make network requests with configured headers. Require explicit consent, command review and disposable sandbox when scanning untrusted sources; do not use `--dangerously-run-mcp-servers` outside reviewed environments.
- Preserve first-party limitation: loopback/private network addresses can be allowed while cloud metadata endpoints are blocked; DNS is re-resolved on connect, leaving a DNS-rebinding window documented upstream. No blanket assertion that server scanning is intrinsically safe or that a clean scan proves absence of vulnerabilities.
- Keep consent, SNYK_TOKEN handling, risk analysis API versions (v0.5 versus v0.6), privacy/data transmission, package/execution mode and signed binary verification explicit. Distinguish from promptfoo, PyRIT, official MCP Inspector and managed Snyk enterprise trust/risk platform.
- Keep Snyk as the current producer while retaining historically sourced Invariant Labs origin; software checks are not ownership over evaluated third-party agent configs.

## Validation

- First-party Snyk repository and dated release support the installed CLI, migration boundary, permission risks and published Apache 2.0 license.
- Exact `produced-by` target is reciprocated by the canonical Snyk `produces` relation.
