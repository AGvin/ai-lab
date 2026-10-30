# Sarvam-105B

Sarvam-105B is Sarvam AI's **open-weight, 105B-plus-parameter Mixture-of-Experts reasoning and chat model**, released on **March 6, 2026**. Sarvam documents **128 sparse experts**, **Multi-head Latent Attention (MLA)** and a **128K-token context window** for its flagship chat endpoint.

## Architecture and evidence

The publisher reports approximately **12 trillion pre-training tokens** across multilingual, code, math and web data, and coverage of ten Indian languages plus English. The official documentation lists **Apache-2.0** for the released model. These are producer-sourced specifications; neither model size nor context limit demonstrates local hardware fit, throughput, or accuracy.

Sarvam's reported language, reasoning, coding and agentic benchmark comparisons are not independent AI Lab measurements. Exact evaluation setup and time window matter.

## Trained model versus access

The current `sarvam-105b` chat API route refers to this flagship model. Current Sarvam docs also list `sarvam-105b-conversations`, a **separately post-trained conversational variant** for real-time dialogue and voice agents. Do not collapse that variant into the base model or count it as a newly accepted model without its own intake. Sarvam-30B has been deprecated on the chat API. Prices, endpoint aliases, regions and availability remain freshness-sensitive.

## Translations

- English

## Relations

- Member of: [Sarvam family](../../../../)

## Official resources

- [Open-source release and architecture](https://www.sarvam.ai/blogs/sarvam-30b-105b)
- [Current Sarvam-105B model documentation](https://docs.sarvam.ai/api/getting-started/models/sarvam-105b)
- [Sarvam model catalog](https://docs.sarvam.ai/api/getting-started/models)
