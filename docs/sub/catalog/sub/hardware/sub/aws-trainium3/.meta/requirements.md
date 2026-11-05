# Documentation Requirements

## Requirements

- Present AWS Trainium3 as AWS's fourth-generation purpose-built AI accelerator chip/hardware identity, distinct from the EC2 Trn3 UltraServer hosted-service/system surface that deploys it.
- Preserve exact chip count, HBM capacity/bandwidth, precision/data type, server topology, Neuron software/runtime version, model artifact, workload, context, batch/concurrency, and cluster conditions whenever model-fit/performance claims are recorded.
- Treat performance, pricing, EC2 availability/regions, cluster scale, software support, and service packaging as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The hardware entity does not collapse into the EC2 service identity merely because Trainium3 is consumed through AWS infrastructure.
- Producer provenance resolves to Amazon Web Services.

## Scoped original-source acceptance — 2026-11-05

- Original manufacturer source: https://aws.amazon.com/ec2/instance-types/trn3/
- AWS Trainium3 is a single purpose-built AI accelerator chip with 144 GB HBM3e and 4.9 TB/s peak chip memory bandwidth. Up to 144 chips, 20.7 TB HBM3e and 706 TB/s bandwidth describe the EC2 Trn3 UltraServer aggregate rather than a single chip. Trn3 and AWS Neuron are the server/service and runtime surfaces, not alternative chip identities. Current regions, SDK/framework versions, network topology, workload/model throughput, legal/control rights and access require separate verification.
- Preserve chip/card/system provenance and exact source limitations. No physical execution, current model/runtime benchmark, whole-catalog freshness/schema/CI/cache/render or full ownership/legal clearance was performed.
