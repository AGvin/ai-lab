# Google TPU7x

Google TPU7x is Google's seventh-generation TPU hardware release and the first Cloud TPU release in the Ironwood family.

## Hardware boundary

TPU7x remains distinct from Cloud TPU as a hosted service, VM or pod and topology configurations, compiler/runtime software, and generic TPU architecture concepts. Chip, memory, interconnect, numeric-format, topology, and system-scale facts apply only at the scope supported by current first-party documentation.

Cloud regions, quotas, pricing, runtime compatibility, available configurations, and workload performance are mutable service or deployment facts.

## Relations

- Produced by [Google](../../../producers/sub/g/sub/google/).

## Official resources

- [Google Cloud TPU7x documentation](https://docs.cloud.google.com/tpu/docs/tpu7x)
- [Cloud TPU documentation](https://docs.cloud.google.com/tpu/docs)

## Scoped original-source qualification — 2026-11-06

Google Cloud documents TPU7x (Ironwood) as a chip with 192 GiB HBM, published BF16 peak 2307 TFLOPS, FP8 peak 4614 TFLOPS and 7380 GB/s memory bandwidth per chip. The tpu7x-standard-4t VM contains four chips with aggregate 768 GiB HBM. Google currently documents JAX/PyTorch support but not TensorFlow support for TPU7x; pod totals, VM quotas, access and Cloud TPU service terms are not chip specifications.

- Official source 1: https://docs.cloud.google.com/tpu/docs/tpu7x
- Official source 2: https://docs.cloud.google.com/compute/docs/tpus/tpu-machines

These manufacturer/source facts are not independent workload benchmarks, availability assurances, legal/ownership clearance or full schema/CI/cache/render and runtime verification.
