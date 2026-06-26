/* QuickTools — shared site behaviour: nav, footer, ads, helpers */
(function () {
  var cfg = window.SITE_CONFIG || {};
  var depth = (document.body.getAttribute("data-depth") === "tool") ? "../" : "";

  var TOOLS = [
    { slug: "word-counter",        icon: "📝", name: "Word Counter",          desc: "Count words, characters, sentences & reading time." },
    { slug: "password-generator",  icon: "🔐", name: "Password Generator",    desc: "Create strong, random, secure passwords instantly." },
    { slug: "loan-calculator",     icon: "🏦", name: "Loan Calculator",       desc: "Monthly payment, total interest & full schedule." },
    { slug: "percentage-calculator", icon: "％", name: "Percentage Calculator", desc: "Solve every common percentage problem fast." },
    { slug: "qr-code-generator",   icon: "🔳", name: "QR Code Generator",     desc: "Turn any link or text into a downloadable QR code." },
    { slug: "case-converter",      icon: "🔤", name: "Case Converter",        desc: "UPPER, lower, Title, sentence & more, instantly." },
    { slug: "color-converter",     icon: "🎨", name: "Color Converter",       desc: "Convert HEX ⇄ RGB ⇄ HSL with a live preview." },
    { slug: "unit-converter",      icon: "📐", name: "Unit Converter",        desc: "Length, weight, temperature & data units." },
    { slug: "bmi-calculator",      icon: "⚖️", name: "BMI Calculator",        desc: "Find your Body Mass Index & weight category." },
    { slug: "age-calculator",      icon: "🎂", name: "Age Calculator",        desc: "Your exact age in years, months & days." },
    { slug: "tip-calculator",      icon: "🧾", name: "Tip Calculator",        desc: "Calculate tips and split the bill fairly." },
    { slug: "discount-calculator", icon: "🏷️", name: "Discount Calculator",   desc: "Sale price and how much you really save." },
    { slug: "compound-interest-calculator", icon: "📈", name: "Compound Interest", desc: "See how savings & investments grow." },
    { slug: "base64-encoder",      icon: "🔠", name: "Base64 Encode/Decode",  desc: "Encode & decode Base64 with Unicode support." },
    { slug: "vat-calculator",      icon: "🧮", name: "VAT Calculator",        desc: "Add or remove VAT / sales tax at any rate." },
    { slug: "json-formatter",      icon: "{ }", name: "JSON Formatter",        desc: "Beautify, validate & minify JSON privately." },
    { slug: "random-number-generator", icon: "🎲", name: "Random Number",      desc: "Pick random numbers, with or without duplicates." },
    { slug: "lorem-ipsum-generator", icon: "✒️", name: "Lorem Ipsum",          desc: "Placeholder text by paragraph, sentence or word." }
  ];
  window.QT_TOOLS = TOOLS;

  /* ---------- NAV ---------- */
  function buildNav() {
    var el = document.getElementById("site-header");
    if (!el) return;
    el.className = "site-header";
    el.innerHTML =
      '<div class="container"><nav class="nav">' +
        '<a class="brand" href="' + depth + 'index.html"><span class="logo">⚡</span>' + (cfg.SITE_NAME || "QuickTools") + '</a>' +
        '<div class="nav-links">' +
          '<a href="' + depth + 'index.html">All Tools</a>' +
          '<a href="' + depth + 'tools/loan-calculator.html">Loan Calc</a>' +
          '<a href="' + depth + 'tools/password-generator.html">Passwords</a>' +
          '<a href="' + depth + 'tools/word-counter.html">Word Counter</a>' +
          '<a href="' + depth + 'guides/index.html">Guides</a>' +
          '<a href="' + depth + 'about.html">About</a>' +
          (cfg.SUPPORT_URL ? '<a href="' + cfg.SUPPORT_URL + '" target="_blank" rel="noopener" style="color:#fff;background:linear-gradient(135deg,var(--brand),var(--brand-2))">' + (cfg.SUPPORT_LABEL || '❤ Support') + '</a>' : '') +
        '</div>' +
      '</nav></div>';
  }

  /* ---------- FOOTER ---------- */
  function buildFooter() {
    var el = document.getElementById("site-footer");
    if (!el) return;
    var year = new Date().getFullYear();
    var toolLinks = TOOLS.map(function (t) {
      return '<a href="' + depth + 'tools/' + t.slug + '.html">' + t.name + '</a>';
    }).join("");
    var affiliate = (cfg.AFFILIATE_URL && cfg.AFFILIATE_LABEL)
      ? '<a href="' + cfg.AFFILIATE_URL + '" rel="sponsored nofollow" target="_blank">' + cfg.AFFILIATE_LABEL + '</a>' : "";
    el.className = "site-footer";
    el.innerHTML =
      '<div class="container"><div class="footer-grid">' +
        '<div style="max-width:280px"><h4>' + (cfg.SITE_NAME || "QuickTools") + '</h4>' +
          '<p style="color:var(--muted);font-size:.9rem">' + (cfg.SITE_TAGLINE || "Free online tools") +
          '. 100% in your browser — your data never leaves your device.</p>' + affiliate + '</div>' +
        '<div><h4>Popular Tools</h4><div class="footer-links">' + toolLinks + '</div></div>' +
        '<div><h4>Site</h4><div class="footer-links">' +
          '<a href="' + depth + 'index.html">Home</a>' +
          '<a href="' + depth + 'about.html">About</a>' +
          '<a href="' + depth + 'privacy.html">Privacy Policy</a>' +
          '<a href="' + depth + 'terms.html">Terms</a>' +
        '</div></div>' +
      '</div><div class="copyright">© ' + year + ' ' + (cfg.SITE_NAME || "QuickTools") +
      '. Made for people who just want the job done.</div></div>';
  }

  /* ---------- ADS ---------- */
  function loadAdSense() {
    var pub = cfg.ADSENSE_PUBLISHER_ID;
    if (!pub) return; // no ID yet -> placeholders stay, layout intact
    // Auto Ads: a single tag lets Google place ads automatically.
    var s = document.createElement("script");
    s.async = true;
    s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + pub;
    document.head.appendChild(s);
    if (cfg.USE_AUTO_ADS !== false) {
      var en = document.createElement("script");
      en.innerHTML = '(adsbygoogle = window.adsbygoogle || []).push({google_ad_client:"' +
        pub + '", enable_page_level_ads:true});';
      document.head.appendChild(en);
    }
    // Fill manual in-content slots if any exist.
    document.querySelectorAll(".ad-slot[data-ad]").forEach(function (slot) {
      slot.style.border = "none";
      slot.innerHTML =
        '<ins class="adsbygoogle" style="display:block;width:100%" data-ad-client="' + pub +
        '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }

  /* ---------- HELPERS shared by tools ---------- */
  window.QT = {
    copy: function (text) {
      navigator.clipboard && navigator.clipboard.writeText(text);
      QT.toast("Copied!");
    },
    toast: function (msg) {
      var t = document.getElementById("qt-toast");
      if (!t) { t = document.createElement("div"); t.id = "qt-toast"; t.className = "toast"; document.body.appendChild(t); }
      t.textContent = msg; t.classList.add("show");
      clearTimeout(t._tm); t._tm = setTimeout(function () { t.classList.remove("show"); }, 1400);
    },
    download: function (filename, dataUrl) {
      var a = document.createElement("a"); a.href = dataUrl; a.download = filename;
      document.body.appendChild(a); a.click(); a.remove();
    }
  };

  /* ---- SEO: FAQ rich-snippet structured data ----
     Auto-builds FAQPage JSON-LD from the visible FAQ on each page so the
     pages are eligible for Google's expandable FAQ rich results, which
     lift click-through rate (and therefore traffic + revenue). */
  function injectFaqSchema() {
    var dets = document.querySelectorAll(".faq details");
    if (!dets.length) return;
    var items = [];
    dets.forEach(function (d) {
      var q = d.querySelector("summary"), a = d.querySelector("p");
      if (q && a) {
        items.push({ "@type": "Question", "name": q.textContent.trim(),
          "acceptedAnswer": { "@type": "Answer", "text": a.textContent.trim() } });
      }
    });
    if (!items.length) return;
    var s = document.createElement("script");
    s.type = "application/ld+json";
    s.textContent = JSON.stringify({ "@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items });
    document.head.appendChild(s);
  }

  /* ---- PWA: manifest + theme colour for installability / repeat visits ---- */
  function injectPwaMeta() {
    if (!document.querySelector('link[rel="manifest"]')) {
      var l = document.createElement("link");
      l.rel = "manifest"; l.href = depth + "site.webmanifest";
      document.head.appendChild(l);
    }
    if (!document.querySelector('meta[name="theme-color"]')) {
      var m = document.createElement("meta");
      m.name = "theme-color"; m.content = "#0f1220";
      document.head.appendChild(m);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    buildNav(); buildFooter(); loadAdSense(); injectFaqSchema(); injectPwaMeta();
    // render tool grid on home if present
    var grid = document.getElementById("tool-grid");
    if (grid) {
      grid.innerHTML = TOOLS.map(function (t) {
        return '<a class="tool-card" href="tools/' + t.slug + '.html">' +
          '<div class="icon">' + t.icon + '</div>' +
          '<h3>' + t.name + '</h3><p>' + t.desc + '</p></a>';
      }).join("");
    }
  });
})();
