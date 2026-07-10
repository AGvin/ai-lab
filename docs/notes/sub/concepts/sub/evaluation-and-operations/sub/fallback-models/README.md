# Fallback Models

<!--
ai_content:
  managed: true
  l10n: true
-->

Fallback models are alternative models used when the preferred model is unavailable, exceeds policy limits, fails validation, or cannot satisfy a request.

## Core idea

A fallback is part of reliability design, not merely a second API key. The alternative may differ in capability, context size, schema behavior, safety policy, cost, or data location, so the workflow must define when substitution is acceptable.

## Practical use

- Continue service during provider outages.
- Escalate from a small model to a stronger model after failure.
- Switch to a local model when sensitive data cannot leave the environment.
- Use a text-only fallback when no image input is present.

## Trade-offs and limitations

Fallbacks can produce inconsistent answers and may violate assumptions made for the primary model. A cross-provider fallback can introduce different privacy, residency, or licensing conditions.

## Good practice

Test fallback paths regularly. Validate schemas and prompt compatibility. Communicate degraded capability when relevant. Do not silently route sensitive data to a less trusted provider.

## Common mistakes

- Configuring a fallback that has never been tested.
- Retrying indefinitely before switching.
- Assuming equivalent context and tool support.
- Using fallback success to hide persistent primary failures.

## Related concepts

- [Evaluation and Operations](../../)
- [Model Routing](../model-routing/)
- [Failure Recovery](../../../agents-and-automation/sub/failure-recovery/)
- [Data Residency](../../../safety-privacy-and-reliability/sub/data-residency/)
