# Documentation Requirements

## Requirements

- Use the reader-facing title `Few-Shot Prompting`.
- Define few-shot prompting as supplying a small set of demonstrations or exemplars in the current prompt/context so the model can condition its response to a new instance on the demonstrated task, format, label space, style, or transformation pattern.
- Explain that ordinary few-shot prompting is an in-context/inference-time technique and does not update model weights. Keep fine-tuning, supervised training, retrieval of demonstrations, and learned prompt parameters as separate mechanisms even when they can supply or optimize examples.
- Treat `few` as context-relative rather than a universal fixed number. Zero-shot, one-shot, and few-shot are practical prompting regimes whose exact example counts depend on the task and convention.
- Explain that demonstrations can communicate input/output structure, label semantics, edge-case handling, domain terminology, and other task regularities, but the model need not be literally learning a durable new task rule or storing the examples beyond the active context.
- Present demonstration choice, formatting, labels, ordering, similarity, diversity, and context position as variables that can materially affect results; do not claim one universally optimal ordering, balance rule, or example count.
- Make clear that demonstration quality does not guarantee generalization. Examples can induce copying, anchoring, spurious patterns, bias, leakage, or contradictory behavior and therefore require task-specific evaluation.
- Distinguish few-shot prompting from retrieval-augmented generation: retrieved examples may be used as demonstrations, but retrieval is the mechanism for selecting external information while few-shot prompting is the way exemplars are supplied in context.
- Keep task-specific example-selection recipes, benchmark-optimized prompt sets, sensitive example data, provider-specific context limits, and model-selection guidance with their applicable learning, evidence, retrieval, privacy, or decision owners.
- Use the canonical entity references as research inputs for in-context demonstration semantics and sensitivity when reader-facing rendering is activated.

## Validation

- The page does not describe ordinary few-shot prompting as a weight update or durable fine-tuning process.
- No universal fixed example count defines `few-shot`.
- The page does not guarantee that more examples, balanced labels, similar examples, or one ordering always improves performance.
- Few-shot prompting is distinguished from retrieval, fine-tuning, and learned prompt-parameter methods.
- Demonstrations are not assumed to encode a faithful human-readable rule or to generalize beyond evaluated cases.
- Legacy design guidance is preserved only as qualified conceptual boundaries rather than copied as universal instructions.
