---
layout: page
title: خط زمانی
icon: fas fa-stream
order: 6
---

<style>
  .tl-wrap {
    position: relative;
    padding-right: 1.6rem;
    border-right: 3px solid var(--border-color, #dee2e6);
    direction: rtl;
  }
  .tl-group {
    margin-bottom: 2.5rem;
  }
  .tl-decade-marker {
    position: relative;
    margin-bottom: 0.8rem;
  }
  .tl-decade-marker::before {
    content: '';
    position: absolute;
    right: -2.05rem;
    top: 0.35rem;
    width: 13px;
    height: 13px;
    border-radius: 50%;
    background: #d64534;
    border: 2px solid var(--body-bg, #fff);
    box-shadow: 0 0 0 2px #d64534;
  }
  .tl-decade-label {
    font-size: 1rem;
    font-weight: 700;
    color: #d64534;
    margin: 0;
    letter-spacing: 0.02em;
  }
  .tl-book {
    display: flex;
    align-items: baseline;
    gap: 0.65rem;
    padding: 0.22rem 0;
    font-size: 0.9rem;
  }
  .tl-year {
    color: #888;
    white-space: nowrap;
    font-size: 0.8rem;
    min-width: 3rem;
    flex-shrink: 0;
  }
  .tl-title a {
    color: inherit;
    text-decoration: none;
  }
  .tl-title a:hover {
    color: #d64534;
    text-decoration: underline;
  }
  .tl-country {
    font-size: 0.75rem;
    color: #aaa;
    white-space: nowrap;
  }
  .tl-summary {
    font-size: 0.85rem;
    color: #888;
    margin-bottom: 1.5rem;
    direction: rtl;
  }
</style>

<p class="tl-summary" id="tl-summary"></p>
<div class="tl-wrap" id="tl-wrap"></div>

<script>
const books = [
  {% for post in site.posts %}
    {% unless post.path contains "template" %}
      {% assign after_rating = "" %}
      {% assign year_tag = "" %}
      {% for tag in post.tags %}
        {% if after_rating == "yes" and year_tag == "" %}
          {% assign year_tag = tag | strip %}
        {% endif %}
        {% if tag contains "⭐" or tag contains "☆" %}
          {% assign after_rating = "yes" %}
        {% endif %}
      {% endfor %}
      {% if year_tag != "" and year_tag != "۰۰۰۰" %}
        {% assign yr = year_tag | replace:"۰","0" | replace:"۱","1" | replace:"۲","2" | replace:"۳","3" | replace:"۴","4" | replace:"۵","5" | replace:"۶","6" | replace:"۷","7" | replace:"۸","8" | replace:"۹","9" | plus: 0 %}
        {% if yr > 0 %}
  { title: {{ post.title | jsonify }}, url: {{ post.url | jsonify }}, year: {{ yr }}, yearFa: {{ year_tag | jsonify }}, country: {{ post.tags | first | strip | jsonify }} },
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endfor %}
];

function toPersian(n) {
  return String(n).replace(/[0-9]/g, d => '۰۱۲۳۴۵۶۷۸۹'[+d]);
}

// Sort ascending by year
books.sort((a, b) => a.year - b.year);

// Group by decade
const groups = new Map();
for (const b of books) {
  const d = Math.floor(b.year / 10) * 10;
  if (!groups.has(d)) groups.set(d, []);
  groups.get(d).push(b);
}

// Summary line
document.getElementById('tl-summary').textContent =
  `${toPersian(books.length)} کتاب از ${toPersian(books[0].year)} تا ${toPersian(books[books.length-1].year)}`;

// Render
const wrap = document.getElementById('tl-wrap');

for (const [decade, items] of groups) {
  const group = document.createElement('div');
  group.className = 'tl-group';

  const marker = document.createElement('div');
  marker.className = 'tl-decade-marker';

  const label = document.createElement('p');
  label.className = 'tl-decade-label';
  label.textContent = `دهه ${toPersian(decade)}`;
  marker.appendChild(label);
  group.appendChild(marker);

  for (const b of items) {
    const row = document.createElement('div');
    row.className = 'tl-book';

    const year = document.createElement('span');
    year.className = 'tl-year';
    year.textContent = b.yearFa;

    const title = document.createElement('span');
    title.className = 'tl-title';
    const link = document.createElement('a');
    link.href = b.url;
    link.textContent = b.title;
    title.appendChild(link);

    const country = document.createElement('span');
    country.className = 'tl-country';
    country.textContent = b.country;

    row.appendChild(year);
    row.appendChild(title);
    row.appendChild(country);
    group.appendChild(row);
  }

  wrap.appendChild(group);
}
</script>
