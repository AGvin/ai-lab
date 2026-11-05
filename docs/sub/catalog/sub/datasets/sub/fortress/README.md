# FORTRESS

**FORTRESS** — Expert-curated adversarial and paired benign requests for high-level safety evaluation of frontier language models; benchmark data and separately hosted judging software are distinct.

## Data and evaluation boundary

Scale AI's official FORTRESS description distinguishes 500 public adversarial prompts from a larger 1,010-plus prompt original benchmark and private held-out evaluation material. Each adversarial prompt is paired with benign counterparts and instance-specific rubrics; these are not model generation recipes or public permission to reproduce private prompts.

The [official dataset card](https://huggingface.co/datasets/ScaleAI/fortress_public) was reviewed 2026-11-05 (publisher updated 2025-08-05). Original dataset records and evaluation software were not downloaded; the connected metadata did not expose an immutable source revision SHA.

## Rights, limitations and safety

The public Hugging Face card lists CC BY 4.0 but the publisher explicitly describes this as safety evaluation content that must not be repurposed for harmful misuse. Never publish operational harmful examples, reconstruct hidden test data, or equate reported judge/leaderboard outcomes with validated safety.

**Access:** public. **Publisher-described licensing:** CC BY 4.0 (HF metadata). No harmful prompts, model responses or external experiments were executed or republished. No comprehensive rights audit was run.

## Official source snapshot

- [Publisher dataset card](https://huggingface.co/datasets/ScaleAI/fortress_public)
- [Publisher or paper context](https://labs.scale.com/leaderboard/fortress)
