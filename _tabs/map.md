---
layout: page
title: نقشه جهانی
icon: fas fa-globe
order: 5
---

<link rel="stylesheet" href="/assets/leaflet/leaflet.css"/>
<script src="/assets/leaflet/leaflet.min.js"></script>

<style>
  #book-map {
    height: 520px;
    width: 100%;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    z-index: 0;
  }
  .map-legend {
    background: var(--card-bg, #fff);
    border: 1px solid var(--border-color, #ddd);
    border-radius: 8px;
    padding: 0.8rem 1rem;
    font-size: 0.85rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem 1.2rem;
    align-items: center;
    direction: rtl;
  }
  .legend-item {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  .legend-circle {
    border-radius: 50%;
    background: rgba(214, 69, 52, 0.65);
    border: 1.5px solid #c0392b;
    flex-shrink: 0;
  }
  .leaflet-popup-content b { font-size: 1rem; }
  .leaflet-popup-content ul {
    margin: 0.4rem 0 0;
    padding-right: 1.1rem;
    padding-left: 0;
    list-style: disc;
    max-height: 200px;
    overflow-y: auto;
  }
  .leaflet-popup-content ul li { margin: 2px 0; }
  .leaflet-popup-content a { color: #c0392b; }
</style>

<div id="book-map"></div>

<div class="map-legend">
  <span style="font-weight:600;">تعداد کتاب‌ها:</span>
  <span class="legend-item"><span class="legend-circle" style="width:10px;height:10px;"></span> ۱–۲</span>
  <span class="legend-item"><span class="legend-circle" style="width:16px;height:16px;"></span> ۳–۶</span>
  <span class="legend-item"><span class="legend-circle" style="width:24px;height:24px;"></span> ۷–۱۵</span>
  <span class="legend-item"><span class="legend-circle" style="width:34px;height:34px;"></span> ۱۶+</span>
</div>

<script>
/* Coordinates come from _data/countries.yml — the single source of truth. */
const coords = {
  {% for c in site.data.countries %}
  {{ c[0] | jsonify }}: [{{ c[1][0] }}, {{ c[1][1] }}],
  {% endfor %}
};

/* The country list is derived from the posts themselves (a post's first tag
   is its country), so a book from a new country appears on the map as soon
   as its coordinates are added to _data/countries.yml. */
{% assign names_str = "" %}
{% for post in site.posts %}
  {% unless post.path contains "template" %}
    {% assign names_str = names_str | append: post.tags.first | append: "|" %}
  {% endunless %}
{% endfor %}
{% assign country_list = names_str | split: "|" | uniq | sort %}

const countryData = [
  {% for country in country_list %}
    {% assign posts_in_country = site.tags[country] %}
    {% assign count = posts_in_country | size %}
    {% if count > 0 %}
  {
    name: {{ country | jsonify }},
    count: {{ count }},
    books: [{% for post in posts_in_country %}{ title: {{ post.title | jsonify }}, url: {{ post.url | jsonify }} }{% unless forloop.last %},{% endunless %}{% endfor %}]
  },
    {% endif %}
  {% endfor %}
];

const map = L.map('book-map', { zoomControl: true }).setView([25, 15], 2);

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/">CARTO</a>',
  subdomains: 'abcd',
  maxZoom: 19
}).addTo(map);

/* A country tagged on a post but absent from _data/countries.yml would be
   dropped silently, so surface it instead of losing the books. */
const missing = countryData.filter(d => !coords[d.name]);
if (missing.length) {
  console.warn(
    'نقشه: این کشورها در _data/countries.yml مختصات ندارند و روی نقشه نیستند: ' +
    missing.map(d => `${d.name} (${d.count})`).join('، ')
  );
}

countryData.forEach(d => {
  const latlng = coords[d.name];
  if (!latlng) return;

  const radius = 5 + Math.sqrt(d.count) * 5;

  const bookListHTML = d.books
    .map(b => `<li><a href="${b.url}" target="_blank">${b.title}</a></li>`)
    .join('');

  const popup = `<b>${d.name}</b> — ${d.count} کتاب<ul>${bookListHTML}</ul>`;

  L.circleMarker(latlng, {
    radius: radius,
    fillColor: '#d64534',
    color: '#9b1c0e',
    weight: 1.5,
    fillOpacity: 0.65,
  })
  .addTo(map)
  .bindPopup(popup, { maxWidth: 280, maxHeight: 320 });
});
</script>
