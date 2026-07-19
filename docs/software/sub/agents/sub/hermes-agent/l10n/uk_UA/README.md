<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:20f44cb65eef29af51ff38ad1ce3335797525ac5
  mode: translated
-->

# Hermes Agent

Hermes Agent — самовдосконалювана система агента ШІ від Nous Research.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: Система агента ШІ
Основний сценарій: Сталий персональний або workflow agent із memory, skills, scheduled automations, multi-channel access, subagents і terminal tooling
Модель доступу: Open-source пакет із bring-your-own або hosted model/provider access
Ліцензія: MIT
Модель вихідного коду: Open source
Сигнал прав використання: Permissive core; провайдерів моделей, hosted infrastructure, channels і third-party services слід перевіряти окремо
Сигнал моделі вартості: BYO cost; runtime може бути self-managed, але робота залежить від model/provider, infrastructure і channel credentials
Модель розгортання: Hybrid; local, VPS, container, SSH, Singularity, Modal, Daytona, serverless-style і gateway-based messaging
Сигнал впровадження: Popular; видиме на GitHub поширення високе, але production maturity потребує перевірки для проєкту
Експлуатаційні вимоги: Runtime Hermes, credentials вибраних model/provider і необов’язкові messaging gateway credentials
Режими інтеграції: CLI, terminal UI, gateway process, Telegram, Discord, Slack, WhatsApp, Signal, local/Docker/SSH/Singularity/Modal/Daytona terminal backends, model providers, skills, scheduled automations, subagents і RPC-style tool use
Джерело: https://github.com/NousResearch/hermes-agent
Примітки щодо ризиків: Високодовірений сталий агент. Hermes Agent може запускати commands, під’єднувати messaging channels, використовувати зовнішніх model providers, зберігати memory, створювати чи покращувати skills, запускати subagents і scheduled automations. Перевірте tool permissions, credentials, memory behavior, enabled channels, terminal isolation, automation scope та approval gates.
Востаннє перевірено: 2026-07-06
```

## Призначення

Відстежуйте Hermes Agent як систему агента ШІ для майбутніх setup notes, порівнянь і аналізу ризиків.

## Що це

Hermes Agent описує себе як самовдосконалюваного агента ШІ з вбудованим learning loop. Upstream-документація наголошує на agent-curated memory, створенні skills із досвіду, покращенні skills під час використання, scheduled automations, subagents і multi-channel access.

Проєкт призначений для роботи не лише на одному laptop: підтримуються локальні машини, VPS deployments, containers, SSH environments і serverless-style backends.

## Релевантність для ШІ

Hermes Agent релевантний AI Lab як приклад сталої агентної системи, що поєднує terminal work, messaging access, memory, skills, automation, гнучкість model providers і делегованих subagents.

## Знімок перевірки

Станом на 2026-07-06 upstream-репозиторій представляє Hermes Agent як open-source проєкт Nous Research за ліцензією MIT. Проєкт позиціонує себе як гнучкий щодо model providers і явно підтримує Nous Portal, OpenRouter, OpenAI та custom endpoints.

Проєкт також документує широкі runtime й access modes: CLI/TUI, gateway-based messaging channels, local і remote terminal backends, scheduled automations, skills та subagents. Це робить інструмент експлуатаційно потужним, але високодовіреним: ті самі можливості створюють exposure credentials, memory, shell access, messaging channels і unattended tasks.

## Нотатки з розгортання

Upstream README описує шляхи встановлення для Linux, macOS, WSL2, Termux і native Windows. Він також підтримує вибір model/provider через commands на зразок `hermes model` і gateway process для messaging channels.

## Нотатки з безпеки

Сприймайте Hermes Agent як високодовірену інфраструктуру. Його цінність походить із поєднання memory, skills, tool use, terminal access, messaging channels, scheduled automations і subagents; ці ж функції збільшують експлуатаційний ризик.

До використання оцініть:

- налаштованих model providers і tool gateways;
- місце зберігання API keys і messaging credentials;
- використовуваний terminal backend та його ізоляцію;
- увімкнені tools і skills;
- memory, що зберігається між сесіями;
- дозволені дії scheduled automations;
- доступ subagents до чутливих файлів або сервісів;
- потребу в людських approval gates до shell, repository, credential або external-account actions.

## Посилання

- GitHub Hermes Agent: https://github.com/NousResearch/hermes-agent
- Сайт Hermes Agent: https://hermes-agent.nousresearch.com/
- Документація Hermes Agent: https://hermes-agent.nousresearch.com/docs/
