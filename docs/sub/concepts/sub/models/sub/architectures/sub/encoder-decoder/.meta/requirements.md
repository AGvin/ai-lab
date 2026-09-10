# Documentation Requirements

## Requirements

- Use the reader-facing title `Encoder-Decoder Architectures`.
- Define the general architectural roles: an encoder transforms source input into one or more internal/contextual representations, while a decoder produces or reconstructs target output conditioned on relevant internal state, encoded source information, prior output context, or some combination defined by the architecture.
- Explain an encoder-decoder architecture as a composition that separates source representation from target production or reconstruction, without requiring one neural architecture family, modality, sequence type, or information-transfer mechanism.
- Distinguish the general encoder-decoder pattern from Transformer-specific encoder/decoder blocks. Recurrent, convolutional, Transformer, multimodal, autoencoding, and other architectures can instantiate encoder and decoder roles differently.
- Explain that early sequence-to-sequence systems compressed source information into a fixed-size representation, while attention-based and other designs can expose richer or variable source representations to the decoder; a single fixed-length bottleneck is therefore not part of the universal definition.
- Treat cross-attention as a common mechanism for connecting encoded source representations to a decoder, especially in Transformers, but not as a universal requirement of every encoder-decoder architecture.
- Distinguish encoder-only and decoder-only architectures as related role-specialized designs rather than implying they are themselves complete encoder-decoder pairs. Do not define encoders as inherently bidirectional or decoders as inherently autoregressive.
- Explain that autoregressive decoding is one important output-generation pattern, while non-autoregressive, parallel, iterative, reconstruction, classification/head-based, and other output mechanisms can use decoder-like or encoder/decoder roles depending on the architecture.
- Keep training objective separate from architectural role: masked modeling, next-token prediction, denoising, translation objectives, reconstruction, and other objectives may be paired with encoder, decoder, or encoder-decoder structures without defining those structures universally.
- Avoid turning common task associations into architectural guarantees. Encoder-only does not inherently mean embeddings/classification, decoder-only does not inherently mean chat/general-purpose generation, and encoder-decoder does not inherently mean translation/summarization.
- Keep concrete model families, task benchmarks, runtime/cache behavior, parameter comparisons, model-selection recommendations, and deployment guidance with their applicable catalog, evidence, inference, or decision owners.
- Use the canonical entity references as research inputs for historical and current encoder-decoder boundaries when reader-facing rendering is activated.

## Validation

- The page does not equate encoder-decoder architecture with Transformers or one sequence-to-sequence implementation.
- Encoders are not universally described as bidirectional and decoders are not universally described as autoregressive.
- Fixed-length bottlenecks and cross-attention are described as design variants rather than universal requirements.
- Architecture roles are kept separate from training objectives and common task/product interfaces.
- Encoder-only, decoder-only, and encoder-decoder task associations are presented as common usage patterns at most, not intrinsic suitability guarantees.
- Legacy product/model-selection advice is not duplicated into this canonical architecture concept.
