# Retries

Retries repeat an eligible failed operation under bounded rules intended to recover from transient problems.

## Core idea

A retry policy should distinguish transient failures from permanent errors. Network timeouts, rate limits, or temporary service unavailability may succeed later; invalid arguments, denied permissions, and unsupported operations usually will not.

## Good retry policy

- Limit the maximum number of attempts.
- Use exponential backoff and jitter.
- Respect provider retry-after guidance.
- Retry only idempotent or safely deduplicated actions.
- Record every attempt and final outcome.
- Escalate or switch strategy after the budget is exhausted.

## Trade-offs and limitations

Retries increase latency and can amplify outages when many workers retry simultaneously. A model retry may produce a different answer but does not correct missing data or invalid assumptions.

## Common mistakes

- Retrying every exception with no classification.
- Immediately repeating requests in a tight loop.
- Retrying non-idempotent writes after an ambiguous timeout.
- Hiding repeated failures from observability systems.

## Related concepts

- [Agents and Automation](../../)
- [Idempotency](../idempotency/)
- [Failure Recovery](../failure-recovery/)
- [Rate Limits](../../../evaluation-and-operations/sub/rate-limits/)
