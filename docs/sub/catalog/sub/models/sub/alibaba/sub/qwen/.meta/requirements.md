# Documentation Requirements

## Requirements

- Introduce Qwen as the model family represented by the child model series.
- Link the canonical Qwen Team producer rather than duplicating producer identity content.
- Preserve every reviewed Qwen series from the legacy corpus that has a selected canonical model owner and add newly researched series only from current authoritative evidence.

## Content Specification

- Use `Qwen` as the page title.
- Keep the introduction short and model-family focused.
- Link Qwen Team from the canonical `produced-by` relation.
- Include the official Qwen website and official Hugging Face organization.
- Link Qwen2.5-Coder, Qwen3, Qwen3-Coder, Qwen3.8, Qwen3-VL, Qwen Omni, and Qwen-Image as currently materialized child model series.
- Do not infer missing Qwen branches merely from naming; materialize additional series when current source evidence and content justify them.

## Decision and Operational Boundaries

- Qwen is the model family produced by Qwen Team; its members include language, vision, coding, image, speech, and retrieval models.
- Do not inherit one member's license, modality, reasoning mode, or context limit across the family; follow the exact checkpoint or hosted model reference.
- Distinguish open-weight execution from Qwen Studio, Qwen Cloud, and Model Studio service behavior.
- For Model Studio use, distinguish the no-training commitment from retention: standard inference data can be retained for up to 30 days subject to exceptions, while stateful features persist until deletion; verify exact feature and model eligibility before relying on ZDR.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Producer details are not duplicated from the Qwen Team producer profile.
- Every child and producer link resolves.
- The page does not imply ownership where only production and organizational relations are validated.
- Child series are not typed as additional top-level model families.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
