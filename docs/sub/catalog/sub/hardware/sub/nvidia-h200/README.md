# NVIDIA H200 Tensor Core GPU

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Manufacturer attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

NVIDIA H200 Tensor Core GPU is a Hopper data-center accelerator for AI training, inference and scientific computing. NVIDIA publishes 141 GB HBM3e memory and 4.8 TB/s peak memory bandwidth per GPU. These figures do not describe the combined memory of an HGX or DGX multi-GPU system. H100 80 GB HBM3 and A100 80 GB HBM2e are separate accelerator identities.

## Deployment boundaries

H200 SXM and H200 NVL have different integration boundaries. The current NVIDIA table lists SXM up to 700 W and NVL PCIe up to 600 W, both configurable, with distinct interconnect and MIG layouts. Its specification footnote marks these figures as preliminary and subject to change; confirm the delivered OEM configuration.

Choose a qualified server with the appropriate power, cooling, baseboard and topology. A PCIe NVL card is not equivalent to an SXM module, and NVLink does not remove software parallelism requirements. Model fit, precision, batch size, context length and runtime determine usable capacity and measured throughput. Vendor comparisons apply to their stated workloads and baselines. Software entitlement, cloud instance packaging, regional availability and support require separate current checks.

## Producer

- Produced by [NVIDIA](../../../producers/sub/n/sub/nvidia/README.md).

## Source interpretation

NVIDIA identifies H200 as a Hopper GPU with 141 GB HBM3e and 4.8 TB/s published memory bandwidth per GPU. SXM and NVL integration, power and interconnect configurations differ. These figures are not system-total memory or measured application throughput; delivered OEM and software configurations need separate checks.

This bounded source review does not establish current pricing, local availability, full specification freshness, software entitlements or measured performance. No hardware or runtime validation was performed.

## Official resources

- [H200 SXM/NVL specifications and technical resources](https://www.nvidia.com/en-us/data-center/h200/)
