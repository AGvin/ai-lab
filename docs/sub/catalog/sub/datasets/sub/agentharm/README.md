# AgentHarm

**AgentHarm** is an original AI-agent safety benchmark introduced in **2024** by a joint research team from **Gray Swan AI** and the **UK AI Safety Institute** (now UK AI Security Institute). It measures how tool-using LLM agents respond to harmful multi-step requests: whether they refuse, and what happens if an agent attempts to follow such requests. The [original research paper](https://arxiv.org/abs/2410.09024) was later published at ICLR 2025. It is **not** a jailbreak product, exploitation guide, agent implementation or broad certification of AI safety.

## Scope, versions and interpretation

The original [institute's research summary](https://www.aisi.gov.uk/research/agentharm-a-benchmark-for-measuring-harmfulness-of-llm-agents) describes **110 harmful base behaviors, 440 cases after augmentations, and 11 harm categories**. The actual [original public dataset](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) initially exposes **44 public-test base behaviors (176 augmented cases)** and **8 validation base behaviors (32 augmented cases)**, not the full paper's private-test inventory. Matched benign examples help reveal over-refusal; harmful, benign and chat-only configurations are dataset views, **not separate independent benchmark identities**. The Hub's aggregate row count is not interchangeable with the research paper's 440-case experimental inventory.

AgentHarm focuses on deliberate misuse of **agents with tools** and evaluates refusal alongside multi-step task completion with task-specific graders. This differs from **AgentDojo**, which centers on prompt injection into agents pursuing legitimate tasks, and from **AILuminate**, which evaluates broader generative-AI safety configurations. A model's AgentHarm score does not certify safety in production, and low success on one malicious subset cannot guarantee it rejects other abuse.

The original benchmark release and later [Inspect Evals AgentHarm implementation](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm) must be versioned separately. Maintainer documentation describes several grading/refusal/tool-call corrections in **2026**, including versions 3-B through 8-B; it names **6-B** as the recommended revision until a wider review. Pin the dataset/split and grader revision, judge model, allowed tools, prompting and actual model/agent configuration before comparing any reported result. No benchmark execution or score replication was performed for this entry.

## License, provenance and safety controls

The publisher's dataset card labels the license [`other`](https://huggingface.co/datasets/ai-safety-institute/AgentHarm), with a [specific LICENSE](https://huggingface.co/datasets/ai-safety-institute/AgentHarm/blob/69e7a23c331a75d4e438a65233a4f8b459fe95c7/LICENSE): **MIT-style text plus an additional restriction prohibiting purposes other than improving AI safety and security**. This is **not unrestricted MIT**, and standard-MIT licensing on the broader Inspect Evals codebase does not override the dataset's purpose restriction. Review license and access fit before commercial, republished, adapted or other uses.

The original paper and dataset acknowledge **both Gray Swan AI and the UK AI Safety Institute** as developers. Both organizations now have canonical producer profiles with reciprocal research-provenance links. Their joint contribution does **not** establish either organization's exclusive intellectual-property ownership or override the original dataset license.

**Risk boundary:** The source corpus deliberately contains harmful or offensive scenarios. Do not train on the evaluation prompts, treat its canary as a data-leak warning, or replay misuse instructions against real services. Safety research should use isolated, permissioned, synthetic tool environments, controlled network/file access, test credentials and budget-limited model calls. Never copy public attack examples into operational workflows or assume test logs are safe to share. This documentation neither imports unsafe prompts nor executes the evaluator.

## Provenance

- Co-developed and published with the [UK AI Security Institute](../../../producers/sub/u/sub/uk-ai-security-institute/) (known as the UK AI Safety Institute during original research).
- Jointly developed with [Gray Swan AI](../../../producers/sub/g/sub/gray-swan-ai/), now independently qualified as a producer. This is the same original dataset and does not add another benchmark identity.

## Original resources

- [Original AISI dataset and split/license card](https://huggingface.co/datasets/ai-safety-institute/AgentHarm)
- [Dataset's purpose-restricted LICENSE](https://huggingface.co/datasets/ai-safety-institute/AgentHarm/blob/69e7a23c331a75d4e438a65233a4f8b459fe95c7/LICENSE)
- [UK institute's research publication](https://www.aisi.gov.uk/research/agentharm-a-benchmark-for-measuring-harmfulness-of-llm-agents)
- [Gray Swan AI research publication](https://www.grayswan.ai/research/agentharm)
- [Original AgentHarm research paper](https://arxiv.org/abs/2410.09024)
- [Maintained Inspect Evals AgentHarm reference](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm)
