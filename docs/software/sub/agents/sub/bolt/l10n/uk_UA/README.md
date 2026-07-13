<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:a68169f78053293b2233f405410ba96a6d527953
  mode: translated
-->

# Bolt

AI builder застосунків і вебсайтів для створення ПЗ через розмову з агентом.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: платформа агента створення застосунків
Основний сценарій використання: створювати, ітеративно вдосконалювати, рефакторити, тестувати й публікувати застосунки або вебсайти з natural-language prompts і design inputs
Модель доступу: пропрієтарна hosted platform з individual, team і enterprise plans
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, generated application code і platform services
Операційні вимоги: Bolt account, project workspace, generated application environment, token budget, необов’язкові GitHub, Figma, Supabase, hosting, MCP і team configuration
Режими інтеграції: Web app builder, Bolt Agent, design-system import, Figma, GitHub, Supabase, hosting, databases, authentication, MCP servers, team workspaces, Bolt Cloud
Джерело: https://bolt.new/
Примітки щодо ризиків: app-building platform із високим рівнем довіри й доступом до generated code, hosted project state, GitHub, design system, database, hosting, MCP і team; перевірте generated dependencies, secrets, workspace roles, deployment controls, external integrations і review людиною перед production use.
```

## Огляд

Bolt — AI builder застосунків і вебсайтів від StackBlitz для створення ПЗ через розмову з агентом.

Він призначений для переходу від ідеї чи design input до робочого застосунку з підтримкою project planning, generation, iteration, refactoring, testing, hosting та integrations GitHub, Figma, Supabase і MCP servers.

## Відповідність AI Lab

Bolt належить до `agents/`, оскільки його основна задокументована роль — агентоподібна система створення застосунків.

Використовуйте його як орієнтир для:

- chat-driven генерації застосунків і вебсайтів;
- app-building agents із hosting та backend services;
- generation за допомогою design systems і Figma;
- generated-code workflows, підключених до GitHub;
- порівняння з Lovable і Replit Agent.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- ownership generated code і модель експорту;
- GitHub integration та межі repository;
- token budget і model-routing behavior;
- доступ до database, hosting, authentication та MCP integrations;
- permissions workspace і team;
- review generated dependencies та vulnerabilities;
- придатність для prototypes порівняно з production applications.

## Джерела

- Вебсайт Bolt: https://bolt.new/
- Довідковий центр Bolt: https://support.bolt.new/
