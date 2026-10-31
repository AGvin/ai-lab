# Jamba2 3B

Jamba2 3B is AI21 Labs' dense 3-billion-parameter model using the Jamba hybrid SSM-Transformer design. AI21 publishes the AI21-Jamba2-3B weights under Apache 2.0 and documents a 256K-token context window. [Primary source](https://www.ai21.com/blog/introducing-jamba2/)

## Model and artifact

AI21 identifies the 3B member as dense and based on its hybrid SSM-Transformer design. The official repository is `ai21labs/AI21-Jamba2-3B`; its model card states Apache 2.0 and a 256K-token context window. [Architecture and size](https://www.ai21.com/blog/introducing-jamba2/) · [Official model card](https://huggingface.co/ai21labs/AI21-Jamba2-3B)

## Access and operation

The weights are downloadable. AI21's current foundation-model table marks this member's API endpoint N/A, so family-level Studio language does not establish hosted access for 3B. For local evaluation, pin the revision, tokenizer/chat template, runtime and precision, and measure memory use with the intended context. On-device positioning does not guarantee full-context operation on every phone or computer. [Current endpoint table](https://docs.ai21.com/docs/jamba-foundation-models) · [Artifact and deployment guidance](https://huggingface.co/ai21labs/AI21-Jamba2-3B)

## Evaluation boundary

Test grounding, instruction following and language coverage on representative inputs. Treat retrieved documents as untrusted inputs, and keep permissions for external tools separate from generated instructions. The published context limit and vendor benchmark positioning do not establish application accuracy or operational safety.

## Relations

- Member of: [Jamba2](../../../../README.md)

## Official resources

- <https://www.ai21.com/blog/introducing-jamba2/>
- <https://docs.ai21.com/docs/jamba-foundation-models>
- <https://huggingface.co/ai21labs/AI21-Jamba2-3B>
