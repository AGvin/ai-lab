<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:1f7e68b52ff14c3499520f8716646a014507025c
  mode: copy-through
-->

# Hybrid Search

Retrieval that combines semantic and lexical search signals.

## Переклади

- [English](../../../../l10n/uk_UA/)
- Українська — поточна

## Core idea

Retrieval that combines semantic and lexical search signals. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Hybrid search combines lexical scores with vector-similarity scores.
- Results may be merged by weighted scoring, reciprocal-rank fusion, or a reranking stage.
- Metadata filters can be applied before or after candidate generation depending on the index.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Hybrid Search affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Retrieve both semantic paraphrases and exact model names, error messages, or configuration keys.
- Improve robustness for mixed natural-language and technical queries.

## Example

A query containing an exact error code and a natural-language symptom can benefit from BM25 plus vector retrieval.

## Trade-offs and limitations

- Score calibration and fusion settings need evaluation on the real corpus.
- Combining two weak retrievers does not automatically produce a strong system.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Hybrid Search expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Retrieval and Knowledge](../../../../l10n/uk_UA/)
- [Semantic Search](../../../semantic-search/l10n/uk_UA/)
- [Grounding](../../../grounding/l10n/uk_UA/)
