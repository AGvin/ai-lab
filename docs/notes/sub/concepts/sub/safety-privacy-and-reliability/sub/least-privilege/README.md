# Least Privilege

Least privilege grants an AI system only the permissions and data access required for the current task.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A capable model should not automatically receive broad operational authority. Permissions should be narrow in scope, time, resource, and action. Read, draft, approve, and execute capabilities should be separated where practical.

## Practical controls

- Use task-specific service accounts.
- Prefer read-only access for analysis.
- Limit tools to explicit business operations.
- Restrict file paths, repositories, recipients, and tenants.
- Use short-lived credentials.
- Require approval for sensitive writes.

## Trade-offs and limitations

Fine-grained permissions require more configuration and may create workflow interruptions. However, the operational cost is usually lower than the impact of a compromised or mistaken high-privilege agent.

## Common mistakes

- Giving an agent administrator credentials for convenience.
- Reusing a human user's unrestricted session.
- Allowing a generic shell when a narrow API is sufficient.
- Granting permanent access for a one-time task.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Sandboxing](../sandboxing/)
- [Human in the Loop](../../../agents-and-automation/sub/human-in-the-loop/)
- [Autonomy Levels](../../../agents-and-automation/sub/autonomy-levels/)
