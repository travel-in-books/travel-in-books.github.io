---
layout: page
title: نویسندگان
icon: fas fa-feather
order: 4
---

<style>
  .au-summary {
    font-size: 0.85rem;
    color: #888;
    margin-bottom: 1.5rem;
    direction: rtl;
  }

  .au-list {
    direction: rtl;
  }

  .au-group {
    margin-bottom: 2rem;
  }

  .au-name {
    font-size: 1rem;
    font-weight: 700;
    color: var(--heading-color, inherit);
    margin: 0 0 0.4rem;
    display: flex;
    align-items: center;
    gap: 0.55rem;
    direction: rtl;
  }

  .au-count {
    font-size: 0.7rem;
    font-weight: 600;
    background: #d64534;
    color: #fff;
    border-radius: 9px;
    padding: 0.1rem 0.45rem;
    line-height: 1.6;
    flex-shrink: 0;
  }

  .au-books {
    padding-right: 0.8rem;
    border-right: 3px solid var(--border-color, #dee2e6);
    margin-right: 0.15rem;
  }

  .au-book {
    display: flex;
    align-items: baseline;
    gap: 0.55rem;
    padding: 0.2rem 0;
    direction: rtl;
  }

  .au-year {
    font-size: 0.75rem;
    color: #aaa;
    white-space: nowrap;
    flex-shrink: 0;
  }

  .au-title a {
    font-size: 0.9rem;
    color: inherit;
    text-decoration: none;
  }
  .au-title a:hover {
    color: #d64534;
    text-decoration: underline;
  }

  .au-divider {
    border: none;
    border-top: 1px solid var(--border-color, #dee2e6);
    margin: 0 0 2rem;
  }

  /* Letter index bar */
  .au-index {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-bottom: 1.5rem;
    direction: rtl;
  }
  .au-index-letter {
    font-size: 0.8rem;
    color: #d64534;
    cursor: pointer;
    padding: 0.1rem 0.3rem;
    border-radius: 4px;
    border: 1px solid transparent;
    text-decoration: none;
  }
  .au-index-letter:hover {
    border-color: #d64534;
  }
</style>

<p class="au-summary" id="au-summary"></p>
<div class="au-list" id="au-list"></div>

<script>
const posts = [
  {% for post in site.posts %}
    {% unless post.path contains "template" %}
      {% assign after_rating = "" %}
      {% assign after_year = "" %}
      {% assign year_tag = "" %}
      {% assign author_tag = "" %}
      {% for tag in post.tags %}
        {% if after_year == "yes" and author_tag == "" %}
          {% assign author_tag = tag | strip %}
        {% endif %}
        {% if after_rating == "yes" and year_tag == "" %}
          {% assign year_tag = tag | strip %}
          {% assign after_year = "yes" %}
        {% endif %}
        {% if tag contains "⭐" or tag contains "☆" %}
          {% assign after_rating = "yes" %}
        {% endif %}
      {% endfor %}
      {% if author_tag != "" %}
  { title: {{ post.title | jsonify }}, url: {{ post.url | jsonify }}, author: {{ author_tag | jsonify }}, yearFa: {{ year_tag | jsonify }} },
      {% endif %}
    {% endunless %}
  {% endfor %}
];

/* Strip author name from title ("X از Y" → "X") */
function bookTitle(fullTitle, author) {
  const sep = ' از ';
  const idx = fullTitle.lastIndexOf(sep);
  if (idx !== -1) return fullTitle.slice(0, idx).trim();
  return fullTitle;
}

/* Group by author */
const byAuthor = new Map();
for (const p of posts) {
  if (!byAuthor.has(p.author)) byAuthor.set(p.author, []);
  byAuthor.get(p.author).push(p);
}

/* Sort authors using Persian locale */
const authors = [...byAuthor.keys()].sort((a, b) => a.localeCompare(b, 'fa'));

document.getElementById('au-summary').textContent =
  `${authors.length} نویسنده — ${posts.length} کتاب`;

const list = document.getElementById('au-list');

for (const author of authors) {
  const books = byAuthor.get(author);

  const group = document.createElement('div');
  group.className = 'au-group';
  group.id = 'au-' + author.replace(/\s+/g, '-');

  const heading = document.createElement('h3');
  heading.className = 'au-name';

  const nameSpan = document.createElement('span');
  nameSpan.textContent = author;

  const countBadge = document.createElement('span');
  countBadge.className = 'au-count';
  countBadge.textContent = books.length;

  heading.appendChild(nameSpan);
  heading.appendChild(countBadge);
  group.appendChild(heading);

  const bookList = document.createElement('div');
  bookList.className = 'au-books';

  for (const b of books) {
    const row = document.createElement('div');
    row.className = 'au-book';

    const year = document.createElement('span');
    year.className = 'au-year';
    year.textContent = b.yearFa || '';

    const title = document.createElement('span');
    title.className = 'au-title';
    const link = document.createElement('a');
    link.href = b.url;
    link.textContent = bookTitle(b.title, b.author);
    title.appendChild(link);

    row.appendChild(year);
    row.appendChild(title);
    bookList.appendChild(row);
  }

  group.appendChild(bookList);

  const hr = document.createElement('hr');
  hr.className = 'au-divider';
  group.appendChild(hr);

  list.appendChild(group);
}
</script>
