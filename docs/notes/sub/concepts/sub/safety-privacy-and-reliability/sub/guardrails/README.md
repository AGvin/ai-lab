# Guardrails

<!--
ai_content:
  managed: true
  l10n: true
-->

Guardrails are controls that validate, restrict, monitor, or redirect model inputs, outputs, and actions.

## Types of guardrails

- Input validation and content classification.
- Output schemas and domain validation.
- Tool allowlists and argument constraints.
- Permission and policy checks.
- Rate, cost, and action limits.
- Human approval and escalation.
- Post-generation moderation or redaction.

## Core idea

Guardrails work best as layered application controls. A model-based classifier may help interpret content, but deterministic enforcement should protect permissions, data access, and side effects.

## Trade-offs and limitations

Guardrails can create false positives, false negatives, latency, and maintenance overhead. Attackers may adapt to known filters. A single universal safety classifier rarely covers all application-specific risks.

## Common mistakes

- Treating a system prompt as the only guardrail.
- Blocking unsafe text while allowing unsafe tool actions.
- Adding filters without measuring legitimate-user impact.
- Failing open when a guardrail service is unavailable.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Prompt Injection](../prompt-injection/)
- [Content Moderation](../content-moderation/)
- [Human in the Loop](../../../agents-and-automation/sub/human-in-the-loop/)
