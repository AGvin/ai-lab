# MiniMax Music 3

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Control-chain review is incomplete; no Russian-control finding or adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

MiniMax Music 3 is the publisher's released composite text-to-music model, taking lyrics plus a music description. It combines an 8B global LM initialized from Qwen3-8B, a 0.6B local LM, a 2.4B flow-matching stage and a 123M VAE decoder; these are component figures, not an asserted aggregate model size. The publisher describes songs up to five minutes with 32 kHz, 16-bit stereo output. GitHub's older two-CUDA-GPU serving recipe and the Hugging Face card's newer Diffusers/offloading paths are runtime-specific, not universal hardware guarantees.

The original MiniMax-Music3 Community License requires notices, commercial UI attribution, prior written authorization above USD 20 million aggregate yearly product/service revenue including affiliates, AUP compliance and downstream safeguards. It separately identifies Apache-2.0 Qwen3-8B and MIT Stable Audio/DAC code ancestry; those licenses do not replace the model's custom terms. This is source review, not legal, ownership or deployment clearance.

The card documents non-streaming CUDA inference and a 5,000-token text limit. Offloading trades memory for latency; published memory examples are not independently reproduced here. Use only authorized lyrics and reference content. No downloads of weights, execution or license acceptance. Source review: 2026-11-05.

## Relations

- Produced by: [MiniMax](../../../../../producers/sub/m/sub/minimax/)

## Official resources

- <https://huggingface.co/MiniMaxAI/MiniMax-Music3>
- <https://huggingface.co/MiniMaxAI/MiniMax-Music3/blob/9c47cc42eb579455170bd868a600ac7096d7e5e0/LICENSE>
- <https://github.com/MiniMax-AI/MiniMax-Music3>
