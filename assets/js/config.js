/* ===================================================================
   SITE CONFIG  —  THE ONLY FILE YOU EDIT TO TURN ON INCOME
   ===================================================================
   You have THREE ways to earn, listed fastest-to-slowest to set up.
   Fill in ANY ONE of them (or several) and that revenue surface goes
   live the moment Netlify redeploys. Until then the site looks clean
   and complete — no broken layout, no empty boxes.

   ── OPTION A · "Support" button — FASTEST, no approval, works today ──
   Create a free Ko-fi (https://ko-fi.com) or Buy Me a Coffee
   (https://buymeacoffee.com) page in ~2 minutes. Paste its URL into
   SUPPORT_URL below. A tasteful "Support this site" button appears on
   every page. This needs NO approval and can take money immediately.

   ── OPTION B · Affiliate link — fast, no approval beyond the program ─
   If you have (or sign up for) an affiliate link — Amazon Associates,
   NordVPN, Bluehost, etc. — paste it into AFFILIATE_URL. It shows in
   the footer. You earn a commission on referred sales.

   ── OPTION C · Display ads (AdSense) — most passive, slowest to start ─
   Sign up at https://adsense.google.com (free, needs site review +
   traffic). Once approved you get a "ca-pub-..." ID — paste it into
   ADSENSE_PUBLISHER_ID and ads auto-place across the whole site.
   =================================================================== */

window.SITE_CONFIG = {

  /* ---- OPTION A: instant "Support / tip" button (recommended first) ---- */
  // Paste your Ko-fi / Buy Me a Coffee / Gumroad / PayPal.me URL here.
  SUPPORT_URL: "",
  SUPPORT_LABEL: "❤ Support this site",

  /* ---- OPTION B: affiliate / sponsor link (shown in footer) ---- */
  AFFILIATE_URL: "",
  AFFILIATE_LABEL: "",

  /* ---- OPTION C: Google AdSense display ads ---- */
  // <<< PASTE YOUR ADSENSE PUBLISHER ID HERE (keep the "ca-pub-" prefix)
  ADSENSE_PUBLISHER_ID: "",
  USE_AUTO_ADS: true, // let Google auto-place ads (lowest effort)

  /* ---- Site identity ---- */
  SITE_NAME: "QuickTools",
  SITE_TAGLINE: "Free, fast, private online tools",
  // Set to your real Netlify domain once you have it.
  SITE_URL: "https://quicktools.netlify.app"
};
