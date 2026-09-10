# Documentation Requirements

## Requirements

- Teach Pruning as removing parameters, connections, or structures according to an explicit criterion while distinguishing nominal sparsity from realized runtime acceleration.
- Establish an unchanged-model baseline and target deployment constraint before selecting pruning ratio, pattern, criterion, target components, or schedule.
- Record source checkpoint, pruning configuration, masks or structurally removed units, retraining/recovery configuration, and resulting artifact identity needed to reproduce the experiment.
- Compare several pruning levels when the acceptable quality/resource frontier is unknown and preserve intermediate checkpoints when they reduce recovery cost or clarify where capability loss begins.
- Evaluate immediately after pruning and again after any recovery fine-tuning so structural-removal effects remain distinguishable from retraining effects; keep a known-good pre-pruning rollback artifact.
- Verify that the actual runtime/compiler/kernel/accelerator or compacted representation can exploit the produced sparsity pattern before claiming acceleration.
- Measure serialized size, resident memory, latency, throughput, batch behavior, energy/power where relevant, and end-to-end application cost on the target system.
- Evaluate target quality together with long-tail capabilities, calibration, robustness, safety behavior, future fine-tuning headroom, and compare against smaller, quantized, distilled, or unpruned alternatives when relevant.

## Validation

- Zero weights, nominal sparsity, or theoretical FLOP reduction are not reported as realized acceleration without deployment evidence.
- Recovery tuning does not hide structural-removal regressions.
- Pruned artifacts remain reproducible and rollback-compatible.
