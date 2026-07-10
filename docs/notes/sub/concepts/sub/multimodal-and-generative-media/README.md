# Multimodal and Generative Media

Concepts for models and workflows involving images, audio, video, and combinations of modalities.

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`vision-language-models/`](./sub/vision-language-models/) — Models that jointly process visual inputs and natural language.
- [`image-generation/`](./sub/image-generation/) — Producing images from text, images, layouts, masks, or other conditioning inputs.
- [`diffusion-models/`](./sub/diffusion-models/) — Generative models that learn to reverse a progressive noising process.
- [`image-to-image/`](./sub/image-to-image/) — Generating a transformed image while conditioning on an existing image.
- [`inpainting/`](./sub/inpainting/) — Regenerating selected masked regions of an image.
- [`controlnet/`](./sub/controlnet/) — Conditioning diffusion models with structural controls such as edges, depth, or pose.
- [`multimodal-context/`](./sub/multimodal-context/) — Combined text, image, audio, video, or document information available to a model request.

## Useful

- [`text-to-image/`](./sub/text-to-image/) — Generating images from natural-language descriptions.
- [`outpainting/`](./sub/outpainting/) — Extending an image beyond its original boundaries.
- [`image-embeddings/`](./sub/image-embeddings/) — Vector representations used to compare, retrieve, or classify visual content.
- [`speech-to-text/`](./sub/speech-to-text/) — Converting spoken audio into written text.
- [`text-to-speech/`](./sub/text-to-speech/) — Synthesizing spoken audio from written text.
- [`video-generation/`](./sub/video-generation/) — Producing or transforming sequences of visual frames with generative models.

## Specialized

- [`latent-space/`](./sub/latent-space/) — A compressed learned representation in which generative models encode and manipulate information.
- [`audio-generation/`](./sub/audio-generation/) — Producing music, speech, sound effects, or other audio with generative models.
