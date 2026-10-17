# Documentation Requirements

## Requirements

- Identify Browser Use as the first-party MIT-licensed open-source Python agent/browser automation framework that can execute a user-configured browser agent through Chromium-based browsers over Chrome DevTools Protocol (CDP) and user-chosen LLMs. Keep this installable library separate from the independently operated Browser Use Cloud hosted agent/task execution service.
- Preserve three distinct operation modes from first-party FAQ: locally hosted Python agent plus local browser; locally operated Python agent with hosted browser/session; and fully managed Browser Use Cloud API where the provider operates both agent and browser. Only the third is owned by the existing service record.
- Keep optional CLI, browser harness, MCP endpoints, third-party model providers, cloud SDK, model `BU2` and benchmark examples as distinct product/model/support surfaces; do not duplicate this framework merely because a cloud plan exists or presume every accessory is packaged in this repo.
- Pin Python library version, browser binary and CDP client version; pin Playwright separately only when the selected integration uses it, Chrome profile/cookie state, model settings, tool definitions, domain/permission boundaries, login credential policy, task timeout and evaluation metrics. Browser reuse can expose authenticated sites; treat profiles/cookies as secrets.
- The MIT license covers the published library, not model inference, premium stealth/proxy service, hosted browser sessions, or third-party task outcomes; their costs and terms can differ. CAPTCHA bypass claims do not confer website access authorization or success guarantees.
- Maintain the same Browser Use brand producer already recorded for the independent Cloud service, adding its exact second reciprocal software `produces` link.

## Validation

- The first-party maintained repository substantiates released installable software and the distinct source/task/evaluation or hosted boundary.
- Pinning sources and operating environment does not conflate upstream benchmark or downstream service identity.
- Exact producer inverse resolves to the existing Browser Use producer entity at `catalog/producers/b/browser-use`.
