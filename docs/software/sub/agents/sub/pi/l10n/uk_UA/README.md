<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:c98812bb62abc5fa48972cf27bde1ced93b40508
  mode: translated
-->

# Pi

Pi — малий terminal runtime для створення й запуску налаштованого coding-agent.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: Harness coding agent на основі ШІ
Основний сценарій: Створення локального для проєкту terminal coding agent навколо файлів репозиторію, shell tools, провайдерів моделей і власних workflow extensions
Модель доступу: Open-source пакет і hosted/subscription або API-key провайдери моделей залежно від конфігурації
Ліцензія: MIT
Модель вихідного коду: Open source
Експлуатаційна вимога: Установлення Node.js package і provider authentication або API keys
Режими інтеграції: Terminal UI, print/JSON mode, SDK, RPC mode, JSON event stream mode, TypeScript extensions, skills, prompt templates, themes і Pi packages
Джерело: документація pi.dev
Примітки щодо ризиків: Pi може бути настільки потужним, наскільки потужні під’єднані tools, extensions, skills, shell access, provider credentials і project permissions. Перевіряйте всі локальні й third-party компоненти до роботи з чутливими репозиторіями.
```

## Що це

Pi найкраще розуміти як **coding-agent workbench для terminal**.

Це не лише вікно chat і не повноцінна IDE. Це тонкий agent runtime, що працює в каталозі проєкту й дає моделі змогу працювати з контекстом проєкту, інструкціями, файлами, commands та власними tools.

Спрощена ментальна модель:

```text
Pi = ядро terminal AI agent + інструкції проєкту + tools + необов’язкові власні extensions/skills/packages
```

Важливо, що Pi призначений для формування навколо workflow. Замість одного фіксованого агентного продукту користувач може зберігати мале ядро й додавати лише потрібну поведінку.

Це не розмовний assistant-продукт `pi.ai`. Сторінка стосується ПЗ, задокументованого на `pi.dev`.

## Практичні приклади

Pi може бути корисним для:

- запуску локального для репозиторію coding assistant у terminal;
- завантаження правил проєкту з файлів на зразок `AGENTS.md` і використання їх під час змін коду чи документації;
- запитів агенту на перевірку файлів, пропозицію змін і редагування вмісту репозиторію;
- створення повторюваного workflow підтримки документації;
- створення command на зразок `/prepare-pr`, `/audit-docs` або `/summarize-branch`;
- пакування поширеного workflow в повторно використовуваний skill;
- створення TypeScript extension із власним tool, command, keyboard shortcut, event hook або terminal UI element;
- надання Pi через SDK, RPC чи JSON event streams для керування з іншого локального інструмента;
- пакування командного набору extensions, skills, prompt templates і themes як Pi package.

## Чому це належить до агентів

Pi належить до `agents/`, бо основний об’єкт — agent harness для запуску й налаштування workflow агента ШІ.

Його не слід документувати як редактор коду, бо він не замінює editor UI. Також його не слід документувати лише як library, адже звичайний сценарій — інтерактивна terminal-сесія coding agent.

## Відмінність від типового coding assistant

Типовий coding assistant часто є фіксованим продуктом із визначеним інтерфейсом і набором функцій.

Pi ближчий до конструктора агентів:

- terminal session — дефолтний інтерфейс;
- проєкт може надавати власні інструкції;
- extensions можуть додавати tools і поведінку;
- skills можуть надавати повторно використовувані task-specific знання;
- prompt templates можуть перетворювати повторювані prompts на commands;
- packages можуть поширювати повний набір власної поведінки;
- програмні режими дають іншим tools змогу вбудовувати агент або керувати ним.

## Що оцінювати

До регулярного використання Pi оцініть:

- процес установлення й оновлення;
- підтримуваних провайдерів і перемикання моделей;
- спосіб завантаження інструкцій та контексту проєкту;
- безпечність shell access і редагування файлів;
- достатність guardrails для приватних репозиторіїв;
- роботу дозволів extensions, skills і packages;
- чи легше підтримувати власні workflows у Pi, ніж у standalone scripts, GitHub Actions або іншому coding agent.

## Посилання

- https://pi.dev/
- https://pi.dev/docs/latest
- https://pi.dev/docs/latest/sdk
- https://pi.dev/docs/latest/extensions
- https://pi.dev/docs/latest/skills
- https://pi.dev/docs/latest/packages
