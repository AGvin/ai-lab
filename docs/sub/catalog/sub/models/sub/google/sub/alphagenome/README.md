# AlphaGenome

Google DeepMind model for predicting genomic sequence and variant effects on molecular properties; the API client, research implementation, and AlphaGenome Atlas are distinct assets.

## Relations

- Produced by: [Google DeepMind](../../../../../producers/sub/g/sub/google-deepmind/)

## Source-scoped operating boundaries

- The public API repository contains client code; it is not the trained weights. The research implementation separately links pretrained weights and requires acceptance of non-commercial model terms. Its Apache-2.0 code license does not replace those weight terms. [API client](https://github.com/google-deepmind/alphagenome) · [Research code and model weights](https://github.com/google-deepmind/alphagenome_research).
- AlphaGenome Atlas contains precomputed predictions and is not a second trained model. Variant predictions are evidence for research and experimental follow-up, not a clinical diagnosis. [Model and Atlas boundary](https://deepmind.google/science/alphagenome/).

## Official resources

- <https://deepmind.google/science/alphagenome/>
- <https://github.com/google-deepmind/alphagenome>
- <https://github.com/google-deepmind/alphagenome_research>
