# CoCoNot

**CoCoNot** is an evaluation resource from Allen Institute for AI for studying when a language model should decline a request and when it should not over-refuse.

## Dataset composition

The [pinned publisher README](https://github.com/allenai/noncompliance/blob/25bf77cc668814360405cdb8197c4368205806c7/README.md) distinguishes an **Original Set** (1,001 evaluation and 11,477 supervised fine-tuning examples) from a **Contrast Set** (379 evaluation examples and 927 preference examples). Those configurations belong to one benchmark family; a training set, evaluation split and scoring script are not independent product identities.

The original [Hugging Face release](https://huggingface.co/datasets/allenai/coconot) carries downloadable data. The publisher's evaluation process invokes Open-Instruct, a separately maintained inference/evaluation implementation. Reproducibility depends on task split, prompt context, model revision, and the definition of acceptable refusals.

## License, safety and interpretation

The source [MIT LICENSE](https://github.com/allenai/noncompliance/blob/25bf77cc668814360405cdb8197c4368205806c7/LICENSE) applies to covered repository materials; separately hosted data, original seed prompts, model outputs and evaluation dependencies may carry additional conditions. Handle potentially unsafe prompts responsibly and distinguish justified refusals from excessive rejection of benign requests.

No download, live evaluation, scoring replication, complete rights check or clean pass was performed.

## Official source snapshot

- [Upstream repository](https://github.com/allenai/noncompliance)
- [Pinned README](https://github.com/allenai/noncompliance/blob/25bf77cc668814360405cdb8197c4368205806c7/README.md)
- [Pinned root LICENSE](https://github.com/allenai/noncompliance/blob/25bf77cc668814360405cdb8197c4368205806c7/LICENSE)
