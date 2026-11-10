# Robostral Navigate 8B

Robostral Navigate 8B is Mistral AI’s embodied-navigation model, introduced in July 2026 for RGB observations and natural-language instructions.

## Translations

- English

## Relations

- Family: [Robostral](../../../../)

## Model profile

The 8B model predicts a next target location and orientation by pointing in the current image; it can use local-frame displacement when the target is outside the field of view. [Robostral Navigate release](https://mistral.ai/news/robostral-navigate/)

Mistral’s lifecycle register lists Robostral Navigate as active. Its release page offers contact with the robotics team rather than documenting a public weight download or serverless API. [Robostral Navigate lifecycle](https://legal.mistral.ai/ai-governance/models/robostral-navigate/) [Robostral Navigate release](https://mistral.ai/news/robostral-navigate/)

## Operational boundaries

A single RGB camera is the model’s documented observation interface. Navigation benchmark results do not establish collision avoidance, fail-safe actuation or safe operation on every robot. Robot control and physical safeguards remain separate system responsibilities. [Robostral Navigate technical report](https://arxiv.org/abs/2607.20785)

## Official resources

- [Robostral Navigate release](https://mistral.ai/news/robostral-navigate/)
- [Robostral Navigate lifecycle](https://legal.mistral.ai/ai-governance/models/robostral-navigate/)
- [Robostral Navigate technical report](https://arxiv.org/abs/2607.20785)
