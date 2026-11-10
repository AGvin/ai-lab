# Documentation Requirements

## Requirements

- Identify Qwen2.5-Coder as a coding-specialized model series within the Qwen family.
- Preserve series-level facts that are genuinely shared across represented Qwen2.5-Coder models.
- Link the canonical Qwen family and Qwen Team producer without duplicating producer identity content.
- Keep model-selection, local-hardware suitability, total-cost, and accepted-result-quality conclusions outside this canonical series profile.

## Content Specification

- Use `Qwen2.5-Coder` as the page title.
- Describe the series as code-specific causal language models for code generation, code reasoning, code repair, and coding-assistant workflows.
- Preserve only shared distinctions supported by current upstream material; keep concrete model architecture details, parameter counts, context, and licenses on exact model pages.
- Link Qwen through the canonical `member-of` relation and Qwen Team through the canonical `produced-by` relation.
- Include the official Qwen2.5-Coder family release and introduction references.
- Link a concrete-model index containing the represented 3B Instruct and 7B Instruct models.

## Decision and Operational Boundaries

- Qwen2.5-Coder is a code-specialized language-model series with separately released model sizes.
- Keep the 3B Research License distinct from the 7B Apache-2.0 license; both license and context must be checked on the exact model.
- Do not transfer 7B long-context claims to the 3B model; preserve current 3B card limits even when historical cards differ.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The page does not treat Qwen2.5-Coder as one exact concrete model or as a second top-level model family.
- Concrete-model parameter counts and licenses remain on the corresponding model pages.
- Selection and cost conclusions are not presented as intrinsic series facts.
- Producer and family relations resolve to canonical nodes.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
