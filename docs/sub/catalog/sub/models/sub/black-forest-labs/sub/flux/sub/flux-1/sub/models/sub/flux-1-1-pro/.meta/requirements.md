# Documentation Requirements

## Identity and provenance

- Identify FLUX1.1 [pro] as a distinct, released, proprietary BFL-hosted text-to-image model introduced on October 2, 2024; do not conflate it with the earlier FLUX.1 [pro] or the open-weight FLUX.1 [dev]/[schnell] checkpoints. [BFL announcement](https://bfl.ai/blog/24-10-02-flux) [Model profile](https://bfl.ai/models/flux-pro).
- The BFL API lists POST /v1/flux-pro-1.1. The official 2024 Ultra/Raw announcement calls both new capabilities **modes of FLUX1.1 [pro]**, rather than separate trained models. Treat POST /v1/flux-pro-1.1-ultra and its Raw option as serving modes, not extra model identities. [BFL Ultra/Raw announcement](https://bfl.ai/blog/24-11-06-ultra) [API](https://api.bfl.ai/docs).
- Keep the current FLUX.1 grouping explicit as a catalog family/series navigation boundary for earlier-generation FLUX1.1, not as evidence that it shares released weights or directly derives from an indexed FLUX.1 checkpoint.

## Decision and operational boundaries

- Text-to-image is the supported core workflow. BFL promotes fast generation and prompt-following relative to earlier variants; claimed speed or ranking is publisher-provided historical evidence, not an independently reproduced result. [BFL announcement](https://bfl.ai/blog/24-10-02-flux).
- Ultra adds up to 4 MP higher-resolution output; Raw is a photographic-style option. Output quality, latency, current quotas, aspect ratio, prompt policy and pricing must be confirmed for the specific current API mode. [BFL modes](https://bfl.ai/blog/24-11-06-ultra).
- API inference access is distinct from downloadable weights, license grants or local deployment rights. No published local checkpoint, training-parent lineage, parameter count, independent image test or VRAM-fit measurement is established by these sources.
- Contrast previous-generation FLUX1.1 with newer FLUX.2 and FLUX 3 offerings; do not assume that its documented API has been retired simply because later models exist. [Current BFL models](https://bfl.ai/models/).
- Preserve service-specific authentication, usage policies, output terms, billing, and retention qualification; avoid static current price or quality rankings.

## Validation

- One exact member-of relation to FLUX.1 and one reciprocal has-member link; reader and index links resolve.
- Do not create additional Ultra, Raw or fine-tuned-route model nodes from serving parameters.
- No final catalog cache/CI, complete source freshness, independent image benchmark or local runtime acceptance claimed.
