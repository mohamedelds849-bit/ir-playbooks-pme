#!/usr/bin/env python3
"""Build the IR playbooks PDF from the Markdown sources in ../docs.

Usage:  python build/build_pdf.py
Output: output/AgriSouss-Reponse-Incidents.pdf  and  diagrams/*.mmd

Only a small Markdown subset is supported (the one used in docs/):
headings (#..####), paragraphs, bullet / numbered / checkbox lists, pipe tables,
fenced code blocks (``` and ```mermaid), blockquotes, **bold**, *italic*, `code`,
and the marker <!-- pagebreak -->.

Mermaid diagrams are NOT rendered as images: they are printed as source text in
the PDF and exported to diagrams/*.mmd (GitHub and mermaid.live render them).
"""
from __future__ import annotations

import os
import re
import sys
from datetime import date
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT_DIR = os.path.join(ROOT, "output")
DIAG_DIR = os.path.join(ROOT, "diagrams")
OUT_PDF = os.path.join(OUT_DIR, "AgriSouss-Reponse-Incidents.pdf")

SOURCES = [
    "00-introduction.md",
    "01-politique-reponse-incidents.md",
    "02-playbook-phishing-bec.md",
    "03-playbook-ransomware.md",
    "04-playbook-compromission-site-web.md",
    "05-exercice-tabletop-ransomware.md",
    "06-fiches-reflexes.md",
]
LARGE = {"06-fiches-reflexes.md"}  # one-page printable sheets: larger type

# ---------------------------------------------------------------- fonts
FONT_DIRS = [r"C:\Windows\Fonts", "/usr/share/fonts/truetype/msttcorefonts",
             "/usr/share/fonts/truetype/dejavu", "/Library/Fonts"]
CANDIDATES = {
    "Body": ["arial.ttf", "DejaVuSans.ttf", "Arial.ttf"],
    "Body-Bold": ["arialbd.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf"],
    "Body-Italic": ["ariali.ttf", "DejaVuSans-Oblique.ttf", "Arial Italic.ttf"],
    "Body-BoldItalic": ["arialbi.ttf", "DejaVuSans-BoldOblique.ttf", "Arial Bold Italic.ttf"],
    "Mono": ["consola.ttf", "DejaVuSansMono.ttf", "Courier New.ttf"],
}


def find_font(names):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.isfile(p):
                return p
    return None


def register_fonts():
    paths = {k: find_font(v) for k, v in CANDIDATES.items()}
    if not all(paths.values()):
        missing = [k for k, v in paths.items() if not v]
        sys.exit(f"Missing TrueType fonts {missing}; Unicode (French, arrows, □) needs a TTF.")
    for name, path in paths.items():
        pdfmetrics.registerFont(TTFont(name, path))
    pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                  italic="Body-Italic", boldItalic="Body-BoldItalic")


# ---------------------------------------------------------------- styles
NAVY = colors.HexColor("#1F3A5F")
TEAL = colors.HexColor("#2E7D6B")
LIGHT = colors.HexColor("#EEF3F8")
GRID = colors.HexColor("#B8C4D2")
QUOTE_BG = colors.HexColor("#F6F4EC")
CODE_BG = colors.HexColor("#F3F3F3")


def make_styles(scale=1.0):
    ss = getSampleStyleSheet()
    s = {}
    b = 9.6 * scale
    s["body"] = ParagraphStyle("body", parent=ss["Normal"], fontName="Body", fontSize=b,
                               leading=b * 1.38, spaceAfter=4 * scale)
    s["h1"] = ParagraphStyle("h1", parent=s["body"], fontName="Body-Bold", fontSize=17 * scale,
                             leading=21 * scale, textColor=NAVY, spaceBefore=2, spaceAfter=10 * scale)
    s["h2"] = ParagraphStyle("h2", parent=s["body"], fontName="Body-Bold", fontSize=12.5 * scale,
                             leading=16 * scale, textColor=NAVY, spaceBefore=9 * scale, spaceAfter=5 * scale)
    s["h3"] = ParagraphStyle("h3", parent=s["body"], fontName="Body-Bold", fontSize=10.8 * scale,
                             leading=14 * scale, textColor=TEAL, spaceBefore=7 * scale, spaceAfter=3 * scale)
    s["h4"] = ParagraphStyle("h4", parent=s["h3"], fontSize=10 * scale, textColor=colors.black)
    for h in ("h2", "h3", "h4"):
        s[h].keepWithNext = 1  # avoid headings stranded at the bottom of a page
    s["li"] = ParagraphStyle("li", parent=s["body"], leftIndent=14, bulletIndent=3, spaceAfter=1.5 * scale,
                             bulletFontName="Body", bulletFontSize=b)
    s["cell"] = ParagraphStyle("cell", parent=s["body"], fontSize=b * 0.86, leading=b * 0.86 * 1.3,
                               spaceAfter=0)
    s["cellh"] = ParagraphStyle("cellh", parent=s["cell"], fontName="Body-Bold", textColor=colors.white)
    s["code"] = ParagraphStyle("code", parent=s["body"], fontName="Mono", fontSize=7.4 * scale,
                               leading=9.4 * scale, spaceAfter=0)
    s["caption"] = ParagraphStyle("caption", parent=s["body"], fontName="Body-Italic",
                                  fontSize=8 * scale, textColor=colors.HexColor("#555555"))
    s["quote"] = ParagraphStyle("quote", parent=s["body"], fontSize=b * 0.95, leading=b * 0.95 * 1.35,
                                spaceAfter=2)
    return s


# ---------------------------------------------------------------- inline markdown
def inline(text: str) -> str:
    """Convert inline markdown to reportlab mini-HTML (code spans protected)."""
    parts = re.split(r"(`[^`]+`)", text)
    out = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append('<font name="Mono" size="-0.5">' + escape(p[1:-1]) + "</font>")
            continue
        p = escape(p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", p)
        p = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", p)
        out.append(p)
    return "".join(out)


# ---------------------------------------------------------------- doc template
class IRDoc(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                         topMargin=2.1 * cm, bottomMargin=1.9 * cm,
                         title="AgriSouss SARL - Dispositif de réponse aux incidents",
                         author="Mohamed Elansari",
                         subject="Politique IR, playbooks, exercice sur table (projet de portfolio, entreprise fictive)",
                         **kw)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame], onPage=self._cover),
            PageTemplate(id="normal", frames=[frame], onPage=self._decorate),
        ])
        self._bm = 0

    def beforeDocument(self):
        self._bm = 0  # stable bookmark keys across multiBuild passes

    def _cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, A4[1] - 7.5 * cm, A4[0], 7.5 * cm, fill=1, stroke=0)
        canv.setFillColor(TEAL)
        canv.rect(0, A4[1] - 7.8 * cm, A4[0], 0.3 * cm, fill=1, stroke=0)
        canv.restoreState()

    def _decorate(self, canv, doc):
        canv.saveState()
        canv.setFont("Body", 7.5)
        canv.setFillColor(colors.HexColor("#666666"))
        canv.drawString(2 * cm, A4[1] - 1.3 * cm,
                        "AgriSouss SARL (fictive) — Dispositif de réponse aux incidents — v1.0")
        canv.drawRightString(A4[0] - 2 * cm, A4[1] - 1.3 * cm, "Usage interne — projet de portfolio")
        canv.setStrokeColor(GRID)
        canv.line(2 * cm, A4[1] - 1.45 * cm, A4[0] - 2 * cm, A4[1] - 1.45 * cm)
        canv.drawCentredString(A4[0] / 2, 1.1 * cm, f"Page {doc.page}")
        canv.restoreState()

    def afterFlowable(self, flowable):
        lvl = getattr(flowable, "_toc_level", None)
        if lvl is None:
            return
        text = flowable.getPlainText()
        key = f"bm{self._bm}"
        self._bm += 1
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=lvl, closed=lvl > 0)
        self.notify("TOCEntry", (lvl, text, self.page, key))


# ---------------------------------------------------------------- markdown -> flowables
def col_widths(rows, total, font_size):
    """Width proportional to content, but never narrower than the longest word."""
    n = len(rows[0])
    lens = [0.0] * n
    minw = [1.2 * cm] * n
    for r in rows:
        for i, c in enumerate(r[:n]):
            plain = re.sub(r"[*`]", "", c)
            words = plain.split() or [""]
            longest = max(words, key=lambda w: pdfmetrics.stringWidth(w, "Body-Bold", font_size))
            minw[i] = max(minw[i], pdfmetrics.stringWidth(longest, "Body-Bold", font_size) + 9)
            lens[i] = max(lens[i], min(len(plain), 70) + 4)
    s = sum(lens)
    w = [max(total * l / s, m) for l, m in zip(lens, minw)]
    # shrink the flexible columns if the minimums pushed us over the page width
    over = sum(w) - total
    if over > 0:
        flex = [i for i in range(n) if w[i] > minw[i]]
        room = sum(w[i] - minw[i] for i in flex) or 1
        for i in flex:
            w[i] -= over * (w[i] - minw[i]) / room
    k = total / sum(w)
    return [x * k for x in w]


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def build_table(rows, st, width):
    header, body = rows[0], rows[1:]
    n = len(header)
    data = [[Paragraph(inline(c), st["cellh"]) for c in header]]
    for r in body:
        r = (r + [""] * n)[:n]
        data.append([Paragraph(inline(c), st["cell"]) for c in r])
    t = Table(data, colWidths=col_widths(rows, width, st["cell"].fontSize), repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.4, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]))
    return t


def code_block(lines, st, width, lang, diag_name):
    txt = "<br/>".join(escape(l).replace(" ", "&nbsp;") for l in lines)
    p = Paragraph(txt, st["code"])
    box = Table([[p]], colWidths=[width])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
        ("BOX", (0, 0), (-1, -1), 0.5, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    out = []
    if lang == "mermaid":
        out.append(Paragraph(
            f"Diagramme de décision — source Mermaid (non rendu graphiquement dans ce PDF ; "
            f"rendu sur GitHub ou mermaid.live, fichier <font name='Mono'>diagrams/{diag_name}</font>). "
            f"Lecture : chaque flèche « A --&gt; B » est une étape, « -- Oui --&gt; » une branche.",
            ParagraphStyle("captionk", parent=st["caption"], keepWithNext=1)))  # stay with the block
    out.append(box)
    out.append(Spacer(1, 5))
    return out


def quote_block(lines, st, width):
    paras = []
    buf = []
    for l in lines + [""]:
        if l.strip() == "":
            if buf:
                paras.append(Paragraph(inline(" ".join(buf)), st["quote"]))
                buf = []
        elif re.match(r"^(\d+\.|-|—)\s", l.strip()):
            if buf:
                paras.append(Paragraph(inline(" ".join(buf)), st["quote"]))
                buf = []
            paras.append(Paragraph(inline(l.strip()), st["quote"]))
        else:
            buf.append(l.strip())
    t = Table([[paras]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), QUOTE_BG),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return [t, Spacer(1, 5)]


def md_to_flowables(md, st, width, src_name, first_h1_pagebreak=True):
    flow = []
    lines = md.splitlines()
    i = 0
    para = []
    diag_count = 0
    base = os.path.splitext(src_name)[0]

    def flush():
        nonlocal para
        if para:
            flow.append(Paragraph(inline(" ".join(para)), st["body"]))
            para = []

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s == "<!-- pagebreak -->":
            flush(); flow.append(PageBreak()); i += 1; continue
        if s.startswith("```"):
            flush()
            lang = s[3:].strip()
            j = i + 1
            block = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                block.append(lines[j]); j += 1
            name = ""
            if lang == "mermaid":
                diag_count += 1
                name = f"{base}-decision-{diag_count}.mmd"
                with open(os.path.join(DIAG_DIR, name), "w", encoding="utf-8") as fh:
                    fh.write("\n".join(block) + "\n")
            flow.extend(code_block(block, st, width, lang, name))
            i = j + 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush()
            lvl = len(m.group(1))
            p = Paragraph(inline(m.group(2)), st[f"h{lvl}"])
            if lvl <= 2:
                p._toc_level = lvl - 1
            if lvl == 1 and first_h1_pagebreak:
                flow.append(PageBreak())
            flow.append(p)
            i += 1; continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-{3,}", lines[i + 1].strip()):
            flush()
            rows = [split_row(lines[i])]
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append(split_row(lines[j])); j += 1
            flow.append(build_table(rows, st, width))
            flow.append(Spacer(1, 6))
            i = j; continue
        if s.startswith(">"):
            flush()
            block = []
            j = i
            while j < len(lines) and lines[j].strip().startswith(">"):
                block.append(re.sub(r"^\s*>\s?", "", lines[j])); j += 1
            flow.extend(quote_block(block, st, width))
            i = j; continue
        m = re.match(r"^(\s*)(- \[ \]|- \[x\]|-|\*|\d+\.)\s+(.*)$", line)
        if m:
            flush()
            marker, text = m.group(2), m.group(3)
            indent = len(m.group(1)) // 2
            # continuation lines
            j = i + 1
            while j < len(lines) and lines[j].startswith("   ") and lines[j].strip() and \
                    not re.match(r"^\s*(- |\* |\d+\. )", lines[j]):
                text += " " + lines[j].strip(); j += 1
            if marker.startswith("- ["):
                bullet = "☑" if "x" in marker else "□"
            elif marker in ("-", "*"):
                bullet = "•"
            else:
                bullet = marker
            style = ParagraphStyle("lix", parent=st["li"], leftIndent=st["li"].leftIndent + 12 * indent + (6 if bullet[0].isdigit() else 0),
                                   bulletIndent=st["li"].bulletIndent + 12 * indent)
            flow.append(Paragraph(inline(text), style, bulletText=bullet))
            i = j; continue
        if s == "":
            flush(); i += 1; continue
        para.append(s)
        i += 1
    flush()
    return flow


# ---------------------------------------------------------------- cover + toc
def cover(st, width):
    title = ParagraphStyle("t", parent=st["h1"], fontSize=25, leading=30, textColor=colors.white)
    sub = ParagraphStyle("s", parent=st["body"], fontSize=12.5, leading=17, textColor=colors.white)
    meta = ParagraphStyle("m", parent=st["body"], fontSize=10, leading=15)
    note = ParagraphStyle("n", parent=st["body"], fontSize=8.8, leading=12.5, textColor=colors.HexColor("#444444"))
    f = [Spacer(1, 0.6 * cm),
         Paragraph("Dispositif de réponse aux incidents de sécurité", title),
         Spacer(1, 0.3 * cm),
         Paragraph("AgriSouss SARL — PME agricole fictive, Souss-Massa (Maroc)", sub),
         Spacer(1, 4.2 * cm)]
    rows = [
        ["Contenu", "Politique de réponse aux incidents · 3 playbooks (BEC, rançongiciel, site web) · "
                    "kit d'exercice sur table · fiches réflexes"],
        ["Référentiels", "NIST SP 800-61 r2 (phases) et r3 (2025, profil CSF 2.0) · SANS PICERL · RFC 3227 · "
                         "lois marocaines 09-08, 05-20, 07-03"],
        ["Auteur", "Mohamed Elansari — élève ingénieur en cybersécurité, Universiapolis Agadir"],
        ["Version / date", f"1.0 — {date.today().strftime('%Y-%m')}"],
        ["Classification", "Projet de portfolio — entreprise, personnes et incidents fictifs"],
    ]
    t = Table([[Paragraph(f"<b>{a}</b>", meta), Paragraph(b, meta)] for a, b in rows],
              colWidths=[3.6 * cm, width - 3.6 * cm])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.4, GRID), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    f += [t, Spacer(1, 1.2 * cm), Paragraph(
        "Avertissement : document pédagogique à visée uniquement défensive. Les éléments juridiques "
        "reflètent la lecture des textes publics par l'auteur et ne constituent pas un avis juridique ; "
        "ils doivent être validés par un juriste, la CNDP ou la DGSSI avant tout usage réel. "
        "Les diagrammes de décision sont fournis en source Mermaid (texte) dans ce PDF.", note)]
    return f


def toc_flow(st):
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName="Body-Bold", fontSize=10.5, leading=15, leftIndent=0, spaceBefore=5),
        ParagraphStyle("toc1", fontName="Body", fontSize=9, leading=12, leftIndent=14),
    ]
    return [Paragraph("Sommaire", st["h1"]), toc]


def main():
    register_fonts()
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(DIAG_DIR, exist_ok=True)
    st = make_styles(1.0)
    st_l = make_styles(1.18)
    doc = IRDoc(OUT_PDF)
    width = doc.width
    from reportlab.platypus import NextPageTemplate
    story = cover(st, width)
    story += [NextPageTemplate("normal"), PageBreak()]
    story += toc_flow(st)
    for name in SOURCES:
        with open(os.path.join(DOCS, name), encoding="utf-8") as fh:
            md = fh.read()
        story += md_to_flowables(md, st_l if name in LARGE else st, width, name)
    doc.multiBuild(story)
    print(f"PDF written: {OUT_PDF}")


if __name__ == "__main__":
    main()
