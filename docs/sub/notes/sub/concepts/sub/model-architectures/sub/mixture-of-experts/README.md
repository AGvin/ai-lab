# Mixture of Experts

Mixture of Experts (MoE) is a sparse architecture in which a router selects a subset of expert networks to process each token or input.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

In many transformer MoE models, experts replace or augment selected feed-forward blocks. A router scores the available experts and activates a small number, often called the top-k experts, for each token.

This allows a model to contain substantially more total parameters than it activates for one token. The architecture increases model capacity without requiring every expert to run for every token.

MoE is a common sparse architecture, but sparse architecture is the broader category.

## Components

- **Shared model components** — embeddings, attention layers, normalization, and other blocks used by all tokens, depending on the design.
- **Experts** — alternative parameterized subnetworks, commonly feed-forward blocks.
- **Router or gating network** — scores experts for each token or input.
- **Top-k selection** — chooses the experts that receive the token.
- **Combination step** — merges selected expert outputs using routing weights or another defined method.
- **Load-balancing mechanism** — discourages routing collapse and excessive concentration on a small subset of experts.

Architectures vary. Do not assume every MoE model uses the same number of experts, routing method, shared experts, or top-k value.

## Total and active parameters

MoE documentation should distinguish:

| Measure | Meaning |
| --- | --- |
| Total parameters | All shared and expert parameters in the complete model |
| Active parameters | The approximate parameters participating in one token's selected computation path |

A notation such as `100B total / 10B active` describes two different operational properties:

- total parameters primarily influence artifact size, loading, and memory residency;
- active parameters more directly influence arithmetic work per token;
- neither value alone predicts latency, throughput, or quality.

Active parameters are not always a simple multiple of one expert size. Shared layers, shared experts, routing design, and implementation details must be included when the model publisher defines the count.

## Practical implications

### Capacity and compute

MoE can increase total capacity without proportional per-token arithmetic. This can improve quality per unit of theoretical compute, but real results depend on training quality, expert utilization, and serving implementation.

### Memory and storage

Inactive experts still normally need to be stored and available. A model with 10B active parameters can require memory closer to its full total parameter count than to a dense 10B model.

Quantization can reduce that memory requirement, but it does not change the MoE architecture or the total-versus-active distinction.

### Runtime support

Efficient inference requires support for routing, expert dispatch, batching, memory placement, and output combination. A runtime that can load an MoE model may still execute it inefficiently.

### Multi-device deployment

Experts may be distributed across GPUs or nodes. Token dispatch can then create communication overhead, synchronization cost, and uneven device utilization. Interconnect bandwidth and expert placement become important parts of hardware fit.

### Local inference

MoE can be useful locally when all weights fit in available RAM or VRAM and the runtime implements the architecture efficiently. The active count alone must not be used as the memory requirement.

CPU offloading or split placement may make a model loadable while still producing poor latency.

### Batching and load balance

Large batches can improve expert utilization, while small interactive batches may expose routing overhead. Uneven routing can overload popular experts and leave other capacity underused.

## Use in model documentation

Record reliable fields separately:

```text
Architecture: Sparse — MoE
Total parameters: <value or Unknown>
Active parameters: <value or Unknown>
Experts: <count or Unknown>
Experts selected per token: <value or Unknown>
Shared experts: <value or Not documented>
Runtime notes: <relevant support or placement constraints>
```

Do not derive undocumented values from naming conventions or divide total parameters by expert count without an authoritative architecture description.

## Common mistakes

- Treating total parameters as per-token compute.
- Treating active parameters as storage or VRAM requirements.
- Assuming inactive experts consume no memory.
- Comparing an MoE model with a dense model using only total parameters.
- Assuming every expert represents a clean human-readable subject domain.
- Assuming a model is faster merely because the active count is smaller.
- Ignoring routing, batching, communication, and runtime implementation.
- Treating MoE as a model scale class or a synonym for frontier.

## Related concepts

- [Model Architectures](../../)
- [Dense and Sparse Architectures](../dense-and-sparse-architectures/)
- [Small and Large Language Models](../../../model-classification/sub/language-model-scale/)
- [Model Loading](../../../inference-and-serving/sub/model-loading/)
- [GPU Offloading](../../../inference-and-serving/sub/gpu-offloading/)
- [Throughput](../../../inference-and-serving/sub/throughput/)
- [Continuous Batching](../../../inference-and-serving/sub/continuous-batching/)
