#!/usr/bin/env python3
"""
Generate marketing / listing images for the Freelancer Finance Toolkit.

Produces high-resolution PNGs ready to upload as Etsy / Gumroad listing
photos:  cover, dashboard mockup, features, what's-inside.

    python3 build_previews.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "listing-images")
os.makedirs(OUT, exist_ok=True)

# palette (matches the workbook)
NAVY   = (27, 58, 91)
TEAL   = (44, 122, 123)
INK    = (31, 41, 51)
LIGHT  = (237, 242, 247)
ACCENT = (230, 255, 250)
WHITE  = (255, 255, 255)
MUTED  = (113, 128, 150)
GOOD   = (39, 103, 73)
WARN   = (156, 66, 33)
PAPER  = (248, 250, 252)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def f(size, bold=True):
    return ImageFont.truetype(FONTB if bold else FONT, size)


def rrect(d, box, radius, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def center(d, cx, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill)


def icon(d, box, kind, color=WHITE):
    """Draw a simple line icon inside box (square)."""
    x0, y0, x1, y1 = box
    w = x1 - x0
    s = w * 0.08  # stroke
    pad = w * 0.18
    ax0, ay0, ax1, ay1 = x0 + pad, y0 + pad, x1 - pad, y1 - pad
    if kind == "dashboard":
        bw = (ax1 - ax0) / 4
        heights = [0.5, 0.8, 0.35]
        for i, h in enumerate(heights):
            bx = ax0 + i * (bw + bw * 0.3)
            d.rectangle((bx, ay1 - (ay1 - ay0) * h, bx + bw, ay1), fill=color)
    elif kind == "invoice":
        d.rounded_rectangle((ax0, ay0, ax1, ay1), radius=w * 0.06, outline=color, width=int(s))
        for i in range(3):
            yy = ay0 + (ay1 - ay0) * (0.32 + i * 0.22)
            d.line((ax0 + pad * 0.5, yy, ax1 - pad * 0.5, yy), fill=color, width=int(s * 0.8))
    elif kind == "expense":
        # receipt with zigzag bottom
        d.rectangle((ax0, ay0, ax1, ay1 - (ay1 - ay0) * 0.12), outline=color, width=int(s))
        for i in range(2):
            yy = ay0 + (ay1 - ay0) * (0.3 + i * 0.25)
            d.line((ax0 + pad * 0.5, yy, ax1 - pad * 0.5, yy), fill=color, width=int(s * 0.7))
    elif kind == "rate":
        # percent sign
        d.line((ax0, ay1, ax1, ay0), fill=color, width=int(s))
        rr = w * 0.11
        d.ellipse((ax0, ay0, ax0 + 2 * rr, ay0 + 2 * rr), outline=color, width=int(s * 0.8))
        d.ellipse((ax1 - 2 * rr, ay1 - 2 * rr, ax1, ay1), outline=color, width=int(s * 0.8))
    elif kind == "tax":
        # bank: roof triangle + columns
        d.polygon([(ax0, ay0 + (ay1 - ay0) * 0.35),
                   ((ax0 + ax1) / 2, ay0),
                   (ax1, ay0 + (ay1 - ay0) * 0.35)], fill=color)
        cy = ay0 + (ay1 - ay0) * 0.4
        d.rectangle((ax0, ay1 - s, ax1, ay1), fill=color)
        for i in range(3):
            cx = ax0 + (ax1 - ax0) * (0.16 + i * 0.34)
            d.rectangle((cx, cy, cx + s * 1.2, ay1 - s), fill=color)
    elif kind == "project":
        # folder
        tabw = (ax1 - ax0) * 0.45
        d.rectangle((ax0, ay0 + (ay1 - ay0) * 0.18, ax0 + tabw, ay0 + (ay1 - ay0) * 0.38), fill=color)
        d.rounded_rectangle((ax0, ay0 + (ay1 - ay0) * 0.3, ax1, ay1), radius=w * 0.05, fill=color)


def icon_tile(d, x, y, size, kind):
    rrect(d, (x, y, x + size, y + size), size * 0.22, fill=TEAL)
    icon(d, (x, y, x + size, y + size), kind, color=WHITE)


def shadow_card(img, box, radius=24, fill=WHITE):
    """Card with a soft drop shadow."""
    x0, y0, x1, y1 = box
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle((x0 + 6, y0 + 10, x1 + 6, y1 + 10), radius=radius,
                         fill=(20, 30, 50, 55))
    sh = sh.filter_blur() if False else sh
    from PIL import ImageFilter
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(sh)
    d = ImageDraw.Draw(img)
    rrect(d, box, radius, fill=fill)


# --------------------------------------------------------- dashboard mockup
def dashboard_mockup(W=1600, H=1200):
    img = Image.new("RGBA", (W, H), PAPER + (255,))
    d = ImageDraw.Draw(img)

    # window chrome
    shadow_card(img, (60, 60, W - 60, H - 60), radius=28, fill=WHITE)
    d = ImageDraw.Draw(img)
    # banner
    rrect(d, (60, 60, W - 60, 150), 28, fill=NAVY)
    d.rectangle((60, 110, W - 60, 150), fill=NAVY)
    icon(d, (95, 72, 145, 122), "dashboard", color=(120, 220, 215))
    d.text((160, 80), "Dashboard", font=f(40), fill=WHITE)
    d.text((100, 130), "Live snapshot of your business — updates automatically",
           font=f(20, False), fill=(200, 220, 235))

    # KPI cards
    cards = [
        ("INCOME RECEIVED", "€ 18,450", GOOD),
        ("OUTSTANDING", "€ 2,300", WARN),
        ("TOTAL EXPENSES", "€ 3,920", WARN),
        ("NET PROFIT", "€ 14,530", NAVY),
        ("TAX TO SET ASIDE", "€ 3,632", WARN),
        ("TAKE-HOME", "€ 10,898", GOOD),
    ]
    cx0, cy0 = 100, 185
    cw, ch, gx, gy = 440, 120, 30, 25
    for i, (label, val, col) in enumerate(cards):
        r, c = divmod(i, 3)
        x = cx0 + c * (cw + gx)
        y = cy0 + r * (ch + gy)
        rrect(d, (x, y, x + cw, y + ch), 16, fill=LIGHT)
        rrect(d, (x, y, x + 10, y + ch), 16, fill=col)
        d.text((x + 30, y + 18), label, font=f(18), fill=MUTED)
        d.text((x + 30, y + 50), val, font=f(40), fill=col)

    # progress bar to goal
    py = cy0 + 2 * (ch + gy) + 20
    d.text((100, py), "Progress to annual goal", font=f(22), fill=INK)
    d.text((100, py + 34), "61.5%", font=f(48), fill=TEAL)
    bar_x0, bar_x1 = 360, W - 110
    bar_y = py + 55
    rrect(d, (bar_x0, bar_y, bar_x1, bar_y + 30), 15, fill=LIGHT)
    rrect(d, (bar_x0, bar_y, bar_x0 + int((bar_x1 - bar_x0) * 0.615), bar_y + 30),
          15, fill=TEAL)

    # bar chart: income vs expenses
    chart_y0 = py + 130
    d.text((100, chart_y0), "Income vs Expenses by month", font=f(24), fill=INK)
    base = chart_y0 + 250
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    inc_vals = [0.4, 0.55, 0.7, 0.5, 0.85, 0.95, 0.6, 0.75]
    exp_vals = [0.15, 0.2, 0.1, 0.25, 0.18, 0.22, 0.14, 0.2]
    bx = 120
    slot = 150
    maxh = 200
    for m, iv, ev in zip(months, inc_vals, exp_vals):
        d.rectangle((bx, base - iv * maxh, bx + 45, base), fill=TEAL)
        d.rectangle((bx + 50, base - ev * maxh, bx + 95, base), fill=WARN)
        center(d, bx + 47, base + 12, m, f(18, False), MUTED)
        bx += slot
    # legend
    lx = W - 430
    d.rectangle((lx, chart_y0 + 6, lx + 26, chart_y0 + 28), fill=TEAL)
    d.text((lx + 36, chart_y0 + 4), "Income", font=f(20, False), fill=INK)
    d.rectangle((lx + 170, chart_y0 + 6, lx + 196, chart_y0 + 28), fill=WARN)
    d.text((lx + 206, chart_y0 + 4), "Expenses", font=f(20, False), fill=INK)

    return img.convert("RGB")


# --------------------------------------------------------- cover image
def cover(W=2000, H=2000):
    img = Image.new("RGBA", (W, H), NAVY + (255,))
    d = ImageDraw.Draw(img)
    # subtle top band gradient-ish
    for i in range(260):
        c = (27 + i // 12, 58 + i // 10, 91 + i // 8)
        d.line((0, i, W, i), fill=c)

    d.text((130, 150), "FREELANCER", font=f(120), fill=WHITE)
    d.text((130, 290), "FINANCE", font=f(150), fill=(120, 220, 215))
    d.text((130, 460), "& BUSINESS TOOLKIT", font=f(78), fill=WHITE)
    d.text((136, 580), "Invoices · Expenses · Tax · Rates · Dashboard",
           font=f(40, False), fill=(190, 210, 225))

    # embed a scaled dashboard mockup
    dash = dashboard_mockup().convert("RGBA")
    scale = (W - 280) / dash.width
    dash = dash.resize((int(dash.width * scale), int(dash.height * scale)))
    # card behind it
    from PIL import ImageFilter
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle((130, 700, 130 + dash.width, 700 + dash.height + 0),
                         radius=30, fill=(0, 0, 0, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(25))
    img.alpha_composite(sh)
    img.alpha_composite(dash, (140, 700))

    d = ImageDraw.Draw(img)
    # footer badges
    by = H - 150
    badges = ["✓ Excel + Google Sheets", "✓ No formulas to set up", "✓ Instant download"]
    bx = 130
    for b in badges:
        w = d.textlength(b, font=f(34, False)) + 60
        rrect(d, (bx, by, bx + w, by + 70), 35, fill=(255, 255, 255, 30))
        d.text((bx + 30, by + 16), b, font=f(34, False), fill=WHITE)
        bx += w + 30
    return img.convert("RGB")


# --------------------------------------------------------- features image
def features(W=1600, H=1200):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    rrect(d, (0, 0, W, 170), 0, fill=NAVY)
    center(d, W / 2, 45, "Everything you need to run the money side", f(52), WHITE)
    center(d, W / 2, 115, "of your freelance business — in one file", f(34, False),
           (190, 210, 225))

    items = [
        ("dashboard", "Auto Dashboard", "Profit, tax & take-home update as you type. Charts included."),
        ("invoice", "Invoice Tracker", "Log invoices with Paid / Unpaid / Overdue status."),
        ("expense", "Expense Tracker", "Categorised costs with a deductible flag for tax time."),
        ("rate", "Rate Calculator", "Know the exact hourly & day rate to hit your income goal."),
        ("tax", "Tax Set-Aside", "Always reserve the right amount — never get caught short."),
        ("project", "Project Tracker", "See your pipeline and your real effective hourly rate."),
    ]
    cw, ch, gx, gy = 700, 280, 40, 40
    x0, y0 = 80, 220
    for i, (icon, title, desc) in enumerate(items):
        r, c = divmod(i, 2)
        x = x0 + c * (cw + gx)
        y = y0 + r * (ch + gy)
        shadow_card(img, (x, y, x + cw, y + ch), radius=22, fill=WHITE) if False else \
            rrect(d, (x, y, x + cw, y + ch), 22, fill=WHITE, outline=LIGHT, width=2)
        rrect(d, (x, y, x + 14, y + ch), 22, fill=TEAL)
        icon_tile(d, x + 45, y + 40, 90, icon)
        d.text((x + 175, y + 45), title, font=f(40), fill=NAVY)
        # wrap desc
        words = desc.split()
        line, yy = "", y + 120
        for wd in words:
            test = (line + " " + wd).strip()
            if d.textlength(test, font=f(28, False)) > cw - 215:
                d.text((x + 175, yy), line, font=f(28, False), fill=MUTED)
                yy += 40
                line = wd
            else:
                line = test
        d.text((x + 175, yy), line, font=f(28, False), fill=MUTED)
    return img


def main():
    cover().save(os.path.join(OUT, "1-cover.png"))
    dashboard_mockup().save(os.path.join(OUT, "2-dashboard.png"))
    features().save(os.path.join(OUT, "3-features.png"))
    print("Wrote listing images to", OUT)
    for fn in sorted(os.listdir(OUT)):
        print("  -", fn)


if __name__ == "__main__":
    main()
