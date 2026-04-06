#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIR = ROOT / "docs" / "chapters"
FULL_MD = ROOT / "docs" / "manuscript-full.md"
PDF_OUT = ROOT / "docs" / "manuscript.pdf"


def chapter_files() -> list[Path]:
    return sorted(CHAPTER_DIR.glob("*.md"))


def build_markdown(files: list[Path]) -> str:
    parts = [
        "# Ormleden: En Österlenthriller",
        "",
        "_Arbetsmanus genererat från `docs/chapters/`._",
        "",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        parts.append(text)
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def markdown_to_plain_text(markdown: str) -> list[str]:
    lines: list[str] = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            lines.append("")
            continue
        line = re.sub(r"^#+\s*", "", line)
        line = line.replace("**", "")
        line = line.replace("_", "")
        line = re.sub(r"`([^`]+)`", r"\1", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        lines.append(line)
    return lines


def wrap_line(text: str, font_name: str, font_size: int, max_width: float) -> list[str]:
    if not text:
        return [""]
    words = text.split()
    wrapped: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if stringWidth(candidate, font_name, font_size) <= max_width:
            current = candidate
        else:
            wrapped.append(current)
            current = word
    wrapped.append(current)
    return wrapped


def build_pdf(markdown: str) -> None:
    c = canvas.Canvas(str(PDF_OUT), pagesize=A4)
    width, height = A4
    margin_x = 22 * mm
    margin_y = 22 * mm
    max_width = width - 2 * margin_x
    y = height - margin_y

    def new_page() -> None:
        nonlocal y
        c.showPage()
        y = height - margin_y

    plain_lines = markdown_to_plain_text(markdown)
    for line in plain_lines:
        is_heading = bool(line) and len(line) < 80 and line == line.title()
        font_name = "Helvetica-Bold" if is_heading else "Times-Roman"
        font_size = 15 if is_heading else 11
        leading = 18 if is_heading else 14

        for chunk in wrap_line(line, font_name, font_size, max_width):
            if y < margin_y + leading:
                new_page()
            c.setFont(font_name, font_size)
            c.drawString(margin_x, y, chunk)
            y -= leading
        if not line:
            y -= 6
        elif is_heading:
            y -= 4

    c.save()


def main() -> None:
    files = chapter_files()
    markdown = build_markdown(files)
    FULL_MD.write_text(markdown, encoding="utf-8")
    build_pdf(markdown)
    print(f"Built {FULL_MD}")
    print(f"Built {PDF_OUT}")


if __name__ == "__main__":
    main()
