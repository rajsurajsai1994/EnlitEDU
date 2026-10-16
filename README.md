# EnlitEDU website — Edupls-based redesign

A complete redesign of enlitedu.com built on the **Edupls** template framework, with the
structure and voice modelled on moderncampus.com (products by family, solutions by outcome,
customer stories, answer-first content) and EnlitEDU's own brand.

Open `index.html` directly in a browser, or serve the folder:

```bash
python -m http.server 8112
```

## Rebuild after editing content

All pages are generated from Python data files, so header, footer, schema and navigation
stay identical everywhere.

```bash
python _build/build.py
```

| File | What it holds |
|---|---|
| `_build/core.py` | Site settings (**GTM ID**, address, socials), navigation, header/footer, image map, schema helpers |
| `_build/data_modules.py` | Content for the 7 module pages |
| `_build/data_more.py` | 5 solution pages, 4 audience pages, 29 glossary terms, FAQ hub |
| `_build/pages.py`, `_build/pages2.py` | Page layouts (home, module, solution, audience, stories, about, demo…) |
| `_build/build.py` | Ports the 17 existing blog posts, builds blog, sitemap, robots.txt, llms.txt |
| `assets/css/enlitedu.css` | Design system (brand tokens, type, components, responsive) |
| `assets/js/enlitedu.js` | Mega menu, mobile drawer, tabs, tiles, FAQ, counters, video modal, forms |

The blog posts are read from the Eleventy source at
`C:\Users\SurajPaluri\Downloads\Enlitedu_Website\src\blog`. Update `SRC` in `_build/pages2.py`
if that folder moves.

## What's in it (54 pages)

- Home, Platform, How LioraAI works, Integrations
- 7 modules (same URLs as today): `articulate`, `assess`, `pla`, `veterans`, `athletics`, `degree-pathway`, `mobility`
- 5 solutions: `/solutions/…` (speed, transfer enrollment, military & adult learners, audit-ready, completion)
- 4 audiences: `/who-we-serve/…` (community colleges, universities, HBCUs & MSIs, state systems)
- Customer stories hub + Roane State and Nashville State story pages (with the YouTube interviews)
- Blog index + all 17 existing posts, Glossary (DefinedTermSet schema), FAQ hub
- About (with leadership), Contact, Request a Demo, Thank you, Security, Privacy, Terms, Accessibility, Careers, Events, 404
- `sitemap.xml`, `robots.txt`, `llms.txt`

Every page has a title, meta description, canonical, Open Graph, and JSON-LD
(Organization, BreadcrumbList, plus SoftwareApplication / FAQPage / Article / BlogPosting /
VideoObject / DefinedTermSet / HowTo where relevant). Visible FAQs match FAQPage markup exactly.

## From the template

Reused: Bootstrap 5 grid, Swiper, AOS, Font Awesome, and the template's design motifs
(pill eyebrows, floating notification cards, dotted orbit ring, avatar stack, play button,
carousels, back-to-top). The template's own `style.css` and placeholder images are **not**
used — almost all Edupls photos are grey placeholder boxes.

Note: the template ships an older Font Awesome font file, so a few newer icons don't render.
Icons used on the site were checked; if you add icons, stick to long-standing ones.

## Images

- EnlitEDU's own assets: logos, customer headshots, campus/graduate photos, SIS logos, badges.
- Stock photography from **Unsplash** (free for commercial use, no attribution required),
  currently loaded from `images.unsplash.com` with responsive sizes. Before launch, consider
  downloading and self-hosting them (IDs are in the `U` map in `_build/core.py`).
- Product UI is drawn in HTML/CSS (the old `dashboard-preview.png` is a placeholder).
  **Real LioraAI screenshots per module would be the single biggest upgrade.**

## Phase 1: Georgia / Atlanta local SEO

- Local pages: `georgia.html`, `georgia/atlanta-transcript-evaluation.html`, `georgia/freshman-transcript-evaluation.html`,
  `georgia/transfer-credit-evaluation.html`, `georgia/military-transcript-evaluation.html`, `transcript-evaluation-near-me.html`
  (content in `_build/data_georgia.py`, layout in `_build/pages3.py`).
- National articles (U.S. community college transfer data, state transfer policies, dual enrollment) live in `_build/data_us_posts.py`; every figure is sourced in the post. Long post headlines get a short `<title>` via `SEO_TITLE` in `build.py`.
- **Positioning rule:** EnlitEDU serves colleges across the U.S. The pages above (content in `_build/data_regional.py`) are national-first guides with ONE labelled Georgia section each; Georgia appears elsewhere only as
  the address, and one "Georgia (HQ state)" link in the nav/footer. National pages, the homepage title, top bar,
  module pages and blog index stay national. Georgia-only posts carry `region="Georgia"`: they sit in a labelled
  "State Guides: Georgia" block on blog.html and are never suggested as related posts on national articles.
  Check with `python _build/geo_scan.py`.
- Georgia articles: TCSG→USG under Core IMPACTS, HOPE GPA vs admissions GPA, buyer's checklist (also in `data_georgia.py`).
- Re-run checks after any edit:

```bash
python _build/build.py
python _build/audit.py         # titles, descriptions, H1s, headings, schema, FAQ parity, links, sitemap
python _build/keyword_map.py   # confirms each target keyword is on its target page
python _build/schema_audit.py  # every JSON-LD node: required/recommended props, @id refs, breadcrumbs, FAQ text, speakable, robots, llms.txt
python _build/geo_scan.py      # Georgia/Atlanta mentions on national pages (should be HQ + one regional link only)
python _build/prelaunch_check.py  # sitemap XML, robots, head tags, titles, duplicate H1s, images, http://, long dashes, leftovers
```

- Off-site (required for "near me" / map results): Google Business Profile at the Cumming address,
  a business phone number, Bing Places, Search Console + Bing Webmaster Tools sitemap submission.

## Verify before publishing

1. **Claims** carried over from the current site: Roane State 90% / 3 weeks → 2 days / 18-day
   Banner go-live; Nashville State +24% transfer yield / 3 pathways; 1M+ course descriptions;
   <60s per transcript; 130+ countries. Confirm each with the source.
2. **Customer stories**: the Roane State and Nashville State write-ups contain only facts from the
   current site and videos. Have each college review its page before it goes live.
3. **Logo strip** ("Trusted by enrollment teams across the U.S."): same six institutions as the
   current homepage. Confirm permission for each logo.
4. **Security wording**: the site says "SOC 2 program (report under NDA)", matching the current
   Security page; the old module FAQs said "SOC 2 Type II certified". Confirm the accurate status.
5. **Legal**: Privacy and Terms are ported unchanged from the current site and still need counsel review.
6. **Analytics**: set `"gtm"` in `_build/core.py` and rebuild.
7. **Forms** post to Web3Forms with the existing access key and redirect to `thank-you.html`.
8. **Tagline** "Recognize Every Credit. Advance Every Learner." is the recommended option from the
   redesign plan, pending CEO sign-off.

## Module names and hidden modules (Oct 2026)

- **LioraAI Transfer Credit Intelligence** (`transfer-credit-intelligence.html`, was "LioraAI Articulate") and
  **LioraAI Freshman Intelligence** (`freshman-intelligence.html`, was "LioraAI Assess"). The old `articulate.html` and
  `assess.html` are noindex pages that forward to the new addresses. Old names in the ported blog posts are rewritten at
  build time (`_rename()` in `build.py`).
- **NCAA / Athlete Transcripts is hidden until launch.** `athletics.html` is still built but is `noindex`, left out of the
  sitemap, llms.txt, menus, footer and all module grids, and nothing links to it. To launch it, remove `"athletics"` from
  `HIDDEN` in `_build/data_modules.py`, rebuild, and restore any NCAA copy you want back (platform FAQ, universities page).

## House style and proof points (Oct 2026)

- **No long dashes.** `tidy_dashes()` in `core.py` runs on every generated page and on llms.txt: en dashes become
  hyphens; em dashes become a comma where they join a clause, otherwise a spaced hyphen.
- **Nashville State** facts come only from the "Case Study 01" PDF (LioraAI platform data as of Sept 9, 2026):
  Transfer Credit Intelligence, 15 min to ~2 min per transcript (-87%), approval 18 to 8 hrs (-56%), 2,158+ transcripts,
  834+ sent to Banner, 89% match confidence (498/558), 18 faculty reviewers, live July 2026. The old "+24% transfer
  yield with Mobility Intelligence" claim was removed everywhere because the case study does not support it.
- **E-E-A-T:** blog posts show "Reviewed by Chaitanya Saripalli, Founder & CEO" with LinkedIn; BlogPosting has
  `editor` -> Person `#chaitanya-saripalli` (sameAs LinkedIn); Organization has `founder`.

## Deploying: redirects, error pages, headers (generated by `_build/deploy.py` on every build)

One redirect map (old site URLs, short links, renamed modules, folder URLs, legacy WordPress paths, old `/images/...`
files, `/favicon.ico`) is written out for every host, so they never drift apart:

| Host | Files it uses | One-time settings |
|---|---|---|
| **Vercel** (GitHub `rajsurajsai1994/EnlitEDU`) | `vercel.json`, `.vercelignore` (keeps `_build/` and README off the site) | Domains: add `www.enlitedu.com` as primary and redirect `enlitedu.com` to it. Vercel serves `404.html` with a real 404 automatically. `*.vercel.app` preview URLs send `X-Robots-Tag: noindex`. |
| **AWS S3 + CloudFront** (current live site) | `cloudfront-function-redirects.js` | Create a CloudFront Function from the file (runtime 2.0) on *viewer request*. Error pages: **403 -> /404.html (code 404)** and **404 -> /404.html (code 404)**. S3 returns 403 for missing files, and the live site does this today. Add a response-headers policy (HSTS, nosniff, SAMEORIGIN, Referrer-Policy). Do not upload `_build/`. |
| Netlify / Cloudflare Pages | `_redirects`, `_headers` | none |
| Apache | `.htaccess` | none |

- `google6a18e45d8fd24580.html` (Search Console verification, copied from the old site) and `manifest.json` stay in the root.
- `/index.html` is deliberately **not** redirected to `/`, because internal links use `index.html` so the site also works
  from disk. The canonical tag points to `/`.
- Check links any time: `python _build/link_check.py` (internal) or `python _build/link_check.py --external` (live).
