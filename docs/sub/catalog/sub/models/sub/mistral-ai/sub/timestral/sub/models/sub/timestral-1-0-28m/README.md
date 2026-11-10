# Timestral 1.0 28M

Timestral 1.0 28M is Mistral AI’s 28M-parameter time-series forecasting checkpoint in the October 2026 Timestral release.

## Translations

- English

## Relations

- Family: [Timestral](../../../../)

## Model profile

The patch-based transformer has 12 layers and an embedding width of 256; it processes numeric series, not chat tokens. [Timestral 28M released weights](https://huggingface.co/mistralai/Timestral-28M)

It accepts up to 32,768 time steps and forecasts 1,024 steps per forward pass, returning 21 quantiles. Longer forecasts feed each block’s median back as context. [Timestral 28M released weights](https://huggingface.co/mistralai/Timestral-28M)

The released weights are published by Mistral AI; its model card labels this release public preview. [Timestral 1.0 28M model card](https://docs.mistral.ai/models/timestral-1-0-28m)

## Operational boundaries

The Modified MIT weight license restricts use above US$20 million in preceding-month global consolidated company/employer revenue. The inference code’s Apache 2.0 license does not replace the weight license. [Timestral 28M Modified MIT license](https://huggingface.co/mistralai/Timestral-28M/blob/main/LICENSE)

Supply only covariates available at forecast time and preserve missing-value masks. Quantile outputs are model estimates, not guaranteed coverage; evaluate leakage and calibration on held-out time periods.

## Official resources

- [Timestral 28M released weights](https://huggingface.co/mistralai/Timestral-28M)
- [Timestral 1.0 28M model card](https://docs.mistral.ai/models/timestral-1-0-28m)
- [Timestral 28M Modified MIT license](https://huggingface.co/mistralai/Timestral-28M/blob/main/LICENSE)
- [Timestral inference code and input contract](https://github.com/mistralai/timestral)
