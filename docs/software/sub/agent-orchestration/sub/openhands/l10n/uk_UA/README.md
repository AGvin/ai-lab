<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:f3d816f7126fab1fb73bf92fa1541824bd7de372
  mode: translated
-->

# OpenHands

Локалізована точка входу для developer control center for coding agents and automations.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: Платформа оркестрації агентів і control center для coding agents
Основний сценарій: Запуск і координація coding agents у local, remote, cloud та enterprise backends для репозиторних й engineering automation tasks
Модель доступу: Open-source core із self-hosted deployment, OpenHands Cloud і OpenHands Enterprise
Ліцензія: MIT для core OpenHands і agent-server Docker images; enterprise directory має окрему enterprise license
Модель вихідного коду: Open-source core із source-available enterprise components
Сигнал прав використання: Permissive core; умови Cloud, Enterprise, enterprise directory, managed infrastructure і third-party agents/providers слід перевіряти окремо
Сигнал моделі вартості: Open core; self-hosted core має MIT, а cloud, enterprise, hosted infrastructure, model providers і third-party agents можуть бути платними
Модель розгортання: Hybrid; локальний запуск за замовчуванням і підключення local, Docker, VM, company infrastructure, OpenHands Cloud або Enterprise backends
Сигнал впровадження: Mainstream; видиме на GitHub поширення високе, але production потребує перевірки backend isolation, licensing та operational controls
Експлуатаційні вимоги: Runtime OpenHands, credentials вибраних agent/model/provider і налаштовані local, remote, cloud або enterprise backends чи integrations
Режими інтеграції: Agent Canvas, local/remote/cloud backends, GitHub, Slack, Linear, Jira, Notion, ACP-compatible agents, coding agents, automations, Cloud, Enterprise
Джерело: https://github.com/OpenHands/OpenHands
Примітки щодо ризиків: Високодовірений control center coding agents. Перевірте workspace isolation, filesystem і shell access, repository permissions, integration scopes, backend isolation, automation triggers, cloud/enterprise boundaries та approval gates.
Востаннє перевірено: 2026-07-06
```

## Огляд

OpenHands — self-hosted control center для coding agents та engineering automations.

Він корисний, коли потрібно не лише запустити одного агента, а координувати developer agents, tasks, tools, repository workflows, automations і execution backends зі спільного control plane.

## Відповідність AI Lab

OpenHands належить до `agent-orchestration/`, бо його основна роль — координація й запуск coding agents, а не робота як одного персонального агента.

Використовуйте його як орієнтир для:

- self-hosted control planes coding agents;
- repository automation із людськими approval gates;
- виконання агентів у local, remote, cloud та enterprise backends;
- engineering workflows з GitHub, Slack, Linear, Jira, Notion або подібними системами;
- порівняння із самостійними агентами та multi-agent frameworks.

## Знімок перевірки

Станом на 2026-07-06 офіційна документація описує Agent Canvas як browser-based UI і backend server для запуску agents та automations. Він може працювати локально, self-hosted на VM або підключатися до OpenHands Cloud.

Офіційна документація розрізняє OpenHands Cloud та Enterprise. Вона вказує, що Enterprise можна self-host у VPC клієнта через Kubernetes і що після одного місяця потрібна ліцензія. Також увесь вміст має MIT, окрім directory `enterprise/`, а core `openhands` і `agent-server` Docker images повністю ліцензовані за MIT.

## Нотатки з оцінювання

До впровадження оцініть:

- модель deployment й upgrade;
- межі ліцензій core, cloud та enterprise;
- підтримувані backends і властивості їх ізоляції;
- межі filesystem та shell permissions;
- scopes доступу до GitHub і репозиторію;
- scopes інтеграцій Slack, Linear, Jira, Notion та інших;
- людські approval і review gates;
- поведінку на приватних чи чутливих репозиторіях;
- сумісність із наявними automation workflows;
- місце виконання агентів: local, Docker, VM, company infrastructure чи OpenHands-hosted infrastructure.

## Посилання

- Сайт OpenHands: https://openhands.dev
- GitHub OpenHands: https://github.com/OpenHands/OpenHands
- Документація OpenHands: https://docs.openhands.dev
- Вступ до OpenHands: https://docs.openhands.dev/overview/introduction
