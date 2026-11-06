# Documentation Requirements

## Requirements

- Identify Megatron Core as NVIDIA's independently packaged, open-source composable library for large-scale model training, installed as megatron-core and imported through megatron.core.
- Place it under Model Development because its primary role is reusable training building blocks, model components, distributed optimizers, parallelism and training-time efficiency.
- Distinguish the Core library from the Megatron-LM reference training implementation even though they share a repository. Keep Megatron Bridge and other independently published NeMo products separate; ordinary internal kernels, parallelism modules and example recipes are not extra software identities.
- Preserve NVIDIA producer attribution from official documentation and explicit package contact metadata without asserting exclusive authorship.
- Explain that supported tensor/pipeline/data/context/expert parallelism and mixed precision require compatible model architecture, cluster topology and release configuration; do not generalize a specific benchmark to arbitrary hardware or workloads.
- Treat PyTorch, CUDA, communication libraries, Transformer Engine, package extras, Python requirements, checkpoint formats and model support as release-sensitive. Distinguish a tagged package from source main/dev and match installation guidance to that release.
- Keep Core's PyPI Production/Stable classifier separate from promises that every experimental branch feature or integration is stable.
- Use the selected release's actual LICENSE and component notices for licensing facts. Package metadata contains conflicting BSD and Apache labels; use the selected release's LICENSE and notices rather than inferring a blanket license from package classifiers or a README badge.
- Render the standard entity-relations block from validated current-entity relations and include official overview, installation, package and source references.

## Validation

- Megatron Core is a separately packaged training library, not a duplicate of Megatron-LM, a trained model or a hosted training service.
- Producer provenance is reciprocal to NVIDIA and every rendered destination resolves.
- Performance and compatibility claims remain configuration- and release-scoped.
