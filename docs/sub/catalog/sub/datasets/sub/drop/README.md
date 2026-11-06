# DROP

**DROP** (*Discrete Reasoning Over the content of Paragraphs*) is an Ai2 reading-comprehension dataset released in 2019. Its English passage-grounded questions require reference resolution and discrete reasoning, such as counting, adding, comparing and sorting facts rather than just copying matching text.

## Dataset and evaluation boundaries

The [original Ai2/AllenNLP publisher source](https://github.com/allenai/allennlp-website/blob/master/drop.html) describes about **96,000 questions across 6,700 passages**: about 77,000 training, 9,500 development and a similar-size **hidden test** set. The [TensorFlow Datasets 2.0.0 builder](https://www.tensorflow.org/datasets/catalog/drop) lists **77,409 train and 9,536 dev** examples; it does not expose the hidden test answers as a public evaluation split.

The [final NAACL 2019 paper abstract](https://aclanthology.org/N19-1246/) separately states **55,000 questions**. These are differing original published scope statements. Do not silently replace the dataset publisher's larger released-corpus count with the paper's smaller number. Reproducible comparison needs the exact source release, train/dev/test split, normalization, evaluator, and model run settings; historic reported F1 or exact-match scores are not current model performance.

An original DROP data release, the AllenNLP implementation, the NAQANet baseline model, and any live leaderboard are different artifacts. The hidden test partition should not be treated as publicly accessible verified answers.

## Data license and safe use

The original publisher explicitly states **CC BY-SA 4.0** for the DROP data. However, the [Ai2-managed AWS Open Data Registry](https://registry.opendata.aws/allenai-drop/) abbreviates the license as **CC BY**, so the statements do not match. Before downloading for redistribution, commercial training or another reuse, verify the precise file-level terms, original attribution/share-alike conditions and any third-party paragraph rights; the license of model code or a mirror does not independently clear the source content.

Ai2 [still identifies DROP in its official open-data catalog](https://allenai.org/open-data), even though its original AllenNLP website repository is archived. No raw dataset, hidden labels, model, evaluator, independent rights clearance or benchmark run was performed for this profile.

## Relations

- Original publisher: [Ai2 (Allen Institute for AI)](../../../producers/sub/a/sub/ai2/)
- Separate Ai2 question datasets: [ARC](../ai2-reasoning-challenge/) and [OpenBookQA](../openbookqa/)

## Original resources

- [Ai2 open-data catalog](https://allenai.org/open-data)
- [Original archived publisher page and license statement](https://github.com/allenai/allennlp-website/blob/master/drop.html)
- [Original NAACL 2019 paper](https://aclanthology.org/N19-1246/)
- [Ai2-managed AWS Registry listing](https://registry.opendata.aws/allenai-drop/)
- [TensorFlow Datasets DROP 2.0.0](https://www.tensorflow.org/datasets/catalog/drop)
