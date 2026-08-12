# Documentation Requirements

## Requirements

- Define model selection for language and research by exact task and output contract.
- Cover the selected task families: general assistance, reasoning/problem solving, research/synthesis, writing/editing, translation/localization, summarization, question answering, extraction, and classification.
- Require task evidence for semantic correctness, omissions, grounding, terminology/style, structured output, long-context behavior, correction effort, latency, retries, and cost per accepted result when relevant.
- Prevent one language-task ranking from being generalized to unrelated language tasks.
- Preserve useful concrete broad-language/reasoning/research candidate hypotheses that were embedded in legacy model-reference and portfolio pages only after current first-party identity/capability verification.
- Present retained candidates as bounded evaluation starting points for the specific text/reasoning hypothesis they originally supported, not as a universal language-model rank.
- Keep compact local/private hypotheses, economical hosted routes, and capability-first hosted/self-hosted routes distinguishable by their intended experiment and evidence boundary.
- Treat provider positioning, long context, multilingual capability, tool support, or low token price as eligibility evidence only; require workload evidence before assigning a recommendation state.
- Recheck mutable hosted aliases, prices, limits, availability, tool surfaces, and data-path constraints at decision time rather than embedding them in a durable ranking.
- Keep translation/localization-specific candidates and acceptance rules in `sub/translation-and-localization/` when that child has the more specific owner.
- Link canonical model facts from `../../../reference/` instead of duplicating model profiles.
- Materialize a more specific selected child only when its shortlist, rubric, or acceptance criteria materially differ.

## Validation

- The page contains no universal language-model ranking.
- Useful legacy broad-language candidate hypotheses are not discarded merely because they were embedded in model-reference or environment/portfolio pages.
- Every retained candidate has an explicit task hypothesis and evidence boundary rather than an unsupported current-winner claim.
- Task-specific conclusions are scoped to their workload and evidence.
- Translation-specific guidance is not duplicated when the translation child is the more specific owner.
- Canonical model identity remains in reference documentation.
