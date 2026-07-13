<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:18f2df70d1c64fc53bd23da2d41bd509aca28265
  mode: translated
-->

# Оцінювання людиною

Оцінювання людиною використовує людей для перевірки outputs моделі за явними критеріями або порівняння альтернативних відповідей.

## Переклади

- [English](../../)
- Українська

## Основна ідея

Люди потрібні, коли якість залежить від нюансів значення, domain expertise, usability, tone або реальних наслідків, яких не охоплюють автоматичні metrics. Надійне human evaluation потребує чіткої rubric і послідовного annotation process.

## Практичний дизайн

- Визначайте критерії з позитивними й негативними прикладами.
- Навчайте evaluators і вимірюйте agreement.
- Рандомізуйте й приховуйте identity моделі.
- Відокремлюйте фактичну правильність від style preferences.
- Записуйте uncertainty і причини складних judgments.
- Ескалуйте спеціалізовані теми domain experts.

## Компроміси й обмеження

Human evaluation дороге, повільне й залежить від fatigue, culture, preference і presentation order. Agreement може бути низьким, коли rubric нечітка або задача справді суб’єктивна.

## Типові помилки

- Питати, яка відповідь «краща», без критеріїв.
- Використовувати одного evaluator для високоimpactних висновків.
- Показувати назви моделей або очікуваний ranking.
- Вважати majority preference фактичною правильністю.

## Пов’язані поняття

- [Оцінювання та експлуатація](../../../../l10n/uk_UA/)
- [LLM як суддя](../../../../sub/llm-as-a-judge/l10n/uk_UA/)
- [Оптимізація вподобань](../../../../../training-and-adaptation/sub/preference-optimization/l10n/uk_UA/)
- [Datasets оцінювання](../../../../sub/evaluation-datasets/l10n/uk_UA/)
