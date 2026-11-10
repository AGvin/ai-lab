# Documentation Requirements

## Requirements

- Identify MCP Inspector as the official published developer testing/debugging package `@modelcontextprotocol/inspector` from the Model Context Protocol first-party project, maintained under AAIF governance, distinct from A2A Inspector, third-party MCP scanners, agent frameworks and the MCP specification.
- Preserve the released **v2.11.0 (2026-10-14)** boundary: the one npm package provides Web UI, CLI and TUI via the `mcp-inspector` launcher. The experimental `mcpdo` persistent-connection CLI is another binary bundled within the same v2 package, not another stable independent product.
- Keep the v1-latest maintenance line distinct from current v2, including breaking Node engine/CLI/config differences. v2 development occurs on `v2/main` and milestone releases ship on `main`; pin published npm tag/package and supported protocol revision/transport before reporting test outcomes.
- Cover authenticated server/resource/prompt/tool inspection, request/result schema verification, capability negotiation and diagnostics. Keep Inspector distinct from protocol conformance certification, formal security scanning and independent red-team evaluation.
- **Security**: Inspector handles OAuth tokens, client secrets and stdio environment values. Its current official README warns that systems without an OS keychain may store these in `~/.mcp-inspector/secrets.json` without encryption unless a key is provided. Require trusted machine/runtime, bound interface, reviewed commands and safe secret-store configuration; never casually expose the web Inspector on a public interface.
- **Licensing**: its first-party `LICENSE` states an in-progress project migration from MIT to Apache-2.0; new contributions are Apache-2.0, some historical non-relicensed code remains MIT, and non-specification docs are CC-BY-4.0. Do not describe the entire current repository as uniformly MIT or Apache 2.0.
- Attribute first-party maintainership to the MCP community project under the Agentic AI Foundation, not automatic original authorship or exclusive ownership by every foundation member.

## Validation

- First-party current release metadata confirms v2.11.0 is a non-prerelease published package and confirms Web/CLI/TUI and experimental mcpdo responsibilities.
- Project `LICENSE` and security documentation support mixed transition licensing and secret-storage warning.
- The `maintained-by` link has an exact `maintains` inverse at the existing AAIF producer.
