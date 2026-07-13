<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:b3b2450c91323443788addbae07b94b813b38cc2
  mode: translated
-->

# AutoGen

Локалізована точка входу для multi-agent conversation framework.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: Framework оркестрації агентів
Основний сценарій: Створення й координація multi-agent systems через conversable agents, використання tools, виконання коду та участь людини
Модель доступу: Open-source проєкт із локальним framework і пов’язаними дослідницькими інструментами Microsoft
Ліцензія: MIT для коду; CC-BY-4.0 для документації та іншого вмісту репозиторію
Модель вихідного коду: Open source
Сигнал прав використання: Permissive core; trademarks Microsoft, cloud services, провайдерів моделей і third-party integrations слід перевіряти окремо
Сигнал моделі вартості: BYO cost; framework open-source, але робота залежить від вибраних провайдерів моделей, execution environments, tools та необов’язкової інфраструктури
Модель розгортання: Hybrid; локальний framework із необов’язковими tools, code execution environments, providers і Studio/ecosystem tooling
Сигнал впровадження: Popular; видиме на GitHub поширення високе, але зрілість package line і migration path потребують перевірки
Експлуатаційні вимоги: Framework AutoGen, вибрані провайдери моделей, tools, credentials, середовище виконання коду й необов’язковий Studio або ecosystem tooling
Режими інтеграції: Python, conversable agents, multi-agent conversations, tool execution, code execution, human-in-the-loop workflows, model providers, AutoGen Studio
Джерело: https://github.com/microsoft/autogen
Примітки щодо ризиків: Multi-agent і code-execution framework. Перевірте sandboxing, browser access, localhost exposure, дозволи tools, виконання згенерованого коду, credentials провайдерів, дані для model APIs і людські approval gates.
Востаннє перевірено: 2026-07-06
```

## Огляд

AutoGen — framework для створення multi-agent AI applications навколо розмов між агентами.

Основна ідея полягає в conversable agents: вони обмінюються повідомленнями, викликають tools, виконують код, запитують input людини й координуються для виконання задачі через структуровані шаблони взаємодії.

## Відповідність AI Lab

AutoGen належить до `agent-orchestration/`, бо його основна роль — координація кількох агентів і протоколів взаємодії, а не робота як одного самостійного агента.

Використовуйте його як орієнтир для:

- multi-agent conversation patterns;
- співпраці агентів через message passing;
- workflows, що поєднують LLM agents, tools, code execution і human checkpoints;
- порівняння з graph-based runtimes на зразок LangGraph;
- порівняння з crew/task abstractions на зразок CrewAI;
- оцінювання development tools на зразок AutoGen Studio.

## Знімок перевірки

Станом на 2026-07-06 upstream GitHub-репозиторій описує AutoGen як programming framework для agentic AI. Legal notice репозиторію визначає ліцензію MIT для коду й CC-BY-4.0 для документації та іншого вмісту.

Поточний upstream-репозиторій далі посилається на документацію AutoGen і матеріали AutoGen Studio, але впровадження має включати перевірку package line і migration path, бо AutoGen пройшов кілька етапів пакетів та API.

## Нотатки з оцінювання

До впровадження оцініть:

- зрілість поточної package line AutoGen і migration path;
- підтримуваних провайдерів моделей та tool integrations;
- sandboxing виконання коду й межі файлової системи;
- browser, localhost і network exposure у development tools;
- семантику human-in-the-loop approval;
- observability і debugging multi-agent runs;
- роботу з чутливими prompts, credentials, source code та execution artifacts.

## Посилання

- GitHub AutoGen: https://github.com/microsoft/autogen
- Документація AutoGen: https://microsoft.github.io/autogen
- Стаття AutoGen: https://arxiv.org/abs/2308.08155
- Стаття AutoGen Studio: https://arxiv.org/abs/2408.15247
