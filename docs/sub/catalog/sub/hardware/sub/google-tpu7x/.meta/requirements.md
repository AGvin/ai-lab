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
