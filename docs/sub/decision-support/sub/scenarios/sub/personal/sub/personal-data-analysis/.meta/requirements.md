# Documentation Requirements

## Scenario Fit

- Present this scenario for an individual repeatedly analyzing their own structured or semi-structured data: spreadsheets, CSV/JSON exports, budgets, expenses, subscriptions, fitness/activity history, utility or smart-home telemetry, inventories, collections, logs, surveys, trackers, and similar personal datasets.
- Keep the scenario explicitly **personal**. Professional/client/employer datasets and governed business analytics belong in the applicable professional/team/organization routes when workplace policy, shared definitions, regulated data, access control, or production reporting materially change the decision.
- Distinguish this scenario from `everyday-home-user/`: occasional help with one table can stay there; this scenario applies when data preparation, repeatable calculation, visualization, comparison, or longitudinal analysis is a recurring workflow that materially changes the useful model/tool route.
- Distinguish it from `personal-knowledge-base-user/`: that scenario owns grounded retrieval and synthesis over a durable document corpus; this scenario owns structured-data calculation, transformation, aggregation, statistics, and visualization.
- Distinguish it from future/professional analyst scenarios: the user may use sophisticated methods, but the operating boundary remains their personal data and individual decisions rather than shared enterprise metrics or production data systems.

## Separate the Analysis Workloads

- Classify the recurring need before selecting one assistant/model:
  - inspect and understand an unfamiliar export or workbook;
  - clean, normalize, deduplicate, join, reshape, or categorize records;
  - calculate totals, rates, rolling values, cohorts, distributions, correlations, or other statistics;
  - compare periods, categories, devices, accounts, or scenarios;
  - find anomalies, missing values, outliers, or inconsistent records;
  - build charts, summaries, dashboards, or reports;
  - explain formulas, calculations, trends, and assumptions;
  - generate or repair spreadsheet formulas;
  - write or run Python/SQL for repeatable analysis;
  - forecast or model scenarios when the assumptions can be stated and validated.
- Do not force every workload into pure conversational reasoning. Spreadsheet formulas, SQL, Python/R, deterministic transformations, and purpose-built domain tools can be more appropriate computation engines, with the model acting as interface, code author, explainer, and reviewer.
- Preserve the distinction between **descriptive analysis** (`what the data contains`), **inference/modeling** (`what pattern or estimate follows under assumptions`), and **decision advice** (`what the user should do`). A model may help with all three, but they require different evidence and verification.

## Default Code-Backed Managed Route

- Use a managed assistant with uploaded-file support and an inspectable code-backed analysis environment as the default low-administration route when hosted processing fits the user's data boundary.
- Current ChatGPT data analysis supports common structured file types including spreadsheet and CSV files, can create tables/charts, and can run calculations, transformations, and statistical analysis with Python in a stateful Jupyter environment for applicable tasks. Treat exact file limits, plan access, model selection, connected-source support, and UI behavior as mutable.
- Prefer code-backed execution over asking the language model to perform non-trivial arithmetic mentally or to infer aggregate values from a large table in prose.
- When the product exposes generated analysis code, intermediate data, or assumptions, inspect them before relying on important results. Current ChatGPT guidance explicitly instructs users to review generated code, source data, and assumptions.
- Current Gemini Apps can upload and analyze spreadsheets and other files, and Gemini in Google Sheets can generate formulas, analysis/insights, charts, pivot-style operations, and other spreadsheet actions on eligible plans. Treat product availability and plan requirements as mutable.
- Evaluate assistants on the user's real datasets and accepted outputs rather than generic benchmark reputation: correct ingestion, transformations, calculations, reproducibility, chart accuracy, explanation quality, privacy boundary, latency, and correction effort.

## Spreadsheet-Native Route

- Prefer an assistant embedded in Excel or Google Sheets when the user's authoritative data already lives in a workbook and preserving formulas, references, tabs, formatting, and iterative edits is more useful than exporting data into a chat.
- Current ChatGPT for Excel and Google Sheets can build, update, and explain spreadsheets directly, including multi-tab files with formulas, references, and assumptions; current availability and usage limits remain mutable.
- Current Gemini in Sheets can create formulas, analyze sheet data, generate charts, and apply supported spreadsheet actions. Use available analysis-step/action-preview/undo surfaces as verification aids rather than treating generated edits as inherently correct.
- Before allowing broad edits, create or preserve a recoverable workbook version. Review changed formulas, ranges, references, units, and source rows before accepting a transformed workbook.
- Do not assume a chart remains linked to original source data merely because it was generated in a spreadsheet assistant; verify the actual chart data/range and refresh behavior for the specific product/workflow.
- For repeatable analysis, prefer explicit formulas, named ranges, queries, scripts, or notebooks that can be rerun over one-off conversational calculations whose method is not preserved.

## Source Data and Schema Integrity

- Preserve an immutable/raw copy of each source export before cleaning or transforming it.
- Record where the data came from, export date/time, covered period, timezone, locale, currency/unit conventions, and any filters already applied when those facts can change interpretation.
- Inspect column meanings and types before analysis. A column that looks numeric may contain IDs, percentages, currency, durations, timestamps, encoded categories, or mixed units.
- Treat missing, zero, blank, `null`, `N/A`, suppressed, and not-recorded values as potentially different states rather than normalizing them automatically.
- Verify duplicate semantics before deduplication. Repeated rows can be errors, legitimate repeated events, periodic snapshots, split transactions, retries, or versioned records.
- When joining datasets, state the join key/cardinality and inspect unmatched and duplicated matches. Do not silently join on display names, rounded timestamps, or other unstable keys when a stable identifier exists.
- Preserve source row identifiers or another reversible mapping when transformations materially change the dataset so suspicious outputs can be traced back to originals.

## Dates, Time, Units, and Currency

- Normalize date/time formats explicitly and retain timezone information when event ordering, daily totals, sleep/activity windows, travel, billing periods, or daylight-saving changes matter.
- Do not silently interpret ambiguous dates such as `03/04/2026`; establish locale or parse rules first.
- Normalize units only with an explicit conversion and preserve the original value/unit where errors would matter.
- For financial data, preserve transaction currency and distinguish original amount, converted amount, exchange rate/source, and conversion date when multiple currencies occur.
- Keep gross/net, debit/credit, balance/flow, planned/actual, and similar accounting semantics explicit instead of relying on column-name intuition.

## Deterministic Calculation Boundary

- Require deterministic code/formulas for totals, percentages, rates, balances, date arithmetic, unit conversion, statistical metrics, and other calculations whose correctness matters.
- Treat the LLM as the author/reviewer of the calculation, not the arithmetic oracle. The accepted result should be reproducible by rerunning the formula, query, or code against the same input.
- For a material result, preserve the exact formula/code and the rows/columns used. Ask the assistant to explain the method in plain language so the user can detect a wrong denominator, filter, grouping, or time window.
- Cross-check a few manually computable examples or an independent calculation path before trusting a large batch result.
- For statistical analysis, state sample/population choice, missing-value treatment, weighting, confidence assumptions, multiple comparisons, and other choices that materially affect interpretation.
- Correlation, clustering, anomaly detection, or forecast output does not establish causation. Keep model-generated explanations separate from patterns actually supported by the dataset.

## Data Cleaning and Transformation

- Make cleaning steps explicit and ordered. Typical operations include parsing, trimming, normalization, type conversion, missing-value handling, duplicate review, category mapping, unit conversion, filtering, joins, and derived fields.
- Produce a short transformation log or executable script for recurring analysis instead of manually repeating hidden conversational edits.
- Do not overwrite raw values merely to make an analysis convenient; create derived/normalized columns or a cleaned copy when provenance matters.
- Inspect before/after row counts, null counts, key uniqueness, range/distribution checks, and unmatched records after material transformations.
- If the input is an image, scanned PDF, screenshot, or visually complex document, treat extraction as a separate uncertain step. Current ChatGPT documentation warns that exact values from image-based tables or complex visual layouts may be unreliable; prefer the original spreadsheet/text export when accuracy matters.

## Visualization and Reporting

- Choose the visualization from the question and data shape rather than aesthetics: time series, category comparison, distribution, scatter/relationship, cumulative flow, or composition each require different chart semantics.
- Verify axes, units, scales, aggregation level, sorting, labels, missing intervals, and denominator before accepting a chart.
- Avoid truncated axes, incompatible dual axes, excessive smoothing, or category aggregation that materially changes the visual conclusion without disclosure.
- Pair important charts with the underlying metric definition and a small table or reproducible query when practical.
- Separate observed values from forecasts/estimates visually and textually.
- Keep generated narrative summaries traceable to the actual analysis output. A plausible story about a chart is not additional evidence.

## Personal Finance Data

- Personal finance is a common workload, but keep analysis separate from financial advice or transaction authority.
- Useful low-risk analysis can include categorization, cash-flow summaries, recurring-subscription detection, budget variance, historical spending trends, fee/interest inspection, and scenario calculation from user-supplied assumptions.
- Reconcile important totals against bank/card/export summaries before treating the analysis as authoritative; imports can omit pending transactions, duplicate entries, reverse charges, or use inconsistent signs/categories.
- Do not infer tax treatment, credit/legal status, investment suitability, or guaranteed future returns from transaction history. Use current authoritative rules and qualified advice where consequences are material.
- Do not grant an analysis agent permission to transfer funds, trade, pay bills, or change account settings merely because it can inspect the data.

## Fitness, Health, and Activity Data

- Wearable/fitness exports can support descriptive personal analysis such as activity trends, sleep-duration summaries, training volume, routine consistency, and correlations between self-recorded variables.
- Treat sensor measurements and consumer-device classifications as measurements with device/method limitations, not clinical diagnoses.
- Do not convert correlations or anomalies into diagnoses, treatment, medication, or emergency conclusions. For concerning symptoms/measurements, use the relevant clinician/device guidance and authoritative medical sources.
- Preserve device/source identity, sampling frequency, units, timezone, gaps, firmware/device changes, and manual corrections when comparing periods.

## Smart-Home, Utility, and Sensor Data

- For household telemetry, separate sensor events, derived states, automation logs, energy readings, and manually entered data before aggregation.
- Account for device resets, offline periods, clock drift, calibration changes, missing telemetry, and sampling-rate changes before declaring a trend or anomaly.
- Use analysis to identify patterns or candidate automation improvements, but require explicit review before converting statistical findings into side-effecting control rules for locks, alarms, heating, power, appliances, or other safety-relevant systems.

## Privacy and Data Minimization

- Personal datasets can expose finances, health/activity, precise location, routines, home occupancy, purchases, contacts, identifiers, and other sensitive information even when no single column looks highly sensitive.
- Before using a hosted assistant, determine whether the full dataset is necessary. Remove unrelated columns/rows, replace direct identifiers, aggregate locally, or sample representative data when that preserves the analysis objective.
- Treat connected-source authorization as real data access. Review account scopes, workspace/admin controls, retention/model-improvement settings, and revocation behavior for the chosen service.
- Do not upload passwords, private keys, recovery codes, full payment credentials, authentication tokens, or other secrets embedded in exports/logs.
- When sharing an analysis result, inspect charts, row samples, filenames, metadata, notebook output, and generated workbooks for accidental disclosure of raw personal data.

## Local and Hybrid Route

- Use a local route when sensitive data, offline operation, reproducibility, large repeat workloads, or provider independence justify setup cost and the exact hardware/runtime is verified.
- Prefer a **local deterministic analysis stack**—for example Python/pandas, DuckDB/SQLite, a notebook, or spreadsheet engine—as the computation source of truth. Add a local LLM for query translation, code generation, explanation, schema exploration, or iterative assistance rather than replacing the computation engine.
- `Phi-4 Mini Instruct` is a compact current local text/code-assistance candidate for constrained hardware; `Qwen3 8B` is a broader local reasoning/code candidate where measured memory and latency allow it. Validate the exact code-generation, schema-understanding, and language workload rather than assuming model-card capability proves analytical correctness.
- A hybrid route can keep raw/sensitive data and execution local while sending only sanitized schema, aggregates, error messages, or public-domain questions to a stronger hosted assistant.
- Do not infer local fit from parameter count, quantized artifact size, or successful model loading. Route exact model/runtime/device feasibility to the sibling hardware journey.

## Reproducibility and Auditability

- For any analysis the user may revisit, preserve: source file/version, transformation script/formulas, environment/tool version when material, parameters/filters, resulting dataset or summary, and analysis date.
- Prefer notebooks/scripts/formulas that rerun from raw input to result over a chain of manual conversational edits.
- If the assistant changes code after an error, re-run the full relevant pipeline rather than trusting outputs computed from stale notebook state.
- Check that the displayed result corresponds to the final code/data state, especially in stateful notebook environments.
- Record uncertainty or unresolved data-quality issues explicitly instead of silently filling them with model assumptions.

## Cost and Accepted Analysis Outcome

- Compare routes by **cost per accepted analysis outcome**: subscription/API cost, spreadsheet/plugin limits, upload/transfer overhead, local compute/storage, cleaning effort, code review, reruns, verification time, and the cost of a wrong conclusion.
- A managed code-backed assistant can be the lowest-total-cost route for occasional datasets because it removes environment setup while preserving inspectable computation.
- Spreadsheet-native assistance can be lower friction for workbook-heavy users because formulas/source cells remain visible, but it is not automatically more accurate than a notebook route.
- Local execution can be economically attractive for repeated/private datasets when the user already owns suitable hardware and can maintain the environment; include administration and validation effort rather than treating token cost as the whole comparison.
- Use a larger or second model only when it measurably reduces accepted-result correction/review cost for the user's real analyses.

## Escalation Triggers

- Move from `everyday-home-user/` to this scenario when structured analysis becomes recurring and reproducibility matters.
- Move from conversational analysis to code/formula-backed execution when calculations, transformations, or row counts exceed what can be reliably inspected manually.
- Move to spreadsheet-native assistance when the workbook itself is the authoritative artifact and preserving its formulas/references is the dominant need.
- Move to a notebook/SQL/local deterministic stack when data volume, repeatability, privacy, custom logic, or debugging exceeds the managed assistant's practical limits.
- Move toward `personal-knowledge-base-user/` when retrieval/synthesis over documents becomes the dominant problem rather than structured computation.
- Move to a professional/team/organization data-analysis route when datasets become employer/client/shared assets, governed metrics, regulated records, production systems, or multi-user decision infrastructure.
- Escalate to qualified financial/medical/legal or other domain review when the analysis is being used for a high-consequence decision rather than personal exploration.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when the user chooses local model assistance and exact owned hardware materially constrains model/runtime fit.
- Use `../../../hardware/sub/computers/` for ordinary personal desktop/laptop analysis and the applicable accelerator specialization when known.
- The deterministic Python/SQL/spreadsheet workload may be practical even when a useful local LLM is not; do not make local model inference a prerequisite for private local data analysis.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link managed assistant examples to `catalog/services/assistant-workspaces/chatgpt` and `catalog/services/assistant-workspaces/gemini` when named.
- Link local candidates to `catalog/models/microsoft/phi/phi-4/models/phi-4-mini-instruct` and `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link sibling scenario/hardware owners instead of duplicating complete product, model, runtime, or device-fit profiles.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI ChatGPT data-analysis and spreadsheet documentation, current Google Gemini Apps/Sheets file and analysis documentation, and canonical AI Lab model/service owners.
- Current OpenAI evidence establishes spreadsheet/CSV and other file analysis, Python/Jupyter-backed calculations and transformations for applicable tasks, chart/table output, and explicit review of generated code/data/assumptions. Current Google evidence establishes spreadsheet upload/analysis plus Gemini in Sheets formula, analysis, chart, and supported action workflows.
- Spreadsheet assistants, file limits, supported formats, connected-source behavior, analysis environments, plan eligibility, pricing/usage limits, model aliases, and privacy/retention settings are mutable; recheck them before rendering current advice.
- Provider capability claims establish tool availability, not independent correctness. Accepted results require dataset-specific validation and reproducible computation.

## Validation

- The scenario remains personal structured-data analysis and does not become professional/enterprise analytics architecture.
- Raw source data is preserved before transformations.
- Schema, missingness, duplicates, joins, dates/timezones, units, and currencies are explicit analytical concerns rather than hidden assumptions.
- Important arithmetic/statistics use deterministic formulas or executable code rather than prose-only model reasoning.
- Generated code, intermediate data, assumptions, and material spreadsheet edits are reviewable before acceptance.
- Visualizations are checked against underlying data, units, aggregation, and axis semantics.
- Personal finance, health/fitness, and smart-home analysis preserve their high-consequence boundaries and do not grant transactional/control authority.
- Hosted routes minimize sensitive data; local routes keep deterministic computation as the source of truth and do not equate `local` with automatic correctness/security.
- Reproducibility is preserved for analyses likely to be revisited.
- Exact local model identities are canonical and hardware fit is delegated to the sibling hardware journey.
- Mutable current claims carry the 2026-08-24 evidence boundary.
