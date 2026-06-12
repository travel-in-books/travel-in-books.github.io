# Technical SEO & Growth Notes

Reference notes for improving discoverability and traffic for **سفر در کتاب‌ها**
(travel-in-books.github.io). Not built into the site (the `docs/` folder is in
`exclude:` in `_config.yml`).

_Last reviewed: 2026-06-12. Site: Jekyll + Chirpy 7.5.0, Persian/RTL, GitHub Pages._

---

## 🔴 Priority 1 — Fix the broken sitemap (highest impact)

A stale, hand-committed `sitemap.xml` in the repo root **shadows** the
`jekyll-sitemap` plugin (the plugin skips generation when a `sitemap.xml`
already exists).

- Committed/static sitemap: **75 URLs** (what search engines currently see)
- Plugin-generated sitemap: **494 URLs** (all posts + category/tag/author pages)

So search engines have been told about only ~15% of the site, and the file does
not update as new posts are added.

**Fix:** delete the static `sitemap.xml` from the repo root and let the plugin
generate it on every build. Verified: removing it yields the full 494-URL
sitemap.

```bash
git rm sitemap.xml
# rebuild; _site/sitemap.xml should now contain ~490+ <url> entries
```

---

## 🔴 Priority 2 — Fill in placeholder social / SEO config

`_config.yml` still has the Chirpy template defaults:

```yaml
twitter:
  username: twitter_username      # placeholder
social:
  - https://twitter.com/username  # placeholder — post bylines link here (broken)
github:                            # empty
```

Every post's author byline currently links to the broken `twitter.com/username`.

**Fix:** set real handles, or remove these keys. `jekyll-seo-tag` uses them for
`og:`/`twitter:` meta and the byline link.

---

## ⚠️ Priority 3 — Submit to search engines (single biggest growth lever)

The site has **no `google_site_verification`** set, which usually means it is
not registered in Google Search Console. A new site is essentially invisible
until this is done.

Steps:
1. Add the site to **Google Search Console** (https://search.google.com/search-console).
   - Verify via the HTML-tag method; Chirpy supports it:
     ```yaml
     # _config.yml
     webmaster_verifications:
       google: <verification-code>
     ```
     (Older Chirpy used a top-level `google_site_verification:` key — check the
     version's `_config.yml` comments.)
   - Submit the sitemap: `https://travel-in-books.github.io/sitemap.xml`
2. Repeat with **Bing Webmaster Tools** (https://www.bing.com/webmasters) — it
   also feeds Yahoo and DuckDuckGo, and can import directly from Search Console.
3. After fixing the sitemap, use "Request indexing" for a few key posts to seed
   crawling.

---

## ✅ Already healthy

- `robots.txt` present and points to the sitemap.
- `jekyll-seo-tag` active: `og:title/description/url/image`, canonical links OK.
- Per-post Open Graph cover images now set (good social-share previews).
- Atom feed generated (`/feed.xml`).
- RTL pagination arrows fixed.

---

## Beyond technical SEO — distribution for a Persian book blog

Indexing gets the site *found*; these get it *read*:

1. **Cross-post to ویرگول (Virgool)** with a canonical link back — ranks well in
   Persian search and has a built-in book audience; drives referral traffic
   without duplicate-content issues.
2. **Share where Persian readers are:** Telegram کتاب‌خوانی channels/groups,
   Instagram bookstagram accounts, X/Threads Persian book community. The new
   cover images make these shares look good — cover + 2-line hook + link.
3. **Goodreads / طاقچه reviews** with a link back; those pages rank and refer.
4. **Enable comments (giscus)** — Chirpy supports it via GitHub Discussions;
   adds engagement signals and return visits. Currently no commenting.
5. **Match Persian search intent** — people search «نقد کتاب X»، «خلاصه X»،
   «معرفی X». Descriptions already say «نقد و بررسی»; get those terms into
   titles/headings too.
6. **Custom domain (optional)** — e.g. `travelinbooks.ir`/`.com` reads as more
   trustworthy than `github.io`; easy to point at GitHub Pages.

---

## Quick checklist

- [ ] `git rm sitemap.xml` (let the plugin generate the full one)
- [ ] Fill/replace `twitter`, `social`, `github` in `_config.yml`
- [ ] Google Search Console: verify + submit sitemap
- [ ] Bing Webmaster Tools: verify + submit sitemap
- [ ] Enable giscus comments
- [ ] Set up a Virgool cross-posting routine
- [ ] (Optional) custom domain
