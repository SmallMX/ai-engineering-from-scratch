#!/usr/bin/env python3
"""Check Chinese translation coverage for lesson docs, quizzes, and outputs.

Usage:
    python3 scripts/audit_translations.py [--phase N] [--limit N] [--json]

Exit codes:
    0 - all expected Chinese translation files are present
    1 - translation gaps were found
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
PHASES_DIR = ROOT / "phases"


@dataclass
class Gap:
    kind: str
    source: str
    expected: str

    def to_dict(self) -> dict[str, str]:
        return {
            "kind": self.kind,
            "source": self.source,
            "expected": self.expected,
        }


@dataclass
class Report:
    lessons_checked: int = 0
    docs_present: int = 0
    quizzes_present: int = 0
    outputs_present: int = 0
    gaps: list[Gap] = field(default_factory=list)

    def add_gap(self, kind: str, source: Path, expected: Path) -> None:
        self.gaps.append(
            Gap(
                kind=kind,
                source=source.relative_to(ROOT).as_posix(),
                expected=expected.relative_to(ROOT).as_posix(),
            )
        )


def iter_lesson_dirs(phase_filter: int | None) -> Iterable[Path]:
    for phase in sorted(PHASES_DIR.iterdir()):
        if not phase.is_dir():
            continue
        if phase_filter is not None:
            try:
                phase_num = int(phase.name.split("-", 1)[0])
            except ValueError:
                continue
            if phase_num != phase_filter:
                continue
        for lesson in sorted(phase.iterdir()):
            if lesson.is_dir():
                yield lesson


def translated_output_path(path: Path) -> Path:
    return path.with_name(f"{path.stem}.zh-CN{path.suffix}")


def audit_lesson(report: Report, lesson: Path) -> None:
    report.lessons_checked += 1

    doc = lesson / "docs" / "en.md"
    if doc.is_file():
        translated = lesson / "docs" / "zh-CN.md"
        if translated.is_file():
            report.docs_present += 1
        else:
            report.add_gap("docs", doc, translated)

    quiz = lesson / "quiz.json"
    if quiz.is_file():
        translated = lesson / "quiz.zh-CN.json"
        if translated.is_file():
            report.quizzes_present += 1
        else:
            report.add_gap("quiz", quiz, translated)

    outputs = lesson / "outputs"
    if outputs.is_dir():
        for source in sorted(outputs.glob("*.md")):
            if source.name.endswith(".zh-CN.md"):
                continue
            translated = translated_output_path(source)
            if translated.is_file():
                report.outputs_present += 1
            else:
                report.add_gap("output", source, translated)


def render_report(report: Report, limit: int) -> str:
    lines = [
        (
            "audit_translations.py - "
            f"{report.lessons_checked} lesson(s) checked, "
            f"{len(report.gaps)} translation gap(s)"
        ),
        "",
        "Present translations:",
        f"  docs/zh-CN.md: {report.docs_present}",
        f"  quiz.zh-CN.json: {report.quizzes_present}",
        f"  outputs/*.zh-CN.md: {report.outputs_present}",
    ]
    if report.gaps:
        visible_gaps = report.gaps if limit == 0 else report.gaps[:limit]
        lines.append("")
        lines.append(f"Missing translations shown: {len(visible_gaps)} of {len(report.gaps)}")
        for gap in visible_gaps:
            lines.append(f"  [{gap.kind}] {gap.expected} (source: {gap.source})")
        if limit != 0 and len(report.gaps) > limit:
            lines.append("")
            lines.append("Use --limit 0 to show every gap.")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", type=int, default=None, help="restrict to a single phase")
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="maximum gaps to print in text mode; use 0 for all gaps",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON report")
    args = parser.parse_args(argv)

    report = Report()
    for lesson in iter_lesson_dirs(args.phase):
        audit_lesson(report, lesson)

    if args.json:
        json.dump(
            {
                "lessons_checked": report.lessons_checked,
                "docs_present": report.docs_present,
                "quizzes_present": report.quizzes_present,
                "outputs_present": report.outputs_present,
                "gaps": [gap.to_dict() for gap in report.gaps],
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_report(report, args.limit) + "\n")

    return 1 if report.gaps else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
