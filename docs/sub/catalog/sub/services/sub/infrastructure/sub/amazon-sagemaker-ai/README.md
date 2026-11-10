# Amazon SageMaker AI

Amazon SageMaker AI is Amazon Web Services' managed platform for developing, training, optimizing, deploying and monitoring machine-learning models and their inference infrastructure. Its custom-model endpoints and managed training lifecycle make it an infrastructure service, not a single trained-model family or ordinary hosted foundation-model API. [SageMaker AI](https://aws.amazon.com/sagemaker/ai/).

## Model deployment and service boundary

SageMaker AI supports real-time, serverless, asynchronous and batch inference patterns. They represent deployment modes of the same service, not independent canonical services. Training jobs, Studio, pipelines, model registries and SDKs are related product functions. Amazon Bedrock and Amazon Bedrock AgentCore have different model-access and managed-agent runtime boundaries. [Inference options](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html).

## Lifecycle and operations

AWS's **July 30, 2026** new-customer access restrictions apply to named legacy SageMaker AI capabilities, not to the entire SageMaker AI platform. Verify exactly which feature is available to the target account. Region, GPU/instance type, container/runtime, supported framework, IAM/VPC network controls, data storage, scaling, quotas and end-to-end billing remain deployment-specific. Do not extrapolate benchmark throughput to different models or hardware. [SageMaker AI features](https://aws.amazon.com/sagemaker/ai/features/).

## Relations

- Produced by [Amazon Web Services](../../../../../producers/sub/a/sub/amazon-web-services/).

## Official resources

- [SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
- [Deployment options](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html)
- [Real-time inference endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
