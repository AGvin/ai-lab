# Qasper

**Qasper (QASPER)** is Ai2's **2021** research-paper question-answering dataset: **5,049 information-seeking questions over 1,585 English NLP scientific papers**. A person writes each question after seeing only the paper title and abstract, while another practitioner reads the full paper and provides both an answer and supporting evidence.

## Dataset and split boundaries

The [original research paper](https://aclanthology.org/2021.naacl-main.365/) and [Ai2 dataset card](https://huggingface.co/datasets/allenai/qasper) agree on the 5,049 questions and 1,585 paper scope. The [publisher's original 0.3.0 builder metadata](https://huggingface.co/datasets/allenai/qasper/blob/main/dataset_infos.json) contains **888 train / 281 validation / 416 test paper records**. Each record can contain multiple questions and answers; those counts are **papers, not questions**.

Answer annotations include extractive spans, free-form responses, yes/no and unanswerable cases, along with paragraph or figure/table evidence. Pin the exact dataset revision, the train/dev/test split, text preprocessing and answer/evidence evaluator when reproducing F1 scores. Qasper is separate from the Longformer/LED baseline model, evaluator software and a live leaderboard. Historic baseline results do not establish current frontier-model rankings.

## Rights and operational cautions

The original Ai2-managed dataset card declares **CC BY 4.0**. Scientific full-text material was collected from **S2ORC**, so that card alone does not independently clear licenses for each source paper, figure, table or redistribution. Check original publication rights, required attribution and the intended use of exact files before rehosting the corpus or commercial training. Raw annotations may contain worker pseudonyms and experience metadata; apply proportionate data handling.

Ai2 [continues to list the historical Qasper dataset](https://allenai.org/open-data). The later SCROLLS evaluation suite includes Qasper, but that grouping is not another original Ai2 release. This profile does not claim that any dataset was downloaded, any model/evaluator run, or any item-level source-rights or privacy audit completed.

## Relations

- Publisher: [Ai2 (Allen Institute for AI)](../../../producers/sub/a/sub/ai2/)
- Other distinct Ai2 original datasets: [DROP](../drop/), [ARC](../ai2-reasoning-challenge/) and [OpenBookQA](../openbookqa/)

## Original resources

- [Ai2 open-data portfolio](https://allenai.org/open-data)
- [Original Ai2 Qasper dataset, evidence and CC BY 4.0 card](https://huggingface.co/datasets/allenai/qasper)
- [Original NAACL 2021 paper](https://aclanthology.org/2021.naacl-main.365/)
- [Publisher's dataset 0.3.0 split metadata](https://huggingface.co/datasets/allenai/qasper/blob/main/dataset_infos.json)
- [Ai2 LED baseline software](https://github.com/allenai/qasper-led-baseline)
