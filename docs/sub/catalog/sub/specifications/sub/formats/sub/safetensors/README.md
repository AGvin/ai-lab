# Safetensors

Safetensors is an upstream tensor-serialization format with a defined metadata/header representation, tensor metadata and offsets, and tensor payload region.

## Format boundary

The formal contract defines the file layout and validity constraints. Its safety properties apply only as described by the upstream format and implementation documentation; they do not make an arbitrary model artifact trusted or operationally safe. Sharding indexes, framework adapters, model-hub repository conventions, and higher-level checkpoint packaging are separate unless the upstream format explicitly makes them normative.

Safetensors serialization does not imply framework or runtime support, model quality, architecture compatibility, tokenizer compatibility, licensing or redistribution rights, or workload fit. Those concerns remain with software, model, evidence, and decision owners.

## Official resources

- [Safetensors documentation](https://huggingface.co/docs/safetensors/index)
- [Safetensors repository](https://github.com/huggingface/safetensors)
