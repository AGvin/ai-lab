# Granite TimeSeries TTM R3

Granite TimeSeries TTM R3 is represented as a model series. IBM's model card calls R3 a family of pretrained Tiny Time Mixer models, while the official Granite TSFM toolkit selects specific R3 revision keys according to context length, forecast horizon, decomposed architecture, and Lite/non-Lite mode.

The small default artifact shown on the repository page is therefore one distribution state, not the exhaustive identity of the R3 release. Revision keys remain implementation selectors unless a later intake establishes durable child-model identities.

## Capabilities and evidence scope

The current R3 card lists zero-shot forecasting, few-shot adaptation, full fine-tuning, multivariate forecasting, exogenous/control-variable integration, and high-throughput batch inference. It describes the family as spanning 1–35M parameters for non-Lite models and 1–18M for Lite models.

The card also publishes GIFT-Eval scores and CPU/GPU throughput comparisons. Those figures remain provider-reported model-card evidence here; they have not been independently reproduced by this catalog work.

## Translations

- English

## Relations

- Member of: [`catalog/models/ibm/granite-timeseries`](../../../../)

## Official resources

- <https://huggingface.co/ibm-granite/granite-timeseries-ttm-r3>
- <https://github.com/ibm-granite/granite-tsfm/blob/main/tsfm_public/toolkit/get_model.py>