# HellaSwag

HellaSwag is the historical 2019 commonsense sentence-completion evaluation dataset introduced by Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi and Yejin Choi in [their research paper](https://arxiv.org/abs/1905.07830). It presents a context with candidate endings and measures whether a system can select a plausible continuation.

## Current access and rights warning

**Original source access is blocked, and underlying data rights are unresolved.** On November 1, 2026, GitHub's API returned HTTP 451 for the [original research repository](https://github.com/rowanz/hellaswag), citing a DMCA access block. The [September 14, 2026 wikiHow takedown notice published by GitHub](https://github.com/github/dmca/blob/master/2026/09/2026-09-14-wikihow.md) explicitly lists that repository. This is evidence of an active copyright/access dispute, **not a court finding** that every item infringes.

The [Rowan HellaSwag distribution on Hugging Face](https://huggingface.co/datasets/Rowan/hellaswag) is still visible, but its reviewed metadata does not specify an explicit dataset license. Older repository MIT labels do not independently settle copyright or redistribution rights in source WikiHow/ActivityNet material. **Do not treat accessibility as permission to redistribute, reuse for training or bypass the original block.** Confirm applicable rights with the authorized rights holders before moving or deploying the data.

## Dataset boundary

The historical dataset was built with adversarial filtering for difficult commonsense language understanding, distinct from the training/evaluation scripts and later model leaderboard entries. The [TensorFlow Datasets catalog](https://www.tensorflow.org/datasets/catalog/hellaswag) reports 39,905 training, 10,042 validation and 10,003 test examples, or 59,950 total. It also distinguishes ActivityNet versus WikiHow sources and in-domain versus out-of-domain splits.

Evaluation comparisons depend on exact data revision, split, candidate ordering and accuracy protocol. Public benchmark exposure creates contamination risk, and a single multiple-choice score does not establish general model reasoning, truthfulness or safety. No score was independently reproduced here.

## Attribution and usage scope

The original research is attributable to the five named authors. Academic affiliations do not by themselves establish sole corporate ownership, so no unsubstantiated producer relationship is asserted. This profile is retained for research identification and risk assessment, **not as an unconditional recommended training or evaluation-data source**. A complete copyright, license, ultimate beneficial ownership or sanctions audit has not been carried out.

## Primary resources

- [Original HellaSwag paper](https://arxiv.org/abs/1905.07830)
- [Original repository (currently blocked)](https://github.com/rowanz/hellaswag)
- [Existing author-named Hugging Face distribution](https://huggingface.co/datasets/Rowan/hellaswag)
- [TensorFlow Datasets source and split description](https://www.tensorflow.org/datasets/catalog/hellaswag)
- [GitHub-published September 2026 wikiHow takedown notice](https://github.com/github/dmca/blob/master/2026/09/2026-09-14-wikihow.md)
