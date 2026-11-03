# Playwright MCP

Playwright MCP is Microsoft's open-source Model Context Protocol (MCP) server for browser automation. It exposes browser actions and structured accessibility snapshots to a compatible MCP client. The separately distributed `@playwright/mcp` package is distinct from the underlying [Playwright](../playwright/) testing framework and the separately offered Playwright CLI.

## How it works

A compatible MCP client can start the local server and use its browser tools to navigate pages, inspect accessibility snapshots and interact with page elements. By default, this workflow does not require a vision model. Optional capabilities can include vision, browser debugging and PDF workflows; availability depends on the server configuration and MCP client.

The upstream configuration uses `npx @playwright/mcp` as the server command. Check the client's MCP configuration contract and the project documentation for supported options. Pin a reviewed package version for repeatable deployments rather than assuming `@latest` remains unchanged. The examined source snapshot at commit `ec572ee8354015293bed67145db21eed386e876d` (2026-11-01) declares `@playwright/mcp` version `0.0.84`, Node.js 18 or newer, and Apache-2.0 licensing. These are source-manifest observations, not a completed local installation or a guarantee of the latest package release.

## Browser access and safety

An isolated browser profile reduces cross-session state sharing, whereas persistent or imported storage state can contain cookies and authenticated sessions. Connecting through the browser extension may expose an already signed-in profile. Use separate authorized browser accounts and least-privilege credentials for automation involving third-party pages, and avoid granting access to personal or production profiles by default.

**Playwright MCP is not a security boundary.** Upstream documentation explicitly cautions that origin allow/block settings do not provide robust isolation, including across redirects. Enforce approvals and permissions in the MCP client, use a controlled execution environment and network policy where necessary, and verify targets before submitting forms, making changes or handling sensitive information.

Automated browsing can contact external hosts, transmit page content and write artifacts or logs. Apply appropriate retention and data-minimization controls. The server's Apache-2.0 license does not grant rights to unrelated website content, browser binaries or private data.

## Relations

- Produced by: [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/)
- Related: [Playwright](../playwright/) — underlying browser automation and end-to-end testing framework, not another name for this MCP server.

## Official resources

- [Playwright MCP repository](https://github.com/microsoft/playwright-mcp)
- [Pinned usage and security guidance](https://github.com/microsoft/playwright-mcp/blob/ec572ee8354015293bed67145db21eed386e876d/README.md)
- [Pinned npm package manifest](https://github.com/microsoft/playwright-mcp/blob/ec572ee8354015293bed67145db21eed386e876d/package.json)
- [Apache-2.0 license](https://github.com/microsoft/playwright-mcp/blob/ec572ee8354015293bed67145db21eed386e876d/LICENSE)
