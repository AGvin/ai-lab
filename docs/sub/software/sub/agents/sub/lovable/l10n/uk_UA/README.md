<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:26a0f60ac439f3a3c68d98cbc6ebe11195d5c013
  mode: translated
-->

# Lovable

Full-stack платформа розробки на основі ШІ для створення й ітеративного вдосконалення вебзастосунків природною мовою.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: платформа агента створення застосунків
Основний сценарій використання: створювати, ітеративно вдосконалювати, розгортати й підтримувати full-stack вебзастосунки з natural-language prompts із редагованим згенерованим кодом
Модель доступу: пропрієтарна hosted platform з individual, team і enterprise plans
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, згенерованим application code та GitHub integration
Операційні вимоги: account або workspace Lovable, доступ до проєкту, workspace згенерованого застосунку, необов’язкові GitHub sync, deployment, database, authentication та integration configuration
Режими інтеграції: Web application builder, shared workspaces, generated codebase, GitHub sync, deployment workflows, databases, authentication, integrations, Lovable MCP server, ChatGPT app, API
Джерело: https://docs.lovable.dev/introduction/welcome
Примітки щодо ризиків: app-building platform із високим рівнем довіри й доступом до generated code, workspace, GitHub sync, deployment, database, authentication та integrations; перевірте ownership коду, generated dependencies, secrets, production data, workspace roles, deployment controls і review людиною перед експлуатацією production applications.
```

## Огляд

Lovable — full-stack платформа розробки на основі ШІ для створення вебзастосунків природною мовою.

Вона генерує редагований application code і підтримує життєвий цикл від prototype до deployment зі collaboration, GitHub sync, integrations і governance features.

## Відповідність AI Lab

Lovable належить до `agents/`, оскільки його основна задокументована поведінка — агентоподібне створення ПЗ за інструкціями природною мовою.

Він ширший за coding assistant і ближчий до платформи app-building agent.

Використовуйте Lovable як орієнтир для:

- генерації застосунків природною мовою;
- full-stack workflows згенерованих застосунків;
- app-building platforms із GitHub connection;
- low-code або vibe-coding agent products;
- порівняння з Replit Agent і Bolt.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- ownership згенерованого коду й модель експорту;
- GitHub sync і межі репозиторію;
- controls ролей і дозволів workspace;
- безпеку database, authentication та integrations;
- workflow review deployment і production changes;
- review generated dependencies та vulnerabilities;
- придатність для prototypes порівняно з підтримуваними production systems.

## Джерела

- Документація Lovable: https://docs.lovable.dev/introduction/welcome
- Вебсайт Lovable: https://lovable.dev/
