# Documentation Requirements

## Requirements

- Identify Lightning / PyTorch Lightning as the open-source training framework that structures PyTorch model training, evaluation, checkpointing, logging, and distributed execution.
- Preserve the framework boundary around LightningModule/Trainer, callbacks, loggers, strategies, precision, checkpointing, and supported distributed backends without folding hosted Lightning AI services into the software node.
- Keep PyTorch as the underlying framework and DeepSpeed/FSDP/other distributed engines as integrations rather than Lightning-owned products.
- Treat supported PyTorch/Python versions, accelerators, distributed strategies, precision modes, logging/checkpoint integrations, release versions, and deprecations as freshness-sensitive.
- Attribute performance/scaling claims to exact Lightning/PyTorch/backend/hardware configurations.

## Validation

- Lightning remains a PyTorch-oriented training framework rather than the PyTorch core or Lightning cloud.
- Integrations do not transfer producer ownership.
- Producer provenance resolves to Lightning AI.
