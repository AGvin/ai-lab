# Stagehand

[Stagehand](https://github.com/browserbase/stagehand) is Browserbase's open-source, MIT-licensed SDK for AI-assisted browser automation and browser agents. It combines model-directed `act()` actions, `observe()` selectors, and structured `extract()` operations with programmable browser control. Stagehand is a software framework, distinct from the [Browserbase](../../../../../services/sub/infrastructure/sub/browserbase/) managed browser infrastructure service and from Browser Use.

## Execution and lifecycle

Stagehand supports local browser operation as well as integration with provider-hosted browser sessions, and can use independently configured LLM providers. Its TypeScript package is `@browserbasehq/stagehand`; the original repository also publishes a Python SDK. Browserbase [announced Stagehand 4.3](https://www.browserbase.com/changelog/stagehand-4-3) on **2026-10-20**; its source manifest lists version 4.3.0 with Node.js **>=22.18.0**, and the Python package declares **>=3.11**. Recheck current packages, browsers and provider compatibility before deployment. Other repository tools and API/server variants are not additional copies of this SDK identity.

## Trust and operational boundaries

Agent instructions and observed web content can contain prompt injection or misleading controls. Browser profiles, cookies, credentials, page contents, model calls, browser sessions and external actions require explicit privacy, authorization and isolation decisions. Use domain restrictions and scoped model/tool privileges, require human approval for sensitive state changes, and validate extracted results against current UI expectations. A selector-driven login example does not guarantee sensitive data never reaches an external model. MIT source licensing does not cover third-party websites, hosted infrastructure, model-provider charges or external data rights.

## Relations

- Produced by: [Browserbase, Inc.](../../../../../producers/sub/b/sub/browserbase-inc/)
- Complementary hosted infrastructure: [Browserbase](../../../../../services/sub/infrastructure/sub/browserbase/)

## Official resources

- [Stagehand source repository](https://github.com/browserbase/stagehand)
- [Documentation](https://docs.stagehand.dev/)
- [Stagehand 4.3 original release](https://www.browserbase.com/changelog/stagehand-4-3)
- [TypeScript SDK package metadata](https://github.com/browserbase/stagehand/blob/main/packages/sdk-ts/package.json)
- [Python SDK package metadata](https://github.com/browserbase/stagehand/blob/main/packages/sdk-python/pyproject.toml)
