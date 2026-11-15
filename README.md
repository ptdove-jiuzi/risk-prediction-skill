# Risk Prediction Skill

**中文名：风险预测skill · Developer: PT-dove**

[简体中文说明](README.zh-CN.md)

A multilingual scenario-generation Skill for exploring positive and negative possibilities. It provides matching Markdown tables and mobile-ready offline HTML reports with probability filters.

## Download

- **[Download v1.0.0 ZIP](https://github.com/ptdove-jiuzi/risk-prediction-skill/archive/refs/tags/v1.0.0.zip)** — recommended
- [Download latest source ZIP](https://github.com/ptdove-jiuzi/risk-prediction-skill/archive/refs/heads/main.zip)
- [Open SKILL.md](SKILL.md)

## Install and choose a language

1. Download and extract the ZIP.
2. Run the language selector from the extracted directory:

   ```bash
   python scripts/configure_language.py
   ```

3. Choose **English** or **简体中文**. The choice is saved in `language.json` and reused for tables, webpages, categories, controls, and responses.

To set a language without an interactive prompt:

```bash
python scripts/configure_language.py en
python scripts/configure_language.py zh-CN
```

## Repository interface

- **Top navigation:** switch to the Chinese guide with one click.
- **Download section:** stable-version and latest-source ZIP links appear before the feature details.
- **Quick setup:** two commands cover interactive and direct language selection.
- **Project files:** the Skill entry point is at the repository root; reusable scripts, references, and the HTML template are grouped by purpose.

## Included

- Installation-time language selection: English or Chinese.
- One shared `Positive·Subject` / `Negative·Subject` and `正向·小分类` / `负向·小分类` taxonomy across tables and webpages.
- Positive scenarios sorted from high to low probability, followed by negative scenarios from low to high.
- Detailed HTML reports with 100–500 scenarios, including clearly marked extremely small probabilities.
- Dropdown and dual-slider probability selectors.
- Desktop tables and dedicated mobile event cards at widths of 820px or less.
- Offline single-file output with no external web dependencies.
- Compact JSON and one reusable template to reduce repeated generation and token usage.

## Project structure

```text
risk-prediction-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── assets/
│   └── probability-page-template.html
├── references/
│   ├── category-taxonomy.md
│   ├── language-and-disclaimer.md
│   ├── output-contract.md
│   ├── probability-guide.md
│   ├── risk-taxonomy.md
│   ├── safety-and-evidence.md
│   ├── token-efficiency.md
│   └── web-mode.md
└── scripts/
    ├── build_probability_page.py
    └── configure_language.py
```

## Disclaimer

This project and all generated content are for entertainment only and do not constitute professional advice, a basis for decision-making, or recommendations for action. AI-generated content may contain errors, omissions, or bias. Users must independently verify all information and accept sole responsibility for every direct or indirect consequence of using, relying on, or distributing this project or its content. **PT-dove accepts no legal, financial, or other liability.**
