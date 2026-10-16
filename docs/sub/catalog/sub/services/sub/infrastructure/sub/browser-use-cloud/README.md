# Browser Use Cloud

Browser Use Cloud is the **fully hosted** Browser Use service for API-driven remote browser-agent tasks. The provider runs both agent and browser sessions, offering task results, live inspection and account-based billing.

## Service boundary

This managed agent execution service is separate from the [Browser Use open-source Python framework](../../../../../software/sub/agent-frameworks/sub/browser-use/), locally managed browser servers and raw hosted-browser infrastructure such as Browserbase or Cloudflare Browser Rendering.

First-party documentation describes authenticated session/task creation, asynchronous task-status/result retrieval and browser profile/SDK interfaces. API v3 and older v2 examples have different API lifecycles; pin the supported API version for each integration.

## Security and operations

Use API-key authentication, protect persistent profiles, and review permissions, session lifetimes, proxy/network configuration, region availability and data retention. Pricing, quotas, model/provider choices, concurrency and SLAs are time-sensitive and must be checked against current Cloud terms. Hosted automation does not establish permission to access external websites.

## Relations

- Produced by: [Browser Use](../../../../../producers/sub/b/sub/browser-use/)

## Official resources

- [Cloud console](https://cloud.browser-use.com/)
- [API documentation](https://docs.browser-use.com/api-reference/api-v1/get-browser-use-version)
