#!/usr/bin/env python3
"""
Generate ready-to-post Pinterest pins for the toolkit.

Pinterest is the highest-leverage *passive* free-traffic source for
spreadsheet templates: pins keep getting discovered for months. These are
vertical 1000x1500 images sized exactly to Pinterest's 2:3 spec.

    python3 build_pins.py
"""
from PIL import Image, ImageDraw, ImageFilter
import os

from build_previews import (
    f, rrect, center, icon, icon_tile,
    NAVY, TEAL, INK, LIGHT, WHITE, MUTED, GOOD, WARN, PAPER,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pinterest-pins")
os.makedirs(OUT, exist_ok=True)

W, H = 1000, 1500


def wrap(d, text, font, max_w):
    words, lines, line = text.split(), [], ""
    for wd in words:
        test = (line + " " + wd).strip()
        if d.textlength(test, font=font) > max_w and line:
            lines.append(line)
            line = wd
        else:
            line = test
    if line:
        lines.append(line)
    return lines


def base():
    img = Image.new("RGB", (W, H), PAPER)
    return img, ImageDraw.Draw(img)


def cta(d, y):
    bw, bh = 620, 92
    x = (W - bw) // 2
    rrect(d, (x, y, x + bw, y + bh), bh // 2, fill=TEAL)
    center(d, W / 2, y + 24, "Tap to get the template →", f(36), WHITE)


def mini_dashboard(img, x, y, w):
    """Small dashboard card to anchor the pin visually."""
    d = ImageDraw.Draw(img)
    h = int(w * 0.44)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x + 5, y + 9, x + w + 5, y + h + 9),
                                         radius=22, fill=(20, 30, 50, 60))
    sh = sh.filter(ImageFilter.GaussianBlur(12))
    img.paste(Image.alpha_composite(img.convert("RGBA"), sh).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)
    rrect(d, (x, y, x + w, y + h), 22, fill=WHITE)
    rrect(d, (x, y, x + w, y + 70), 22, fill=NAVY)
    d.rectangle((x, y + 45, x + w, y + 70), fill=NAVY)
    icon(d, (x + 18, y + 16, x + 56, y + 54), "dashboard", color=(120, 220, 215))
    d.text((x + 66, y + 22), "Dashboard", font=f(28), fill=WHITE)
    cards = [("INCOME", "€18,450", GOOD), ("PROFIT", "€14,530", NAVY),
             ("TAX SET-ASIDE", "€3,632", WARN), ("TAKE-HOME", "€10,898", GOOD)]
    cw = (w - 60) // 2
    cardh = 86
    for i, (lab, val, col) in enumerate(cards):
        r, c = divmod(i, 2)
        cx = x + 20 + c * (cw + 20)
        cy = y + 90 + r * (cardh + 16)
        rrect(d, (cx, cy, cx + cw, cy + cardh), 12, fill=LIGHT)
        rrect(d, (cx, cy, cx + 8, cy + cardh), 12, fill=col)
        d.text((cx + 22, cy + 12), lab, font=f(18), fill=MUTED)
        d.text((cx + 22, cy + 40), val, font=f(34), fill=col)


PINS = [
    ("The only spreadsheet a\nfreelancer needs", "Invoices · Expenses · Tax · Profit", "dashboard"),
    ("Know EXACTLY what to\ncharge per hour", "Free yourself from guessing your rate", "rate"),
    ("Never get caught short\non taxes again", "Auto set-aside on every euro you earn", "tax"),
    ("Track every invoice\n& expense — automatically", "Paid, unpaid & overdue at a glance", "invoice"),
    ("Your freelance money,\nsorted in one file", "Works in Excel & Google Sheets", "expense"),
]

CAPTIONS = """PINTEREST CAPTIONS (paste one per pin)

Pin 1 — The only spreadsheet a freelancer needs
Title: Freelancer Finance Spreadsheet (Excel + Google Sheets)
Description: Run the whole money side of your freelance business in one
automatic spreadsheet — invoices, expenses, tax set-aside and profit, with a
live dashboard. Works in Excel & Google Sheets. #freelancer #freelancetips
#spreadsheet #smallbusiness #bookkeeping #googlesheets #selfemployed

Pin 2 — Know exactly what to charge
Title: Freelance Hourly Rate Calculator
Description: Stop guessing your rate. This template tells you the exact hourly
and day rate to hit your income goal — plus tracks invoices, expenses and tax.
#freelancerate #freelancetips #pricing #freelancer #sidehustle #smallbusiness

Pin 3 — Never get caught short on taxes
Title: Freelance Tax Set-Aside Tracker
Description: Automatically reserve the right amount of tax on every euro you
earn, so tax season never surprises you. Part of an all-in-one freelancer
finance template. #taxes #freelancer #selfemployed #bookkeeping #moneytips

Pin 4 — Track invoices & expenses automatically
Title: Invoice & Expense Tracker for Freelancers
Description: Log invoices and costs once; see paid, unpaid and overdue plus your
real profit instantly. Excel & Google Sheets. #invoicetracker #expensetracker
#freelancer #smallbusiness #bookkeeping #spreadsheettemplate

Pin 5 — Your freelance money, sorted
Title: All-in-One Freelancer Finance Toolkit
Description: One clean spreadsheet for invoices, expenses, tax and rates — does
all the math for you. Instant download, works in Excel & Google Sheets.
#freelancer #freelancetips #digitaldownload #googlesheets #budgettemplate

TIP: Pin 2-3 of these per week to a board like "Freelance Tips" / "Small
Business Finance". Link every pin to your Etsy/Gumroad listing URL.
"""


def build():
    for i, (headline, sub, ic) in enumerate(PINS, 1):
        img, d = base()
        # top color band
        d.rectangle((0, 0, W, 70), fill=TEAL)
        center(d, W / 2, 18, "FREELANCER FINANCE TOOLKIT", f(30), WHITE)
        # icon tile
        icon_tile(d, (W - 150) // 2, 120, 150, ic)
        # headline
        y = 310
        for line in headline.split("\n"):
            center(d, W / 2, y, line, f(64), NAVY)
            y += 78
        # subheading
        for line in wrap(d, sub, f(34, False), W - 140):
            center(d, W / 2, y + 20, line, f(34, False), MUTED)
            y += 46
        # mini dashboard
        mini_dashboard(img, 90, 720, W - 180)
        d = ImageDraw.Draw(img)
        # CTA + footer
        cta(d, 1300)
        center(d, W / 2, 1430, "Excel · Google Sheets · instant download", f(26, False), MUTED)
        img.save(os.path.join(OUT, f"pin-{i}.png"))

    with open(os.path.join(OUT, "captions.txt"), "w") as fh:
        fh.write(CAPTIONS)
    print("Wrote pins + captions to", OUT)
    for fn in sorted(os.listdir(OUT)):
        print("  -", fn)


if __name__ == "__main__":
    build()
