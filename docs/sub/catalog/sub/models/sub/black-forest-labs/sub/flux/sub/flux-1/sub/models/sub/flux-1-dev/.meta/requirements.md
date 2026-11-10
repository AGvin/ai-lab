# Documentation Requirements

## Identity and provenance

- Identify FLUX.1-dev as the exact `black-forest-labs/FLUX.1-dev` released text-to-image checkpoint and preserve its distinct 12B guidance-distilled rectified-flow model identity. [BFL source model card](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md).
- The parent FLUX.1 series also contains FLUX.1-schnell, but schnell's 1–4-step workflow, Apache 2.0 weights and model behavior must not be copied to dev. [BFL official project](https://github.com/black-forest-labs/flux/blob/main/docs/text-to-image.md).

## Operational decision boundaries

- Downloadable gated weights use the [FLUX dev Non-Commercial License](https://bfl.ai/legal/non-commercial-license-terms). Commercial model use needs separately established permission; model weights, generated output rights and hosted API terms are distinct.
- The model card describes guidance distillation and reference inference code. No measured GPU/VRAM, speed, batch capacity or guaranteed prompt-fidelity claims may be inferred from its publication. [BFL model card](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-dev.md).
- Image generation is not a factual information source; review prompt adherence, representational bias and published license restrictions on real use.

## Validation

- Preserve an exact `member-of` relation to the FLUX.1 series, with one reciprocal `has-member` endpoint and resolving navigation links.
- Render complete current identity and decision boundaries, not just generic placeholder text; link the publisher's original weights, model card and current license terms.
- Do not materialize quantization, LoRA, hosted endpoints or precision formats as additional trained FLUX.1-dev identities without independent source evidence.
