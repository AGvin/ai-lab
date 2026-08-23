# Documentation Requirements

## Requirements

- Cover Intel PCs where Intel NPU/iGPU/CPU is the intended local inference route, especially Core Ultra/OpenVINO-class systems.
- Identify exact CPU/platform generation, NPU/iGPU availability, OS, OpenVINO/Windows ML or other backend, supported model/export/precision, and memory budget.
- Distinguish NPU, iGPU, and CPU execution; a device marketed as an AI PC does not mean the intended model benefits from the NPU.
- Record operator/model partitioning and CPU/GPU fallback where it affects latency/power.
- Measure context/cache memory, prompt/decode or task latency, sustained power/thermals, and accepted-result quality on the selected device/backend.
- Route to `cpu/` when no useful supported accelerator path exists for the intended workload.

## Validation

- NPU presence is not equated with model support.
- Exact OpenVINO/backend/device route is pinned.
- Marketing TOPS does not substitute for workload measurement.
