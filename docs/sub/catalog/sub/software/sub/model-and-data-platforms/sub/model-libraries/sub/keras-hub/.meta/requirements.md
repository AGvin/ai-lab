# Documentation Requirements

## Requirements

- Identify KerasHub as the independently released, open-source Keras pretrained-model library installed as keras-hub and imported as keras_hub.
- Place it under Model Libraries: architectures, pretrained presets, weights/loaders, task APIs, backbones and preprocessors are its primary role, even when models support fine-tuning or training.
- Keep the core Keras framework and backend frameworks separate. The directly renamed KerasNLP project is historical identity/compatibility context, not a second current software node; do not promise unchanged KerasCV APIs from the consolidation announcement.
- Preserve Keras Team provenance from explicit package author metadata. Backend support, model hosting and individual model authorship do not establish producer ownership of the library.
- Preserve the package's Alpha classifier and the upstream 0.y.z compatibility caveat; a published non-prerelease distribution does not imply stable APIs or saved-model compatibility.
- Explain that backend selection is configured before importing Keras libraries and that a preset combines model configuration/state with weights and processing assets. Check backend, tokenizer/preprocessor, precision, accelerator and model compatibility against the installed release.
- Keep preprocessing/import behavior separate from installed dependencies. Current release notes describe Python/PyGrain changes, while dependency metadata still includes platform-specific tensorflow-text; do not infer a universal TensorFlow-free installation from multi-backend support or optional TensorFlow imports.
- Keep downloaded model licenses and access conditions separate from the library license. Model availability and support vary by preset and release.
- Render the standard entity-relations block from validated current-entity relations and include official documentation, package and repository references.

## Validation

- KerasHub is a local model library, not a remote model hub, core training framework or alias for every Keras-branded package.
- KerasNLP rename, KerasCV consolidation and current Alpha/API maturity remain distinct statements.
- The Keras Team producer relation is reciprocal and rendered destinations resolve.
