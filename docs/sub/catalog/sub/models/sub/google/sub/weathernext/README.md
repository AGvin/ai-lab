# WeatherNext

Google DeepMind weather-forecasting model family; trained releases, forecast datasets/APIs, enterprise delivery, and the Weather Lab exploration interface are separate assets.

## Relations

- Produced by: [Google DeepMind](../../../../../producers/sub/g/sub/google-deepmind/)
- Has member: [WeatherNext 3](sub/models/sub/weathernext-3/)

## Source-scoped operating boundaries

- WeatherNext 3 is an ensemble model with hourly forecast generation; data delivery through BigQuery, Earth Engine, Cloud Storage, or Maps Platform is an integration choice, not another trained model. [WeatherNext 3 overview](https://deepmind.google/science/weathernext/).
- Weather Lab's experimental forecasts are not an officially supported Google product. Official weather forecasts and warnings must come from the relevant meteorological agency; keep that research-interface boundary separate from enterprise data availability. [Weather Lab status](https://developers.google.com/weathernext/guides/weatherlab).

## Official resources

- <https://deepmind.google/science/weathernext/>
- <https://developers.google.com/weathernext/guides/weatherlab>

## Models

- [WeatherNext Models](sub/models/)
