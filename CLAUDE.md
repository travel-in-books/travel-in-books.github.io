# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

Persian-language book review blog — **سفر در کتاب‌ها** (Travel in Books) — built with Jekyll and the Chirpy theme. Posts are written primarily in Persian (RTL) with some English elements (filenames, original book titles).

## Commands

```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Build for production
JEKYLL_ENV=production bundle exec jekyll b

# Run HTML proofer (same as CI)
bundle exec htmlproofer _site --disable-external --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"
```

## Post Format

**Filename:** `_posts/YYYY-MM-DD-Title-by-Author.md`

**Frontmatter:**
```yaml
---
title: <Persian title> از <Persian author name>
categories: [ادبیات داستانی, <genre>]
tags: [<country>, <rating stars>, <Persian year>]
toc: true
---
```

**Rating tag format:** `⭐⭐⭐⭐⭐☆☆☆☆☆ 5/10` (10 stars total, filled/unfilled)

**Post body starts with a Markdown table:**
```markdown
| نام اثر | <title> |
| نویسنده | <author> |
| نام اصلی اثر | <original title and author in English> |
| سال چاپ | <Persian/Arabic numeral year> |
| کشور | <country in Persian> |
| ژانر | <genre in Persian> |
| امتیاز | <same rating as tag> |
```

**New post helper:** `python3 create_file.py` — interactive script that generates a post skeleton.

## Architecture

- **Theme:** `jekyll-theme-chirpy` (~7.0) — layouts, includes, and JS are all inherited from the gem; this repo does not contain `_layouts/` or `_includes/` directories.
- **Deployment:** GitHub Actions (`.github/workflows/pages-deploy.yml`) builds on push to `main` and deploys to GitHub Pages.
- **Plugin:** `_plugins/posts-lastmod-hook.rb` — hooks into Jekyll build to track post last-modified dates.
- **Python utilities** (in repo root): `create_file.py` (scaffold new post), `tools.py` (bulk find-replace in markdown), `extract_data.py` (parse post data), `generate_headers.py` (frontmatter generation), `convert_faslha.py` (Persian text conversion), `iterate_and_check.py` (post validation).
- **Localization:** Site language is `fa` (Persian); locale strings live in `_data/locales/`.
- **Analytics:** GoatCounter (id: `travel-in-books`), configured in `_config.yml`.
