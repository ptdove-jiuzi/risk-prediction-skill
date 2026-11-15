#!/usr/bin/env python3
"""Validate compact scenario data and build a localized offline probability page."""

import argparse
import json
import math
from pathlib import Path

LANGUAGE_DIRECTIONS = {"zh-CN": ("正向", "负向"), "en": ("Positive", "Negative")}
IMPACTS = {"低", "中", "高", "极高", "Low", "Medium", "High", "Critical"}
CONFIDENCE = {"高", "中", "低", "High", "Medium", "Low"}
MIN_ITEMS = 100
MAX_ITEMS = 500
MIN_NEGATIVE_MULTIPLIER = 1.20
MAX_NEGATIVE_MULTIPLIER = 1.35

EN_REPLACEMENTS = [
    ("本次 AI 预测的可能性、概率、影响、依据和应对", "AI-predicted scenarios, probabilities, impacts, triggers, and actions for this event"),
    ("aria-label=\"本次 AI 预测的可能性总数\"", "aria-label=\"AI-predicted scenario total\""),
    ("<span class=\"total-kicker\">本次 AI 预测</span>", "<span class=\"total-kicker\">AI predicted</span>"),
    ("正向 0 · 负向 0", "Positive 0 · Negative 0"),
    ("lang=\"zh-CN\"", "lang=\"en\""),
    ("事件可能性与概率情景分析", "Scenario and probability analysis for an event"),
    ("本项目及其所有生成内容仅供娱乐，不构成任何专业意见、决策依据或行动建议。内容由 AI 基于假设生成，可能存在错误、遗漏或偏差，使用者须自行核实、独立判断，并自行承担使用、参考、依赖或传播本项目及生成内容所造成的一切直接或间接后果。开发者 PT-dove 不承担任何法律、经济或其他责任。", "This project and all generated content are for entertainment only and do not constitute professional advice, a basis for decision-making, or recommendations for action. AI-generated content may contain errors, omissions, or bias. Users must independently verify all information and accept sole responsibility for every direct or indirect consequence of using, relying on, or distributing this project or its content. PT-dove accepts no legal, financial, or other liability."),
    ("这次事件的概率", "Probability of This Event"),
    ("AI scenario index / AI 预测情景索引", "AI-predicted scenario index"),
    ("跳到可能性列表", "Skip to scenario list"),
    ("可能性总数", "Total scenarios"),
    ("概率选择方式", "Probability selector mode"),
    ("概率选择器", "Probability"),
    ("列表选择", "List"),
    ("滑块选择", "Slider"),
    ("最低概率", "Minimum probability"),
    ("最高概率", "Maximum probability"),
    ("事件方向", "Direction"),
    ("全部概率", "All probabilities"),
    ("全部事件", "All events"),
    ("仅正向事件", "Positive only"),
    ("仅负向事件", "Negative only"),
    ("仅法律事件", "Legal only"),
    ("仅极端事件", "Extreme only"),
    ("搜索细分选项", "Search scenarios"),
    ("输入事件、条件或应对", "Search event, condition, or action"),
    ("重置筛选", "Reset filters"),
    ("筛选可能性", "Filter scenarios"),
    ("事件概率表", "Scenario probability table"),
    ("正向：概率由高到低 ↓　｜　负向：概率由低到高 ↑　｜　各情景可共存，概率不相加", "Positive: high to low ↓ | Negative: low to high ↑ | Scenarios may coexist; probabilities are not additive"),
    ("序号", "No."), ("分类", "Category"), ("可能事件", "Scenario"), ("影响", "Impact"),
    ("依据／触发条件", "Evidence / trigger"), ("预防／应对", "Prevention / action"), ("概率条", "Probability bar"),
    ("没有符合这些条件的情景", "No scenarios match these filters"),
    ("试试更宽的概率范围，或清空搜索词。", "Try a wider probability range or clear the search."),
    ("查看全部可能性", "Show all scenarios"),
    ("概率为基于假设的粗粒度情景估计，并非现实统计或确定预言。", "Probabilities are coarse scenario estimates based on assumptions, not real-world statistics or certain predictions."),
    ("事件：${data.event}", "Event: ${data.event}"),
    ("估计条件：${data.assumptions}", "Assumptions: ${data.assumptions}"),
    ("按概率范围", "By probability range"),
    ("按具体概率", "By exact probability"),
    ("恰好 ", "Exactly "),
    ("把握 ${item.confidence}", "Confidence ${item.confidence}"),
    ("估计概率约 ${percent(item.probability)}", "Estimated probability ${percent(item.probability)}"),
    ("`正向 ${positiveCount} · 负向 ${negativeCount}`", "`Positive ${positiveCount} · Negative ${negativeCount}`"),
    ("`本次 AI 预测 ${items.length} 种可能性，正向 ${positiveCount}，负向 ${negativeCount}`", "`AI predicted ${items.length} scenarios: ${positiveCount} positive and ${negativeCount} negative`"),
    ("当前显示 <strong>${filtered.length}</strong> 条／本次 AI 共预测 <strong>${items.length}</strong> 种可能性", "Showing <strong>${filtered.length}</strong> of <strong>${items.length}</strong> AI-predicted scenarios"),
    ("种可能性", "scenarios"),
]


def validate_category(category, index, language):
    if not isinstance(category, str) or category.count("·") != 1:
        raise ValueError(f"Item {index}: category must be '<direction>·<single subject>'")
    direction, subcategory = category.split("·")
    if direction not in LANGUAGE_DIRECTIONS[language] or not subcategory.strip():
        raise ValueError(f"Item {index}: invalid direction or subcategory for {language}: {category}")
    if "/" in subcategory or "／" in subcategory or "\\" in subcategory:
        raise ValueError(f"Item {index}: use one subject without slashes: {category}")


def load_and_validate(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Unable to read JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    language = data.get("language", "zh-CN")
    if language not in LANGUAGE_DIRECTIONS:
        raise ValueError("language must be 'zh-CN' or 'en'")
    data["language"] = language
    for key in ("event", "assumptions"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"{key} must be a non-empty string")
    items = data.get("items")
    if not isinstance(items, list) or not MIN_ITEMS <= len(items) <= MAX_ITEMS:
        raise ValueError(f"items must contain {MIN_ITEMS}–{MAX_ITEMS} scenarios")

    seen = set()
    normalized = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, list) or len(item) != 7:
            raise ValueError(f"Item {index} must be a seven-field array")
        category, event, probability, impact, trigger, advice, confidence = item
        validate_category(category, index, language)
        if impact not in IMPACTS:
            raise ValueError(f"Item {index}: invalid impact: {impact}")
        if confidence not in CONFIDENCE:
            raise ValueError(f"Item {index}: invalid confidence: {confidence}")
        if isinstance(probability, bool) or not isinstance(probability, (int, float)):
            raise ValueError(f"Item {index}: probability must be numeric")
        if not math.isfinite(probability) or not 0 < probability < 100:
            raise ValueError(f"Item {index}: probability must be between 0 and 100")
        for field_name, value in (("event", event), ("trigger", trigger), ("advice", advice)):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Item {index}: {field_name} must be a non-empty string")
        fingerprint = event.strip().casefold()
        if fingerprint in seen:
            raise ValueError(f"Item {index}: duplicate event: {event}")
        seen.add(fingerprint)
        normalized.append([category, event.strip(), probability, impact, trigger.strip(), advice.strip(), confidence])

    positive_prefix, negative_prefix = (prefix + "·" for prefix in LANGUAGE_DIRECTIONS[language])
    positive = sorted((x for x in normalized if x[0].startswith(positive_prefix)), key=lambda x: -x[2])
    negative = sorted((x for x in normalized if x[0].startswith(negative_prefix)), key=lambda x: x[2])
    if not positive or not negative:
        raise ValueError("At least one positive and one negative scenario are required")
    minimum_negative = math.ceil(len(positive) * MIN_NEGATIVE_MULTIPLIER)
    maximum_negative = math.floor(len(positive) * MAX_NEGATIVE_MULTIPLIER)
    if not minimum_negative <= len(negative) <= maximum_negative:
        raise ValueError(
            f"Negative scenario count must be 20%–35% higher than positive: "
            f"{len(positive)} positive requires {minimum_negative}–{maximum_negative} negative, got {len(negative)}"
        )
    data["items"] = positive + negative
    return data


def main():
    parser = argparse.ArgumentParser(description="Build a localized offline probability HTML page")
    parser.add_argument("input", type=Path, help="Compact JSON data file")
    parser.add_argument("output", type=Path, nargs="?", help="Output HTML file")
    parser.add_argument("--check-only", action="store_true", help="Validate data without generating HTML")
    parser.add_argument("--template", type=Path, help="Optional custom template path")
    args = parser.parse_args()
    if not args.check_only and args.output is None:
        parser.error("an output path is required when generating HTML")

    try:
        data = load_and_validate(args.input)
        positive_prefix = LANGUAGE_DIRECTIONS[data["language"]][0] + "·"
        positive_count = sum(item[0].startswith(positive_prefix) for item in data["items"])
        negative_count = len(data["items"]) - positive_count
        premium = (negative_count / positive_count - 1) * 100
        summary = f"Validated: {len(data['items'])} scenarios (positive {positive_count}, negative {negative_count}, negative premium {premium:.1f}%, language {data['language']})"
        if args.check_only:
            print(summary)
            return

        template_path = args.template or Path(__file__).resolve().parents[1] / "assets" / "probability-page-template.html"
        template = template_path.read_text(encoding="utf-8")
        if template.count("__PROBABILITY_DATA__") != 1:
            raise ValueError("Template must contain exactly one __PROBABILITY_DATA__ placeholder")
        if data["language"] == "en":
            for source, translated in EN_REPLACEMENTS:
                template = template.replace(source, translated)
        payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        payload = payload.replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
        payload = payload.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
        html = template.replace("__PROBABILITY_DATA__", payload)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(html, encoding="utf-8")
        print(f"{summary}\nCreated: {args.output.resolve()}")
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
