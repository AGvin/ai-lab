# Documentation Requirements

## Requirements

- Identify Gray Swan AI as a first-party AI safety/security research and product organization, distinct from the benchmark dataset AgentHarm and its other security testing, red-teaming and runtime offerings.
- Official [About](https://www.grayswan.ai/about) and [research](https://www.grayswan.ai/research) identify AI security assessment and original research; avoid treating vendor comparative/marketing claims as independently validated protection or safety certifications.
- Preserve **joint original AgentHarm authorship** by Gray Swan researchers and the UK AI Safety Institute, explicitly documented in Gray Swan's [October 14, 2024 announcement](https://www.grayswan.ai/blog/agentharm). Do not replace or downgrade the institute's existing reciprocal producer relation.
- Link `catalog/producers/g/gray-swan-ai` `produces` to existing `catalog/datasets/agentharm`, and add a second reciprocal `produced-by` relation on AgentHarm. Two supported originating organizations do not double the dataset's catalog identity or mean both have independently transferable legal ownership rights.
- The original AgentHarm benchmark dataset has a purpose-restricted MIT-like license; software implementations and research papers can have separate terms. Clarify that research attribution does not grant unrestricted rights to benchmark data, underlying harmful prompts or evaluation tools.
- Do not present unsafe benchmark prompts or red-team exploits. Legitimate assessments must be authorized, isolated, logged safely and limited to controlled environments with synthetic credentials and model usage budgets.
- Enterprise safety product features, model compatibility, policies, guarantees and prices may change. No marketing performance ranking, actual exploit deployment, product integration, sensitive dataset import, full rights audit, full CI or whole-catalog clean pass is claimed.

## Validation

- Producers G lists Gray Swan AI once and the existing AgentHarm dataset has two reciprocal original-producer links.
- AgentHarm's existing publisher, purpose-restricted license, research scope and non-execution caveats remain unchanged.
