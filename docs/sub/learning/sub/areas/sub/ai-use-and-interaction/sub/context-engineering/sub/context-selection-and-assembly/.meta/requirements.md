# Documentation Requirements

## Requirements

- Teach Context Selection and Assembly as choosing and organizing only the information needed for the current task and verification contract.
- Cover the common model-visible components: governing instructions, relevant conversation turns, tool schemas/results, files or multimodal inputs, retrieved evidence, and output/generation capacity where the concrete interface uses a shared or reserved budget.
- Prefer task-relevant evidence and constraints over indiscriminate accumulation; avoid unnecessary repetition that consumes capacity without improving the decision or result.
- Keep critical constraints explicit and prominent enough to survive long or heterogeneous context.
- Use the tokenizer/accounting rules of the concrete model or service when exact request sizing matters; do not substitute generic token heuristics for provider-specific limits.
- Verify long-context behavior with representative inputs and workloads rather than assuming nominal capacity guarantees reliable use of every supplied item.

## Validation

- The page teaches selection and assembly, not maximum context-window definition.
- Exact provider accounting is treated as mutable external evidence.
- More context is not presented as automatically better context.
