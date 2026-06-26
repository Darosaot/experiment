# Passive Income Asset — Freelancer Finance & Business Toolkit

This repo contains a **complete, ready-to-sell digital product** built to give
you a realistic shot at **€150+/month** in mostly-passive income, with the least
possible effort on your side.

The product is a polished spreadsheet toolkit for freelancers — a large,
paying, evergreen audience. It works in Excel and Google Sheets, does all its
own math, and needs essentially no customer support.

## 👉 Start here
Open **[`LAUNCH-CHECKLIST.md`](LAUNCH-CHECKLIST.md)** — it's the ~20-minute,
one-time setup that only you can do (connecting a payout account = legal KYC I
can't do for you). Everything else is already done.

## What's in this repo

```
product/
  Freelancer-Finance-Toolkit.xlsx   ← the product you sell (7 tabs, automatic)
  BUYER-QUICKSTART.md               ← short guide that ships to buyers
  build_toolkit.py                  ← regenerates the .xlsx from scratch
  build_previews.py                 ← regenerates the listing images
  listing-images/                   ← ready-to-upload Etsy/Gumroad photos
    1-cover.png  2-dashboard.png  3-features.png

marketing/
  etsy-listing.md            ← title, tags, description (Etsy — do this first)
  gumroad-listing.md         ← same, for Gumroad
  pricing-and-strategy.md    ← the honest €150/month math + pricing
  promotion-free-traffic.md  ← lowest-effort ways to get seen
  faq.md                     ← buyer FAQ

LAUNCH-CHECKLIST.md          ← your 20-minute one-time setup
```

## The honest version
- I built 100% of the **asset**: product, design, images, copy, pricing, plan.
- The **only** thing I can't do is receive money for you — every payout channel
  legally requires your identity + bank details. That's the 20-minute checklist.
- No one can *guarantee* income; it depends on traffic and reviews that build
  over ~8–12 weeks. The math to your goal is modest (~14 sales/month at €12),
  the niche has steady demand, and the listing is as strong as I can make it.

## Regenerating the files
```bash
cd product
pip install openpyxl pillow
python3 build_toolkit.py     # rebuilds the .xlsx
python3 build_previews.py    # rebuilds the listing images
```
