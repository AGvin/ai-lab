# Documentation Requirements

## Requirements

- Identify Playwright MCP as Microsoft's separately distributed `@playwright/mcp` npm package and independently runnable Model Context Protocol server for browser automation through Playwright. Keep it distinct from the Playwright Test framework, core Playwright browser library, and separately released Playwright CLI.
- Preserve the existing Microsoft canonical producer identity, with reciprocal `produced-by` and `produces` relations. Do not make a second manufacturer or equate an MCP client, the browser, and the server into one product identity.
- Describe accessibility-snapshot-based browser tools and the role of an MCP client; distinguish structured DOM/accessibility interaction from optional vision/PDF/devtools capabilities. The server is neither an LLM nor a hosted browser service.
- Use the inspected source commit `ec572ee8354015293bed67145db21eed386e876d` (2026-11-01), whose `package.json` declares `@playwright/mcp` version `0.0.84`, Node.js >=18 and Apache-2.0 licensing. Treat these as pinned source-manifest facts rather than an assertion about today's latest package or global runtime compatibility.
- Include a bounded orientation to configuration with `npx @playwright/mcp` through a compatible MCP client; for reproducible installation use a pinned release rather than `@latest`. Browser support, launch options, and remote dependencies can vary by environment. Do not claim tests or browser sessions have been executed.
- Distinguish isolated, persistent and existing-browser extension modes: persistent profiles and storage-state files may retain authentication; extension mode may expose an already logged-in browser. Explain explicit browser/session authorization and safe handling of cookies, secrets, and test environments.
- Explain that Playwright MCP and browser-origin restrictions are not a security boundary; official documentation warns that `allowed-origins` and `blocked-origins` cannot enforce redirect-level isolation. Use client-side approvals, least privilege, network restrictions and isolated test profiles for untrusted pages.
- Respect target-site permissions and avoid production-impacting browser actions without explicit authorization. Browser tools can read content, submit forms, navigate to external sites and expose sensitive data; use controlled accounts, audit requests and budget resource use.
- Keep software license separate from browser binaries, site content, external MCP clients, and third-party data rights. Do not duplicate Playwright's core entry as another MCP software identity.
- Provide official first-party references pinned to the inspected source for the project, package manifest, and license; indicate that current operational support is subject to source-specific updates.

## Validation

- First-party [README](https://github.com/microsoft/playwright-mcp/blob/ec572ee8354015293bed67145db21eed386e876d/README.md), [package manifest](https://github.com/microsoft/playwright-mcp/blob/ec572ee8354015293bed67145db21eed386e876d/package.json), and [Apache-2.0 license](https://github.com/microsoft/playwright-mcp/blob/ec572ee8354015293bed67145db21eed386e876d/LICENSE) establish the product identity, runtime floor and licensing at the pinned source.
- Canonical metadata has one `produced-by` relation to Microsoft and the existing Microsoft producer has a reciprocal `produces` relation; both resolve to materialized nodes.
- Reader content distinguishes Playwright MCP, Playwright Test and Playwright CLI, provides a practical usage orientation and an actionable browser/session safety boundary, and lists first-party sources.
- Testing Tools index lists this child exactly once, and all updated relative paths resolve against the pinned catalog tree.
- No assertion of full CI, runtime browser execution, a complete freshness audit or a whole-catalog clean pass unless independently verified.
