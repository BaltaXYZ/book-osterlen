#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
import math
import re
from typing import Iterable
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFilter
from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIR = ROOT / "docs" / "chapters"
BOOK_PDF = ROOT / "docs" / "book-edition.pdf"
COVER_ART = ROOT / "docs" / "book-cover-art.png"
TITLE = "Ormleden"
SUBTITLE = "En Österlenthriller"
FULL_TITLE = f"{TITLE}: {SUBTITLE}"


AVENIR = Path("/System/Library/Fonts/Avenir Next.ttc")
PALATINO = Path("/System/Library/Fonts/Palatino.ttc")


@dataclass
class Chapter:
    sort_key: str
    label: str
    title: str
    paragraphs: list[str]


def register_fonts() -> None:
    font_specs = [
        ("AvenirNextBold", AVENIR, 0),
        ("AvenirNextMedium", AVENIR, 5),
        ("AvenirNextRegular", AVENIR, 7),
        ("Palatino", PALATINO, 0),
        ("PalatinoItalic", PALATINO, 1),
        ("PalatinoBold", PALATINO, 2),
        ("PalatinoBoldItalic", PALATINO, 3),
    ]
    for name, path, index in font_specs:
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(path), subfontIndex=index))


def chapter_paths() -> list[Path]:
    return sorted(CHAPTER_DIR.glob("*.md"))


def clean_heading(raw: str) -> tuple[str, str]:
    text = raw.lstrip("#").strip()
    match = re.match(r"^([0-9]{2}[A-Z]?|[0-9]{2}[a-z]?)\.\s+(.*)$", text)
    if match:
        label = match.group(1).upper()
        title = match.group(2).strip()
        return label, title
    return "", text


def parse_chapter(path: Path) -> Chapter:
    text = path.read_text(encoding="utf-8").strip()
    lines = text.splitlines()
    heading = next((line for line in lines if line.strip().startswith("#")), path.stem)
    label, title = clean_heading(heading)
    body = "\n".join(lines[1:]).strip()
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    return Chapter(sort_key=path.name, label=label, title=title, paragraphs=paragraphs)


def load_chapters() -> list[Chapter]:
    return [parse_chapter(path) for path in chapter_paths()]


def convert_inline_markdown(text: str) -> str:
    converted = escape(text)
    converted = re.sub(r"`([^`]+)`", r"\1", converted)
    converted = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", converted)
    converted = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", converted)
    converted = re.sub(r"_([^_]+)_", r"<i>\1</i>", converted)
    return converted


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug or "entry"


def build_cover_art() -> None:
    width = 1800
    height = int(width * math.sqrt(2))
    image = Image.new("RGB", (width, height), "#0f1b24")
    draw = ImageDraw.Draw(image)

    for y in range(height):
        ratio = y / max(height - 1, 1)
        if ratio < 0.55:
            blend = ratio / 0.55
            top = (13, 24, 33)
            mid = (40, 78, 101)
            color = tuple(int(top[i] + (mid[i] - top[i]) * blend) for i in range(3))
        else:
            blend = (ratio - 0.55) / 0.45
            mid = (40, 78, 101)
            bottom = (193, 144, 82)
            color = tuple(int(mid[i] + (bottom[i] - mid[i]) * blend) for i in range(3))
        draw.line((0, y, width, y), fill=color)

    sea_top = int(height * 0.54)
    for y in range(sea_top, int(height * 0.73)):
        ratio = (y - sea_top) / max(int(height * 0.19), 1)
        c1 = (32, 67, 83)
        c2 = (18, 35, 46)
        color = tuple(int(c1[i] + (c2[i] - c1[i]) * ratio) for i in range(3))
        draw.line((0, y, width, y), fill=color)

    sea_horizon = int(height * 0.56)
    draw.line((0, sea_horizon, width, sea_horizon), fill=(160, 171, 171), width=2)

    far_ridge = [
        (0, int(height * 0.67)),
        (int(width * 0.11), int(height * 0.66)),
        (int(width * 0.22), int(height * 0.64)),
        (int(width * 0.34), int(height * 0.61)),
        (int(width * 0.46), int(height * 0.60)),
        (int(width * 0.60), int(height * 0.59)),
        (int(width * 0.73), int(height * 0.60)),
        (int(width * 0.88), int(height * 0.63)),
        (width, int(height * 0.65)),
        (width, height),
        (0, height),
    ]
    draw.polygon(far_ridge, fill=(44, 58, 45))

    village_white = (225, 219, 207)
    village_red = (117, 58, 43)
    village_shadow = (54, 52, 48)
    houses = [
        (0.14, 0.705, 0.06, 0.028),
        (0.21, 0.695, 0.07, 0.03),
        (0.29, 0.706, 0.065, 0.026),
        (0.37, 0.698, 0.075, 0.031),
        (0.47, 0.704, 0.07, 0.028),
    ]
    for x, y, w, h in houses:
        left = int(width * x)
        top = int(height * y)
        right = int(width * (x + w))
        bottom = int(height * (y + h))
        draw.rectangle((left, top, right, bottom), fill=village_white)
        roof = [
            (left - 8, top),
            ((left + right) // 2, top - int(height * 0.016)),
            (right + 8, top),
        ]
        draw.polygon(roof, fill=village_red)
        draw.rectangle((left + 4, top + 5, left + 8, bottom), fill=village_shadow)

    harbor_pier = [
        (int(width * 0.08), int(height * 0.76)),
        (int(width * 0.23), int(height * 0.74)),
        (int(width * 0.33), int(height * 0.73)),
        (int(width * 0.46), int(height * 0.72)),
        (int(width * 0.58), int(height * 0.73)),
        (int(width * 0.66), int(height * 0.75)),
        (int(width * 0.66), int(height * 0.78)),
        (int(width * 0.08), int(height * 0.79)),
    ]
    draw.polygon(harbor_pier, fill=(63, 66, 58))
    for mast_x in [0.11, 0.16, 0.20]:
        x = int(width * mast_x)
        draw.line((x, int(height * 0.69), x, int(height * 0.75)), fill=(36, 38, 34), width=3)
        draw.line((x, int(height * 0.705), x + 18, int(height * 0.718)), fill=(36, 38, 34), width=2)

    field = [
        (0, int(height * 0.82)),
        (int(width * 0.14), int(height * 0.80)),
        (int(width * 0.27), int(height * 0.81)),
        (int(width * 0.45), int(height * 0.78)),
        (int(width * 0.61), int(height * 0.81)),
        (int(width * 0.79), int(height * 0.79)),
        (width, int(height * 0.83)),
        (width, height),
        (0, height),
    ]
    draw.polygon(field, fill=(85, 86, 49))

    haze = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    haze_draw = ImageDraw.Draw(haze)
    haze_draw.ellipse(
        (
            int(width * 0.16),
            int(height * 0.22),
            int(width * 0.80),
            int(height * 0.62),
        ),
        fill=(244, 198, 116, 80),
    )
    haze = haze.filter(ImageFilter.GaussianBlur(70))
    image = Image.alpha_composite(image.convert("RGBA"), haze)

    mist = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    mist_draw = ImageDraw.Draw(mist)
    mist_draw.rectangle(
        (0, int(height * 0.56), width, int(height * 0.77)),
        fill=(220, 226, 226, 25),
    )
    mist = mist.filter(ImageFilter.GaussianBlur(35))
    image = Image.alpha_composite(image, mist)

    draw = ImageDraw.Draw(image)
    stone_color = (24, 27, 29)
    ridge_y = int(height * 0.655)
    xs = [0.20, 0.29, 0.38, 0.47, 0.56, 0.65, 0.74]
    heights = [0.070, 0.090, 0.075, 0.108, 0.080, 0.092, 0.073]
    widths = [0.017, 0.016, 0.014, 0.019, 0.015, 0.017, 0.014]
    for x_frac, h_frac, w_frac in zip(xs, heights, widths):
        cx = int(width * x_frac)
        stone_h = int(height * h_frac)
        stone_w = int(width * w_frac)
        draw.rounded_rectangle(
            (
                cx - stone_w // 2,
                ridge_y - stone_h,
                cx + stone_w // 2,
                ridge_y,
            ),
            radius=10,
            fill=stone_color,
        )
    draw.line(
        (int(width * 0.16), ridge_y, int(width * 0.78), ridge_y),
        fill=(53, 58, 49),
        width=5,
    )

    path_points = [
        (int(width * 0.50), height),
        (int(width * 0.49), int(height * 0.90)),
        (int(width * 0.51), int(height * 0.84)),
        (int(width * 0.48), int(height * 0.77)),
        (int(width * 0.45), int(height * 0.72)),
        (int(width * 0.43), int(height * 0.69)),
    ]
    draw.line(path_points, fill=(178, 160, 118), width=18)
    draw.line(path_points, fill=(204, 186, 142), width=8)

    snake = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    snake_draw = ImageDraw.Draw(snake)
    snake_points = []
    for step in range(28):
        t = step / 27
        x = int(width * (0.11 + 0.76 * t))
        y = int(height * (0.33 + 0.035 * math.sin(t * 4.2 * math.pi) + 0.02 * t))
        snake_points.append((x, y))
    snake_draw.line(snake_points, fill=(232, 214, 179, 88), width=9)
    snake = snake.filter(ImageFilter.GaussianBlur(2))
    image = Image.alpha_composite(image, snake)

    grain = Image.effect_noise((width, height), 12).convert("L")
    grain = grain.point(lambda p: min(255, max(0, int(p * 0.35))))
    grain_rgba = Image.merge("RGBA", (grain, grain, grain, Image.new("L", (width, height), 26)))
    image = Image.alpha_composite(image, grain_rgba)

    image.convert("RGB").save(COVER_ART)


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        self.book_title = TITLE
        self.current_header = TITLE
        self.title_style_names = {"ChapterTitle"}

        margin_left = 18 * mm
        margin_right = 18 * mm
        margin_top = 22 * mm
        margin_bottom = 18 * mm
        frame = Frame(
            margin_left,
            margin_bottom,
            A5[0] - margin_left - margin_right,
            A5[1] - margin_top - margin_bottom,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
            id="normal",
        )
        self.addPageTemplates(
            [
                PageTemplate(id="FrontMatter", frames=[frame], onPage=self.draw_frontmatter),
                PageTemplate(id="Body", frames=[frame], onPage=self.draw_body),
            ]
        )

    def draw_frontmatter(self, canv: canvas.Canvas, doc: BaseDocTemplate) -> None:
        canv.setFillColor(colors.HexColor("#2b2d2f"))
        canv.setStrokeColor(colors.HexColor("#d0c4ab"))
        canv.setLineWidth(0.5)
        canv.line(18 * mm, A5[1] - 14 * mm, A5[0] - 18 * mm, A5[1] - 14 * mm)

    def draw_body(self, canv: canvas.Canvas, doc: BaseDocTemplate) -> None:
        width, height = A5
        header_y = height - 12 * mm
        canv.setStrokeColor(colors.HexColor("#d5c9b1"))
        canv.setLineWidth(0.45)
        canv.line(18 * mm, height - 15 * mm, width - 18 * mm, height - 15 * mm)
        canv.setFillColor(colors.HexColor("#55524d"))
        canv.setFont("AvenirNextRegular", 8)
        page_text = str(canv.getPageNumber())
        if canv.getPageNumber() % 2 == 0:
            canv.drawString(18 * mm, header_y, page_text)
            canv.drawRightString(width - 18 * mm, header_y, self.book_title)
        else:
            canv.drawString(18 * mm, header_y, self.current_header)
            canv.drawRightString(width - 18 * mm, header_y, page_text)

    def afterFlowable(self, flowable) -> None:
        if isinstance(flowable, Paragraph) and flowable.style.name in self.title_style_names:
            toc_text = getattr(flowable, "toc_text", flowable.getPlainText())
            key = slugify(toc_text)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(toc_text, key, level=0, closed=False)
            self.notify("TOCEntry", (0, toc_text, self.page, key))
            self.current_header = flowable.getPlainText()


def build_styles() -> dict[str, ParagraphStyle]:
    sample = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=sample["BodyText"],
        fontName="Palatino",
        fontSize=10.7,
        leading=14.3,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#222222"),
        firstLineIndent=5 * mm,
        spaceAfter=0,
        spaceBefore=0,
    )
    body_first = ParagraphStyle(
        "BodyFirst",
        parent=body,
        firstLineIndent=0,
    )
    chapter_kicker = ParagraphStyle(
        "ChapterKicker",
        parent=sample["Heading2"],
        fontName="AvenirNextBold",
        fontSize=10,
        leading=12,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#7b654a"),
        spaceBefore=0,
        spaceAfter=5 * mm,
    )
    chapter_title = ParagraphStyle(
        "ChapterTitle",
        parent=sample["Heading1"],
        fontName="PalatinoBold",
        fontSize=19,
        leading=22,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#1f1e1b"),
        spaceBefore=0,
        spaceAfter=8 * mm,
    )
    title_page_title = ParagraphStyle(
        "TitlePageTitle",
        parent=sample["Title"],
        fontName="PalatinoBold",
        fontSize=26,
        leading=32,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1c1b19"),
    )
    title_page_subtitle = ParagraphStyle(
        "TitlePageSubtitle",
        parent=sample["Normal"],
        fontName="AvenirNextMedium",
        fontSize=11,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#7b654a"),
    )
    title_page_meta = ParagraphStyle(
        "TitlePageMeta",
        parent=sample["Normal"],
        fontName="PalatinoItalic",
        fontSize=10.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#54514d"),
    )
    front_heading = ParagraphStyle(
        "FrontHeading",
        parent=sample["Heading1"],
        fontName="PalatinoBold",
        fontSize=18,
        leading=22,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#1f1e1b"),
        spaceAfter=6 * mm,
    )
    toc_entry = ParagraphStyle(
        "TOCEntry",
        parent=sample["Normal"],
        fontName="Palatino",
        fontSize=10.6,
        leading=13.8,
        textColor=colors.HexColor("#24211d"),
        leftIndent=0,
        firstLineIndent=0,
    )
    return {
        "Body": body,
        "BodyFirst": body_first,
        "ChapterKicker": chapter_kicker,
        "ChapterTitle": chapter_title,
        "TitlePageTitle": title_page_title,
        "TitlePageSubtitle": title_page_subtitle,
        "TitlePageMeta": title_page_meta,
        "FrontHeading": front_heading,
        "TOCEntry": toc_entry,
    }


def add_title_page(story: list, styles: dict[str, ParagraphStyle]) -> None:
    story.append(Spacer(1, 34 * mm))
    story.append(Paragraph(TITLE, styles["TitlePageTitle"]))
    story.append(Spacer(1, 7 * mm))
    story.append(Paragraph(SUBTITLE, styles["TitlePageSubtitle"]))
    story.append(Spacer(1, 20 * mm))
    story.append(
        Paragraph(
            "Formgiven bokutgåva byggd från kapitelmanuset i <i>docs/chapters/</i>.",
            styles["TitlePageMeta"],
        )
    )
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Omslagsillustration: originalbild inspirerad av Ales stenar, Kåseberga och Österlenkusten.",
            styles["TitlePageMeta"],
        )
    )
    story.append(PageBreak())


def add_contents_page(story: list, styles: dict[str, ParagraphStyle]) -> None:
    story.append(Paragraph("Innehåll", styles["FrontHeading"]))
    toc = TableOfContents()
    toc.levelStyles = [styles["TOCEntry"]]
    toc.dotsMinLevel = 0
    story.append(toc)
    story.append(PageBreak())


def add_chapters(story: list, styles: dict[str, ParagraphStyle], chapters: Iterable[Chapter]) -> None:
    first_chapter = True
    for chapter in chapters:
        if not first_chapter:
            story.append(PageBreak())
        first_chapter = False
        story.append(Spacer(1, 10 * mm))
        kicker_text = f"KAPITEL {chapter.label}" if chapter.label else "KAPITEL"
        story.append(Paragraph(kicker_text, styles["ChapterKicker"]))
        title_para = Paragraph(chapter.title, styles["ChapterTitle"])
        title_para.toc_text = f"Kapitel {chapter.label}. {chapter.title}" if chapter.label else chapter.title
        story.append(title_para)
        for idx, paragraph in enumerate(chapter.paragraphs):
            if paragraph.strip() in {"***", "* * *"}:
                story.append(Spacer(1, 4 * mm))
                story.append(Paragraph("~", styles["TitlePageMeta"]))
                story.append(Spacer(1, 4 * mm))
                continue
            style = styles["BodyFirst"] if idx == 0 else styles["Body"]
            story.append(Paragraph(convert_inline_markdown(paragraph), style))
            story.append(Spacer(1, 1.2 * mm))


def build_interior_pdf(output_path: Path, chapters: list[Chapter]) -> None:
    styles = build_styles()
    doc = BookDocTemplate(
        str(output_path),
        pagesize=A5,
        title=FULL_TITLE,
        author="OpenAI Codex",
    )
    story: list = []
    add_title_page(story, styles)
    add_contents_page(story, styles)
    story.append(NextPageTemplate("Body"))
    add_chapters(story, styles, chapters)
    doc.multiBuild(story)


def draw_wrapped(canvas_obj: canvas.Canvas, text: str, x: float, y: float, width: float, style: ParagraphStyle) -> None:
    paragraph = Paragraph(convert_inline_markdown(text), style)
    w, h = paragraph.wrap(width, A5[1])
    paragraph.drawOn(canvas_obj, x, y - h)


def build_cover_pdf(output_path: Path) -> None:
    c = canvas.Canvas(str(output_path), pagesize=A5)
    width, height = A5
    c.drawImage(ImageReader(str(COVER_ART)), 0, 0, width=width, height=height, mask="auto")
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.25))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#f7f0e4"))
    c.setFont("AvenirNextMedium", 11)
    c.drawCentredString(width / 2, height - 24 * mm, "ROMAN")
    c.setFont("PalatinoBold", 30)
    c.drawCentredString(width / 2, height - 54 * mm, TITLE)
    c.setFont("AvenirNextMedium", 12)
    c.setFillColor(colors.HexColor("#eadabf"))
    c.drawCentredString(width / 2, height - 70 * mm, SUBTITLE)
    c.setFont("AvenirNextRegular", 10.5)
    c.drawCentredString(width / 2, height - 84 * mm, "av Kristian Sundström")
    c.setStrokeColor(colors.HexColor("#d7c1a1"))
    c.setLineWidth(1.2)
    c.line(18 * mm, 30 * mm, width - 18 * mm, 30 * mm)
    c.save()


def build_back_pdf(output_path: Path) -> None:
    blurb = (
        "När antikvarien Nils Severin hittas död vid Ales stenar dras arkeologen "
        "Maja Malm tillbaka till det Österlen hon lämnat bakom sig. Tillsammans med "
        "utredaren Noah Rask följer hon ett spår mellan Kivik, Glimmingehus, "
        "Stenshuvud och Kåseberga, där äldre monument visar sig bära på något långt "
        "farligare än ett lättsålt mysterium om försvunnen tro.\n\n"
        "Snart står det klart att gåtan inte handlar om en obruten kult, utan om hur "
        "makt gång på gång har tagit det människor burit i bruk och gjort om det till "
        "något som kan ägas, visas upp och styras. Och någon i nuet är beredd att döda "
        "för att få stå i mitten när berättelsen åter tas i bruk.\n\n"
        "Ormleden är en thriller där landskapet inte bara är bakgrund "
        "utan själva maskinen: vägarna, byarna, kustlinjen och stenarna driver jakten "
        "framåt hela vägen till en gryning vid havet där sanningen måste släppas fri "
        "utan att bli rov."
    )
    c = canvas.Canvas(str(output_path), pagesize=A5)
    width, height = A5
    c.drawImage(ImageReader(str(COVER_ART)), 0, 0, width=width, height=height, mask="auto")
    c.setFillColor(colors.Color(12 / 255, 17 / 255, 22 / 255, alpha=0.78))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#f2ebde"))
    c.setFont("AvenirNextBold", 10)
    c.drawString(18 * mm, height - 22 * mm, "ÖSTERLENTHRILLER")
    style = ParagraphStyle(
        "BackBlurb",
        fontName="Palatino",
        fontSize=10.4,
        leading=14.2,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#f2ebde"),
    )
    draw_wrapped(c, blurb, 18 * mm, height - 30 * mm, width - 36 * mm, style)
    c.setStrokeColor(colors.HexColor("#c8af85"))
    c.setLineWidth(0.8)
    c.line(18 * mm, 24 * mm, width - 18 * mm, 24 * mm)
    footer_style = ParagraphStyle(
        "BackFooter",
        fontName="AvenirNextRegular",
        fontSize=8.5,
        leading=11,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#d4c8b4"),
    )
    draw_wrapped(
        c,
        "Omslagsillustration skapad lokalt för denna bokutgåva, inspirerad av Ales stenar och Österlenkusten.",
        18 * mm,
        20 * mm,
        width - 36 * mm,
        footer_style,
    )
    c.save()


def merge_pdfs(front: Path, interior: Path, back: Path, output: Path) -> None:
    writer = PdfWriter()
    for source in [front, interior, back]:
        reader = PdfReader(str(source))
        for page in reader.pages:
            writer.add_page(page)
    with output.open("wb") as handle:
        writer.write(handle)


def main() -> None:
    register_fonts()
    build_cover_art()
    chapters = load_chapters()
    with TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        front = tmp / "front.pdf"
        interior = tmp / "interior.pdf"
        back = tmp / "back.pdf"
        build_cover_pdf(front)
        build_interior_pdf(interior, chapters)
        build_back_pdf(back)
        merge_pdfs(front, interior, back, BOOK_PDF)
    print(f"Built {COVER_ART}")
    print(f"Built {BOOK_PDF}")


if __name__ == "__main__":
    main()
