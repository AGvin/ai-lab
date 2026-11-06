# WeatherNext 3

WeatherNext 3 is an ensemble weather model from Google DeepMind and Google Research that directly uses satellite observations and generates global forecasts hourly.

## Relations

- Member of: [WeatherNext](../../../../)

## Source-scoped operating boundaries

- Hourly forecast generation is distinct from a dataset's forecast lead times and delivery latency. The model overview reports 5 km station-targeted temperature/humidity and 10 km for other surface variables such as wind; preserve variable-specific resolution rather than claiming one universal grid. [Forecast scope](https://deepmind.google/science/weathernext/).
- Enterprise forecast data and Weather Lab's experimental research interface have different operational boundaries. Weather Lab directs users to official meteorological agencies for forecasts and warnings; model accuracy claims do not replace those warnings. [Weather Lab guidance](https://developers.google.com/weathernext/guides/weatherlab).

## Official resources

- <https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-weathernext-3/>
- <https://deepmind.google/science/weathernext/>
- <https://developers.google.com/weathernext/guides/weatherlab>
