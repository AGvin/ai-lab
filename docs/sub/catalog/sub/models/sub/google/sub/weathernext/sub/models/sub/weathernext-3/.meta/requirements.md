# Documentation Requirements

## Requirements

- Identify WeatherNext 3 as the concrete global AI weather-forecasting model introduced by Google DeepMind and Google Research on 2026-09-03.
- Preserve its first-party-described boundary: direct use of live geostationary satellite observations plus traditional historical analysis, hourly forecast generation, multi-resolution global outputs, precipitation forecasting, station-level outputs, and clean-energy variables.
- Keep BigQuery, Earth Engine, Google Cloud Storage, Search, Maps, Gemini, Maps Platform Weather API, and Weather Lab as distribution/integration surfaces rather than separate trained-model identities.
- Treat operational availability, variables, forecast resolution/cadence, data sources, product integrations, and evaluation results as freshness-sensitive.
- Attribute provider and third-party accuracy claims explicitly and do not use the model for official severe-weather or public-safety guidance; current first-party material directs users to official meteorological agencies for those uses.

## Validation

- WeatherNext 3 remains one concrete WeatherNext model, not the complete Google weather-data service.
- Forecast/evaluation claims remain source- and revision-scoped.
