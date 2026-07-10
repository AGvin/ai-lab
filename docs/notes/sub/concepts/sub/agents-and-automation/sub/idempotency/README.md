# Idempotency

An idempotent operation can be repeated without creating additional unintended effects after the first successful application.

## Core idea

Agent workflows frequently retry after timeouts or ambiguous failures. Without idempotency, a retry may send the same email twice, create duplicate records, charge twice, or apply the same repository change repeatedly. Idempotency is normally implemented in the tool or application layer rather than through prompting.

## Practical techniques

- Attach a stable idempotency key to each logical action.
- Use upsert or compare-and-set operations where appropriate.
- Record completed side effects in durable state.
- Check the current external state before retrying.
- Separate read-only planning from write operations.

## Trade-offs and limitations

Idempotency requires storage, key design, and clear action boundaries. Some operations cannot be made perfectly idempotent and instead need compensation or manual reconciliation.

## Common mistakes

- Assuming a timeout means nothing happened.
- Generating a new request identifier on every retry.
- Retrying an entire workflow when only one step failed.
- Relying on the model to remember whether an action was completed.

## Related concepts

- [Agents and Automation](../../)
- [Retries](../retries/)
- [Failure Recovery](../failure-recovery/)
- [Agent State](../agent-state/)
