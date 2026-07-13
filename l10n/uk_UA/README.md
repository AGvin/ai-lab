<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:27d2f4b90f01df57f127ad4ca034e92d926b06f1
  mode: translated
-->

# AI Lab

Практична лабораторія ШІ для моделей, інструментів, локального inference, benchmarks, нотаток про обладнання та automation workflows.

## Переклади

- [English](../../)
- Українська

## Статус

Цей репозиторій є активною публічною лабораторією документації. Вміст додається поступово, коли тема має реальні нотатки, посилання або практичну цінність для оцінювання.

## Мапа документації

### Почати звідси

- [`overview/`](../../docs/overview/l10n/uk_UA/) — модель документації репозиторію, поточна структура, правила assets і настанови з розширення.

### Software

- [`software/`](../../docs/software/l10n/uk_UA/) — пов’язане зі ШІ ПЗ, платформи моделей, inference tools, агенти, засоби автоматизації та виконувані development workflows.
  - [`development-workflows/`](../../docs/software/sub/development-workflows/l10n/uk_UA/) — інструменти, що структурують розроблення ПЗ за допомогою ШІ через специфікації, плани, задачі, валідацію та етапи реалізації.
    - [`spec-kit/`](../../docs/software/sub/development-workflows/sub/spec-kit/l10n/uk_UA/) — open-source toolkit GitHub для Spec-Driven Development з coding agents на основі ШІ.

### Нотатки й підтримка рішень

- [`concepts/`](../../docs/notes/sub/concepts/l10n/uk_UA/) — практичні й фундаментальні поняття ШІ за темою та пріоритетом читання.
  - [Основи й архітектура](../../docs/notes/sub/concepts/sub/foundations-and-architecture/l10n/uk_UA/) — ключові поняття, що пояснюють, чим є сучасні моделі ШІ та як співвідносяться їхні головні архітектурні сімейства.
    - Основні
      - [`foundation-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/foundation-models/l10n/uk_UA/) — великі моделі багаторазового використання, навчені на широких даних і адаптовані до багатьох подальших задач.
      - [`large-language-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/large-language-models/l10n/uk_UA/) — орієнтовані на мову фундаментальні моделі, які прогнозують і генерують послідовності токенів.
      - [`multimodal-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/multimodal-models/l10n/uk_UA/) — моделі, які обробляють або генерують кілька модальностей, зокрема текст, зображення, аудіо чи відео.
    - Корисні
      - [`transformers/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/transformers/l10n/uk_UA/) — архітектури нейронних мереж, побудовані навколо уваги й паралельного оброблення послідовностей.
      - [`attention/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/attention/l10n/uk_UA/) — механізм, що зважує важливість елементів вхідних даних для операції моделі.
      - [`mixture-of-experts/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/mixture-of-experts/l10n/uk_UA/) — розріджені архітектури моделей, які спрямовують кожен вхід через вибрані експертні компоненти.
    - Спеціалізовані
      - [`artificial-intelligence/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/artificial-intelligence/l10n/uk_UA/) — широка галузь систем, що виконують задачі сприйняття, міркування, генерації або ухвалення рішень.
      - [`machine-learning/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/machine-learning/l10n/uk_UA/) — методи, які навчаються закономірностей із даних замість опори лише на явно запрограмовані правила.
      - [`deep-learning/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/deep-learning/l10n/uk_UA/) — машинне навчання на основі нейронних мереж із багатьма шарами оброблення.
      - [`neural-networks/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/neural-networks/l10n/uk_UA/) — параметризовані обчислювальні структури зі з’єднаних шарів або блоків оброблення.
      - [`self-attention/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/self-attention/l10n/uk_UA/) — увага, обчислена між позиціями однієї послідовності.
      - [`encoder-decoder/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/encoder-decoder/l10n/uk_UA/) — структури моделей, що кодують вхідні дані, генерують вихідні або поєднують обидві ролі.
      - [`dense-and-sparse-models/`](../../docs/notes/sub/concepts/sub/foundations-and-architecture/sub/dense-and-sparse-models/l10n/uk_UA/) — щільні моделі активують більшість параметрів для кожного входу, а розріджені — вибрані підмножини.
  - [Використання моделей і генерація](../../docs/notes/sub/concepts/sub/model-usage-and-generation/l10n/uk_UA/) — поняття для ефективного використання навчених моделей через чати, API, застосунки й локальні середовища виконання.
    - Основні
      - [`tokens-and-tokenization/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/tokens-and-tokenization/l10n/uk_UA/) — процес поділу вхідних і вихідних даних на одиниці, які модель читає й генерує.
      - [`context-window/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/context-window/l10n/uk_UA/) — обмежений обсяг токенізованої інформації, який модель може врахувати в одному запиті.
      - [`prompting/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/prompting/l10n/uk_UA/) — надання інструкцій, контексту, прикладів і обмежень для спрямування моделі.
      - [`system-prompts/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/system-prompts/l10n/uk_UA/) — високопріоритетні інструкції, що визначають роль, поведінку й операційні межі асистента.
      - [`structured-output/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/structured-output/l10n/uk_UA/) — вихід моделі, обмежений машинозчитуваною структурою на кшталт JSON або схеми.
      - [`hallucinations/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/hallucinations/l10n/uk_UA/) — непідтверджений або неправильний вихід моделі, поданий у правдоподібній формі.
    - Корисні
      - [`few-shot-prompting/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/few-shot-prompting/l10n/uk_UA/) — промптинг із невеликою кількістю прикладів бажаної поведінки.
      - [`sampling-parameters/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/sampling-parameters/l10n/uk_UA/) — параметри на кшталт температури, top-p, top-k і seed, що впливають на вибір токенів.
      - [`reasoning-models/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/reasoning-models/l10n/uk_UA/) — моделі, оптимізовані витрачати додаткові обчислення на багатоетапне розв’язання задач.
      - [`model-capabilities-and-limitations/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/model-capabilities-and-limitations/l10n/uk_UA/) — практичні сильні сторони, межі й режими відмови конкретної моделі або розгортання.
    - Спеціалізовані
      - [`constrained-generation/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/constrained-generation/l10n/uk_UA/) — генерація, обмежена граматикою, схемою, набором токенів або іншим формальним обмеженням.
      - [`chain-of-thought/`](../../docs/notes/sub/concepts/sub/model-usage-and-generation/sub/chain-of-thought/l10n/uk_UA/) — проміжний текст міркування або внутрішні обчислення для підтримки багатоетапних відповідей.
  - [Retrieval і знання](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/l10n/uk_UA/) — поняття для під’єднання моделей до зовнішньої інформації, придатних до пошуку документів і контексту, підкріпленого свідченнями.
    - Основні
      - [`rag/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/rag/l10n/uk_UA/) — Retrieval-Augmented Generation поєднує зовнішній retrieval із генерацією моделі.
      - [`embeddings/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/embeddings/l10n/uk_UA/) — числові представлення, що розміщують семантично пов’язані елементи поруч у векторному просторі.
      - [`chunking/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/chunking/l10n/uk_UA/) — поділ вихідного матеріалу на придатні до retrieval одиниці зі збереженням достатнього контексту.
      - [`semantic-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/semantic-search/l10n/uk_UA/) — retrieval на основі значення, а не лише точних збігів слів.
      - [`hybrid-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/hybrid-search/l10n/uk_UA/) — retrieval, що поєднує сигнали семантичного й лексичного пошуку.
      - [`grounding/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/grounding/l10n/uk_UA/) — обмеження згенерованих тверджень наданими свідченнями, інструментами чи авторитетними джерелами.
    - Корисні
      - [`vector-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-search/l10n/uk_UA/) — retrieval найближчих сусідів у векторах embeddings.
      - [`vector-databases/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/vector-databases/l10n/uk_UA/) — системи зберігання й індексування, оптимізовані для векторів і пошуку подібності.
      - [`keyword-search/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/keyword-search/l10n/uk_UA/) — лексичний retrieval за термінами, присутніми у вихідному тексті.
      - [`reranking/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/reranking/l10n/uk_UA/) — модель релевантності другого етапу, що змінює порядок отриманих кандидатів.
      - [`citations/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/citations/l10n/uk_UA/) — посилання, що пов’язують згенеровані твердження з підтвердними джерелами.
      - [`metadata-filtering/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/metadata-filtering/l10n/uk_UA/) — обмеження retrieval за атрибутами джерела, дати, версії, tenant або політики доступу.
    - Спеціалізовані
      - [`bm25/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/bm25/l10n/uk_UA/) — імовірнісний метод лексичного ранжування, широко вживаний у retrieval документів.
      - [`graph-rag/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/graph-rag/l10n/uk_UA/) — RAG, що використовує структури графа та зв’язки для формування контексту.
      - [`knowledge-graphs/`](../../docs/notes/sub/concepts/sub/retrieval-and-knowledge/sub/knowledge-graphs/l10n/uk_UA/) — структуровані представлення сутностей та їхніх зв’язків.
  - [Агенти й автоматизація](../../docs/notes/sub/concepts/sub/agents-and-automation/l10n/uk_UA/) — поняття для налаштування систем ШІ, які планують, використовують інструменти, підтримують стан і виконують контрольовані дії.
    - Основні
      - [`ai-agents/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/ai-agents/l10n/uk_UA/) — системи ШІ, які досягають цілей завдяки рішенням моделі, інструментам, стану та ітеративним діям.
      - [`agentic-workflows/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/agentic-workflows/l10n/uk_UA/) — контрольовані багатоетапні процеси, що поєднують рішення моделі з детермінованою логікою робочого процесу.
      - [`tool-calling/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/tool-calling/l10n/uk_UA/) — вибір моделлю зареєстрованої зовнішньої операції та формування аргументів для її виконання.
      - [`agent-state/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/agent-state/l10n/uk_UA/) — явні робочі дані, що відстежують поступ, рішення та проміжні результати.
      - [`agent-memory/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/agent-memory/l10n/uk_UA/) — механізми збереження корисної інформації поза межами поточного запиту.
      - [`planning/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/planning/l10n/uk_UA/) — вибір і впорядкування дій, потрібних для досягнення цілі.
      - [`verification-and-reflection/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/verification-and-reflection/l10n/uk_UA/) — перевірка результатів і перегляд підходу за потреби.
      - [`human-in-the-loop/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/human-in-the-loop/l10n/uk_UA/) — перевірка, схвалення або втручання людини на визначених етапах.
      - [`idempotency/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/idempotency/l10n/uk_UA/) — проєктування дій так, щоб безпечне повторення не створювало дубльованих наслідків.
      - [`failure-recovery/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/failure-recovery/l10n/uk_UA/) — безпечне відновлення поступу після збоїв моделі, інструмента, мережі чи робочого процесу.
    - Корисні
      - [`function-calling/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/function-calling/l10n/uk_UA/) — структурований інтерфейс інструментів, у якому вихід моделі визначає функцію та аргументи.
      - [`task-decomposition/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/task-decomposition/l10n/uk_UA/) — поділ великої задачі на менші одиниці, які можна перевірити.
      - [`retries/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/retries/l10n/uk_UA/) — повторення допустимих невдалих операцій за обмеженими правилами.
      - [`autonomy-levels/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/autonomy-levels/l10n/uk_UA/) — ступінь самостійності в ухваленні рішень, наданий системі ШІ.
    - Спеціалізовані
      - [`multi-agent-systems/`](../../docs/notes/sub/concepts/sub/agents-and-automation/sub/multi-agent-systems/l10n/uk_UA/) — системи, у яких кілька агентів координуються, конкурують, перевіряють роботу або спеціалізуються.
  - [Інференс і обслуговування моделей](../../docs/notes/sub/concepts/sub/inference-and-serving/l10n/uk_UA/) — поняття для локального запуску навчених моделей або надання їх як сервісів, а також розуміння використання ресурсів і продуктивності.
    - Основні
      - [`inference/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/inference/l10n/uk_UA/) — запуск навченої моделі для оброблення входу й створення виходу.
      - [`quantization/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/quantization/l10n/uk_UA/) — зменшення числової точності для зниження вимог моделі до пам’яті й обчислень.
      - [`numerical-precision/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/numerical-precision/l10n/uk_UA/) — числовий формат ваг, активацій і обчислень моделі.
      - [`model-formats/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/model-formats/l10n/uk_UA/) — файлові формати й формати серіалізації для зберігання та завантаження артефактів моделі.
      - [`gpu-offloading/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/gpu-offloading/l10n/uk_UA/) — перенесення вибраних обчислень або шарів моделі на GPU, коли інша робота залишається деінде.
      - [`kv-cache/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/kv-cache/l10n/uk_UA/) — кешовані ключі й значення уваги, повторно використовувані під час авторегресійної генерації.
      - [`latency/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/latency/l10n/uk_UA/) — час, потрібний для створення відповіді або досягнення визначеного етапу виходу.
      - [`throughput/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/throughput/l10n/uk_UA/) — обсяг роботи моделі, виконаний за одиницю часу.
      - [`performance-metrics/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/performance-metrics/l10n/uk_UA/) — показники часу до першого токена, токенів за секунду, затримки й використання пам’яті.
    - Корисні
      - [`model-serving/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/model-serving/l10n/uk_UA/) — надання інференсу через керований процес, API, чергу або сервіс середовища виконання.
      - [`model-loading/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/model-loading/l10n/uk_UA/) — переміщення артефактів моделі до RAM, VRAM або керованої середовищем пам’яті для виконання.
      - [`cpu-inference/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/cpu-inference/l10n/uk_UA/) — виконання обчислень моделі переважно на процесорах загального призначення.
      - [`gpu-inference/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/gpu-inference/l10n/uk_UA/) — виконання обчислень моделі переважно на графічних процесорах для паралельних навантажень.
      - [`context-caching/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/context-caching/l10n/uk_UA/) — повторне використання раніше обробленого контексту промпту для зменшення повторних обчислень.
    - Спеціалізовані
      - [`flash-attention/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/flash-attention/l10n/uk_UA/) — реалізації уваги, оптимізовані для зменшення обміну з пам’яттю й підвищення ефективності GPU.
      - [`continuous-batching/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/continuous-batching/l10n/uk_UA/) — динамічне об’єднання активних запитів інференсу для ефективнішого обслуговування.
      - [`speculative-decoding/`](../../docs/notes/sub/concepts/sub/inference-and-serving/sub/speculative-decoding/l10n/uk_UA/) — використання швидшого чернеткового процесу для пропонування токенів, які перевіряє цільова модель.
  - [Навчання й адаптація](../../docs/notes/sub/concepts/sub/training-and-adaptation/l10n/uk_UA/) — поняття для навчання моделей або адаптації наявних моделей до задач, доменів, переваг та обмежень розгортання.
    - Основні
      - [`fine-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/fine-tuning/l10n/uk_UA/) — продовження навчання моделі на цільових даних для зміни поведінки або продуктивності задачі.
      - [`parameter-efficient-fine-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/parameter-efficient-fine-tuning/l10n/uk_UA/) — методи адаптації, що навчають лише невелику частину параметрів моделі або додані компоненти.
      - [`lora/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/lora/l10n/uk_UA/) — Low-Rank Adaptation навчає компактні низькорангові оновлення замість усіх ваг базової моделі.
      - [`qlora/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/qlora/l10n/uk_UA/) — адаптація на основі LoRA з квантованою базовою моделлю для зменшення використання пам’яті.
    - Корисні
      - [`supervised-fine-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/supervised-fine-tuning/l10n/uk_UA/) — fine-tuning на розмічених прикладах, які поєднують inputs із бажаними outputs.
      - [`adapters/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/adapters/l10n/uk_UA/) — невеликі навчувані модулі, приєднані до базової моделі для повторно використовуваної спеціалізації.
      - [`instruction-tuning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/instruction-tuning/l10n/uk_UA/) — навчання моделі на прикладах «інструкція — відповідь» для кращого виконання задач.
      - [`synthetic-data/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/synthetic-data/l10n/uk_UA/) — дані навчання або оцінювання, згенеровані правилами, симуляціями чи моделями.
      - [`datasets/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/datasets/l10n/uk_UA/) — організовані колекції прикладів для навчання, адаптації або оцінювання.
      - [`overfitting/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/overfitting/l10n/uk_UA/) — ситуація, коли модель надто точно підлаштовується під навчальні дані й погано працює на нових прикладах.
    - Спеціалізовані
      - [`pretraining/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/pretraining/l10n/uk_UA/) — масштабне початкове навчання, що створює базову модель із широкими можливостями.
      - [`preference-optimization/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/preference-optimization/l10n/uk_UA/) — методи навчання, які віддають перевагу відповідям, оціненим як кращі за даними про переваги.
      - [`rlhf/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/rlhf/l10n/uk_UA/) — Reinforcement Learning from Human Feedback використовує сигнали людських переваг для зміни поведінки моделі.
      - [`dpo/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/dpo/l10n/uk_UA/) — Direct Preference Optimization навчає безпосередньо на парах бажаних і відхилених відповідей.
      - [`distillation/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/distillation/l10n/uk_UA/) — навчання меншої чи простішої моделі імітувати потужнішу модель-учителя.
      - [`pruning/`](../../docs/notes/sub/concepts/sub/training-and-adaptation/sub/pruning/l10n/uk_UA/) — вилучення параметрів або структур моделі, які вважають непотрібними для цільової мети.
  - [Мультимодальні й генеративні медіа](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/l10n/uk_UA/) — поняття для моделей і робочих процесів із зображеннями, аудіо, відео та поєднаннями модальностей.
    - Основні
      - [`vision-language-models/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/vision-language-models/l10n/uk_UA/) — моделі, що спільно обробляють візуальні входи й природну мову.
      - [`image-generation/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-generation/l10n/uk_UA/) — створення зображень із тексту, зображень, макетів, масок чи інших умов.
      - [`diffusion-models/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/diffusion-models/l10n/uk_UA/) — генеративні моделі, які навчаються обертати поступове додавання шуму.
      - [`image-to-image/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-to-image/l10n/uk_UA/) — генерація перетвореного зображення з урахуванням наявного.
      - [`inpainting/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/inpainting/l10n/uk_UA/) — повторна генерація вибраних замаскованих ділянок зображення.
      - [`controlnet/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/controlnet/l10n/uk_UA/) — зумовлення дифузійних моделей структурними засобами: краями, глибиною чи позою.
      - [`multimodal-context/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/multimodal-context/l10n/uk_UA/) — сукупна текстова, візуальна, аудіо-, відео- чи документна інформація в запиті моделі.
    - Корисні
      - [`text-to-image/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-image/l10n/uk_UA/) — генерація зображень з описів природною мовою.
      - [`outpainting/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/outpainting/l10n/uk_UA/) — розширення зображення за його початкові межі.
      - [`image-embeddings/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/image-embeddings/l10n/uk_UA/) — векторні подання для порівняння, пошуку чи класифікації візуального вмісту.
      - [`speech-to-text/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/speech-to-text/l10n/uk_UA/) — перетворення усного мовлення на письмовий текст.
      - [`text-to-speech/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/text-to-speech/l10n/uk_UA/) — синтез усного мовлення з письмового тексту.
      - [`video-generation/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/video-generation/l10n/uk_UA/) — створення або перетворення послідовностей відеокадрів генеративними моделями.
    - Спеціалізовані
      - [`latent-space/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/latent-space/l10n/uk_UA/) — стиснене навчене подання, у якому генеративні моделі кодують і змінюють інформацію.
      - [`audio-generation/`](../../docs/notes/sub/concepts/sub/multimodal-and-generative-media/sub/audio-generation/l10n/uk_UA/) — створення музики, мовлення, звукових ефектів чи іншого аудіо генеративними моделями.
  - [Безпека, приватність і надійність](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/l10n/uk_UA/) — поняття для керування поведінкою моделей, захисту даних і зменшення операційних ризиків систем ШІ.
    - Основні
      - [`prompt-injection/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/prompt-injection/l10n/uk_UA/) — вхід, створений для перевизначення чи маніпулювання інструкціями системи ШІ.
      - [`indirect-prompt-injection/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/indirect-prompt-injection/l10n/uk_UA/) — шкідливі або суперечливі інструкції в зовнішньому вмісті.
      - [`trust-boundaries/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/trust-boundaries/l10n/uk_UA/) — явне розділення довірених інструкцій, систем, користувачів і недовірених даних.
      - [`least-privilege/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/least-privilege/l10n/uk_UA/) — надання системі лише дозволів для поточної задачі.
      - [`sandboxing/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/sandboxing/l10n/uk_UA/) — ізоляція виконання для обмеження наслідків збоїв або шкідливої поведінки.
      - [`secret-handling/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/secret-handling/l10n/uk_UA/) — захист облікових даних, токенів, ключів та інших чутливих даних.
      - [`data-privacy/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-privacy/l10n/uk_UA/) — контроль збирання, оброблення, зберігання й передавання особистих або конфіденційних даних.
      - [`retrieval-poisoning/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/retrieval-poisoning/l10n/uk_UA/) — маніпулювання індексованими знаннями для повернення оманливого чи шкідливого контексту.
    - Корисні
      - [`guardrails/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/guardrails/l10n/uk_UA/) — засоби перевірки, обмеження й моніторингу входів, виходів і дій моделі.
      - [`data-residency/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-residency/l10n/uk_UA/) — географічне або юрисдикційне місце зберігання чи оброблення даних.
      - [`provenance/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/provenance/l10n/uk_UA/) — відомості про походження, власність, перетворення й зберігання даних або артефактів моделі.
      - [`content-moderation/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/content-moderation/l10n/uk_UA/) — виявлення чи обмеження вмісту за політиками безпеки, права або платформи.
    - Спеціалізовані
      - [`jailbreaking/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/jailbreaking/l10n/uk_UA/) — спроби обійти налаштовані обмеження моделі.
      - [`model-alignment/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/model-alignment/l10n/uk_UA/) — спрямування поведінки моделі до визначених цілей, цінностей і політик.
      - [`data-poisoning/`](../../docs/notes/sub/concepts/sub/safety-privacy-and-reliability/sub/data-poisoning/l10n/uk_UA/) — псування навчальних даних для погіршення чи маніпулювання поведінкою моделі.
  - [Оцінювання та експлуатація](../../docs/notes/sub/concepts/sub/evaluation-and-operations/l10n/uk_UA/) — поняття для вибору, тестування, спостереження й експлуатації систем ШІ за реальних обмежень якості, вартості та надійності.
    - Основні
      - [`evals/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/evals/l10n/uk_UA/) — повторювані тести відповідності моделі чи системи ШІ визначеним вимогам.
      - [`model-selection/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/model-selection/l10n/uk_UA/) — вибір моделі за якістю задачі, можливостями, вартістю, затримкою, безпекою й обмеженнями розгортання.
      - [`model-routing/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/model-routing/l10n/uk_UA/) — динамічний вибір моделі відповідно до запиту чи операційної політики.
      - [`observability/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/observability/l10n/uk_UA/) — використання logs, metrics, traces і events для розуміння поведінки системи ШІ.
      - [`tracing/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/tracing/l10n/uk_UA/) — запис послідовності операцій моделі, інструментів, retrieval і workflow для одного виконання.
      - [`cost-management/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/cost-management/l10n/uk_UA/) — вимірювання й контроль витрат на моделі, інфраструктуру, сховища та інструменти.
      - [`latency-and-throughput/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/latency-and-throughput/l10n/uk_UA/) — балансування часу відповіді й обсягу роботи за одиницю часу.
      - [`quality-cost-tradeoffs/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/quality-cost-tradeoffs/l10n/uk_UA/) — вибір прийнятного балансу між якістю результату й операційними витратами.
    - Корисні
      - [`benchmarks/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/benchmarks/l10n/uk_UA/) — стандартизовані задачі чи datasets для порівняння моделей або систем.
      - [`evaluation-datasets/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/evaluation-datasets/l10n/uk_UA/) — добірки прикладів для тестування якості, безпеки, retrieval або виконання задач.
      - [`human-evaluation/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/human-evaluation/l10n/uk_UA/) — оцінювання результатів моделі людьми за явними критеріями.
      - [`fallback-models/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/fallback-models/l10n/uk_UA/) — альтернативні моделі, коли бажана модель не працює або недоступна.
      - [`caching/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/caching/l10n/uk_UA/) — повторне використання попередніх результатів чи оброблених даних для зменшення повторної роботи.
      - [`rate-limits/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/rate-limits/l10n/uk_UA/) — controls, що обмежують обсяг запитів за певний час.
    - Спеціалізовані
      - [`llm-as-a-judge/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/llm-as-a-judge/l10n/uk_UA/) — використання мовної моделі для оцінювання, ранжування чи критики результатів інших моделей.
      - [`retrieval-evaluation/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/retrieval-evaluation/l10n/uk_UA/) — вимірювання релевантності, повноти й правильності ранжування evidence у retrieval.
      - [`reproducibility/`](../../docs/notes/sub/concepts/sub/evaluation-and-operations/sub/reproducibility/l10n/uk_UA/) — можливість повторити оцінювання чи workflow за порівнюваних умов і результатів.
- [`benchmarks/`](../../docs/notes/sub/benchmarks/l10n/uk_UA/) — довідкові ресурси benchmark і leaderboard для оцінювання моделей, провайдерів і систем ШІ.
- [`comparisons/`](../../docs/notes/sub/comparisons/l10n/uk_UA/) — порівняння для підтримки рішень щодо моделей, інструментів, workflows, платформ і систем ШІ.

## Ліцензія

Цей репозиторій ліцензовано за MIT License.

Під час повторного використання чи адаптації матеріалів зберігайте оригінальне повідомлення про copyright і посилайтеся на цей репозиторій як на джерело.
