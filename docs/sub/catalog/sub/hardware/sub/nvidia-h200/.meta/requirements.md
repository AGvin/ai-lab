# Documentation Requirements

## Requirements

- Identify NVIDIA H200 as a released NVIDIA Hopper-generation data-center Tensor Core GPU for AI inference/training and HPC, with **141 GB HBM3e** and up to **4.8 TB/s per-GPU peak memory bandwidth** per NVIDIA's published data.
- Separate NVIDIA H200 SXM and H200 NVL/PCIe-class packaging: published maximum power, interconnect, rack/system compatibility, cooling, and MIG partition availability differ, so do not imply a uniform plug-in form factor or consumer workstation compatibility.
- Distinguish H200 GPU memory and bandwidth from H100 80 GB HBM3, older A100 80 GB HBM2e, NVIDIA HGX/DGX H200 eight-GPU server totals and hosted H200 cloud-instance products; individual GPU bandwidth does not scale automatically with host topology.
- Treat pricing, deployment region, drivers, CUDA/TensorRT-LLM, virtual GPU/MIG support, NVLink arrangement, thermal design and inference performance as mutable source- and platform-scoped statements.
- Scope marketing throughput improvements to the workload, batch size, GPU count, precision, input/output tokens, cache state, software version and benchmark configuration. Do not assume a claimed model speedup is universal.
- Maintain NVIDIA first-party product references and the exact reciprocal producer relation.

## Validation

- 141 GB/4.8 TB/s applies to an individual H200 GPU, not an eight-GPU node.
- H200 SXM and H200 NVL published form-factor and power differences remain explicit.
- H200, H100, A100 and DGX H200 are distinct hardware identities.
- The NVIDIA `produces` link inverses this exact `produced-by` relation.
