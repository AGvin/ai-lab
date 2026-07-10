# Failure Recovery

Failure recovery restores a workflow to a known safe state after model, tool, network, infrastructure, or validation failures.

## Core idea

Recovery is broader than retrying. It may resume from a checkpoint, skip a non-critical step, switch to a fallback, compensate for a completed side effect, request human intervention, or stop safely with enough information for later continuation.

## Practical design

- Persist checkpoints after meaningful completed stages.
- Classify failures as transient, permanent, partial, or ambiguous.
- Record which external effects definitely occurred.
- Use compensating actions when rollback is impossible.
- Preserve enough diagnostic context for operators.
- Define terminal states instead of looping indefinitely.

## Trade-offs and limitations

Robust recovery adds workflow complexity and storage requirements. Distributed systems may not offer a single authoritative answer about whether a timed-out operation completed.

## Common mistakes

- Restarting the entire task after every error.
- Losing state when the process exits.
- Assuming all actions can be rolled back.
- Continuing after validation failure without marking the result as unsafe.

## Related concepts

- [Agents and Automation](../../)
- [Retries](../retries/)
- [Idempotency](../idempotency/)
- [Fallback Models](../../../evaluation-and-operations/sub/fallback-models/)
