# Documentation Requirements

## Requirements

- Use the reader-facing title `System Prompts`.
- Define a system prompt as a system- or platform-supplied instruction context used by some model interfaces to establish behavior, policy, role, task framing, or other higher-level guidance outside ordinary user content.
- Make clear that `system prompt` is an interface/system concept, not a universal intrinsic layer inside every model. Some APIs expose a literal `system` role, others use different instruction parameters, authority levels, presets, hidden platform context, or no equivalent public mechanism.
- Distinguish system-prompt content from the surrounding instruction-hierarchy contract. A provider may assign system instructions higher authority than developer/user/tool content, but the exact hierarchy, override rules, persistence, and message semantics are provider/model-specific and mutable.
- Explain that system prompts can contain stable behavior and task constraints, but dynamic source data, retrieved documents, tool results, and user-provided content should not be reclassified as trusted system instructions merely because they are inserted into the same textual context.
- State that a system prompt can influence model behavior but is not by itself an authorization, isolation, confidentiality, or security enforcement boundary. Consequential permissions and data-access restrictions require enforcement outside model-generated text.
- Explain that conflicts, prompt injection, model updates, context construction, and hidden provider instructions can affect realized behavior; existence of a system prompt does not guarantee compliance with every sentence in it.
- Keep current provider authority hierarchies, concrete hidden/default prompts, API parameters, product presets, security controls, and prompt-engineering recipes with their applicable catalog, platform, trustworthy-AI, or learning owners.
- Use the canonical entity references only to illustrate current real-world system-prompt contracts and their variation; do not turn either provider's implementation into the generic definition.

## Validation

- The page does not claim every model/API has a literal system-message role or identical instruction hierarchy.
- System prompts are distinguished from model architecture, training, user prompts, retrieved data, and external authorization controls.
- A system prompt is not presented as a complete prompt-injection defense or security boundary.
- Provider-specific hierarchy semantics are explicitly scoped and not generalized as universal facts.
- Mutable product default prompts and API syntax are not copied into the canonical concept as stable semantics.
- Legacy operational/security recommendations are preserved as boundaries without turning the concept page into an implementation playbook.
