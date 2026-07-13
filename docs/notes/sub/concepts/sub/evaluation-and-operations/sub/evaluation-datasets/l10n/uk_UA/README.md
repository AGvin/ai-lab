<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:769fa226fe2fbe2e6d794d9c800c2a2b90a81165
  mode: translated
-->

# Datasets оцінювання

Dataset оцінювання — підготовлений набір inputs, очікуваних властивостей, reference answers, labels або scoring criteria для тестування моделі чи системи.

## Переклади

- [English](../../)
- Українська

## Основна ідея

Dataset повинен представляти distribution і risk реального використання. Він може містити звичайні cases, складні edge cases, invalid inputs, adversarial examples та historical incidents. Очікуваний результат може бути точним, rubric-based або відкритим для judgment людиною залежно від задачі.

## Практичний дизайн

- Розділяйте development, validation і held-out test sets.
- Записуйте source, license, date і data transformations.
- За можливості видаляйте duplicates і near-duplicates із training data.
- Додавайте приклади для кожної важливої категорії відмов.
- Версіонуйте dataset і scoring rules разом.

## Компроміси й обмеження

Статичний dataset застаріває зі зміною поведінки користувачів і моделей. Малі набори легко перевіряти, але вони мають високу variance; великі поліпшують coverage, але дорогі в labeling та inspection.

## Типові помилки

- Повторно використовувати test set для prompt tuning.
- Додавати лише раніше успішні приклади.
- Вважати synthetic labels ground truth.
- Змінювати labels без запису нової версії.

## Пов’язані поняття

- [Оцінювання та експлуатація](../../../../l10n/uk_UA/)
- [Оцінювання](../../../../sub/evals/l10n/uk_UA/)
- [Datasets](../../../../../training-and-adaptation/sub/datasets/l10n/uk_UA/)
- [Відтворюваність](../../../../sub/reproducibility/l10n/uk_UA/)
