# QuickTools — a passive-income web app

A fast, fully static collection of free online tools (word counter, password
generator, loan calculator, QR generator, converters, and more). It's built to
earn **passive advertising income** with essentially zero ongoing effort from
you: the tools attract recurring Google search traffic, and Google AdSense
**Auto Ads** monetise that traffic automatically.

Everything runs in the visitor's browser — there is **no backend, no database,
and no server cost**, which makes it perfect for free Netlify hosting.

---

## 💶 How this makes money (and what you must do)

Realistically, money has to land in **your** account, so there are a few
one-time steps only you can do. They take ~15 minutes total. After that it runs
itself.

### Step 1 — Deploy to Netlify (≈2 min)
Netlify is already connected on your side, so you just point it at this repo:
1. In Netlify, **Add new site → Import an existing project → pick this repo**
   and the branch `claude/passive-income-netlify-hq21iv` (or `main` after you
   merge the PR).
2. Build command: **leave empty**. Publish directory: **`.`** (already set in
   `netlify.toml`, so Netlify will detect it automatically).
3. Click **Deploy**. You'll get a live URL like `https://<name>.netlify.app`.

### Step 2 — Turn on the money (≈10 min, one time)
1. Go to **https://adsense.google.com** and sign up with your Google account
   (free). Add your new Netlify site URL.
2. Google reviews the site (this is why it ships with real content, an About
   page, a Privacy Policy and Terms — those are required for approval).
3. Once approved, Google gives you a **publisher ID** like
   `ca-pub-1234567890123456`.
4. Open **`assets/js/config.js`** and paste it:
   ```js
   ADSENSE_PUBLISHER_ID: "ca-pub-1234567890123456",
   ```
5. Also open **`ads.txt`** and replace `pub-0000000000000000` with the same
   number (the digits after `pub-`). Commit & push. Netlify redeploys
   automatically.

That's it. **Auto Ads** now place ads across every page and earnings accrue in
your AdSense dashboard. You are paid out by Google once you pass their payout
threshold (€70 in most of Europe).

### Step 3 — (Optional) point traffic at it
The more visitors, the more income. Lowest-effort options:
- Submit the site to **Google Search Console** (`https://search.google.com/search-console`)
  and add the `sitemap.xml` — this is the single highest-impact thing you can do.
- Share individual tools where relevant (Reddit, forums, social).

---

## 📈 Honest expectations

I built and deployed all the engineering. What I **cannot** do is manufacture
traffic instantly — ad income scales with visitors, which builds over weeks as
Google indexes and ranks the pages.

- Display-ad RPM (revenue per 1,000 views) for this kind of utility/finance
  content is typically **€5–€20**.
- To clear **€150/month** you therefore need roughly **10,000–30,000 page views
  per month** (~350–1,000/day). Tool sites in evergreen niches realistically
  reach this within a few months of indexing, faster if you do Step 3.
- The finance tools (loan calculator) carry the highest ad value, so they're
  given prominence.

This is a genuine, durable asset — not a get-rich-quick switch. It keeps working
with no maintenance.

---

## 🛠️ What's in the box

```
index.html              Homepage / tool directory
tools/                  8 self-contained tools (each its own SEO page)
about.html              About page (AdSense requirement)
privacy.html            Privacy policy (AdSense requirement)
terms.html              Terms of use
404.html                Friendly not-found page
assets/css/style.css    Design system
assets/js/config.js     >>> THE ONE FILE YOU EDIT (your AdSense ID) <<<
assets/js/main.js        Shared nav/footer/ad injection + helpers
netlify.toml            Netlify config (zero-build static deploy + headers)
sitemap.xml, robots.txt SEO
ads.txt                 AdSense seller authorisation
```

Adding a new tool later: drop a new file in `tools/` and add one line to the
`TOOLS` array in `assets/js/main.js` — it appears on the homepage, nav and
footer automatically.

## 🔒 Privacy
Every tool runs 100% client-side. No user data is ever uploaded. This is both an
honest selling point and a reason the site is cheap and safe to run.
