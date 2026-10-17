# Microsoft Olive

Microsoft Olive is a self-managed model-optimization toolkit for transforming models through optimization, conversion, compression, quantization, packaging, and target-specific preparation.

## Software boundary

Olive is optimizer and artifact-transformation-first. Runtime integrations and deployment helpers are downstream targets and capabilities rather than an inference-runtime identity, while generic fine-tuning and model-development facts remain outside the profile unless they directly serve Olive's optimization workflow.

Supported passes, accelerators, runtimes, model formats, and version-specific features are freshness-sensitive.

## Telemetry

Olive's privacy guide documents telemetry enabled by default, including automatically collected application, device, and version information. It lists `--disable_telemetry` or `OLIVE_DISABLE_TELEMETRY=1` as controls for additional command, performance, and exception telemetry, and says telemetry is automatically disabled in detected CI/CD environments. When enabled telemetry cannot be sent to Microsoft, it can be cached locally and transmitted when connectivity returns.

## Relations

- Produced by [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/).

## Official resources

- [Microsoft Olive documentation](https://microsoft.github.io/Olive/)
- [Microsoft Olive repository](https://github.com/microsoft/Olive)
- [Privacy and telemetry](https://microsoft.github.io/Olive/privacy.html)
