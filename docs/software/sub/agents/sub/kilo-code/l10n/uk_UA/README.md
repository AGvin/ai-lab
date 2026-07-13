<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:ad7e3c8842b4a0959199e0c76eadc172be3f09a0
  mode: translated
-->

# Kilo Code

Платформа coding-agent із поверхнями VS Code, JetBrains, CLI, gateway та інфраструктурою hosted agents.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: платформа coding-agent
Основний сценарій використання: писати, редагувати, розуміти й автоматизувати код та співпрацювати над ним через процеси coding-agent у редакторі й CLI
Модель доступу: компоненти відкритої та хостингової платформи з обліковим записом, gateway і необов’язковим командним або enterprise-доступом
Ліцензія: змішана; перед впровадженням перевірте ліцензії окремих компонентів
Модель вихідного коду: проєкт із відкритим кодом і хостинговими платформними сервісами
Операційні вимоги: розширення або CLI Kilo Code, вибраний постачальник моделей чи доступ до Kilo Gateway, робочий простір репозиторію, налаштовані rules, дозволи MCP або автоматизації та необов’язкова інфраструктура hosted-agent KiloClaw
Режими інтеграції: VS Code, JetBrains, CLI, custom rules, modes, MCP, Kilo Gateway, KiloClaw, hosted agents, chat platforms, інструменти розробки, процеси автоматизації
Джерело: https://kilo.ai/docs
Примітки щодо ризиків: платформа coding-agent з високим рівнем довіри й доступом до редактора, CLI, репозиторію, model gateway, MCP, автоматизації та hosted agents; перевірте ліцензії компонентів, облікові дані постачальників, дозволи репозиторію, створені diffs, області автоматизації, межі hosted agents і контрольні точки схвалення людиною.
```

## Огляд

Kilo Code — платформа coding-agent, що охоплює розширення редакторів, CLI, доступ до model gateway, співпрацю, автоматизацію та інфраструктуру hosted agents.

Вона ширша за одне розширення редактора, оскільки задокументована поверхня продукту містить VS Code, JetBrains, CLI, custom modes, rules, MCP, Kilo Gateway і hosted agents KiloClaw.

## Відповідність AI Lab

Kilo Code належить до `agents/`, оскільки його основна задокументована роль — система coding-agent, а не автономний редактор коду.

Використовуйте його як орієнтир для:

- платформ coding-agent із поверхнями редактора й CLI;
- процесів multi-model gateway;
- coding-автоматизації з підтримкою MCP;
- інфраструктури hosted agents, суміжної з coding agents;
- порівняння з Cline, Roo Code, Aider і Goose.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- ліцензію та модель вихідного коду кожного компонента;
- область редактора, CLI, gateway і hosted agents;
- оброблення облікових даних постачальників моделей і gateway;
- межі дозволів репозиторію та файлової системи;
- межі довіри custom rules і modes;
- області дозволів MCP та автоматизації;
- review створених diffs перед commit, push або створенням PR.

## Джерела

- Документація Kilo: https://kilo.ai/docs
- GitHub Kilo Code: https://github.com/Kilo-Org/kilocode
