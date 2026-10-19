# Documentation Requirements

## Requirements

- Identify AlphaGenome as Google DeepMind's AI model for predicting how genomic sequence variants affect molecular biological processes, including coding and non-coding regulatory effects.
- Keep AlphaGenome distinct from AlphaGenome Atlas, which is a separately released precomputed dataset/platform built from AlphaGenome predictions, and from AlphaMissense.
- Preserve exact input sequence assumptions, prediction modalities, supported tracks, model/API access, commercial/research access, evaluation results, and downstream workflows only from current first-party material.
- Keep clinical/medical use boundaries explicit and do not turn research predictions into diagnostic or treatment claims.
- Attribute model-performance claims to Google DeepMind or the named evaluation source.

## Validation

- AlphaGenome remains a trained-model identity rather than the Atlas dataset or API/service surface.
- Producer provenance resolves to Google DeepMind.

## Verified identity and provenance

Google DeepMind model for predicting genomic sequence and variant effects on molecular properties; the API client, research implementation, and AlphaGenome Atlas are distinct assets.

## Source-scoped operating boundaries

- The public API repository contains client code; it is not the trained weights. The research implementation separately links pretrained weights and requires acceptance of non-commercial model terms. Its Apache-2.0 code license does not replace those weight terms. [API client](https://github.com/google-deepmind/alphagenome) · [Research code and model weights](https://github.com/google-deepmind/alphagenome_research).
- AlphaGenome Atlas contains precomputed predictions and is not a second trained model. Variant predictions are evidence for research and experimental follow-up, not a clinical diagnosis. [Model and Atlas boundary](https://deepmind.google/science/alphagenome/).

## Source evidence

- <https://deepmind.google/science/alphagenome/>
- <https://github.com/google-deepmind/alphagenome>
- <https://github.com/google-deepmind/alphagenome_research>
