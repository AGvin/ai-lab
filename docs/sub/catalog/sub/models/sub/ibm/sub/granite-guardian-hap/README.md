# Granite Guardian HAP

IBM English toxicity-classification family with two separately trained checkpoints: a four-layer 38M model and a twelve-layer 125M model. HAP screens hateful, abusive, profane and other toxic text; it is distinct from generative Guardian risk evaluation.

## Decision boundaries

Compare quality and throughput on representative English data. Calibrate thresholds, evaluate false positives, false negatives and contextual bias. Classifier output does not guarantee safety. Member weights use Apache-2.0; hosted terms are separate.

## Deployment and evidence

Pin the selected 38M or 125M model revision, tokenizer, classification label mapping and inference runtime. Compare memory use, CPU/GPU latency, throughput and false-positive/false-negative rates on representative English data before choosing a threshold. IBM benchmark and latency comparisons are producer claims, not reproduced measurements here; runtime performance, cache freshness and final reader rendering remain unverified.

## Members

- [Granite Guardian HAP 38M](./sub/models/sub/granite-guardian-hap-38m/)
- [Granite Guardian HAP 125M](./sub/models/sub/granite-guardian-hap-125m/)

## Official resources

- [38M checkpoint](https://huggingface.co/ibm-granite/granite-guardian-hap-38m)
- [125M checkpoint](https://huggingface.co/ibm-granite/granite-guardian-hap-125m)
