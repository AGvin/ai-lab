# Timestral

Timestral is Mistral AI’s family of numeric time-series foundation models, released on October 15, 2026.

## Translations

- English

## Relations

- Producer: [Mistral AI](../../../../../producers/sub/m/sub/mistral-ai/)
- Model: [Timestral 1.0 123M](./sub/models/sub/timestral-1-0-123m/)
- Model: [Timestral 1.0 209M](./sub/models/sub/timestral-1-0-209m/)
- Model: [Timestral 1.0 28M](./sub/models/sub/timestral-1-0-28m/)
- Model: [Timestral 1.0 5M](./sub/models/sub/timestral-1-0-5m/)

## Scope and status

Four independently released sizes—5M, 28M, 123M and 209M—produce probabilistic forecasts from univariate or multivariate histories and covariates. [Timestral release](https://mistral.ai/news/timestral/)

## Operational boundaries

Time steps and forecast horizons are numeric-series units, not LLM token context. The inference code uses Apache 2.0; released model weights use their own Modified MIT licenses. [Timestral inference code and input contract](https://github.com/mistralai/timestral)

Forecasts are estimates. Evaluation must respect time ordering and use only information available when each forecast would have been made.

## Official resources

- [Timestral release](https://mistral.ai/news/timestral/)
- [Timestral inference code and input contract](https://github.com/mistralai/timestral)
