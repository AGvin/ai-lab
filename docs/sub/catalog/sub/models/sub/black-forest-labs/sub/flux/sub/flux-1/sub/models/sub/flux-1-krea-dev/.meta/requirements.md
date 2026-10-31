# Documentation Requirements

## Identity and provenance

- Identify the exact released `black-forest-labs/FLUX.1-Krea-dev` 12B text-to-image checkpoint, jointly developed by BFL and Krea. [BFL release](https://bfl.ai/blog/flux-1-krea-dev).
- Preserve the more precise training account: BFL supplied `flux-dev-raw`; SFT uses synthetic Krea-1 samples and is followed by preference optimization. Keep Hub's FLUX.1-dev fine-tune classification source-attributed, without asserting equal starting weights or Krea-1 weight inheritance. [Krea technical report](https://www.krea.ai/blog/flux-krea-open-source-release) [Hub](https://huggingface.co/black-forest-labs/FLUX.1-Krea-dev).
- Render the standard current-entity relation block and distinguish canonical placement from exclusive authorship.

## Operational decision boundaries

- Separate gated non-commercial model-weight terms from output permissions and hosted API contracts; architectural compatibility does not establish a license or local hardware fit. [Official model card](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-Krea-dev.md).
- Present aesthetics, realism and quality rankings as publisher claims requiring assignment-level evaluation, not independent measurements.
- State prompt mismatch, bias and factual-reliability limitations; no runtime test, VRAM guarantee or independent quality benchmark is established.

## Validation

- Preserve one model identity with resolving series and joint-producer relations and exact reciprocal endpoints.
- Do not create an unverified public flux-dev-raw node or an unconditional derived-from edge to released FLUX.1-dev.
- Keep Krea's application and Krea-1 synthetic-data provenance separate from the published checkpoint identity.
