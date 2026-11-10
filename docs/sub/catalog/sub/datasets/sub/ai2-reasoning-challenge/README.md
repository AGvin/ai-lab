# Ai2 Reasoning Challenge (ARC)

The Ai2 Reasoning Challenge (ARC) is the original 2018 English grade-school science question-answering dataset released by [Ai2 (Allen Institute for AI)](../../../producers/sub/a/sub/ai2/). It contains **7,787 multiple-choice questions** designed to study scientific knowledge and reasoning. This **ARC is not [ARC-AGI](../arc-agi-1/)**, which concerns abstract pattern generalization under a different project and producer.

## Source and split boundaries

The publisher's [ARC dataset card](https://huggingface.co/datasets/allenai/ai2_arc) divides the questions into two configurations:

| Configuration | Train | Validation | Test | Total |
| --- | ---: | ---: | ---: | ---: |
| ARC-Challenge | 1,119 | 299 | 1,172 | 2,590 |
| ARC-Easy | 2,251 | 570 | 2,376 | 5,197 |

The Challenge questions were selected because both a retrieval baseline and a word co-occurrence baseline answered them incorrectly. That is a historical construction criterion, not proof that a contemporary model cannot solve them. The [Ai2 open-data catalog](https://allenai.org/open-data) also describes an additional corpus of more than 14 million science sentences, which is distinct from the question set itself.

The question sets are not scoring software, an evaluation leaderboard or the separate ARC Prize competition. Compare reported results only with the same configuration, revision, question/answer formatting, prompt and scoring protocol.

## Licensing, attribution and limitations

The Ai2-owned Hugging Face card declares **CC-BY-SA-4.0** as dataset metadata, but the card's narrative licensing section remains incomplete. Preserve applicable attribution/share-alike duties and verify rights for any third-party question material before redistribution. The [Ai2 leaderboard code repository](https://github.com/allenai/aristo-leaderboard) uses a separate [Apache-2.0 software license](https://github.com/allenai/aristo-leaderboard/blob/master/LICENSE), which is not a replacement dataset grant.

ARC was released publicly years ago and can be exposed in model training. Accuracy alone does not establish general reasoning capability, independence from benchmark data, truthfulness or production safety. No model execution or independently reproduced score is claimed here. An exhaustive question-rights, corporate-control or sanctions review was not performed.

## Provenance

- Produced by: [Ai2](../../../producers/sub/a/sub/ai2/).

## Primary resources

- [Ai2 original ARC listing](https://allenai.org/open-data)
- [Official Ai2 ARC dataset card and splits](https://huggingface.co/datasets/allenai/ai2_arc)
- [Original research paper](https://arxiv.org/abs/1803.05457)
- [Ai2 Aristo leaderboard tools](https://github.com/allenai/aristo-leaderboard)
- [Code-only Apache-2.0 LICENSE](https://github.com/allenai/aristo-leaderboard/blob/master/LICENSE)
