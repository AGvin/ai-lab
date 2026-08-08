# Documentation Requirements

## Requirements

- Identify GPT-5.6 as a GPT generation with the represented Sol, Terra, and Luna tiers.
- Preserve generation-level model/API facts shared by the represented tiers.
- Keep mutable pricing, rate limits, product-plan availability, regional rollout, and migration/workflow guidance outside the canonical generation profile.
- Keep tier-specific identifiers, positioning, and any tier-only capability differences on the exact concrete model pages.

## Content Specification

- Use `GPT-5.6` as the page title.
- Link the canonical GPT family.
- Explain that `5.6` identifies the generation while Sol, Terra, and Luna identify distinct named tiers within it.
- Preserve the documented shared input/output modalities: text and image input; text output.
- Preserve multilingual and vision support as provider-documented capabilities.
- Preserve the documented 1,050,000-token context window and 128,000-token maximum output.
- Preserve the February 16, 2026 knowledge cutoff.
- Preserve the documented reasoning-effort values `none`, `low`, `medium`, `high`, `xhigh`, and `max` as hosted model controls.
- Preserve the generation alias `gpt-5.6` as a mutable API alias that routes to GPT-5.6 Sol, without treating the alias as a separate model entity.
- Link a concrete-model index containing GPT-5.6 Sol, GPT-5.6 Terra, and GPT-5.6 Luna.
- Include the official GPT-5.6 launch announcement and model catalog.

## Excluded Residual Content

Preserve outside this canonical generation profile:

- API pricing and long-context pricing multipliers;
- rate limits, regional availability, caching policy, and product rollout state;
- ChatGPT and Codex availability details;
- migration guidance from GPT-5.5 or GPT-5.4 and reasoning-setting recommendations;
- Responses API workflow recommendations;
- tier-selection advice and workload-specific quality, latency, or accepted-result-cost conclusions.

## Validation

- Sol, Terra, and Luna are represented as separate concrete model entities, not aliases of one another.
- Mutable pricing and product availability are not presented as stable generation identity.
- The generation alias is not treated as a fourth model.
- Shared properties are not silently generalized beyond the represented GPT-5.6 tier pages.
