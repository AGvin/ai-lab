# Playwright

Playwright is Microsoft's open-source framework for web testing and browser automation. It drives Chromium, Firefox, and WebKit through a common automation model and is represented here as a **Development Testing Tool**.

## Testing and agent boundary

Playwright Test is the end-to-end testing surface; Playwright can also be used as a browser automation library. Current upstream tooling additionally exposes Playwright CLI and MCP surfaces for coding/AI agents. Those surfaces let an external agent operate Playwright; they do not turn Playwright into a standalone coding-agent identity.

Test browser contexts are designed for isolation, while explicit integrations can connect to an existing browser/profile and thereby reuse authenticated sessions, cookies, or extensions. Treat browser/session permissions, network access, test credentials, target environments, CI secrets, destructive actions, and existing-profile access as separate trust boundaries.

## Related

- [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/) — canonical producer organization.

## Official resources

- [Playwright](https://playwright.dev/)
- [Playwright Test](https://playwright.dev/docs/intro)
- [Playwright MCP](https://playwright.dev/mcp/installation)
- [Repository](https://github.com/microsoft/playwright)
