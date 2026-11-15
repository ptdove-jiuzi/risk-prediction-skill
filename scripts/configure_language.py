#!/usr/bin/env python3
"""Select and persist the Skill output language during installation."""

import argparse
import json
from pathlib import Path

LANGUAGES = {"en": "English", "zh-CN": "简体中文"}


def main():
    parser = argparse.ArgumentParser(description="Select the Risk Prediction Skill output language")
    parser.add_argument("language", nargs="?", choices=sorted(LANGUAGES), help="en or zh-CN; omit for an interactive choice")
    args = parser.parse_args()
    language = args.language
    if language is None:
        print("Choose output language / 选择输出语言:")
        print("  1. English")
        print("  2. 简体中文")
        while language is None:
            choice = input("Enter 1 or 2 / 输入 1 或 2: ").strip().lower()
            if choice in {"1", "en", "english"}:
                language = "en"
            elif choice in {"2", "zh", "zh-cn", "中文", "简体中文"}:
                language = "zh-CN"
            else:
                print("Invalid choice / 无效选择")
    config = Path(__file__).resolve().parents[1] / "language.json"
    config.write_text(json.dumps({"language": language}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if language == "en":
        print(f"Language saved: English ({config})")
    else:
        print(f"语言已保存：简体中文（{config}）")


if __name__ == "__main__":
    main()
