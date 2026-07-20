<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:764cafbe76e0db634ac6af0797f6cd1658b56bd1
  mode: translated
-->

# OpenClaw

OpenClaw — персональний assistant ШІ, що працює на пристроях під контролем користувача й під’єднується до messaging channels.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: Система агента ШІ
Основний сценарій: Персональний always-on assistant у messaging channels і на локальних або self-managed пристроях
Модель доступу: Open-source пакет із local-first gateway і companion/node surfaces
Ліцензія: MIT
Модель вихідного коду: Open source
Сигнал прав використання: Permissive core; провайдерів моделей, hosted services, channels, mobile app stores і third-party skills слід перевіряти окремо
Сигнал моделі вартості: BYO cost; core може бути open-source, але робота залежить від моделі/провайдера, runtime, channel credentials і необов’язкових companion surfaces
Модель розгортання: Hybrid; local-first gateway із Docker/Nix/source setup, companion apps, device nodes, messaging channels і зовнішніми model providers
Сигнал впровадження: Mainstream; видиме на GitHub поширення дуже високе, але безпекова позиція й operational fit потребують окремої перевірки
Експлуатаційні вимоги: Node.js runtime, local або self-hosted gateway, model/provider authentication, channel credentials, workspace, skills і необов’язковий daemon або companion app
Режими інтеграції: Gateway daemon, CLI onboarding, messaging channels, macOS/iOS/Android voice interfaces, live Canvas, Docker, Nix, companion apps, device nodes, browser/canvas/nodes/cron/session tools і workspace skills
Джерело: https://github.com/openclaw/openclaw
Примітки щодо ризиків: Високодовірений персональний агент. OpenClaw може під’єднувати messaging channels, локальні пристрої, filesystem/workspace state, skills, model providers, browser-like tools, nodes, cron і зовнішні сервіси. Перевірте credentials, DM policies, channel permissions, daemon behavior, third-party skills, device-node permissions і data exposure.
Востаннє перевірено: 2026-07-06
```

## Призначення

Використовуйте цю сторінку для відстеження OpenClaw як персональної системи агента ШІ для майбутніх setup notes, порівнянь і аналізу ризиків.

## Що це

OpenClaw описує себе як персонального assistant ШІ, що працює на власних пристроях користувача. Проєкт позиціонує Gateway як control plane, а assistant — як продукт.

Assistant призначений для взаємодії через уже використовувані користувачем channels, включно з messaging platforms і companion interfaces.

## Релевантність для ШІ

OpenClaw релевантний AI Lab як local-first або self-hosted workflow персонального агента із широкими channel integrations і сталою агентною поведінкою.

## Знімок перевірки

Станом на 2026-07-06 upstream-репозиторій представляє OpenClaw як персональний assistant ШІ за ліцензією MIT, який користувачі запускають на власних пристроях. README описує Gateway як control plane і перелічує широку підтримку messaging channels.

Upstream README також документує local onboarding, Docker/Nix/source setup paths, workspace skills, device nodes, companion apps і security defaults для direct-message access. Це робить OpenClaw сильним кандидатом на персонального агента, але створює широку межу довіри навколо channels, local workspace state, skills, device nodes, model providers і вхідних недовірених повідомлень.

## Нотатки з розгортання

Upstream README рекомендує `openclaw onboard` як setup path. Він також описує вимоги Node.js runtime, роботу gateway, workspace setup, development channels, Docker/Nix/source paths і необов’язкові companion/device-node surfaces.

## Нотатки з безпеки

Сприймайте OpenClaw як високодовірену інфраструктуру. Персональний assistant, під’єднаний до messaging channels, model providers, локальних сервісів, файлів, skills, пристроїв і зовнішніх облікових записів, створює велику поверхню атаки.

До використання оцініть:

- під’єднані channels та облікові записи;
- чи direct-message access paired, allowlisted або публічний;
- місце зберігання credentials;
- увімкнені skills, tools, nodes та integrations;
- чи Gateway працює як постійний daemon;
- наданий агенту filesystem, workspace, browser, node і shell access;
- дані, що надсилаються hosted model providers;
- чи довірені, перевірені й pinned third-party skills;
- можливість ізолювати тестовий instance до production.

## Посилання

- GitHub OpenClaw: https://github.com/openclaw/openclaw
- Сайт OpenClaw: https://openclaw.ai
- Документація OpenClaw: https://docs.openclaw.ai
