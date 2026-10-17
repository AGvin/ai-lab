# Browser Use

Browser Use is an open-source **MIT-licensed Python browser-agent framework**. Developers run the Python agent against local or provider-hosted browsers with a configured model.

## Execution models

Three first-party operating modes have different owners: a locally operated agent with a local browser; a locally operated agent with a hosted browser; and fully managed [Browser Use Cloud](../../../../../services/sub/infrastructure/sub/browser-use-cloud/) with both agent and browser hosted by the provider. Only the last is the separately cataloged Cloud service.

CLI, browser harnesses, MCP integrations, provider connectors, the BU2 model, and benchmarks are adjacent capabilities or products, not alternate identities of the framework.

## Safety and reproducibility

Pin the Python library, browser binary and CDP client versions, browser profile state, model settings, allowed domains, tool permissions and task timeouts. Current browser control uses CDP; pin Playwright separately if using its optional integration. Session cookies and browser profiles can expose authenticated accounts. Automation does not itself confer permission to access websites. Hosted services, proxies and third-party models have terms/costs independent of the MIT source license.

## Relations

- Produced by: [Browser Use](../../../../../producers/sub/b/sub/browser-use/)

## Official resources

- [Repository](https://github.com/browser-use/browser-use)
- [Documentation](https://docs.browser-use.com/)
