# Documentation Requirements

## Requirements

- Teach Generation Latency through distinct user/runtime milestones such as queue delay, prompt/prefill processing, time to first output, inter-output cadence, and total completion time rather than one undifferentiated duration.
- Measure under representative input/context size, output length, batch/concurrency, warm/cold state, cache state, model/runtime/hardware configuration, and failure handling.
- Use appropriate percentile/distribution summaries when average latency hides tail behavior that affects the target workload.
- Explain that batching, longer prompts, queueing, cache misses, model loading, and dependency calls can move the critical path; performance engineering must measure the actual path rather than infer it from one kernel/model number.
- Keep application-level retrieval, tool, network, validation, and post-processing latency with broader system owners while showing how those stages compose with model latency when the user-visible milestone is end-to-end.

## Validation

- Time to first output and inter-output latency remain distinguishable from total completion time.
- Best-case single-request measurements are not generalized to representative concurrent workload behavior.
- Tail latency remains visible when it materially affects the acceptance contract.
