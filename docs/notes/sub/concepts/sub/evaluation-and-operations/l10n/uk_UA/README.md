<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:fa166a1e301e055fc6825c36c635242f92552b73
  mode: translated
-->

# Оцінювання та експлуатація

Поняття для вибору, тестування, спостереження й експлуатації систем ШІ за реальних обмежень якості, вартості та надійності.

Поняття згруповано за практичним пріоритетом. Пріоритет визначає порядок читання, а не тематичне розміщення.

## Переклади

- [English](../../)
- Українська

## Основні

- [`evals/`](../../sub/evals/l10n/uk_UA/) — повторювані тести відповідності моделі чи системи ШІ визначеним вимогам.
- [`model-selection/`](../../sub/model-selection/l10n/uk_UA/) — вибір моделі за якістю задачі, можливостями, вартістю, затримкою, безпекою й обмеженнями розгортання.
- [`model-routing/`](../../sub/model-routing/l10n/uk_UA/) — динамічний вибір моделі відповідно до запиту чи операційної політики.
- [`observability/`](../../sub/observability/l10n/uk_UA/) — використання logs, metrics, traces і events для розуміння поведінки системи ШІ.
- [`tracing/`](../../sub/tracing/l10n/uk_UA/) — запис послідовності операцій моделі, інструментів, retrieval і workflow для одного виконання.
- [`cost-management/`](../../sub/cost-management/l10n/uk_UA/) — вимірювання й контроль витрат на моделі, інфраструктуру, сховища та інструменти.
- [`latency-and-throughput/`](../../sub/latency-and-throughput/l10n/uk_UA/) — балансування часу відповіді й обсягу роботи за одиницю часу.
- [`quality-cost-tradeoffs/`](../../sub/quality-cost-tradeoffs/l10n/uk_UA/) — вибір прийнятного балансу між якістю результату й операційними витратами.

## Корисні

- [`benchmarks/`](../../sub/benchmarks/l10n/uk_UA/) — стандартизовані задачі чи datasets для порівняння моделей або систем.
- [`evaluation-datasets/`](../../sub/evaluation-datasets/l10n/uk_UA/) — добірки прикладів для тестування якості, безпеки, retrieval або виконання задач.
- [`human-evaluation/`](../../sub/human-evaluation/l10n/uk_UA/) — оцінювання результатів моделі людьми за явними критеріями.
- [`fallback-models/`](../../sub/fallback-models/l10n/uk_UA/) — альтернативні моделі, коли бажана модель не працює або недоступна.
- [`caching/`](../../sub/caching/l10n/uk_UA/) — повторне використання попередніх результатів чи оброблених даних для зменшення повторної роботи.
- [`rate-limits/`](../../sub/rate-limits/l10n/uk_UA/) — controls, що обмежують обсяг запитів за певний час.

## Спеціалізовані

- [`llm-as-a-judge/`](../../sub/llm-as-a-judge/l10n/uk_UA/) — використання мовної моделі для оцінювання, ранжування чи критики результатів інших моделей.
- [`retrieval-evaluation/`](../../sub/retrieval-evaluation/l10n/uk_UA/) — вимірювання релевантності, повноти й правильності ранжування evidence у retrieval.
- [`reproducibility/`](../../sub/reproducibility/l10n/uk_UA/) — можливість повторити оцінювання чи workflow за порівнюваних умов і результатів.
