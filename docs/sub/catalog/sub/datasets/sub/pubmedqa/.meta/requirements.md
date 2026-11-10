# Documentation Requirements

## Requirements

- Scope PubMedQA as a biomedical question answering dataset, not a clinical decision-support system, medical advice model, hosted API, or a new identity per subset.
- Official repository README documents PQA-L bundled in the data directory and PQA-U/PQA-A obtained separately; it supplies split generation procedures, but explicitly notes no official split code for PQA-U. Record split and original version with any measurement.
- Evaluation script expects prediction JSON keyed by PubMed ID (PMID) with exactly one of yes, no or maybe as the answer. This is biomedical research QA, not a definitive clinical diagnostic reference.
- Pinned repository README and root LICENSE show MIT project code, but paper abstracts, downloaded PubMed texts, externally hosted datasets and biomedical content may have independent licenses or reuse requirements.
- Document medical evidence limitations, possible training-set contamination, class imbalance, answer uncertainty, annotation quality, prompt/retrieval differences and downstream safety risk. A high benchmark score does not confer medical validity.
- No data download, biomedical quality validation, model scoring, reproduction of paper outcomes, provider API invocation or whole-catalog clean pass was performed.

## Validation

- Exactly one canonical dataset identity, pinned publisher sources, and a resolvable dataset index link.
- Distinguish repository and benchmark data rights; do not award runtime, complete source audit or whole-catalog clean-pass credit.
