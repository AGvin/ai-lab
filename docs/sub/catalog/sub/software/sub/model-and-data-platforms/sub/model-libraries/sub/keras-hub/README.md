# KerasHub

An open-source pretrained-model library for [Keras](../../../model-development/sub/keras/), distributed as `keras-hub` and imported as `keras_hub`.

## Capabilities and software boundary

KerasHub provides pretrained architectures, weights, task APIs, backbones and preprocessing components for text, image and audio workflows. Presets connect model configuration and state with the relevant weights and processing assets. Models can be used for inference and fine-tuning through supported Keras backends.

KerasNLP was renamed to KerasHub; the legacy name is compatibility history within this identity. The KerasCV consolidation does not imply that every old vision API is interchangeable. Core Keras and remote model-hosting services retain separate roles.

## Compatibility, evidence and operations

The package metadata labels development Alpha, and upstream cautions that its 0.y.z APIs and saved-model compatibility may change. Choose the backend before importing Keras libraries and match the model, tokenizer/preprocessor, precision and accelerator configuration to the installed release.

Preprocessing and dependencies vary by release and platform. Multi-backend operation or optional TensorFlow imports do not guarantee a TensorFlow-free installation. The library uses Apache-2.0 licensing; downloaded pretrained models retain their own licenses and access conditions.

## Relations

- Produced by: [Keras Team](../../../../../../../producers/sub/k/sub/keras-team/)

## Official resources

- [KerasHub documentation](https://keras.io/keras_hub/)
- [Getting started and presets](https://keras.io/keras_hub/getting_started/)
- [Repository](https://github.com/keras-team/keras-hub)
- [Package and lifecycle metadata](https://pypi.org/project/keras-hub/)
- [KerasNLP rename and KerasCV consolidation announcement](https://github.com/keras-team/keras-hub/issues/1831)
