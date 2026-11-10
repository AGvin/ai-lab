# MLPerf Mobile v6.0

## Relations

- Produced by: [MLCommons](../../../producers/sub/m/sub/mlcommons/)

MLPerf Mobile v6.0 is MLCommons' released on-device AI inference benchmark suite, including new generative-language-model tests.

## Scope and boundaries

The June 2026 release uses Llama 3.2 1B Instruct, Llama 3.2 3B Instruct and Llama 3.1 8B Instruct with TinyMMLU and IFEval prompts for its LLM tests. These are workloads within the Mobile suite, separate from desktop MLPerf Client and datacenter MLPerf Inference.

CPU execution and selected NPU-accelerated backends have different device and software requirements. Interpret results with the exact app build, workload, device/SoC, memory, thermal behavior, drivers and accuracy criteria. A score from one supported path does not rank all phones or imply that every iOS/Android device supports every LLM test.

## Official resources

- [MLPerf Mobile v6.0 release](https://mlcommons.org/2026/06/mlperf-mobile-v6/)
- [MLPerf Mobile repository](https://github.com/mlcommons/mobile_app_open)
