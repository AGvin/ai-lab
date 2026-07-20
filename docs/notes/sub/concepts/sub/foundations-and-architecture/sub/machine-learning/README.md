# Machine Learning

Machine learning is a set of methods that learn patterns or decision rules from data instead of relying only on manually programmed logic.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A learning algorithm adjusts model parameters to reduce an objective on training data. The resulting model is then evaluated on unseen data to estimate how well it generalizes beyond the examples used to fit it.

## Common categories

- **Supervised learning:** learns from labeled input-output examples.
- **Unsupervised learning:** discovers structure without explicit target labels.
- **Self-supervised learning:** creates learning signals from the data itself.
- **Reinforcement learning:** learns behavior from rewards and interaction.

## Practical use

Machine learning is useful when rules are difficult to write but representative data and measurable outcomes exist. Typical applications include classification, recommendation, forecasting, anomaly detection, speech recognition, and generative models.

## Trade-offs and limitations

A model may fit historical data while failing after conditions change. Data quality, label quality, leakage, class imbalance, and evaluation design often matter more than algorithm complexity.

## Common mistakes

- Evaluating on training examples.
- Treating correlation as causal evidence.
- Deploying without monitoring data drift.
- Selecting a complex model before establishing a simple baseline.

## Related concepts

- [Foundations and Architecture](../../)
- [Deep Learning](../deep-learning/)
- [Evaluation Datasets](../../../evaluation-and-operations/sub/evaluation-datasets/)
- [Overfitting](../../../training-and-adaptation/sub/overfitting/)
