# PubMedQA

**PubMedQA** is a biomedical research question-answering benchmark in which an answer to a research question is expressed as **yes**, **no** or **maybe**, based on evidence associated with a PubMed article.

## Data and evaluation

The [original source README](https://github.com/pubmedqa/pubmedqa/blob/1cbae8e92f72f20c8d3747cbb3bf5bc53554d997/README.md) describes PQA-L (labeled), PQA-U (unlabeled) and PQA-A (artificially generated) data as components of one benchmark family. PQA-L is included in the checked-out data directory; PQA-U and PQA-A are distributed through separate upstream download links. Split processing is version-specific; the README states that an official PQA-U splitter is not provided.

Evaluation consumes a JSON mapping from PMID to yes/no/maybe predictions. Preserve source records, split, prompt and answer parsing before comparing scores. Benchmark samples represent research article content and annotations; their judgments should not be presented as medical advice or validated clinical outcomes.

## Data rights and risk

The [root MIT LICENSE](https://github.com/pubmedqa/pubmedqa/blob/1cbae8e92f72f20c8d3747cbb3bf5bc53554d997/LICENSE) covers project material within its grant, but PubMed abstracts and externally linked biomedical content can carry distinct source terms. Check the provenance and permissions for the exact exported dataset. Review data leakage, evidence uncertainty and model hallucinations before consequential use.

No dataset was downloaded, clinical validity checked, model evaluation executed or whole-catalog clean pass performed.

## Official source snapshot

- [Publisher repository](https://github.com/pubmedqa/pubmedqa)
- [Pinned README](https://github.com/pubmedqa/pubmedqa/blob/1cbae8e92f72f20c8d3747cbb3bf5bc53554d997/README.md)
- [Pinned LICENSE](https://github.com/pubmedqa/pubmedqa/blob/1cbae8e92f72f20c8d3747cbb3bf5bc53554d997/LICENSE)
