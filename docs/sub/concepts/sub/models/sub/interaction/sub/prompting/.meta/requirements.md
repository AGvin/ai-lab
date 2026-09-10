# Documentation Requirements

## Requirements

- Use the reader-facing title `Prompting`.
- Define prompting as conditioning a model's current behavior by supplying task-relevant instructions, questions, context, demonstrations, constraints, delimiters, or other supported input representations at inference/interaction time.
- Distinguish ordinary prompting from model training and weight adaptation. Fine-tuning, prompt tuning, prefix tuning, learned soft prompts, and other parameterized adaptation methods belong to training/adaptation even when their names contain `prompt`.
- Explain that prompts can be plain natural language, structured text, code, schemas, multimodal inputs, or combinations supported by the model/system; do not reduce prompting to one chat-message format.
- Distinguish task instructions from source/evidence content and from provider/system metadata. Their relative authority and parsing are determined by the surrounding interface/model contract rather than by visible text alone.
- Present zero-shot, few-shot, system-level instructions, role/task specification, output constraints, and other prompt patterns as techniques within the broader prompting concept, while keeping selected child concepts such as `system-prompts/` and `few-shot-prompting/` in their own nodes.
- Explain that prompt changes can materially affect model behavior but cannot create missing model capability, guarantee factual knowledge, grant unavailable tools/data, or replace external authorization, validation, or deterministic enforcement.
- Treat prompt effectiveness as model-, task-, context-, and version-dependent. Prompt patterns are hypotheses to evaluate against representative cases rather than universal incantations or stable performance guarantees.
- Keep procedural prompt-writing recipes, templates, exercises, task-specific examples, provider-specific role syntax, prompt libraries, and model-selection recommendations with their applicable learning, catalog, or decision owners.
- Use the canonical entity references as research inputs for prompting and in-context task-specification boundaries when reader-facing rendering is activated.

## Validation

- The page does not equate prompting with training, fine-tuning, or learned prompt-parameter methods.
- The page does not assume one provider's chat roles or message schema is universal.
- Prompting is not presented as a security boundary, factuality guarantee, capability expansion mechanism, or substitute for evaluation.
- Selected child concepts are introduced without duplicating their detailed canonical content.
- Prompt techniques are qualified as model/task/context dependent rather than guaranteed best practices.
- Legacy procedural prompt-writing guidance is not duplicated wholesale into this canonical concept owner.
