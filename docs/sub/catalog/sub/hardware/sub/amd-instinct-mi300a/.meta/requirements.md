# Documentation Requirements

## Requirements

- Identify AMD Instinct MI300A as the independently released server-class **CDNA 3 GPU + 24-core Zen 4 CPU APU** with **128 GB unified/coherent HBM3 per package** and up to **5.3 TB/s peak package memory bandwidth**, materially different from the discrete AMD MI300X 192 GB HBM3 OAM accelerator.
- Preserve the distinction between unified shared memory accessible to the APU's CPU/GPU and dedicated GPU-only VRAM on discrete accelerator modules. Do not describe the MI300A's 128 GB as a consumer-installable PCIe card or as a separate 128 GB allocation for CPU plus an additional 128 GB for GPU.
- Scope AMD's official APU SH5 socket packaging, qualified server platform, 550 W TDP / up to 760 W peak product envelope, Linux kernel, ROCm stack, firmware/BIOS, thermal design, host topology and Infinity Fabric integration to current first-party system acceptance criteria.
- Keep application-specific HPC/AI advantages distinct from MI300X/MI325X discrete accelerator throughput; software support, CPU-GPU memory sharing, availability and model execution performance depend on supported ROCm/OS/kernel release and exact server system.
- Preserve original **2023-12-06** launch/lifecycle evidence and source-backed 128 GB HBM3 package capacity. Do not infer the system aggregates of four or more MI300A APUs are single-APU capacities.
- Maintain AMD producer `produced-by` / `produces` reciprocal relation and distinguish AI-enabled APU identity from architecture/general CPU platform concepts.

## Validation

- CPU/GPU unified HBM3 is correctly distinguished from MI300X dedicated discrete accelerator memory.
- The 128 GB per-APU and 5.3 TB/s numbers are not conflated with multi-APU system aggregate.
- Packaging/power/ROCm support are not misrepresented as ordinary consumer GPU compatibility.
- The AMD producer inverse resolves for `catalog/hardware/amd-instinct-mi300a`.
