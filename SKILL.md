---
name: risk-prediction-skill
description: This skill should be used when the user describes an intended action, plan, event, project, journey, purchase, investment, publication, conversation, or other situation and asks to predict risks, foresee what might happen, identify positive or negative outcomes, uncover hidden dangers, assess legal exposure, or make a contingency plan. It produces a scenario table covering opportunities as well as ordinary, serious, and catastrophic negative events, with calibrated probability estimates, impacts, triggers, and practical mitigations. When the user requests detailed sub-options, an expanded possibility list, a web version, or an interactive probability page, it generates a self-contained HTML page titled “这次事件的概率” with 100 or more scenarios, list and slider percentage filters, and probability bars. It supports Chinese prompts such as “预判未来”“预知风险”“细分选项”“我做……可能遇到什么”“这件事有什么法律风险” and “帮我列一下好运和坏结果”. Before the first substantive analysis, it asks once for city, Agent application, optional real-time time/system access, and optional age, height, weight, and relevant health context, with a clear promise that the information stays in the current conversation and is not uploaded.
agent_created: true
---

# Risk Prediction Skill / 风险预测skill

## Purpose

Analyze plausible future scenarios rather than claim supernatural foresight. Balance beneficial opportunities with dangerous events, and convert vague worry into actionable prevention and contingency steps. State assumptions, distinguish evidence from speculation, and never present an estimate as a certainty.

## Language and Central Disclaimer

Read `references/language-and-disclaimer.md` before the first response and before generating HTML. Honor the language selected during installation and stored in `language.json`; if no selection exists, ask once and save `en` or `zh-CN`. Use that language for every table, webpage, category, control, and response instead of defaulting to Chinese.

Display the selected-language central disclaimer in every response: Chinese `本项目及其所有生成内容仅供娱乐，不构成任何专业意见、决策依据或行动建议。内容由 AI 基于假设生成，可能存在错误、遗漏或偏差，使用者须自行核实、独立判断，并自行承担使用、参考、依赖或传播本项目及生成内容所造成的一切直接或间接后果。开发者 PT-dove 不承担任何法律、经济或其他责任。`; English `This project and all generated content are for entertainment only and do not constitute professional advice, a basis for decision-making, or recommendations for action. AI-generated content may contain errors, omissions, or bias. Users must independently verify all information and accept sole responsibility for every direct or indirect consequence of using, relying on, or distributing this project or its content. PT-dove accepts no legal, financial, or other liability.` Keep the only permitted developer attribution as `PT-dove`, with no other developer or development-process information.

## First-use Context and Privacy

Read `references/user-context-onboarding.md` and ask for user context once before the first substantive analysis. Start with a clear notice in the selected language: the information is used only for the current conversation, is not uploaded to GitHub, written into the Skill, sent to third parties, or used for analytics; city-level location is sufficient, and optional items may be skipped.

Ask in one compact message for city, Agent application and version, permission or values for real-time date/time/timezone and basic system environment, plus optional age, height, weight, and activity-relevant health factors. Tailor what can be read automatically to the named Agent; if a capability is unavailable, ask the user instead of guessing. Never request a detailed address, credentials, ID numbers, or unrelated medical history.

Keep the profile transient. Do not write it to repository files, memory logs, language config, generated JSON/HTML metadata, URLs, examples, or commits. Use only the factors that materially change the analysis, avoid repeating sensitive details, and proceed with explicit assumptions if the user skips everything.

## Required Output

Return one Markdown table for each user-supplied event unless the user explicitly requests another format. Label every scenario as `正向·小分类` or `负向·小分类`, with one unambiguous subject after the direction. Put positive events at the top, sorted by probability from high to low. Continue with all negative events sorted by probability from low to high across ordinary inconveniences, serious harm, legal or other special risks, and rare catastrophic scenarios; use category labels without interrupting this probability ordering. Never combine distinct subjects with labels such as `法律/合规`. Read `references/category-taxonomy.md` and `references/output-contract.md` before producing the table and follow their exact grouping, ordering, columns, and fallback rules.

Use the exact same category vocabulary in Markdown tables and HTML pages. If the same scenario appears in both modes, its full category string must be identical. Do not use table-only or web-only aliases, legacy labels such as `幸运`, `不幸`, `安全`, `危险`, or compound labels such as `法律/合规`.

Do not output only dangers. Include plausible positive outcomes when they are genuinely relevant. Do not invent alarming events merely to fill every category; mark a category “未识别出有依据的显著场景” when necessary.

## Detailed Web Mode

Activate this mode instead of the short table when the user mentions detailed sub-options, asks for a much larger possibility list, or requests a web version or interactive probability page. Read `references/language-and-disclaimer.md`, `references/category-taxonomy.md`, `references/web-mode.md`, and `references/token-efficiency.md` before generating files.

Create an actual self-contained HTML file titled “这次事件的概率”. Include 100–200 distinct scenarios by default, but honor explicit expansion requests that require more. Use `正向·小分类` and `负向·小分类` labels, preserve the positive/descending then negative/ascending order, provide both list and slider percentage selectors, include extremely small nonzero probabilities when relevant, and place a purple percentage bar in the table's rightmost column. Include the exact notice “本项目及其所有生成内容仅供娱乐，不构成任何专业意见、决策依据或行动建议。内容由 AI 基于假设生成，可能存在错误、遗漏或偏差，使用者须自行核实、独立判断，并自行承担使用、参考、依赖或传播本项目及生成内容所造成的一切直接或间接后果。开发者 PT-dove 不承担任何法律、经济或其他责任。”. On screens 820px wide or narrower, switch from the desktop table to purpose-built vertical event cards with single-column controls, fluid typography, no horizontal scrolling, and touch targets at least 44px high; never merely shrink the desktop interface. Keep the page quiet and minimal: no autoplay, automatic navigation, unsolicited modal, or automatically opening tutorial.

Use `assets/probability-page-template.html` and `scripts/build_probability_page.py` rather than writing repeated HTML rows. Generate only the compact scenario data, run the builder, validate the result, and return the finished file without pasting the full HTML into chat.

## Workflow

### 0. Offer first-use context intake

After language selection and before the first substantive analysis, show the privacy notice and ask the compact context form from `references/user-context-onboarding.md`. Ask once per conversation. If the user declines or skips items, continue with explicit assumptions; do not block the task or ask again.

### 1. Parse the event

Extract the intended action, actor, place, time, duration, transport or tools, counterparties, assets at stake, jurisdiction, and constraints. Distinguish facts supplied by the user from assumptions. Ask at most three high-impact clarifying questions only when the missing answers would materially change the assessment; otherwise proceed with explicit, conservative assumptions.

### 2. Establish context

Identify immediate, delayed, direct, indirect, reversible, and irreversible consequences. Consider the full event chain: preparation, execution, interaction with other people or systems, completion, and aftermath.

Use current, location-specific information when available and material, such as weather, local regulations, platform rules, or known hazards. Cite the source and date when tools provide it. If current information is unavailable, state the limitation and use conditional scenarios instead of guessing facts.

### 3. Enumerate balanced scenarios

Read `references/risk-taxonomy.md` and scan every applicable domain. Include positive events, routine inconveniences, health and safety hazards, financial or property loss, legal exposure, platform rules, privacy and cybersecurity issues, social or reputational effects, operational delays, extremely low-probability severe events, and second-order consequences.

Generate scenarios from mechanisms, not stereotypes. Avoid attributing risk to nationality, ethnicity, religion, disability, gender, or other protected traits. Do not infer that a specific person will commit wrongdoing without concrete behavioral evidence.

### 4. Estimate and prioritize

Read `references/probability-guide.md`. Estimate the probability of each scenario within the event's stated time window, conditional on the assumptions. Use quantitative ranges only with a defensible basis; otherwise use ordered qualitative bands. Provide a separate confidence or evidence-strength indication.

Prioritize by probability for the required table ordering, but use impact and urgency in the advice so that a rare catastrophic risk is not ignored. Never hide a high-impact risk merely because its probability is low.

### 5. Add controls and contingencies

Give one concise preventive or opportunity-capturing action for each row when useful. Favor specific, proportionate, low-cost controls. For severe scenarios, include an early warning sign or an immediate response. Avoid generic advice that does not follow from the scenario mechanism.

### 6. Calibrate and verify

Read `references/safety-and-evidence.md` for high-stakes topics, legal language, uncertainty, and prohibited overclaiming. Before responding, verify that:

- The response contains exactly one table, plus at most a brief assumptions line and an optional concise priority note.
- Every category starts with `正向·` or `负向·`, followed by one subject without a slash.
- Positive rows appear first and are ordered from higher to lower probability.
- Negative rows follow and are ordered from lower to higher probability.
- Every probability has the same event window and assumptions.
- Speculation, missing context, and weak evidence are labeled.
- Legal conclusions are jurisdiction-aware and not presented as definitive legal advice.
- No row uses unsupported precision, deterministic prophecy, or gratuitously graphic detail.
- The advice addresses both common disruptions and low-probability high-impact outcomes.

## Default Response Shape

Start with one short assumptions line in the selected language, followed by the central disclaimer on its own line. Then provide the required table. End with at most one concise note naming the highest-priority mitigation or the missing fact that would most improve the assessment. Do not add a long essay before or after the table.

## Reference Map

- Use `references/language-and-disclaimer.md` for installation language selection, localization, central disclaimers, and attribution limits.
- Use `references/user-context-onboarding.md` for first-use questions, Agent capability handling, and transient profile privacy.
- Use `references/category-taxonomy.md` as the single shared category vocabulary for both Markdown tables and HTML pages.
- Use `references/output-contract.md` for table structure, sorting, probability display, and sparse-information behavior.
- Use `references/risk-taxonomy.md` for broad scenario coverage and second-order effects.
- Use `references/probability-guide.md` for calibrated estimates, evidence strength, and prioritization.
- Use `references/safety-and-evidence.md` for legal, medical, financial, security, privacy, and catastrophic-risk boundaries.
- Use `references/web-mode.md` for detailed HTML page triggers, data schema, generation, and acceptance checks.
- Use `references/token-efficiency.md` to minimize repeated markup, context usage, and unnecessary output.
- Use `assets/probability-page-template.html` as the reusable offline page template.
- Use `scripts/build_probability_page.py` to validate compact JSON data and build the final HTML file.
