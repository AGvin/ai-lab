# Documentation Requirements

## Identity and provenance

- Materialize exactly `google/siglip2-so400m-patch16-384`: a separately trained fixed-resolution So400m image/text encoder with patch 16 and 384×384 image preprocessing. It is not NaFlex, an image resize switch, a quantization variant or a conversational VLM. [Exact card](https://huggingface.co/google/siglip2-so400m-patch16-384) [Target-resolution training](https://arxiv.org/html/2502.14786v1) [Released checkpoint](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
- The complete contrastive distribution includes vision and text towers, approximately 1.136B stored parameters. So400m describes the vision scale; do not use it as total checkpoint memory/parameters. [Exact config](https://huggingface.co/google/siglip2-so400m-patch16-384/blob/main/config.json).

## Operational boundaries

- Use the matching processor/tokenizer and fixed 384×384 input mapping. These checkpoints are image/text encoders for retrieval and zero-shot classification, not chat or image generators. Use the exact checkpoint processor and tokenizer; fixed-resolution preprocessing does not inherit NaFlex native-aspect behavior. The So400m label refers to the vision tower, while the full image/text checkpoint is approximately 1.136B stored parameters. Equal vector widths do not establish shared embedding spaces. Re-embed/re-index incompatible spaces and evaluate representative retrieval/classification workloads. [Exact card](https://huggingface.co/google/siglip2-so400m-patch16-384).
- The exact Google Hub cards declare Apache-2.0; their public roots have no standalone LICENSE file listed. The big_vision software LICENSE is Apache-2.0, while the SigLIP2 release README separately marks other materials CC-BY. Preserve distribution-specific notices rather than transferring one software license to every NPZ, weight artifact or downstream VLM. [Exact card](https://huggingface.co/google/siglip2-so400m-patch16-384) [Release notices](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
- The vision component initializes North Micro Vision Instruct. Preserve exact reciprocal derived-from pairs and their component scope. No Google text-tower inclusion, sole-parent claim, inherited model capability or transfer of downstream noncommercial terms. [North Micro Vision Instruct provenance](https://huggingface.co/blog/CohereLabs/meet-north-micro-vision-instruct).
- No exact public training parent among sibling SigLIP2 checkpoints was established; do not infer one from paper-stage initialization. No independently run inference, benchmark, total ownership, sanctions classification or deployment guarantee.

## Validation

- Preserve the exact model identity and reciprocal family/derivative pairs. Render a complete reader with correct relative links and complete operating/license boundaries.
- No whole-current-HEAD schema/cache/CI, final rendering, clean research pass or publication-gate credit.
