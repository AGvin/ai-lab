# Documentation Requirements

## Requirements

- Identify Poe as a hosted assistant/bot distribution and interaction platform and developer ecosystem, not one foundation model, source-available bot runtime, or underlying API provider.
- Official creator docs distinguish **Prompt Bots, Server Bots, Script Bots, API Bots and external applications**. The current `creator.poe.com` reference is mutable: authenticate and verify features against relevant product and account tier.
- Document the API Bot boundary: the creator connects a compatible Chat Completions or Responses API endpoint; Poe forwards user messages to the external endpoint and streams responses, subject to creator configuration and usage-based point/token charging.
- Keep Poe API keys and creator-hosted endpoint secrets distinct. External applications can use account-scoped Poe API keys; the API can charge the authorized account's points.
- Clarify that bot builders and third-party model providers are independent data processors with their own availability, terms, privacy, retention, content/moderation policies and possible fees.
- Treat publishing/untrusted bot prompts, private chats, file content, API keys and external action permissions as security/privacy risks. Avoid blanket guarantees about data retention, cross-bot isolation, pricing or model access.
- Do not claim an active Poe account, authorized API request, created bot, installed server, token benchmark, full contract audit or whole-catalog clean pass.

## Validation

- One canonical service reader under the selected category and one relative index link; distinct source software, model, content and operator boundaries remain explicit.
- First-party evidence supports the scoped profile only. Do not infer runtime tests, full rights/contract audits or repository-wide clean status.

## Scoped original-source qualification — 2026-11-07

- Poe is a hosted multi-bot assistant and distribution platform; prompt/server/API bots may be operated by different creators, and use of an API bot does not make Poe the owner of the external model or endpoint.
- First-party product/documentation surface: https://creator.poe.com/docs/
- Scoped identity/source boundary only; no authenticated execution, security/privacy audit, full-repository clean pass or final-gate credit.
