# ChipBench

**ChipBench** — RTL generation, debugging and cross-language reference-model evaluation.

## Data and evaluation boundary

The publisher describes Verilog generation tasks, buggy RTL debugging tasks with references and tests, and Python/CXXRTL/SystemC reference-model tasks. Its `sv-generate` scripts and Make/Docker workflows are evaluation tooling, not separate dataset identities.

The [pinned first-party README](https://github.com/zhongkaiyu/ChipBench/blob/b4ba3a06759804ec88c26c3cf15b28b9a90b3443/README.md) is the identity and version source. Data, benchmark tasks, evaluator software, trained models and published leaderboards must be attributed separately.

## Rights, limitations and safety

The root LICENSE contains MIT terms with NVIDIA Research Projects copyright. This does not alone establish rights for all underlying HDL problems, third-party IP blocks or external toolchains. Generated RTL must be isolated and functionally checked before hardware use.

No Docker image, Verilog simulation, generated RTL or physical chip workflow was run. No complete rights audit or repository-wide validation was run.

## Official source snapshot

- [Repository](https://github.com/zhongkaiyu/ChipBench)
- [Pinned README](https://github.com/zhongkaiyu/ChipBench/blob/b4ba3a06759804ec88c26c3cf15b28b9a90b3443/README.md)
- [Pinned LICENSE](https://github.com/zhongkaiyu/ChipBench/blob/b4ba3a06759804ec88c26c3cf15b28b9a90b3443/LICENSE)
