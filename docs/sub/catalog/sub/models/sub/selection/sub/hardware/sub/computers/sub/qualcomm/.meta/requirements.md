# Documentation Requirements

## Requirements

- Cover Snapdragon X-class Windows/PC systems where Qualcomm NPU/GPU/CPU is the intended on-device route.
- Identify exact Snapdragon X SKU, Windows/driver stack, ARM64 runtime availability, QNN/AI Hub/Windows ML backend, and supported model export/precision.
- Separate NPU-deployable local models from hosted Copilot/service features; service availability is not local model compatibility.
- Account for ARM64 application/runtime support and any emulation/fallback path that changes performance or memory.
- Measure context/cache, latency, memory, power/battery, and accepted-result quality under real PC workloads.
- Recheck Qualcomm AI Hub/device support and Windows execution-provider support before current recommendations.

## Validation

- ARM64 runtime compatibility is explicit.
- Cloud/service features are not treated as NPU model support.
- AI Hub compatibility remains provider-documented evidence, not independent benchmark proof.
