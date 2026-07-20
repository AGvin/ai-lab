<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:f9e27d507bbaf2d7a44493abd1a970d9c5b1d4bf
  mode: translated
-->

# OMP (Oh My Pi)

OMP — terminal coding-agent із відкритим кодом, створений на основі Pi й розширений інтегрованим набором інструментів розроблення.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: terminal AI coding-agent і розширюваний agent runtime
Основний сценарій використання: аналіз репозиторію, редагування, debugging, research і делеговані coding tasks через terminal agent із широким набором tools
Модель доступу: локальний застосунок із відкритим кодом із зовнішніми, subscription-routed, gateway або local model providers залежно від конфігурації
Модель вартості: OMP безплатний за ліцензією MIT; вибрані model providers, coding plans, gateways або hosted services можуть мати окрему вартість
Ліцензія: MIT
Модель вихідного коду: відкритий код
Операційні вимоги: установлений OMP, доступ до проєкту, Bun або підтримуваний installer та облікові дані вибраних model providers
Режими інтеграції: Terminal UI, CLI, SDK, RPC, model roles, built-in tools, LSP, DAP, persistent Python і JavaScript execution, browser і research tools, subagents, extensions, skills та MCP discovery
Джерело: https://github.com/can1357/oh-my-pi
Примітки щодо ризиків: OMP надає широкий tool surface, який може змінювати репозиторії, виконувати shell і language-runtime code, звертатися до debuggers та browsers, делегувати роботу subagents і викликати remote providers. Обмежуйте tools і credentials, перевіряйте approval settings та створені зміни й використовуйте ізоляцію для недовірених репозиторіїв або задач.
Остання перевірка: 2026-07-17
```

## Огляд

OMP, також брендований як **Oh My Pi**, — terminal-first coding-agent із широким інтегрованим середовищем розроблення. Він поєднує coding-agent session із repository tools, операціями language server і debugger, persistent code execution, browser та research capabilities і workflows subagents.

Executable та актуальна назва продукту використовують `omp`, тоді як репозиторій вихідного коду й походження package зберігають назви Oh My Pi та Pi.

## Зв’язок із Pi

OMP є fork Pi. Обидва продукти надають terminal coding-agent sessions і розширювані runtime surfaces, але мають різні акценти:

- **Pi** зберігає мале ядро й очікує, що користувач формуватиме workflow з extensions, skills, prompts і packages.
- **OMP** містить значно ширший built-in набір tools і providers та прагне бути повноцінним одразу після встановлення.

Їх слід документувати окремо, оскільки вони мають незалежні repositories, packages, releases, configurations, capabilities і maintenance lifecycles.

## Набір інструментів розроблення

OMP інтегрує можливості розроблення, які часто постачаються окремими застосунками або plugins:

- repository read, write, search і structured edit operations;
- виконання shell із підтримкою terminal і background processes;
- операції language server для symbols, references, diagnostics і code intelligence;
- debugger operations через DAP integrations;
- structural search та editing із syntax-aware tooling;
- persistent Python і JavaScript execution, що може викликати agent tools;
- browser, documentation, research і vulnerability-data retrieval;
- delegated tasks і налаштовувані ролі subagents.

Великий built-in каталог tools підвищує доступність можливостей, але також збільшує permission і review surface.

## Моделі, постачальники й ролі

OMP підтримує багато direct APIs, gateways, subscription-routed coding plans і local model servers. Model roles дають змогу використовувати різні моделі для звичайної роботи, дешевих delegated tasks, глибшого reasoning, planning і commit-oriented output.

Доступність provider і authentication behavior можуть змінюватися незалежно від OMP. Перед стандартизацією конфігурації перевіряйте точний installed release, умови provider, OAuth flow, сумісність із local server, pricing і model capabilities.

## SDK, RPC і MCP

SDK надає in-process доступ до agent state, events, sessions, models, tools і discovery. RPC mode підтримує cross-process або cross-language керування.

OMP може знаходити MCP servers як частину extensibility surface. MCP servers слід оцінювати як незалежні довірені integrations, оскільки вони можуть відкривати tools, context, credentials або remote services. Архітектуру протоколу описано на сторінці [Model Context Protocol](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/).

## Установлення й підтримка платформ

Офіційні варіанти встановлення включають shell і PowerShell installers, Bun package та release-oriented tools, зокрема Mise. Проєкт документує підтримку macOS, Linux і Windows та наразі вимагає сумісну версію Bun для package installation.

Закріплюйте відому версію для відтворюваних середовищ. OMP швидко розвивається й може змінювати tools, provider integrations, settings, edit formats і approval behavior.

## Безпека й операційні ризики

Перевіряйте щонайменше такі межі:

- які tools видимі й доступні для виконання в кожному mode;
- approval rules для read, write, shell, debugger, browser і delegated actions;
- provider credentials і OAuth tokens;
- network access і дані, що надсилаються зовнішнім сервісам;
- persistent state Python або JavaScript;
- extensions, skills, prompts і project instructions;
- scope, concurrency і cost subagents;
- rollback і перевірку diff після automated edits.

Tool-rich operation не слід плутати із sandboxing. Для задач або репозиторіїв без повної довіри використовуйте containers, disposable worktrees, обмежені credentials чи ізоляцію операційної системи.

## Відповідність AI Lab

OMP належить до `agents/`, оскільки його основна роль — інтерактивний coding-agent. LSP, DAP, browser, SDK, RPC та orchestration-like features розширюють цього агента, але не змінюють канонічну категорію продукту.

Використовуйте цю сторінку як довідку для:

- batteries-included terminal coding agents;
- порівняння з меншим harness Pi;
- інтегрованих LSP і debugger workflows;
- persistent language runtimes із доступом до agent tools;
- model-role routing і широкої підтримки providers;
- tool-rich workflows subagents і research.

## Контрольний список оцінювання

Перед упровадженням перевірте:

- точний release і підтримуваний спосіб установлення;
- сумісність із потрібними операційними системами та shells;
- authentication, pricing і fallback behavior model providers;
- якість і безпеку edit, shell, LSP, DAP, browser та evaluation tools;
- approval controls і можливість активації прихованих або динамічно знайдених tools;
- межі довіри extensions, skills, MCP і project instructions;
- стабільність SDK або RPC, якщо OMP вбудовується в іншу систему;
- resource usage, вартість subagents і відновлення після часткового збою.

## Джерела

- Вебсайт OMP: https://omp.sh/
- Репозиторій вихідного коду: https://github.com/can1357/oh-my-pi
- Документація SDK: https://github.com/can1357/oh-my-pi/blob/main/docs/sdk.md
- Конфігурація моделей і providers: https://github.com/can1357/oh-my-pi/blob/main/docs/models.md
- Releases: https://github.com/can1357/oh-my-pi/releases
- Ліцензія: https://github.com/can1357/oh-my-pi/blob/main/LICENSE