# Documentation Requirements

## Requirements

- Identify WeatherNext as Google DeepMind's AI weather-forecasting model family.
- Preserve family identity separately from concrete releases, Google product integrations, hosted forecast datasets/APIs, Weather Lab, and traditional numerical weather-prediction systems.
- Keep model architecture, training inputs, forecast cadence/resolution, target variables, availability, evaluation results, and integrations scoped to the applicable concrete WeatherNext release.
- Attribute accuracy/performance claims to Google/Google DeepMind or the named independent evaluator and preserve the exact evaluation context.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- WeatherNext remains a model family rather than a weather-data service or product integration.
- Producer provenance resolves to Google DeepMind.

## Verified identity and provenance

Google DeepMind weather-forecasting model family; trained releases, forecast datasets/APIs, enterprise delivery, and the Weather Lab exploration interface are separate assets.

## Source-scoped operating boundaries

- WeatherNext 3 is an ensemble model with hourly forecast generation; data delivery through BigQuery, Earth Engine, Cloud Storage, or Maps Platform is an integration choice, not another trained model. [WeatherNext 3 overview](https://deepmind.google/science/weathernext/).
- Weather Lab's experimental forecasts are not an officially supported Google product. Official weather forecasts and warnings must come from the relevant meteorological agency; keep that research-interface boundary separate from enterprise data availability. [Weather Lab status](https://developers.google.com/weathernext/guides/weatherlab).

## Source evidence

- <https://deepmind.google/science/weathernext/>
- <https://developers.google.com/weathernext/guides/weatherlab>
