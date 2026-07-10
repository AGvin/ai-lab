# Autonomy Levels

<!--
ai_content:
  managed: true
  l10n: true
-->

Autonomy levels describe how much independent decision-making and action an AI system is allowed to perform.

## Example spectrum

- **Advisory:** the model suggests information or actions but cannot execute them.
- **Drafting:** the system prepares artifacts for human review.
- **Approval-gated:** selected actions execute only after confirmation.
- **Bounded autonomous:** the agent acts independently inside predefined tools, budgets, and policies.
- **Broad autonomous:** the system can plan and act across many capabilities with limited supervision.

## Core idea

Autonomy should be assigned per capability and risk, not as one label for the whole system. An agent may autonomously read public documentation while requiring approval to modify a repository or send email.

## Practical use

Choose the lowest autonomy that still provides useful efficiency. Increase autonomy only after measuring reliability, adding observability, narrowing permissions, and defining recovery procedures.

## Trade-offs and limitations

Higher autonomy reduces manual effort but increases the impact of incorrect assumptions, prompt injection, compromised tools, and repeated side effects.

## Common mistakes

- Equating model intelligence with operational trust.
- Granting the same autonomy to read and write actions.
- Removing approval without first improving validation.
- Failing to communicate the actual autonomy level to users.

## Related concepts

- [Agents and Automation](../../)
- [Human in the Loop](../human-in-the-loop/)
- [Least Privilege](../../../safety-privacy-and-reliability/sub/least-privilege/)
- [AI Agents](../ai-agents/)
