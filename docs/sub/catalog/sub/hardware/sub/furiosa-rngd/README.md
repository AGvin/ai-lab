# FuriosaAI RNGD

**PROVENANCE/OWNERSHIP REVIEW PENDING.** See the [provenance policy](../../../../../project/sub/policies/sub/russia-linked-ai/).

## Exact hardware scope

FuriosaAI RNGD is a 48 GB HBM3 PCIe Gen5 x16 inference NPU built around a Tensor Contraction Processor. Official 2026 developer documentation states a 150 W TDP, while Furiosa's product specification page states 180 W; treat this discrepancy as unresolved for host cooling and power budgeting. INT4/INT8 peak figures and SR-IOV capability are vendor specifications, not independent inference throughput.

## Deployment boundaries

RNGD is a data-center inference accelerator, not a complete NXT server, a model-hosting service or a generic Tensor Contraction Processor architecture. Validate supported SDK versions, virtual-function isolation, model fit, forced airflow for its passive cooling and the board's actual power envelope before physical deployment.

## Producer

- [FuriosaAI](../../../producers/sub/f/sub/furiosa-ai/).

## Original references

- [FuriosaAI official source 1](https://developer.furiosa.ai/v2026.1.0-rc2/en/overview/rngd.html)
- [FuriosaAI official source 2](https://furiosa.ai/renegade-spec)

No independent device execution, benchmark, full schema/cache/CI/render or legal/provenance audit was performed.
