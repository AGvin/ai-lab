# Granite 4.0 Nano

Granite 4.0 Nano is IBM's compact language-model family spanning 350M- and 1B-class dense and hybrid variants, each represented by distinct base and instruction-tuned weights.

## Model family boundaries

The dense and hybrid architectures are not interchangeable runtime targets. Base checkpoints are intended for adaptation; instruction-tuned checkpoints have a different training stage. Compact parameter classes do not establish memory use, latency, or task quality on a specific device. Verify the selected checkpoint and runtime independently.

## Models

| Checkpoint | Architecture | Role |
| --- | --- | --- |
| [Granite 4.0 1B Base](./sub/models/sub/granite-4-0-1b-base/) | Dense | Base |
| [Granite 4.0 1B](./sub/models/sub/granite-4-0-1b/) | Dense | Instruct |
| [Granite 4.0 350M Base](./sub/models/sub/granite-4-0-350m-base/) | Dense | Base |
| [Granite 4.0 350M](./sub/models/sub/granite-4-0-350m/) | Dense | Instruct |
| [Granite 4.0 H 1B Base](./sub/models/sub/granite-4-0-h-1b-base/) | H hybrid | Base |
| [Granite 4.0 H 1B](./sub/models/sub/granite-4-0-h-1b/) | H hybrid | Instruct |
| [Granite 4.0 H 350M Base](./sub/models/sub/granite-4-0-h-350m-base/) | H hybrid | Base |
| [Granite 4.0 H 350M](./sub/models/sub/granite-4-0-h-350m/) | H hybrid | Instruct |

## Official model resources

- [Granite 4.0 1B — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-1b)
- [Granite 4.0 1B Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-1b-base)
- [Granite 4.0 350M — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-350m)
- [Granite 4.0 350M Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-350m-base)
- [Granite 4.0 H 1B — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-h-1b)
- [Granite 4.0 H 1B Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-h-1b-base)
- [Granite 4.0 H 350M — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-h-350m)
- [Granite 4.0 H 350M Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.0-h-350m-base)

## License and deployment checks

The eight member checkpoints target constrained and on-device use cases. Their downloaded weights use Apache-2.0. Hosted-service terms and runtime-specific or quantized artifacts must be checked separately; an artifact does not establish a new trained-model identity.

Pin the checkpoint revision and runtime version. Preserve the selected checkpoint's configuration and verify architecture-specific kernel support. Evaluate precision, context-state memory and batch size together, then measure memory, latency and task quality on representative inputs. Dense and H hybrid variants require separate compatibility checks.

Published benchmark figures remain producer claims; this page does not report independently reproduced benchmarks or deployment tests.
