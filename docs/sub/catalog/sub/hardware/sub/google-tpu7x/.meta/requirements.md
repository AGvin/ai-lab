# Documentation Requirements

## Requirements

- Identify Google TPU7x as the concrete seventh-generation TPU hardware release documented by Google Cloud and as the first release in the Ironwood family.
- Keep TPU7x hardware identity distinct from Cloud TPU as a hosted service, VM/pod/topology configuration, compiler/runtime software, and generic TPU architecture concepts.
- Preserve chip, memory, interconnect, numeric-format, topology, and system-scale facts only at the exact scope supported by current first-party documentation.
- Treat cloud regions, quotas, pricing, VM/runtime compatibility, available configurations, and performance claims as mutable service or deployment facts requiring current verification.
- Render the standard `entity-relations` block and preserve Google as the producer.

## Validation

- TPU7x is not collapsed with the Cloud TPU service or with every Ironwood system/configuration.
- Cloud availability and pricing are not presented as intrinsic timeless hardware facts.
- The `produces` / `produced-by` relation pair resolves consistently to Google.

## Scoped original-source acceptance — 2026-11-06

- Google Cloud documents TPU7x (Ironwood) as a chip with 192 GiB HBM, published BF16 peak 2307 TFLOPS, FP8 peak 4614 TFLOPS and 7380 GB/s memory bandwidth per chip. The tpu7x-standard-4t VM contains four chips with aggregate 768 GiB HBM. Google currently documents JAX/PyTorch support but not TensorFlow support for TPU7x; pod totals, VM quotas, access and Cloud TPU service terms are not chip specifications.
- Official source 1: https://docs.cloud.google.com/tpu/docs/tpu7x
- Official source 2: https://docs.cloud.google.com/compute/docs/tpus/tpu-machines
- This scoped qualification does not establish full freshness, general stock, vendor-neutral benchmarks, framework support, ownership/legal clearance, schema/CI/cache/render or physical hardware testing.
