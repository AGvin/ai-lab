# Model Capabilities and Limitations

Model capabilities and limitations describe what a specific model and deployment can do reliably, under which conditions, and where it tends to fail.

## Core idea

A model name alone is not a complete capability description. Behavior depends on the exact version, context size, modalities, tool access, system prompt, inference settings, provider restrictions, and workload. Capabilities should therefore be treated as measured properties of a configured system rather than permanent labels.

## Important dimensions

- Supported input and output modalities.
- Context capacity and long-context quality.
- Reasoning, coding, language, and domain performance.
- Structured-output and tool-calling reliability.
- Latency, throughput, memory, and cost.
- Safety restrictions, privacy properties, and deployment options.

## Practical use

Create a task-specific evaluation set and test candidate models under realistic prompts. Record failure modes, not only average scores. Re-evaluate when the model version, provider, quantization, or system prompt changes.

## Trade-offs and limitations

A stronger general benchmark score may not translate to a specific workflow. Larger models often cost more or require more hardware. Local models offer control and privacy but may have lower capability or require operational maintenance.

## Common mistakes

- Selecting a model only by parameter count or leaderboard rank.
- Generalizing from a few successful demos.
- Ignoring the effect of quantization and runtime configuration.
- Treating provider marketing claims as production evidence.

## Related concepts

- [Model Usage and Generation](../../)
- [Model Selection](../../../evaluation-and-operations/sub/model-selection/)
- [Benchmarks](../../../evaluation-and-operations/sub/benchmarks/)
- [Evals](../../../evaluation-and-operations/sub/evals/)
