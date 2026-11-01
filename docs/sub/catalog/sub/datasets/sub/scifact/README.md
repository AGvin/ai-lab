# SciFact

**SciFact** is Ai2's original **2020** scientific claim verification dataset, introduced in [*Fact or Fiction: Verifying Scientific Claims*](https://aclanthology.org/2020.emnlp-main.609/). It pairs approximately **1.4K expert-written claims** with research-paper abstracts and evidence rationales that can **support or contradict** a claim. This is evidence-grounded scientific fact checking, not Qasper's full-paper question answering, DROP's paragraph arithmetic, or a trained fact-checking model.

## Source and evaluation boundaries

The [original Ai2 repository](https://github.com/allenai/scifact) distributes claim train/dev/test files and a separate evidence abstract corpus. The source explicitly states **original test gold labels are not publicly released**; local test-set predictions do not independently calculate official gold scores.

The original EMNLP 2020 paper describes approximately **1.4K** claims. By contrast, the publisher's [Hub builder 1.0.0 metadata](https://huggingface.co/datasets/allenai/scifact/blob/main/dataset_infos.json) lists **1,261 training / 450 validation / 300 test claim rows**, plus a separate **5,183-abstract corpus**. These are release/configuration-specific counts; do not silently treat the current builder rows as the original paper's exact annotation totals. Pin source release, evidence labels, retrieval setup and scoring protocol before comparing evaluations. SCIVER, BEIR and related model implementations are distinct task aggregations or software, not new independently authored original SciFact data.

## Licensing conflict: verify exact files

**The publisher's two first-party license statements disagree in scope.** Original [`allenai/scifact/LICENSE.md`](https://github.com/allenai/scifact/blob/master/LICENSE.md) grants **CC BY 4.0 for original claims and evidence annotations**, **ODC-By 1.0 for S2ORC-origin research abstracts**, and **Apache-2.0 for repository code**. However, the [Ai2-managed Hugging Face distribution card](https://huggingface.co/datasets/allenai/scifact) declares **CC BY-NC 2.0** for the dataset overall. Do not infer either unrestricted commercial use or a universal prohibition for every file from a single card. Verify exact payload, license version, attribution, commercial restrictions and third-party source-abstract rights before training, redistribution, hosted service use or commercial deployment.

The original source repository also contains older Python baseline scripts and a historical leaderboard. A source-controlled release is not a validated 2026 model-score, production-ready clinical fact checker or a reliable medical decision aid. No individual claims, scientific abstracts or evaluator were downloaded or executed for this catalog review.

## Relations

- Produced by: [Ai2 (Allen Institute for AI)](../../../producers/sub/a/sub/ai2/)
- Other distinct Ai2 research datasets: [Qasper](../qasper/), [DROP](../drop/), [ARC](../ai2-reasoning-challenge/) and [OpenBookQA](../openbookqa/)

## Original resources

- [Ai2 open-data portfolio](https://allenai.org/open-data)
- [Original SciFact source repository](https://github.com/allenai/scifact)
- [Original component-specific LICENSE.md](https://github.com/allenai/scifact/blob/master/LICENSE.md)
- [Original EMNLP 2020 paper](https://aclanthology.org/2020.emnlp-main.609/)
- [Publisher's Hugging Face distribution and conflicting license](https://huggingface.co/datasets/allenai/scifact)
- [Publisher builder/split metadata](https://huggingface.co/datasets/allenai/scifact/blob/main/dataset_infos.json)
