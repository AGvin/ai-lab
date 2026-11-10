# Granite 4.0 H 350M

Granite 4.0 H 350M is an IBM hybrid instruction-tuned language model in the Granite 4.0 Nano family. This separately released instruction-tuned model is distinct from its base-weight counterpart.

## Identity and deployment boundaries

This hybrid instruction-tuned checkpoint is a separate trained-model identity. Verify model-specific architecture support in the chosen runtime, and measure task quality, memory use, and latency on the target hardware. Parameter class alone does not establish deployment suitability.

## Family and official resource

- [Granite 4.0 Nano family](../../../../)
- [Official IBM model card](https://huggingface.co/ibm-granite/granite-4.0-h-350m)

## License and deployment checks

This checkpoint's downloaded weights use Apache-2.0. Hosted-service terms and runtime-specific or quantized artifacts must be checked separately; an artifact does not establish a new trained-model identity.

Pin the checkpoint revision and runtime version. Preserve the selected checkpoint's configuration and verify architecture-specific kernel support. Evaluate precision, context-state memory and batch size together, then measure memory, latency and task quality on representative inputs. Dense and H hybrid variants require separate compatibility checks.

Published benchmark figures remain producer claims; this page does not report independently reproduced benchmarks or deployment tests.
