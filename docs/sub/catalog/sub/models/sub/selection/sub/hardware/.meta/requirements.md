# Documentation Requirements

## Requirements

- Present this journey for readers whose hardware is already owned/fixed and who need to select practical models for it.
- Route first by hardware class: `mobile/`, `computers/`, `single-board/`, `embedded/`, `servers/`.
- Define practical fit as the intersection of exact compute target, supported runtime/model format, usable memory, precision/quantization, context/cache headroom, modality support, measured latency/throughput, thermals/power, concurrency, and accepted-result quality.
- State that successful loading/conversion, published artifact size, nominal RAM/VRAM, parameter count, or TOPS alone do not prove practical fit.
- Treat unmeasured or unsupported combinations as `Unknown`; distinguish official support, AI Lab measurement, independent measurement, inference, and untested states.
- Link canonical model facts from Model Reference and runtime/software/hardware facts from their canonical owners rather than duplicating full profiles.
- Keep hardware purchasing outside this journey. Existing-hardware limitations may trigger a hosted/hybrid/different-hardware escalation, but the page does not choose what device to buy.
- Keep `decision-guides/local-resource-fit/` as the model-first inverse route and cross-link it when the reader starts from a specific artifact instead of a device.
- Recheck mutable drivers, OS/toolkit versions, runtime backends, supported devices/operators/models, exports/quantizations, and platform APIs before current recommendations.
- Require substantive child pages only; every materialized child in this package has a distinct runtime/compatibility route.

## Validation

- Exactly five first-level groups are materialized: mobile, computers, single-board, embedded, servers.
- Edge/local/cloud are not treated as hardware classes.
- No page becomes a hardware catalog or buying guide.
- Runtime/platform support is not transferred between OS/device/vendor generations without evidence.
- Multi-accelerator capacity is not inferred from simple memory sums.
