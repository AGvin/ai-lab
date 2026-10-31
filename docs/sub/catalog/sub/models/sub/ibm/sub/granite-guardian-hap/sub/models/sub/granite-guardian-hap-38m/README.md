# Granite Guardian HAP 38M

IBM four-layer 38M English toxicity classifier for hateful, abusive and profane text. Calibrate output thresholds and measure false positives and negatives for the intended domain. It is not a general-purpose Guardian evaluator.

## Deployment and evidence

Published checkpoint weights use Apache-2.0; hosted-service and runtime-specific artifact terms are separate. Pin the exact checkpoint revision, tokenizer, output-label mapping and inference runtime. For English HAP screening or bulk annotation, measure memory, latency, throughput and precision/recall on representative inputs, and calibrate probability thresholds against false-positive and false-negative costs. IBM performance comparisons are producer-reported, not independently reproduced here; cache freshness and final rendering are not validated by this reader.

- [Granite Guardian HAP family](../../../../)
- [Official model card](https://huggingface.co/ibm-granite/granite-guardian-hap-38m)
