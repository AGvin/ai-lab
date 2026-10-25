# Granite 4.0 1B

IBM Granite 4.0 1B is a separately released instruction-tuned language model in the Granite 4.0 Nano family. It is distinct from the base-weight and hybrid variants.

## Model identity and boundaries

This is the dense, instruction-tuned 1B-class member. Validate runtime support, task quality, memory usage, and latency for the intended deployment; parameter class alone does not establish hardware fit.

## Family and resources

- [Granite 4.0 Nano family](../../../../)
- [Official IBM Granite 4.0 1B model card](https://huggingface.co/ibm-granite/granite-4.0-1b)

## License and deployment checks

This checkpoint's downloaded weights use Apache-2.0. Hosted-service terms and runtime-specific or quantized artifacts must be checked separately; an artifact does not establish a new trained-model identity.

Pin the checkpoint revision and runtime version. Preserve the selected checkpoint's configuration and verify architecture-specific kernel support. Evaluate precision, context-state memory and batch size together, then measure memory, latency and task quality on representative inputs. Dense and H hybrid variants require separate compatibility checks.

Published benchmark figures remain producer claims; this page does not report independently reproduced benchmarks or deployment tests.
