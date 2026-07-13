<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:bc2e39fc740c6651435d1a7a2068a13a0b5789ae
  mode: translated
-->

# Goose

Локальний агент ШІ з відкритим кодом для програмування, досліджень, автоматизації, письма й workflow-задач.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: локальний агент ШІ загального призначення
Основний сценарій використання: виконувати локальні агентні процеси для програмування, досліджень, автоматизації, письма, аналізу даних і задач розробника
Модель доступу: локальний агент із відкритим кодом, desktop-, CLI- та API-використанням і credentials зовнішнього model provider
Ліцензія: Apache-2.0
Модель вихідного коду: відкритий код
Операційні вимоги: desktop app, CLI або API Goose; credentials вибраного model provider; доступ до локальної файлової системи й інструментів; необов’язкові MCP extensions
Режими інтеграції: Desktop app, CLI, API, local files, shell або workflow tasks, model providers, MCP extensions, developer automation workflows
Джерело: https://github.com/aaif-goose/goose
Примітки щодо ризиків: локальний агент із високим рівнем довіри й доступом до filesystem, tools, extensions і providers; перед використанням із чутливими репозиторіями чи приватними даними перевірте розкриття локальних даних, дозволи shell/workflow, області MCP extensions, credentials providers, attack surface desktop/API, approval gates людини й sandboxing.
```

## Огляд

Goose — локальний агент ШІ з відкритим кодом для роботи загального призначення на машині розробника.

Він ширший за coding-only assistant: може підтримувати програмування, workflows, дослідження, письмо, автоматизацію й аналіз даних через desktop, CLI та API.

## Відповідність AI Lab

Goose належить до `agents/`, оскільки його основна задокументована роль — локальна агентоподібна система, що виконує задачі через tools, local context, model providers і extensions.

Це не фреймворк оркестрації агентів. Використовуйте `agent-orchestration/` для frameworks, runtimes або control planes, що координують кілька агентів чи agent workflows.

Використовуйте Goose як орієнтир для:

- локальних agent workflows загального призначення;
- використання агентів у desktop і CLI;
- доступу до tools через MCP extensions;
- порівняння з Aider, Cline, Pi, Claude Code і Codex CLI;
- оцінювання меж безпеки локальних агентів для приватних файлів і репозиторіїв;
- розуміння компромісів між спеціалізованими coding agents і ширшими task agents.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- відповідність desktop, CLI або API workflow;
- підтримку model provider і оброблення credentials;
- межі дозволів local filesystem і shell/workflow;
- довіру до MCP extensions та області дозволів;
- розкриття приватного вихідного коду, документів і даних providers або tools;
- approval gates людини й auditability;
- стратегію sandboxing для чутливих репозиторіїв і приватних даних.

## Джерела

- GitHub Goose: https://github.com/aaif-goose/goose
- Документація Goose: https://goose-docs.ai
