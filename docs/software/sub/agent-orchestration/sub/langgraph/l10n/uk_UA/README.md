<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:a87e1e2c6de17e19f4902f6c4e93bb3c20bf7cd9
  mode: translated
-->

# LangGraph

Локалізована точка входу для stateful agent orchestration framework and runtime.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: Framework і runtime оркестрації агентів
Основний сценарій: Створення, координація й запуск graph-structured agent workflows із durable execution, persistence, streaming, memory та людським наглядом
Модель доступу: Open-source пакет із необов’язковими сервісами екосистеми LangChain/LangSmith
Ліцензія: MIT
Модель вихідного коду: Open-source core із необов’язковими хостинговими сервісами екосистеми
Сигнал прав використання: Permissive core; умови LangSmith, deployment, observability, hosted services та enterprise слід перевіряти окремо
Сигнал моделі вартості: Open core; локальний пакет є open-source, а хостингові observability, deployment, platform або enterprise services можуть бути платними
Модель розгортання: Hybrid; локальний package/runtime із необов’язковими LangSmith observability, deployment, Studio та ecosystem integrations
Сигнал впровадження: Mainstream; видиме на GitHub поширення високе, але production-відповідність потребує перевірки для проєкту
Експлуатаційні вимоги: Пакет LangGraph, вибрані провайдери моделей, tools, сховище runtime state і необов’язкові LangSmith observability або deployment services
Режими інтеграції: Python, JavaScript/TypeScript, компоненти LangChain, LangSmith, провайдери моделей, tools, persistence backends, human-in-the-loop review points
Джерело: https://github.com/langchain-ai/langgraph
Примітки щодо ризиків: Runtime оркестрації для stateful tool-using workflows. Перевірте дозволи tools, persistence storage, розкриття checkpoint data, людські approval gates, облікові дані провайдерів, production observability і межі hosted services до роботи з чутливими репозиторіями чи даними.
Востаннє перевірено: 2026-07-06
```

## Огляд

LangGraph — low-level orchestration framework і runtime для створення, керування й розгортання довготривалих stateful agents.

Він зосереджений на інфраструктурному рівні агентних систем, а не на одному самостійному assistant чи coding agent. Його основна цінність — явний контроль graph-structured виконання, стану агента, persistence, streaming і human-in-the-loop втручання.

## Відповідність AI Lab

LangGraph належить до `agent-orchestration/`, бо його основна задокументована роль — координація й запуск stateful agent workflows.

Використовуйте його як орієнтир для:

- graph-based agent workflow runtimes;
- durable execution довготривалих агентів;
- stateful workflows із checkpointing і persistence;
- human-in-the-loop точок схвалення чи виправлення;
- порівняння з higher-level agent frameworks і самостійними агентами;
- production agent architecture, що відокремлює orchestration від окремих model calls.

## Знімок перевірки

Станом на 2026-07-06 upstream GitHub-репозиторій указує ліцензію MIT, а офіційна документація описує LangGraph як low-level orchestration framework і runtime для довготривалих stateful agents.

Офіційна документація позиціонує LangGraph у ширшій екосистемі LangChain/LangSmith: LangGraph можна використовувати для orchestration, а LangSmith надає tracing, evaluation, prompts, observability, deployment, Studio та пов’язані можливості. Сприймайте open-source runtime і hosted ecosystem services як окремі поверхні впровадження.

## Нотатки з оцінювання

До впровадження оцініть:

- підтримуваний language/runtime шлях проєкту;
- модель persistence стану й checkpoint storage;
- семантику human-in-the-loop переривання та схвалення;
- межі інтеграції моделей та tools;
- workflow observability і debugging;
- експлуатаційну залежність від необов’язкових сервісів LangChain або LangSmith;
- роботу з чутливими prompt, tool, state, memory, trace і checkpoint data;
- шлях розгортання production workloads.

## Посилання

- Документація LangGraph: https://docs.langchain.com/oss/python/langgraph/overview
- GitHub LangGraph: https://github.com/langchain-ai/langgraph
