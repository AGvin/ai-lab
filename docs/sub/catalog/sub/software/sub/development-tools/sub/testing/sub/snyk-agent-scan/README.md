# Snyk Agent Scan

Snyk Agent Scan is a released open-source local security assessment CLI for MCP servers, agent environments and Agent Skills.

## Product scope

The project, originally Invariant Labs' MCP-Scan and subsequently maintained by Snyk, assesses configuration risks including tool poisoning, prompt injection and sensitive-data exposure. It is separate from the official MCP Inspector and Snyk's managed enterprise platform.

## Operational boundaries

The canonical released boundary is v0.6.8 (2026-09-29), using `uvx snyk-agent-scan` or signed binaries and a Snyk API token. Scans may execute discovered stdio commands or connect to remote endpoints; obtain consent, review commands and use isolated test environments. Analysis sends agent details, MCP configuration/signatures, tool descriptions and skill content to the Snyk analysis API after secret redaction; review this transfer before scanning private material. The v0.6 risk-based CLI output remains experimental and unsuitable as a fixed production schema. Upstream documents a DNS-rebinding limitation. A clean scan does not prove absence of vulnerabilities.

## Relations

- Produced by: [Snyk](../../../../../../../producers/sub/s/sub/snyk/)

## Official resources

- [First-party reference](https://github.com/snyk/agent-scan)
