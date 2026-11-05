# AWS Trainium3

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

AWS Trainium3 is Amazon Web Services' fourth-generation purpose-built AI accelerator chip.

## Hardware boundary

Trainium3 hardware remains distinct from the EC2 Trn3 UltraServer hosted-service and system surface that deploys it. Any performance or model-fit comparison must preserve chip count, HBM capacity and bandwidth, precision, server topology, Neuron software version, model artifact, workload, context, batch or concurrency, and cluster conditions.

Performance, pricing, EC2 region availability, cluster scale, software support, and service packaging are freshness-sensitive deployment facts rather than timeless chip identity.

## Relations

- Produced by [Amazon Web Services](../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [AWS Trainium3 and EC2 Trn3 UltraServers general availability](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-ec2-trn3-ultraservers/)

## Scoped original-source acceptance — 2026-11-05

AWS Trainium3 is a single purpose-built AI accelerator chip with 144 GB HBM3e and 4.9 TB/s peak chip memory bandwidth. Up to 144 chips, 20.7 TB HBM3e and 706 TB/s bandwidth describe the EC2 Trn3 UltraServer aggregate rather than a single chip. Trn3 and AWS Neuron are the server/service and runtime surfaces, not alternative chip identities. Current regions, SDK/framework versions, network topology, workload/model throughput, legal/control rights and access require separate verification.

No independent hardware benchmarking, model/runtime execution, full freshness/schema/CI/cache/render or ownership/legal clearance was performed.
