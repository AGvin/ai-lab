# Grounding

Grounding ties generated claims to supplied evidence, tool results, or authoritative data instead of relying only on the model's internal statistical knowledge.

## Core idea

A grounded answer should be supported by information available to the system at generation time. Grounding may use retrieved documents, database records, calculations, code execution, sensors, or APIs. The application should preserve the relationship between claims and evidence so the result can be checked.

## Practical use

- Answer questions from internal documentation.
- Produce current data from APIs or databases.
- Generate summaries with source references.
- Use calculators or code for exact computations.
- Restrict recommendations to verified catalog data.

## Trade-offs and limitations

Grounding quality depends on evidence quality. Incorrect, outdated, or malicious sources can create confidently grounded but wrong answers. A model may also cite a relevant passage that does not actually support the specific claim.

## Good practice

Retrieve narrowly, record provenance, and distinguish direct evidence from inference. Validate critical values outside the model. Allow the system to state that evidence is insufficient.

## Common mistakes

- Calling an answer grounded merely because documents were placed in context.
- Accepting citation presence without checking citation support.
- Mixing trusted data with untrusted instructions.
- Hiding source conflicts instead of reporting them.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Citations](../citations/)
- [RAG](../rag/)
- [Hallucinations](../../../model-usage-and-generation/sub/hallucinations/)
