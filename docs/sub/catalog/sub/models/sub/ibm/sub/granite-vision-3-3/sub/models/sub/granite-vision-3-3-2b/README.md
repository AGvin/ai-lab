# Granite Vision 3.3 2B

Granite Vision 3.3 2B is IBM's visual-document understanding checkpoint for image input and document-oriented image-to-text output, directed by English instructions. A newer Vision generation exists; this checkpoint remains the explicit parent of the specialist [Granite Vision 3.3 2B Embedding](../granite-vision-3-3-2b-embedding/).

## Task boundaries

Use for document-image understanding and extraction. Segmentation, doctags and multipage behavior are experimental and must not be represented as generally validated. Assess extraction accuracy, hallucinations and layout handling on representative documents. This generative interface is distinct from the derivative model's ColBERT-style page retrieval.

The published weights use Apache-2.0; hosted-service terms differ. Pin the checkpoint and runtime before measuring quality, memory and latency.

## Family and official source

- [Granite Vision 3.3 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-vision-3.3-2b)
