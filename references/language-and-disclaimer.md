# Language Selection and Disclaimer

## Installation language

Support `en` and `zh-CN`. Read `language.json` from the Skill root before responding.

1. If the file exists, use its `language` value for every user-facing part of the output.
2. If it does not exist, ask once: `Choose output language / 选择输出语言：English / 简体中文`.
3. Save the choice with `python scripts/configure_language.py <en|zh-CN>` when file execution is available. Otherwise retain the choice for the current session and explain how to save it later.
4. Do not ask again on every query. Change the saved language only when the user requests it.
5. Use the selected language for scenario text, category names, table headers, probability controls, buttons, empty states, mobile cards, and final responses. Do not mix languages unless the user requests bilingual output.

The compact web JSON must include `"language":"en"` or `"language":"zh-CN"`. Use `Positive·Subject` and `Negative·Subject` for English data, or `正向·小分类` and `负向·小分类` for Chinese data. The same scenario and subcategory must retain the same meaning across both languages and both output modes.

## Central disclaimer

Show this disclaimer prominently in every Markdown table response and every generated HTML page. Do not replace it with the previous AI-content notice.

Chinese, exact text:

> 本项目及其所有生成内容仅供娱乐，不构成任何专业意见、决策依据或行动建议。内容由 AI 基于假设生成，可能存在错误、遗漏或偏差，使用者须自行核实、独立判断，并自行承担使用、参考、依赖或传播本项目及生成内容所造成的一切直接或间接后果。开发者 PT-dove 不承担任何法律、经济或其他责任。

English:

> This project and all generated content are for entertainment only and do not constitute professional advice, a basis for decision-making, or recommendations for action. AI-generated content may contain errors, omissions, or bias. Users must independently verify all information and accept sole responsibility for every direct or indirect consequence of using, relying on, or distributing this project or its content. PT-dove accepts no legal, financial, or other liability.

For Markdown, place the disclaimer immediately after the assumptions line and before the table. For HTML, center it prominently above the filters and repeat it in the footer. Keep the disclaimer in the selected language. Risk estimates remain uncertain regardless of the disclaimer; do not use the disclaimer to justify fabricated facts or unsafe advice.

## Identity boundary

The only permitted developer attribution is `PT-dove`. Do not include any other developer, company, assistant, connector, or development-process attribution in the project, package, generated pages, repository description, or release notes.
