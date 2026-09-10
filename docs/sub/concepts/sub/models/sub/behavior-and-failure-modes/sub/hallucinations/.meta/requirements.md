# Documentation Requirements

## Requirements

- Use the reader-facing title `Hallucinations (Confabulations)` while retaining `hallucinations` as the selected canonical path/search term.
- Define the phenomenon as generated content that is presented as an answer, claim, rationale, citation, or other model output but is false, internally inconsistent, unsupported by the required evidence/source/context, or divergent from the supplied input in a way that violates the task's truth/faithfulness expectations.
- Explain `confabulation` as an established alternative term used by NIST for generative-AI risk discussion and `hallucination` as the widely used research/industry term; do not imply that the field has one universally preferred vocabulary.
- Distinguish factuality from source faithfulness. An output can be factually plausible or even true yet unsupported by a required source, while an output can faithfully repeat incorrect retrieved/source material and still be false for reasons not attributable solely to model hallucination.
- Distinguish hallucination from intentional creative generation, hypothetical reasoning, uncertainty, approximation, ordinary deterministic calculation bugs, retrieval failures, stale source data, or application-side data corruption unless the generated output also violates the applicable truth/faithfulness contract.
- Explain that hallucinations can involve facts, quotations, citations, identifiers, code/API claims, calculations, summaries, reasoning steps, or multimodal descriptions; do not restrict the phenomenon to fabricated named entities or factual prose.
- Avoid a single-cause explanation. Training data, objective/model behavior, prompt/context conditions, retrieval/evidence quality, decoding, task ambiguity, and system design can all contribute, and observed output alone may not identify the root cause.
- Make clear that fluent or confident wording, low sampling temperature, schema validity, retrieval augmentation, citations-shaped text, or a detailed rationale do not by themselves establish truth or eliminate hallucination risk.
- Keep concrete hallucination rates, benchmark taxonomies, detection metrics, domain-specific risk assessments, incident evidence, mitigation procedures, and product/model comparisons with their applicable evaluation, trustworthy-AI, evidence, engineering, or decision owners.
- Use the canonical entity references as research inputs for terminology, factuality/faithfulness boundaries, and generative-AI risk context when reader-facing rendering is activated.

## Validation

- The page does not define every incorrect output as a hallucination without considering the task's source/truth contract and other failure sources.
- Intentional fiction or hypothetical content is not mislabeled as hallucination merely because it is non-factual by design.
- Factual correctness and source faithfulness are distinguished.
- Hallucination is not attributed to one universal root cause or treated as eliminated by RAG, low temperature, schema compliance, citations, or visible reasoning.
- `confabulation` is preserved as alternative authoritative terminology without renaming the selected canonical slug.
- Legacy mitigation advice is not copied as a universal operational recipe.
