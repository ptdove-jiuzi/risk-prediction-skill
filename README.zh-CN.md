# 风险预测skill

**英文名：risk-prediction-skill · 开发者：PT-dove**

[Switch to English](README.md)

用于探索正向与负向可能性的多语言情景生成 Skill。普通表格与手机端离线网页共用分类，并提供概率筛选功能。

## 快速下载

- **[下载 v1.0.0 ZIP](https://github.com/ptdove-jiuzi/risk-prediction-skill/archive/refs/tags/v1.0.0.zip)** —— 推荐
- [下载最新源码 ZIP](https://github.com/ptdove-jiuzi/risk-prediction-skill/archive/refs/heads/main.zip)
- [查看 SKILL.md](SKILL.md)

## 安装与语言选择

1. 下载并解压 ZIP。
2. 在解压后的目录运行：

   ```bash
   python scripts/configure_language.py
   ```

3. 选择 **English** 或 **简体中文**。选择会保存到 `language.json`，并应用于后续表格、网页、分类、控件和回答。

也可以直接指定语言：

```bash
python scripts/configure_language.py en
python scripts/configure_language.py zh-CN
```

## GitHub 页面布局

- **顶部语言切换**：一键返回英文说明。
- **快速下载区**：固定版本和最新源码下载链接放在功能介绍之前。
- **安装说明**：提供交互选择和直接指定两种语言设置方式。
- **项目文件**：Skill 入口位于仓库根目录，脚本、参考资料和网页模板按用途分类。

## 已包含

- 安装时选择英文或中文。
- 表格与网页共用`正向·小分类`、`负向·小分类`及对应英文分类。
- 正向事件按概率从高到低，负向事件按概率从低到高。
- 100–500 条详细网页情景，支持非零极小概率。
- 下拉列表与双滑块概率选择器。
- 电脑表格与 820px 以下手机事件卡片。
- 无外部依赖的离线单文件网页。
- 紧凑 JSON 与统一模板，减少重复生成和 Token 消耗。

## 免责声明

本项目及其所有生成内容仅供娱乐，不构成任何专业意见、决策依据或行动建议。内容由 AI 基于假设生成，可能存在错误、遗漏或偏差，使用者须自行核实、独立判断，并自行承担使用、参考、依赖或传播本项目及生成内容所造成的一切直接或间接后果。**开发者 PT-dove 不承担任何法律、经济或其他责任。**
