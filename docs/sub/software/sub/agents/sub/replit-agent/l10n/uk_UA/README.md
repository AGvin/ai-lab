<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5b842780d28dffbc083c821050515bc8adc149c3
  mode: translated
-->

# Replit Agent

Агент створення застосунків на основі ШІ, що перетворює natural-language prompts на застосунки й вебсайти в Replit.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: агент створення застосунків
Основний сценарій використання: створювати, ітеративно вдосконалювати, діагностувати, розгортати й публікувати застосунки або вебсайти з natural-language prompts у середовищі Replit
Модель доступу: пропрієтарний продукт Replit із доступом через обліковий запис, plan і workspace
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом і згенерованим кодом застосунків у Replit workspaces
Операційні вимоги: обліковий запис Replit, доступ Replit Agent, workspace проєкту, середовище згенерованого застосунку, конфігурація deployment чи publishing та необов’язкові процеси імпорту або інтеграції GitHub
Режими інтеграції: Replit workspace, chat interface, app generation, website generation, deployment, publishing, database and integrations, screenshots або multimodal inputs, GitHub import, Replit hosting
Джерело: https://replit.com/ai
Примітки щодо ризиків: агент створення застосунків із високим рівнем довіри й доступом до workspace, згенерованого коду, deployment, database, інтеграцій і hosting; перевірте створені dependencies, секрети, дозволи проєкту, публічну видимість, deployment controls і review людиною перед експлуатацією production-застосунків.
```

## Огляд

Replit Agent — агент Replit для створення застосунків і вебсайтів із natural-language prompts.

Він працює всередині середовища Replit і призначений для швидкого переходу від ідеї до робочого прототипу або розгорнутого застосунку з підтримкою ітерацій, debugging і publishing-процесів.

## Відповідність AI Lab

Replit Agent належить до `agents/`, оскільки його основна задокументована роль — агентоподібний app builder, що виконує задачі створення ПЗ за інструкціями користувача.

Використовуйте його як орієнтир для:

- агентів створення застосунків природною мовою;
- hosted development environments із вбудованими агентами ШІ;
- процесів від prototype до deployment;
- досвіду app generation для розробників і користувачів без навичок розробки;
- порівняння з Lovable і Bolt.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- модель облікового запису, plan і workspace Replit;
- право власності на згенерований код і шлях експорту;
- дозволи workspace і проєкту;
- межі GitHub import або sync;
- доступ до database, integrations і hosting;
- видимість deployment і controls публічного поширення;
- review створених dependencies і безпеки.

## Джерела

- Сторінка продукту Replit Agent: https://replit.com/ai
- Документація Replit: https://docs.replit.com/
