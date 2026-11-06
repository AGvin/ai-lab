# Granite Guardian HAP 125M

IBM twelve-layer 125M English toxicity classifier for hateful, abusive and profane text. It is not a general-purpose generative Guardian evaluator.

## Evaluation

Calibrate output labels and thresholds for the intended English domain. Measure false positives, false negatives, contextual bias, throughput and accuracy against the 38M classifier. Published weights use Apache-2.0; hosted terms differ.

## Deployment and evidence

Pin the exact checkpoint revision, tokenizer, output-label mapping and inference runtime. Compare memory, latency, throughput, precision/recall and contextual bias against the 38M model on representative English inputs before setting classification thresholds. IBM benchmark comparisons are producer-reported, not independently reproduced here; runtime performance, cache freshness and final rendering are not validated by this reader.

- [Granite Guardian HAP family](../../../../)
- [Official model card](https://huggingface.co/ibm-granite/granite-guardian-hap-125m)
