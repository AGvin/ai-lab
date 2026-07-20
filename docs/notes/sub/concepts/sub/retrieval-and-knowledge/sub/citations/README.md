# Citations

Citations connect generated statements to the sources or evidence used to support them.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A useful citation is traceable, specific, and attached to the claim it supports. It should identify the source and, when possible, a page, section, line range, record ID, or timestamp. Citation generation must be based on retrieved source metadata rather than invented reference text.

## Practical use

- Evidence-backed research summaries.
- Answers over policy, legal, or technical documentation.
- Audit trails for data extracted from files or databases.
- User interfaces that let readers inspect supporting passages.

## Citation quality checks

- **Correctness:** the cited passage supports the claim.
- **Completeness:** important factual claims have evidence.
- **Specificity:** the reference points to the relevant location.
- **Provenance:** source identity and version are preserved.

## Trade-offs and limitations

A citation can point to a low-quality or outdated source. Excessive citations reduce readability, while sparse citations make verification difficult. Some generated claims combine several sources and require more than one reference.

## Common mistakes

- Allowing the model to invent URLs, titles, or page numbers.
- Citing a document that discusses the topic but not the claim.
- Losing citation offsets after document preprocessing.
- Treating citations as a substitute for source evaluation.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Grounding](../grounding/)
- [Provenance](../../../safety-privacy-and-reliability/sub/provenance/)
- [Retrieval Evaluation](../../../evaluation-and-operations/sub/retrieval-evaluation/)