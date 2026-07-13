<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:2e51820195e5571ff0680ff685387d706e7e3e35
  mode: translated
-->

# Qodo

Набір агентів code review з інтеграцією в процеси Git pull request.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: агент code review
Основний сценарій використання: перевіряти pull requests із контекстом репозиторію, спеціалізованими review agents, правилами й стандартами організації
Модель доступу: пропрієтарний продукт Qodo з hosted-, team-, enterprise- та deployment-model options
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, публічною документацією та інтеграціями
Операційні вимоги: доступ Qodo, інтеграція Git provider, дозволи репозиторію, правила або стандарти організації та необов’язкова конфігурація deployment model
Режими інтеграції: Git workflows, pull requests, review agents, rule system, repository context, organizational standards, ticketing integrations, CI feedback, compliance configuration
Джерело: https://docs.qodo.ai/qodo-documentation/code-review
Примітки щодо ризиків: review-agent з високим рівнем довіри й доступом до репозиторію, pull request, стандартів організації та compliance context; перевірте дозволи, джерела правил, false positives і false negatives, створені пропозиції, розкриття секретів та обов’язкове review людиною перед merge.
```

## Огляд

Qodo — інтегрований у Git-процеси засіб code review на основі ШІ.

Його задокументований фокус — review pull request, аналіз із контекстом репозиторію, забезпечення правил і виявлення bugs чи issues з меншим review noise. Його доцільно розглядати як агента code review, а не універсального coding assistant.

## Відповідність AI Lab

Qodo належить до `agents/`, оскільки його основна задокументована поведінка — агентоподібне code review з контекстом репозиторію та спеціалізованими review agents.

Використовуйте його як орієнтир для:

- агентів AI pull-request review;
- review-процесів із контекстом репозиторію;
- систем review на основі правил і стандартів організації;
- порівняння з CodeRabbit та іншими review-орієнтованими агентами;
- оцінювання якості review коду, створеного ШІ.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- Git provider і deployment model;
- області дозволів репозиторію та організації;
- джерело правил і governance стандартів;
- signal-to-noise ratio та точність review;
- оброблення секретів і приватного коду;
- інтеграцію з CI та ticketing systems;
- обов’язкові контрольні точки review людиною перед merge.

## Джерела

- Документація Qodo code review: https://docs.qodo.ai/qodo-documentation/code-review
- Вебсайт Qodo: https://www.qodo.ai/
