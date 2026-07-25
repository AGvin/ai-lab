# Event-Driven Agent Architecture

An event-driven agent architecture coordinates agents and services through typed events delivered by a runtime, broker, queue, or message bus rather than one central conversational loop.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established distributed-systems and multi-agent architecture pattern.

## Core idea

```text
producer -> event bus or runtime -> subscribed agent A -> new event
                                -> subscribed agent B -> new event
                                -> workflow or human gate
```

Agents react to declared event types, update durable state, perform bounded work, and emit new events. The runtime manages delivery, identity, lifecycle, and often local or distributed execution.

## Distinguish related patterns

- **Event-driven:** typed events trigger decoupled handlers asynchronously.
- **Graph or DAG:** explicit edges define allowed execution transitions; events may drive node activation.
- **Blackboard:** specialists read and write shared problem state; events may announce state changes.
- **Group chat:** agents exchange conversational messages under a speaking policy.
- **Pipeline:** fixed stages pass artifacts in a known sequence.

An event stream is not automatically an authoritative state store. Preserve durable workflow state separately when replay, reconciliation, or audit matters.

## Event contract

Every event type should define:

```text
Event type and schema version:
Event ID:
Producer and producer version:
Correlation, workflow, task, and causation IDs:
Occurred-at and published-at timestamps:
Partition or ordering key:
Payload and artifact references:
Data classification and permissions:
Expected consumers:
Delivery and retention semantics:
Expiry and replay policy:
```

Events should contain data, not executable prompt instructions or hidden logic. Treat payload content as untrusted input to handlers.

## Delivery semantics

Assume delivery behavior explicitly:

- at-most-once;
- at-least-once;
- effectively-once through idempotent handling and deduplication;
- ordered only within a partition or key;
- unordered across topics, agents, or network boundaries.

“Exactly once” claims should be verified for the complete side effect, not only broker delivery. External APIs, files, databases, and model calls may still duplicate work after timeout or retry.

## Handler contract

Each agent or handler should define:

- subscribed event types and versions;
- filtering and authorization;
- required state and artifacts;
- input and output schema;
- model, tools, permissions, and side effects;
- idempotency key and deduplication window;
- timeout, retry, backoff, and dead-letter policy;
- emitted events and terminal result;
- concurrency, ordering, and resource requirements.

A handler should reject unknown or incompatible schema versions rather than guessing.

## Idempotency and deduplication

Use stable event and operation IDs. Before performing a side effect:

1. check whether the event or operation was processed;
2. reserve or compare-and-set the target state;
3. perform the action with provider idempotency where available;
4. persist the result and emitted-event intent atomically or through an outbox pattern;
5. mark completion;
6. reconcile ambiguous outcomes before retrying.

A language model's statement that an event is new is not a deduplication mechanism.

## Ordering and causality

Record correlation and causation. Define behavior when:

- an update arrives before creation;
- a cancellation arrives after completion;
- a retry arrives after a newer version;
- two agents emit conflicting updates;
- clocks differ;
- a late event targets an expired workflow.

Use state versions, sequence numbers, monotonic generations, or vector and domain-specific conflict rules where appropriate. Do not rely on wall-clock timestamps alone for authority.

## Backpressure and overload

Define:

- queue and concurrency limits;
- per-tenant or per-workflow quotas;
- priority classes;
- shedding, delay, or fail-closed policy;
- maximum event age;
- batch size and model-service capacity;
- expensive-resource admission;
- alert thresholds.

Model calls can be slower and less predictable than ordinary handlers. A burst of events must not create unbounded API cost, GPU allocation, or context growth.

## Retry and dead-letter handling

Classify failures:

- transient transport or provider failure;
- rate limit or capacity exhaustion;
- malformed or unsupported event;
- stale or unauthorized state;
- semantic model failure;
- deterministic validation failure;
- irreversible side-effect ambiguity.

Use bounded exponential backoff with jitter for eligible transient failures. Send poison or exhausted events to a dead-letter or quarantine path with owner, reason, attempts, cost exposure, and safe replay procedure.

Repeated semantic model failure usually requires a different route, stronger model, human review, or terminal failure rather than more identical delivery attempts.

## State and replay

Events may be retained for audit or state reconstruction, but replay is safe only when:

- handlers are deterministic enough or exact model artifacts and parameters are pinned;
- external side effects are idempotent or suppressed;
- schema migrations are defined;
- secrets and expired permissions are not reintroduced;
- current policy permits the historical input;
- output differences are expected and recorded.

For model-based handlers, preserve terminal artifacts and decisions rather than assuming replay will reproduce them.

## Workflow completion

Event-driven systems need explicit terminal state. Define:

- expected task or branch completion events;
- correlation and join rules;
- timeout and missing-event behavior;
- cancellation propagation;
- success, partial success, failure, and expired outcomes;
- artifact and review gates;
- resource cleanup and billing reconciliation.

Do not infer workflow completion from an idle queue. Events may be delayed, lost under at-most-once delivery, quarantined, or waiting on external systems.

## Security boundaries

- Authenticate producers and authorize event types and targets.
- Validate schemas, sizes, artifact references, and signatures where required.
- Separate tenant, environment, and data-class topics or enforce equivalent policy.
- Do not place reusable credentials or unnecessary personal data in event payloads.
- Restrict handler tools and side effects independently from prompt instructions.
- Treat event text, documents, and media as untrusted data.
- Preserve audit and deletion policies across broker, logs, dead-letter queues, and artifacts.

## Suitable uses

- asynchronous and distributed multi-agent systems;
- long-running workflows and external callbacks;
- incident, monitoring, and automation systems;
- hosted model jobs and on-demand resource lifecycle;
- high-volume independent tasks;
- integration across languages, processes, or machines;
- systems requiring decoupled producers and consumers.

## Poor fits

Avoid or simplify this pattern when:

- one synchronous call or fixed local pipeline is sufficient;
- strict global ordering is required but unavailable;
- the team cannot operate broker, schema, replay, and reconciliation complexity;
- every event requires the complete shared context;
- low-latency interaction is harmed by asynchronous hops;
- side effects cannot be made idempotent or reconciled.

## Strengths

- decouples producers, agents, runtimes, and scaling;
- supports asynchronous and distributed execution;
- absorbs bursts through queues and backpressure;
- permits independent deployment and specialist subscriptions;
- provides natural audit, retry, and dead-letter boundaries;
- integrates external systems and callbacks.

## Limitations

- ordering, duplication, replay, and eventual consistency are difficult;
- debugging requires correlation across many handlers;
- stale or conflicting events can corrupt state;
- brokers and queues become operational dependencies;
- retries can multiply model cost or side effects;
- terminal completion is less obvious than in a linear workflow.

## Evaluation metrics

Record:

- accepted, rejected, duplicated, stale, and dead-letter events;
- delivery, queue, handler, and end-to-end latency;
- retry attempts and semantic versus transient failures;
- ordering and state-conflict incidents;
- idempotency and duplicate-side-effect failures;
- backlog age, throughput, saturation, and dropped work;
- workflow terminal success and timeout;
- orphaned resources and incomplete cleanup;
- infrastructure and model cost per accepted result;
- replay and recovery success.

## Evidence and established usage

AutoGen Core describes itself as an event-driven programming framework for scalable multi-agent systems. Its runtime provides message delivery, agent identities and lifecycle management, and standalone or distributed execution, while messages remain serializable data handled by registered agents.

Sources:

- [AutoGen Core](https://microsoft.github.io/autogen/stable/index.html)
- [AutoGen agent runtime environments](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/core-concepts/architecture.html)
- [AutoGen messages and communication](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/message-and-communication.html)

## Related concepts

- [Multi-Agent Systems](../..)
- [Blackboard Architecture](../blackboard/)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Pipeline Architecture](../pipeline/)
- [Resource Lifecycle Controller Architecture](../resource-lifecycle-controller/)
- [Agent State](../../../agent-state/)
