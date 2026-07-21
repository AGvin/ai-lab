<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5c11d8ee7be5443f10b28e2aa34e653069dea924
  mode: translated
-->

# Створення Agent Skills

Цей tutorial пояснює, як проєктувати, реалізовувати, тестувати й публікувати Agent Skill. Попередній досвід роботи зі skills не потрібен.

Якісний skill перетворює повторно використовуваний спосіб роботи на невеликий пакет, який легко перевірити. Мета не в тому, щоб приховати reasoning у великому prompt. Мета — зробити workflow discoverable, predictable, maintainable і safe.

## Переклади

- [English](../../)
- Українська

## Навчальні цілі

Після завершення цього guide ви повинні вміти:

- визначати, чи має workflow бути skill, prompt, tool, repository instruction, MCP server або plugin;
- створювати valid skill directory і `SKILL.md`;
- писати discovery metadata, що активує skill для правильних tasks;
- відокремлювати core instructions від references, scripts і assets;
- проєктувати approval gates і failure behavior;
- тестувати discovery, activation, execution і portability;
- version і publish skill без несподіванок для users.

## 1. Визначте, чи skill є правильною abstraction

Створюйте skill, коли ту саму **procedure** потрібно повторно використовувати в різних tasks або projects і завантажувати лише за потреби.

Типові приклади:

- diagnosis складного bug через disciplined loop;
- підготовка release notes із визначеного source range;
- review pull request відповідно до repository standards;
- інтерв’ювання user перед створенням technical design;
- перетворення recurring report на consistent document.

Не створюйте skill лише тому, що prompt довгий.

| Потреба | Кращий варіант |
|---|---|
| One-off instruction для поточної conversation | Prompt |
| Facts і conventions, що мають завжди діяти в одному repository | Repository instructions, наприклад `AGENTS.md` або `CLAUDE.md` |
| Deterministic operation, яку model має виконати | Tool або script |
| Standard connection до external tools, resources або prompts | MCP server |
| Installable platform-specific bundle зі skills та integrations | Plugin |
| Reusable procedure, що вибирається лише для relevant tasks | Agent Skill |

Skill може викликати tools, читати repository instructions, використовувати MCP capabilities і поширюватися всередині plugin. Ці concepts доповнюють одне одного.

## 2. Визначте behavioral contract до створення files

Створіть коротку design note з такими fields:

```text
Назва:
Проблема користувача:
Використовувати, коли:
Не використовувати, коли:
Потрібні inputs:
Очікувані outputs:
Доступні tools:
Side effects:
Approval points:
Failure behavior:
Критерії успіху:
```

Приклад:

```text
Назва: release-notes
Проблема користувача: Maintainers потрібні consistent evidence-backed release notes.
Використовувати, коли: Підготовка release, changelog або summary merged changes.
Не використовувати, коли: Написання marketing copy без відомого change range.
Потрібні inputs: Base і head revisions або список merged changes.
Очікувані outputs: Categorized Markdown release notes із source references.
Доступні tools: Git history і pull-request reader.
Side effects: За замовчуванням відсутні.
Approval points: Запитати перед publication або створенням release.
Failure behavior: Зупинитися, якщо release range неможливо встановити.
Критерії успіху: Кожне твердження відповідає included change.
```

Цей contract запобігає перетворенню skill на необмежену instruction «зроби все».

## 3. Створіть мінімальний directory

Portable skill починається з одного directory, що містить `SKILL.md`:

```text
release-notes/
└── SKILL.md
```

Використовуйте lowercase name з одиничними hyphens:

```text
release-notes       # добре
ReleaseNotes        # уникайте
release_notes       # уникайте
release--notes      # уникайте
```

Open format вимагає, щоб entrypoint directory називався точно `SKILL.md`.

## 4. Напишіть valid frontmatter

Почніть `SKILL.md` із YAML frontmatter:

```markdown
---
name: release-notes
description: Draft evidence-backed release notes from a known revision range or set of merged changes. Use when preparing a software release, changelog, or stakeholder change summary.
---
```

Обов’язкові fields:

- `name` — stable machine-readable identifier;
- `description` — discovery text, який пояснює, що робить skill і коли його слід вибирати.

Standard також визначає optional fields:

```yaml
license: MIT
compatibility: Requires Git history or pull-request access.
metadata:
  author: example-team
  version: "1.0.0"
  category: release-management
```

Деякі clients розпізнають додаткові fields. Залишайте client-specific extensions optional і документуйте behavior, коли інший client їх ігнорує.

### Напишіть description достатньої якості для discovery

Слабкий description описує лише output:

```yaml
description: Creates release notes.
```

Сильніший description містить:

1. task;
2. qualifying context;
3. корисну trigger language;
4. важливі exclusions, коли можлива ambiguity.

```yaml
description: Draft evidence-backed release notes from Git commits or merged pull requests. Use for release preparation, changelog generation, or stakeholder summaries when a concrete change range is available; do not use for speculative product marketing.
```

Не розміщуйте весь workflow у description. Discovery metadata має бути достатньо compact для відображення в skill catalog.

## 5. Напишіть instruction body

Beginner-friendly body skill зазвичай містить:

```markdown
# Release notes workflow

## When to use

## Required inputs

## Workflow

## Output format

## Approval and safety rules

## Failure handling

## References
```

Віддавайте перевагу imperative і testable steps:

```markdown
## Workflow

1. Establish the exact base and head revisions.
2. Enumerate changes inside that range.
3. Exclude merges, formatting-only changes, and internal refactors unless they affect users.
4. Group retained changes by user impact.
5. Identify breaking changes and migrations explicitly.
6. Attach a source commit or pull request to every non-trivial claim.
7. Present the draft for review; do not publish it without explicit approval.
```

Уникайте vague language, наприклад «make it good», «use best practices» або «handle errors appropriately». Визначайте observable behavior.

## 6. Зберігайте entrypoint focused

Повний `SKILL.md` завантажується під час activation skill. Великі background references не повинні споживати context при кожному invocation.

Зі зростанням complexity використовуйте таку structure:

```text
release-notes/
├── SKILL.md
├── references/
│   ├── categories.md
│   └── style-guide.md
├── scripts/
│   └── collect-changes.py
└── assets/
    └── release-template.md
```

### `references/`

Використовуйте references для material, який model має читати лише в конкретних situations:

- domain terminology;
- довгі classification rules;
- provider-specific instructions;
- examples і edge cases;
- API або file-format details.

Явно посилайтеся на references із `SKILL.md`:

```markdown
When classifying a change, read [`references/categories.md`](./references/categories.md).
```

### `scripts/`

Використовуйте scripts для deterministic або повторно error-prone operations:

- parsing logs;
- collecting Git history;
- validating schemas;
- checking links;
- generating fixed report structure.

Script повинен:

- declare runtime і dependencies;
- validate input;
- produce machine-readable або clearly delimited output;
- повертати non-zero exit status при failure;
- уникати hidden network access або destructive defaults;
- за можливості підтримувати dry-run mode для consequential changes.

### `assets/`

Використовуйте assets для files, які копіюються або адаптуються в output:

- document templates;
- configuration skeletons;
- sample datasets;
- diagrams або images;
- style resources.

Assets є output resources, а не instructions. Behavioral guidance розміщуйте у `SKILL.md` або `references/`.

## 7. Приклад A: мінімальний skill

Directory:

```text
friendly-release-notes/
└── SKILL.md
```

Повний `SKILL.md`:

```markdown
---
name: friendly-release-notes
description: Turn a supplied list of completed changes into concise, user-facing Markdown release notes. Use when the user provides a concrete release scope and wants readable notes; do not invent changes or publish automatically.
license: MIT
---

# Friendly release notes

## Required input

Obtain a concrete list of completed changes. If no reliable source is available, stop and ask for one.

## Workflow

1. Remove duplicates and implementation-only details that do not affect users.
2. Group changes under `Added`, `Changed`, `Fixed`, and `Deprecated` only when those groups contain content.
3. Rewrite each item in plain language while preserving technical accuracy.
4. Mark breaking changes with **Breaking** and include the required migration action.
5. Do not invent benefits, dates, issue numbers, or compatibility claims.

## Output

Return Markdown with a one-sentence summary followed by grouped bullets.

## Safety

Produce a draft only. Publishing, tagging, or creating a release requires explicit approval.
```

Цей skill корисний без tools. У tool-enabled client його можна розширити для automatic gathering change list, але ця capability не припускається.

## 8. Приклад B: skill із references

Directory:

```text
sfcc-log-analyzer/
├── SKILL.md
└── references/
    └── error-classification.md
```

`SKILL.md`:

```markdown
---
name: sfcc-log-analyzer
description: Deduplicate Salesforce Commerce Cloud production errors, count occurrences, preserve representative stack traces, and rank investigation priority. Use when analyzing SFCC log exports or repeated application exceptions.
compatibility: Requires readable text logs; optional shell or scripting access improves large-file processing.
---

# SFCC log analysis

## Workflow

1. Preserve the original log as read-only evidence.
2. Normalize volatile request IDs, timestamps, and thread identifiers without removing class names, messages, controller routes, or stack frames.
3. Group records only when the normalized error signature and relevant stack root match.
4. Count all occurrences and retain one representative full stack trace.
5. Classify each group using [`references/error-classification.md`](./references/error-classification.md).
6. Rank by impact, frequency, reproducibility, and confidence.
7. Separate confirmed causes from hypotheses.

## Output

For every group provide signature, count, priority, representative stack trace, likely owner, evidence, and next diagnostic action.

## Safety

Redact credentials, tokens, personal data, session IDs, and customer payloads before reproducing log content.
```

`references/error-classification.md`:

```markdown
# Error classification

## Priority 1

Security exposure, checkout failure, data corruption, widespread authentication failure, or an exception blocking a critical customer journey.

## Priority 2

Repeated functional failure with a workaround, significant operational noise, or a defect affecting a limited segment.

## Priority 3

Low-frequency issue, recoverable integration failure, or warning without demonstrated user impact.

## Confidence

- Confirmed: directly supported by stack trace and surrounding evidence.
- Probable: multiple signals support one explanation but reproduction is missing.
- Unknown: evidence is insufficient; state the next observation required.
```

Classification document може розвиватися, не збільшуючи activation instructions без потреби.

## 9. Приклад C: skill зі script

Directory:

```text
repository-link-checker/
├── SKILL.md
└── scripts/
    └── check-links.py
```

`SKILL.md`:

```markdown
---
name: repository-link-checker
description: Validate relative Markdown links in a documentation tree and report missing targets without modifying files. Use before documentation commits or pull requests.
compatibility: Requires Python 3.10 or newer.
---

# Repository link checker

1. Determine the documentation root.
2. Run `python3 scripts/check-links.py <root>`.
3. Treat non-zero exit status as a failed validation.
4. Report each broken source path, link target, and line number.
5. Do not rewrite links automatically unless the user explicitly requests fixes.
6. After fixes, rerun the checker and report the final count.
```

Спрощений `scripts/check-links.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check-links.py <documentation-root>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    failures = 0
    for source in root.rglob("*.md"):
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for raw_target in LINK.findall(line):
                target = raw_target.split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (source.parent / target).resolve()
                if not resolved.exists():
                    failures += 1
                    print(f"{source}:{line_number}: missing {raw_target}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Script виконує deterministic checking. Skill забезпечує judgment щодо scope, remediation і reporting.

## 10. Спроєктуйте використання tools і approvals

Skill сам по собі ніколи не надає tool. Документуйте required capabilities і явно обробляйте їх відсутність.

Для кожного side effect визначте:

- operation;
- affected data і system;
- чи є він reversible;
- required approval;
- verification після execution.

Приклад:

```markdown
Before creating a Git tag:

1. Show the exact tag name, target commit, and release notes.
2. Wait for explicit approval.
3. Create the tag only on the approved target.
4. Read the tag back and verify its commit.
```

Не приховуйте approval requirements наприкінці довгого document.

## 11. User-invoked і model-invoked behavior

Open specification не вимагає universal invocation-mode field. Clients і collections можуть додавати conventions, наприклад:

- explicit slash-command orchestration skills;
- automatically selected discipline skills;
- fields, що disable model invocation;
- platform UI metadata.

Проєктуйте broad interview або orchestration workflows для explicit invocation, якщо automatic activation буде disruptive. Проєктуйте narrow clearly triggered disciplines для automatic discovery.

Зберігайте portable workflow valid, навіть коли client ігнорує invocation-specific extensions.

## 12. Додавайте client metadata лише за потреби

Деякі clients або plugin systems підтримують додаткові files, наприклад presentation definition `agents/openai.yaml` або plugin manifests.

Розглядайте ці files як adapters навколо portable skill:

```text
release-notes/
├── SKILL.md
└── agents/
    └── openai.yaml
```

Не переносьте essential workflow rules виключно в client-specific file. Інший client Agent Skills може ніколи його не прочитати.

## 13. Протестуйте skill

Тестуйте чотири layers окремо.

### Structural validation

Перевірте:

- directory і `name` збігаються;
- `SKILL.md` використовує точну capitalization;
- YAML parse успішно;
- required fields існують;
- referenced paths існують;
- scripts працюють у clean environment;
- licenses і dependencies задокументовані.

### Discovery tests

Напишіть positive prompts, які повинні expose або select skill:

```text
Prepare user-facing release notes for commits v2.3.0..HEAD.
```

Напишіть близькі negative prompts:

```text
Write a launch announcement for a feature that has not shipped yet.
```

Skill має відповідати першому й не претендувати на другий.

### Execution tests

Використовуйте representative fixtures і перевіряйте observable invariants:

- required questions ставляться;
- steps виконуються в expected order;
- evidence зберігається;
- dangerous actions зупиняються для approval;
- output відповідає promised schema;
- failures не створюють silent partial success.

### Cross-client tests

Коли portability важлива, запускайте однакові fixtures у кожному supported client. Фіксуйте відмінності в:

- discovery;
- invocation syntax;
- path resolution;
- script execution;
- permissions;
- unsupported metadata;
- context або output limits.

## 14. Перевірте поширені failure modes

### Description надто broad

Symptom: skill активується для unrelated requests.

Fix: додайте qualifying context, звузьте task і перенесіть broad orchestration до explicit invocation.

### Description надто vague

Symptom: skill ніколи не знаходиться.

Fix: додайте concrete tasks і language, яку users використовують природно.

### `SKILL.md` містить цілий handbook

Symptom: activation споживає excessive context і model пропускає operational steps.

Fix: зберігайте workflow в entrypoint, а background material перенесіть у `references/`.

### Skill припускає недоступні tools

Symptom: він вигадує tool results або зупиняється.

Fix: declare compatibility, detect capability availability і визначте conversational fallback або explicit stop condition.

### Scripts приховують consequential behavior

Symptom: коротка instruction запускає opaque writes або network calls.

Fix: документуйте inputs, outputs, dependencies, side effects, dry-run behavior і approval gates.

### Happy path протестовано, а failure — ні

Symptom: missing inputs або partial tool failures створюють plausible, але incorrect output.

Fix: тестуйте absent files, malformed data, denied permissions, network failures і interrupted execution.

## 15. Version і publish

Для published skill:

1. виберіть stable source repository;
2. додайте license;
3. документуйте supported clients і runtime dependencies;
4. tag releases або record immutable revisions;
5. підтримуйте changelog для behavioral changes;
6. розглядайте changes instructions як code changes, що потребують review;
7. тестуйте upgrades із попередньої published version;
8. не розширюйте permissions або network access без явного повідомлення.

Collection може поширюватися через direct copy, installer, наприклад `skills.sh`, або platform-specific plugin. Див. [Джерела й колекції](../../../sources/l10n/uk_UA/) і [Plugins](../../../../../plugins/l10n/uk_UA/).

## Контрольний список створення

- [ ] Проблема procedural і recurring.
- [ ] Умови використання й невикористання explicit.
- [ ] Inputs, outputs, tools, side effects, approvals і failures визначено.
- [ ] `name` і directory збігаються.
- [ ] `description` проходить positive і negative discovery tests.
- [ ] Entrypoint focused.
- [ ] References, scripts і assets мають чіткі ролі.
- [ ] Scripts validate input і fail visibly.
- [ ] Consequential actions потребують explicit approval.
- [ ] Structural, discovery, execution, failure і cross-client tests проходять.
- [ ] License, compatibility, source revision і update policy задокументовано.

## Джерела

- Специфікація Agent Skills: https://agentskills.io/specification
- Огляд створення skills: https://agentskills.io/skill-creation
- Оптимізація descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- [Використання Agent Skills](../../../using/l10n/uk_UA/)
- [Підтримка платформ](../../../platform-support/l10n/uk_UA/)
