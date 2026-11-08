# Documentation Requirements

## Requirements

- Identify AlphaGenome Atlas as Google DeepMind's released precomputed genomics dataset/platform containing AlphaGenome-derived predictions for roughly 9 billion possible single-nucleotide variants across the human genome.
- Preserve its distinction from the AlphaGenome trained model: Atlas owns the precomputed dataset, AlphaGenome Variant Impact (AVI) score/attributions, portal/query resource, and dataset-scale access boundary.
- Keep the website portal, AlphaGenome API, Google Antigravity skills, and Google Cloud access as distribution/integration surfaces rather than separate dataset identities.
- Treat dataset size, access terms, update cadence, score definitions, API availability, research/commercial access, and benchmark/evaluation claims as freshness-sensitive.
- Preserve research/clinical boundaries and do not present predicted variant effects as independently validated diagnoses.
- Attribute performance/use-case claims to Google DeepMind or named external collaborators.

## Validation

- AlphaGenome Atlas remains a dataset/resource identity rather than the AlphaGenome trained model.
- Producer provenance resolves to Google DeepMind.

## Scoped original-source qualification — 2026-11-08

- **AlphaGenome Atlas** is Google DeepMind's original **2026-09-08** released public research resource of AlphaGenome-predicted molecular impacts for roughly **9 billion possible human single-nucleotide variants**, not the trained AlphaGenome model itself or experimental evidence that each variant is pathogenic. The freely browsable research portal, atlas predictions and combined **AlphaGenome Variant Impact (AVI)** scoring layer are part of one Atlas resource, not separately accepted datasets or clinical products.
- Precomputed molecular and regulatory variant effects may be accessed through the publisher's portal and documented AlphaGenome interfaces. AVI combines prediction information from AlphaGenome and AlphaMissense; underlying predicted effects vary by variant, molecular assay, tissue and model release. A model-derived prediction, including authors' validation anecdotes, is not clinical interpretation, a diagnostic test, or a validated human-disease risk claim.
- Public original publisher sources: https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/ ; https://deepmind.google/science/alphagenome/ .
- Source gate validates one existing publisher-owned dataset/platform identity and dated research-access, predicted-versus-measured, producer and model boundaries only. No atlas query, bulk dataset redistribution or license clearance, personalized medical decision, independent experimental confirmation, complete security/privacy/legal audit, reader repair, repository-wide schema/cache/CI/render, clean or final gate.
